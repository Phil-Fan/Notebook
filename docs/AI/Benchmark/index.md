# Benchmark 总览

LLM / Agent 常见评测基准（benchmark）速查。每个 benchmark 一个文件，统一按「发行时间与论文 → 结构 → 重点测试能力 → 举例」组织。

## 能力矩阵

| 能力维度 | Benchmark | 一句话定位 |
|----------|-----------|------------|
| 数学推理 | [GSM8K](01-gsm8k.md) | 小学数学应用题，链式推理 |
| 知识广度 | [MMLU](02-mmlu.md) | 57 学科四选一，多任务知识 |
| 代码生成 | [HumanEval](03-humaneval.md) | 164 道手写 Python 函数题 |
| 软件工程 | [SWE-bench](04-swebench.md) | 真实 GitHub Issue → patch |
| 工具调用 | [ToolBench](05-toolbench.md) | 16000+ 真实 REST API |
| 函数调用 | [BFCL](06-bfcl.md) | 函数调用准确性 / 多轮状态跟踪 |
| 通用 Agent | [GAIA](07-gaia.md) | 需要工具组合的问答题 |
| 终端 Agent | [Terminal-Bench](08-terminal-bench.md) | 真实命令行环境任务 |
| 工具调用 | [API-Bank](09-apibank.md) | 对话式三级工具调用（调用 / 检索 / 规划） |
| 工具调用 | [ToolAlpaca](10-toolalpaca.md) | 3000 条合成数据，测工具泛化 |
| 多跳问答 | [HotpotQA](11-hotpotqa.md) | 跨维基百科文章的多跳推理 |
| 浏览 Agent | [BrowseComp](12-browsecomp.md) | 深度网络浏览（deep research） |

## 选型建议

- **评基座模型**：MMLU（知识）+ GSM8K（推理）+ HumanEval（代码）是经典三件套。
- **评 Agent 框架 / 工具链**：API-Bank（分级诊断）→ BFCL（单点函数调用）→ ToolBench（大规模 API）→ GAIA（端到端）逐级加难；小模型工具化训练参考 ToolAlpaca。
- **评 Coding Agent**：HumanEval（函数级）→ SWE-bench（仓库级）→ Terminal-Bench（环境级）。
- **评检索 / 研究能力**：HotpotQA（多跳 RAG）→ BrowseComp（深度浏览）。

!!! note "与 Agents/03-benchmark 的关系"
    `AI/Agents/03-benchmark.md` 有 SWE-bench 系列的深入笔记（数据格式、sb-cli 提交流程、SWE-bench Pro 等），本目录的 [04-swebench.md](04-swebench.md) 只作概览并指向该文。

## 其他值得了解的 benchmark

| 类别 | Benchmark | 简介 |
|------|-----------|------|
| 数学 | MATH | 竞赛级数学，7500 题，GSM8K 的进阶版 |
| 数学 | AIME 2024/2025 | 奥数邀请赛题，前沿模型区分度高 |
| 推理 | ARC | 小学科学选择题，Easy / Challenge 两档 |
| 推理 | BBH (BIG-Bench Hard) | 23 个 BIG-Bench 中模型表现差的任务 |
| 推理 | HellaSwag | 常识性句子补全 |
| 代码 | MBPP | 974 道入门级 Python 题，比 HumanEval 简单 |
| 代码 | LiveCodeBench | 持续采集新题，防数据污染 |
| Agent | AgentBench | 8 个环境（OS / DB / 知识图谱等）综合评测 |
| Agent | TAU-bench | 客服场景工具 - 用户交互，含用户模拟器 |
| 多模态 | MMMU | 大学级多模态多学科理解 |

## 参考

- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [LMSYS Chatbot Arena](https://lmarena.ai/)
- [Hugging Face Datasets](https://huggingface.co/datasets)
