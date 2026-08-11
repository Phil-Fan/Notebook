# Agent 一轮回复详解

以 OpenAI Chat Completions API 格式为例，拆解 Agent 一次完整 tool call 循环中每个阶段的数据结构和流转。

## 整体流程

```text
用户输入
  ↓
┌─────────────────────────────────────────────┐
│ STEP A  组装请求 messages + tools           │
│          → 发给 LLM                         │
├─────────────────────────────────────────────┤
│ STEP B  模型返回 assistant message           │
│          finish_reason = tool_calls | stop  │
├─────────────────────────────────────────────┤
│ STEP C  框架解析 tool_calls → 执行本地工具   │
│          → 拼装 role=tool 结果               │
├─────────────────────────────────────────────┤
│ STEP D  把工具结果追加进 history → 再请求     │
│          → 模型返回最终回复                   │
└─────────────────────────────────────────────┘
  ↓
返回用户（或继续循环）
```

## STEP A：组装请求

发给模型的请求包含三部分：`messages`、`tools`、`tool_choice`。

### messages

对话历史，按时间顺序排列。每条消息有 `role` 和 `content`。

| role | 说明 |
|------|------|
| `system` | 系统指令，设定 Agent 身份和行为约束 |
| `user` | 用户输入 |
| `assistant` | 模型上一轮输出（含 tool_calls） |
| `tool` | 工具执行结果，通过 `tool_call_id` 关联 |

```json
[
  {
    "role": "system",
    "content": "You are an airline customer-service agent. When you need reservation data, call the tool. Do not invent reservation details."
  },
  {
    "role": "user",
    "content": "Hi, I need to cancel my reservation EHGLP3. Please look it up first."
  }
]
```

### tools

工具声明，告诉模型有哪些函数可调用、参数格式是什么。

```json
[
  {
    "type": "function",
    "function": {
      "name": "get_reservation_details",
      "description": "Get the details of a reservation by its ID.",
      "parameters": {
        "type": "object",
        "properties": {
          "reservation_id": {
            "type": "string",
            "description": "The reservation ID, e.g. 'EHGLP3'."
          }
        },
        "required": ["reservation_id"]
      }
    }
  }
]
```

字段说明：

| 字段 | 说明 |
|------|------|
| `type` | 固定 `"function"` |
| `function.name` | 函数名，模型调用时使用 |
| `function.description` | 函数描述，模型据此判断何时调用 |
| `function.parameters` | JSON Schema，定义参数类型和约束 |

### tool_choice

控制模型是否调用工具：

| 值 | 行为 |
|----|------|
| `"auto"` | 模型自行决定是否调用（默认） |
| `"none"` | 禁止调用工具 |
| `"required"` | 必须调用至少一个工具 |
| `{"type": "function", "function": {"name": "xxx"}}` | 强制调用指定函数 |

## STEP B：模型返回

模型返回一个 completion 对象，关键字段：

### 顶层字段

| 字段 | 说明 |
|------|------|
| `id` | 请求唯一标识 |
| `model` | 实际使用的模型 |
| `object` | `"chat.completion"` |
| `choices` | 候选回复列表（通常只有 1 个） |
| `usage` | token 统计 |

### choices[0] 关键字段

| 字段 | 说明 |
|------|------|
| `finish_reason` | `"tool_calls"` 表示本轮以工具调用结束；`"stop"` 表示以文本结束 |
| `message.role` | 固定 `"assistant"` |
| `message.content` | 模型对用户的文本回复。调工具时通常为空字符串 `""` |
| `message.tool_calls` | 工具调用列表，每项包含 `id`、`name`、`arguments` |
| `message.reasoning_content` | 模型内部思考过程（thinking），不进入下一轮上下文 |

### 实际输出示例（调工具轮）

```json
{
  "role": "assistant",
  "content": "",
  "tool_calls": [
    {
      "id": "call_03a56923d120409d889dd150",
      "type": "function",
      "function": {
        "name": "get_reservation_details",
        "arguments": "{\"reservation_id\": \"EHGLP3\"}"
      }
    }
  ],
  "reasoning_content": "Thinking Process:\n1. Identify User Intent: ..."
}
```

要点：

- `content` 为空 — 模型选择"只调工具、不说话"。
- `arguments` 是 **JSON 字符串**（不是对象），框架需要 `json.loads()` 解析。
- `reasoning_content` 是模型的思考链，由模型生成，但**默认不进入下一轮 messages**。
- `tool_calls` 也是模型生成的，不是框架编的。

### 实际输出示例（最终回复轮）

