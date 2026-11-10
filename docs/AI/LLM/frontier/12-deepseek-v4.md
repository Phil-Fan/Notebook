# DeepSeek-V4

> [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) — DeepSeek，2026，预览。Pro 为 1.6T 总参数、49B 激活；Flash 为 284B 总参数、13B 激活。上下文 1M。

相对 [V3](10-deepseek-v3.md)，MoE 框架和 MTP 还在。换掉的是注意力和残差，优化器也换了。和 [V3.2](11-deepseek-v32.md) 比，1M 上下文下 Pro 的单 token 等效 FP8 FLOPs 约 27%、KV cache 约 10%；Flash 约 10% 和 7%。

## 这篇论文代表什么

DSA 仍在原始 token 上挑选。百万长度下，挑选之前应先把序列变短。V4 代表的是：长上下文的下一步是压缩记忆槽，而不是继续加大 top-k。

## CSA 和 HCA

两条注意力交错使用，都另留一个 128 token 的未压缩滑窗，补回当前压缩块内部和最近邻的细节。压缩会让查询看不到同一块里的其他 token，而语言模型又偏爱最近的 token，所以滑窗不是可有可无的装饰。

**CSA（Compressed Sparse Attention）。** 每 \(m = 4\) 个 token 合成 1 条 KV，再对压缩后的条目做 [DSA](11-deepseek-v32.md)。Flash 的 top-k 是 512，Pro 是 1024。压缩用两组重叠的加权池化，实际序列长度变成原来的 \(1/4\)。

**HCA（Heavily Compressed Attention）。** 压缩率 \(m' = 128\)，不做重叠，压缩后走普通稠密注意力，不再 top-k。槽已经很少，稀疏选择的收益让给了压缩本身。

层的排法：

| 模型 | 开头 | 之后 | CSA top-k |
|------|------|------|-----------|
| Flash | 前 2 层纯滑窗 | CSA 与 HCA 交替 | 512 |
| Pro | 前 2 层 HCA | CSA 与 HCA 交替 | 1024 |

压缩后的条目同时当 key 和 value，也就是 MQA。核心注意力前，查询和这条压缩 KV 做 RMSNorm，避免 logit 爆炸，并沿用 attention sink。

位置只加在每个向量的最后 64 维。KV 同时是 value，加权求和会把绝对位置带进输出。输出端对这 64 维再乘一个位置为 \(-t\) 的旋转，使这部分贡献变成相对距离，而不是绝对位置的混合。

三条注意力因此是三级，不要并成一个名字：

- MLA 压每个 token 的宽度。
- DSA 减少参与注意力的 token 数。
- CSA / HCA 先把 token 合成更少的槽，再在槽上做稀疏或稠密注意力。

## MoE 相对 V3 的改动

仍是细粒度路由专家加 1 个共享专家，无辅助损失的偏置均衡还在，另加一个权重很小的序列级均衡损失，防止单条序列内部极端不均。

| | 层数 | 隐藏维 | 路由专家 | 每 token 激活 | 专家中间维 |
|--|------|--------|----------|----------------|------------|
| Flash | 43 | 4096 | 256 | 6 | 2048 |
| Pro | 61 | 7168 | 384 | 6 | 3072 |

亲和度从 sigmoid 改成 \(\sqrt{\mathrm{softplus}(\cdot)}\)。V3 开头的稠密 FFN 换成 Hash 路由的 MoE：前几层不学 router，用哈希把 token 分到专家，用来换训练稳定性。路由目标节点数的限制也去掉了。MTP 深度为 1。

路由专家权重在后训练里用 MXFP4，CSA indexer 的 QK 也走 FP4。这是量化，不是新的连接。

## mHC

[Manifold-Constrained Hyper-Connections](https://arxiv.org/abs/2512.24880) 改的是残差，不是注意力。普通残差是一条流，\(x + F(x)\) 里的恒等映射让深层训得动。Hyper-Connections 把残差加宽成 \(n\) 条，层与层用矩阵混合，表达力上去，恒等映射没了，深层数值会漂。

mHC 用 Sinkhorn-Knopp 把混合矩阵投到双随机矩阵上：元素非负，每行每列的和为 1。混合变成凸组合，特征均值守恒，谱范数不超过 1，多层连乘仍守得住。V4 取 \(n_{hc} = 4\)，Sinkhorn 20 步。mHC 论文自己的大规模实验里，\(n = 4\) 的额外时间大约 6.7%。

## 优化器和后训练

大部分参数用 Muon，嵌入、输出头和 RMSNorm 仍用 AdamW。这是优化器，不要和 mHC 说成一个模块。

后训练先按数学、代码、智能体、指令遵循分别做 SFT 和 GRPO，再用来自学生自己轨迹的 on-policy distillation 合成一个模型。那是对齐路线。架构题收到 CSA、HCA 和 mHC 即可。

## 面试里怎么收束

> V4 仍是 DeepSeekMoE。长上下文的新块是先压缩再注意：CSA 每 4 个 token 压成 1 条然后做 DSA，HCA 每 128 个压成 1 条然后做稠密注意力，旁边都有 128 的滑窗。mHC 把加宽残差约束成双随机矩阵，用来把恒等映射的稳定性找回来。
