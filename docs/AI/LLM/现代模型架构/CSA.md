# Compressed Sparse Attention (CSA)

> [DeepSeek-V4](https://arxiv.org/abs/2606.19348) §2.3.1。CSA 是 V4 混合注意力里稀疏的那一支：先把序列压成记忆槽，再在槽上做 [DSA](./07-DSA.md)。模型叙事见 [V4](../frontier/12-deepseek-v4.md)。

[DSA](./07-DSA.md) 在原始 token 上挑，挑选之前序列还是 \(n\) 那么长。CSA 把顺序换过来：每 \(m = 4\) 个 token 合成 1 条 KV，序列变成 \(n/m\)，Lightning Indexer 再在这些槽上取 top-k。Flash 的 \(k = 512\)，Pro 的 \(k = 1024\)。

## 第一层：重叠压缩

一句话：每 \(m = 4\) 个 token，用 softmax 归一化的权重（含 learnable 位置偏置）从当前块的 \(C^a\) 和前一块的 \(C^b\) 共 \(2m\) 个位置加权合并成 1 条压缩 KV。序列长度 \(n \to n/m\)。

隐藏状态 \(H \in \mathbb{R}^{n \times d}\) 先投出两套 KV 和两套打分，头维都是 \(c\)（Flash / Pro 都是 512）：

$$
C^a = H W^{aKV}, \quad C^b = H W^{bKV}, \quad
Z^a = H W^{aZ}, \quad Z^b = H W^{bZ}
$$

第 \(i\) 条压缩 KV 用的不是同一套向量切两半，而是两套投影各取一块：

- 当前块：\(C^a,\ Z^a\) 的下标 \([mi,\ m(i+1)-1]\)，再加偏置 \(B^a \in \mathbb{R}^{m \times c}\)
- 前一块：\(C^b,\ Z^b\) 的下标 \([m(i-1),\ mi-1]\)，再加偏置 \(B^b\)

两块 logits 拼成 \(2m\) 行，**按通道**做 softmax（\(Z\) 和 \(B\) 都是宽 \(c\)，每个通道各自在这 \(2m\) 个位置上归一化），再逐通道乘回去求和：

$$
[S^a_{mi:m(i+1)-1};\ S^b_{m(i-1):mi-1}]
= \mathrm{Softmax}_{\text{row}}\!\left([Z^a_{mi:m(i+1)-1}+B^a;\ Z^b_{m(i-1):mi-1}+B^b]\right)
$$

$$
C^{\mathrm{Comp}}_i
= \sum_{j=mi}^{m(i+1)-1} S^a_j \odot C^a_j
+ \sum_{j=m(i-1)}^{mi-1} S^b_j \odot C^b_j
$$

\(B^a, B^b\) 只依赖块内偏移，不依赖绝对位置。\(i = 0\) 时前一块不存在：\(Z^b\) 填 \(-\infty\)，\(C^b\) 填 0，softmax 退化为只看当前 \(m\) 个 token。

以 \(m = 4\) 看槽 1 和槽 2：

| 槽 | 当前块 \(C^a\)（token） | 前一块 \(C^b\)（token） |
|----|--------------------------|--------------------------|
| 1 | 4, 5, 6, 7 | 0, 1, 2, 3 |
| 2 | 8, 9, 10, 11 | 4, 5, 6, 7 |

token 4–7 既作为槽 1 的 \(C^a\)，又作为槽 2 的 \(C^b\)。相邻槽共享边界上的原始 token，只是经过不同的投影。所以压缩比是 \(1/m\)，混合窗口是 \(2m\)。这就是论文说的 overlapped compression：块边界不会因为对齐不巧被切丢。

## 第二层：Lightning Indexer

压缩后的槽在 1M 上下文下仍有 25 万条。CSA 把 [DSA 的 Lightning Indexer](./07-DSA.md) 原样搬到槽上，打分对象从 token 换成压缩块。

Indexer 的 key 用**同一套重叠压缩**得到 \(K^{\mathrm{IComp}} \in \mathbb{R}^{n/m \times c^I}\)，\(c^I = 128\)。查询走低秩，而且和主注意力共用同一条潜变量 \(\mathbf{c}_t^Q\)：

$$
\mathbf{c}_t^Q = \mathbf{h}_t W^{DQ}, \qquad
\mathbf{q}_t^I = \mathbf{c}_t^Q W^{IUQ}
$$

\(\mathbf{q}_t^I\) 拆成 \(n_h^I = 64\) 个头。头权重单独从 \(\mathbf{h}_t\) 投出来，\(w_t^I = \mathbf{h}_t W^w \in \mathbb{R}^{64}\)。查询 \(t\) 对已经完成的压缩块 \(s\)（\(s < \lfloor t/m \rfloor\)）打分：

$$
I_{t,s} = \sum_{h=1}^{n_h^I} w_{t,h}^I \cdot \mathrm{ReLU}\!\left(\mathbf{q}_{t,h}^I \cdot K^{\mathrm{IComp}}_s\right)
$$

和 V3.2 的 indexer 同一组设计：key 在头之间共享，ReLU 把大量点积压成 0，分数不做 softmax，只有相对大小用于排序。相对 V3.2 多出来的是三件事：key 已经是 \(n/m\) 条槽；查询先降到 \(d_c\)（Flash 1024，Pro 1536）再升回；QK 在 FP4 里算。后训练的 QAT 还把 \(I_{t,s}\) 从 FP32 收到 BF16，top-k 选择快一倍，KV 召回率 99.7%。

选出的集合交给主注意力：

$$
\mathcal{C}^{\mathrm{SprsComp}}_t = \left\{ C^{\mathrm{Comp}}_s \mid I_{t,s} \in \mathrm{Top}\text{-}k(I_{t,:}) \right\}
$$

\(t < m-1\) 时第一扇窗口还没合上，indexer 没有合法的 \(s\)，这些查询只靠下面的滑窗。

## 主注意力读这些槽

选中的槽同时当 key 和 value，也就是 MQA：128 或 64 个查询头共享这一份 \(c = 512\) 维的压缩向量。查询从同一条 \(\mathbf{c}_t^Q\) 用 \(W^{UQ}\) 升起来，不给 indexer 和主注意力各做一次降维。

核心注意力之前，查询的每个头和这一份压缩 KV 都过 RMSNorm，避免 logit 爆炸。位置只加在每个向量的最后 64 维。KV 同时又是 value，加权求和会把绝对位置带进输出，所以输出端对这 64 维再乘一个位置为 \(-t\) 的旋转，贡献变回相对距离。

\(c \cdot n_h\) 直接投回 \(d\) 太贵（Pro 是 \(512 \times 128\)）。输出按组投影：Pro 把 128 个头分成 \(g = 16\) 组，每组先收到 \(d_g = 1024\)，再拼起来投回隐藏维。Flash 是 64 个头、\(g = 8\)，中间维同样 1024。

因果性要求查询只能看**已经完成的**压缩块，于是同一块里的其他 token 它看不见，而语言模型又偏爱最近的 token。CSA 和 HCA 都另留 \(n_{\mathrm{win}} = 128\) 条未压缩 KV，和选中的槽一起进核心注意力。滑窗补的是块内和最近邻，不是第二套稀疏选择。

## 和 HCA、DSA 怎么分

| | CSA | HCA | V3.2 的 DSA |
|--|-----|-----|-------------|
| 压缩 | \(m = 4\)，\(C^a\) 当前块 + \(C^b\) 前一块，有重叠 | \(m' = 128\)，单流，块与块不重叠 | 不压缩 |
| 选择 | Lightning Indexer，top-k 512 / 1024 条**槽** | 压缩后全看，不再 top-k | top-2048 个**token** |
| 序列变成 | \(n/4\) | \(n/128\) | 仍是 \(n\) |

HCA 的公式是 CSA 拿掉 \(C^b\) 之后的特例：一块 \(m'\) 个位置、一个 softmax、一条压缩 KV。槽已经很少，稀疏选择的收益让给了压缩本身。层怎么交替见 [V4](../frontier/12-deepseek-v4.md)。

复杂度跟着两级一起降。Indexer 仍扫全部已完成的槽，但槽数是 \(n/m\)，每对只做 64 个头 × 128 维的 ReLU 点积，并且走 FP4。主注意力只读 \(k\) 条 512 维的槽，加上 128 条滑窗。KV cache 按槽存，再叠加 RoPE 维 [BF16](../reasoning/quantization/01-浮点精度.md)、其余 FP8，1M 上下文下 Pro 的 cache 大约是 V3.2 的 10%，Flash 大约是 7%。

## 面试里怎么收束

> CSA 先压缩再稀疏。每 4 个 token，用带可学习位置偏置的 softmax，把当前块的 \(C^a\) 和前一块的 \(C^b\) 共 8 个位置加权合成 1 条 KV，序列变成原来的 \(1/4\)，相邻槽在边界上重叠。Lightning Indexer 再用 64 个低秩头、共享 key 的 ReLU 点积在这些槽上打分，取 top-k（Flash 512，Pro 1024）交给 MQA。同一块内部和最近 128 个 token 靠未压缩滑窗补回来。它减的是序列长度，DSA 减的是参与计算的条数，两级叠在一起。

## 参考

- [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)（§2.3.1 的式 (9)–(19)，Flash / Pro 的 \(m\)、\(k\)、头数在 §3）
- [读懂 DeepSeek V4（二）：Hybrid Attention（CSA + HCA）](https://zhuanlan.zhihu.com/p/2031146581542580917)
- [DeepSeek-V3.2](https://arxiv.org/abs/2512.02556)（Lightning Indexer 的前身）
- [Hugging Face：DeepSeek-V4](https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v4)（`compress_rate_csa = 4`，以及 \(t < m-1\) 时 indexer 没有合法槽）
