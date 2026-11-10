# 前沿基座模型

经典技术报告按时间线留在各页。近一到两年的面试准备看 [架构面试提纲](08-interview.md)：每篇论文代表哪一个约束被拆开，以及块上到底改了什么。

## 怎么读

2024 年之前的默认块是 Pre-Norm、RMSNorm、SwiGLU、RoPE、GQA。之后开源前沿模型仍是 Decoder-only Transformer，分歧在三条线上：

- **注意力**：KV 的宽度（GQA、MLA）、参与计算的 token（DSA、NSA）、序列先压缩再注意（CSA、HCA）、或把大部分层换成线性注意力。
- **MoE**：总参数和激活参数拆开。DeepSeek 用很多小专家加共享专家；Llama 4 每 token 只进一个路由专家；Qwen3 拿掉了共享专家。
- **连接**：DeepSeek-V4 用 mHC 把加宽的残差流约束回双随机矩阵，换深层稳定性。

GPT、Claude 和 Gemini 的多数报告公开的是能力与训练问题，不是可复述的块。提纲里把这两组分开。

公开的二手总结里，最接近这个问法的是 Sebastian Raschka 的 [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) 和 [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms)，以及 [Awesome-LM-Architecture](https://github.com/Superposition09m/Awesome-LM-Architecture)。V4 的 CSA / HCA 要以技术报告为准，那些总结还没覆盖到。

## 论文与它代表的事

| 模型 | 时间 | 代表的事 | 笔记 |
|------|------|----------|------|
| GPT-3 | 2020 | 规模与 in-context learning | [01](01-gpt3.md) |
| GPT-4 | 2023 | 多模态与对齐；架构未公开 | [02](02-gpt4.md) |
| LLaMA 系列 | 2023 | 公开的稠密默认块 | [03](03-llama.md) |
| Llama 3 | 2024.07 | 这套稠密块的规模终点 | [15](15-llama3.md) |
| Llama 4 | 2025.04 | MoE + iRoPE | [16](16-llama4.md) |
| DeepSeek-V2 | 2024.05 | MLA + 细粒度 MoE | [09](09-deepseek-v2.md) |
| DeepSeek-V3 | 2024.12 | 无辅助损失均衡、MTP | [10](10-deepseek-v3.md) |
| DeepSeek-V3.2 | 2025.12 | DSA，稀疏注意力续训进 MLA | [11](11-deepseek-v32.md) |
| DeepSeek-V4 | 2026 | CSA / HCA、mHC | [12](12-deepseek-v4.md) |
| Qwen 早期 | 2023–2024 | GQA 默认块上的模型族 | [05](05-qwen.md) |
| Qwen3 | 2025.05 | 统一思考模式；块改动很小 | [13](13-qwen3.md) |
| Qwen3-Next | 2025.09 | 3 : 1 混合线性注意力 | [14](14-qwen3-next.md) |
| MiniMax-01 | 2025.01 | 7 : 1 Lightning Attention | [17](17-minimax.md) |
| Kimi Linear | 2025.10 | 通道级门控 + NoPE MLA | [18](18-kimi-linear.md) |
| Gemini | 2023 | 原生多模态能力报告 | [06](06-gemini.md) |
| Gemini 2.5 | 2025 | 确认稀疏 MoE，不公开块的细节 | [19](19-gemini25.md) |
| Claude 3 | 2024 | 安全与有用性；没有架构论文 | [07](07-claude.md) |
