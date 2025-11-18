# 04 | 矩阵分解

## LDU decomposition

- L: lower triangular matrix
- D: diagonal matrix
- U: upper triangular matrix

```matlab
A = [1 2 3; 4 5 6; 7 8 9];
[L, D, U] = ldu(A);
```

## 变换矩阵

### 正交变换

标准正交变换：最后变换后的向量的协方差矩阵是对角矩阵

高度相关的向量进行解相关操作

$$
\mathbb{E}(\omega \omega^H) = \Sigma\\
\mathbb{E}(\Phi (x-b)(x-b)^H \Phi^H) = \Sigma\\
\Phi \mathbb{E}((x-b)(x-b)^H) \Phi^H = \Sigma\\
$$

令

$$
b = m_x
$$

$$
\Phi \mathbb{E}((x-m_x)(x-m_x)^H) \Phi^H = \Sigma\\
\Phi {\color{red}{C_x}} \Phi^H = \Sigma\\
\Phi {\color{red}{U \Sigma U^H}} \Phi^H = \Sigma\\
\implies \Phi U  = I\\
\implies\Phi = U^H\\
$$

所以标准正交变换

$$
U^H(x-m_x) = \omega
$$

### 迷向圆变换

最后变换后的向量的协方差矩阵是单位矩阵

随机向量不仅变成了独立的，能量还是 1，想当于是白噪声

所以需要想办法把$\Sigma$变成单位矩阵

$$
\Sigma^{-\frac{1}{2}} \Sigma \Sigma^{-\frac{1}{2}} = I
$$

$$
\begin{cases}
\tilde{\Phi} = \Sigma^{-\frac{1}{2}} \Phi\\
b = mx
\end{cases}
$$

$$
\omega' = \Sigma^{-\frac{1}{2}} U^H(x-m_x)
$$

### KL 变换

与 PCA 本质是一样的，但是从信号重构的视角出发

$$
\omega = U^Hx \quad \text{标准正交变换}
$$

信号的重构过程为

$$
\tilde{\omega} = U_M^Hx \longrightarrow \hat{x} = U_M \tilde{\omega}
$$

重构的最优性

$$
\begin{aligned}
e &= x- \hat{x} \\
  &= U\omega - U\tilde{\omega} \\
  &= U(\omega - \tilde{\omega}) \\
  &= \sum_{i=1}^D u_i \omega_i - \sum_{i=1}^M u_i \omega_i \\
  &= \sum_{i=M+1}^D u_i \omega_i \\
  &= \begin{bmatrix}U_{M+1} & \cdots & U_D\end{bmatrix} \omega_e \\
  &= U_e
\end{aligned}
$$

$$
\begin{aligned}
\mathbb{E}(e^H e)
    &= \mathbb{E}(\omega_e^H U_e^H U_e \omega_e) \\
    &= \mathbb{E}(\omega_e^H \omega_e) \\
    &= \sum_{i=M+1}^D |\omega_i|^2 \\
    &= \sum_{i=M+1}^D \lambda_i \\
\end{aligned}
$$

## EVD | 特征分解

处理的一般是

$$
A = U \Sigma U^H
$$

- A：数据协方差矩阵
- U 拿出来之后，可以用来降维；
- 可以用来去相关 (标准正交变换)

$$
\{y_n\}_{n=1}^N \xrightarrow{\text{求解协方差}} c = \frac1{N-1} \sum^{N}_{n=1} y_n y_n^H \xrightarrow{\text{EVD}} 下游任务
$$

绕不开的操作是求解协方差矩阵

### 计算方法

[全网最快速的特征向量暴力求法（纯干货技巧）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aT411E75Q/?spm_id_from=333.337.top_right_bar_window_history.content.click)

