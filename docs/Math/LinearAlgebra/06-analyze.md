# 06 | 特征分析

为什么要研究特征分析？

给系统一个很好的表征

找到复杂信号的简单表达

## 线性空间

## 基与坐标

### 正交化

我们可以采集到很多信号，可以用均值、协方差来表征

但是，信号可能是耦合关联的，这说明有冗余信息

我们希望建立一个向量组，元素和元素之间是无关的，协方差矩阵是对角矩阵

### 线性映射

线性映射（Linear Mapping）是指满足齐次性（Homogeneity）和叠加性（Additivity）的映射。

$$
T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})
$$

其中，$c_1$ 和 $c_2$ 是任意标量，$\mathbf{u}$ 和 $\mathbf{v}$ 是任意向量。

举例：投影矩阵

!!! example "正交投影矩阵"

    平面，向y轴投影

    $$
    \omega = T(\begin{bmatrix} x \\ y \end{bmatrix})
    $$

    $$
    T = \begin{bmatrix} 0&0\\0&1 \end{bmatrix}
    $$

## 特征值

对于方阵$A$，满足以下方程的$\lambda$称为特征值

第一定义

$$
\mathbf{A} \mathbf{v} = \lambda \mathbf{v}
$$

第二定义

$$
det(\mathbf{A} - \lambda \mathbf{I}) = 0
$$

- $A = A^H$，特征值为实数
- 同一特征值的重复次数称为代数重数
- 特征值的个数称为几何重数

特征值和正定性

- 特征值为正，矩阵正定
- 特征值非负，矩阵半正定
- 特征值为负，矩阵负定
- 特征值非正，矩阵半负定
- 特征值有正有负，矩阵不定

性质

$$
det(A) = \prod_{i=1}^n \lambda_i
$$

$$
tr(A) = \sum_{i=1}^n \lambda_i
$$

### 谱

矩阵的谱是指该矩阵的所有特征值的集合：

$$
\sigma(A)=\{\lambda_1,\lambda_2,...,\lambda_n\}
$$

矩阵的谱半径是该矩阵所有特征值的绝对值中的最大值：

$$
\rho(A)=\max\{|\lambda_1|,|\lambda_2|,...,|\lambda_n|\}
$$

### 矩阵多项式

假设 $A$ 是一个$n\times n$的方阵，$p(A)$ 是以矩阵$A$为变量的一个矩阵多项式，即：

$$
p(A)=c_0I+c_1A+c_2A^2+...+c_kA^k
$$

其中，$c_0, c_1, . . . , c_k$ 是常数，$I$ 是单位矩阵。

矩阵$A$的特征值为$\lambda_1,\lambda_2,...,\lambda_n$,则矩阵多项式$p(A)$的特征值为：

$$
p(\lambda_i)=c_0+c_1\lambda_i+c_2\lambda_i^2+...+c_k\lambda_i^k,\quad i=1,2,...,n
$$

也就是说，矩阵多项式 $p(A)$ 的特征值等于将矩阵 $A$ 的每个特征值代入多项式中所得$p(\lambda_i)$

!!! note "证明$A^k x = \lambda^k x$"

    当 $k = 1$ 时：

    $$
    A^1 x = Ax = \lambda x
    $$

    假设 $k = m$ 时 $A^m x = \lambda^m x$ 成立
    
    则当 $k = m + 1$ 时：

    $$
    A^{m+1} x = A^m (Ax) = A^m (\lambda x) = \lambda (A^m x) = \lambda (\lambda^m x) = \lambda^{m+1} x
    $$

    因此由数学归纳法得出

    $$
    A^k x = \lambda^k x, \quad \text{其中 } k = 1, 2, ...$$
    则有：
    
    $$
    p(A) x = (c_0 I + c_1 A + c_2 A^2 + ... + c_k A^k) x = (c_0 + c_1 \lambda_i + c_2 \lambda_i^2 + ... + c_k \lambda_i^k) x
    $$

    则矩阵多项式 $p(A)$ 的特征值为：
    
    $$
    p(\lambda_i) = c_0 + c_1 \lambda_i + c_2 \lambda_i^2 + ... + c_k \lambda_i^k, \quad i = 1, 2, ..., n
    $$

!!! example "求矩阵指数 $e^A$的特征值"

    对于一个方阵$A$,矩阵的指数$e^A$定义为矩阵的幂级数：


    $$
    e^A=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+...=\sum_{k=0}^\infty\frac{A^k}{k!}$$

    如果矩阵$A$的特征值为$\lambda_1,\lambda_2,...,\lambda_n$,那么矩阵$e^A$的特征值为：

    $$
    1+\lambda_i+\frac{\lambda_i^2}{2!}+\frac{\lambda_i^3}{3!}+...=\sum_{k=0}^\infty\frac{\lambda_i^k}{k!}=e^{\lambda_i},\quad i=1,2,...,n
    $$

### Cayley-Hamilton 定理 - 求逆

任何一个$n\times n$的方阵$A$ 都满足以它自身为变量的特征多项式，即$p(A)=0$

具体来说，设矩阵$A$的特征多项式为：

$$
p(\lambda)=\det\left(\lambda I-A\right)=\lambda^n+a_{n-1}\lambda^{n-1}+\cdots+a_1\lambda+a_0
$$

则有：

$$
p(A)=A^n+a_{n-1}A^{n-1}+\cdots+a_1A+a_0I=0
$$

在矩阵求逆上的应用：

当矩阵$A$是可逆的 (即$\det(A)\neq0$) 时，可以利用 Cayley-Hamilton 定理来求$A^{-1}$的表达式。

1. **求特征多项式 $p(\lambda)$：**

   计算 $p(\lambda) = \det(\lambda I - A)$，得到特征多项式的系数 $a_i$。

2. **写出 Cayley-Hamilton 方程：**

   $$
   A^n + a_{n-1}A^{n-1} + \cdots + a_1A + a_0I = 0
   $$

3. **两边同时左乘 $A^{-1}$，整理关于 $A^{-1}$ 的项：**

   $$
   A^{n-1} + a_{n-1}A^{n-2} + \cdots + a_1I + a_0A^{-1} = 0
   $$

4. **移项并解出 $A^{-1}$：**

   $$
   A^{-1} = -\frac{1}{a_0}\left(A^{n-1} + a_{n-1}A^{n-2} + \cdots + a_1I\right)
   $$

## 特征向量
