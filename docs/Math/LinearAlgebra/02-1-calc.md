# 02 | 矩阵运算

## 单个矩阵

!!! note "要关注矩阵运算对于矩阵维度的影响"

| 性质/指标 | 描述 |
| --- | --- |
| 二次型 | 矩阵的正定性与负定性 |
| 行列式 | 矩阵的奇异性 |
| 特征值 | 矩阵的奇异性、正定性和对角元素的结构 |
| 迹 | 矩阵对角元素之和、特征值之和 |
| 秩 | 行（或列）之间的线性无关性、矩阵方程的适定性 |

### Conjugate

- 共轭性质：$(A+B)^{*} = A^{*} + B^{*}$

### Transpose

- 转置性质：$(A+B)^{\mathrm{T}} = A^{\mathrm{T}} + B^{\mathrm{T}}$，$(AB)^{\mathrm{T}} = B^{\mathrm{T}}A^{\mathrm{T}}$

#### Hermitian 转置（共轭转置/ Hermitian 伴随/ Hermitian 共轭）

$A^\text{H} = \begin{bmatrix} a_{11}^* & a_{21}^* & \cdots & a_{m1}^* \\ a_{12}^* & a_{22}^* & \cdots & a_{m2}^* \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n}^* & a_{2n}^* & \cdots & a_{mn}^* \end{bmatrix}$

$A^\text{H} = (A^*)^\text{T} = (A^\text{T})^*$

- Hermitian 转置性质：$(A+B)^{\mathrm{H}} = A^{\mathrm{H}} + B^{\mathrm{H}}$，$(AB)^{\mathrm{H}} = B^{\mathrm{H}}A^{\mathrm{H}}$

- Hermitian 矩阵性质：对于任意矩阵$A$，矩阵$B = A^{\mathrm{H}}A$都是 Hermitian 矩阵。

### Inverse

详见矩阵方程一节

### norm

#### 诱导范数（Induced Norm）

- 诱导范数定义为：$\|A\| = \max \{\|Ax\| : x \in K^n, \|x\| = 1 \}$
- 或者等价地定义为：$\|A\| = \max \left\{ \frac{\|Ax\|}{\|x\|} : x \in K^n, x \neq 0 \right\}$

**常用的诱导范数 - p 范数（p-Norm）**：

- p 范数定义为：$\|A\|_p = \max_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}$

=== "当 $p = 1$"
    得到绝对列和范数
    列的绝对值和的最大值

    $$ 
    \|A\|_1 = \max_{1 \leq j \leq n} \sum_{i=1}^m |a_{ij}| 
    $$

=== "$p = 2$"
    得到矩阵的最大奇异值（Spectral Norm）

    $$
    \|A\|_2 = \|A\|_{\text{spec}} 
    $$

=== "$p = \infty$"
    得到绝对行和范数（Absolute Row Sum Norm）

    $$ 
    \|A\|_{\infty} = \max_{1 \leq i \leq m} \sum_{j=1}^n |a_{ij}| 
    $$

#### “元素形式”范数

$$
\|A\|_p \stackrel{\text{def}}{=}\left(\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|^p\right)^{1/p}
$$

1. $L_1$ 范数 (和范数) $(p=1)$，绝对值的和

    $$
    \|A\|_1 \stackrel{\text{def}}{=} \sum_{i=1}^m \sum_{j=1}^n |a_{ij}|
    $$

2. Frobenius 范数 $(p=2)$，平方和的平方根

    $$
    \|A\|_F \stackrel{\text{def}}{=} \left( \sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2 \right)^{1/2}
    $$

3. 最大范数 (max norm) 即 $p=\infty$ 的 $p$ 范数，定义为

    $$
    \|A\|_{\infty} = \max_{i=1,\cdots,m; j=1,\cdots,n} \{|a_{ij}|\}
    $$

### quadratic form | 二次型

对于任意一个二次型函数 $f(x_1, \ldots, x_n) = \sum_{i=1}^n \sum_{j=1}^n \alpha_{ij} x_i x_j$，存在许多矩阵 $A$，它们的二次型 $x^T A x = f(x_1, \ldots, x_n)$ 相同。

> 二次型一般用两个 sum 来表示

唯一性条件

- 只有实对称矩阵或复共轭对称矩阵满足唯一性，即 $x^T A x = f(x_1, \ldots, x_n)$。
- 二次型函数一定是实值函数。

**二次型理论**：二次型刻画矩阵的正定性