[相似对角化太难算，哈 - 凯定理怒斩 A 的 n 次方！（细节拉满了）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV11P411w716/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

**求特征值**：

- 计算矩阵 $A$ 的特征值 $\lambda_i$ ，这些特征值将构成对角矩阵 $\Lambda$ 的对角线元素。

**求特征向量**：

- 对于每个特征值 $\lambda_i$，求解特征向量 $v_i$，这些特征向量将构成矩阵 $P$ 的列。

**构造对角矩阵和特征向量矩阵**：

- 对角矩阵 $\Lambda$：

$$
\Lambda = \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

- 特征向量矩阵 $P$：

$$
P = \begin{bmatrix}
| & | & & | \\
v_1 & v_2 & \cdots & v_n \\
| & | & & |
\end{bmatrix}
$$

**验证对角化**：

- 验证 $A = P \Lambda P^{-1}$ 是否成立。

### Hermitian 矩阵特征分解

设 $X$ 是一个 $n \times n$ 的 Hermitian 矩阵，特征值分解 (Eigenvalue Decomposition, EVD) 可以写成：

$$
X = U \Sigma U^H = [u_1 \quad u_2 \cdots \quad u_n] \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix} \begin{bmatrix}
u_1^H \\
u_2^H \\
\vdots \\
u_n^H
\end{bmatrix} = \sum_{i=1}^{n} \lambda_i u_i u_i^H
$$

这里：
$u_1, u_2, ..., u_n$ 是矩阵的特征向量; $\lambda_1, \lambda_2, ..., \lambda_n$ 是矩阵的特征值

### PCA | 主成分分析

线性降维写成矩阵乘法形式：

$$
\Phi x_n=z_n
$$

- 投影矩阵：$\Phi\in R^M\times D$
- 原始数据向量：$\mathbf{x}_n\in R^{D\times1}$
- 降维后的向量：$\mathbf{z}_n\in R^M\times1$

**主成分分析 (PCA):**

PCA 是一种基于特征分解的统计技术，用于简化数据集的复杂性，同时保留尽可能多的方差 (信息)。它通过找到数据集中方差最大的方向 (主成分),将高维数据投影到这些方向上，实现降维。

对于样本 $\{x_n\}_{n=1}^N$，PCA 的步骤如下：

1. **计算数据均值向量（或中心化）：**

    $$
    \mu = \frac{1}{N} \sum_{n=1}^N x_n
    $$

2. **估计协方差矩阵：**

    $$
    \widehat{C} = \frac{1}{N-1} \sum_{n=1}^N (x_n - \mu)(x_n - \mu)^H
    $$

3. **对协方差矩阵 $\widehat{C}$ 进行特征值分解 EVD：**

    $$
    \widehat{C} = U \Sigma U^H
    $$

    或者写为

    $$
    \widehat{C} =
    \begin{bmatrix}
    u_1 & u_2 & \cdots & u_n
    \end{bmatrix}
    \begin{bmatrix}
    \lambda_1 & 0 & \cdots & 0 \\
    0 & \lambda_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \lambda_n
    \end{bmatrix}
    \begin{bmatrix}
    u_1 & u_2 & \cdots & u_n
    \end{bmatrix}^H
    $$

    其中 $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$。

4. **降维：**  
若从 $D$ 维降到 $M$ 维，则选择最大的前 $M$ 个特征值对应的特征向量，构成投影矩阵：

$$
\Phi_{M \times D} \triangleq
\begin{bmatrix}
u_1^H \\
u_2^H \\
\vdots \\
u_M^H
\end{bmatrix}
$$

---

核心思想：降维后，数据方差最大

上述过程等价于求解二次型的有约束极值问题：

$$
\begin{aligned}
&\text{证明：} \\
&\text{假设 } M=1, \\
&\quad Var(z_n) = E[(z_n - \overline{z_n})(z_n - \overline{z_n})^H] \\
&\quad = E\left[(\Phi_1^H x_n - \Phi_1^H \overline{x}_n)(x_n^H \Phi_1 - \overline{x_n^H} \Phi_1)\right] \\
&\quad = \Phi_1^H E\left[(x_n - \overline{x}_n)(x_n^H - \overline{x_n^H})\right] \Phi_1 \\
&\quad = \Phi_1^H C \Phi_1 \\
&\text{约束优化问题：} \\
&\quad \max_{\Phi_1} \Phi_1^H C \Phi_1 \\
&\quad \text{Subject to} \quad \Phi_1^H \Phi_1 = 1
\end{aligned}
$$

