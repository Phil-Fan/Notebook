# 04 | DeepSeek-V3

> DeepSeek-V3 Technical Report — DeepSeek, 2024

<iframe src="https://arxiv.org/pdf/2412.19437" width="100%" height="600px"></iframe>

## 这条线在证明什么

块从 V2 定下来，后面的论文是在同一骨架上换约束。每代的机制分开写，对照在 [架构面试提纲](08-interview.md)。

| 报告 | 它代表的事 | 结构 |
|------|------------|------|
| [DeepSeekMoE](https://arxiv.org/abs/2401.06066) | 专家要切细，并分出共享专家 | 细粒度路由 + 共享专家 |
| [V2](09-deepseek-v2.md) | 压缩 KV 和 MoE 可以同时成立 | MLA |
| [V3](10-deepseek-v3.md) | 这套块可以训到前沿，且不必靠辅助损失硬拉均衡 | 671B / 37B；256 选 8，加 1 个共享专家；MTP；FP8 |
| [NSA](https://arxiv.org/abs/2502.11089) | 稀疏注意力可以原生训练 | 压缩、选择、滑窗三条支路。不是 V3 的检查点，说明放在 [V3.2](11-deepseek-v32.md) |
| [V3.2](11-deepseek-v32.md) | 稀疏注意力可以续训进已有 MLA | DSA：indexer 打分，主注意力只看 top-k |
| [V4](12-deepseek-v4.md) | 百万 token 要先压缩序列 | CSA + HCA；mHC。Pro 1.6T / 49B，Flash 284B / 13B |

V3 的训练账单（2.788M H800 GPU hours）是系统结果。R1 沿用 V3 的块，贡献在 GRPO，不在新的层。