- $\mathbf{H(f)}$负定，有极大值：奇数阶主子式为负数，偶数阶为正数
- $\mathbf{H(f)}$正定，有极小值：顺序主子式都为正数
- $\mathbf{H(f)}$不定，鞍点：特征值有正有负
- $\mathbf{H(f)}$不可逆，无法判断：特征值有 0

<img src="https://img.philfan.cn/Math__LinearAlgebra__assets__02-1-calc.assets__b05544056c037bc56f9070e45533f02.webp" alt="b05544056c037bc56f9070e45533f02" style="zoom: 33%;" />

!!! note "正定的理解"
    假设 $\mathbf{A}x = m$, 则 $\langle x,m \rangle = x^{\mathbf{H}} m = x^{\mathbf{H}} \mathbf{A} x$

    所以正定意味着x,m夹角小于90度
    
    任意输入，输出偏离都不会太大，都是一个锐角
    
    正定的话，所有特征值都大于零
    
    $$
    \begin{align*}
    &x_i^T A x_i > 0 \\
    &\Rightarrow x_i^T \lambda_i x_i > 0 \\
    &\Rightarrow \lambda_i \|x_i\|^2 > 0 \\
    &\Rightarrow \lambda_i > 0
    \end{align*}
    $$

### 特征值和特征向量

### Trace | 迹

所有特征值之和

$$
tr(A) = \sum_{i=1}^n \lambda_i
$$

### Determinant | 行列式

$$
det(AB) = det(A) \cdot det(B)
$$

#### 求值

??? note "$det = \Pi_i^n \lambda_i$"
    矩阵的行列式等于其特征值的乘积<br>

    对于一个 $n \times n$ 的方阵 $A$，如果它有 $n$ 个线性无关的特征向量 $v_1, v_2, \ldots, v_n$，那么 $A$ 可以表示为：
    
    $$ 
    A = V \Lambda V^{\mathbf{H}}
    $$
    
    $$
    det(A) = det(V) \cdot det(\Lambda) \cdot det(V^{\mathbf{H}}) = det(\Lambda) 
    $$
    
    而特征向量矩阵 $V$ 是正交矩阵$V\cdot V^{\mathbf{H}} = I$；所以 $det(V) = 1$
    
    又因为 $det(\Lambda) = \lambda_1 \lambda_2 \cdots \lambda_n$，所以 $A$ 的行列式等于它的特征值的乘积。

行列式与奇异性

- $\exists \lambda_i = 0$，行列式为 0，矩阵奇异
- $\forall \lambda_i \neq 0$，行列式不为 0，矩阵非奇异

#### 常用方法

### rank

独立的方程的个数;
矩阵中线性无关的行或者列的数目

- $rank(A) = rank(A^T)$
- $rank(A) = rank(A^H)$
- $rank(A) = rank(AA^H)$

### Tensors（todo）

### Matrix Norms

三维到二维的变换 $T : \mathbb{R}^3 \mapsto \mathbb{R}^2$

$$
T_1(x) = \begin{bmatrix} x_1 + x_2 \\ x_1 - x_2 \end{bmatrix}, \quad \text{其中}, \quad x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
$$

$$
T_2(x) = \begin{bmatrix} x_1 - x_2 \\ x_2 + x_3 \end{bmatrix}, \quad \text{其中}, \quad x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
$$

正交投影算子 $w = T(x)$

$$
\begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
$$

## 矩阵之间

!!! attention "关注矩阵运算是如何改变矩阵的维度的"

### 矩阵乘法

矩阵乘法的行视角：每一行都代表不同样本的特征；
左乘行向量相当于对行进行操作

矩阵乘法的列视角：每一列都作为最后结果中的一个成分（采集语音）
右乘列向量相当于对列进行操作

!!! note "鸡尾酒会问题 Blind Signal Seperation"

