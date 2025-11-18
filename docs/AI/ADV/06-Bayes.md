# 06 | Bayes

## 范式

### 人工智能范式

第一代是基于符号模型

第二代是基于亚符号模型 —— 数据驱动

### 编程范式变化

- 传统编程
  - 用 C++, Java, Python 等语言
  - 每行代码均是明确的
  - 实现程序员直接设定的功能

- 面向人工智能的编程
  - 更加抽象、包括权重等不易理解的部分
  - 间接的通过优化目标函数，让程序具有期望的功能

  - 计算同质化
  - 便于硬件实现
  - 模块化
  - 计算和存储代价是固定的
  - 实际性能好！

### 问题

- 过于自信，不知道自己知不知道
- 鲁棒性差
- 可解释性不好

刻画不确定性是解决问题的关键

- 数据不确定性
- 模型不确定性：数据集大小增加 有用信息增加不多

知道自己不知道！

## bayes

### 概率图模型 Bayes+ 图论

### 贝叶斯网络

### Bayes + 神经网络

- David mackay - Bayesian Methods for adaptive models
- RM Neal - Bayesian Learning for Neural Networks

当隐含神经元趋于无穷的时候，收敛到高斯过程

### model

构建灵活高效的深度贝叶斯模型

- 隐函数定理
- 构造可微分隐函数
- 一层隐函数严格优于手工
- 扩散模型，已有学习方法是次优的

算法的稳定性分析与加强：使用控制领域分析稳定性的方法

- understanding & stablizing GANS via Control Theory

Analytic-DPM ICLR 2022

高效贝叶斯推断算法

### algorithms

### programming

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=260100976&bvid=BV1be411g7u7&cid=818975260&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

有拒绝的学习
