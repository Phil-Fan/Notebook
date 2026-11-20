# 多查询注意力（MQA）

> [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150) — Noam Shazeer, 2019。第一次明确把「decode 是内存带宽受限」写成论文标题级别的判断。

MHA 见 [上一页](./01-MHA.md)。MQA 是这条压缩路线的第一刀，也是 [GQA](./03-GQA.md) 的极端值（$n_g = 1$）。

## 只改一处：K/V 的头数

| | MHA | MQA |
|---|---|---|
| 查询头数 | $n_h$ | $n_h$（不变） |
| K/V 头数 | $n_h$ | **1** |
| 每 token 每层缓存 | $2 \cdot n_h \cdot d_h$ | $2 \cdot d_h$ |
| 打分 | 每个头用自己的 $K_i, V_i$ | 所有头共用同一个 $K, V$ |

常见的误读是「MQA 只有一个查询头」。不是：仍然有 $n_h$ 个查询头，只是它们被迫读同一份 K/V。

## 省下来的量级

以 LLaMA-2-7B 的尺寸（$n_h = 32, d_h = 128$，32 层，fp16）估：

| | 每 token 的 KV cache |
|---|---|
| MHA | $2 \cdot 32 \cdot 128 \cdot 32 \cdot 2\text{B} \approx 512$ KB |
| MQA | $2 \cdot 128 \cdot 32 \cdot 2\text{B} \approx 16$ KB |

和 $n_h$ 同比例缩小。更关键的是**算术强度**：同一份 KV 被 $n_h$ 个查询头复用，decode 一步的 FLOP/Byte 大约放大 $n_h$ 倍（≈ $n_h$，即几十），从「差两个数量级」拉回一个量级——但离算力上限仍差一截，还得靠大 batch 才吃满。论文的实测是解码明显变快、质量只有轻微下降，具体倍数随 batch 和序列长度变化。

## 质量与训练

代价很直接：所有头共用一组 key/value 子空间，头间多样性被压制；长上下文里的精确检索最先感受到损失。训练也比 MHA 更不稳，通常要更小的学习率、更长的 warmup。

参数上 $W_K, W_V$ 缩小了 $n_h$ 倍，但相对 FFN 可以忽略。**MQA 的卖点从来不是参数，是缓存和带宽。**

## 工程侧的几个连带结论

- **kernel 零改动**：把 $n_{kv} = 1$ 代入 GQA 的 kernel 即可，MQA 是 GQA 的特例。
- **张量并行不友好**：MHA 沿头维切分，K/V 天然分到各卡；MQA 只有一份 KV，不能切，必须在每个 TP rank 上复制或重算。绝对值小，但算 TP 效率账时要记上，这也是大模型最终多选 GQA 的原因之一。
- **KV 量化更难**：只剩一个头，没有多头平均来稀释误差，INT8/FP8 KV 的精度考核要重做。
- **长上下文更亏**：MQA 只解决「宽度」，不解决 $O(L^2)$；序列一长照样要回到稀疏化。

## 谁用过

PaLM、Falcon、StarCoder 一代是 MQA 的代表。到 2023 年之后，主流开源模型基本转向 GQA：MQA 的质量风险在更大规模上不够划算。

## 面试里怎么收束

> MQA 把 K/V 头数从 $n_h$ 砍到 1，所有查询头共享同一份 K/V，缓存和 decode 带宽都降 $n_h$ 倍，prefill 几乎不变。代价是头间表达被强制耦合、训练不稳、TP 下 KV 还要复制，所以工业界最终多选 GQA 这个折中，而 MQA 成了它的 $n_g = 1$ 特例。

## 参考

- [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150)（2019）
- [GQA](https://arxiv.org/abs/2305.13245)（2023，把 MQA 推广成折中）
- [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311)（2022）
- [Falcon](https://arxiv.org/abs/2311.16867)（2023）