这个问题可以通过拉格朗日乘数法求解。构造拉格朗日函数：

$$
f(\Phi_1) \triangleq \Phi_1^H C \Phi_1 + \lambda (1 - \Phi_1^H \Phi_1)
$$

对 $f(\Phi_1)$ 关于 $\Phi_1$ 求导并令其为零：

$$
C \Phi_1 = \lambda \Phi_1
$$

即 $\Phi_1$ 是 $C$ 的一个特征向量。此时：

$$
f(\Phi_1) = \Phi_1^H C \Phi_1 = \lambda \Phi_1^H \Phi_1 = \lambda
$$

因此，取最大的特征值 $\lambda_1$ 时 $f(\Phi_1)$ 最大，此时 $\Phi_1$ 为最大特征值对应的特征向量 $\mathbf{u}_1$。

## SVD | 奇异值分解

能否跳过协方差矩阵的计算？直接对数据向量$\{y_n\}_{n=1}{N}$进行操作？

如何对非方阵进行分解？

$$
A = U \Sigma V^H
$$

- $U^HU = UU^H = I$     左奇异向量
- $V^HV = VV^H = I$     右奇异向量
- $\Sigma \in \mathbb{C}^{m \times n}$ 对角线上的元素是奇异值，不是方阵

$$
\Sigma_{m\times n} =
\begin{bmatrix}
\sigma_1 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
0 & \sigma_2 & \cdots & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & & \vdots \\
0 & 0 & \cdots & \sigma_r & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
\end{bmatrix}_{m\times n}= \begin{bmatrix}
\Sigma_r & 0_{r, n-r} \\
0_{m-r, r} & 0_{m-r, n-r}
\end{bmatrix}_{m\times n}\\
\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 \quad \text{且} \quad \text{rank}(A) = r
$$

$\sigma_i$ 是奇异值，$r$ 是秩

### 性质

$$
\begin{aligned}
&\text{Y 是方阵} \qquad && Y = U\Sigma U^H \\
&&& Y^2 = U\Sigma^2 U^H \\[1.5ex]
&\text{Y 不是方阵} \quad Y_{m\times n} \qquad && Y = U\Sigma V^H \\
&&& YY^H = U\Sigma V^H V \Sigma^H U^H \\
&&& \phantom{YY^H} = U \Sigma \Sigma^H U^H \\
&&& \phantom{YY^H} = U
    \begin{bmatrix}
        \Sigma_r & 0 \\
        0 & 0
    \end{bmatrix}
    \begin{bmatrix}
        \Sigma_r^H & 0 \\
        0 & 0
    \end{bmatrix}
    U^H \\
&&& \phantom{YY^H} = U \Sigma^2 U^H \\
\end{aligned}
$$

### SVD 计算方法

$$
\{y_n\}_{n=1}^N \xrightarrow{\text{SVD}} Y = U\Sigma V^H \rightarrow \begin{cases}
U_{\color{red}{m\times m}} \quad 标准正交变换\\
U_r{\color{red}{m\times r}} \quad PCA/KL\\
\end{cases}
$$

- $Y Y^H = U \Sigma V^H V \Sigma^H U^H = U \Sigma^2 U^H$
  - 构造矩阵$Y Y^H$
  - 对$Y Y^H$进行特征值分解 EVD，得到特征值$\lambda_i$和特征向量$u_i$
  - $\sigma_i = \sqrt{\lambda_i}$

- $Y^H Y = V \Sigma^H U^H U \Sigma V^H = V \Sigma^2 V^H$
  - 构造矩阵$Y^H Y$
  - 对$Y^H Y$进行特征值分解 EVD，得到特征值$\lambda_i$和特征向量$v_i$
  - $\sigma_i = \sqrt{\lambda_i}$

注意，奇异值的定义中就是大于 0 的

### 直观理解

变换 = 旋转和伸缩组合

那么如果想把一个变换表示成为旋转和伸缩的组合，考虑先旋转到坐标轴，再做伸缩，最后再旋转回来，这就是奇异值分解

