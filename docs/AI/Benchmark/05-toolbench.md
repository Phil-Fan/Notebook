# ToolBench

清华 & OpenBMB 随 ToolLLM 发布的大规模真实 API 工具调用基准：16,000+ 个 RapidAPI 真实 REST API 上的指令跟随与多工具协作。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2023-07（arXiv），ICLR 2024 spotlight |
| 论文 | [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789)（Qin et al.） |
| 代码 | [OpenBMB/ToolBench（GitHub）](https://github.com/OpenBMB/ToolBench) |

## Bench 结构

整套工作分三部分：**数据构建 → 训练（ToolLLaMA）→ 评测（ToolEval）**。

### 数据：ToolBench 指令集

- **API 池**：从 RapidAPI 平台爬取 49 个类别、16,464 个真实 REST API（含文档、参数 schema）。
- **指令**：用 ChatGPT 基于 API 文档生成约 34,512 条自然语言指令，分三档：

    | 档位 | 说明 |
    |------|------|
    | I1-Inst | 单工具、单步指令 |
    | I1-Tool | 单工具、可能多步（需探索 API 内多个端点） |
    | I2-Cat / I3-Inst | 跨类别 / 跨工具的多工具协作指令 |

### 求解：DFSDT

提出 **DFSDT（Depth-First Search-based Decision Tree）**：把工具调用决策展开成树，允许模型探索多条推理路径并回溯，替代单链 CoT，显著提升复杂指令成功率。

### 评测：ToolEval

- **自动评估器**：用 ChatGPT 作 judge，对比两条解答：
  - **Pass Rate**：能否成功执行到最终答案；
  - **Win Rate**：两条可行解的偏好对比（结合执行效率与合理性）。
- 与人工评估一致性约 87%。

## 重点测试能力

- **大规模工具选择**：从上千个候选 API 中挑对工具（检索 + 选择）。
- **API 文档理解与参数填充**：真实 schema 常有噪声、缺文档，考验鲁棒性。
- **多工具编排**：跨 API 的依赖规划（如「查天气 → 换算货币 → 生成报告」）。
- **错误恢复**：API 报错、限流时的重试与换路。

!!! note "现状"
    ToolBench 是 2023 年工具调用评测的代表，后续被 BFCL（更严格的确定性评测）、τ-bench 等补充。其 API 依赖 RapidAPI 在线服务，部分端点已失效，复现需注意。

## 举例

```text
指令（I2-Cat，跨类别）:
  "I'm planning a trip to Paris next week. Can you check the weather
   there and convert 500 USD to EUR for my budget?"

期望调用链:
  weather_api.get_forecast(city="Paris")
  → currency_api.convert(amount=500, from="USD", to="EUR")
  → 汇总成自然语言回答
```

## 参考

- [arXiv 2307.16789 — ToolLLM](https://arxiv.org/abs/2307.16789)
- [OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench)
- [ToolEval Leaderboard](https://openbmb.github.io/ToolBench/)
