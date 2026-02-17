# 01 | 基础

## Vectors

### Norm | 范数

[什么是范数（norm）？以及 L1,L2 范数的简单介绍\_l1 norm-CSDN 博客](https://blog.csdn.net/qq_37466121/article/details/87855185)

应用：聚类、流行学习、特征学习的重点就是设计一种合理的范数

=== "$L_0$ 范数"
    指的是非零元素的个数

    $$
    \|x\|_0 \stackrel{\text{def}}{=} \text{非零元素的个数}
    $$

=== "$L_1$ 范数"
    绝对值的和

    $$
    \|x\|_1 \stackrel{\text{def}}{=} \sum_{i=1}^{m} |x_i| = |x_1| + \cdots + |x_m|
    $$

    对应Laplace分布

=== "$L_2$ 范数"
    Euclidean norm，Frobenius norm

    $$
    \|x\|_2 = \sqrt{(x_1)^2 + \cdots + (x_m)^2}
    $$

    对应Gaussian分布

=== "$L_\infty$ 范数"
    无穷范数

    $$
    \|x\|_\infty = \max\{|x_1|, \cdots, |x_m|\}
    $$
    
    用于worst case control等领域

    $$
    e = \begin{pmatrix} e_1 \\ \vdots \\ e_m \end{pmatrix}
    $$

    $$
    L_{\infty} = max\{|e_1|,|e_2|,\dots,|e_m|\}
    $$

    控制目标：控制最坏情况

    $$
    \mathop{min}_e ||e||_{\infty}
    $$

=== "$L_p$ 范数"
    Hölder 范数

    $$
    \|x\|_p = \left(\sum_{i=1}^{m} |x_i|^p\right)^{1/p}, \quad p \geq 1
    $$

=== "随机向量范数"

    $$
    \|x(\xi)\|^2 \stackrel{\text{def}}{=} \mathbb{E}\{x^H(\xi) x(\xi)\}
    $$

### inner Product | 内积

内积把向量降维成为标量

典范内积

$$
\langle x, y \rangle = x^H y = \sum_{i=1}^n x_i^* y_i
$$

加权内积

$$
\langle x, y \rangle = x^H G y
$$

其中，$G$ 为正定 Hermitian 矩阵（二次型大于零）。

函数向量内积

$$
\langle x(t), y(t) \rangle \stackrel{\text{def}}{=} \int_a^b x^*(t) y(t) \, dt
$$

!!! note "DFT 变换"
    $$
    X(f) = \sum_{n=0}^{N-1} x(n) e^{-j \left(\frac{2\pi}{N}\right) n f} = e_N^H x = \langle e_{N-1}, x \rangle
    $$

夹角定义

$$
\cos \theta \stackrel{\text{def}}{=} \frac{\langle x, y \rangle}{\sqrt{\langle x, x \rangle} \sqrt{\langle y, y \rangle}} = \frac{\int_a^b x^H(t) y(t) \, dt}{\|x(t)\| \cdot \|y(t)\|}
$$

其中，

$$
\|x(t)\| \stackrel{\text{def}}{=} \left(\int_a^b x^H(t) x(t) \, dt\right)^{1/2}
$$

随机向量内积

$$
\langle x(\xi), y(\xi) \rangle \stackrel{\text{def}}{=} \mathbb{E}\{x^H(\xi) y(\xi)\}
$$

### outer product | 外积（升维）

如果想计算两个向量的正交性

$$
\mathbb{E}\{x(\xi) y^H(\xi)\} = O_{m \times n}
$$

两个向量之间互不含有任何成分，不存在任何相互作用或干扰。

### rotate

### Vector Projection

## 特殊矩阵

### 对角矩阵

### 幂次矩阵

- 幂等矩阵的特征值为 0 或 1
- 幂等矩阵的行列式为 1
- 幂等矩阵的迹为矩阵的秩
- 幂等矩阵的逆矩阵为幂等矩阵
- 幂等矩阵的秩为矩阵的秩
- 幂等矩阵的特征值为 1

幂零矩阵

- 幂零矩阵的特征值为 0
- 幂零矩阵的行列式为 0
- 幂零矩阵的迹为 0
- 幂零矩阵的逆矩阵不存在

### Hermitian 矩阵

复共轭对称矩阵 $R = R^{H}$

- 满足线性关系
- 相关矩阵、协方差矩阵

$$
\mathbf{R}=\begin{bmatrix}r_{11}&r_{21}^*&r_{31}^*&r_{41}^*\\r_{21}&r_{22}&r_{32}^*&r_{31}^*\\r_{31}&r_{32}&r_{22}&r_{21}^*\\r_{41}&r_{31}&r_{21}&r_{11}\end{bmatrix}
$$

### 置换矩阵 | permutation matrix

每一行以及每一列只有一个元素为 1，其他元素为 0

性质

- **右乘是对列重新排列**
- **左乘是对行进行重新排列**

1. $(P_{m \times n})^T = P_{n \times m}$
2. $P^T P = P P^T = I$，这说明置换矩阵是正交矩阵。
3. $P^T = P^{-1}$

### 广义置换矩阵

$$
\begin{align*}
G = \begin{bmatrix} 0 & 0 & 0 & 0 & \alpha \\ 0 & 0& \beta  & 0 & 0 \\ 0 & \gamma & 0 & 0 & 0 \\ 0 & 0 & 0 & \lambda & 0 \\ \rho & 0 & 0 & 0 & 0 \end{bmatrix} &= \begin{bmatrix} 0 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 & 0 \end{bmatrix}
\begin{bmatrix}
\rho & & & & 0\\
 &\gamma & & & \\
 & &\beta & & \\
& & & \lambda& \\
0& & & & \alpha\\
\end{bmatrix}\\
&= P\cdot\Lambda
\end{align*}
$$

一个正方矩阵称为广义置换矩阵，简称 g 矩阵，若其每行和每列有一个并且仅有一个非零元素

G 可写为一个置换矩阵和一个非奇异对角阵的乘积，$G = P\Lambda$

!!! note "作用：观测数据模型"

    $$
    \mathbf{x}(t)=\mathbf{As}(t)=\sum_{i=1}^{\infty}\mathbf{a}_is_i(t)
    $$


    > 例子：手机的麦克风阵列，来判定说话的有几个人、什么方向、说的什么内容;
    > 阵面接受，阵面接收的信号是多个信号的叠加，这些信号的幅度、相位、频率、方向等参数都不确定，
    > 用$\alpha$建模方向，用$s(t)$建模source发出的信号波形

    则已知阵列接收的信号$x(t)$，需要恢复出$s(t)$，就是一个求广义逆矩阵的问题
    
    $\hat{\mathbf{s}}( t) = \mathbf{A}^\dagger \mathbf{x}( t)$，$\mathbf{A}^\dagger = ( \mathbf{A}^\mathrm{T} \mathbf{A}) ^{- 1}\mathbf{A}^\mathrm{T}$广义逆矩阵

    得到的$\hat{\mathbf{s}}(t)$有两种不确定性：

    1. permutation ambiguity 累加导致信号顺序不确定
    2. scale ambiguity 信号幅度不确定 $x( t) = \sum _{i= 1}^n\frac {\mathbf{a}_i}{\alpha _i}\alpha _is_i( t)$

    这两种不确定性可以通过广义置换矩阵进行描述

    所以，真实信号$s(t)$可以写成：

    $$
    \mathbf{s}(t) = \hat{\mathbf{s}}(t) \mathbf{P} \Lambda
    $$

    如果再进一步，我们把$x(t)$拆分成 1-T 时刻，写成矩阵的形式


    $$
    X_{m \times T}  = A_{m \times n} S_{n\times T}
    $$

    
    下一步的问题是，我们是否可以唯一的分解出$A$和$S$？

    显然是不可以的中间乘一个可逆矩阵，就可以变换成其他的形式

    $$
    \begin{align*}
    X_{m \times T}  &= A_{m \times n} S_{n\times T} \\
    &= (A_{m \times n} I )(I^{-1}S_{n\times T})\\
     &= C D
    \end{align*}
    $$

    所以如果矩阵形式给定，才可以保证唯一性

    张量的 CP 分解：有 Vandermonde 结构，有可识别性

### 酉矩阵 | Unitary matrix

定义在复数域，方阵

$$
U U^{H} = U^{H} U = I
$$

- 向量内积、向量范数、向量夹角在酉变换下不变

  - 内积：$\langle Ux, Uy\rangle = (Ux)^H (Uy) = x^H U^H U y = x^H y = \langle x, y\rangle$
  - 长度：$||Ux||^2 = \langle Ux, Ux\rangle = \langle x, x\rangle = ||x||^2$
  - 夹角：$\cos\theta = \frac{\langle Ux, Uy\rangle}{||Ux|| ||Uy||} = \frac{\langle x, y\rangle}{||x|| ||y||} = \cos\theta$

- 正交矩阵在实数域而酉矩阵在复数域

!!! note "并不是将实数域的 Transpose 扩展到复数域改成 Hermitian"
    | 实向量、实矩阵 | 复向量、复矩阵 |
    |----------------|----------------|
    | $\|x\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$ | $\|x\| = \sqrt{\|x_1\|^2 + \|x_2\|^2 + \cdots + \|x_n\|^2}$ |
    | 转置 $A^T = [a_{ji}]$， $(AB)^T = B^T A^T$ | 共轭转置 $A^H = [a_{ji}]$， $(AB)^H = B^H A^H$ |
    | 内积 $(x, y) = x^T y$ | 内积 $(x, y) = x^H y$ |
    | 正交性 $x^T y = 0$ | 正交性 $x^H y = 0$ |
    | 对称矩阵 $A^T = A$ | Hermitian矩阵 $A^H = A$ |
    | 正交矩阵 $Q^T = Q^{-1}$ | 酉矩阵 $U^H = U^{-1}$ |
    | 特征值分解 $A = Q \Lambda Q^{-1} = Q \Lambda Q^T$ | 特征值分解 $A = U \Sigma U^H = U \Sigma U^{-1}$ |
    | 范数的正交不变性 $\|Qx\| = \|x\|$ | 范数的酉不变性 $\|Ux\| = \|x\|$ |
    | 内积的正交不变性 $(Qx, Qy) = (x, y)$ | 内积的酉不变性 $(Ux, Uy) = (x, y)$ |

### 正交矩阵 ｜ Orthogonal matrix

定义在实数域，方阵

- $Q^T = Q^{-1}$
- $Q^T Q = Q Q^T = I$
- $Q^T = Q^{-1}$

### 三角矩阵

1. **下三角矩阵$L$**：若 $a_{ij} = 0$ $(i < j)$。

2. **严格下三角矩阵**：若 $a_{ij} = 0$ $(i \leqslant j)$。

3. **单位下三角矩阵**：若 $a_{ij} = 0$ $(i < j)$ 且 $a_{ii} = 1$ $(\forall i)$。

4. **上三角矩阵$U$**：若 $a_{ij} = 0$ $(i > j)$。

5. **严格上三角矩阵**：若 $a_{ij} = 0$ $(i \geqslant j)$。

6. **单位上三角矩阵**：若 $a_{ij} = 0$ $(i > j)$ 且 $a_{ii} = 1$ $(\forall i)$。

### 反对称矩阵 | Skew-Symmetric Matrix

一个矩阵 $A$ 被称为反对称矩阵（Skew-Symmetric Matrix），如果它满足以下条件：

$$
A^T = -A
$$

即矩阵的转置等于其负值。

#### 性质

1. **对角线元素为零**：由于 $a_{ii} = -a_{ii}$，所以对角线上的元素必须为零。
2. **奇数阶反对称矩阵的行列式为零**：因为 $det(A) = det(A^T) = det(-A) = (-1)^n det(A)$，当 $n$ 为奇数时，$det(A) = 0$。
3. **特征值**：反对称矩阵的特征值要么为零，要么是纯虚数。
4. **与正交矩阵的关系**：反对称矩阵可以与正交矩阵结合用于描述旋转等操作。
5. **二次型为 0**：$A$ 的二次型为 0 是 $A$是反对称矩阵的充分必要条件。

!!! note "证明"
    **充分性** ：如果 $A$ 的二次型为零，即对于任意向量 $x$，有 $x^T A x = 0$，则可以推导出 $A^T = -A$，从而证明 $A$ 是反对称矩阵。

    $$
    x^T A x = 0 \implies x^T A^T x = 0 \implies x^T (A + A^T) x = 0
    $$

    由于 $A + A^T$ 是对称矩阵，且对于任意向量 $x$，$x^T (A + A^T) x = 0$，所以 $A + A^T = 0$，即 $A^T = -A$。

    **必要性** ：如果 $A$ 是反对称矩阵，即 $A^T = -A$，则对于任意向量 $x$，有 $x^T A x = 0$。这显然成立，因为：

    $$
    x^T A x = x^T (-A^T) x = -x^T A^T x = -(x^T A x)^T = -x^T A x
    $$

    所以 $2x^T A x = 0$，即 $x^T A x = 0$。

#### 应用

- 在物理中，反对称矩阵常用于描述角速度、旋转等。
- 在计算机图形学中，反对称矩阵用于表示三维空间中的叉积操作。
- 在控制理论中，反对称矩阵用于描述系统的稳定性和对称性。

### Vandermonde 矩阵 - 等比数列

Vandermonde 矩阵的每行或每列的元素组成一个等比数列。

是一个强结构性矩阵，只需要一行元素就可以决定整个矩阵

$$
A = \begin{bmatrix} 1 & 1 & \cdots & 1 \\ x_1 & x_2 & \cdots & x_n \\ x_1^2 & x_2^2 & \cdots & x_n^2 \\ \vdots & \vdots & \ddots & \vdots \\ x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1} \end{bmatrix}
$$

