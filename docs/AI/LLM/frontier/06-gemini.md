# 06 | Gemini

> Gemini: A Family of Highly Capable Multimodal Models — Google DeepMind, 2023

<iframe src="https://arxiv.org/pdf/2312.11805" width="100%" height="600px"></iframe>

## 核心贡献

- **原生多模态**：从训练开始融合文本、图像、音频、视频
- 三个规模：Ultra / Pro / Nano，覆盖云端到端侧
- 在 MMLU 等基准上首次超越人类专家水平
- 自研 TPU v4/v5 大规模训练基础设施

## 之后的报告公开了什么

[Gemini 2.5](19-gemini25.md) 写明模型是稀疏 MoE Transformer，原生接受文本、图像和音频，并把相对 1.5 的进展归到训练稳定性与信号传播。专家个数和注意力变体没有公开。
