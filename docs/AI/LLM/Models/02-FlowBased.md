# 02 | Flow-Based 流模型与 Flow Matching

## Flow-Based 生成模型

基于可逆变换的生成模型，通过变量替换定理进行精确似然估计。

### 关键论文

- [NICE: Non-linear Independent Components Estimation (2015)](https://arxiv.org/abs/1410.8516)
- [Real NVP (2017)](https://arxiv.org/abs/1605.08803)
- [Glow: Generative Flow with Invertible 1x1 Convolutions (2018)](https://arxiv.org/abs/1807.03039)

## Flow Matching

Flow Matching 是一种基于连续归一化流（Continuous Normalizing Flow, CNF）的生成建模方法，将简单分布通过 ODE 逐步变换为目标数据分布。

### 核心论文

- [Flow Matching for Generative Modeling (2023)](https://arxiv.org/abs/2210.02747) — 奠基性工作
- [Conditional Flow Matching (2023)](https://arxiv.org/abs/2302.00482)
- [Flow Matching Guide (2025)](https://arxiv.org/abs/2412.06264) — 综述

### 参考资料

<iframe src="https://www.youtube.com/embed/7NNxK3CqaDk" allowfullscreen></iframe>

- [Flow Matching Guide - Hugging Face](https://huggingface.co/blog/flow-matching)
