# 并行策略：DP、TP、PP、EP

> 训练大模型时，DP、TP、PP、EP 切的是不同的轴。选择顺序是：先算参数状态放不放得下，再决定切批次、切层内、切深度还是切专家。通信重的维度留在 NVLink 域里，跨节点优先用流水线和数据并行。

一张卡上的训练状态远大于权重本身。混合精度 Adam 下，每个参数大约占 **16 字节**：

| 状态 | 精度 | 字节 |
|------|------|------|
| 权重 | bf16 | 2 |
| 梯度 | bf16 | 2 |
| FP32 master、动量、方差 | fp32 × 3 | 12 |

7B 大约 112 GB，70B 大约 1.1 TB，还没算激活。激活随 batch、序列长度和层数涨，激活重计算可以用算力换这块显存。8-bit 优化器和 CPU offload 把 16 这个常数降下来，并行维度的选择逻辑不变。

## 每种策略切哪一轴

| 策略 | 切什么 | 每卡少掉的显存 | 通信 | 放在哪 |
|------|--------|----------------|------|--------|
| DP 数据并行 | 全局 batch | 参数仍是完整一份 | 每步一次梯度 all-reduce | 跨节点扩吞吐 |
| ZeRO / FSDP | DP 组里的优化器、梯度、参数 | ZeRO-1 切优化器，ZeRO-3 / FSDP 连参数一起切 | 切得越深，集合通信越多 | 模型还放得进一个高带宽域时 |
| TP 张量并行 | 一层里的权重和计算 | 参数、梯度、激活都约除以 TP | 每层 all-reduce，或 all-gather + reduce-scatter | 节点内 NVLink |
| SP 序列并行 | TP 组里 LayerNorm / Dropout 的激活 | 去掉 TP 下被复制的那部分激活 | 与 TP 同一组 | 开了 TP 就一起开 |
| PP 流水线并行 | 层，按深度切成 stage | 参数约除以 PP | 相邻 stage 之间传激活，点对点 | 跨节点 |
| CP 上下文并行 | 序列维 | 激活约除以 CP，权重仍复制 | 注意力要交换 KV，环形点对点 | 序列约 8K 以上 |
| EP 专家并行 | MoE 的专家 | 专家参数约除以 EP | 每层 MoE 两次 all-to-all | 优先节点内；很大的 EP 才跨节点 |

世界规模要满足两条独立的分解。`ETP` 缺省等于 `TP`。

```text
world_size = TP × CP × PP × DP
world_size = ETP × EP × PP × EDP
```

专家个数必须能被 EP 整除。隐藏维和头数要能被 TP 整除。层数要能被 PP 整除，开了虚拟流水线还要能被每卡的 stage 块数整除。

EP 用的是第二条式子。64 卡、TP = 1、PP = 4、EP = 8 时，稠密侧 DP = 16，专家侧 EDP = 2：同一张卡在注意力上属于某个数据并行副本，在专家上属于某个专家分片，两边的副本数可以不同。

## DP：切批次

每张卡一份完整模型，各拿全局 batch 的一块，反向之后 all-reduce 梯度。Ring all-reduce 的流量约是梯度体积的 \(2(p-1)/p\)，一个 step 只发生一次，可以和反向重叠。

模型状态放得下时，DP 是吞吐扩展的默认轴。放不下时，DP 仍然留着：TP 和 PP 先把一份模型切到单卡能放下，剩下的卡继续做 DP。DP = 1 表示只有一份模型，加卡不再提高样本吞吐。

### ZeRO 和 FSDP

朴素 DP 的浪费是每张卡都存同一份优化器状态。ZeRO 在 DP 组里把状态切开，算完再拼回来：

| 阶段 | 切开的状态 | 相对一份完整状态 |
|------|------------|------------------|
| ZeRO-1 | 优化器状态（那 12 字节） | 参数和梯度仍复制 |
| ZeRO-2 | 优化器 + 梯度 | 参数仍复制 |
| ZeRO-3 / FSDP | 优化器 + 梯度 + 参数 | 用到某一层时再 all-gather |

Megatron 的 distributed optimizer 对应 ZeRO-1。PyTorch FSDP 对应 ZeRO-3。

