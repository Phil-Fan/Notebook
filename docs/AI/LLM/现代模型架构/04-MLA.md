# 多头潜在注意力（MLA）

> [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434) — DeepSeek, 2024.05。MLA 的完整定义在这一篇；V2 之后 DeepSeek 全线（V3、V3.2、V4 的全局部分）都从它出发。

前几页在「少存几份 K/V」上做文章（[MQA](./02-MQA.md)、[GQA](./03-GQA.md)），都是常数倍。MLA 换了轴：**每个 token 只缓存一个低维潜变量，用的时候再升维回各个头。**

## 缓存里存什么

对隐状态 \(h_t \in \mathbb{R}^{d}\)：

$$
c^{KV}_t = W_{DKV}\,h_t \in \mathbb{R}^{d_c},\qquad
k^C_t = W_{UK}\,c^{KV}_t,\qquad v^C_t = W_{UV}\,c^{KV}_t
$$

位置信息单独走一路（原因见下一节）：

$$
k^R_t = \mathrm{RoPE}(W_{KR}\,h_t) \in \mathbb{R}^{d_R}
$$

最终每个头的 key 是内容部分拼上位置部分，value 只有内容部分：

$$
k_t = [\,k^C_t\,;\,k^R_t\,],\qquad v_t = v^C_t
$$

**缓存只存 \(c^{KV}_t\) 和 \(k^R_t\)**，也就是 \(d_c + d_R\) 个数。DeepSeek-V2/V3 的配置是 \(d_c = 512,\ d_R = 64\)。

## 缓存账

同样按 V2 的配置（\(n_h = 128,\ d_h = 128\)）：

| 结构 | 每 token 每层缓存 | 相对 MHA |
|---|---|---|
| MHA | \(2 \cdot 128 \cdot 128 = 32768\) | 100% |
| GQA-8 | \(2 \cdot 8 \cdot 128 = 2048\) | 6.25% |
| MQA | \(2 \cdot 128 = 256\) | 0.78% |
| **MLA** | \(512 + 64 = 576\) | **1.76%** |

比 GQA-8 还少 3.5 倍，只比 MQA 多一倍多，而质量比两者都好。和整个 DeepSeek 67B（MHA）相比，官方口径是 KV cache 降 **93.3%**、最大生成吞吐 **5.76×**。

## 为什么 RoPE 要解耦

这是最容易被问倒的细节。RoPE 是乘性的旋转，只对 \(q^\top k\) 这个点积有意义。如果先把 key 降到 \(c^{KV}\) 再升维，RoPE 和这两个投影矩阵不可交换——位置会被升维矩阵搅乱，相对位置性质直接破坏。V2 的消融里强行给 \(k^C\) 加 RoPE 确实崩了，所以拆成两路：

$$
\mathrm{score} = \underbrace{q^C \cdot k^C}_{\text{内容，走潜变量}} + \underbrace{q^R \cdot k^R}_{\text{位置，64 维小头}}
$$

代价是多缓存 64 维；收益是位置编码可以照常外推。

## 推理时的「吸收」

训练时按定义算最直白，但 decode 若真把 \(c^{KV}\) 升维成 128 个头的 K/V，就等于白省了带宽。所以要做**矩阵吸收**：

- \(W_{UK}\) 折进查询侧：\(q^\top W_{UK} c = (W_{UK}^\top q)^\top c\)，直接用 \(c^{KV}\) 当 key 打分；
- \(W_{UV}\) 折进输出侧：所有 token 共享同一个 \(W_{UV}\)，可以先对 \(c^{KV}\) 加权求和再做投影。

结果是 decode 退化成「**MQA 式的 latent 注意力 + 一路 64 维 RoPE 点积**」。这才是它能写进 FlashMLA 这类专用 kernel 的原因，而不只是「低秩所以省内存」。

吸收的代价：

- RoPE 那一路不能吸收，必须物化，kernel 要把主项和补充项分开算；
- \(W_{UK}, W_{UV}\) 并进 \(W_Q, W_O\) 后矩阵变宽，**prefill 的 FLOPs 上升**，所以很多实现按 prefill / decode 分别决定是否吸收；
- 张量并行下 \(c^{KV}\) 是**复制**而不是切分（每个 rank 都要完整潜变量才能算自己的头），显存和通信账要记一笔，但潜变量本身很小。

## 量化与后续演化

- 潜变量低维、动态范围温和，FP8/INT8 量化 KV 比较自然；V3 整网就是 FP8 训练 + FP8 推理权重/激活。
- V3 原封不动留下 MLA，只换训练策略、MoE 规模和 FP8；671B / 37B 的配置不变。
- [V3.2 的 DSA](./06-DSA.md) 装在 MLA 的 MQA 模式上——稀疏选择要的是「多个查询头共享同一份 KV」，刚好是吸收后的形态。
- Kimi Linear 的全局层是**不带位置编码的 MLA**：NoPE 之后连那 64 维解耦 key 都不用留，推理时是纯 MQA。
- V4 进一步把序列先压成记忆槽（CSA/HCA），见 [DeepSeek-V4](../frontier/12-deepseek-v4.md)。

## 训练与转换

- 从零训练需要足够大的 \(d_c\)：\(d_c\) 太小会变成信息瓶颈，V2 的消融显示 \(d_c = 512\) 已经够用，再大收益有限。
- 已有 MHA/GQA 模型想转 MLA：论文给了继续预训练的做法，用约 1B token 量级即可转换，且转换后优于同预算的 GQA 基线。
- 注意 MLA 不是「GQA 的升级版参数化」，它多了一组 down / up 投影，注意力参数与 MHA 同量级，相对 FFN 可忽略。

## 面试里怎么收束

> MLA 不缓存 K/V，而是缓存每个 token 的低维潜变量 \(c^{KV}\)（512 维）加一路解耦的 64 维 RoPE key，用时再升维成各个头。缓存降到 MHA 的约 1/57，比 GQA-8 还少 3.5 倍，质量不降。推理时把升维矩阵吸收进查询和输出投影，退化成 MQA 式的潜变量注意力，这是它能跑专用 kernel 的原因。它是「压宽度」，和 DSA 的「减 token 数」正交。

## 参考

- [DeepSeek-V2](https://arxiv.org/abs/2405.04434)（2024）
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)（2024）
- [DeepSeek-V3.2-Exp 仓库](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp)
- [FlashMLA](https://github.com/deepseek-ai/FlashMLA)（MLA 的 Hopper kernel）
- [Kimi Linear](https://arxiv.org/abs/2510.26692)（2025，NoPE 的 MLA 全局层）
