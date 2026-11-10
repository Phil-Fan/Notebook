# Llama 4

> [The Llama 4 herd](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) — Meta，2025.04。没有单独的架构论文。结构以官方博客、[Hugging Face 的说明](https://huggingface.co/blog/llama4-release) 和 [llama-models 实现](https://github.com/meta-llama/llama-models/blob/main/models/llama4/model.py) 为准。

上一代稠密配方见 [Llama 3](15-llama3.md)。

## 规模

| 模型 | 总参数 | 激活 | 专家 | 发布时的上下文 | 状态 |
|------|--------|------|------|----------------|------|
| Scout | 109B | 17B | 16 | 10M | 开放权重 |
| Maverick | 400B | 17B | 128 | 1M | 开放权重 |
| Behemoth | 未作为权重发布 | 288B | 16 | — | 发布时仍是训练中的教师 |

两个开放模型的激活参数都是 17B。Scout 在 INT4 下被宣称可以放进单张 H100。Behemoth 用来蒸馏 Scout 和 Maverick，不要把它说成已经可以下载的模型。

原生多模态用 early fusion：文本和图像在训练早期就进同一个模型，而不是在一个纯语言模型上后挂视觉编码器。知识截止日期在模型卡里是 2024 年 8 月。

## MoE：一个路由专家

这是 Llama 第一次用 MoE。Maverick 的讲法最具体：稠密层和 MoE 层交替。MoE 层有 128 个路由专家和 1 个共享专家。每个 token 进入共享专家，再进入 1 个路由专家。

和 [DeepSeek-V3](10-deepseek-v3.md) 的「256 选 8，专家很窄」相反。Llama 4 专家更大、选得更少，激活比压到 17B / 400B，优先的是服务成本。Scout 是 16 个专家的 MoE，同样 17B 激活；交错稠密层是 Maverick 被明确写出来的配置。

块里没有 MLA，也没有线性注意力。注意力仍是 GQA 这一类分组查询。

## iRoPE

标准 RoPE 每一层都带位置。长度外推时，频率基和注意力 softmax 会一起出问题：序列越长，softmax 的质量越摊越平。

Llama 4 把层分成两种，每 4 层一轮：

- **3 层 RoPE。** 只做长度 8192 的分块局部注意力。这些层负责近处的词序，不看整段上下文。
- **1 层 NoPE。** 不加位置编码，使用完整因果掩码。这些层按内容做全局聚合。推理时对这一层做 attention temperature scaling，而且把缩放做成不影响短上下文的形式，避免长序列上 softmax 饱和。

Meta 把「NoPE 与 RoPE 交错，再加上这套温度」叫做 iRoPE。判断是：不是每一层都需要知道 token 在句子里的绝对位置。全局层故意不加 RoPE，长度外推不必被频率基绑死。

10M 和 1M 是发布时的产品上下文。讲的时候把位置编码的结构和「这个长度上的实际稳定性」分开。

## 面试里怎么收束

> Llama 4 代表开源权重侧改走 MoE，但路线和 DeepSeek 不同：Maverick 每个 token 只进 1 个路由专家，再加共享专家，激活 17B。长上下文靠 iRoPE，而不是 MLA 或线性注意力。每 4 层里 3 层 RoPE 只看 8192 的局部块，1 层 NoPE 看全文。
