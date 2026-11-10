# Gemini 2.5

> [Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261) — Google DeepMind，2025。

上一代能力报告仍在 [Gemini](06-gemini.md)。这一页只记录 2.5 真正写出来的结构，以及哪些数字不能编。

## 这篇论文代表什么

2.5 是少数把「我们用稀疏 MoE」写进正文的闭源前沿报告。它要证明的是能力：推理、多模态、长上下文和智能体。架构段落很短，公开的是模型族的种类和训练稳定性，不是一张可以复现的配置表。

## 报告里写了的

Gemini 2.5 Pro 与 Flash 是稀疏 Mixture-of-Experts Transformer，原生接受文本、图像和音频。稀疏的含义和开源 MoE 相同：每个 token 只走一部分参数，总容量和单 token 成本可以分开。报告把相对 Gemini 1.5 Pro 的性能提升，部分归到架构上的改动。

写得更具体的是训练动力学，不是层类型。大规模 Transformer 和稀疏 MoE 都会出现训练不稳。2.5 的工作是改善信号传播和优化动力学，使预训练结束时就比前一代强，而不是只靠后训练补。

## 报告里没有的

没有专家个数，没有每个 token 激活几个专家，也没有总参数。没有说注意力是 MHA、GQA、MLA 还是滑窗。任何「Gemini 2.5 用了某某注意力」的二手表格，只要报告正文没有对应句子，都不要当成结构事实。

Gemini 3（2025.11）是产品发布。公开材料继续把稀疏 MoE 和长上下文当作产品能力，没有一份和 DeepSeek-V4 对等的架构论文。

## 面试里怎么收束

> Gemini 2.5 可以确认是原生多模态的稀疏 MoE Transformer，并且论文把训练稳定性写成架构进展。专家数和注意力变体没有公开。再往下讲 MLA 或 iRoPE，就是在编。和它对位的开源结构应举 DeepSeek、Llama 4 或 Qwen3-Next。
