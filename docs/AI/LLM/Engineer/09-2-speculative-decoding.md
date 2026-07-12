# Speculative Decoding（推测解码）

## Intuition (one sentence)

**Speculative decoding first drafts several tokens with a cheap method, then verifies them in one pass with the large model: keep correct guesses, discard wrong ones.** If guesses are good, one step can advance multiple tokens.

## Why this helps

- During decoding, GPU time is often dominated by **loading model weights from memory** (memory-bound), not pure compute.
- The idea is: weight-loading cost is still paid, but we do extra verification work in the same round, so each round becomes more productive.
- Guessing extra tokens increases **KV cache** usage, but usually much less than model-weight footprint.

## How to draft guesses

1. **N-gram**: continue based on patterns already seen in context (fast, simple).
2. **Draft model**: use a smaller model to propose several next tokens (usually more accurate, but requires running another model).

Drafting can be **parallel** (faster, less accurate) or **autoregressive** (slower, more accurate).

## Verify

- **Greedy / temperature 0**: a tiny mismatch can collapse the whole drafted span, so speculative decoding often helps less.
- **Stochastic decoding**: accept/reject can follow probability-based rules (details vary by implementation).

**Connection to lossless sampling (optional detail)**: let draft distribution be `q` and target distribution be `p`. A common implementation uses **rejection sampling**: accept a candidate with probability `min(p/q, 1)`, then sample rejected mass from the **residual distribution** `norm(p - q)`. This preserves equivalence to sampling directly from `p`.

## 落地难点（工程向）

- 草稿模型也要 **KV**，显存怎么分、怎么和主模型配合。
- 草稿很小：**不一定和主模型用同一套并行**；多卡时可能出现 **某几张卡闲着、显存却不好匀**（例如 vLLM 一类约束）。
- 给「待验证的一串词」预留 KV 时，可能 **撞上块（block）边界**，要处理丢弃或重排。
- **猜几个词** 要调参；有的请求 **根本不跑** spec decode，要区分对待。
- 小模型本身若强行上大并行，**未必划算**（相对它自己的规模）。

## 论文阅读

- 开山之作 一作[Yaniv Leviathan](https://yanivle.github.io/about/)，[ICML Talk - Fast Inference from Transformers via Speculative Decoding](https://slideslive.com/39006668/fast-inference-from-transformers-via-speculative-decoding?ref=search-presentations-yaniv+leviathan)
- SpecInfer
  - SSM 数据训练方式，每次减掉与 LLM 输出相同的
  - Tree Attention
  - [CMU 发布「投机式推理」引擎 SpecInfer，大小模型联动让 LLM 推理提速 2-3 倍！ - 知乎](https://zhuanlan.zhihu.com/p/634342816)
- self-speculative: draft & verify
  - 跳过一些层，使用贝叶斯优化决定跳过哪些层
  - 动态 draft 退出机制
- REST
  - 建立数据库
  - 召回数据库当中与目标 context 上下文最符合的最长的序列集合
  - 给这个集合建立字典树
  - 使用最大堆维护出现频率和最长后缀
  - 剪枝，选择 c 个作为 draft 候选
  - 使用 tree attention 并行验证
- medusa
  - [Medusa：使用多个解码头并行预测后续多个 token - 知乎](https://zhuanlan.zhihu.com/p/15978788714)
  - head
  - 技巧
    - typical acceptance：使用一个概率，如果熵高的话，也可以接受
    - 自蒸馏：使用模型的输出，并使用 KL 散度，偏向教师模型，而不是直接偏向模型的输出
    - 优化树：使用笛卡尔积比较慢，独立假设，使用概率相乘
- eagle
  - [EAGLE and EAGLE-2： Lossless Inference Acceleration for LLMs](https://www.bilibili.com/video/BV13zPieoECX/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5) 这个视频也介绍了 SD 的基础知识
  - next token prediction is hard, next feature prediction is easier
    - 所以使用 transformer 的 output  用来预测，把特征和 emmedding 向量拼接起来，加了一个单层的 Transformer 来预测下一个 token
  - tree attention
  - 训练：feature smooth L1 loss + token 分类概率交叉熵
  - advanced token sequence：把 token 序列提前一个时间步（shifted by one）作为额外输入，和 feature 拼接（concatenate）用现在的 emmeding 和上一步的 feature
- eagle-2
  - 对树结构进行了改造，使用 confidence score 来选择最优的候选 发现是左偏的
- eagle-3
  - 不仅仅使用 fc 层，也使用 decoder layer 的 output，多层特征经过一个 MLP 后再训练一个模型
  - 在 batch 较高的时候，表现也好
- MTP
  - [MTP（Multi-Token Prediction）的前世今生 - 知乎](https://zhuanlan.zhihu.com/p/18056041194)
  - [大模型推理加速：从 EAGLE 到 DFlash - 知乎](https://zhuanlan.zhihu.com/p/2004595351189987521)
- DFlash
- Pearl
- SwiftSpec 字节
- Speculative Speculative Decoding
  - [谈一下 tri dao 的并行投机采样论文 - 小红书](https://www.xiaohongshu.com/explore/69a9283a000000001b01656d?xsec_token=ABZtxGliDRKNrO14vzxzv3Ii9yeCblV_fJsM2CvxUHD6g=&xsec_source=pc_user)
- TorchSpec

## 参考资料

- [vllm 从源码到部署，speculative decoding - YouTube](https://www.youtube.com/watch?v=9kEbuGTfLZA)
- [Speculative Decoding 必读 10 篇](https://www.xiaohongshu.com/discovery/item/692fa589000000001e00bcc8)

kv 稀疏
