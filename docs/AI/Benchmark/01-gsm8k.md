# GSM8K

小学数学应用题基准，是「LLM 数学推理」最经典的评测之一。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2021-10（arXiv v1） |
| 论文 | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168)（OpenAI，Cobbe et al.） |
| 数据 | HuggingFace [`openai/gsm8k`](https://huggingface.co/datasets/openai/gsm8k) |

论文的核心贡献其实是 **verifier（验证器）**：训练一个验证器对多个候选解打分，选最优解，把 GPT-3 在 GSM8K 上的准确率从约 18% 提到 55%。

## Bench 结构

- **规模**：7.5K 训练 + 1K 测试，共 8.5K 题（Grade 3–5 小学应用题）。
- **格式**：每题一个 `question`（自然语言故事题）+ 一个 `answer`（分步解法）。
- **答案规范**：解答中每步一行算式，最后一行用 `#### <数字>` 给出最终数值答案。评测只比对 `####` 后的数字。

```text
Question: Natalia sold clips to 48 of her friends in April, and then she sold
half as many clips in May. How many clips did Natalia sell altogether in
April and May?

Answer: Natalia sold 48 clips in April.
She sold 48/2 = <<48/2=24>>24 clips in May.
So she sold 48+24 = <<48+24=72>>72 clips altogether.
#### 72
```

- **评测指标**：accuracy（提取最终数字与 gold 精确匹配）。
- **求解特点**：每题需 2–8 步初等运算（加减乘除），难点在**多步链式推理**而非计算本身。

## 重点测试能力

- **链式推理（multi-step reasoning）**：把故事题拆解为中间步骤，是 CoT（Chain-of-Thought）论文的标准评测场景。
- **数值计算与单位跟踪**：分数、百分比、多对象数量关系。
- **抗干扰**：题干含冗余信息，需要识别有效条件。

!!! note "现状"
    前沿模型已接近满分（>95%），区分度耗尽，且存在明显**数据污染**（题目大量出现在训练语料）。现在评数学推理更多用 MATH、AIME、LiveBench 等。GSM8K 的价值在于便宜、快、适合小模型和消融实验。

## 举例

```text
Question: A robe takes 2 bolts of blue fiber and half that much white fiber.
How many bolts in total does it take?

Answer: It takes 2/2 = <<2/2=1>>1 bolt of white fiber.
So it takes 2+1 = <<2+1=3>>3 bolts in total.
#### 3
```

## 参考

- [arXiv 2110.14168 — Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168)
- [HuggingFace openai/gsm8k](https://huggingface.co/datasets/openai/gsm8k)
- [openai/grade-school-math（GitHub）](https://github.com/openai/grade-school-math)
