# Kimi Linear

> [Kimi Linear: An Expressive, Efficient Attention Architecture](https://arxiv.org/abs/2510.26692) — 月之暗面，2025.10。48B 总参数，每个 token 激活 3B。开放 KDA kernel 和指令模型 [Kimi-Linear-48B-A3B](https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct)。

同样是 3 : 1 混合的 [Qwen3-Next](14-qwen3-next.md) 见另一页。更早的 7 : 1 是 [MiniMax-01](17-minimax.md)。

## 这篇论文代表什么

前两家证明混合线性注意力能用、而且往往比纯线性或纯 softmax 好。Kimi Linear 要证明的更强：在同样的训练配方下，这套混合可以超过全注意力的 MLA 基线，短上下文、长上下文和 RL 都包括在内。它不是只在超长序列上「更快但更差」。

相对全 MLA，1M 上下文的 KV cache 最多减少约 75%，解码吞吐最高约 6 倍。公平对比用的是同一套规模和数据，而不是拿一个小线性模型和一个大 softmax 模型比。

## KDA：每个通道一个遗忘门

线性层是 Kimi Delta Attention，从 [Gated DeltaNet](https://arxiv.org/abs/2412.06464) 改来。Gated DeltaNet 和 Mamba2 一样，每个头一个标量门，整头的状态用同一个速度遗忘。KDA 改成通道级：状态的每个特征维度有自己的遗忘率，更接近 Gated Linear Attention 的细粒度，同时保留 delta rule 对状态的改写。

固定大小的 RNN 状态因此可以被更细地使用。哪些维度该快忘、哪些该留着，不再被头级标量绑在一起。论文同时给了一种分块算法，用对角加低秩的转移矩阵把这个门控做成在 GPU 上划算的形式。

混合是按层而不是按头：每 3 层 KDA 接 1 层全注意力。消融里 3 : 1 的训练和验证损失最好。7 : 1 训练损失接近，验证明显变差；1 : 1 验证还行，但推理更贵；纯全注意力在他们的设置里更差。

## 全局层是不带位置的 MLA

全局层用 [MLA](09-deepseek-v2.md)，并且这些层是 NoPE，完全不加位置编码。位置和「更近的 token 更重要」都交给 KDA。

NoPE 有两个工程后果：

- 推理时 MLA 可以收成纯 MQA，不必为 RoPE 保留那条解耦 key 的特殊路径。
- 长上下文不必再调 RoPE 的频率基，也不用 YaRN。

MoE 比照 Moonlight 的配置，稀疏度提高到 32 倍一类的设置：256 个专家里激活 8 个，其中包含 1 个共享专家。第一层是稠密层，用来稳住训练。48B / 3B 就是这个配比。

## 面试里怎么收束

> Kimi Linear 是 3 层 KDA 配 1 层 NoPE 的 MLA。KDA 相对 Gated DeltaNet，把遗忘门从每头一个标量改成每个通道一个。NoPE 让全局层在推理时变成 MQA，位置全部由线性层负责。48B 里激活 3B，256 个专家选 8 个、含 1 个共享专家。论点是公平对比下能超过全 MLA，而不只是更省。
