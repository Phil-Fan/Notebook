# DeepSeek-V2

> [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — DeepSeek，2024.05。236B 总参数，每个 token 激活 21B。

对照表见 [架构面试提纲](08-interview.md)。V2 是后面整条 DeepSeek 线的结构起点：V3 留下这套块，只改训练策略。

## 这篇论文代表什么

两件原本分开的效率手段可以装进同一个前沿模型：

- **MLA** 压缩 KV cache 的宽度，让长上下文的显存和访存下来。
- **DeepSeekMoE** 把总参数和每 token 的计算量拆开。

论文要证明的是经济性：同样的能力，训练和推理都比当时的稠密开源模型便宜。块上的新意是 MLA，不是又一种 Transformer。

## MLA

GQA 的办法是少存几份 K/V：若干查询头共用一组 key 和 value，缓存缩小一个常数倍。序列一长，这个常数不够。

MLA 缓存的不是 K/V 本身，而是一个低维潜变量 \(c^{KV}\)。注意力计算时再把它升维成各个头的 key 和 value。省掉的是每个 token 的缓存宽度，序列长度仍然是 \(L\)。所以它和后面 V3.2 的稀疏注意力是正交的：一个压宽度，一个减参与计算的 token 数。

有一个必须一起讲的细节。如果把带 RoPE 的 key 也压进同一个低秩空间，位置信息和内容会抢这个瓶颈，升维之后位置对不齐。V2 把 key 拆开：

- 内容进潜变量，不带位置。
- RoPE 加在单独的、不经过这层压缩的解耦 key 上。

推理时，升维矩阵可以吸收进查询侧的投影。主注意力变成类似 MQA 的形式：所有头共享那一份潜变量。这是它能写成高性能 kernel 的原因，而不只是「低秩所以省内存」。

V2 的消融是：同样的推理预算下，MLA 的建模好于 GQA。DeepSeek 从这一代起不再用 GQA。

## DeepSeekMoE

来源是更早的 [DeepSeekMoE](https://arxiv.org/abs/2401.06066)。和 Mixtral 那种「少量大专家、top-2」不同，它把 FFN 切成很多小专家，每个 token 多选几个。

另外设少量共享专家，每个 token 都会走过。共享专家吸收「什么句子都需要」的通用变换，路由专家更容易专精，而不是每个专家都重复存一份常识。

V2 把这套 MoE 和 MLA 放到了 236B / 21B 的规模上。具体到 671B 的专家个数是 V3 的配置，不要安到 V2 头上。

## 面试里怎么收束

> V2 代表「KV 宽度」和「激活参数」可以同时省。MLA 缓存低维潜变量，RoPE 走解耦 key，推理时退化为共享 KV 的注意力。MoE 用细粒度专家加共享专家。V3 没有换掉这两块。
