# 09 | LLaVA 多模态模型

## 核心思想

怎么理解图像中的信息呢
用模型 GPT4(text only models) 来提升数据集的效果，

## 怎么做？

LLaVA 的架构是基于 LLaMA 的，但是它能够理解图像和文本，并能够进行对话。

## 数据集准备

1. VQA：要训练理解图像能力，就要构造成问答对
2. Describe image in detail
3. complex reasoning

## 训练

1. 单轮对话数据：视觉 token 投影到文本 token，单独训练 projection layer
2. fine-tuning end-to-end model 微调文本模型
   1. multimodel chatbot
   2. science QA

把图片 token 编码成向量，再替换掉原有的 token

## 相关工作

- LLaVA-Med
