# Agent 基础

Agent 是“LLM + 状态 + 工具 + 控制循环”的组合。LLM 负责语言理解、推理和策略选择；Agent runtime 负责保存状态、调用工具、执行权限控制、处理错误和决定何时停止。

## 基本抽象

| 抽象 | 作用 |
|------|------|
| Goal | 用户给出的目标或系统拆出的子任务 |
| State | 当前上下文、工具结果、中间产物和约束 |
| Policy | 由 LLM 或规则决定下一步动作 |
| Tool | 可被调用的外部能力，如搜索、代码执行、文件读写 |
| Observation | 工具执行后的返回结果 |
| Memory | 跨步骤或跨会话保存的信息 |
| Verifier | 判断动作或最终答案是否满足要求 |

## 主循环

最小 Agent loop：

```text
while not done:
    observe current state
    decide next action
    execute tool or produce answer
    append observation to state
    check stop condition
```

工程实现中通常要加入：

- 最大步数，避免无限循环。
- 工具白名单和权限确认。
- 结构化输出解析，降低工具调用失败率。
- 错误恢复策略，例如重试、降级、请求人类确认。
- 轨迹日志，便于调试和评测。

## ReAct：推理与行动交替

论文 [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)

ReAct 把 reasoning trace 和 action trace 交错组织：

```text
Thought: 我需要查找最新信息。
Action: search("...")
Observation: 搜索结果 ...
Thought: 现在可以综合答案。
Final: ...
```

它解决的问题是：纯 chain-of-thought 容易闭门造车，纯 action-only 又缺少中间推理解释。ReAct 让模型边思考边使用外部环境。

## Tool calling

现代 Agent 框架通常用结构化 tool calling 替代自由文本 action：

```json
{
  "tool": "search",
  "arguments": {
    "query": "smolagents CodeAgent ToolCallingAgent"
  }
}
```

好处：

- 参数可验证。
- 工具可按 schema 自动生成说明。
- 返回值可结构化进入下一轮上下文。
- 更容易做权限、审计和回放。

## Workflow 与 Agent 的区别

| 类型 | 特征 | 适用场景 |
|------|------|----------|
| Workflow | 步骤固定，分支有限 | ETL、报告生成、固定审批流 |
| Agent | 步骤由模型动态决定 | 搜索研究、代码修复、网页操作 |
| Hybrid | 外层 workflow，局部使用 agent | 生产系统中最常见 |

!!! note "工程经验"
    能用 workflow 解决的部分优先 workflow 化；真正不确定、需要探索和决策的部分再交给 Agent。

## 常见失败模式

- 目标漂移：执行多步后忘记原始任务。
- 工具幻觉：编造不存在的工具或参数。
- 观察误读：没有正确理解工具返回值。
- 过度探索：一直搜索和计划，不交付结果。
- 权限越界：执行用户未授权的外部操作。
- 奖励投机：只迎合 rubric 表面指标。

## 参考资料

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
