# DFlash 源码：`dflash/model.py` 由简入深详解

本文面向对 DFlash 完全陌生的读者，从「它是干什么的」讲起，逐层深入到每个函数、每个参数的作用，最后拆解关键算法的计算过程。文中所有行号均以 [z-lab/dflash](https://github.com/z-lab/dflash) `main` 分支提交 [`07ebd93`](https://github.com/z-lab/dflash/blob/07ebd93db9f472af339b644bb70221ad8428328a/dflash/model.py)（2026-08-18）中的 `dflash/model.py` 为准。论文与部署综述见 [DFlash](dflash.md)。

---

## 目录

1. [30 秒理解 DFlash](#1-30-秒理解-dflash)
2. [背景知识：投机解码与块扩散](#2-背景知识投机解码与块扩散)
3. [文件地图：每个组件在做什么](#3-文件地图每个组件在做什么)
4. [主线：`dflash_generate` 生成主循环](#4-主线dflash_generate-生成主循环)
5. [采样工具函数](#5-采样工具函数)
6. [草稿模型 `DFlashDraftModel`](#6-草稿模型-dflashdraftmodel)
7. [注意力层：`Qwen3DFlashAttention` 与 `Qwen3DFlashDecoderLayer`](#7-注意力层qwen3dflashattention-与-qwen3dflashdecoderlayer)
8. [DFlash 2 的三件新武器](#8-dflash-2-的三件新武器)
9. [配置项（`dflash_config`）速查表](#9-配置项dflash_config速查表)
10. [端到端走一遍的例子](#10-端到端走一遍的例子)

---

## 1. 30 秒理解 DFlash

大语言模型（下称**目标模型**，target）生成文本时是一个字一个字往外蹦的：每生成一个 token 都要把整个大模型跑一遍前向计算。模型越大，这一步越慢。

**投机解码（speculative decoding）** 的思路是：

1. 让一个小而快的**草稿模型（draft model）** 一口气「猜」出接下来的若干个 token；
2. 让目标模型**一次性并行验证**这几个 token 是否符合自己的分布；
3. 接受猜对的部分、拒绝猜错的部分。

只要草稿模型猜得够准，一次目标模型前向就能产出多个 token，速度成倍提升；而数学上可以证明：**接受/拒绝机制保证最终输出分布与直接用目标模型采样完全一致**——加速不牺牲质量。

**DFlash 的特别之处**在于草稿模型怎么「猜」。传统草稿模型仍然是自回归的（猜 k 个 token 也要串行跑 k 次）。DFlash 是一个**块扩散（block diffusion）**模型：它把要猜的一整块位置先填上特殊的 `[MASK]` 占位符，然后**一次并行前向**就把整块 token 全部预测出来。草稿成本从 O(k) 次前向降到约 1 次。

本文件实现了两代模型：

| 类 | 说明 |
|---|---|
| `DFlashDraftModel`（`model.py:550`） | 第一代：一个小型 Qwen3 结构 Transformer，读入目标模型中间层的特征，一次并行预测一整块 token |
| `DFlash2DraftModel`（`model.py:630`） | 第二代：在第一代基础上加了**动态因果卷积**（更强的局部序列建模）和 **`CandidateSelector`**（用二元语法打分挑选候选序列），草稿质量更高 |

驱动它们干活的是顶层函数 `dflash_generate`（`model.py:180`）：prefill → 循环（草稿 → 验证 → 接受/拒绝）→ 返回结果。

---

## 2. 背景知识：投机解码与块扩散

### 2.1 自回归解码为什么慢

生成第 *t* 个 token 时，模型的主要开销不是计算量，而是把几十 GB 的权重从显存读进计算单元（memory-bound）。所以「一次前向算 1 个 token」和「一次前向算 16 个 token」的耗时差距远小于 16 倍。验证 16 个草稿 token 的代价，大约只比生成 1 个 token 贵一点——这就是投机解码能加速的物理基础。

### 2.2 接受/拒绝（rejection sampling）

设目标模型在某位置的概率分布为 *p*，草稿模型的分布为 *q*，草稿采样出 token *x*：

- 以概率 `min(1, p(x)/q(x))` 接受 *x*；
- 拒绝时，从残差分布 `norm(max(0, p - q))` 重新采样。

可以证明这样得到的样本恰好服从 *p*。贪心解码（temperature = 0）是退化情形：直接比较草稿 token 与目标模型 argmax 是否相等，找到第一个不等的位置为止。

### 2.3 块扩散草稿

DFlash 草稿模型的一个生成块形如：

```text
[ 锚点 token, MASK, MASK, MASK, ... ]
```

- **锚点（anchor）**：上一轮已确认的最后一个 token，提供「从哪儿接着写」的信息；
- **MASK 位置**：待预测的位置。它们通过目标模型的特征（上下文条件）+ 位置编码 + 块内自注意力，**并行地**各自输出一个预测分布。

由于扩散式草稿模型在训练中见过「部分位置被掩码」的情形，它也能利用上一块已确认的 token 作为额外条件，这正是代码中 `noise_embedding` 的含义（见 §6.3）。

---

## 3. 文件地图：每个组件在做什么

```text
dflash/model.py
│
├─ 一、配置/小工具
│   ├─ build_target_layer_ids      决定从目标模型哪些层抽特征
│   ├─ extract_context_feature     把多层隐藏状态拼接成一个上下文特征
│   ├─ _draft_config/_draft_value  读取 config.dflash_config 里的超参
│   ├─ _raw_input_embeddings       取目标模型的词嵌入（可缩放）
│   ├─ _output_head                取目标模型的 lm_head（词表投影头）
│   ├─ _make_cache / _crop_to      KV cache 的创建与裁剪
│   ├─ _attention_mask             按 因果/滑窗 规则构造布尔掩码
│   └─ _cuda_time                  CUDA 同步计时（统计用）
│
├─ 二、采样
│   ├─ sample                      采样入口：温度 0=贪心，否则随机采样
│   ├─ _sampling_probs             温度缩放 + top-k + top-p → 概率分布
│   ├─ _sample_probs               按概率分布抽一个 token
│   ├─ _validate_sampling          参数合法性检查
│   └─ _rejection_sample           ★ 投机解码的核心：接受/拒绝
│
├─ 三、生成主循环
│   └─ dflash_generate             ★ prefill + 草稿 + 验证 + 接受，直到结束
│
├─ 四、草稿模型（第一代）
│   ├─ apply_rotary_pos_emb        RoPE 旋转位置编码
│   ├─ Qwen3DFlashAttention        ★ 交叉 + 自注意力混合层
│   ├─ Qwen3DFlashDecoderLayer     一层 = 注意力 + MLP（带残差）
│   └─ DFlashDraftModel            组装所有层；forward / compute_logits / spec_generate
│
└─ 五、草稿模型（第二代）
    ├─ _grouped_dynamic_convolve   ★ 分组动态因果卷积的实际计算
    ├─ GroupedDynamicCausalConv    上述卷积的模块封装（prepare/finish）
    ├─ CandidateSelector           ★ 用一元分数 + 二元语法分数挑选候选序列
    └─ DFlash2DraftModel           继承第一代，挂上卷积和选择器
```

★ 号为关键函数，下文重点拆解。

---

## 4. 主线：`dflash_generate` 生成主循环

签名（`model.py:180`）：

```python
@torch.inference_mode()
def dflash_generate(
    model: "DFlashDraftModel",   # 草稿模型（DFlash 或 DFlash2）
    target: nn.Module,           # 目标大模型
    input_ids: torch.LongTensor, # 提示词 token，形状 (1, seq_len)
    max_new_tokens: int,         # 最多生成多少新 token
    stop_token_ids: list[int] | None,  # 遇到这些 token 就停止
    temperature: float = 0.0,    # 0 = 贪心；>0 = 随机采样
    top_p: float = 1.0,          # 核采样阈值
    top_k: int = 0,              # top-k 采样，0 = 关闭
    block_size: int | None = None,     # 每块草稿多少个 token，默认取 model.block_size
    return_stats: bool = False,  # 是否返回耗时/接受率统计
)
```

整个函数分三个阶段。

### 4.1 初始化（`model.py:193-202`）

```python
output_ids = torch.full((1, max_length + 1), model.mask_token_id, ...)
position_ids = torch.arange(output_ids.shape[1]).unsqueeze(0)
past_key_values_target = _make_cache(target.config)
past_key_values_draft  = _make_cache(model.config)
```

- `output_ids`：预分配的输出缓冲区，先全部填成 `mask_token_id`，之后逐段写入真实 token。`+1` 是留一个位置的余量。
- 两个 **KV cache**：目标模型和草稿模型各一份，用于增量解码（只算新 token，不重复算旧 token）。`_make_cache` 里调用 `activate_past_recording()`，让 cache 在 `update` 时保留全部历史（而非只保留上一步），方便后面用 `_crop_to` 精确修剪。

### 4.2 Prefill：处理提示词，产出第一个 token（`model.py:204-221`）

```python
output = target(
    input_ids,
    position_ids=position_ids[:, :num_input_tokens],
    past_key_values=past_key_values_target,
    use_cache=True,
    logits_to_keep=1,                       # 只保留最后一个位置的 logits，省显存
    output_hidden_states=block_size > 1,    # 只有要做块草稿时才需要中间层特征
)
output_ids[:, :num_input_tokens] = input_ids
output_ids[:, num_input_tokens:num_input_tokens + 1] = sample(output.logits, ...)
if block_size > 1:
    target_hidden = extract_context_feature(output.hidden_states, model.target_layer_ids)
_crop_to(past_key_values_target, num_input_tokens)
```

要点：

1. 目标模型一次性读完整个提示词（这是它唯一「正常」跑的一次），顺手采样出**第 1 个生成 token**。
2. `extract_context_feature` 从目标模型的**中间层**抽取特征（而不是最后一层），拼成 `target_hidden`——这是草稿模型的「上下文条件」。为什么是中间层、抽哪些层，见 §6.2。
3. `_crop_to` 把目标模型的 KV cache 裁回提示词长度：`output.logits` 占用了一个额外位置，但它的 KV 不该留。

### 4.3 解码循环：草稿 → 验证 → 接受（`model.py:223-308`）

循环变量 `start` 指向「已确认的最后一个 token」的位置。每一轮迭代产出一个块：

**第 0 步：确定本轮块大小**

```python
verify_size = min(block_size, max_length - start)
block_output_ids = output_ids[:, start : start + verify_size].clone()
```

`block_output_ids[0]` 是锚点（上一轮确认的 token），`[1:]` 初始全是 MASK，等着被草稿填上。

**第 1 步：草稿模型并行预测整块**（仅当 `verify_size > 1`，`model.py:237-268`）

```python
noise_embedding = _raw_input_embeddings(target, block_output_ids, scale)
draft_hidden = model(
    target_hidden=target_hidden,
    noise_embedding=noise_embedding,
    position_ids=position_ids[:, start - target_hidden.shape[1] : start + verify_size],
    past_key_values=past_key_values_draft,
    use_cache=True,
)[:, 1 - verify_size :, :]          # 只保留对应 MASK 位置的输出
_crop_to(past_key_values_draft, start)
```

- `noise_embedding`：把 `block_output_ids`（锚点 + 一串 MASK）过**目标模型的词嵌入表**（乘一个缩放系数），作为草稿模型的输入。MASK 位置的嵌入就是训练时学好的「待预测」信号。
- 注意位置编码的范围从 `start - target_hidden.shape[1]` 开始（不要写成 `len(target_hidden)`：张量的 `len` 是 batch 维，这里要的是上下文长度）：**上下文特征的每个位置与它在目标序列中的真实位置对齐**，位置编号是全局连续的。
- 草稿模型前向后，`[:, 1-verify_size:, :]` 切掉前缀的上下文输出，只留 MASK 位置的隐藏状态。
- `_crop_to(draft_cache, start)`：**丢弃草稿模型刚写入的这一块的 KV**。草稿模型的自回归 KV 缓存只保留「历史块」的信息，当前块内部的依赖由交叉注意力（§7）处理。

然后分两种草稿模型出草稿：

- **DFlash2**（`model.py:251-258`）：调用 `model.propose(...)`，由 `CandidateSelector` 结合一元分数和二元语法分数**顺序**选出一条候选链，同时返回采样概率 `draft_probs` 与候选索引 `draft_indices`（供拒绝采样用）。
- **DFlash**（`model.py:260-268`）：`compute_logits` 直接得到每个位置的 logits；温度 > 0 就按分布采样每个位置，温度 = 0 就逐位置取 argmax。

**第 2 步：目标模型并行验证整块**（`model.py:269-275`）

```python
output = target(
    block_output_ids,               # 锚点 + 草稿填好的整块
    position_ids=block_position_ids,
    past_key_values=past_key_values_target,
    use_cache=True,
    output_hidden_states=verify_size > 1,
)
```

目标模型一次前向，同时给出块内**每个位置**的 logits——位置 0（锚点）的 logits 对应「下一个该是什么」，正好用来验证草稿第 1 个 token，以此类推。

**第 3 步：接受/拒绝**（`model.py:277-292`）

- 温度 > 0：`target_probs = _sampling_probs(output.logits, ...)`，然后 `_rejection_sample(...)` 返回 `acceptance_length`（连续接受了多少个）和 `bonus`（一个额外的奖励 token）。数学细节见 §5.5。
- 温度 = 0（贪心）：

```python
posterior = torch.argmax(output.logits, dim=-1)
acceptance_length = (block_output_ids[:, 1:] == posterior[:, :-1]).cumprod(dim=1).sum(dim=1)
bonus = posterior[:, acceptance_length]
```

`cumprod`（累乘）的作用是「一票否决」：一旦某位置不相等，之后全部计 0，从而得到**最长的相等前缀**长度。源码随后会再取 `[0].item()`，把长度变成 Python `int`，`bonus` 则再取 `[0]` 变成单个 token。

**第 4 步：写回结果、推进、停止检查**（`model.py:293-308`）

```python
output_ids[:, start : start + acceptance_length + 1] = block_output_ids[:, : acceptance_length + 1]
output_ids[:, start + acceptance_length + 1] = bonus
produced = min(acceptance_length + 1, max_length - start - 1)
```

本轮实际产出 = 接受数 + 1（bonus，或拒绝位置的修正采样）。随后检查新产出的部分有没有停止符（`torch.isin`），有就截断并退出；把目标模型 KV cache 裁到新的 `start`；若下一块大于 1，取本轮输出前 `produced` 个位置的隐藏状态作为下一块的 `target_hidden`（源码是 `[:, :produced, :]`）。

> **为什么 `target_hidden` 要裁成 `[:, :produced, :]`？**
> 只有被接受的 token 才是「可信上下文」。被拒绝的草稿位置对应的目标特征不应参与下一轮条件。

循环结束后裁剪 `output_ids` 到实际长度，`return_stats=True` 时额外返回 `SimpleNamespace`，包含：token 数、首字延迟（time_to_first_token）、平均每 token 耗时、每轮接受长度列表（可算接受率）。

### 4.4 参数小结

| 参数 | 作用 | 备注 |
|---|---|---|
| `model` / `target` | 草稿 / 目标模型 | 草稿模型复用目标模型的词嵌入表和 lm_head |
| `max_new_tokens` | 生成长度上限 | |
| `stop_token_ids` | 停止符 | 如 EOS；出现在接受序列中立即截断 |
| `temperature` | 0 贪心，>0 随机 | 决定走拒绝采样还是相等前缀比较 |
| `top_p` / `top_k` | 截断采样 | 草稿和目标使用同样的截断，保证分布一致 |
| `block_size` | 块大小 | 越大潜在加速越高，但草稿准确率下降；量化推理建议 ≤ 5 |
| `return_stats` | 返回统计信息 | 基准测试用 |

---

## 5. 采样工具函数

### 5.1 `_validate_sampling`（`model.py:77`）

一行检查：`temperature ≥ 0`、`0 < top_p ≤ 1`、`top_k ≥ 0`，不合法就抛 `ValueError`。

### 5.2 `sample`（`model.py:82`）

采样统一入口：

```python
if temperature <= 0:
    return torch.argmax(logits, dim=-1)        # 贪心
return _sample_probs(_sampling_probs(logits, temperature, top_p, top_k))
```

### 5.3 `_sampling_probs`（`model.py:46`）—— logits → 截断后的概率分布

四步：

1. **温度缩放**：`scores = logits.float() / temperature`。温度越高分布越平（更随机），越低越尖。用 float32 防止半精度下 softmax 溢出。
2. **top-k**：若 `0 < top_k < vocab_size`，用 `torch.topk` 只保留分数最高的 k 个，其余记在 `indices` 里，最后再散射（scatter）回完整词表（被筛掉的概率为 0）。
3. **softmax** 得到概率。
4. **top-p（核采样）**：把概率从大到小排序，保留「累计概率刚好不足 `top_p`」的那一批（判断式 `cumsum - 自身 < top_p` 保证当前这个大概率词本身总被保留），其余清零，再归一化。

返回一个**完整的词表大小概率向量**（被截断处为 0），这对后面的拒绝采样很重要——`p` 和 `q` 必须在同一词表空间里逐元素相减。

### 5.4 `_sample_probs`（`model.py:72`）

`torch.multinomial` 按概率抽一个索引；先把任意批量形状压平成二维，抽完再恢复形状。

### 5.5 `_rejection_sample`（`model.py:94`）★

签名：

```python
def _rejection_sample(draft_tokens, target_probs, draft_probs, draft_indices=None)
    -> (accepted: int, bonus_token: Tensor)
```

设 γ = 草稿长度。

**第 1 步：取出草稿 token 在两个分布下的概率**（`model.py:101-105`）

```python
p = target_probs[:, :gamma].gather(-1, draft_tokens[..., None])[..., 0]
q = draft_probs.gather(...)  # 或经 draft_indices 的 one-hot 内积
```

- `p[0, t]` = 目标模型在第 t 个草稿位置给草稿 token 的概率；
- `q[0, t]` = 草稿模型自己的概率。`draft_indices` 分支服务于 DFlash2：`CandidateSelector` 只在 top-k 候选子空间里定义概率，需要用候选索引表把「词表 id」映射回「子空间概率」（用 `(draft_indices == token)` 的 one-hot 乘法实现）。

**第 2 步：接受判定**（`model.py:106-108`）

```python
accepted = (torch.rand_like(q) * q < p).to(torch.int32).cumprod(-1).sum(-1)[0].item()
```

逐位置生成均匀随机数 *u*，条件 `u·q < p` 等价于以概率 `min(1, p/q)` 接受——这正是标准拒绝采样。`cumprod` 再次发挥「一票否决」作用：得到**从头开始连续接受**的个数。

**第 3 步：全接受 → 发 bonus**（`model.py:109-110`）

γ 个全中时，直接从目标模型在最后一个位置的分布采一个额外 token（它是免费的，因为验证时已经算出来了）。

**第 4 步：有拒绝 → 从残差分布补一个**（`model.py:112-124`）

在第一个拒绝位置构造残差分布，直觉上就是：

```python
residual = max(0, p - q)          # 逐元素相减后截断到非负
residual = residual / residual.sum()   # 归一化；若全零则退回 p
```

从 `residual` 采样作为该位置的最终输出。这就是 §2.2 提到的、保证输出分布严格等于目标分布的标准做法。

源码里还多了两处实现细节：若传入了 `draft_indices`（DFlash2），`q` 只定义在 top-k 候选上，要用 `scatter_add_` 把候选概率减到完整词表上的残差里；若残差求和为 0，则退回该位置的目标分布 `p`。

---

## 6. 草稿模型 `DFlashDraftModel`

### 6.1 结构总览（`model.py:550-571`）

```python
self.layers    = [Qwen3DFlashDecoderLayer × num_hidden_layers]  # 通常 1 层
self.norm      = Qwen3RMSNorm(...)        # 最终归一化
self.rotary_emb = Qwen3RotaryEmbedding(...)  # RoPE 位置编码
self.fc        = nn.Linear(len(target_layer_ids) * hidden_size, hidden_size)
self.hidden_norm = Qwen3RMSNorm(...)
self.block_size   # 默认 16：一块草稿几个 token
self.mask_token_id  # 扩散掩码占位符的 id
self.target_layer_ids  # 从目标模型哪些层抽特征
```

草稿模型是个**迷你 Transformer**（隐层宽度与目标模型相同，层数极少，通常只有 1 层），因此跑起来很快。

### 6.2 `build_target_layer_ids`（`model.py:25`）与 `extract_context_feature`（`model.py:37`）

草稿模型不看目标模型的最后一层输出，而是抽**若干中间层**的隐藏状态拼起来：

```python
build_target_layer_ids(36, 4)  # 目标 36 层、草稿 4 个特征层 → [1, 12, 22, 33]
build_target_layer_ids(36, 1)  # → [18]（中间层）
```

多个特征层时在 `[1, num_target_layers-3]` 区间均匀取点；单特征层取正中间。中间层特征兼具语义与局部信息，且「目标模型还没算完」的位置也有值，适合给草稿模型当条件。

```python
def extract_context_feature(hidden_states, layer_ids):
    offset = 1
    selected = [hidden_states[layer_id + offset] for layer_id in layer_ids]
    return torch.cat(selected, dim=-1)
```

`offset = 1` 是因为 HuggingFace 的 `output.hidden_states` 元组第 0 项是**词嵌入**，第 *i+1* 项才是第 *i* 层的输出。拼接后形状 `(1, ctx_len, k·hidden_size)`。

### 6.3 `forward`（`model.py:573-597`）

```python
def forward(self, position_ids, attention_mask=None, noise_embedding=None,
            target_hidden=None, past_key_values=None, use_cache=False, **kwargs):
    hidden_states = noise_embedding                      # 输入 = 锚点+MASK 的词嵌入
    target_hidden = self.hidden_norm(self.fc(target_hidden))  # 多层特征 → 压缩融合
    position_embeddings = self.rotary_emb(hidden_states, position_ids)
    for layer in self.layers:
        hidden_states = layer(hidden_states=..., target_hidden=..., ...)
    return self.norm(hidden_states)
```

两路输入：

- **`noise_embedding`**（「噪声流」）：当前块的锚点 token + MASK 占位符的词嵌入，是草稿模型要加工的对象；
- **`target_hidden`**（「上下文流」）：目标模型中间层特征经 `fc` 融合、RMSNorm 后的条件向量，在每一层以 K/V 形式被注意力读取（见 §7）。

### 6.4 `compute_logits`（`model.py:599-605`）

把草稿隐藏状态投影到词表：

```python
logits = output_head(hidden)                       # 复用目标模型的 lm_head
logits *= output_multiplier                        # 可配缩放（默认 1.0）
logits = tanh(logits / softcap) * softcap          # 可选 softcap，抑制极端 logit
```

**复用目标的 `lm_head`** 意味着草稿模型无需自己维护一个词表大小的输出矩阵，参数量小、且输出空间天然与目标一致。`final_logit_softcapping` 用 `tanh` 把 logits 平滑地压在 ±softcap 之间。

### 6.5 `spec_generate`（`model.py:607-627`）

便捷封装：`self.eval()` 后转发给 `dflash_generate`。

---

## 7. 注意力层：`Qwen3DFlashAttention` 与 `Qwen3DFlashDecoderLayer`

### 7.1 `apply_rotary_pos_emb`（`model.py:331-337`）

标准 RoPE，唯一的定制是 **Q 与 K 长度不同**：

```python
q_embed = q * cos[..., -q_len:, :] + rotate_half(q) * sin[..., -q_len:, :]
k_embed = k * cos + rotate_half(k) * sin
```

K 序列 = 缓存的历史 + 上下文 + 当前块，比 Q 长；Q 只取 `cos/sin` 的**最后 `q_len` 行**，对应「K 序列末尾的那段位置」，与 `cache_position` 的语义一致。

### 7.2 `Qwen3DFlashAttention`（`model.py:340-420`）★

这是草稿模型与目标模型最大的结构差异：**K/V 由两路拼接而成**——目标上下文（交叉注意力部分）+ 草稿自身序列（自注意力部分）。

`__init__` 的关键成员（GQA 布局，与 Qwen3 相同）：

| 成员 | 含义 |
|---|---|
| `head_dim` | 每个注意力头的维度 |
| `num_key_value_groups` | 查询头数 / KV 头数（分组查询注意力） |
| `scaling = head_dim ** -0.5` | 注意力分数缩放因子 |
| `q_proj / k_proj / v_proj / o_proj` | 四个线性投影（K、V 投影被两路共享） |
| `q_norm / k_norm` | Qwen3 特有的对 Q、K 逐头 RMSNorm |
| `is_causal` / `sliding_window` | 该层是否因果掩码、是否滑窗，由 `config.layer_types[layer_idx]` 决定 |

`forward` 的计算流程：

```python
q = q_norm(q_proj(hidden_states))            # 只有草稿流当 Query
k_ctx, v_ctx   = k_proj(target_hidden), v_proj(target_hidden)   # 上下文流当 K、V
k_noise, v_noise = k_proj(hidden_states),  v_proj(hidden_states) # 草稿流也当 K、V
k = cat([k_ctx, k_noise]);  v = cat([v_ctx, v_noise])
q, k = apply_rotary_pos_emb(q, k, cos, sin)
k, v = past_key_values.update(k, v, layer_idx, ...)   # 写入 KV cache
if 需要掩码: attention_mask = _attention_mask(q, k, ...)
out = sdpa(q, k, v, attention_mask, scaling=...)      # 标准缩放点积注意力
return o_proj(reshape(out))
```

直觉：**每个 MASK 位置（Query）同时看两样东西**——目标模型给的上下文特征（「前文讲了什么」）和块内/历史草稿位置（「块里别的格子猜了什么」）。上下文流的 K/V 只在前向时现算，不长期占用草稿缓存（缓存每轮被 `_crop_to` 修剪，见 §4.3）。

### 7.3 `_attention_mask`（`model.py:157-171`）

当外部没传掩码、但层需要因果/滑窗时，手工构造一个 `(1,1,qlen,clen)` 的布尔矩阵：

```python
query_position = key_len - query_len + arange(query_len)   # 每个 Q 在 K 序列中的绝对位置
key_position   = arange(key_len)
visible = ones
if is_causal:       visible &= key_position <= query_position      # 只看过去
if sliding_window:  visible &= query_position - key_position < W   # 且距离 < 窗口
                    visible &= key_position - query_position < W   # 双向滑窗时两侧都限
```

`query_position` 从 `key_len - query_len` 起步，是因为 K 序列前段是缓存的历史，Q 对应 K 的**末尾**一段——与 RoPE 的切片逻辑（§7.1）保持一致。

### 7.4 `Qwen3DFlashDecoderLayer`（`model.py:423-475`）

标准 pre-norm 残差块，骨架是：

```text
x → RMSNorm → DFlashAttention(+, target_hidden) → + 残差
  → RMSNorm → MLP                               → + 残差
```

两个可选钩子 `attention_conv` / `mlp_conv`（默认 `None`）：DFlash2 会在注意力和 MLP **前后各插一个动态因果卷积**（§8.1）。`GradientCheckpointingLayer` 基类只在训练时生效（用时间换显存）。

---

## 8. DFlash 2 的三件新武器

`DFlash2DraftModel`（`model.py:630`）继承第一代，在 `__init__` 里给每一层挂上两个 `GroupedDynamicCausalConv`（分别包在注意力和 MLP 外侧），并新增一个 `CandidateSelector`。`from_pretrained` 里的 `key_mapping` 只是权重文件的命名兼容（代码库的 Embedding 权重名比 checkpoint 多一个 `.weight` 后缀）。

### 8.1 `GroupedDynamicCausalConv` 与 `_grouped_dynamic_convolve` ★

**动机**：扩散模型一次并行出整块，缺少自回归模型那种「逐字依赖」。在每层前后加一个**因果（只看左侧）短卷积**，让每个位置的表示融合左侧邻近位置的信息，补上局部序列结构。

**「动态」的含义**：卷积核不是固定的，而是由当前隐状态经 `kernel_projection` 线性变换**逐位置生成**的——不同内容用不同核。

结构（`model.py:492-499`）：

```python
self.base_kernel      # 形状 (2, kernel_size, hidden_size)：2 个基础核（进/出各一）
self.kernel_projection  # hidden_size → 2·kernel_size·groups 的线性层（生成动态核）
```

`prepare(hidden)`（进注意力前）：

1. 用 `kernel_projection` 从隐状态算出动态核，拆成两份；
2. 用 **0 号基础核 + 动态核第 0 份**做一次卷积；
3. 返回（卷积后的隐状态，动态核第 1 份）——第 1 份留给 `finish` 用，**一次投影两处复用**。

`finish(hidden, dynamic)`（出注意力/MLP 后）：用 **1 号基础核 + 动态核第 1 份**再卷积一次。

卷积本体 `_grouped_dynamic_convolve`（`model.py:478-489`）逐步展开：

```python
blocks  = hidden.view(batch, length, groups, group_size)        # 通道分组
dynamic = dynamic.view(batch, length, kernel_size, groups, 1)   # 每位置的动态核
output  = 0
for offset in range(kernel_size):
    values = blocks 向左平移 offset 位（offset=0 即自身；否则右侧补零 → 因果）
    kernel = base[offset]                                        # 基础核在该偏移的权重
    output = output + kernel * values                            # 基础核贡献（静态）
    output = output + dynamic[:, :, offset] * values             # 动态核贡献（逐位置）
```

即：**输出 = Σₒ (基础核ₒ + 动态核ₒ(位置)) × 左侧第 ₒ 个邻居**。「分组」（每 `group_size` 个通道共享一组核系数）大幅减少参数量。因果性由「只取左侧邻居 + 右侧补零」保证。

### 8.2 `CandidateSelector`（`model.py:515-547`）★

**动机**：第一代草稿对块内每个位置独立取 argmax/采样，位置之间没有协调，容易拼出别扭的序列。`CandidateSelector` 用**二元语法（bigram）打分**把整条候选链一起挑出来。

结构：

```python
self.predecessor_codebook  # Embedding(vocab, rank)：每个词作为「前驱」的向量
self.successor_codebook    # Embedding(vocab, rank)：每个词作为「后继」的向量
self.hidden_projection     # hidden_size → rank：把上下文压进同一低秩空间
self.top_k                 # 每个位置从 logits 取多少个候选
```

`select(hidden, logits, anchor_ids, temperature)` 逐位置推进：

```python
unary, candidates = topk(logits, top_k)          # 一元分数 + 候选词表
hidden = hidden_projection(hidden)               # (batch, len, rank)
predecessor = anchor_ids                         # 第一个位置的前驱 = 锚点
for position in range(len):
    scores = unary[:, position]                          # 一元：该位置本身的 logits
           + einsum("br,bkr->bk",                       # 二元：前驱×后继内积
               predecessor_codebook(predecessor) * hidden[:, position],
               successor_codebook(candidates[:, position]))
    index  = argmax(scores)（或按温度采样，并记录概率 q）
    predecessor = candidates[position][index]            # 选中的词成为下一位置的前驱
    path.append(predecessor)
return stack(path), candidates, stack(q)
```

打分公式（每个候选 *k* 在位置 *t*）：

```text
score(t, k) = logits(t, k)                                    ← 一元：草稿模型说它多像
            + ⟨ e_pred(前一个词) ⊙ h_t ,  e_succ(候选词) ⟩     ← 二元：和前文的搭配度
```

- `⊙` 是逐元素乘：上下文向量 `h_t` 充当「门控」，决定此刻更看重前驱 - 后继搭配的哪些方面；
- `einsum("br,bkr->bk")` = 每个候选与门控后的前驱向量做内积；
- `rank` 是这个低秩空间的大小，控制共现建模的容量。

贪心时逐位置取 argmax；温度 > 0 时把 scores 看作该位置的分布采样，并把概率 `q` 逐行存下来——它们就是拒绝采样里的「草稿分布」，随 `propose` 返回给 `dflash_generate`（这就是 §5.5 中 `draft_indices` 分支的由来）。

> 注意：这个选择是**顺序的**（位置 *t* 依赖位置 *t−1* 的选择），但计算量极小（只是 top-k 上的内积），不会抹掉并行草稿带来的加速。

### 8.3 `propose`（`model.py:653-659`）

一行胶水：`compute_logits` 之后交给 `candidate_selector.select`。

---

## 9. 配置项（`dflash_config`）速查表

`_draft_config` / `_draft_value`（`model.py:127-132`）的读取顺序：先查 `config.dflash_config` 字典，再退回 `config` 同名属性，最后用默认值。常见键：

| 键 | 出现处 | 含义 |
|---|---|---|
| `block_size`（默认 16） | `DFlashDraftModel.__init__` | 一块草稿的 token 数 |
| `mask_token_id` | 同上 | 扩散掩码占位符的词表 id |
| `target_layer_ids` | 同上，缺省由 `build_target_layer_ids` 算 | 抽特征的目标层编号 |
| `input_embedding_scale`（默认 1.0） | `dflash_generate` | 噪声嵌入的缩放系数 |
| `output_multiplier`（默认 1.0） | `compute_logits` | logits 缩放 |
| `final_logit_softcapping` | `compute_logits` | >0 时对 logits 做 tanh 软截断 |
| `conv_kernel_size` / `conv_group_size` | `DFlash2DraftModel` | 动态卷积的核宽 / 通道分组大小 |
| `selector_rank` / `selector_top_k` | `CandidateSelector` | 二元打分的低秩维度 / 每位置候选数 |

---

## 10. 端到端走一遍的例子

设 `block_size = 4`，提示词已 prefill 完毕，第一个生成词是 `"猫"`（位于位置 `start`）。

```text
轮次 1
├─ 块输入：  [猫，MASK, MASK, MASK]
├─ 草稿：DFlash 并行预测 → [猫，坐，在，地，毯]？不，块大小 4 → 预测 3 个：坐/在/地
├─ 目标验证：一次前向，得到 4 组 logits
├─ 贪心比较：目标 argmax = [坐，在，垫] → 前 2 个相等，第 3 个不符
├─ 接受：acceptance_length = 2，bonus = 垫
└─ 产出：坐 在 垫（3 个新 token），start += 3
轮次 2
├─ target_hidden ← 本轮「坐 在 垫」对应位置的目标中间层特征
├─ 块输入：  [垫，MASK, MASK, MASK]
└─ ……
```

若某轮 4 个草稿全被接受，还会额外白拿一个 bonus，单轮最多产出 `block_size` 个 token；若第 1 个就被拒，也至少产出 1 个（修正采样/目标 argmax），**任何情况下都在前进**。

衡量加速效果的关键统计量就是 `acceptance_lengths`：平均每轮产出越接近 `block_size`，加速比越高。

---

## 附：与仓库其余部分的衔接

- `dflash/cli.py:52-81`：`dflash generate transformers` 子命令加载目标 + 草稿模型后直接调用 `dflash_generate`（导入在第 60 行，调用在第 71 行）。
- `dflash/benchmark.py`：提供 `load_transformers_models`、停止符列表、计时基准等（`return_stats=True` 的数据消费者）。
- `dflash/__init__.py`：对外导出 `DFlashDraftModel`、`DFlash2DraftModel`、`extract_context_feature`、`sample`。
- `dflash/model_mlx.py`：同一套生成逻辑的 MLX 后端实现，供 `dflash generate mlx` 使用，不在本文展开。
