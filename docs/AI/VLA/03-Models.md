# 03 | VLA 模型族

## RT 系列（Google DeepMind）

### RT-1 (2022)

首个基于 Transformer 的端到端机器人控制模型，在 130k 真实世界演示上训练。使用 EfficientNet 视觉编码 + FiLM 条件语言，通过 Transformer 输出离散化动作。

- **论文**：[RT-1: Robotics Transformer for Real-World Control](https://arxiv.org/abs/2212.06817)
- **数据**：130k 真实演示，Everyday Robots 平台
- **动作空间**：7 DoF 末端位姿 + 夹爪 + 基座

<iframe src="https://arxiv.org/abs/2212.06817" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

### RT-2 (2023)

里程碑工作：首次将 web-scale VLM（PaLI-X/PaLM-E）直接作为 VLA 骨干，证明互联网规模视觉-语言知识可迁移到机器人控制。

- **论文**：[RT-2: Vision-Language-Action Models](https://arxiv.org/abs/2307.15818)
- **核心创新**：将连续动作离散化为 token，与文本 token 统一处理
- **关键发现**：web 预训练带来 emergent 泛化能力（未见物体、未见指令、未见场景）
- **Co-fine-tuning**：机器人数据 + 原始 VLM 数据混合训练

<iframe src="https://arxiv.org/abs/2307.15818" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

### RT-X / RT-2-X (2024)

跨具身泛化的里程碑：在 Open X-Embodiment 多机器人数据上 co-fine-tuning。

- **论文**：[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)
- 核心结论：**多机器人联合训练能提升特定机器人的泛化性能**
- 数据多样性比单机器人数据量更关键

<iframe src="https://arxiv.org/abs/2310.08864" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

---

## Octo（UC Berkeley, 2024）

开源通才机器人策略，基于 Transformer 扩散解码器。

- **论文**：[Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)
- **参数**：27M-93M，提供 4 个模型尺寸
- **视觉**：DINOv2；**语言**：Gemma（可选）
- **训练数据**：Open X-Embodiment 子集（25 数据集，~800k 轨迹）
- **许可**：MIT 全开源

<iframe src="https://arxiv.org/abs/2405.12213" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

---

## OpenVLA（Stanford/UC Berkeley, 2024）

全开源 7B VLA，目前社区使用最广泛的开源 VLA 基础模型。

- **论文**：[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)
- **参数**：7B（Llama-2 7B + SigLIP + DINOv2）
- **预训练数据**：970k 轨迹（Open X-Embodiment）
- **许可**：Apache 2.0，模型/代码/数据全开源
- **亮点**：支持 LoRA 高效微调，29 任务 zero-shot 平均成功率高于 RT-2-X 和 Octo
- **GitHub**：[github.com/openvla/openvla](https://github.com/openvla/openvla)

<iframe src="https://arxiv.org/abs/2406.09246" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

---

## π0（Physical Intelligence, 2024）

基于流匹配（Flow Matching）的通用 VLA，演示了叠衣服等高难度精细操作。

- **论文**：[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)
- **参数**：3B（PaliGemma VLM + 流匹配动作专家），另有 470M pi0-small
- **动作生成**：流匹配输出连续高频信号（最高 50 Hz）
- **训练数据**：Open X-Embodiment + 8 种机器人平台内部数据
- **关键成果**：在叠衣服、装袋、清垃圾等任务上显著超越 OpenVLA 和 Octo

<iframe src="https://arxiv.org/abs/2410.24164" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

---

## RDT-1B（清华, 2024）

基于扩散 Transformer 的双臂操作基础模型，推理速度达到 381 actions/sec。

- **论文**：[RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)
- **参数**：1.2B
- **统一动作空间**：将不同机器人控制映射到归一化表示
- **训练数据**：46 个数据集、100 万+ episodes 预训练 + 6K+ episodes ALOHA 双臂微调
- **HuggingFace**：[robotics-diffusion-transformer/rdt-1b](https://huggingface.co/robotics-diffusion-transformer/rdt-1b)

<iframe src="https://arxiv.org/abs/2410.07864" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

---

## Helix（Figure AI, 2025）

双系统 VLA，首次在完整人形机器人上实现 200Hz 全身控制。

- **发布**：[Helix: A VLA Model for Generalist Humanoid Control](https://www.figure.ai/news/helix)
- **架构**：System 2（7B VLM, 7-9Hz）→ System 1（80M 交叉注意力头, 200Hz）
- **动作空间**：35 DoF（手指、手腕、躯干），直接输出连续电机信号
- **训练数据**：~500 小时遥操作演示，自动 VLM 生成 hindsight instruction
- **亮点**：zero-shot 多机器人协作，零样本泛化到未见物品

---

## GR00T N1（NVIDIA, 2025）

人形机器人专用开源基础模型。

- **论文**：[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- 双系统架构，配套 NVIDIA Isaac Sim 仿真框架
- 支持仿真训练到真实迁移

<iframe src="https://arxiv.org/abs/2503.14734" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

---

## Gemini Robotics（Google DeepMind, 2025）

- **发布**：[Gemini Robotics](https://deepmind.google/models/gemini-robotics/)
- VLA + Embodied Reasoning (ER) 双模型配对
- ER 模型专精空间推理，可自主多步规划，支持工具调用
- 三个设计原则：通用性、交互性、灵巧性

---

## 其他重要模型

| 模型 | 机构 | 年份 | 亮点 |
|------|------|------|------|
| **CogVLA** | 清华 | 2025 | 认知对齐 VLA，instruction-driven routing，NeurIPS 2025 |
| **Qwen-VLA** | 阿里 | 2025 | 基于 Qwen 系列，跨具身统一 |
| **CogACT** | 清华 | 2025 | 认知驱动动作生成，开源 |
| **UniPi** | Google | 2023 | 通用策略，文本+视频+动作统一 |
| **GATO** | DeepMind | 2022 | 多任务多模态通才 agent |

## 模型能力对比

| 模型 | 参数 | 推理频率 | 开源 | 多具身 | 代表性任务 |
|------|------|---------|------|--------|-----------|
| RT-2 | 55B | 1-3 Hz | 否 | 有限 | 桌面操作 |
| Octo | 27-93M | 1-10 Hz | MIT | 是 | 通用操作 |
| OpenVLA | 7B | 1-5 Hz | Apache 2.0 | 是 | 通用操作 |
| π0 | 3B | 10-50 Hz | 部分 | 是 | 精细操作 |
| RDT-1B | 1.2B | ~381 Hz | MIT | 是 | 双臂操作 |
| Helix | 7B+80M | 200 Hz | 否 | 人形 | 全身控制 |
| GR00T N1 | — | — | 开源 | 人形 | 全身控制 |

## Acknowledgement

- [Awesome-VLA-Papers](https://github.com/Psi-Robot/Awesome-VLA-Papers)
- [VLA Survey (2025)](https://vla-survey.github.io/)
