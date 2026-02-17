# 随机变量

## Probability

### Random variables

### statistics

[从随机变量到随机向量再到随机矩阵：那个你不一定知道的矩阵高斯分布 - 知乎](https://zhuanlan.zhihu.com/p/26286575)

统计不相关：互协方差矩阵是 0 矩阵 $C_{xy} = O_{m\times n}$
正交：互相关矩阵式零矩阵 $R_{xy} = O_{m\times n}$

#### 均值向量 (Mean Vector)

对于随机向量 $\mathbf{x}$，其均值向量 $\mu_x$ 定义为：

$$
\mu_x = E\{\mathbf{x}(\xi)\} = \begin{bmatrix} E\{x_1(\xi)\} \\ E\{x_2(\xi)\} \\ \vdots \\ E\{x_m(\xi)\} \end{bmatrix} = \begin{bmatrix} \mu_1 \\ \mu_2 \\ \vdots \\ \mu_m \end{bmatrix}
$$

#### correlation 相关矩阵

**自相关**矩阵 $R_x$ 定义为：

$$
R_x = E\{\mathbf{x}(\xi)\mathbf{x}^H(\xi)\} = \begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1m} \\ r_{21} & r_{22} & \cdots & r_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ r_{m1} & r_{m2} & \cdots & r_{mm} \end{bmatrix}
$$

其中，$\mathbf{x}^H(\xi)$ 表示 $\mathbf{x}(\xi)$ 的共轭转置，$r_{ij}$ 表示 $x_i(\xi)$ 和 $x_j(\xi)$ 之间的自相关函数。自相关矩阵是复共轭对称矩阵，即 Hermitian 矩阵。

互相关

$$
R_{xy} = E\{\mathbf{x}(\xi)\mathbf{y}^H(\xi)\} = \begin{bmatrix} r_{x_1,y_1} & r_{x_1,y_2} & \cdots & r_{x_1,y_n} \\ r_{x_2,y_1} & r_{x_2,y_2} & \cdots & r_{x_2,y_n} \\ \vdots & \vdots & \ddots & \vdots \\ r_{x_m,y_1} & r_{x_m,y_2} & \cdots & r_{x_m,y_n} \end{bmatrix}
$$

其中，$r_{x_i,y_j}$ 表示 $x_i(\xi)$ 和 $y_j(\xi)$ 之间的互相关函数。

#### Covariance 协方差矩阵

[如何通俗地解释协方差｜马同学图解数学](https://www.bilibili.com/video/BV1gY4y187TL)

[【什么是自相关矩阵，自协方差矩阵，互相关矩阵，互协方差矩阵？】 - 知乎](https://zhuanlan.zhihu.com/p/447221519)
**自协方差**矩阵 $C_x$ 定义为：

$$
C_x = E\{\left[\mathbf{x}(\xi) - \mu_x\right]\left[\mathbf{x}(\xi) - \mu_x\right]^H\} = \begin{bmatrix} c_{11} & c_{12} & \cdots & c_{1m} \\ c_{21} & c_{22} & \cdots & c_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ c_{m1} & c_{m2} & \cdots & c_{mm} \end{bmatrix}
$$

其中，$c_{ij}$ 表示 $x_i(\xi)$ 和 $x_j(\xi)$ 之间的协方差。自协方差矩阵也是复共轭对称矩阵。

$$
\mathbf{C_x} = \mathbf{R_x} - \mathbf{\mu_x} \mathbf{\mu_x}^H
$$

**互协方差**矩阵 $C_{xy}$ 定义为：

$$
C_{xy} = E\{\left[\mathbf{x}(\xi) - \mu_x\right]\left[\mathbf{y}(\xi) - \mu_y\right]^H\} = \begin{bmatrix} c_{x_1,y_1} & c_{x_1,y_2} & \cdots & c_{x_1,y_n} \\ c_{x_2,y_1} & c_{x_2,y_2} & \cdots & c_{x_2,y_n} \\ \vdots & \vdots & \ddots & \vdots \\ c_{x_m,y_1} & c_{x_m,y_2} & \cdots & c_{x_m,y_n} \end{bmatrix}
$$

其中，$c_{x_i,y_j}$ 表示 $x_i(\xi)$ 和 $y_j(\xi)$ 之间的协方差。

#### 相关系数

相关系数矩阵（Correlation Matrix）用于衡量随机向量中各个分量之间的线性相关程度。对于随机向量 $\mathbf{x}$，其相关系数矩阵 $\mathbf{R}_x$ 定义为：

$$\mathbf{R}_x = \begin{bmatrix} 1 & \rho_{12} & \rho_{13} & \cdots & \rho_{1m} \\ \rho_{21} & 1 & \rho_{23} & \cdots & \rho_{2m} \\ \rho_{31} & \rho_{32} & 1 & \cdots & \rho_{3m} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \rho_{m1} & \rho_{m2} & \rho_{m3} & \cdots & 1 \end{bmatrix}$$

其中，$\rho_{ij}$ 表示 $x_i(\xi)$ 和 $x_j(\xi)$ 之间的相关系数，其取值范围为 $[-1, 1]$。具体来说，相关系数 $\rho_{ij}$ 定义为：

$$\rho_{ij} = \frac{E\{[x_i(\xi) - \mu_i][x_j(\xi) - \mu_j]^*\}}{\sqrt{E\{[x_i(\xi) - \mu_i]^2\}}\sqrt{E\{[x_j(\xi) - \mu_j]^2\}}}$$

其中，$\mu_i = E\{x_i(\xi)\}$ 和 $\mu_j = E\{x_j(\xi)\}$ 分别表示 $x_i(\xi)$ 和 $x_j(\xi)$ 的均值，$E\{\cdot\}$ 表示期望操作，$[\cdot]^*$ 表示复共轭。

相关系数矩阵具有以下性质：

1. 对角线上的元素全为 1，即 $\rho_{ii} = 1$。
2. 相关系数矩阵是复共轭对称矩阵，即 $\mathbf{R}_x = \mathbf{R}_x^H$。
3. 相关系数矩阵的行列式为 1，即 $\det(\mathbf{R}_x) = 1$。

### 高斯随机变量

!!! note "为什么噪声一般建模为高斯"
    中心极限定理：独立同分布的随机变量的和，其分布趋近于高斯分布

### complex normal

### Probability distributions

### Bayes’ Theorem（todo）

### Probability Distributions

## Information theory

### Entropy

不确定性函数$f$是概率$P$的减函数；两个独立符号所产生的不确定性应等于各自不确定性之和，即$f(P1,P2)=f(P1)+f(P2)$，这称为可加性。同时满足这两个条件的函数$f$是对数函数，即$f(P)=\log\frac{1}{P} = -\log P$。

### Kullback–Leibler Divergence (todo)

### Cross-entropy（todo）

## 概率

### 概率与统计

| 中文名 | 英文名 |
| -------------------- | ------------------------------- |
| 概率密度函数 | Probability Density Function (pdf) |
| 累计分布函数 | Cumulative Distribution Function (cdf) |
| 均值向量 | Mean Vector |
| 相关矩阵 | Correlation Matrix |
| 协方差矩阵 | Covariance Matrix |

### 信息论

| 中文名 | 英文名 |
| -------------------- | ------------------------------- |
| 熵 | Entropy |
| Kullback–Leibler 散度 | Kullback–Leibler Divergence |
| 交叉熵 | Cross-entropy |
