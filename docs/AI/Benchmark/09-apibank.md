# API-Bank

阿里达摩院提出的工具增强 LLM 基准：以**多轮对话**为载体，分三级考察模型调用 API 的能力，是 2023 年工具调用评测的代表作之一。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2023-04（arXiv），EMNLP 2023 |
| 论文 | [API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs](https://arxiv.org/abs/2304.08244)（Li et al., Alibaba DAMO） |
| 代码 | [AlibabaResearch/DAMO-ConvAI（GitHub）](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank) |

## Bench 结构

- **规模**：53 个 API、2,138 段对话、7,517 条标注样本；API 文档由 GPT-3 辅助生成，对话数据众包标注。
- **三级难度**（核心设计）：

    | 级别 | 能力 | 内容 |
    |------|------|------|
    | Level-1 | API Call | 单步调用：根据用户请求选对 API 并填参（73 个 tool-use API、314 段对话） |
    | Level-2 | Retrieval + Call | 先**检索**出相关 API（从更大候选池，264 个 API），再调用（1,208 段对话） |
    | Level-3 | Planning | 多步规划：把复杂目标拆成 API 调用序列（61 段对话） |

- **交互形式**：模型扮演 assistant，与用户（及 API 执行结果）多轮交互；调用格式为特殊 token 包裹的 `API_NAME(param=...)`。
- **评测指标**：每级 accuracy——调用正确（API 名 + 参数精确匹配）才算通过。

## 重点测试能力

- **对话中的工具触发时机**：何时该调 API、何时直接回答（避免过度调用）。
- **API 检索**：Level-2 考察从大量候选中按文档语义匹配工具。
- **多步规划**：Level-3 考察任务分解与调用顺序。
- **参数依赖跟踪**：后一步调用的参数常来自前一步的返回值。

!!! note "定位"
    相比 ToolBench（万级 API、开放式求解），API-Bank 规模小但**分级清晰、可复现**，适合诊断模型工具能力的短板在哪一级。论文同时给出 tool-augmented 训练方案（用 Level-1/2 数据微调）验证了数据有效性。

## 举例

```text
Level-1 对话:
  User: What's the weather in Shanghai tomorrow?
  Assistant: [Call WeatherAPI(city="Shanghai", date="tomorrow")]
  API return: {"weather": "rainy", "temp": 18}
  Assistant: Tomorrow in Shanghai will be rainy, about 18°C.

Level-3 示例:
  User: "帮我订一张明天北京到上海的高铁票，靠窗。"
  → 查询车次 → 检查余票 → 创建订单 → 确认支付，多步串联。
```

## 参考

- [arXiv 2304.08244 — API-Bank](https://arxiv.org/abs/2304.08244)
- [ACL Anthology（EMNLP 2023）](https://aclanthology.org/2023.emnlp-main.187/)
- [AlibabaResearch/DAMO-ConvAI](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank)
