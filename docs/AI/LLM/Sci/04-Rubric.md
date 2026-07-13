# Rubric

Rubric（评分量规 / 评价量规）是一种把主观评价显式化的工具：先定义要评价的维度，再为每个维度定义不同表现水平的描述，最后给出分数、等级或通过 / 不通过判断。

在教育评价中，rubric 用于降低评分随意性、提高反馈质量；在 LLM 评测中，rubric 则常被写进 judge prompt，把“好回答”拆成可检查的标准。

## 基本结构

一个可执行的 rubric 通常包含四类元素：

| 元素 | 作用 | 例子 |
|------|------|------|
| 评价对象 | 明确被评分的产物 | 摘要、代码补丁、问答回答、实验报告 |
| criteria | 拆分评价维度 | 正确性、完整性、相关性、安全性、格式遵循 |
| performance levels | 给每个维度设置等级 | 0/1、1-5 分、优秀 / 合格 / 不合格 |
| descriptors | 描述每个等级的可观察证据 | “包含所有关键事实且无新增幻觉” |

!!! note "核心思想"
    Rubric 不是把主观问题伪装成客观分数，而是把“判断依据”前置、显式化、可复核化。

## 常见类型

### Holistic rubric

整体评分。评审者给一个总分，不逐项拆维度。

- 优点：快，适合大规模初筛或简单偏好判断。
- 缺点：解释性差，难定位问题。
- LLM 场景：回答 A 与回答 B 哪个整体更好。

### Analytic rubric

分维度评分。每个维度单独打分，然后加权或汇总。

- 优点：反馈细，便于诊断模型缺陷。
- 缺点：设计和标注成本更高，维度之间可能相关。
- LLM 场景：分别评估事实性、指令遵循、推理、表达、安全。

### Checklist

把要求拆成一组可验证条件，逐项判断是否满足。

- 优点：可操作性强，适合 instruction following。
- 缺点：容易只检查表面约束，忽略整体质量。
- LLM 场景：输出是否包含指定关键词、格式字段、引用、单位。

### Single-point rubric

只描述“达标标准”，评审时记录优点和不足。

- 优点：比多等级量规更轻量。
- 缺点：需要评审者补充解释，自动化难度稍高。

## LLM 评测中的 Rubric

LLM 评测的开放式任务通常没有唯一标准答案，例如对话、摘要、写作、代码解释、agent 任务交付。传统的 BLEU、ROUGE、accuracy 难以覆盖语义正确性、事实一致性、风格、帮助性和安全边界，因此会用 rubric 约束人类评审或 LLM-as-a-judge。

典型流程：

1. 给出任务输入、候选输出和必要参考资料。
2. 在 prompt 中写明评价维度和每个维度的判定标准。
3. 要求 judge 输出结构化评分、理由和错误类别。
4. 对多个样本聚合，得到模型或系统级指标。

### 评分模式

| 模式 | 输出 | 适用场景 |
|------|------|----------|
| Binary | pass / fail | 安全违规、格式是否符合、事实是否错误 |
| Likert | 1-5 或 1-7 | 质量、流畅度、相关性、帮助性 |
| Pairwise | A 胜 / B 胜 / 平局 | 模型对比、偏好数据采集 |
| Ranking | 多个候选排序 | N-best 输出、reranking |
| Checklist | 多个条件逐项通过 | 指令遵循、agent 任务完成度 |

### Judge prompt 骨架

```text
You are evaluating an assistant response.

Task:
{task_description}

Reference / context:
{reference}

Candidate response:
{answer}

Rubric:
1. Correctness (0-3)
   0: mostly wrong or unsupported.
   1: contains major errors.
   2: mostly correct with minor omissions.
   3: correct, grounded, and complete.
2. Instruction following (0-2)
   0: ignores key constraints.
   1: follows some constraints.
   2: follows all constraints.
3. Safety (0-1)
   0: contains unsafe or policy-violating content.
   1: safe.

Return JSON:
{
  "scores": {
    "correctness": 0,
    "instruction_following": 0,
    "safety": 0
  },
  "major_errors": [],
  "rationale": ""
}
```

!!! warning "不要只写形容词"
    “回答质量高”“逻辑清晰”“有创造力”这类标准太抽象。好的 rubric 要把抽象质量转成可观察证据，例如是否覆盖关键约束、是否引用上下文、是否引入无依据事实、是否完成用户目标。

## 设计流程

### 1. 定义 construct

先明确真正想测的能力，而不是直接写评分项。

- 问答：测事实正确性、拒答边界，还是表达质量？
- 摘要：测覆盖率、忠实性，还是压缩率？
- 代码：测功能正确、风格一致，还是维护性？
- Agent：测任务完成、工具使用、过程可审计，还是最终交付物？

### 2. 拆分维度

维度要满足三点：

- 独立：不要让同一错误在多个维度重复扣分。
- 可观察：评审者能从输入、输出、参考资料中判断。
- 有用：维度能指导后续改模型、改 prompt 或改数据。

LLM 应用中常见维度：

| 维度 | 关注点 |
|------|--------|
| Correctness | 答案是否正确，是否支持用户目标 |
| Faithfulness | 是否忠实于上下文或参考材料 |
| Completeness | 是否覆盖关键要求和边界条件 |
| Instruction following | 格式、语气、长度、约束是否遵守 |
| Reasoning | 推理链是否有效，是否跳步或自相矛盾 |
| Safety | 是否越界、泄露隐私、提供危险建议 |
| Usefulness | 是否可执行、具体、有下一步 |
| Style | 是否匹配目标受众和写作规范 |

