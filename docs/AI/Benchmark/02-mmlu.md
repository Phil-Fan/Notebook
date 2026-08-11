# MMLU

多学科知识选择题基准，长期是「LLM 知识广度」的代名词，Open LLM Leaderboard 的核心科目之一。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2020-09（arXiv），ICLR 2021 |
| 论文 | [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)（Hendrycks et al., CAIS） |
| 数据 | HuggingFace [`cais/mmlu`](https://huggingface.co/datasets/cais/mmlu) |

## Bench 结构

- **规模**：57 个学科、约 15,908 道四选一选择题（14,042 test + 1,540 val + 285 dev）。
- **学科覆盖**：STEM（数学、物理、计算机等）、人文（历史、法律、哲学等）、社科（经济、心理等）、专业领域（医学、会计、机器学习等），从小学水平到专业从业者水平。
- **格式**：`question` + 4 个 `choices` + `answer`（A/B/C/D 索引）+ `subject`。

```text
Question: The weight percent of sodium hypochlorite in commercial
bleach solutions is typically...
Choices: [ "1%", "5%", "10%", "20%" ]
Answer: 0   # 即 A
```

- **评测指标**：accuracy。惯例报告两种设置：
  - **5-shot**：每科用 5 个 dev 题作 in-context 示例（原论文设置）。
  - **0-shot CoT**：现在 leaderboard 更常用。
- 通常按学科 macro 平均（各科准确率取平均），避免大学科主导。

## 重点测试能力

- **世界知识与事实记忆**：跨学科广度，类似「全科考试」。
- **专业领域理解**：部分题目达到律师、医生执照考试难度。
- 基本不测推理链，是知识型 benchmark 的代表。

!!! note "现状与变体"
    前沿模型 85%+，已近饱和，且被发现有**标注错误与数据污染**。主要变体：

    - **MMLU-Pro**（2024，[arXiv 2406.01574](https://arxiv.org/abs/2406.01574)）：约 12K 题，改为 10 选 1，增加推理型题目，更难。
    - **MMLU-Redux**：人工重标 3000 题，修正标注噪声。
    - **C-MMLU**：中文版，侧重中国文化与知识。

## 举例

```text
Subject: high_school_mathematics
Question: What is the value of x in the equation 2x + 5 = 13?
Choices: [ "4", "6", "8", "9" ]
Answer: A
```

## 参考

- [arXiv 2009.03300 — Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)
- [HuggingFace cais/mmlu](https://huggingface.co/datasets/cais/mmlu)
- [MMLU-Pro（TIGER-Lab）](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)
