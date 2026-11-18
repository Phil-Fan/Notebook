# 多头注意力（MHA）

> [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017。现代 LLM 里所有注意力变体的原点，也是「decode 为什么会被 KV cache 卡住」的根源。

后面几页都只改一件事：每个查询头到底要不要有自己的一份 K/V。先看 [MQA](./02-MQA.md) 和 [GQA](./03-GQA.md) 怎么少存几份，再看 [MLA](./04-MLA.md) 怎么换一种存法。

## 它在算什么

输入 \(X \in \mathbb{R}^{L \times d}\)，\(n_h\) 个头，每头维度 \(d_h = d / n_h\)：

$$
Q_i = XW^i_Q,\quad K_i = XW^i_K,\quad V_i = XW^i_V,\quad
\mathrm{head}_i = \mathrm{softmax}\!\left(\frac{Q_iK_i^\top}{\sqrt{d_h}}\right)V_i
$$

$$
\mathrm{MHA}(X) = [\mathrm{head}_1;\,\dots;\,\mathrm{head}_{n_h}]\,W_O
$$

注意分区方式：\(n_h\) 个头不是各做一次 \(d\) 维注意力，而是把 \(d\) 维空间**切**成 \(n_h\) 份，每份做 \(d_h\) 维注意力。参数量和不切头时完全一样，换来的只是「多个低维子空间」而不是「一个高维子空间」。

## 为什么当初要多头

单个 \(d\) 维内积的注意力分布是被一个线性映射整体塑形的，只能表达一种「相关性」视角。切成 \(n_h\) 份之后，每份有自己的 \(W_Q, W_K, W_V\)，可以在不同子空间里同时关注不同的关系——句法依存、共指、位置邻近可以各自有一份权重。

论文的说法是：单头平均（averaging）会抑制这种多样性。实践里的经验补充更直接：训练好的 MHA 里存在**大量冗余头**，剪掉一些几乎不掉点。这条经验是后来 MQA、GQA 敢把 KV 份数砍到 1 或 8 的前提。

## 代价：decode 是带宽问题，不是算力问题

每 token 每层要缓存 \(2 \cdot n_h \cdot d_h = 2d\) 个元素。decode 一步（序列长 \(L\)，单请求）：

| 量 | 表达式 |
|----|--------|
| 读 KV cache | \(2 \cdot n_h \cdot d_h \cdot L\) 个元素 |
| 算力 | \(4 \cdot n_h \cdot d_h \cdot L\) FLOPs（QK 与 AV 各两倍） |

比值是常数 **约 1 FLOP/Byte**（fp16：每元素 2 字节，读写只算一遍）。而 H100 一类的卡，算力/带宽比在几百 FLOP/Byte 量级。差两个数量级，意味着 decode 时 GPU 的 Tensor Core 在等 HBM——除非 batch 足够大，把同一份 KV 复用 \(B\) 次。

同一个式子还有一个结果：**KV cache 只跟 \(n_h \cdot d_h\) 有关，跟头怎么切无关。** 所以后来所有省缓存的改法，都不是在改「头数」，而是在改「K/V 存几份」（MQA/GQA）或「一份存多宽」（MLA）。

Prefill 则相反：\(O(L^2 d)\) 的计算，算力受限，缓存大小几乎不影响。

## 现代模型里还剩下什么

- 「多头」结构没被淘汰：DeepSeek-V2 用 MLA，仍然是 128 个查询头、每头 128 维；Qwen3、Llama 3 是 GQA，仍保留 \(n_h\) 个查询头。
- 被淘汰的是「每个查询头独立缓存一份 K/V」这条假设。
- 极长上下文下连查询头数也可能变少：稀疏注意力里的 indexer 只用很少几个头打分（见 [DSA](./06-DSA.md)）。

## 面试里怎么收束

> MHA 的问题不是显存总量，而是 decode 每步要把整个 KV cache 读一遍，算术强度只有约 1 FLOP/Byte，注定带宽受限。之后的变体只有三条路：少存几份（MQA / GQA）、把一份压窄（MLA）、少算几个 token（NSA / DSA），以及换掉 softmax 这个范式（混合线性注意力）。

## 参考

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)（2017）
- [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150)（2019，MQA）
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)（2023）
- [Are Sixteen Heads Really Better than One?](https://arxiv.org/abs/1905.10650)（2019，头冗余）
- Sebastian Raschka, [The Big LLM Architecture Comparison](https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison)（2025）
