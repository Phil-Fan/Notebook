# 分组查询注意力（GQA）

> [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245) — Ainslie et al., 2023。MHA 和 MQA 之间的连续插值，2024 年之后开源模型的注意力默认值。

[MHA](./01-MHA.md) 和 [MQA](./02-MQA.md) 的对比见前两页。GQA 的贡献是把「共享」从二值选择变成参数 $n_g$。

## 定义

把 $n_h$ 个查询头分成 $n_g$ 组，组内查询头共用一份 K/V：

$$
\mathrm{head}_i = \mathrm{softmax}\!\left(\frac{Q_i K_{\lfloor i/\,(n_h/n_g) \rfloor}^\top}{\sqrt{d_h}}\right) V_{\lfloor i/\,(n_h/n_g) \rfloor}
$$

两个端点都对得上：$n_g = n_h$ 是 MHA，$n_g = 1$ 是 MQA。所以工程上只需要一个 `n_kv_heads` 参数，kernel 也只需要一条路径。

| | MHA | GQA-8 | MQA |
|---|---|---|---|
| K/V 头数 | $n_h$ | 8 | 1 |
| 每 token 每层缓存 | $2 n_h d_h$ | $2 \cdot 8 \cdot d_h$ | $2 d_h$ |
| Llama-3-8B 实配（$n_h=32, d_h=128$，32 层） | 32 | 8 | 1 |

缓存和带宽下降的倍数是 $n_h / n_g$。以 Llama 3 为例，GQA-8 把每 token 的 KV cache 压到 MHA 的 1/4。

## 它是怎么来的：从 MHA 续训，而不是从头训

这是 GQA 最值得记的一点。论文给了 **uptraining** 的做法：

1. 取一个训好的 MHA 检查点；
2. 每组 $n_h/n_g$ 个 K/V 头用均值池化合成一个头；
3. 用原预训练算力的约 **5%** 继续预训练。

结论是：GQA-8 续训后的质量接近 MHA，同时享有接近 MQA 的解码速度；而同样 5% 算力的 MQA 续训，质量明显掉下来。这条结果说明「共享」掉的质量主要是可以靠短时间适配补回来的，也解释了为什么这么多团队敢于直接迁移。

## 为什么最后是 8

$n_g$ 的选择是「质量 / 缓存」的帕累托前沿，经验上：

- $n_g$ 从 $n_h$ 降到 8，质量损失很小，缓存降 4 倍；
- 从 8 再往下降，质量损失开始明显，缓存收益却被 MLA 这类方案超过；
- 8 也是张量并行的甜点：TP $\le$ 8 时每个 rank 恰好分到一个 KV 头，不需要复制（TP 16 就要复制 2 份）。

所以 Llama 2-70B / Llama 3 全系、Qwen2 / Qwen3、Gemma、Mistral 家族都落在 8 这一档。

## 工程侧

- **kernel 不改**：FlashAttention / PagedAttention 本来就按 $n_{kv}$ 泛化，GQA 只是把它设成 8。
- **PagedAttention 直接受益**：page 里 KV 的头数变少，同样 block 尺寸能装更长上下文。
- **PD 分离 / 前缀缓存**：传输字节数同比例下降，长前缀场景收益最明显。
- **TP 不均衡**：$n_g$ 必须能被子张量并行度整除，否则复制的部分会吃掉一部分扩展效率。

## 和 MLA 的关系

GQA 是**常数倍**地少存 K/V：再好的 $n_g$ 也只能把缓存降到 $2 n_g d_h$。序列越来越长时这个常数不够用，于是有了把宽度也压下去的 [MLA](./04-MLA.md)。

DeepSeek-V2 的消融结论可以直接背：**同样的推理预算下，MLA 的建模质量好于 GQA**。所以 DeepSeek 从 V2 起不再用 GQA。

## 面试里怎么收束

> GQA 把查询头分成 $n_g$ 组，组内共享 K/V，是 MHA（$n_g=n_h$）和 MQA（$n_g=1$）的插值。它可以用 5% 的算力从 MHA 检查点续训得到，质量接近 MHA、速度接近 MQA，8 组是质量、缓存和 TP 的甜点，所以成了 2024 年后开源模型的默认。它只把缓存降一个常数倍，长上下文下还要靠 MLA 或稀疏注意力。

## 参考

- [GQA](https://arxiv.org/abs/2305.13245)（2023）
- [MQA](https://arxiv.org/abs/1911.02150)（2019）
- [Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)（2024）
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)（2025）
