# DeepSeek Sparse Attention (DSA)

> [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556) — DeepSeek，2025.12。DSA 是相对 V3.1-Terminus **唯一的架构改动**，经由续训接入。先以 [V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp)（2025.09.29）放出，正式版 V3.2 用的是完全相同的结构。

MLA 的定义在 [MLA](./04-MLA.md)。[V3.2 的简版](../frontier/11-deepseek-v32.md) 只讲了骨架，这篇补细节。

一句话定位：**MLA 压每个 token 的宽度，DSA 减少参与计算的 token 数**。两者正交。DSA 不是新层，是装在已有 MLA 检查点上的续训模块。

## index

为当前 Query token 生成 64 个 128 维查询向量；
为每个历史 token 生成一份共享的 128 维索引 Key；
每个索引头分别计算 Query–Key 相似度；
对每个头的相似度做 ReLU；
使用当前 Query 生成的 64 个动态权重，将这些头聚合成一个标量分数；
对所有历史 token 的标量分数取 Top‑2048；
主 MLA 只加载这 2048 个 token 的真正 KV cache，并重新计算正常的 softmax attention。


## 它没有改什么

先划边界，面试里最容易被追问。

- MoE、MTP、FP8 训练配方都没动，还是 V3 那套块。
- 没有换掉注意力。主注意力仍然是 MLA，只是在更少的 KV 上做。
- 不是量化，也不是线性注意力。KV cache 一个字节都没省，实际还多了一点（见「收益和代价」）。
- **别把 DSA 当成 V3.2 的全部。** 报告里追上闭源模型靠的是 RL 规模化和智能体数据合成，DSA 只负责把长上下文的成本打下来。

## 两段式：便宜的打分 + 昂贵的注意力

把账拆开看：注意力的总成本 = 「每个查询给每个历史位置打分」+「对高分位置做完整的 QK 和 PV」。稠密注意力把两件事合成一次矩阵乘。DSA 拆开：打分用极便宜的算力做满全历史，注意力只对少数位置做。

### Lightning indexer

对查询 token $\mathbf{h}_t$ 和历史 token $\mathbf{h}_s$：

$$
I_{t,s} = \sum_{j=1}^{H^I} w^I_{t,j} \cdot \mathrm{ReLU}\left( \mathbf{q}^I_{t,j} \cdot \mathbf{k}^I_s \right)
$$

四个设计决定都是为吞吐服务的：

- **头少。** 以 V3.2-Exp 的 `config.json` 为准，$H^I = 64$、$d^I = 128$；主注意力是 $n_h = 128$，每头 QK 192 维（128 内容 + 64 位置）、V 128 维。论文只说「头数很少」，具体数字看 config。
- **key 是共享的。** 式子里 $\mathbf{k}^I_s$ 没有头下标 $j$，只有查询是分头的。indexer 自己也是 MQA，每个历史 token 只存一份 128 维的 index key。
- **ReLU。** 论文给的理由是吞吐。副作用更重要：ReLU 把大量点积压成 0，很多历史 token 的索引分**恰好为 0**；只要非零项多于 $k$，这些位置就永远选不上，等于免费剪枝。
- **可 FP8。** 打分不需要精度，只为排序服务。

注意 $I_{t,s}$ 不是概率，没有在序列维做 softmax。它只是分数，只有相对大小有意义。

### 一次 indexer 前向的完整数据流

官方 demo（`inference/model.py` 的 `Indexer`）只有三个线性投影（外加 index key 上的一次 LayerNorm），输入是本层 hidden $\mathbf{x}_t\in\mathbb{R}^{7168}$ 和 MLA 已经算好的压缩 query $\mathbf{qr}_t\in\mathbb{R}^{1536}$：

| 量 | 怎么来 | 每 token 形状 | 精度 |
|---|---|---|---|
| $\mathbf{q}^I_{t,j}$ | $\mathbf{qr}_t W^I_Q$ | $64\times128$ | FP8 |
| $\mathbf{k}^I_s$ | $\mathrm{LN}_{d^I}(\mathbf{x}_s W^I_K)$ | $128$（全头共享一份） | FP8 |
| $w^I_{t,j}$ | $\mathbf{x}_t W^I_w$ | $64$ | FP32 |

然后五步：

