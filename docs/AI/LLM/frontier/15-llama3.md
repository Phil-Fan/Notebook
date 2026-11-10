# Llama 3

> [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — Meta，2024.07。稠密模型 8B、70B、405B。预训练超过 15T tokens，上下文 128K。

系列里更早的 LLaMA、Llama 2 仍在 [LLaMA 系列](03-llama.md)。下一代换块的是 [Llama 4](16-llama4.md)。

## 这篇论文代表什么

到 2024 年中，开源侧的默认块已经定型：Pre-Norm、RMSNorm、SwiGLU、RoPE、GQA。Llama 3 没有提出新的注意力或 MoE。405B 仍然是每个 token 走完全部参数的稠密模型。

报告要证明的是另一件事：这套块配上更多、更干净的多语言数据，以及完整的后训练，可以走到当时开源模型的规模终点。结构题里把它当成对照物，而不是创新点。

## 块上能说的

- 解码器堆叠，下一 token 预测。
- 注意力是 GQA。KV 头少于查询头，若干查询头共用一组 key / value。相对 MHA，缓存大约缩小「查询头数 / KV 头数」倍；相对 MQA，每个组仍有自己的 KV，建模损失更小。
- 前馈是 SwiGLU，归一化是 RMSNorm，位置是 RoPE。
- 长上下文是在这套 RoPE 上扩展到 128K，不是一种新的位置编码。

GQA 把 KV 缩小一个常数倍。之后 [DeepSeek-V2](09-deepseek-v2.md) 的 MLA、[V3.2](11-deepseek-v32.md) 的 DSA、[Qwen3-Next](14-qwen3-next.md) 的线性注意力，都是在说这个常数到长上下文不够用。Llama 3 自己停在 GQA。

## 面试里怎么收束

> Llama 3 代表稠密配方的终点：405B 全参数激活，块就是 GQA 版的 LLaMA。论文的分量在 15T 级数据和后训练。问结构创新应转到 Llama 4 的 MoE 和 iRoPE，或者 DeepSeek 的 MLA。
