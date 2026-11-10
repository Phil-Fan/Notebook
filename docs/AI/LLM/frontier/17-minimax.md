# MiniMax-01

> [MiniMax-01: Scaling Foundation Models with Lightning Attention](https://arxiv.org/abs/2501.08313) — MiniMax，2025.01。文本模型 MiniMax-Text-01 为 456B 总参数，每个 token 激活 45.9B。训练上下文 1M，推理外推到 4M。视觉语言版本 MiniMax-VL-01 在此之上继续训练约 512B 视觉语言 tokens。

它比 [Qwen3-Next](14-qwen3-next.md) 和 [Kimi Linear](18-kimi-linear.md) 更早，是「线性注意力可以当大基座」的第一个这个规模的证据。

## 这篇论文代表什么

softmax 注意力的算力和 KV cache 随长度二次增长，百万 token 的训练和推理都不划算。MiniMax 选了一种已经有 I/O 感知实现的线性注意力，先确认它在小规模上能跑，再解决一个实验里暴露的问题：纯 Lightning Attention 检索很弱。补法不是放弃线性层，而是每隔几层放回一层 softmax。

## 混合比是 7 : 1

全模型 80 层。每 7 个 Lightning Attention 块后面接 1 个 softmax Transformer 块。Lightning Attention 是线性注意力的一种 I/O 感知实现：块内和块间的矩阵乘分开做，避免朴素因果线性注意力里那次昂贵的累加扫描。历史被压进固定大小的状态，所以长上下文的缓存不随 \(L\) 存下一整份 KV。

softmax 层用来把检索能力补回来。论文里这是先观察到纯线性注意力检索差，再把每 8 层中的 1 层换回 softmax。这个比例后来没有成为主流。Qwen3-Next 和 Kimi Linear 都改到了 3 : 1，全局层更密。

softmax 层本身是普通的现代注意力，不是 MLA：

- 64 头，每头 128 维。
- GQA，组大小 8。
- RoPE 加在头维度的一半上，base 为 10000。
- 隐藏维 6144。

## MoE 是经典 top-2

每层 32 个专家，每个 token 选 2 个。单个专家的 FFN 中间维是 9216。报告没有把共享专家当作贡献。和 DeepSeek、Qwen3-Next 比，MoE 更接近 Mixtral：专家少、每个专家大、top-2。这篇论文的新意在注意力，不在路由。

## 面试里怎么收束

> MiniMax-01 第一次把线性注意力放到 456B。7 层 Lightning Attention 加 1 层 GQA softmax，因为纯线性注意力检索不够。MoE 是 32 选 2。它证明混合架构能当基座；更密的 3 : 1 和通道级门控是后面 Qwen3-Next 和 Kimi Linear 的事。