1.奇异值为非负数
2.奇异值主对角线由小到大排列
3.奇异值是特征值开方

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112996076490296&bvid=BV1ExWxesEVf&cid=500001656999667&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

奇异值分解

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=652439242&bvid=BV1YY4y1U7UX&cid=1024031413&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

作用：求解逆矩阵、伪逆矩阵

### 截断 SVD(truncated SVD)

$$
\begin{aligned}
Y_{\color{red}{m\times n}}
    &= U_{\color{red}{m\times m}}
        \begin{bmatrix}
            \Sigma_{\color{red}{r\times r}} & O \\
            O & O
        \end{bmatrix}_{\color{red}{m\times n}}
        V_{\color{red}{n\times n}}^H \\[1.5ex]
    &=
        \begin{bmatrix}
            {U_r}_{\color{red}{m\times r}} & X
        \end{bmatrix}
        \begin{bmatrix}
            \Sigma_r & O \\
            O & O
        \end{bmatrix}
        \begin{bmatrix}
            {V_r}_{\color{red}{r\times n}} & X
        \end{bmatrix}^H \\[1.5ex]
    &= U_r \Sigma_r V_r^H
\end{aligned}
$$

$$
r \leq \min(m, n)
$$

可以实现数据的压缩

```c title="matlab 代码"
svd(Y,'econ')
```

econ: economic mode

### 应用 1 - 求伪逆矩阵

$$
\Sigma^\dagger = \begin{bmatrix}
\Sigma_r^{-1} & O \\
O & O
\end{bmatrix}
$$

#### 左逆

首先对$A$进行 SVD 分解

$$
A_{\color{red}{m\times n}} = U_{\color{red}{m\times m}} \begin{bmatrix}
\Sigma_n\\
O
\end{bmatrix}_{\color{red}{m\times n}} V_{\color{red}{n\times n}}^H
$$

可以根据$LA = I$的方法构造$L$

$$
LA = I = {\color{red}V \begin{bmatrix}
\Sigma_n^{-1} & O
\end{bmatrix}U^H}{\color{blue}U \begin{bmatrix}
\Sigma_n\\
O
\end{bmatrix}V^H}\\
\therefore L = {\color{red}V \begin{bmatrix}
\Sigma_n^{-1} & O
\end{bmatrix}U^H} \qquad A = {\color{blue}U \begin{bmatrix}
\Sigma_n\\
O
\end{bmatrix}V^H}
$$

$$
m \leq n \quad \text{且} \quad \text{rank}(A) = m \quad \text{列满秩}\\
L = V \Sigma^\dagger U^H
$$

#### 右逆

fat matrix，且行满秩

$$
m \leq n \quad \text{且} \quad \text{rank}(A) = m \quad \text{行满秩}\\
AR = I \qquad R = V\Sigma^\dagger U^H\\
$$

#### 秩亏

$$
rank(A) < \min(m, n) \quad \text{秩亏}\\
A^\dagger = V \Sigma^\dagger U^H
$$

### 应用 2 - 求范数

!!! note "酉变换的性质"
      主要使用“酉矩阵不改变向量的范数”这一性质

      $U$,$V$是酉矩阵，$U^H = U^{-1}$,$V^H = V^{-1}$

      $$
      \langle Ux, Uy \rangle = \langle x, y \rangle\\
      ||Ux||_2 = ||x||_2\\
      $$

**谱范数**

$$
\begin{aligned}
&\|A\|_2=\|A\|_{\mathrm{spec}}=\max_{x\neq0}\frac{\|Ax\|_2}{\|x\|_2}=\sqrt{\lambda_{\max}}=\sigma_{\max}\\
\Leftrightarrow& \max_{x\neq0}\;\frac{\|Ax\|_2^2}{\|x\|_2^2}\quad \text{改成瑞丽商的形式}\\
\Leftrightarrow&\max_{x}\;\|Ax\|_2^2\quad \mathrm{~s.t.~}\|x\|_2=1\\
\Leftrightarrow&\max_{x}\;x^HA^HAx\quad\mathrm{~s.t.~}x^Hx=1\\
\end{aligned}
$$

