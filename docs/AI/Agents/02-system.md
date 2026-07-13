# Agent 工程体系

Agent 系统可以拆成三层：模型层负责生成决策，运行时层负责把决策变成可控执行，产品层负责权限、体验、成本和评测。

## 架构分层

```text
User goal
  ↓
Planner / policy model
  ↓
Agent state ── memory ── retrieval
  ↓
Tool router ── permission ── sandbox
  ↓
Environment / APIs / browser / shell
  ↓
Verifier / evaluator
  ↓
Final answer or next action
```

## Agent loop 设计

| 组件 | 关键问题 | 实现要点 |
|------|----------|----------|
| Planner | 下一步做什么 | ReAct、plan-and-execute、graph state |
| Executor | 动作如何落地 | tool calling、shell、browser、API client |
| Observer | 如何读取反馈 | 结构化结果、错误码、日志摘要 |
| Controller | 何时继续或停止 | step budget、success check、human approval |
| Verifier | 结果是否可靠 | tests、rubric、reference check、self-consistency |

## 工具系统

工具是 Agent 连接外部世界的接口。一个好工具应当具备：

- 明确的名称和职责边界。
- JSON schema 或等价参数规范。
- 可预测的返回结构。
- 错误信息可被模型理解。
- 权限范围最小化。
- 可审计日志。

工具粒度不要过细，也不要过粗：

- 过细：模型需要在大量低级步骤中规划，容易出错。
- 过粗：工具像黑盒，难以组合和恢复。
- 合理：一个工具完成一个稳定业务动作，例如 `search_docs`、`run_tests`、`create_calendar_event`。

## 记忆与上下文

| 类型 | 生命周期 | 用途 |
|------|----------|------|
| Working memory | 单次任务内 | 当前计划、工具结果、中间结论 |
| Episodic memory | 多次任务 | 历史偏好、项目经验、失败案例 |
| Semantic memory | 长期知识 | 文档、知识库、向量检索 |
| Procedural memory | 可复用流程 | 技能、prompt、脚本、playbook |

记忆不是越多越好。生产系统中更重要的是：

- 记录来源，避免污染。
- 支持遗忘和覆盖。
- 区分事实、偏好和推断。
- 在使用记忆前检索相关性。

## 多智能体

多智能体系统把复杂任务拆成多个角色或子流程。

常见模式：

| 模式 | 说明 | 风险 |
|------|------|------|
| Supervisor-worker | 一个主管分派任务，多个 worker 执行 | 主管瓶颈、任务拆分错误 |
| Debate | 多个 agent 给出不同方案，再仲裁 | 成本高，可能制造无效分歧 |
| Pipeline | 研究、实现、测试、评审串联 | 上游错误会传递 |
| Swarm | 多个 agent 并行探索 | 状态同步和冲突处理复杂 |

工程上应优先明确文件、数据或职责的所有权，避免多个 agent 修改同一对象。

## 权限与安全

Agent 能调用工具后，安全边界比普通聊天更重要。

最低要求：

- 默认只读，写操作需要显式授权。
- 高风险工具分级，例如网络、支付、邮件、删除文件。
- 执行环境隔离，例如 Docker、E2B、浏览器沙箱。
- 日志可回放，记录输入、动作、输出和审批。
- 外部内容视为不可信，防 prompt injection。

## 评测

Agent 评测不只看最终答案，还要看过程。

| 指标 | 含义 |
|------|------|
| Task success | 是否完成用户目标 |
| Step efficiency | 工具调用次数、耗时、token 成本 |
| Robustness | 网络失败、工具错误、上下文缺失时能否恢复 |
| Safety | 是否越权、泄露隐私、执行危险动作 |
| Trajectory quality | 计划是否合理，是否有无效循环 |
| Human effort | 需要多少人工确认和修正 |

可以结合 [Rubric](../LLM/Sci/04-Rubric.md) 对最终结果和轨迹打分。

## 框架选择

| 需求 | 倾向选择 |
|------|----------|
| 快速写工具调用 Agent | smolagents、Pydantic AI、OpenAI Agents SDK |
| 复杂状态机和长流程 | LangGraph |
| 多智能体对话与协作 | AutoGen、CrewAI |
| Claude Code / Codex 类编码 Agent 学习 | learn-claude-code、OpenHands、Aider |
| 实时语音 Agent | Pipecat |
| 本地轻量 harness | learn-claude-code、shell 脚本、LangGraph minimal graph |

## 参考资料

- [Hugging Face smolagents documentation](https://huggingface.co/docs/smolagents/index)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
- [Microsoft AutoGen](https://github.com/microsoft/autogen)
- [Pipecat](https://github.com/pipecat-ai/pipecat)
- [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
