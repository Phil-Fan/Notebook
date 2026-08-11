# ToolAlpaca

「通用工具学习」数据集：用多智能体模拟，仅花 3,000 条合成样本就让中小模型学会调用 400 种工具，重点验证**泛化到未见工具**的能力。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2023-06（arXiv），EMNLP 2023 Findings |
| 论文 | [ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases](https://arxiv.org/abs/2306.05301)（Tang et al.） |
| 代码 | [tangqiaoyu/ToolAlpaca（GitHub）](https://github.com/tangqiaoyu/ToolAlpaca) |

## Bench 结构

严格说 ToolAlpaca 是**训练语料 + 评测集**一体，而非纯 leaderboard 基准：

- **工具池**：400 个真实工具 API（从公开工具库收集，含文档描述）。
- **数据生成**：模拟两个角色——「tool master」（精通工具的助手）与「user simulator」（模拟用户），围绕随机抽取的工具展开对话，产出约 3,000 条高质量工具使用实例（单工具 + 多工具组合）。
- **评测设置**：训练与测试工具**不重叠**，考察 zero-shot 泛化到新工具；指标为工具调用的 accuracy / F1（是否选对工具、参数是否正确、是否知道何时不调用）。

## 重点测试能力

- **工具泛化**：核心卖点——只见过少量工具即可迁移到全新 API（类比「学会用一种订票软件就会用所有订票软件」）。
- **小模型工具化**：论文证明 LLaMA-7B 级模型微调后可接近 GPT-3.5 的工具调用水平，说明数据质量 > 数据规模。
- **调用时机判断**：区分「需要工具」与「直接回答」。

!!! note "与 ToolBench / API-Bank 的关系"
    ToolBench 是大规模评测（16k API），API-Bank 是分级对话评测，ToolAlpaca 则回答「最少需要多少数据才能学会用工具」——三者互补，常被一起引用。

## 举例

```text
模拟对话（工具: currency_converter）:
  User simulator: "How much is 200 euros in Japanese yen?"
  Tool master: [call currency_converter(amount=200,
                 from_currency="EUR", to_currency="JPY")]
  → 返回结果后组织自然语言回答。

评测时换成训练中没见过的工具（如 flight_search），
模型需仅凭文档描述完成同样的调用流程。
```

## 参考

- [arXiv 2306.05301 — ToolAlpaca](https://arxiv.org/abs/2306.05301)
- [tangqiaoyu/ToolAlpaca](https://github.com/tangqiaoyu/ToolAlpaca)
- [OpenDataLab ToolAlpaca](https://opendatalab.com/OpenDataLab/ToolAlpaca)
