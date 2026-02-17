# 05 | 矩阵方程

## 问题阐释

对于方程组

$$
\begin{cases}
a_{11}x_{1}+a_{12}x_{2}+\cdots+a_{1n}x_{n}=b_{1}\\
a_{21}x_{1}+a_{22}x_{2}+\cdots+a_{2n}x_{n}=b_{2}\\
\vdots \\
a_{m1}x_{1}+a_{m2}x_{2}+\cdots+a_{mn}x_{n}=b_{m}
\end{cases}
$$

$$
Ax=b
$$

其中

$$
\begin{aligned}
&A=\begin{bmatrix}a_{11}&\cdots&a_{1n}\\\vdots&\ddots&\vdots\\a_{m1}&\cdots&a_{mn}\end{bmatrix}\quad x=\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}\quad b=\begin{bmatrix}b_1\\\vdots\\b_m\end{bmatrix}
\end{aligned}
$$

我们的目的：

- 判断方程有没有解
- 有解的方程去求解
- 无解的方程近似解

!!! example "例子"
    $$
    Ax = b
    $$

    denote 
    
    - $A_{m\times n}$ 数据矩阵，例如每个学生的表现（他们的分数、作业、幻灯片、考试）
    - $x_{n\times 1}$ 是权重向量（未知），例如作业、幻灯片、考试的重要程度
    - $b_{m\times 1}$ 是观测向量（已知），例如学生的最终成绩


    如果把输入输出层看作神经元，那么矩阵方程可以看作是神经网络的线性层


    ![](https://img.philfan.cn/Math__LinearAlgebra__assets__05-matrix_equation.assets__20250511210010.webp)

## 有无解

关注 $m,n,rank(A)$ 之间的关系

> 秩的含义是：线性无关的行（列）向量的最大个数

从矩阵的 column view 理解

- $\text{rank}([A, b])> \text{rank}(A)$ : $b$无法被 A 的列向量线性表示，无解
- $\text{rank}([A, b]) = \text{rank}(A)$ : $b$可以被 A 的列向量线性表示，有解
  - $\text{rank}(A) = n$ : 唯一解
  - $\text{rank}(A) < n$ : 无穷多解

> 奇异的意思是：冗余、重复、线性相关
>
> 非奇异的意思是：线性无关

机械臂的例子理解

- 关节空间：关节的角度（旋转关节）或位移（移动关节）
- 笛卡尔空间：末端执行器的位置和姿态

对于机械臂来说，操作空间维度相当于$m$，关节数目相当于$n$（自变量数目）

- 超定：$m>n$，约束比变量多，可能无解
- 欠定：$m<n$，关节很多，维度比较低，有很多组解

## 方程求解

!!! note "在机器学习当中，已知了样本数据的$A$，以及最终评价$b$，那求解$x$的过程就是模型训练的过程"

### 初等行变换和高斯消元法

$$
A x = b \xrightarrow{\text{初等行变换}} x = A^{-1} b
$$

$$
[A, b] \xrightarrow{\text{初等行变换}} [I, A^{-1} b]
$$

> 参考资料 [线性方程组的最小二乘解和最小范数解 - 一以知行](https://zhuanlan.zhihu.com/p/503664717)

### 矩阵求逆

若 $A$ 和 $B$ 均可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$

性质（对于可逆的正方矩阵 A 和 B）：

- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^{*})^{-1} = (A^{-1})^{*}$
- $(A^{\mathrm{T}})^{-1} = (A^{-1})^{\mathrm{T}}$
- $(A^{\mathrm{H}})^{-1} = (A^{-1})^{\mathrm{H}}$

#### 矩阵求逆引理

background：在许多实际问题中，经常会遇到这样的问题：已知一个矩阵$A$的逆矩阵$A^{-1}$ ,当矩阵$A$产生了一个非常小的变化得到$A+\Delta$时，通过已知的$A^{-1}$，如何简单的求出$(A+\Delta)^{-1}$?

$$
(A + xy^H)^{-1} = A^{-1} - \frac{A^{-1}xy^HA^{-1}}{1 + y^HA^{-1}x}
$$

作用：已经完成了矩阵的求逆，在 A 的基础上加上一个秩为 1 矩阵，求解逆矩阵的变化

应用：

- 自相关矩阵和协方差矩阵估计的更新
- 最小二乘法

!!! warning "证明 todox"
    $$
    \begin{aligned}
    A^{-1} + X              & = (A + BCD)^{-1} \\
    (A + BCD)(A^{-1} + X)   & = I(I\text{为单位阵}) \\
    I + AX + BCDA^{-1} + BCDX & = I \\
    AX + BCDA^{-1} + BCDX   & = 0\text{(0为 0矩阵)} \\
    (A + BCD)X + BCDA^{-1}  & = 0 \\
    X                      & = -(A + BCD)^{-1}BCDA^{-1} \\
    X                      & = -[B(B^{-1}A + CD)]^{-1}BCDA^{-1} \\
    X                      & = -(B^{-1}A + CD)^{-1}CDA^{-1} \\
    X                      & = -[C(C^{-1}B^{-1}A + D)]^{-1}CDA^{-1} \\
    X                      & = -(C^{-1}B^{-1}A + D)^{-1}DA^{-1} \\
    X                      & = -[(C^{-1}B^{-1} + DA^{-1})A]^{-1}DA^{-1} \\
    X                      & = -A^{-1}(C^{-1}B^{-1} + DA^{-1})^{-1}DA^{-1} \\
    X                      & = -A^{-1}[(C^{-1} + DA^{-1}B)B^{-1}]^{-1}DA^{-1} \\
    X                      & = -A^{-1}B(C^{-1} + DA^{-1}B)^{-1}DA^{-1}
    \end{aligned}
    $$

!!! note "应用：自相关矩阵求逆$\hat{R}^{-1}(n)$"

    $\lambda$用来表征遗忘因子;$\lambda$越小，越倾向于相信现在的数据
    
    $$
    (\lambda R + xx^H)^{-1} = \lambda^{-1}R^{-1} - \frac{(\lambda^{-1}R^{-1}x)(\lambda^{-1}R^{-1}x)^H}{1 + \lambda^{-1}x^HR^{-1}x}
    $$

    如果每次全量计算，时间复杂度很高，computational demanding

    改写成递推形式

    $$
    \begin{align*}
    \hat{R}(n) &= \sum_{j=0}^{n} \lambda^{n-j} x(j)x^H(j)\\
    \hat{R}(n) &= \lambda \hat{R}(n-1) + x(n)x^H(n)\\
    \hat{R}^{-1}(n) &= \lambda^{-1}\hat{R}^{-1}(n-1) - g(n)g^H(n)
    \end{align*}
    $$
    
    更新公式
    
    $$
    \begin{align*}
    \bar{g}(n) &= \lambda^{-1}\hat{R}^{-1}(n-1)x(n)\\
    \bar{\alpha}(n) &= 1 + g^H(n)x(n)\\
    g(n) &= \bar{g}(n)/\bar{\alpha}(n)
    \end{align*}
    $$

#### 左右逆矩阵

对于方程 $\mathbf{Ax} = \mathbf{b}$,其中$\mathbf{A}_{m\times n}$， $m$代表方程的个数，$n$代表未知数的个数

!!! note "构造方法：想要构造成已经学过的方阵的求逆问题"
    我们已经知道如何求解方阵的逆矩阵，所以如果想求解非方阵的逆矩阵，需要构造一个方阵

    所以，通过构造方阵的办法，我们很容易就可以求解非方阵的逆矩阵

=== "左逆"

    仅当 $m \geq n$ 时("Tall matrix")，说明这个时候方程的数目大于未知数的个数，方程是过定(overdetermined)的。矩阵 $A$ 可能有**左逆矩阵** 
    
    $$
    A^\dagger_L = \left(A^HA\right)^{-1}A^H
    $$
    
    左逆列满秩的时候一定存在，即$rank(A) = n$

    证明：当$rank(A) = n$时，$A^H A$ is invertible
    
    **超定方程最小二乘解**

=== "右逆"

    仅当 $m \leq n$ 时("fat matrix")，方程数目小于未知数的个数，方程式欠定的。矩阵 $A$ 可能有**右逆矩阵** 
    
    $$
    A^\dagger_R = A^H\left(AA^H\right)^{-1}
    $$
    
    右逆行满秩的时候一定存在
    
    欠定方程最小范数解

#### Moore-Penrose Inverse | 伪逆矩阵

令 $A$ 是任意 $m \times n$ 矩阵，称矩阵 $A^\dagger$ 是 $A$ 的广义逆矩阵，若 $A^\dagger$ 满足以下四个条件（常称 Moore-Penrose 条件）：

1. $AA^\dagger A = A;$
2. $A^\dagger AA^\dagger = A^\dagger;$
3. $AA^\dagger$ 为 Hermitian 矩阵，即 $AA^\dagger = (AA^\dagger)^\mathrm{H};$
4. $A^\dagger A$ 为 Hermitian 矩阵，即 $A^\dagger A = (A^\dagger A)^\mathrm{H}.$

### cramer 法则

### 复矩阵方程求解

$$
(A_r + jA_i)(x_r + jx_i) = b_r + jb_i
$$

$$
\begin{bmatrix} A_r & -A_i \\ A_i & A_r \end{bmatrix} \begin{bmatrix} x_r \\ x_i \end{bmatrix} = \begin{bmatrix} b_r \\ b_i \end{bmatrix}
$$

$$
\begin{bmatrix} A_r & -A_i & b_r \\ A_i & A_r & b_i \end{bmatrix} \xrightarrow{\text{初等行变换}} \begin{bmatrix} I_n & O_n & x_r \\ O_n & I_n & x_i \end{bmatrix}
$$

其中，$A_r$ 和 $A_i$ 是矩阵 $A$ 的实部和虚部，$b_r$ 和 $b_i$ 是向量 $b$ 的实部和虚部，$I_n$ 和 $O_n$ 分别是 $n \times n$ 的单位矩阵和零矩阵，$x_r$ 和 $x_i$ 是向量 $x$ 的实部和虚部。

相当于把复数乘法做了简单的拆分，转换成了矩阵的形式

## 最小二乘解（Least Squares Solution）

### OLS - 优化视角

超定方程组，无解

$$
Ax \approx b
$$

引入一个残差向量$\Delta b$

$$
Ax  = b + \Delta b
$$

目标是最小化**残差向量** $\Delta b = Ax - b$的**欧几里得范数**，即

$$
\begin{align*}
\min_{\mathbf{x}} \| A \mathbf{x} - \mathbf{b} \|_2^2 &= (Ax - b)^T(Ax - b)\\
&= x^TA^TAx - x^TA^Tb - b^TAx + b^Tb
\end{align*}
$$

> 这里求解二范数的原因详见统计视角

通过求导并令导数为零，可以得到

$$
\nabla f(x) = 2 \cdot A^T (Ax - b) = 0\\
\nabla^2 f(x) = 2 \cdot A^TA
$$

Hessian 矩阵是正定的，所以$f(x)$是凸函数，因此平稳点（导数为 0 的点）就是全局最小值点

- $A^T A$可逆：$A_{m\times n}$中$m \geq n$，且$rank(A) = n$,直接求逆

    $$
    \mathbf{x}_{\text{LS}} = (A^T A)^{-1} A^T \mathbf{b}
    $$

- $rank(A) < n$,$m\geq n$，求伪逆矩阵 Moore-Penrose Inverse

    $$
    \mathbf{x}_{\text{LS}} = (A^T A)^{\dagger} A^T \mathbf{b}
    $$

- $rank(A) = m<n$,  不可辨识

### DLS

### TLS - 总体最小二乘

详见[LR](../ML/02-LinearRegression.md)一章的笔记

### 应用 - 稀疏表示和压缩感知

## 最小范数解

最小范数解是离原点最近的解

$$
\begin{align*}
&\text{Minimize:} \quad \| x \| \\
&\text{Subject to:} \quad A x = b
\end{align*}
$$

直接给出结论，此时问题的最小范数解是：

$$
x^* = A^T (A A^T)^{-1} b
$$

!!! note "证明"
    令上述问题的解为 $x^* = A^T (A A^T)^{-1} b$，注意

    $$
    \begin{align*}
    \| x \|^2 &= \| (x - x^*) + x^* \|^2\\
    &= ((x - x^*) + x^*)^T ((x - x^*) + x^*)\\
    &= \| x - x^* \|^2 + \| x^* \|^2 + 2 x^{*T} (x - x^*)
    \end{align*}
    $$

    由于

    $$
    \begin{align*}
    x^{*T} (x - x^*) &= [A^T (A A^T)^{-1} b]^T [x - A^T (A A^T)^{-1} b]\\
    &= b^T (A A^T)^{-1} [A x - (A A^T) (A A^T)^{-1} b]\\
    &= b^T (A A^T)^{-1} (b - b)\\
    &= 0
    \end{align*}
    $$

    故有

    $$
    \| x \|^2 = \| x - x^* \|^2 + \| x^* \|^2
    $$

    由于对于所有 $x \neq x^*$，都有 $\| x - x^* \|^2 > 0$ 成立，因此，对于所有 $x \neq x^*$，都有 $\| x \|^2 > \| x^* \|^2$，即 $\| x \| > \| x^* \|$，显然 $x^*$ 是惟一的。证明完毕。

## 矩阵方程

### Lyapunov 方程

[线性代数 | 李雅普诺夫方程](https://www.zhihu.com/tardis/zm/art/105326895?source_id=1005)

## 方程解的稳定性

条件数的问题

对于方程

$$
Ax = b
$$

假设$A$稳定不变，想要探究$b$的扰动如何影响$x$

$$
A(x + \Delta x) = b + \Delta b
$$

即$\Delta b$ 如何影响 $\Delta x$。如何度量扰动的大小对于解的影响？探究$\frac{\|\Delta x\|}{\|x\|}$与$\frac{\|\Delta b\|}{\|b\|}$的关系

① $A$ 是方阵 $n \times n$

!!! note "Lemma: $||AB||_2 \leq ||A||_2 ||B||_2$"

$$
A\delta x = \delta b\\
\implies \quad ||\delta x||_2 \leq ||A^{-1}||_2 ||\delta b||_2 \tag{①}
$$

$$
Ax = b\\
\implies \quad ||b||_2 \leq ||A||_2 ||x||_2\\
\implies \quad ||x||_2 \geq \frac{1}{||A||_2} \cdot ||b||_2\\
\implies \quad \frac{1}{||x||_2} \leq \frac{||A||_2}{||b||_2} \tag{②}
$$

$$
\begin{aligned}
1: \quad ||\delta x||_2 &\leq ||A^{-1}||_2 ||\delta b||_2\\
2: \quad \frac{1}{||x||_2} &\leq \frac{||A||_2}{||b||_2}\\
\implies \quad \frac{\|\delta x\|}{\|x\|} &\leq (||A||_2 ||A^{-1}||_2)\frac{\|\delta b\|}{\|b\|}
\end{aligned}
$$

所以把$A$的范数和$A^{-1}$的范数相乘，得到一个常数，这个常数就是$A$的 condition number

$$
cond(A) = ||A||_2 ||A^{-1}||_2 =\sigma_{max} \cdot \frac{1}{\sigma_{min}}= \frac{\sigma_{max}}{\sigma_{min}} \geq 1
$$

- if $cond(A) \rightarrow \infty$ then A is ill-conditioned
- if $cond(A) \rightarrow 1$ then A is well-conditioned

改善病态矩阵的方法：

- 增加数据量
- 增加正则化
- 使用更稳定的算法

$$
A + \lambda I \rightarrow \begin{bmatrix}\sigma_1+\lambda & 0 & \cdots & 0 \\ 0 & \sigma_2+\lambda & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \sigma_n+\lambda \end{bmatrix}
$$

$$
cond(A + \lambda I) = \frac{\sigma_{max}+\lambda}{\sigma_{min}+\lambda}
$$

A 如果不是方阵

$$
\begin{aligned}
Ax &= b\\
\underbrace{A^H A}_{视作 A} x &= \underbrace{A^H b}_{视作 b}\\
x &= (A^H A)^{-1} A^H b
\end{aligned}
$$

则按照刚才的算法，可以得到

$$
\begin{aligned}
\text{cond}(A^H A) &=||A^H A||_2 ||(A^H A)^{-1}||_2 \\
&= (\frac{\sigma_{max}}{\sigma_{min}})^2 \quad {\color{gray} A = U\Sigma V^H, A^H A = V\Sigma^2 V^H}\\
&= \left[\text{cond}(A)\right]^2
\end{aligned}
$$

!!! example "例子"
    $$
    \begin{aligned}
    &A\begin{bmatrix}1&1\\\epsilon&0\\0&\epsilon\end{bmatrix}\quad 0<\epsilon<1\quad b=\begin{bmatrix}2\\\epsilon\\\epsilon\end{bmatrix}\\
    &Ax=b\Rightarrow x=\begin{bmatrix}1\\1\end{bmatrix}\\
    &A^HA=\begin{bmatrix}1+\epsilon^{2}&1\\1&1+\epsilon^{2}\end{bmatrix}\\
    &\text{cond}(A)\rightarrow\infty.\quad(MATLAB无法求解)
    \end{aligned}
    $$

## 优化与统计的联系
