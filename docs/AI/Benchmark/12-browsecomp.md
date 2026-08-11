# BrowseComp

OpenAI 发布的**浏览型 Agent** 基准：题目一句话就能说清，但答案需要深度、持续的网络浏览才能找到——专测 deep research 类系统。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2025-04 |
| 论文 | [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516)（OpenAI，Wei et al.） |
| 官网 | [openai.com/index/browsecomp](https://openai.com/index/browsecomp/) |
| 数据 | HuggingFace [`openai/browsecomp`](https://huggingface.co/datasets/openai/browsecomp) |

## Bench 结构

- **规模**：1,266 道题，由专业写手创作并经多轮校验。
- **题目特点**：
  - **简单陈述、极难回答**——答案在网络上存在，但藏在深处，需要反复搜索、换关键词、交叉验证；
  - **答案唯一且可验证**：短答案（名字、数字等），精确匹配评分，无需 LLM judge；
  - **防污染设计**：题目反向构造（先找冷门事实再写问题），确保答案信息不会出现在主流模型的训练数据中。
- **指标**：accuracy（exact match）。

## 重点测试能力

- **长程浏览策略**：不是「搜一次就出答案」，而是几十上百次搜索的坚持与方向调整。
- **查询重构**：搜索失败后换角度、拆解子问题。
- **信息交叉验证**：从多个冷门来源确认事实，避免被误导。

!!! note "成绩参考"
    发布时 GPT-4o 仅约 9%，而 Deep Research 类系统（o3 + 浏览框架）约 51%，说明差距主要在**浏览策略**而非模型本身。与 GAIA 相比，BrowseComp 更专注「纯浏览深度」，几乎不考文件处理或多模态。

## 举例

```text
题目风格（示意）:
  "Name the film whose director was born in a town that
   was the capital of a country for exactly 12 years,
   and which premiered at a festival in 1997."

特点: 每个子条件都可验证，但组合起来只有极少数
冷门条目满足，需要逐层搜索排除。
```

## 参考

- [arXiv 2504.12516 — BrowseComp](https://arxiv.org/abs/2504.12516)
- [OpenAI — BrowseComp 介绍](https://openai.com/index/browsecomp/)
- [HuggingFace openai/browsecomp](https://huggingface.co/datasets/openai/browsecomp)
