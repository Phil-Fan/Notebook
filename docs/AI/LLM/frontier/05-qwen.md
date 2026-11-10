# 05 | Qwen 系列

阿里通义千问大语言模型系列。

## Qwen Technical Report

> Qwen Technical Report — Alibaba, 2023

<iframe src="https://arxiv.org/pdf/2309.16609" width="100%" height="500px"></iframe>

## Qwen2

> Qwen2 Technical Report — Alibaba, 2024

<iframe src="https://arxiv.org/pdf/2407.10671" width="100%" height="500px"></iframe>

## 核心贡献

- 覆盖 0.5B 到 72B 多个规模，支持 30+ 语言
- GQA、SwiGLU、RoPE 等现代架构组件
- Qwen2.5 在数学和代码基准上表现突出

## Qwen3 与 Qwen3-Next

> [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) — 2025.05。Qwen3-Next 见[官方博客](https://www.alibabacloud.com/blog/602580)，2025.09。

- Qwen3 的块相对 Qwen2 只做了两处干净的改动：去掉 QKV bias，加上 QK-Norm。MoE（235B / 22B、30B / 3B）是 128 选 8，并且拿掉了 Qwen2.5-MoE 的共享专家
- 这篇报告要证明的是思考模式和非思考模式放进同一个模型，再用旗舰蒸馏小模型
- Qwen3-Next（80B / 3B）才换块：Gated DeltaNet 与带输出门的标准注意力按 3 : 1 混合，MoE 激活比降到约 1 : 50

两篇不要讲成同一件架构创新。[Qwen3](13-qwen3.md) 和 [Qwen3-Next](14-qwen3-next.md) 各自写了机制，对照见 [架构面试提纲](08-interview.md)。