$x_{\mathrm{opt}}$为$A^HA$最大特征值对应的特征向量

$$
\|Ax_{\mathrm{opt}}\|^2=\lambda_{\max}=\sigma_{\max}^2
$$

**F 范数**

$$
\begin{aligned}
    ||A||_F &= \sqrt{\sum_{i=1}^{m}\sum_{j=1}^{n}|a_{ij}|^2} \\
            &= ||U\Sigma V^H||_F \\
            &= ||\Sigma||_F \\
            &= \sqrt{\sum_{i=1}^{r}\sigma_i^2}
\end{aligned}
$$

### 应用 3 - SVD 图像降噪

!!! note "图像本身就是一个矩阵"

    - Y 图片
    - N 噪声
    - X 去噪后的图片

    $$
    Y = X + N
    $$

$$
\begin{aligned}
    X &= U \Sigma V^H \\
      &= \sum_{i=1}^{r} \sigma_i u_i v_i^H \qquad r \leq \min(m, n)
\end{aligned}
$$

$$
Y = \sum_{i=1}^{k} \tilde{\sigma}_i \tilde{u}_i \tilde{v}_i^H
$$

$$
\hat{X} = \sum_{i=1}^{r} \tilde{\sigma}_i \tilde{u}_i \tilde{v}_i^H
$$

### 应用 4 - 矩阵低秩逼近

需求：$P \leq r$, rank-P 矩阵 $\hat{Y}$,使得$Y$与$\hat{Y}$最接近

问题建模

$$
Y_{\color{red}{m\times n}} \xrightarrow{\text{SVD}} Y = U\Sigma V^H \xrightarrow{\text{截断 SVD}} \hat{Y} = U_r \Sigma_r V_r^H\\
\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0 \quad \text{且} \quad \text{rank}(A) = r \leq \min(m, n)\\
$$

$$
\min_{\hat{Y}} ||Y - \hat{Y}||_F^2 \quad \text{or} \quad \min_{\hat{Y}} ||Y - \hat{Y}||_2^2\\
s.t. \quad \text{rank}(\hat{Y})= P
$$

最优逼近定理

$$
Y = U_r \Sigma_r V_r^H = \sum_{i=1}^{r} \sigma_i u_i v_i^H\\
\hat{Y} = \sum_{i=1}^{P} \sigma_i u_i v_i^H \quad (P \leq r)\quad \text{是} Y \text{的} P \text{阶最佳逼近}\\
$$

把截断 SVD 的前 p 个分量取出来

逼近误差 approximation error

$$
||Y - \hat{Y}|| = ||\sum_{i=1}^r \sigma_i u_i v_i^H - \sum_{i=1}^P \sigma_i u_i v_i^H||\\
= ||\sum_{i=P+1}^r \sigma_i u_i v_i^H||
$$

$$
\begin{aligned}
||Y - \hat{Y}||_F &= \sqrt{\sigma_{P+1}^2 + \sigma_{P+2}^2 + \cdots + \sigma_r^2}\\
||Y - \hat{Y}||_2 &= \sigma_{P+1}
\end{aligned}
$$

有效秩（$P$）的确定：是一个超参数调优的问题

- P 过大，overfit noise
- P 过小，underfit data

SNR 较大的时候，使用拐点图

- 归一化奇异值方法

$$
\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0\\
1 \geq \frac{\sigma_1}{\sigma_2} \geq \cdots \geq \frac{\sigma_{r-1}}{\sigma_r} \geq 0\\
$$

- 范数比方法

$$
\frac{|\hat{Y}|_F}{|Y|_F}= \frac{\sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_P^2}}{\sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_r^2}} \leq 1\\
= V(P)
$$

$$
V(P) \geq \alpha, \quad \alpha  = 0.9,0.95 \cdots
$$

SNR 较低，贝叶斯低秩分解

## 张量 CP 分解

张量分解是矩阵分解的推广，矩阵是 2 阶张量，向量是 1 阶张量，标量是 0 阶张量