```json
{
  "role": "assistant",
  "content": "I've found your reservation. Here are the details:\n\n**Reservation ID:** EHGLP3\n...",
  "tool_calls": null,
  "reasoning_content": "The user wants to cancel reservation EHGLP3..."
}
```

`finish_reason = "stop"`，`tool_calls` 为 null，`content` 包含对用户的自然语言回复。

### usage 字段

```json
{
  "completion_tokens": 221,
  "prompt_tokens": 336,
  "total_tokens": 557,
  "completion_tokens_details": {
    "reasoning_tokens": 186,
    "text_tokens": 221
  },
  "prompt_tokens_details": {
    "text_tokens": 336
  }
}
```

| 字段 | 说明 |
|------|------|
| `prompt_tokens` | 输入 token（system + history + tools schema） |
| `completion_tokens` | 输出 token（含 reasoning + text + tool_calls） |
| `reasoning_tokens` | 思考过程消耗的 token |
| `text_tokens` | 实际文本输出 token |

## STEP C：框架执行工具

框架从 `message.tool_calls` 中提取调用信息：

```text
tool_calls[0]:
  id:   call_03a56923d120409d889dd150
  name: get_reservation_details
  arguments (raw): '{"reservation_id": "EHGLP3"}'
  arguments (parsed): {"reservation_id": "EHGLP3"}
```

框架执行本地工具函数，得到结果：

```json
{
  "reservation_id": "EHGLP3",
  "user_id": "emma_kim_9957",
  "origin": "PHX",
  "destination": "JFK",
  "cabin": "basic_economy",
  "flight_type": "one_way",
  "flights": [
    {"flight_number": "HAT156", "date": "2024-05-17", "origin": "PHX", "destination": "SEA"},
    {"flight_number": "HAT021", "date": "2024-05-17", "origin": "SEA", "destination": "JFK"}
  ],
  "insurance": "no"
}
```

**注意**：工具函数的执行结果是确定性的程序输出，不是模型生成的。

## STEP D：第二轮请求

框架把 assistant 的 tool_calls 和 tool 结果追加进 history，再次请求模型：

```json
[
  {
    "role": "assistant",
    "content": "",
    "tool_calls": [
      {
        "id": "call_03a56923d120409d889dd150",
        "type": "function",
        "function": {
          "name": "get_reservation_details",
          "arguments": "{\"reservation_id\": \"EHGLP3\"}"
        }
      }
    ]
  },
  {
    "role": "tool",
    "tool_call_id": "call_03a56923d120409d889dd150",
    "content": "{\"reservation_id\": \"EHGLP3\", ...}"
  }
]
```

| 字段 | 说明 |
|------|------|
| `role: "assistant"` + `tool_calls` | 原样回传模型上一轮的输出 |
| `role: "tool"` | 工具执行结果 |
| `tool_call_id` | 关联到对应的 tool_call，模型据此知道哪个调用返回了什么 |

模型收到后生成最终回复（`finish_reason = "stop"`），循环结束。

## 数据流归属

一轮完整 tool call 中，各部分数据的**生成者**不同：

| 数据 | 谁生成的 |
|------|----------|
| `messages`（system / user） | 开发者 / 用户 |
| `tools` schema | 开发者定义 |
| `reasoning_content` | **模型生成**（思考过程） |
| `tool_calls`（name + arguments） | **模型生成**（决策） |
| `content`（assistant 文本） | **模型生成**（回复） |
| 工具函数执行结果 | **框架 / 程序执行**（确定性输出） |
| `role: "tool"` message | 框架拼装 |
| `usage` | API 返回的统计 |

## 其他请求参数

Chat Completions API 常用参数：

| 参数 | 说明 |
|------|------|
| `model` | 模型标识，如 `gpt-4o`、`qwen3.6-plus` |
| `messages` | 对话历史 |
| `tools` | 工具声明列表 |
| `tool_choice` | 工具调用策略（auto / none / required / 指定函数） |
| `temperature` | 采样温度，0 = 确定性，越高越随机 |
| `max_tokens` | 最大输出 token 数 |
| `stream` | 是否流式返回（SSE） |
| `stop` | 停止序列 |
| `response_format` | 强制输出格式，如 `{"type": "json_object"}` |
| `parallel_tool_calls` | 是否允许一轮中并行调用多个工具 |

## 多轮循环终止条件

Agent loop 在以下情况停止：

- `finish_reason = "stop"`：模型选择直接回复，不调工具。
- 达到最大步数限制。
- 工具执行出错且无法恢复。
- 框架判定任务已完成（verifier 通过）。

## 参考资料

- [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [SWE-bench 评测](03-benchmark.md)