1. **分头 + RoPE。** 每头 128 维 = 64 维 RoPE + 64 维 nope，只对前 64 维旋转。indexer 吃**非交错**布局，主注意力吃交错布局，不能共用一个 `apply_rotary_emb`。
2. **进 FP8。** 先做 Hadamard 旋转压离群值，再按 128 维一块量化，scale 用 `ue8m0`（纯 2 的幂），反量化等于抬指数。量化后的 index key 直接写进 cache，每 token 每层只多 **128 + 4 字节**。
3. **打分。** 一次 FP8 GEMM 算出 64 个头对全历史的 logits；逐头 $\mathrm{ReLU}$，乘 $1/\sqrt{d^I}$、乘 $w^I_{t,j}$，对 64 个头求和，再乘 key 的 block scale。$1/\sqrt{H^I}$ 预先折进 $w^I$，头数变化时分数尺度不变。**没有 softmax，也没有跨 $s$ 的归一化**。
4. **掩码 + top-k。** $I$ 的形状是 $[B, L_q, L_k]$；未来位置置 $-\infty$，每行取 `topk(min(2048, end_pos))`，得到 $[B, L_q, 2048]$ 的位置下标。$L<2048$ 时退化成全选。
5. **交给主注意力。** 下标 scatter 成 0 / $-\infty$ 的掩码，加到 MLA 的 logits 上再 softmax。选择按 **query token 各选各的、token 粒度**；同一行的 128 个主注意力头共享这一份选择——这就是它必须装在 MLA 的 MQA 模式上的原因。

Q 从 $\mathbf{qr}$ 而不是从 $\mathbf{x}$ 出，是为了和 MLA 的 $W^{UQ}$ 合并成一个 GEMM；只有 $W^I_K$ 和 $W^I_w$ 需要新的 $7168\to\{\cdot\}$ 投影。

!!! note "prefill 的 MHA 模式在干什么"
    官方 demo 的 prefill 分支并没有真的省算力：它把 $\mathbf{c}_s$ 经 $W^{UK}$ 展开成每头 K/V，算出**满的** $L\times L$ 主注意力 logits，再用 top-k 掩码把未选中的位置打成 $-\infty$。这就是报告里说的 masked MHA 模式——短序列下直接用稠密 kernel 更快，结果与真实稀疏等价。真正省算力的 gather 路径在正式 kernel 里。decode 因为 $m=1$ 只能走吸收后的 MQA 模式。

### 为什么瓶颈会从注意力挪到 indexer

单对 $(t,s)$ 的乘加：indexer $64\times128=8192$；主注意力 MHA 模式 $128\times320=40960$（indexer 约 $1/5$），吸收后的 MQA 模式 $128\times(576+512)=139264$（约 $1/17$）。

- $L=4096$、$k=2048$ 的 prefill：causal 下两者都约 $8.4\times10^6$ 对，indexer 占注意力总算力 $8192/(8192+40960)\approx\mathbf{17\%}$。
- 128K decode、单个 query：indexer $128\mathrm{K}\times8192\approx1.07$ GMAC，主注意力 $2048\times139264\approx0.29$ GMAC，**indexer 反超 3.8 倍**。

所以稀疏把主注意力压到足够便宜之后，打分器自己成了长上下文 decode 的瓶颈。这一层的后续优化基本都落在这：DeepGEMM 的 `mqa_logits` / `sparse_mqa_logits` 专用 kernel（demo 里就是 `fp8_index`）、块级预筛再 token 级精排、相邻 decode step 复用 top-k，以及 V4 先把序列压成记忆槽再选。

### 细粒度 top-k 选择

每个查询只把索引分最高的 $k$ 个 KV 潜变量送进主注意力：

$$
\mathbf{u}_t = \mathrm{Attn}\left( \mathbf{h}_t, \left\{ \mathbf{c}_s \mid I_{t,s} \in \mathrm{Top}_k(I_{t,:}) \right\} \right)
$$

$\mathbf{c}_s$ 就是 MLA 那份 $d_c + d_R$ 的潜变量，不是按头展开的 K/V。V3.2 取 $k = 2048$，写死在 config 里（`index_topk`），不随序列长度变。

选择是**token 粒度**的，不是 block 粒度。发布说明里强调的 "fine-grained" 就是这个意思。

有一个必须讲的细节：softmax 只在选中的 $k$ 个位置上做，未选中位置的概率质量直接丢掉。所以训练 indexer 时，目标分布也要在同一个选中集合上重新归一化，否则蒸馏目标和自己算的东西对不上。

## 复杂度账

主注意力从 $O(L^2)$ 变成 $O(Lk)$。indexer 仍是 $O(L^2)$，但每一对的乘加少一个数量级。

