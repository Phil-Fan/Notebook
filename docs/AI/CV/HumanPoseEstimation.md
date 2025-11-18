# HPE 领域综述

[人体姿态估计：深度学习方法 [2024 指南]](https://www.v7labs.com/blog/human-pose-estimation-guide)

[【万字长文！人体姿态估计 (HPE) 入门教程】 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/596043913)

[人体姿态估计的过去，现在，未来 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/85506259)

??? note "基本信息"
    题目 ：**Vision-Based Human Pose Estimation via Deep Learning: A Survey**<br>
    Author ：[Gongjin Lan](https://arxiv.org/search/cs?searchtype=author&query=Lan,+G), [Yu Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Y), [Fei Hu](https://arxiv.org/search/cs?searchtype=author&query=Hu,+F), [Qi Hao](https://arxiv.org/search/cs?searchtype=author&query=Hao,+Q)<br>
    arXiv地址：[Vision-Based Human Pose Estimation via Deep Learning: A Survey (arxiv.org)](https://arxiv.org/abs/2308.13872)<br>

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__CV__assets__HumanPoseEstimation.assets__image-20240318194903268.webp)

## 名词解释

regression paradigm

### Deep learning

#### CNN(`Convolutional Neural Networks`)

AlexNet

ResNet

CNN 在 HPE 任务中通常分为两个主要部分：

1. **骨干网络（Backbone Network）**：这是 CNN 的第一部分，通常采用现成的、经过预训练的通用网络模型来提取图像的特征。例如，ResNet 是一个非常常用的骨干网络，它通过深层的卷积层学习图像中的高级特征。这些特征包含了图像中重要的视觉信息，为后续的姿态预测提供基础。

2. **预测头（Prediction Head）**：这是 CNN 的第二部分，负责使用骨干网络提取出的特征来预测人体的姿态。预测头的设计和实现方式可以有很多种，但它的主要任务是根据输入图像的特征，确定图像中人体各个关节的位置。

   1. 回归范式（直接预测关节坐标）在回归范式中，模型直接从输入图像预测出每个关节的坐标。这种方法通常采用全连接层（fully connected layers）来对具体的关键点坐标进行回归。这意味着模型输出的是一个坐标列表，每个坐标代表一个关节在图像中的位置。

      **举例**：假设我们想要从一张人体图像中预测头部、肩膀、肘部和手腕的位置，使用回归范式的模型将直接输出这些部位的 x 和 y 坐标值，例如，头部可能被预测为 (100, 50)，肩膀为 (120, 80)，等等。

   2. 热图预测范式（生成热图后计算关节坐标）热图预测范式先生成每个关节的热图表示，然后从这些热图中计算出关节坐标。热图是一种概率分布图，表示了关节出现在图像不同位置的可能性。在生成热图之后，通过某种方式（通常是找到热图中的最大值点）来确定关节的最终坐标。为了提高热图的分辨率，常用的操作是上采样（`upsampling`）。

      **举例**：使用热图预测范式来估计同样的头部、肩膀、肘部和手腕的位置时，模型首先为每个关节生成一张热图。例如，头部的热图中最亮的点（最大概率值所在点）位于 (102, 48)，这个点就被认为是头部的预测位置。肩膀、肘部和手腕也以同样的方式从它们各自的热图中确定位置。

#### RNN(`Recurrent Neural Networks`)

They are widely used in video-based HPE by considering videos as sequential RGB images.

#### GCN(`Graph Convolutional Networks`)

GCNs are generally expected to better exploit the relationship among key points and used for the pose refinement, joint association, 2D-to-3D pose lifting

### 方法解释

**自上而下（Top-down）方法：**

1. **流程**：首先通过人体检测器在图像中识别出每个人的位置，即为每个人生成一个边界框（bounding box），然后对每个检测到的人体边界框内的图像进行单人姿态估计。
2. **优点**：通常能提供较高的姿态估计精度，因为每个人体被单独处理，避免了不同人之间的姿态混淆。
3. **缺点**：计算量随着人数的增加而线性增加，因此在人数较多的场景中效率较低。人体检测的准确性直接影响姿态估计的结果。
4. **适用场景**：对精度要求较高的应用，如需要精细分析每个人姿态的场合。

**自下而上（Bottom-up）方法：**

1. **流程**：首先在整个图像范围内直接检测所有的人体关节点，然后使用某种算法（如图匹配、聚类等）将这些检测到的关节点根据归属分配到不同的人体上。
2. **优点**：不需要先进行人体检测，直接在图像上识别关节点，因此计算量不直接随人数增加而增加，适合于处理大规模人群的场景，具有更高的效率。
3. **缺点**：在关节点分配和人体实例的区分上可能面临更大的挑战，尤其是在人体密集或严重遮挡的场景中，可能导致精度略低于自上而下方法。
4. **适用场景**：适用于人群密集的场景，或需要实时处理的应用中。

## metrics

正确部位百分比 (PCP, Percentage of Correct Parts)
PCP 用于衡量肢体的正确检测。如果预测的两个关节位置与真实肢体关节位置之间的距离小于肢体长度的一半，则认为该肢体被正确检测。然而，这种方法有时会对较短的肢体（如前臂）造成不公平的惩罚。

检测关节百分比 (PDJ, Percentage of Detected Joints)
为了解决 PCP 提出的问题，研究者提出了一个新的评估指标。PDJ 测量预测关节与真实关节在躯干直径特定比例范围内的距离。

$PDJ = \frac{\text{检测到的关节数量}}{\text{总关节数量}}$

PDJ 有助于提高定位精度，因为所有关节的检测标准都基于相同的距离阈值，这缓解了 PCP 的缺点。

正确关键点百分比 (PCK, Percentage of Correct Key-points)
PCK 是一个准确率指标，用于衡量预测关键点和真实关节是否在特定距离阈值内。PCK 通常根据目标物体的尺度（由边界框确定）来设置。

$PCK = \frac{\text{正确检测的关键点数量}}{\text{总关键点数量}}$

阈值可以是：

PCKh@0.5：阈值为头部骨骼连接长度的 50%

- $dist(pred, gt) < 0.5 \times head\_bone\_length$

PCK@0.2：预测关节与真实关节之间的距离 < 躯干直径的 0.2 倍

- $dist(pred, gt) < 0.2 \times torso\_diameter$

有时也采用 150 毫米作为阈值。

由于较短的肢体通常对应较小的躯干和头部骨骼连接，这种方法缓解了短肢体的问题。

PCK 可用于 2D 和 3D 姿态估计（PCK3D）

基于对象关键点相似度 (OKS) 的 mAP
OKS 在 COCO 关键点挑战中常用作评估指标。其定义为：

$OKS = \frac{\sum_i \exp(-\frac{d_i^2}{2s^2k_i^2})\delta(v_i>0)}{\sum_i \delta(v_i>0)}$

其中：

$d_i$ 是真实值与预测关键点之间的欧氏距离

$s$ 是目标分割区域面积的平方根

$k_i$ 是控制衰减的每个关键点常数

$v_i$ 是可见性标志，可以是 0（未标注）、1（已标注但不可见）或 2（可见且已标注）

由于 OKS 用于计算距离（0-1），它表明预测关键点与真实关键点的接近程度。

## 主流数据集和技巧

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__CV__assets__HumanPoseEstimation.assets__image-20240318203018496.webp)

### 1. AIC (AI Challenger) Dataset

AI Challenger 是一个综合性的数据集，包含多个挑战，其中包括人体关键点检测任务。这个数据集旨在通过提供大量标注数据，推动人工智能在图像识别、语言理解等方面的研究和发展。

### 2. COCO (Common Objects in Context) Dataset

COCO 数据集是计算机视觉研究领域中最著名的数据集之一，它支持多种任务，包括目标检测、分割和人体关键点检测。COCO 数据集以其大规模和多样性而闻名，提供了大量详细标注的图像，这些图像包含了日常场景中的对象和人体。

### 3. CrowdPose Dataset

CrowdPose 数据集专注于复杂场景下的人体姿态估计，特别是在人群中。它旨在解决传统数据集忽略的问题：高度拥挤的场景中人体姿态的检测和分析。

### 4. H36M (Human 3.6 Million) Dataset

H36M 数据集是一个大规模的 3D 人体姿态数据库，提供了 360 万个 3D 人体姿态。这些数据来自于配备了标记的 9 个参与者执行各种日常活动的视频。H36M 主要用于深度学习和人体姿态估计的研究。

### 5. JHMDB (Joint-annotated Human Motion Data Base) Dataset

JHMDB 数据集是一个用于人体动作识别和姿态估计的数据集，包含从现实世界视频中提取的 21 种不同动作类别。每个视频都有相应的人体关键点标注。

### 6. MHP (Multi-Human Parsing) Dataset

MHP 数据集旨在促进多人体解析的研究，特别是在复杂场景中。它提供了大量的图像，这些图像中的每个人都有详细的像素级标注，用于身体部位的分割。

### 7. MPII Dataset

MPII Human Pose 数据集是一个大规模数据集，用于 2D 人体姿态估计。它包含了多种日常活动场景下的图像，每个图像都配有人体关键点的精确位置标注。

### 8. MPII_TRB Dataset

MPII_TRB 数据集可能是指 MPII 数据集的一个特定子集或变种，用于特定的研究或比赛任务。这个名称不是非常常见，可能需要在特定文档或资料中查找具体细节。

#### 9. OCHuman Dataset

OCHuman 数据集专注于挑战性的人体姿态估计场景，尤其是高遮挡和人体交互场景。它旨在提供一个难度更高的测试基准，以推动相关技术的进步。

### 10. PoseTrack18 Dataset

PoseTrack 是一个大规模的人体姿态估计和跟踪数据集，PoseTrack18 指的是 2018 年发布的版本。它专注于视频中的人体姿态估计和跟踪，提供了大量连续帧中人体姿态的标注。

## 2D HPE

### 单人图像

### 多人图像

### 2D 视频

### 鲁棒性分析

## 3D HPE

## 应用领域