模型放得进一个节点时，ZeRO / FSDP 通常够用，代码路径也比三维并行短。模型大过一个节点之后，ZeRO-3 要在整个 DP 组上逐层搬运参数，跨机流量会压过计算。这时改用节点内 TP、跨节点 PP，再叠加 ZeRO-1，跨机通信从「每层搬参数」变成「每步同步梯度分片」。Megatron 在 175B 和 530B 上比纯 ZeRO-3 高约 70% 吞吐，原因就是这条。

## TP：切一层

Megatron 把 Transformer 一层里的线性层沿隐藏维切开。

- 列并行：输出维切开。前向各算各的，反向时对输入梯度做 all-reduce。
- 行并行：输入维切开。前向把部分和 all-reduce 回完整输出，反向不再为这一刀通信。

一层里注意力输出投影和 FFN 的第二个线性层各有一次这样的集合通信，所以 TP 的通信次数随层数涨，带宽必须高。实践中 TP 取 2、4、8，并停在一个 NVLink / NVSwitch 域里。域有多大，TP 就可以到多大：8 卡节点是 8，NVL72 这类整机域可以更大。把 TP 拉到跨 InfiniBand，集合通信通常会直接吃掉加速比。

序列并行（SP）跟在 TP 后面。纯 TP 时 LayerNorm 和 Dropout 的激活在组内是复制的；SP 把这些激活沿序列切开，集合通信从 all-reduce 换成等流量的 all-gather + reduce-scatter。Megatron 里 TP 和 EP 同时开时要打开 SP，否则序列维对不齐。

## PP：切深度

层太深、或者 TP 已经顶满一个节点而模型仍放不下，就把层分成若干 stage，每张卡只留自己那几层。前向把激活交给下一 stage，反向把梯度传回来。

气泡来自流水线填满和排空。微批数记为 \(m\)，stage 数为 \(p\)：

- 1F1B 的气泡比例大约 \((p-1)/m\)。
- 虚拟流水线让每张卡持有 \(v\) 段不连续的层，气泡大约 \((p-1)/(v m)\)，点对点次数也随之变多。\(v\) 取合法约数里的中间值。

所以 PP 要搭配足够大的全局 batch：全局 batch = 微批 × 微批数 × DP。微批数只比 PP 大一点点时，卡大部分时间在等前后 stage。

PP 的通信是相邻 stage 之间的激活，体积是微批 × 序列 × 隐藏维，频率远低于 TP 的每层集合通信，适合跨节点。Megatron-Turing NLG 530B 的一份模型是节点内 TP = 8、跨节点 PP = 35，共 280 张 A100，再用 DP 往更多节点扩。

## CP：切序列

上下文并行把一条序列切成几段，每张卡只留自己那一段激活。线性层和 LayerNorm 沿序列是逐 token 的，不用改。注意力要看整段 KV，所以 CP 组用环形点对点把 KV 传一圈，和 Ring Attention 同一类通信量；Megatron 的实现按因果掩码配平负载，并直接用 FlashAttention kernel。

CP 复制权重、只切激活，梯度同步落在 DP × CP 这个组上。序列大约 8K 以上、激活或注意力带宽成为瓶颈时再加 CP。短序列上这圈 KV 交换占不满计算，收益很小。

SP 和 CP 都碰到「序列」这个词，范围不同：SP 只处理 TP 组内部被复制的激活，CP 是独立的并行度，把网络输入和全部激活沿序列切开。

## EP：切专家

MoE 的注意力仍是稠密的，巨大的是专家 FFN。GShard 的做法是把不同专家放到不同卡上，token 由路由器选 top-k 个专家，再用 all-to-all 按专家属主重新分组，算完再 all-to-all 送回来。每张卡只存、只算自己的专家。

通信量和 token 数、top-k、隐藏维成正比，和专家参数量无关。专家越大、个数越多，EP 相对「把专家再做 TP」越合适：本地 GEMM 更大，通信量也更小。Mixtral 8×7B 上 EP = 8、TP = 1 优于 EP = 4、TP = 2。专家张量并行 ETP 默认跟稠密 TP 走，多数 MoE 应显式把 ETP 设为 1，只在单个专家本身放不下时再加大。

EP 加大时，每卡专家变少、专家显存下降，all-to-all 的域变大。EDP 加大时，同一份专家有更多副本，优化器状态可以在副本间再切，all-to-all 的域变小。两边要一起看，没有固定的更优方向。