| 部分 | 复杂度 | 每对 $(t,s)$ 的乘加 |
|------|----------|------------------------|
| 稠密主注意力（V3.1） | $O(L^2 \cdot n_h \cdot (d_h + d_R + d_v))$ | $128 \times 320 \approx 4.1\times10^4$ |
| Lightning indexer | $O(L^2 \cdot H^I \cdot d^I)$ | $64 \times 128 \approx 8.2\times10^3$ |
| 稀疏主注意力（DSA） | $O(L \cdot k \cdot n_h \cdot (d_h + d_R + d_v))$ | 只发生 $k$ 次 |

$k = 2048$ 是常数，所以 $k/L$ 随长度走：128K 时主注意力只剩约 $1/64$，1M 时约 $1/500$。序列越长越划算，短序列不划算。

被问「那 indexer 不还是二次的吗」，分三层答：

1. **常量小。** 约 $1/5$ 的乘加，FP8 再压一档，而且没有 online softmax 的 rescale、没有 PV 那一半。
2. **decode 是带宽 bound，不是 FLOPs bound。** 每步要读的 KV，主干是 $L \times 576$ 个 BF16 元素，约 1.1 KB/token；DSA 的打分段只读 index key，$L \times 128$ 个 FP8，128 B/token，约 $1/9$。真正的注意力只读 2048 个潜变量。128K、单层粗算：151 MB → 16.8 + 2.4 ≈ 19 MB，约 8 倍。这和官方 decode 成本曲线在 128K 处的降幅对得上。
3. **二次项最终得换掉。** 下一步是先把 $L$ 本身变小（即 [V4](../frontier/12-deepseek-v4.md) 的 CSA / HCA），而不是继续调 $k$。

## 为什么装在 MLA 的 MQA 模式上

论文给的理由是 kernel 层的：**每个 KV 条目必须被多个查询头共享**，算术强度才够。

稀疏选择之后，一个被选中的 token 会被 128 个查询头同时用到。如果把潜变量按头展开成 MHA 形式，选中 2048 个 token 就要 gather $2048 \times 128$ 份 K/V，gather 的开销会把稀疏省下的算力吃回去。

MQA 模式下，推理时把 $W^{UK}$ 吸收进查询侧、$W^{UV}$ 吸收进输出侧，主注意力直接在 $d_c + d_R$ 的潜变量空间里做。一个被选中的 token 只读一次 576 个元素，128 个头全在寄存器里把它用完。这就是它值得写成 kernel 的原因。

!!! warning "别把这句话说反"
    DSA 没有「又压了一次 MLA 的宽度」。潜变量还是 576 维，KV cache 一点没小。它减的是**参与计算的 token 数**。

## 训练：先蒸 indexer，再放开主模型

从 V3.1-Terminus 的 128K 检查点出发，两阶段续训。数据分布与 128K 长上下文扩展阶段完全对齐。

**Dense warm-up。** 主注意力保持稠密，冻结主模型所有参数，只训 indexer。目标分布是把主注意力分数**跨头求和**、再沿序列维 L1 归一化得到的 $p_{t,:}$，损失是 $\mathbb{D}_{\mathrm{KL}}(p_{t,:} \,\|\, \mathrm{Softmax}(I_{t,:}))$。1000 步、每步 16 条 128K 序列，共 2.1B token。

**Sparse training。** 打开 top-k 选择，全部参数解冻，让模型适应稀疏模式。KL 只在选中集合 $\mathcal{S}_t$ 上算。15000 步、每步 480 条 128K 序列，共 943.7B token，$k = 2048$。

最关键的实现细节：**indexer 的输入从计算图里 detach**。indexer 只被 KL 损失训练，主模型只被语言建模损失训练，两条梯度不混。不这么做，indexer 会被 LM loss 拉去做别的事，不再逼近主注意力的分布。

这也解释了为什么「续训就能接」：块结构没变，不需要重训，也不需要重新设计 kernel 的接口。相对 V3 的 14.8T 预训练量，约 946B 续训 token 只占 6% 左右。

## 收益和代价

同一套训练配置下，公开基准与 V3.1-Terminus 基本持平：MMLU-Pro 85.0 对 85.0，AIME 2025 88.4 → 89.3，HLE 21.7 → 19.8，GPQA-Diamond 80.7 → 79.9。外部长上下文评测里 AA-LCR 反而高约 4 分。

