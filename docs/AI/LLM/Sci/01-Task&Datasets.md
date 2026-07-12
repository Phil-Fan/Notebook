# 01 | Task & Datasets

## 任务分类

### 语言任务（LLM）

- QA：问答能力与知识覆盖
- Reasoning：多步推理一致性
- Long Context：长上下文检索与整合
- MCQ：结构化选择题能力

### 视觉语言任务（VLM/MLLM）

- Image Caption：图像描述生成
- VQA：看图问答
- Y/N：视觉二分类判断
- MCQ：视觉多选题推理
- MTT：多轮图文对话
- MTI：多图输入综合推理

## 数据形态

### 监督数据（SFT）

- 文本：`instruction / input / output`
- 多模态：`{image, question, answer}`

### 偏好数据（Alignment）

- pairwise：优劣回答对
- listwise：多候选排序
- rubric：按维度打分（语义、真实性、审美、安全）

### 对比数据（跨模态对齐）

- 正样本：匹配图文对
- 负样本：不匹配图文对
- 目标：学习共享语义空间与检索能力

## 评测任务与指标（最小集）

- 翻译：BLEU / COMET
- 文本生成：ROUGE / BERTScore
- 分类与 VQA：Accuracy
- 开放式多模态：维度化打分 + 人评

## 数据集设计要点

- 覆盖真实分布与长尾场景
- 去重、去模板污染、去脏数据
- 训练/验证/测试严格隔离
- 偏好标注要有统一规则与仲裁机制
