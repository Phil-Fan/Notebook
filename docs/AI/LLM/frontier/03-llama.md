# 03 | LLaMA 系列

Meta 开源大语言模型系列，从 LLaMA 到 LLaMA 3，引领开源社区发展。

## LLaMA 1

> LLaMA: Open and Efficient Foundation Language Models — Meta, 2023

<iframe src="https://arxiv.org/pdf/2302.13971" width="100%" height="500px"></iframe>

- 核心观点：小模型 + 更多数据 → 更优性能
- 7B/13B/33B/65B 四个规模，纯公开数据训练

---

## LLaMA 2

> Llama 2: Open Foundation and Fine-Tuned Chat Models — Meta, 2023

<iframe src="https://arxiv.org/pdf/2307.09288" width="100%" height="500px"></iframe>

- 引入 RLHF 对齐，发布 Chat 版本
- 2T tokens 训练，上下文翻倍至 4K

---

## LLaMA 3

> The Llama 3 Herd of Models — Meta, 2024

<iframe src="https://arxiv.org/pdf/2407.21783" width="100%" height="500px"></iframe>

- 8B/70B/405B，15T+ tokens 多语言训练
- 128K 上下文，开源中最大规模之一
- 结构上仍是 GQA 版的 LLaMA 块。这篇报告代表数据和后训练，不代表新的注意力

## Llama 4

> The Llama 4 herd — Meta 博客，2025.04。没有单独的架构论文。

- Scout 109B / 17B 激活、16 专家；Maverick 400B / 17B 激活、128 专家。Behemoth 发布时仍是未放出的教师模型
- Maverick 交替稠密层与 MoE 层，每个 token 进入共享专家再加 1 个路由专家
- **iRoPE**：每 4 层中 1 层 NoPE、全长因果注意力，另外 3 层 RoPE 只做 8192 的分块注意力
- 原生多模态用 early fusion

技术说明分开写：[Llama 3](15-llama3.md) 是稠密配方的终点，[Llama 4](16-llama4.md) 才换 MoE 和 iRoPE。对照见 [架构面试提纲](08-interview.md)。
