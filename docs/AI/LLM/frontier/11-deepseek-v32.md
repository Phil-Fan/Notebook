# DeepSeek-V3.2

> [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556) — DeepSeek，2025.12。架构相对 V3.1-Terminus 只多了 DeepSeek Sparse Attention，经由 [V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) 续训得到。

MLA 和 MoE 的定义在 [V2](09-deepseek-v2.md) 和 [V3](10-deepseek-v3.md)。这篇的结构贡献只有 DSA。报告的另一半是可扩展强化学习和智能体数据合成，那是后训练。

## DSA 在解决什么

MLA 把每个 token 的 KV 变窄，注意力仍然看全部历史，复杂度仍是 \(O(L^2)\)。上下文继续变长时，贵的是「每个查询和每个历史 token 做一次完整注意力」。

DSA 把这件事拆成便宜的打分和昂贵的注意力。

**Lightning indexer。** 用很少的头，对查询和历史 token 做 ReLU 点积，再按头加权求和，得到索引分 \(I_{t,s}\)。头数少，又可以用 FP8，所以虽然 indexer 自己仍是 \(O(L^2)\)，常量远小于主注意力。

**细粒度选择。** 每个查询只把 top-k 个历史位置的 KV 送进主注意力。主注意力从 \(O(L^2)\) 变成 \(O(Lk)\)，\(k \ll L\)。

被问「indexer 不还是二次的吗」时，答案是：二次的那部分换成了廉价打分，贵的矩阵乘只发生在 k 个 token 上。

## 为什么套在 MLA 的 MQA 模式上

V3.2 要接着已有检查点训，而不是从头预训练一种新注意力。DSA 因此装在 MLA 上。kernel 希望同一份 KV 被多个查询头共享，所以用的是 MLA 的 MQA 模式：一个潜变量充当该 token 的 KV，所有查询头共用它。不要把 DSA 说成「又压了一次 MLA 的宽度」。它减的是 token 数。

## 和 NSA 不是同一个模块

[Native Sparse Attention](https://arxiv.org/abs/2502.11089)（2025.02）是研究论文，不是 V3 的检查点。它从预训练开始就用三条支路：粗粒度压缩、细粒度选择、滑窗，并且按 GPU 算术强度设计，正向和反向都能训。

DSA 是后来装进生产模型的两段式：indexer 打分，top-k 再做完整注意力，通过续训接在 MLA 上。面试里先把名字分开，再讲 DSA 的两段。

## 面试里怎么收束

> V3.2 的块还是 V3，只把注意力变成稀疏的。Indexer 用廉价 ReLU 点积选 token，MLA 只对 top-k 做。NSA 是更早的可训练稀疏注意力论文，不要说成 V3.2 的层。报告里追上闭源模型的部分来自强化学习规模，不是这个模块单独完成的。
