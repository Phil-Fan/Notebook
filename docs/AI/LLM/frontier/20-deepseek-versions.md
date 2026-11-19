# DeepSeek 版本时间线

> 核对时间 2026-11-19。日期优先取官方发布说明（[API Change Log](https://api-docs.deepseek.com/updates)）与 Hugging Face 仓库创建时间；论文日期和产品上线日不一致时取产品日。

DeepSeek 的「版本」要分三层看：**V 系列**是基座与对话主线，**R 系列**是推理专线，其余是数学、代码、视觉、OCR 这类专项模型。三条线不是并列的：R 线在 2025 年秋并入 [V3.1](10-deepseek-v3.md) 的 thinking 模式，之后不再单独发版；V 线则从 V2 走到 [V4](12-deepseek-v4.md)，再分出 V4.1。结构细节看 [V2](09-deepseek-v2.md)、[V3](10-deepseek-v3.md)、[V3.2](11-deepseek-v32.md)、[V4](12-deepseek-v4.md) 四篇，这里只排时间。

## 主线：V 系列

| 版本 | 日期 | 状态 | 关键改动 |
|------|------|------|----------|
| DeepSeek-LLM 7B / 67B | 2023-11-29 | 已下线 | 首个公开模型，沿用 Llama 架构 |
| DeepSeek-Coder 1.3B / 6.7B / 33B | 2023-11 | 已下线 | 代码专用，分出 base / instruct |
| DeepSeek-MoE 16B | 2024-01-09 | 已下线 | 细粒度专家 + 共享专家，后面整条 MoE 线的起点 |
| **DeepSeek-V2** | 2024-05 | 已下线 | MLA + DeepSeekMoE；236B 总参数 / 21B 激活 |
| DeepSeek-V2-Lite / V2-Chat | 2024-05 | 已下线 | 小尺寸与对话版 |
| DeepSeek-Coder-V2 | 2024-06 | 已下线 | 代码分支，base / instruct / Lite |
| DeepSeek-V2.5 | 2024-09-05 | 已下线 | 合并 Coder 与 Chat 后的通用版 |
| DeepSeek-V2.5-1210 | 2024-12-10 | 已下线 | 滚动更新，MATH-500 74.8 → 82.8 |
| **DeepSeek-V3** | 2024-12-26 | 维护中 | 671B / 37B；无辅助损失负载均衡、MTP、FP8 |
| DeepSeek-V3-0324 | 2025-03-24 | 已被取代 | 只重做后训练 |
| DeepSeek-V3.1 | 2025-08-21 | 已被取代 | 混合思考 + 非思考模式；在 V3 上多训 800B tokens |
| DeepSeek-V3.1-Terminus | 2025-09-22 | 已被取代 | 修中英混排与异常字符，优化 Code / Search Agent |
| DeepSeek-V3.2-Exp | 2025-09-29 | 已被取代 | 首次把 DSA 续训进 MLA，API 同时降价 |
| **DeepSeek-V3.2** | 2025-12-01 | 维护中 | DSA 正式版 |
| DeepSeek-V3.2-Speciale | 2025-12-01 | 实验到期 | 纯推理变体，临时端点，不支持工具调用 |
| **DeepSeek-V4**（预览） | 2026-04-24 | 已被 GA 取代 | V4-Pro 1.6T / 49B、V4-Flash 284B / 13B；1M 上下文、CSA / HCA、mHC、Muon |
| DeepSeek-V4-Flash-0731 | 2026-07-31 | 已退役 | Flash 正式版，架构与预览一致，只重做后训练 |
| DeepSeek-V4-Pro-0813 | 2026-08-13 | 维护中 | Pro 正式版；原生 Responses API，思考力度分 low / high / max |
| DeepSeek-V4-Flash-Vision-Exp | 2026-08-21 | 已退役 | 多模态视觉理解实验版 |
| **DeepSeek-V4.1-Flash** | 2026-09-10 | 已被取代 | 换架构：带因果 encoder 的 encoder-decoder，原生多模态 |
| DeepSeek-V4.1-Flash-1017 | 2026-10-17 | 当前线上 | 同一架构的新 checkpoint，`deepseek-flash` 指向它 |

## 推理线：R 系列

| 版本 | 日期 | 说明 |
|------|------|------|
| DeepSeek-R1-Lite-Preview | 2024-11-20 | 仅 API 与网页，预览 |
| **DeepSeek-R1-Zero** | 2025-01-20 | 纯 RL、不做 SFT 冷启动，MIT |
| **DeepSeek-R1** | 2025-01-20 | 从 V3-Base 初始化，MIT |
| R1 蒸馏系列 | 2025-01-20 | Qwen 1.5B / 7B / 14B / 32B，Llama 8B / 70B |
| DeepSeek-R1-0528 | 2025-05-28 | 最后一代独立 R 模型；AIME 2025 70.0 → 87.5 |
| DeepSeek-R1-0528-Qwen3-8B | 2025-05-29 | 用 R1-0528 蒸馏的 Qwen3 基座 |

2025-08-21 之后 R 线收束：推理能力改由 V3.1 / V3.2 的 thinking 模式提供，**没有 R2**。

## 专项模型

| 模型 | 日期 | 方向 |
|------|------|------|
| DeepSeek-Math 7B（base / instruct / rl） | 2024-02 | 数学；GRPO 的出处 |
| DeepSeek-VL 1.3B / 7B | 2024-03 | 视觉语言理解 |
| DeepSeek-Prover-V1 | 2024-08 | 定理证明 |
| DeepSeek-Prover-V1.5（base / sft / rl） | 2024-08 | 定理证明 |
| Janus 1.3B | 2024-10 | 统一多模态理解与生成 |
| JanusFlow 1.3B | 2024-11 | 同上，流匹配版本 |
| DeepSeek-VL2 tiny / small | 2024-12 | 视觉语言理解，MoE |
| Janus-Pro 1B / 7B | 2025-01-26 | 多模态生成 |
| DeepSeek-Prover-V2 671B / 7B | 2025-04-30 | 定理证明，挂 V3 骨干 |
| DeepSeek-OCR | 2025-10-17 | 文档解析 |
| DeepSeek-Math-V2 | 2025-11-27 | 数学，Apache-2.0 |
| DeepSeek-OCR-2 | 2026-01-27 | 文档解析 |

## API 模型名（只是别名，不是版本）

API 上暴露的名字长期只有两个，背后换过很多次权重：

| 时间 | 模型名 | 实际指向 |
|------|--------|----------|
| 2024-12-26 | `deepseek-chat` | V3 |
| 2025-01-20 | `deepseek-reasoner` | R1 |
| 2025-03-24 | `deepseek-chat` | V3-0324 |
| 2025-05-28 | `deepseek-reasoner` | R1-0528 |
| 2025-08-21 | 两个名字 | V3.1 的非思考 / 思考模式 |
| 2025-09-22 | 两个名字 | V3.1-Terminus |
| 2025-09-29 | 两个名字 | V3.2-Exp |
| 2025-12-01 | 两个名字 | V3.2 |
| 2026-04-24 | `deepseek-v4-pro` / `deepseek-v4-flash` | V4 预览；旧名分别转 V4-Flash 的非思考 / 思考模式 |
| 2026-07-24 | —— | `deepseek-chat` / `deepseek-reasoner` 下线 |
| 2026-07-31 | `deepseek-v4-flash` | V4-Flash-0731 |
| 2026-09-10 | `deepseek-flash` | V4.1-Flash；`deepseek-v4-flash` 兼容转发 |
| 2026-10-17 | `deepseek-flash` | V4.1-Flash-1017 |

App 与网页端不带版本号，自动跟随 `deepseek-flash` 对应的权重。

## 哪些东西不是「版本」

- **NSA**（2025-02）是稀疏注意力层的研究论文，不是 checkpoint，见 [05-NSA.md](../现代模型架构/05-NSA.md)。
- **mHC**（2025-12）是残差连接的论文，被 [V4](12-deepseek-v4.md) 采用，本身不构成一个模型。
- **DSpark / dflash / eagle3**（2026-06 起，Hugging Face 上的一批小仓库）是推测解码的草稿模型，服务于主线模型，不是新代际。
- **V4-Flash / V4-Pro 的 DSpark 包**（2026-06-27）同样是解码加速件，不是 V4 的新版本。

## 主干代际速查

| 代际 | 总参数 | 每 token 激活 | 上下文 | 结构关键词 |
|------|--------|---------------|--------|------------|
| V2 | 236B | 21B | 128k | MLA、细粒度 MoE + 共享专家 |
| V3 | 671B | 37B | 128k | 同上，加无辅助损失均衡、MTP、FP8 |
| V3.2 | 沿用 V3 量级 | 沿用 V3 | 128k | DSA |
| V4-Pro | 1.6T | 49B | 1M | CSA + HCA、mHC、Muon |
| V4-Flash | 284B | 13B | 1M | 同上，层数与专家数更小 |
| V4.1-Flash | 未公开 | 未公开 | 未公开 | 因果 encoder-decoder、原生多模态 |

## 参考

- [DeepSeek API Change Log](https://api-docs.deepseek.com/updates)：历次 API 升级与模型名变更的官方口径
- [DeepSeek-V4 发布说明](https://api-docs.deepseek.com/news/news260424)、[V4-Flash 0731](https://api-docs.deepseek.com/news/news260731)、[V4-Pro 0813](https://api-docs.deepseek.com/news/news260813)
- [DeepSeek-V4.1-Flash](https://api-docs.deepseek.com/news/news260910)、[V4.1-Flash-1017](https://api-docs.deepseek.com/news/news261017)
- [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)：当前在线模型与价格
- [deepseek-ai @ Hugging Face](https://huggingface.co/deepseek-ai)：权重仓库与创建日期
- [DeepSeek - Wikipedia](https://en.wikipedia.org/wiki/DeepSeek)：版本对照表，本页日期与其交叉核对
