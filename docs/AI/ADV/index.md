# 生成式模型

## Acknowledgement

[mli/paper-reading: 深度学习经典、新论文逐段精读](https://github.com/mli/paper-reading?tab=readme-ov-file)

## 任务分类

- seq2labels：词性标注
- seq2label：命名实体识别
- seq2seq：机器翻译

### seq2seq model

- speech recognition
- machine translation
- speech translation：使用 1500h 的台语电视剧和中文字幕，训练一个模型，把台语翻译成中文
- TTS 问题
- chatbot
  - QA：问答
- syntactical parsing：把句子解析成语法树
- multi-label classification：一个样本属于多个类别

## Embedding

one-hot 编码，两个向量没有任何关系

word embedding 词汇之间有语意的关系

但为什么需要用到 Embedding 将唯一的 token 在转换一次，变成一个向量呢？这是因为词与词之间是存在相关性的，我们希望利用上这个信息。例如"man", "gentleman", "guy"表达的意思几乎是相同的，他们生成的 embedding 应该是相似的。而对于长得差不多，但是意义完全不同的单词，则会生成截然不同的 embedding。

embedding 是控制生成图片结果的重要元素之一，正确的 embedding 训练可以触发任意的物体和风格。

!!! example "Embedding"
    === "词语的“意义坐标”"
        词语 → 多维坐标：每个词被分配一个高维空间中的坐标（如“猫”= [0.3, -1.2, 0.8]）。

        语义相似的词语坐标相近（如“猫”和“狗”在向量空间中的距离较小）。
        语义关系可通过向量运算表达：
        
        国王 - 男人 + 女人 ≈ 女王（捕捉性别和地位的类比关系）。
    
    === "鸡尾酒调配"

        词语意义 → 成分配方：每个词的意义由多种“抽象成分”混合而成，如“苹果”= [水果味:0.9, 圆形:0.8, 甜度:0.6]。
        
        Embedding向量的每个维度代表一种语义特征，数值大小表示特征强度。

- 文本
  - **Word2Vec**：通过上下文预测学习词向量（如"银行"在"存钱"和"河流"中的不同含义）。
  - **BERT**：利用 Transformer 模型动态生成上下文相关的向量。

- 图像
  - **CNN**：通过卷积层提取图像特征（如边缘、纹理），输出特征向量。
  - **自编码器**：压缩图像为低维向量，再重建还原。

- 视频
  - **时空块（如 Sora）**：将视频分割为小块，压缩为向量序列，类似文本中的词语。