路由不均时，忙的专家把整组卡住。容量因子、辅助损失，或者不做 token drop 的偏置均衡，都是在管这件事。EP 跨出节点之后，all-to-all 可能占到训练时间的三到四成，需要和计算重叠，不能按节点内的带宽来估。

## 怎么选

按这个顺序加维度，每加一档先跑一个 iteration，看显存峰值和通信占比。

1. **参数状态放得进单卡**：DDP。激活紧就开重计算。
2. **放不进单卡、放得进一个节点**：ZeRO-1 / ZeRO-2 / FSDP，仍是数据并行。先别切层。
3. **单层或隐藏维放不进单卡**：节点内 TP，并打开 SP。TP 停在 NVLink 域的大小，隐藏维和头数要整除。
4. **一个节点放不下整模型，或 TP 已经顶满**：PP 跨节点，并开虚拟流水线。把全局 batch 加大到微批数明显大于 PP。
5. **序列大约 8K 以上**：把一部分并行度给 CP，而不是把 TP 拉出节点。
6. **MoE**：专家用 EP，专家数整除 EP，ETP 取 1。注意力侧保留较小的 TP。EP × TP 尽量留在节点内，跨节点的规模用 PP 和 DP / EDP 补。
7. **剩下的卡给 DP**。DP 才是加卡之后提高样本吞吐的那一轴。

两组具体的账：

- **8×80GB 上全参微调 70B**。70B × 16 字节约 1.1 TB，八张卡完全切开也要每卡约 140 GB，仍超过 80 GB。这一档要么加卡，要么上优化器 offload / 更低精度优化器，单靠把 TP 设成 8 不够。
- **64×80GB 上的 70B**。Megatron 文档的起点是 TP = 4、PP = 4、CP = 2，于是 DP = 2。参数状态按 TP × PP = 16 切开后每卡约 70 GB，剩下的显存给激活。序列不长就把 CP 设回 1，DP 变成 4。

Megatron Core 文档里的起点配置（需要按自己的序列长度和互联再量）：

| 模型 | 卡数 | TP | PP | CP | EP |
|------|------|----|----|----|----|
| LLaMA-3 8B | 8 | 1 | 1 | 2 | — |
| LLaMA-3 70B | 64 | 4 | 4 | 2 | — |
| LLaMA-3.1 405B | 1024 | 8 | 8 | 2 | — |
| GPT-3 175B | 128–512 | 4 | 8 | 1 | — |
| Mixtral 8×7B | 64 | 1 | 4 | 1 | 8 |
| Mixtral 8×22B | 256 | 4 | 4 | 1 | 8 |

推理时名字相同，目标换成延迟和并发。TP 仍留在节点内，用来降单请求延迟。PP 把层切开，单请求要等所有 stage，适合堆很多请求来填管道。EP 仍然是专家 all-to-all。推理侧的 DP 是若干份完整副本各自接请求，没有梯度同步。

## 参考

- [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) — Shoeybi et al., 2019。层内张量并行。
- [Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM](https://arxiv.org/abs/2104.04473) — Narayanan et al., 2021。TP × PP × DP，以及交错流水线。
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — Rajbhandari et al., 2020。
- [Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B](https://arxiv.org/abs/2201.11990) — Smith et al., 2022。TP = 8、PP = 35 的实例。
- [GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding](https://arxiv.org/abs/2006.16668) — Lepikhin et al., 2020。专家分片与 all-to-all。
- [A Hybrid Tensor-Expert-Data Parallelism Approach](https://arxiv.org/abs/2303.06318) — Singh et al., 2023。DeepSpeed-TED。
- [Reducing Activation Recomputation in Large Transformer Models](https://arxiv.org/abs/2205.05198) — Korthikanti et al., 2022。序列并行。
- [Ring Attention with Blockwise Transformers for Near-Infinite Context](https://arxiv.org/abs/2310.01889) — Liu et al., 2023。
- [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277) — Zhao et al., 2023。
- [Megatron Core Parallelism Strategies Guide](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html)
- [Megatron Core Mixture of Experts](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/moe.html)
- [Megatron Core Context Parallel](https://docs.nvidia.com/megatron-core/developer-guide/0.18.2/user-guide/features/context_parallel.html)