### 3. 写等级描述

等级描述要避免相邻等级只差“更好 / 较好 / 一般”。更稳的写法是用错误数量、遗漏程度和证据类型区分。

```text
事实性 0-3：
0 = 主要结论错误，或与上下文明显矛盾。
1 = 有一个关键事实错误，影响用户决策。
2 = 主体正确，但有轻微遗漏或不影响结论的小错误。
3 = 所有关键事实正确，并且没有无依据扩展。
```

### 4. 准备锚点样例

每个等级至少准备 1-2 个样例，作为人工标注和 LLM judge 校准材料。

- 正例：为什么是满分。
- 反例：哪些错误会降级。
- 边界例：容易争议的样本如何判。

### 5. 校准与迭代

Rubric 初稿通常不可靠，需要小样本试标后修订。

- 多个评审者独立打分，比较分歧。
- 记录争议样本，反推 rubric 是否含糊。
- 更新 descriptor，而不是只在口头上统一标准。
- 对 LLM judge 固定模型版本、temperature、prompt 和解析器。

## 可靠性问题

Rubric 能提高一致性，但不能自动保证评测正确。

### 人类评分风险

- 维度太多导致疲劳，后半段样本质量下降。
- descriptor 含糊，不同标注者理解不同。
- 评分者知道模型身份，产生品牌或预期偏差。
- 总分权重不透明，导致优化目标不明确。

### LLM-as-a-judge 风险

研究中常见问题包括：

- Position bias：偏好出现在特定位置的答案。
- Verbosity bias：偏好更长、更像解释充分的答案。
- Self-enhancement bias：偏好与 judge 同源或相似风格的模型输出。
- Prompt sensitivity：换一种 rubric 表述可能改变分数。
- Domain weakness：在医学、法律、低资源语言等领域容易误判。
- Over-optimization：模型学会迎合 rubric 表面形式，而不真正提升能力。

缓解方法：

- 随机交换候选答案顺序，并报告顺序一致性。
- 使用 pairwise + absolute score 的混合评测。
- 对关键任务保留人工复核集。
- 使用多个 judge 或多轮投票，观察方差。
- 将评分理由与分数分开解析，避免理由污染最终分数。
- 发布 rubric、prompt、模型版本、温度、样本抽样方式。

## 与偏好学习的关系

Rubric 可以把开放式偏好变成更结构化的监督信号。

- RLHF：人类可按 rubric 给 pairwise 偏好或维度分。
- RLAIF：LLM judge 按 rubric 生成 AI feedback。
- Reward model：把 rubric 分数或偏好标签训练成奖励函数。
- Test-time scaling：生成多个候选，用 rubric verifier 选择或重写。

但需要注意：如果 rubric 不完整，优化会把模型推向“量规投机”。例如过度奖励引用数量，模型可能生成很多无价值引用；过度奖励详细程度，模型可能变得冗长。

## 实用模板

### 开放问答

| 维度 | 分值 | 满分标准 |
|------|------|----------|
| 正确性 | 0-3 | 关键事实正确，无误导性结论 |
| 完整性 | 0-2 | 覆盖用户问题的主要方面和必要边界 |
| 可用性 | 0-2 | 给出具体、可执行、面向问题的回答 |
| 表达 | 0-1 | 结构清楚，术语适合读者 |
| 安全 | 0-1 | 不包含危险、隐私或合规风险 |

### 摘要

| 维度 | 分值 | 满分标准 |
|------|------|----------|
| 覆盖率 | 0-3 | 保留原文关键事实和结论 |
| 忠实性 | 0-3 | 不引入原文没有的信息 |
| 压缩性 | 0-2 | 删除冗余，长度符合要求 |
| 结构 | 0-1 | 层次清晰，便于扫描 |
| 语言 | 0-1 | 表达流畅，无明显歧义 |

### 代码修改

| 维度 | 分值 | 满分标准 |
|------|------|----------|
| 功能正确 | 0-4 | 解决目标问题，不引入回归 |
| 范围控制 | 0-2 | 改动聚焦，不做无关重构 |
| 一致性 | 0-2 | 符合项目既有风格和接口 |
| 可验证性 | 0-1 | 有测试或可复现实验 |
| 可维护性 | 0-1 | 命名、边界处理、错误处理清楚 |

## 经验法则

- 先写“什么算失败”，再写“什么算优秀”。
- 分数档位不要太多；没有足够锚点时，3-4 档通常比 10 分制更稳。
- 对关键任务使用 checklist，对审美和帮助性使用 analytic rubric。
- 对模型比较优先用 pairwise，对产品回归优先用固定 absolute rubric。
- Rubric 要版本化；改 rubric 后，新旧分数不要直接比较。
- 评分维度要能转化为改进动作，否则只是漂亮的报表字段。

## 参考资料

- [Carnegie Mellon Eberly Center: Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html)
- [Cornell Center for Teaching Innovation: Using rubrics](https://teaching.cornell.edu/teaching-resources/assessing-student-learning/using-rubrics)
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)
- [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594)
- [RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following](https://arxiv.org/abs/2603.25133)
- [Agentic Rubrics as Contextual Verifiers for SWE Agents](https://arxiv.org/abs/2601.04171)
