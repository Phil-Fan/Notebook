# 06 | VLA 数据集与评测

## 主要数据集

### Open X-Embodiment

推动 VLA 发展的核心数据联盟，由 Google DeepMind 联合全球 33 个实验室创建。

- **论文**：[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)
- **规模**：60+ 数据集、**100 万+ 轨迹**、22 种机器人形态
- **覆盖**：单臂、双臂、移动操作、四足、无人机
- **官网**：[robotics-transformer-x.github.io](https://robotics-transformer-x.github.io/)

<iframe src="https://arxiv.org/abs/2310.08864" width="100%" height="500px" style="border:1px solid #ddd;border-radius:4px;" allowfullscreen></iframe>

### DROID

大规模野外真实环境操作数据集。

- **论文**：[DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945)
- **规模**：76k 轨迹、564 个多样场景、18 个机构
- **特点**：野外环境（非实验室），自然光照、复杂背景
- **官网**：[droid-dataset.github.io](https://droid-dataset.github.io/)

### BridgeData V2

桌面操作的标准数据集，使用 WidowX 机器人。

- **规模**：60k+ 轨迹，涵盖 100+ 物体类别
- **任务类型**：拾放、推拉、开关抽屉等
- 被 Octo、OpenVLA 等多个模型用于训练和评估

### ALOHA 双臂数据集

Stanford ALOHA 平台的双臂精细操作数据。

- **规模**：~3k 双臂轨迹
- **特点**：精细操作（倒水、叠毛巾、开瓶盖等）
- 是 RDT-1B、ACT 等方法的核心训练/评估数据

### 数据集对比

| 数据集 | 轨迹数 | 机器人 | 场景 | 年份 |
|--------|--------|--------|------|------|
| Open X-Embodiment | 1M+ | 22 种 | 混合 | 2023-24 |
| DROID | 76k | 多平台 | 野外 | 2024 |
| BridgeData V2 | 60k+ | WidowX | 实验室 | 2023-24 |
| ALOHA | ~3k | 双臂 ALOHA | 实验室 | 2023 |

---

## 标准化评测基准

### LIBERO

最常用的 VLA 标准化评估平台。

- 5 个任务套件、130 个程序化任务
- 涵盖物体泛化、空间泛化、目标泛化
- 支持仿真评估，可复现对比

### CALVIN

长序列语言条件操作基准。

- 多任务连续执行（不重置环境）
- 评估长序列完成率和任务泛化
- 需要模型自行管理任务切换

### RLBench

100 个精心设计的操作任务。

- 支持多种操作类型：拾放、推拉、按钮、开门等
- 每个任务有多个变体（物体、位置随机化）
- 常用作 single-task BC 基线

### VLABench (ICCV 2025)

大规模语言条件长序列操作基准。

- 强调语言理解和长序列规划
- 更贴近真实场景的复杂指令

### VLA Evaluation Harness (AI2)

AI2 的统一评估框架，提供公开 Leaderboard。

- **Leaderboard**：[allenai.github.io/vla-evaluation-harness/leaderboard/](https://allenai.github.io/vla-evaluation-harness/leaderboard/)
- 每月更新
- 整合多种 benchmark，标准化评估协议

---

## 真实世界评估

标准化程度仍低，各实验室使用不同协议。AI2 框架正在整理论文中报告的真实世界评估结果。

### 关键评估维度

1. **成功率**：任务完成比例
2. **泛化能力**：新物体、新场景、新指令的 zero-shot / few-shot
3. **鲁棒性**：视觉扰动、物理扰动下的性能保持
4. **长序列完成率**：多步任务的端到端完成率
5. **效率**：完成任务的平均步数和时间

## Acknowledgement

- [Open X-Embodiment](https://arxiv.org/abs/2310.08864)
- [DROID](https://arxiv.org/abs/2403.12945)
- [VLA Evaluation Harness](https://github.com/allenai/vla-evaluation-harness)
- [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
