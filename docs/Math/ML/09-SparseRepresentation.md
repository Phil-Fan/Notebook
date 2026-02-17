# 09 | 特征选择与稀疏学习

## 稀疏表示 | Sparse Representation

### 稀疏 Sparse 是什么

稀疏向量：一个大多数元素为 0 的向量/矩阵成为稀疏向量/矩阵

绝大多数为 0，但还是有少数不为 0

!!! note "稀疏参数可以提高可解释性"

    例如，预测一个学生的期末成绩($y$)可以用多个因素($x$)的线性组合来表示:

    $$
    y = a_1x_1 + a_2x_2 + a_3x_3 + a_4x_4 + a_5x_5
    $$

    其中 $x_1 \sim x_5$ 分别代表:作业完成度、上课出勤率、学习心情、数学基础、课外复习时间

    非稀疏的参数可能是:$a = [0.3, 0.2, 0.15, 0.25, 0.1]$这表示所有因素都对成绩有一定影响，很难判断哪个因素最关键。

    稀疏的参数可能是:$a = [0.6, 0.4, 0, 0, 0]$，这清晰地表明:作业完成度和上课出勤率是影响成绩的主要因素，而其他因素的影响可以忽略不计。这样的模型更容易解释"为什么会得到这个成绩"。

L1 正则化，一般交叉位置在坐标轴上，可解释性增强

### 如何建模

高斯分布不适合建立稀疏模型

栅极分布，一个参数为 0，另一个参数不为 0；我们希望在栅极采样到点

重尾分布：laplace、混合高斯

### 压缩感知 | Compressive Sensing

**奈奎斯特采样定理**：如果采样频率大于信号最高频率的 2 倍，则可以无失真地恢复信号

**解决问题**：2008-2010 年，陶哲轩，特定条件下突破奈奎斯特采样定理，是否能在更小的频率下恢复信号

即在已知$y$的情况下，把$x$恢复出来

$$
y_{m\times 1} = A_{m\times n}x_{n\times 1}
$$

Nyquist 没有用到的知识：复杂信号，可以表示在某个基底之下，在这个基底之下是稀疏的

$$
x_{n\times 1} = \Phi_{n\times q} \alpha_{q\times 1}
$$

对于$\alpha$来说，如果其中只有 k 个非零元素，其余元素都为 0，则称$\alpha$是 k-sparse 的。此时$x$在基底$\Phi$下具有 k-稀疏性。

> 例如当$k=1$时，$\alpha = \begin{bmatrix} 1 \\ 0 \\\dots\\ 0 \end{bmatrix}$就是一个 1-sparse 向量。

所以可以非线性的重构问题建模为下面的优化问题

$$
\begin{aligned}
\min_{\alpha} \| y - A \Phi \alpha \|_2^2\\
\text{s.t.}\quad \| \alpha \|_0 \leq k
\end{aligned}
$$

其中，$\| \alpha \|_0$ 表示$\alpha$中非零元素的个数。

而压缩感知就是研究在什么条件下，可以恢复出$x$

#### 条件

- $k$ 稀疏度
- $m$ 采样数
- $\Phi$ 采样矩阵

$\Phi \cdot A$ 满足 RIP principle
$m \approx k \cdot c$ 线性

#### 采样矩阵$A$的设计

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Math__ML__assets__09-SparseRepresentation.assets__20241017153420.webp)

- 规则采样下，每个样本点仅包含局部信息
- 随机采样下，每个样本点包含了全局信息

$A$是随机采样，更容易满足 RIP principle

the glory of randomness

## Representation Learning

提升模型表达能力：线性 to 非线性；确定性模型 to 统计模型

### 线性的模型

$$
y = \mathbf{G}c
$$

完备基

- 固定基底：正交、DCT、小波
- 数据驱动：PCA（主成分分析）EVD/SVD

过完备基：$y = A_{m \times n}x,\quad m < n$,列的个数大于行的个数

- 稀疏编码：K-SVD、OMP

### 非线性的模型

自回归

GAN

### 统计的模型

VAE

diffusion

## 特征选择

IBP: indian buffet process

自动学习哪些元可以去掉

[Indian Buffet Process(印度自助餐过程) 介绍-CSDN 博客](https://blog.csdn.net/qy20115549/article/details/78532939)
自动学习哪些元可以去掉
