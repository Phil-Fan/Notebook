# BFCL

Berkeley Function-Calling Leaderboard，UC Berkeley Gorilla 团队维护的函数调用（function calling / tool use）专项评测，是目前工业界引用最多的工具调用榜单。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | v1 2024-02；v2 2024-06；v3 2025-02；v4 2025 |
| 论文 | [Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://openreview.net/forum?id=2GmDdhBdDk)（ICML 2025） |
| 榜单 | [gorilla.cs.berkeley.edu/leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) |
| 代码 | [ShishirPatil/gorilla（GitHub）](https://github.com/ShishirPatil/gorilla) |

## Bench 结构

### 版本演进

| 版本 | 重点 |
|------|------|
| v1 | 单轮函数调用：AST 匹配 + 可执行验证 |
| v2 | 加入 Live 数据（真实用户贡献）、相关性检测、Web search / 缺参场景 |
| v3 | **Multi-turn & Multi-step**：多轮对话 + 状态跟踪、缺函数 / 缺参数处理 |
| v4 | 加入 agentic 任务（web search、memory 等），评测更贴近 agent 场景 |

### 评测类别（v3 为例）

- **Simple**：单函数、参数齐全。
- **Multiple**：从多个候选函数中选一个。
- **Parallel**：一次需并行调用多个函数。
- **Parallel Multiple**：并行 + 选择。
- **Java / JavaScript / REST**：跨语言 API 调用。
- **Relevance Detection**：识别「没有合适函数，应拒绝调用」。
- **Multi-turn**：每轮对话后环境状态改变（如执行 `create_file` 后文件系统变化），模型需跟踪状态；还会注入缺函数、缺参数、长上下文等扰动。

### 评测方式

- **AST 评估**：解析生成的函数调用，与 ground truth 比对函数名与参数（可执行参数会真实执行比对返回值）。
- **可执行评估**：直接运行调用，比对程序状态。
- 指标为各类别 accuracy 的加权综合。

## 重点测试能力

- **Schema 遵循**：严格按 JSON schema 生成合法调用（类型、枚举、必填项）。
- **参数抽取与推理**：从自然语言中抽取并转换参数（单位换算、日期格式化等）。
- **状态跟踪**：多轮中记住环境变化，是 v3 的核心区分点。
- **拒答能力**：无可用工具时不幻觉调用。

!!! note "与 ToolBench 的区别"
    ToolBench 侧重「大规模 API + 开放式求解 + LLM judge」；BFCL 侧重「确定性验证 + 细粒度能力拆解」，结果可复现性更强，因此成为模型发布时的常用报告项。

## 举例

```text
可用函数:
  get_weather(location: str, unit: "celsius" | "fahrenheit")

用户: "北京今天多少度？"

期望输出（AST）:
  get_weather(location="Beijing", unit="celsius")

Multi-turn 扰动示例:
  第 2 轮用户说 "把刚才那个文件删掉"，
  但 delete_file 函数本轮被移除 →
  正确行为是报告缺函数，而不是幻觉调用。
```

## 参考

- [BFCL Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- [BFCL v3 博客 — Multi-Turn & Multi-Step](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html)
- [ShishirPatil/gorilla](https://github.com/ShishirPatil/gorilla)
