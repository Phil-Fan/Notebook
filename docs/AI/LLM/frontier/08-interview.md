# 近两年架构：面试怎么讲

面试问「这个模型和那篇论文有什么特殊的」，先回答它**代表哪一个约束被拆开了**，再讲块上改了什么。2024–2026 的开源前沿模型几乎都还是 Decoder-only Transformer，特殊之处不在「又发明了一种网络」，而在三条线上：

1. **注意力**：长上下文下 KV cache 和 \(O(L^2)\) 算力。
2. **MoE**：总参数（容量）和每 token 激活参数（算力）拆开。
3. **残差 / 训练稳定性**：上面两件事放大之后，信号还传不传得动。

闭源模型（GPT、Claude、Gemini 的多数版本）公开的是能力报告。架构细节没写出来时，不要补一套 MoE 或 MLA。

下面按「代表什么 → 结构特殊在哪 → 面试里怎么收束」来记。数字以技术报告和官方博客为准。

## 已有的总结

写这份笔记时对照过这些二手整理，细节仍回到论文：

- Sebastian Raschka, [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison)（2025）：DeepSeek-V3、Llama 4、Qwen3 的块级对照，MLA / GQA / MoE 讲得最清楚。
- Raschka, [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms)：MiniMax、Qwen3-Next、Kimi Linear、DeepSeek-V3.2 的线性 / 稀疏注意力。
- [Awesome-LM-Architecture](https://github.com/Superposition09m/Awesome-LM-Architecture)：从 MHA 到 MLA、从 MoE 论文到技术报告的清单。
- [Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch)：线性注意力、Mamba、稀疏注意力论文表。

这些总结覆盖到 2025 年秋。DeepSeek-V4（CSA / HCA、mHC）要直接看 [技术报告](https://arxiv.org/abs/2606.19348)。

## 默认块：开口之前先会的骨架

近两年的论文都默认你认识这套「LLaMA 块」。它本身在 2023 年就已经定型，面试里用来当对照，不要当成新贡献。

| 零件 | 论文 | 它解决的事 |
|------|------|------------|
| Decoder-only + 下一 token | [GPT-3](https://arxiv.org/abs/2005.14165) | 规模上去之后，少样本提示就能做任务。架构就是 Transformer 解码器 |
| RoPE | [Su et al., 2021](https://arxiv.org/abs/2104.09864) | 用相对角度编码位置，后面所有长度外推都从这里改 |
| SwiGLU | [Shazeer, 2020](https://arxiv.org/abs/2002.05202) | 门控 FFN，LLaMA 之后的默认前馈 |
| RMSNorm + Pre-Norm | [Zhang & Sennrich, 2019](https://arxiv.org/abs/1910.07467) | 去掉均值中心化，训练更稳 |
| MQA | [Shazeer, 2019](https://arxiv.org/abs/1911.02150) | 所有头共用一套 K/V，解码时少搬 KV |
| GQA | [Ainslie et al., 2023](https://arxiv.org/abs/2305.13245) | 折中：若干查询头共用一组 K/V |
| 把上面拼成默认块 | [LLaMA](https://arxiv.org/abs/2302.13971) | 小模型、多数据、公开配方。代表「块可以先停在这里，数据和对齐继续堆」 |

GQA 是 2024 年大多数开源模型的注意力默认值（Llama 3、Qwen2/3、Gemma）。MLA、稀疏注意力、线性注意力都是在说：GQA 把 KV 缩小一个常数倍，长上下文下仍然不够。

## 对照：每家押的那一件事

| 模型 | 时间 | 论文 / 出处 | 总参 / 激活 | 它代表的事 | 结构上真正不同的一点 |
|------|------|-------------|-------------|------------|----------------------|
| [DeepSeek-V2](09-deepseek-v2.md) | 2024.05 | [2405.04434](https://arxiv.org/abs/2405.04434) | 236B / 21B | MoE + 压缩 KV 可以同时成立 | MLA；细粒度专家 + 共享专家 |
| [DeepSeek-V3](10-deepseek-v3.md) | 2024.12 | [2412.19437](https://arxiv.org/abs/2412.19437) | 671B / 37B | 同一套块训到闭源前沿，而且训练账单可公开 | 无辅助损失负载均衡；MTP；FP8 |
| [DeepSeek-V3.2](11-deepseek-v32.md) | 2025.12 | [2512.02556](https://arxiv.org/abs/2512.02556) | 沿用 V3 量级 | 稀疏注意力可以续训进已有 MLA 模型 | DSA：廉价 indexer 选 token，主注意力只看 top-k |
| [DeepSeek-V4](12-deepseek-v4.md)（预览） | 2026 | [2606.19348](https://arxiv.org/abs/2606.19348) | Pro 1.6T / 49B；Flash 284B / 13B | 百万 token 要先压缩 KV，再决定稀疏还是稠密 | CSA + HCA；mHC；Muon |
| [Qwen3](13-qwen3.md) | 2025.05 | [2505.09388](https://arxiv.org/abs/2505.09388) | 235B / 22B 等 | 思考 / 非思考放进同一个模型 | 块很保守：GQA + QK-Norm；MoE 去掉共享专家 |
| [Qwen3-Next](14-qwen3-next.md) | 2025.09 | [官方博客](https://www.alibabacloud.com/blog/602580) | 80B / 3B | 线性注意力和标准注意力按层混合 | Gated DeltaNet : Gated Attention = 3 : 1 |
| [Llama 3](15-llama3.md) | 2024.07 | [2407.21783](https://arxiv.org/abs/2407.21783) | 最到 405B 稠密 | 稠密配方的终点是数据和后训练 | 结构上就是 GQA 版 LLaMA 块 |
| [Llama 4](16-llama4.md) | 2025.04 | [Meta 博客](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) | Scout 109B / 17B；Maverick 400B / 17B | 开源权重也改走 MoE，并用位置编码换长上下文 | iRoPE；Maverick 每 token 只进 1 个路由专家 |
| [MiniMax-01](17-minimax.md) | 2025.01 | [2501.08313](https://arxiv.org/abs/2501.08313) | 456B / 45.9B | 线性注意力第一次放到这个规模 | 7 层 Lightning Attention + 1 层 softmax |
| [Kimi Linear](18-kimi-linear.md) | 2025.10 | [2510.26692](https://arxiv.org/abs/2510.26692) | 48B / 3B | 混合线性注意力可以在公平对比下超过全注意力 | KDA 做通道级遗忘门；MLA 层用 NoPE |
| [Gemini 2.5](19-gemini25.md) | 2025.07 | [2507.06261](https://arxiv.org/abs/2507.06261) | 未公开 | 闭源 MoE 的能力与训练稳定性 | 报告只确认稀疏 MoE + 原生多模态，不给专家数和注意力变体 |
| Claude / GPT-o 系列 | 2024–2026 | 模型卡、系统卡 | 未公开 | 对齐，以及把算力挪到测试时 | 没有可讲的新块。不要编 |

## 技术说明在各页

机制放在各模型自己的笔记里。这一页只保留对照和开口方式。

## MoE 稀疏度对照

| | 路由 | 共享专家 | 稀疏度直觉 |
|--|------|----------|------------|
| [DeepSeek-V3](10-deepseek-v3.md) | 256 选 8 | 有，1 个 | 细粒度、多专家，换专精和稳定 |
| [Qwen3-235B-A22B](13-qwen3.md) | 128 选 8 | 无（Qwen2.5-MoE 有，Qwen3 拿掉） | 用全局 batch 的均衡损失鼓励专精 |
| [Llama 4 Maverick](16-llama4.md) | 128 选 1，且与稠密层交替 | 有 | 激活比压到 17B / 400B，服务成本优先 |
| [Qwen3-Next](14-qwen3-next.md) | 约 512 选 10 | 有 | 激活比再降一档，配线性注意力 |
| [Kimi Linear](18-kimi-linear.md) | 256 中激活 8（含 1 个共享） | 有 | 第一层是稠密层，用来稳住训练 |
| [MiniMax-01](17-minimax.md) | 32 选 2 | 报告未把共享专家当作贡献 | 更接近经典 top-2，新意在注意力 |

## 闭源模型：只讲论文真正公开的部分

- **GPT-3** 代表规模定律和 in-context learning，架构就是大号解码器。
- **GPT-4 技术报告**代表多模态输入和 RLHF 之后的考试表现。规模和块没有公开。后面的 o 系列代表测试时计算和强化学习，直到出现公开的架构报告之前，都不要讲成某种注意力变体。
- **Gemini 1.5** 代表把长上下文做成产品能力。[Gemini 2.5](19-gemini25.md) 明确写了自己是稀疏 MoE Transformer，原生吃文本、图像和音频，并把训练稳定性、信号传播写成相对 1.5 的架构进展，但没有专家数，也没有 GQA / MLA 的对照实验。Gemini 3 是产品发布，没有一份对等的架构论文。
- **Claude** 的模型卡代表安全与有用性的产品线（Constitutional AI 一路下来的对齐），以及后来的扩展思考。权重结构未公开。

开源侧在 2024–2026 把「块」写成了论文；闭源侧把「能力和训练稳定性」写成了报告。两边都要会讲，而且要讲明自己知道哪一边没有公开。

## 一段可以背的总述

> 2023 年的默认块是 Pre-Norm、RMSNorm、SwiGLU、RoPE、GQA。2024 年 DeepSeek-V2 用 MLA 压缩 KV 宽度，用细粒度 MoE 把容量和算力拆开；V3 去掉辅助损失并加上多 token 预测，把这套块训到前沿。2025 年之后大家分头处理序列长度：Llama 4 用 iRoPE 把位置编码从全局层拿掉，Qwen3-Next 和 Kimi Linear 用 3 : 1 的线性注意力混合层，DeepSeek-V3.2 用 DSA 在 MLA 上做 token 选择。到 V4，序列先被压进更少的记忆槽（CSA / HCA），残差被 mHC 稳住。Qwen3 和 Llama 3 相反，它们代表「块可以不新，模式切换、数据、蒸馏和后训练才是论文要证明的事」。GPT、Claude、Gemini 的多数报告不提供可复述的块，只能讲它们公开的能力和训练问题。

## 参考

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [RoPE](https://arxiv.org/abs/2104.09864) · [SwiGLU](https://arxiv.org/abs/2002.05202) · [RMSNorm](https://arxiv.org/abs/1910.07467) · [MQA](https://arxiv.org/abs/1911.02150) · [GQA](https://arxiv.org/abs/2305.13245)
- [LLaMA](https://arxiv.org/abs/2302.13971) · [Llama 3](https://arxiv.org/abs/2407.21783) · [Llama 4 博客](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [DeepSeekMoE](https://arxiv.org/abs/2401.06066) · [DeepSeek-V2](https://arxiv.org/abs/2405.04434) · [DeepSeek-V3](https://arxiv.org/abs/2412.19437) · [NSA](https://arxiv.org/abs/2502.11089) · [DeepSeek-V3.2](https://arxiv.org/abs/2512.02556) · [mHC](https://arxiv.org/abs/2512.24880) · [DeepSeek-V4](https://arxiv.org/abs/2606.19348)
- [Qwen3](https://arxiv.org/abs/2505.09388) · [Qwen3-Next 博客](https://www.alibabacloud.com/blog/602580) · [Gated DeltaNet](https://arxiv.org/abs/2412.06464)
- [MiniMax-01](https://arxiv.org/abs/2501.08313) · [Kimi Linear](https://arxiv.org/abs/2510.26692)
- [Gemini 2.5](https://arxiv.org/abs/2507.06261)
- Raschka, [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison) · [Beyond Standard LLMs](https://magazine.sebastianraschka.com/p/beyond-standard-llms)
