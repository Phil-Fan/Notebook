# 智能体（Agents）

Agent 原理、工程体系、开源框架与产品形态。

Agent 的核心不是“调用一次大模型”，而是让模型在一个受控运行时中循环完成任务：观察状态、规划下一步、调用工具、读取结果、更新记忆，并在终止条件满足时交付结果。

## 知识地图

| 层次 | 关注问题 | 典型内容 |
|------|----------|----------|
| 模型能力 | LLM 能否理解任务、规划、反思、使用工具 | ReAct、function calling、self-reflection |
| Agent loop | 如何组织观察、思考、行动、反馈 | plan-act-observe、state machine、workflow graph |
| Tool runtime | 工具如何注册、鉴权、执行与回传 | JSON schema、sandbox、browser、shell、RAG |
| Memory / context | 如何保存任务状态与长期知识 | short-term state、episodic memory、vector memory |
| Orchestration | 多步骤和多智能体如何协作 | LangGraph、AutoGen、CrewAI、deepagents |
| Evaluation | 如何判断任务是否完成 | task success、rubric、trajectory eval、human review |
| Safety | 如何限制越权和错误扩散 | permission、policy、least privilege、audit log |

## 目录

| 页面 | 说明 |
|------|------|
| [01-base](01-base.md) | Agent 基础 |
| [02-system](02-system.md) | Agent 工程体系：循环、工具、记忆、权限、评测 |
| [accelerate](accelerate.md) | 加速相关笔记 |
| [开源框架整理](开源框架.md) | 框架 / 产品 / 教程清单 |

框架列表自 Research `Agents/index.md` 迁移，并与本站原有整理合并，见 [开源框架整理](开源框架.md)。