$$
\begin{aligned}&\mathbf{A}(\mathbf{BC})=(\mathbf{AB})\mathbf{C}\\&(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{AC}+\mathbf{BC}\\&A(B+C)=AB+AC\\&\alpha(\mathbf{A}+\mathbf{B})=\alpha\mathbf{A}+\alpha\mathbf{B}\end{aligned}
$$

### 直和 - 对角块拼接

矩阵的维度是变大的

$m \times m$ 矩阵 $A$ 与 $n \times n$ 矩阵 $B$ 的直和（direct sum）记作 $A \oplus B$，它是一个 $(m + n) \times (m + n)$ 矩阵，定义为：

$$
A \oplus B =
\begin{bmatrix}
A & O_{m \times n} \\
O_{n \times m} & B
\end{bmatrix}
$$

其中，$O_{m \times n}$ 和 $O_{n \times m}$ 分别表示 $m \times n$ 和 $n \times m$ 的零矩阵。

block diagonal matrix

- 不满足交换律
- 满足结合律

### Hadamard product - 逐元素相乘

$$
(A_{m\times n} B_{m\times n})_{ij} = a_{ij} b_{ij}
$$

### Kronecker product - 元素乘矩阵

- 应用：雷达、信号处理

每个元素都乘一个矩阵

=== "右 Kronecker 积"

    $m \times n$ 矩阵 $A = [a_{11}, \cdots, a_{mn}]$ 和 $p \times q$ 矩阵 $B$ 的右 Kronecker 积记作 $A \otimes B$，是一个 $mp \times nq$ 矩阵，定义为
    
    $$
    A \otimes B = [a_{ij}B]_{m \times n}^{p \times q} = \begin{bmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{bmatrix}
    $$

=== "左 Kronecker 积"

    $m \times n$ 矩阵 $A$ 和 $p \times q$ 矩阵 $B = [b_{11}, \cdots, b_{pq}]$ 的左 Kronecker 积 $A \otimes B$ 是一个 $mp \times nq$ 矩阵，定义为
    
    $$
    [A \otimes B]_{\text{left}} = [Ab_{ij}]_{m \times n}^{p \times q} = [b_{ij}A]_{p \times q}^{m \times n} = \begin{bmatrix} Ab_{11} & Ab_{12} & \cdots & Ab_{1q} \\ Ab_{21} & Ab_{22} & \cdots & Ab_{2q} \\ \vdots & \vdots & \ddots & \vdots \\ Ab_{p1} & Ab_{p2} & \cdots & Ab_{pq} \end{bmatrix}
    $$

显然，无论左或右 Kronecker 积都是一一映射：$\mathbb{R}^{m \times n} \times \mathbb{R}^{p \times q} \rightarrow \mathbb{R}^{mp \times nq}$

??? note "Kronecker 积的例子"

    $$
    A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix},B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
    $$
    
    $$
    A \otimes B = \begin{bmatrix} 1 \cdot B & 2 \cdot B \\ 3 \cdot B & 4 \cdot B \end{bmatrix}
    $$


    $$
    A \otimes B = \begin{bmatrix} \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} & \begin{bmatrix} 10 & 12 \\ 14 & 16 \end{bmatrix} \\ \begin{bmatrix} 15 & 18 \\ 21 & 24 \end{bmatrix} & \begin{bmatrix} 20 & 24 \\ 28 & 32 \end{bmatrix} \end{bmatrix}
    $$

### 向量化和矩阵化

motivation: 如何把一张图或者一个视频变成一个向量，送到神经网络中

按列堆栈：

$$
A = \begin{bmatrix}
| & | & & | \\
a_1 & a_2 & \cdots & a_n \\
| & | & & |
\end{bmatrix}\quad  \text{vec}(A) = \begin{bmatrix} a_1 \\ \vdots \\ a_n \end{bmatrix}
$$

按行堆栈：

$$
A = \begin{bmatrix}
—— & a_1 & —— \\
—— & a_2 & —— \\
—— & \cdots& —— \\
—— & a_n & —— \\
\end{bmatrix}\quad \text{rvec}(A) = \begin{bmatrix} -a_{1}-,- a_{2}-, \ldots, -a_{n}- \end{bmatrix}
$$

!!! example "向量化和矩阵化"

    Consider a matrix $A$:

    $$
    A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
    $$

    The vectorization of $A$ by stacking its columns is:

    $$
    \text{vec}(A) = \begin{bmatrix} 1 \\ 3 \\ 2 \\ 4 \end{bmatrix}
    $$


    The vectorization of $A$ by stacking its rows is:

    $$
    \text{rvec}(A) = \begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix}
    $$

In numpy, this can be achieved using:

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A.flatten(order='F')) # 按列堆栈 1,3,2,4
print(A.flatten(order='C')) # 按行堆栈 1,2,3,4
```

```python title="按列堆栈和按行堆栈演示"
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A)

print(A.reshape(-1, order='F'))# 按列堆栈 1,3,2,4
print(A.reshape(1, -1))# 按行堆栈 1,2,3,4
```
