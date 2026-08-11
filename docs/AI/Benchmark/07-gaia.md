# GAIA

General AI Assistants 基准：一组「人类觉得简单、当前 AI 觉得难」的问答题，要求模型综合运用推理、联网搜索、文件处理等能力。是通用 Agent 的标杆评测。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2023-11（arXiv），ICLR 2024 oral |
| 论文 | [GAIA: a benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)（Mialon et al.，Meta AI / Hugging Face / AutoGPT） |
| 数据 | HuggingFace [`gaia-benchmark/GAIA`](https://huggingface.co/gaia-benchmark)（300 题验证集公开，166 题测试集隐藏） |

## Bench 结构

- **规模**：466 道精心设计的问答题（300 validation + 166 test）。
- **答案形式**：全部是**无歧义的短答案**——一个字符串、数字或列表，可用精确匹配自动评分，无需 LLM judge。
- **难度分级**：

    | Level | 人类准确率 | GPT-4 + 插件（2023） | 所需步骤 |
    |-------|-----------|---------------------|----------|
    | 1 | 92% | 15% | 通常 ≤5 步，用 1 个工具 |
    | 2 | 92% | 6% | 多步、多工具组合 |
    | 3 | 92% | 2% | 长链条规划与工具编排 |

- **附件**：部分题目附带文件（PDF、Excel、图片、音频、zip 等），模型必须解析文件内容才能作答。
- **指标**：exact-match accuracy（对大小写、格式做归一化后精确匹配）。

## 重点测试能力

- **基础能力的组合**：论文的核心洞察——题目只需「推理 + 网页浏览 + 文件处理」等基础能力，但人类轻松（92%）而模型崩掉，说明**能力组合 / 规划**是瓶颈。
- **多步规划与工具编排**：搜索 → 点击 → 提取 → 计算 → 汇总。
- **多模态文件理解**：读表格、听音频、看图表。
- **抗干扰与精确性**：答案必须精确（如「列出所有满足条件的名字」，漏一个即错）。

!!! note "现状"
    GAIA 测试集隐藏、需提交 Hugging Face leaderboard 评分，防污染较好。2025 年头部 agent 系统已达 60%+（如 Trase、Manus 类系统），但距人类 92% 仍有明显差距。

## 举例

```text
Level 1（附附件）:
  "In the attached spreadsheet, which column contains the
   highest value, and what is that value?"
  → 需要解析 Excel、比较数值、按指定格式输出。

Level 3:
  "Find the director of the 1992 film whose lead actor was
   born in 1956 and who was filmed in a city with a population
   under 50,000. What is the director's birth year?"
  → 需要多次搜索、交叉验证、逐层缩小候选。
```

## 参考

- [arXiv 2311.12983 — GAIA](https://arxiv.org/abs/2311.12983)
- [GAIA Leaderboard（Hugging Face）](https://huggingface.co/spaces/gaia-benchmark/leaderboard)
- [GAIA 数据集](https://huggingface.co/gaia-benchmark)
