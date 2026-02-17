# 01 | Task & Datasets

## 机器翻译

机器翻译就是把一种语言翻译成另外一种语言

- 第一个挑战，译文选择：同义词很多
- 第二个挑战，语序调整，主谓宾等
- 第三个挑战，数据稀疏。

发展历程

| 简称 | RBMT | SMT | NMT |
| --- | --- | --- | --- |
| 正式名称 | 基于规则的机器翻译引擎 | 统计机器翻译引擎 | 神经机器翻译引擎 |
| 概要 | 基于辞典、语法知识的机器翻译 | 基于海量对译数据统计信息的机器翻译 | 应用人工智能采用深度学习技术的机器翻译 |
| 优点 | 翻译速度快忠实于原文适合固定格式文章翻译 | 比 RBMT 翻译质量高能够翻译出比较自然的文章在 BLEU 值 2 评估中往往得分较高 | 比 SMT 翻译质量高能够翻译出自然流畅的文章 |
| 缺点 | 译文表达不够自然 | 译文表达不够自然 | 需要花费时间学习对译数据 |

评估

1. BLEU Score (Bilingual Evaluation Understudy)
   - 最常用的机器翻译自动评估方法
   - 通过比较机器翻译输出和多个参考翻译之间的 n-gram 重叠来工作
   - 示例：
     - 机器输出："the cat is on the mat"
     - 参考输出："the cat is sitting on the mat"
     - 1-gram 精度：5/6
     - 2-gram 精度：4/5
2. METEOR (Metric for Evaluation of Translation with Explicit ORdering)
   - 考虑同义词匹配、词干匹配以及词序
   - 示例：
     - 机器输出："the pet is on the rug"
     - 参考输出："the cat is on the mat"
     - METEOR 会考虑"pet"和"cat"、"rug"和"mat"之间的相似性

3. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

   - 通常用于评估自动文摘，也可用于机器翻译
   - 考虑机器翻译输出和参考翻译之间 n-gram 的召回率
   - 示例：
     - 对于"the cat is on the mat"和"the cat is sitting on the mat"
     - ROUGE-1 召回率：6/7

4. TER (Translation Edit Rate)

   - 衡量将机器翻译输出转换为参考翻译所需的最少编辑次数
   - 包括插入、删除、替换等操作
   - 示例：
     - 机器输出："the cat sat on the mat"
     - 参考输出："the cat is sitting on the mat"
     - TER: 1/7 (需要添加一个"is")

### 数据集

Multi30K 是 Flickr30K 数据集 (Young 等人，2014) 的扩展，具有英语描述的 31,014 德语翻译和 155,070 独立收集的德语描述。翻译是从专业签约的翻译人员那里收集的，而描述是从未经培训的众筹人员那里收集的。这些语料库之间的关键区别在于不同语言的句子之间的关系。在翻译的语料库中，我们知道两种语言的句子之间有很强的对应关系。在描述语料库中，我们只知道句子，无论语言如何，都应该描述相同的图像。

## LLM

### Long Context

### Mathematics

### Reasoning

### QA

### MCQ

## VLM

### Image Caption

[超全 image captioning 资料汇总 - 知乎](https://zhuanlan.zhihu.com/p/495590371)

### VQA

### MCQ: 单项选择题

### Y/N: 正误判断题

### MTT: 多轮对话评测

### MTI: 多图输入评测

‌​‌‌​​​​‌​​​‌‌‌‌‌​​‌‌​‌​‌​​‌​​​‌‌​‌‌‌​‌‌‌​​‌‌‌‌​‌​​​‌​‌‌‌​​‌‌‌‌​‌​‌‌​​‌‌‌​​‌‌‌‌​‌​​‌‌‌​‌

## CLIP

### zeroshot_classification

### zeroshot_retrieval
