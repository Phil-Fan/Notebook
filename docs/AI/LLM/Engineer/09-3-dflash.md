# DFlash: Block Diffusion for Flash Speculative Decoding

<iframe src="https://arxiv.org/abs/2602.06036" width="100%" height="600" style="border:0;border-radius:8px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="DFlash arXiv"></iframe>

若 iframe 无法加载，可直接访问：[arXiv 2602.06036](https://arxiv.org/abs/2602.06036)

## 概述

DFlash 提出了一种基于**块扩散（Block Diffusion）**的推测解码框架，用轻量级扩散模型替代传统自回归草稿模型，在单次前向传播中并行生成整个 token 块，再由目标模型验证，实现**无损加速**。

| 属性 | 说明 |
|------|------|
| 论文 | DFlash: Block Diffusion for Flash Speculative Decoding |
| 作者 | Jian Chen, Yesheng Liang, Zhijian Liu 等 |
| 发表 | ICML 2026 |
| 加速 | 最高 6x+ 无损加速 |
| vs EAGLE-3 | 最高 2.5x 更高吞吐 |
| 代码 | [GitHub](https://github.com/efo-del/DFlash) |

## 动机

传统推测解码的瓶颈：

- **自回归草稿模型**仍然逐 token 生成，加速有限
- **纯扩散模型**做草稿面临生成质量和去噪步数的权衡
- 草稿与目标模型之间的**上下文对齐**不够紧密，导致接受率低

DFlash 的核心思路：将扩散模型作为**专业块预测器**，结合自回归验证的无损性。

## 方法

### 整体架构

```text
目标模型 (Target)
  ↓ 提取多层 hidden states
  ↓ 融合为 context features
  ↓ KV 注入
草稿模型 (Block Diffusion Draft)
  ↓ 单次前向传播 → 并行生成一个 token 块
  ↓
目标模型验证 (Verify)
  ↓ accept / reject
  ↓
输出
```

### 三大核心创新

#### 1. 上下文特征提取（Context Feature Extraction）

从目标模型中提取**多层隐层表示**，融合成紧凑的上下文特征向量，为草稿模型提供强条件信号。

#### 2. KV 注入（KV Injection）

将上下文特征直接注入草稿模型的 **Key-Value 投影**中并缓存重用：

- 提供一致且强大的条件化支持
- 避免额外拼接 token 带来的开销
- 支持 prefix sharing

#### 3. 块级扩散解码（Block Diffusion Decoding）

单次前向传播中，通过扩散过程**并行解码整个掩码块**：

- 大幅降低延迟
- 提升硬件利用率
- 一次生成多个 token，而非逐个

### Immediate Materialization

提前运行投影计算以节省显存空间，并通过以下技术优化：

- **Fused Triton kernels**：融合算子减少 kernel launch 开销
- **Layer-batched linear projections**：跨层批量线性投影

### 训练策略

| 技术 | 说明 |
|------|------|
| 掩码块构建 | 随机采样锚点构建掩码块，训练行为与推理对齐 |
| 指数衰减损失加权 | 强调早期预测的准确性 |
| 嵌入共享 | 草稿模型与目标模型共享 embedding，仅更新轻量 Transformer 层 |
| 参数效率 | 草稿模型约 1.73B 参数（以 Qwen3.6-27B-DFlash 为例） |

## 实验结果

### 主要加速数据

| 模型 / 任务 | DFlash 加速 | EAGLE-3 加速 |
|-------------|------------|-------------|
| Qwen 3-4B, GSM8K | 3.3x | 2.1x |
| Qwen 3-4B, HumanEval | 3.2x | 2.2x |
| Qwen 3-4B, MT-Bench | 2.2x | 1.4x |
| Qwen 3.5 397B-A17B (8×B200) | >4.3x baseline | — |
| 多种模型平均 | ~6x | ~2.4x |

### 消融实验结论

- **5 层**草稿模型在成本与质量间取得最佳平衡
- **大尺寸块训练**具备良好泛化能力
- 高温采样和推理模式下仍保持高效吞吐

## 工程部署

### ModelScope 模型

| 模型 | 链接 |
|------|------|
| Qwen3.6-27B-DFlash | [ModelScope](https://modelscope.cn/models/z-lab/Qwen3.6-27B-DFlash) |
| Qwen3.5-397B-A17B-DFlash | [ModelScope](https://modelscope.cn/models/lmsys/Qwen3.5-397B-A17B-DFlash) |
| gpt-oss-120b-DFlash | [ModelScope](https://modelscope.cn/models/z-lab/gpt-oss-120b-DFlash) |
| GLM-5.2-FP8-DFlash | [ModelScope](https://modelscope.cn/models/UCloud-AILab/GLM-5.2-FP8-DFlash) |

### vLLM 部署

```bash
pip install vllm  # 需使用 DFlash 支持的 PR 版本
vllm serve <target_model> \
  --speculative-config '{"path": "<dflash_drafter_path>"}'
```

### SGLang 部署

```bash
# 需使用 Spec V2 引擎
python -m sglang.launch_server \
  --model-path <target_model> \
  --speculative-algorithm DFLASH \
  --speculative-draft-model-path <dflash_drafter_path>
```

### Spec V2 引擎优化

DFlash V2 集成 SGLang Spec V2 引擎，进一步优化：

- **Overlap scheduler**：host 端清理（`pop_and_process`）与 GPU 执行重叠
- **最小化 host-device 同步**瓶颈
- Qwen 3-8B 单 B200 上吞吐从 11.4 → 15.3 ktok/s（~33% 提升）

## ModelScope 论文笔记

> 来源：[ModelScope 论文页](https://modelscope.cn/papers/2602.06036)

ModelScope 评价该方案为"**范式级突破（paradigm-level breakthrough）**"，认为研究团队在高效推理领域展现了持续的影响力和领导力。

核心方法论总结：

1. 用轻量扩散模型替代自回归草稿，消除序列瓶颈
2. 通过 KV 注入将目标模型的上下文特征直接注入草稿网络，保证高接受率
3. 块级扩散在单次前向传播中并行生成，解决质量 - 延迟权衡

相关模型关联：EAGLE-3、LLaDA 等块扩散架构。

## 与 Speculative Decoding 系列的关系

```text
Speculative Decoding (Leviathan et al., 2023)
  ├── 草稿模型：小 AR 模型逐 token 生成
  ├── Medusa：多个解码头并行预测
  ├── EAGLE / EAGLE-2 / EAGLE-3：特征预测 + 树注意力
  ├── MTP：Multi-Token Prediction
  └── DFlash：块扩散草稿 ← 本页
        ├── V1：block diffusion + KV injection
        └── V2：Spec V2 引擎 + overlap scheduler
```

DFlash 的核心区别在于：草稿不再是自回归的，而是**扩散式的并行块生成**，从根本上改变了 draft 阶段的计算模式。

## 参考资料

- [arXiv: DFlash: Block Diffusion for Flash Speculative Decoding](https://arxiv.org/abs/2602.06036)
- [HuggingFace Papers](https://huggingface.co/papers/2602.06036)
- [ModelScope 论文页](https://modelscope.cn/papers/2602.06036)
- [LMSYS Blog: DFlash V2 + Spec V2](https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/)
- [知乎：大模型推理加速：从 EAGLE 到 DFlash](https://zhuanlan.zhihu.com/p/2004595351189987521)
- [Moonlight Review](https://www.themoonlight.io/zh/review/dflash-block-diffusion-for-flash-speculative-decoding)
- [Speculative Decoding 笔记](09-2-speculative-decoding.md)
