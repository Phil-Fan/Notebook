# HotpotQA

多跳（multi-hop）问答基准：答案需要跨多篇维基百科文章推理拼接，是「检索 + 推理」结合的经典数据集。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2018-09（arXiv），EMNLP 2018 |
| 论文 | [HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering](https://arxiv.org/abs/1809.09600)（Yang et al., CMU / Stanford / Mila） |
| 官网 | [hotpotqa.github.io](https://hotpotqa.github.io/) |

## Bench 结构

- **规模**：约 114k 问答对（众包撰写），基于英文维基百科文章。
- **两种评测设置**：

    | 设置 | 输入 | 考察点 |
    |------|------|--------|
    | distractor | 问题 + 10 篇文章（2 篇相关 + 8 篇干扰） | 阅读理解与多跳推理 |
    | fullwiki | 只有问题，需自行检索全维基 | 检索 + 推理端到端 |

- **两大特色**：
  1. **多跳推理**：答案需串联 ≥2 篇文章的信息（桥接实体或比较）。
  2. **支撑句标注（supporting facts）**：每题标注推理所需的句子，可同时评测模型给出的**解释**是否靠谱。
- **题型**：span 抽取（答案来自原文片段）与 yes/no 判断。
- **指标**：EM / F1（答案）+ EM / F1（支撑句）。

## 重点测试能力

- **多跳推理**：实体桥接（A 的导演也演了 B？）与比较（X 和 Y 谁更高？）。
- **干扰项鲁棒**：distractor 设置下 8 篇无关文章考验信息筛选。
- **可解释性**：支撑句监督让「答对但理由错」可以被发现。

!!! note "现状"
    对前沿 LLM 已偏易（fullwiki 设置 EM >70%），且存在污染；但其「检索 + 多跳」结构被 RAG 系统评测大量沿用。后续更难的多跳基准：2WikiMultiHopQA、MuSiQue、Bamboogle。

## 举例

```text
Q: Were Scott Derrickson and Ed Wood of the same nationality?

推理链:
  文章1: "Scott Derrickson is an American director..."
  文章2: "Edward Davis Wood Jr. was an American filmmaker..."
  → 桥接比较: 两人都是美国人
A: yes
支撑句: 上述两句
```

## 参考

- [arXiv 1809.09600 — HotpotQA](https://arxiv.org/abs/1809.09600)
- [HotpotQA 官网与 Leaderboard](https://hotpotqa.github.io/)
- [HuggingFace hotpot_qa](https://huggingface.co/datasets/hotpot_qa)