成本侧是官方那张 H800 曲线（2 美元/GPU 小时）：128K 位置，prefill 约 $0.65 → $0.19 每百万 token，decode 约 $2.2 → $0.27。4K 附近两者几乎打平甚至略贵——indexer 有固定开销，序列不够长就不划算。所以短 prefill 他们干脆用一个 masked MHA 模式去模拟 DSA。

商业口径是「API 价格下调 50% 以上」：输入 cache hit $0.07 → $0.028，cache miss $0.56 → $0.28，输出 $1.68 → $0.42（每百万 token，2025.09.29 生效）。

代价和坑：

- **KV cache 变大了。** 按元素算，每 token 每层从 576 涨到 704（多了一份 $d^I = 128$ 维的 index key，约 +22%）；index key 可以用 FP8 存，实际字节增幅约一成。省的是访存和算力，不是显存。
- **RoPE 布局不一致。** 2025.11 官方修过一个 bug：indexer 里的 RoPE 要吃非交错（non-interleaved）布局，MLA 里的 RoPE 吃交错布局，demo 实现搞混了会掉点。
- **没有滑窗支路。** top-k 只保证「分数高的」，不保证「最近的」和「开头的 sink」。论文没展开这一点，V4 才显式补上 128 token 的未压缩滑窗。
- `k` 是超参。太小丢召回，太大回退成稠密。2048 是 128K 上下文下的工程折中，不是普适值。

## 和 NSA 不是同一个模块

| | [NSA](./06-NSA&MoBA.md)（2025.02） | DSA（V3.2-Exp / V3.2） |
|--|------------------------------|------------------------|
| 出身 | 研究论文 | 生产模型的一个版本 |
| 支路 | 压缩 + 块级 top-n 选择 + 滑窗，三支路门控融合 | 只有两级：indexer 打分 → top-k 主注意力 |
| 选择粒度 | block | token |
| 训练 | 从头预训练，前向反向都稀疏 | 冻主干、先蒸 indexer，再续训接入 |
| 目标 | 证明稀疏注意力可以原生训练 | 把已有模型的推理成本打下来 |

一句话：NSA 回答「稀疏注意力能不能训」，DSA 回答「已经训好的稠密模型怎么低成本改成稀疏」。

## 和 V4 的 CSA / HCA

DSA 在原始 token 上挑，挑之前序列还是 $L$ 那么长。V4 换的顺序：先把 token 合成更少的记忆槽，再在槽上做稀疏（CSA，每 4 个压 1 条，然后还是 DSA，top-k 512/1024）或稠密（HCA，每 128 个压 1 条）注意力。

所以 DSA 没有消失，它变成了 CSA 里的那个选择算子。压缩公式和槽上的 indexer 见 [CSA](./CSA.md)，模型层面的交替方式见 [DeepSeek-V4](../frontier/12-deepseek-v4.md)。

三层不要并成一个名字：MLA 压宽度，DSA 减 token 数，CSA / HCA 先减序列长度再做注意力。

## 面试里怎么收束

> DSA 是 V3.2 相对 V3.1 唯一的架构改动，两段式：lightning indexer 用少量头、共享 key 的 ReLU 点积给每个历史位置打分，再取 top-2048 交给主注意力，主注意力因此从 $O(L^2)$ 变成 $O(Lk)$。indexer 还是二次的，但每对位置的乘加只有主注意力的五分之一左右，还能走 FP8，所以二次项没消失、只是每一项都便宜了一个量级。它装在 MLA 的 MQA 模式上，因为选中的潜变量要被 128 个查询头共享，否则 gather 会吃掉收益。它减的是参与计算的 token 数，不是 KV 宽度，KV cache 反而因为多存 index key 涨了一点。

## 参考

- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556)（arXiv 2512.02556，DSA 的公式、续训配方、成本图都在 §2）
- [DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp)（官方仓库：推理 demo、benchmark 对齐表、RoPE 布局的修正说明）
- [Introducing DeepSeek-V3.2-Exp](https://api-docs.deepseek.com/news/news250929/)（2025.09.29 发布说明，API 降价口径）
- [DeepSeek-V3.2-Exp `config.json`](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp/raw/main/config.json)（`index_n_heads` / `index_head_dim` / `index_topk` 的实际取值）
- [Native Sparse Attention](https://arxiv.org/abs/2502.11089)（arXiv 2502.11089，对照用）
- [DeepGEMM 的 indexer logit kernel](https://github.com/deepseek-ai/DeepGEMM/pull/200)
[(24 封私信 / 59 条消息) 超细图解 DSA 计算流&性能对比与优化分析 - 知乎](https://zhuanlan.zhihu.com/p/1963371483985319543)