或者写成：

$$
A = \begin{bmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ 1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^{n-1} \end{bmatrix}
$$

若第二行元素各不相同，则矩阵非奇异。

```matlab title="Matlab: Vandermonde 矩阵"
A = vander([1, 2, 3])
```

!!! note "应用"
    DFT中就有Vandermonde矩阵

### Fourier 矩阵

DFT:有限长离散序列，时域离散，频域离散

#### DFT 正变换

$X_k = \sum_{n=0}^{N-1} x_n e^{-j \frac{2\pi kn}{N}} = \sum_{n=0}^{N-1} x_n \omega^{nk}$，其中 $k = 0, 1, \ldots, N-1$
$\hat{x} = F x$

$F = \begin{bmatrix} 1 & 1 & \cdots & 1 \\ 1 & \omega & \cdots & \omega^{N-1} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & \omega^{N-1} & \cdots & \omega^{(N-1)(N-1)} \end{bmatrix}$，其中 $\omega = e^{-j \frac{2\pi}{N}}$，称为 Fourier 矩阵

#### DFT 逆变换

$x = F^{-1} \hat{x} = \frac{1}{N} F^* \hat{x}$

$$
\begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_{N-1} \end{bmatrix} = \frac{1}{N} \begin{bmatrix} 1 & 1 & \cdots & 1 \\ 1 & \omega^* & \cdots & (\omega^{N-1})^* \\ \vdots & \vdots & \ddots & \vdots \\ 1 & (\omega^{N-1})^* & \cdots & (\omega^{(N-1)(N-1)})^* \end{bmatrix} \begin{bmatrix} X_0 \\ X_1 \\ \vdots \\ X_{N-1} \end{bmatrix}
$$

$x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k e^{j \frac{2\pi kn}{N}}$，其中 $n = 0, 1, \ldots, N-1$

傅里叶矩阵是一个酉矩阵

- $F^H F = F F^H = N I$
- $F^{-1} = \frac{1}{N} F^H = \frac{1}{N} F^*$

!!! note "证明：傅里叶矩阵是一个酉矩阵"

    写出傅里叶矩阵，和其共轭转置

    $$
    \begin{align*}
    F &= \begin{bmatrix} 1 & 1 & \dots & 1 \\ 1 & \omega & \dots & \omega^{N-1} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & \omega^{N-1} & \dots & \omega^{(N-1)^2} \end{bmatrix}_{N \times N}\quad where \quad \omega = e^{-j \frac{2\pi}{N}}\\
    &=  \begin{bmatrix} f_1 & f_2 & \dots & f_N \end{bmatrix}
    \end{align*}
    $$

    进行向量化，使用一些notation化简表达式

    $$
    \begin{align*}
    F^{H} F &= \begin{bmatrix} f_1^{H} \\ f_2^{H} \\ \vdots \\ f_N^{H} \end{bmatrix} \begin{bmatrix} f_1 & f_2 & \dots & f_N \end{bmatrix}\\
    &= \begin{bmatrix} f_1^{H} f_1 & f_1^{H} f_2 & \dots & f_1^{H} f_N \\ f_2^{H} f_1 & f_2^{H} f_2 & \dots & f_2^{H} f_N \\ \vdots & \vdots & \ddots & \vdots \\ f_N^{H} f_1 & f_N^{H} f_2 & \dots & f_N^{H} f_N \end{bmatrix}_{N \times N}
    \end{align*}
    $$


    此时我们只需要研究$f_n^H \cdot f_m$,即可得出$F^{H} F = NI$

    $$
    \begin{aligned}
    f_n^H \cdot f_m &= \begin{bmatrix}1\\w^{n-1}\\\vdots\\w^{(n-1)(N-1)}\end{bmatrix}^{H}\begin{bmatrix}1\\w^{m-1}\\\vdots\\w^{(m-1)(N-1)}\end{bmatrix}\\
    &= \begin{bmatrix}1&w^{-(n-1)}&\cdots&w^{-(n-1)(N-1)}\end{bmatrix}\begin{bmatrix}1\\w^{m-1}\\\vdots\\w^{(m-1)(N-1)}\end{bmatrix}\\ 
    &= \sum_{k=0}^{N-1}w^{-(n-1)k}w^{(m-1)k}\\
    &= \sum_{k=0}^{N-1}w^{(m-n)k} = \begin{cases} N, & m = n \\ 0, & m \neq n \end{cases}
    \end{aligned}
    $$



    - $n = m$时，$f_n^H \cdot f_m = N$, 相当于对 1 求和
    - $n \neq m$时，$f_n^H \cdot f_m = 0$
      
    $$
    \begin{aligned}
    f_n^H \cdot f_m &= \sum_{k=0}^{N-1}w^{(m-n)k} \\
    &= \sum_{k=0}^{N-1} \omega_0^{k}\quad (\omega_0 = e^{j \frac{2\pi}{N}})\\
    &= \frac{1-\omega_0^{N}}{1-\omega_0} = 0(\because \omega_0^N = 1)
    \end{aligned}
    $$

### Hadamard 矩阵 - 1-1 矩阵

$H_n \in \mathbb{R}^{n \times n}$ 所有元素取 +1 或者 -1，且满足 $H_n H_n^T = H_n^T H_n = nI_n$。

> 可以由小的 2x2 的矩阵扩充得到大的矩阵

作用：在模拟域，Hadamard 矩阵可以用于构造正交的基函数，用于信号处理、图像处理、通信等领域。

性质

- 只有当 $n = 2^k$ 或者 $n$ 是 4 的整数倍时，Hadamard 矩阵才存在。
- 容易验证 $\frac{1}{\sqrt{n}} H_n$ 为标准正交矩阵。
- $n \times n$ Hadamard 矩阵 $H_n$ 的行列式 $\det(H_n) = n^{n/2}$。

规范化的标准正交 Hadamard 矩阵具有通用构造公式：

$$
\tilde{H}_n = \frac{1}{\sqrt{2}} \begin{bmatrix} \tilde{H}_{n/2} & \tilde{H}_{n/2} \\ \tilde{H}_{n/2} & -\tilde{H}_{n/2} \end{bmatrix}
$$

其中：

$$
\tilde{H}_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

### Toeplitz 矩阵 - 主对角线元素相同

也是一个强结构性的矩阵，只需要一列&一行就可以唯一确定整个矩阵

任何一条对角线的元素取相同值：

$$
A = \begin{bmatrix} a_0 & a_{-1} & a_{-2} & \cdots & a_{-n} \\ a_1 & a_0 & a_{-1} & \cdots & a_{-n+1} \\ a_2 & a_1 & a_0 & \cdots & a_{-n+2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & a_{n-1} & a_{n-2} & \cdots & a_0 \end{bmatrix} = [a_{i-j}]_{i,j=0}^n
$$

对称 Toeplitz 矩阵 $A = [a_{i-j}]_{i,j=0}^n$

若一个复 Toeplitz 矩阵的元素满足复共轭对称关系 $ a_{-i} = a_i^* $，则称为 Hermitian Toeplitz 矩阵：

$$
A = \begin{bmatrix} a_0 & a_1^* & a_2^* & \cdots & a_n^* \\ a_1 & a_0 & a_1^* & \cdots & a_{n-1}^* \\ a_2 & a_1 & a_0 & \cdots & a_{n-2}^* \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & a_{n-1} & a_{n-2} & \cdots & a_0 \end{bmatrix}
$$

!!! note "卷积操作是 Toplitz 矩阵"
    卷积操作 $y = x \ast h$ 可以表示为：

    $$
    y[n] = \sum_{k=0}^{K-1} h[k] \cdot x[n-k] 
    $$

    把sum的表达式写成矩阵的形式，就是Toplitz矩阵


    $y = H \cdot x$
    
    $$ 
    H = \begin{bmatrix} h_0 & 0 & 0 & \cdots & 0 \\ h_1 & h_0 & 0 & \cdots & 0 \\ h_2 & h_1 & h_0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & h_2 & h_1& h_0 \end{bmatrix} 
    $$

    **多项式乘法也可以看作是一个卷积的过程，表示成竖式的形式，其实就是卷积**

### Hankel 矩阵 - 斜对角线元素相同

正方矩阵 $A \in \mathbb{C}^{(n+1) \times (n+1)}$ 称为 Hankel 矩阵，若：

$$
A = \begin{bmatrix} a_0 & a_1 & a_2 & \cdots & a_n \\ a_1 & a_2 & a_3 & \cdots & a_{n+1} \\ a_2 & a_3 & a_4 & \cdots & a_{n+2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & a_{n+1} & a_{n+2} & \cdots & a_{2n} \end{bmatrix}
$$
