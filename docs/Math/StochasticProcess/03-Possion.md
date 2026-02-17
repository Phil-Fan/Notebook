# 03 | 泊松过程

## Cheet Sheet

| 字母 | 含义 |
| ---- | ---- |
| $N(t)$ | 在时间 $t$ 内发生的"事件"数 |
| $W_n$ | 第 $n$ 个事件发生的时刻 |
| $T_i$ | 第 $i$ 个事件和第 $i-1$ 个事件发生的时间间隔 |

齐次泊松过程

$$
\begin{aligned}
P\left[N(t)-N(s)=k\right]&\sim\pi(\lambda(t-s))\\
&=\frac {[\lambda(t-s)]^k·e^{-\lambda(t-s)}}{k!},\quad k=0,1,2,\dots
\end{aligned}
$$

**非齐次泊松过程**:差值变成积分的上下限

$$
\begin{aligned}
P(N(t)-N(s)=k)&\sim \pi(\int_s^{t} \lambda(u) du)
\end{aligned}
$$

数字特征

- 均值函数：$\mu_N(t)=E[N(t)]=\lambda t$
- 方差函数：$D_N(t)=D[N(t)]=\lambda t$

- 自相关函数：$C_N(t_1,t_2)=Cov[N(t_1),N(t_2)]=\lambda min(t_1,t_2)+\lambda^2t_1t_2$

- 自协方差函数：$R_N(t_1,t_2)=E[N(t_1)·N(t_2)]=\lambda min(t_1,t_2)$

求解思路

1. 泊松过程的合成与分解。应用题比较多，这里要注意分类不重不漏。
   - 一般求条件概率，上下的$e$的指数项可以消去
   - 如果有求解$X\geq m$类型的概率，都是使用$1-P(X<m)$来求解。

2. 独立增量过程，将不独立的变量转化为独立增量。

3. 各种相关分布的结论。指数分布刻画时间，柏松分布刻画计数，参数相同

## 独立增量过程

$\forall\;n\geq2$ 且 $n\in Z$ 与 $t_0<t_1<\dots<t_n$ ，增量 $X(t_1)-X(t_0),X(t_2)-X(t_1),\dots,X(t_n)-X(t_{n-1})$ 相互独立。

性质：

若$\left\{X(t),t\geq0\right\}$是独立增量过程，且$X(0)=0$,则：

1. $X( t)$的有限维分布函数族可以由增量$X(t)-X(s)\left(0\leq s<t\right)$的分布所确定；
2. 设 $D_X(t)$ 已知，则$C_X(s, t) = D_X\left(\min(s, t)\right)$

若对$\forall h$和$\forall s<t$,$X(t+h)-X(s+h)\overset{d}{=}X(t)-X(s),$称$\{X(t)\}$平稳增量过程

- 独立增量 + 平稳增量=平稳 (齐次) 独立增量

!!! example "概念辨析"
    下列过程中哪一个不是平稳独立增量过程。()

    - (A) 强度为 $\lambda$ 的泊松过程 $\{N(t); t \geq 0\}$
    - (B) 强度为 $t^2$ 的非齐次泊松过程 $\{N(t); t \geq 0\}$
    - (C) 标准布朗运动 $\{B(t); t \geq 0\}$
    - (D) 随机过程 $\{B(t+1) - B(1); t \geq 0\}$，其中 $\{B(t); t \geq 0\}$ 是标准布朗运动

    --- 
    对于强度为$t^2$的随机过程，不满足平稳增量，每一个相同区间其实是不一样的，比较显然。

## 泊松分布

$$
P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}, \quad k=0,1,2,\dots
$$

记 $X\sim \pi(\lambda)$ ，相当于$n$很大，$p$很小，$np=\lambda$ 的二项分布。

（不用二项分布的原因：当$n$很大的时候，$p^k$,$p^{n-k}$,$C_n^k$ 都计算起来很麻烦）

??? note "简单推导"

    栗子树掉栗子，时间切分 $n$ 份，$k$ 个栗子掉下，$p$ 为每份掉栗子的概率：

    $$
    P(k) = C_n^k p^k (1-p)^{n-k}
    $$

    但是并不知道$p$，所以需要间接求解

    令期望

    $$
    \lambda = E(x) = np \implies p = \frac{\lambda}{n}
    $$

    $$
    \begin{aligned}
    \therefore P(k) &= \lim_{n \to \infty} C_n^k \left(\frac{\lambda}{n}\right)^k \left(1-\frac{\lambda}{n}\right)^{n-k} \\
    &= \lim_{n \to \infty} \frac{n(n-1)\cdots(n-k+1)}{k!} \left(\frac{\lambda}{n}\right)^k \left(1-\frac{\lambda}{n}\right)^{n-k} \\
    &= \lim_{n \to \infty} \frac{\lambda^k}{k!} \left(1-\frac{\lambda}{n}\right)^n \left[\frac{n}{n} \cdot \frac{n-1}{n} \cdots \frac{n-k+1}{n}\right] \left(1-\frac{\lambda}{n}\right)^{-k} \\
    &= \lim_{n \to \infty} \frac{\lambda^k}{k!} \left[\left(1-\frac{\lambda}{n}\right)^{-\frac{n}{\lambda}}\right]^{-\lambda} \quad \text{（利用极限性质）} \\
    &= e^{-\lambda} \frac{\lambda^k}{k!}
    \end{aligned}
    $$

### 条件

- 事件在一定时间发生次数随机，要么发生，要么不发生
- 每段无限小的时间，事件发生两次的概率无限趋近于 0
- 不同时间，事件独立

### 性质

- 期望：$E(X) = \lambda$

- 方差：$D(X) = \lambda$

- 线性：$X\sim \pi(\lambda) ,Y\sim \pi(\lambda_2) \implies X+Y\sim \pi(\lambda_1+\lambda_2)$

??? note "推导"

    $$
    \begin{aligned}
    E(x)&=\sum_{i=0}^{\infty}iP(x-i)=\sum_{i=1}^{\infty}i\frac{e^{-\lambda}\lambda^{i}}{i!}=\lambda e^{-\lambda}\sum_{i=1}^{\infty}\frac{\lambda^{i-1}}{(i-1)!}=\lambda\cdot e^{-\lambda}\cdot e^{\lambda}=\lambda\\
    E(x^{2})&=\sum_{i=0}^{\infty}i^{2}P(x-i)=\sum_{i=1}^{\infty}i^{2}\frac{e^{-\lambda}\lambda^{i}}{i!}=\lambda e^{-\lambda}\sum_{i=1}^{\infty}\frac{i\lambda^{i-1}}{(i-1)!}=\lambda e^{-\lambda}\sum_{i=1}^{\infty}\frac{i\lambda^{i-1}}{(i-1)!}\frac{d}{d\lambda}(\lambda^{i})\\
    &=\lambda e^{-\lambda}\frac{d}{d\lambda}[\lambda_{i=1}^{\infty}\frac{\lambda^{i-1}}{(i-1)!}]=\lambda e^{-\lambda}\frac{d}{d\lambda}(\lambda e^{\lambda})=\lambda e^{-\lambda}(e^{\lambda}+e^{\lambda}\lambda)\\
    \therefore D(x)&=E(x^2)-[E(x)]^{2}=\lambda^{2}+\lambda-\lambda^{2}=\lambda
    \end{aligned}
    $$

### 指数分布与泊松分布

=== "泊松分布"

    * 用于描述**单位时间或单位空间内事件发生的次数**。
    * 若某随机变量 $X \sim \text{Poisson}(\lambda t)$，则表示单位时间内平均有 $\lambda$ 次事件，$t$ 为观察时间长度。
    * 概率质量函数（PMF）：

      $$
      P(X = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}, \quad k = 0, 1, 2, \dots
      $$

=== "指数分布"

    * 用于描述**两个事件之间的时间间隔（等待时间）**。
    * 若等待时间 $T \sim \text{Exp}(\lambda)$，表示事件平均每单位时间发生 $\lambda$ 次。
    * 概率密度函数（PDF）：

      $$
      f(t) = \lambda e^{-\lambda t}, \quad t \geq 0
      $$

1. **泊松过程中的时间间隔分布是指数分布**：

   - 若事件发生服从**泊松过程**（单位时间平均事件数为 $\lambda$，独立且均匀随机地发生），
   - 那么**相邻两次事件的时间间隔**服从参数为 $\lambda$ 的**指数分布**。
   - 换句话说，如果事件发生的次数在时间 $t$ 内是泊松分布的，那么**事件发生的时间间隔是指数分布**。

2. **从指数分布推导泊松分布**：

   - 如果事件间的时间间隔 $T_i \sim \text{Exp}(\lambda)$，
   - 那么在时间 $t$ 内发生的事件数 $N(t)$ 服从泊松分布 $\text{Poisson}(\lambda t)$。

3. **指数分布是泊松过程的“等待时间”分布**：

   - 例如，第一次事件发生的时间 $T_1 \sim \text{Exp}(\lambda)$，
   - 第二次事件发生的时间是两个独立指数分布的和 $T_2 = T_1 + T'_1$，其总和服从**Gamma 分布**。

| 对比项 | 泊松分布 | 指数分布 |
| ---- | -------------------------------------------------- | ------------------------------- |
| 类型 | 离散分布（事件数） | 连续分布（时间） |
| 参数 | $\lambda$（单位时间平均事件数） | $\lambda$（事件速率） |
| 应用场景 | 某时间内事件数 | 两个事件之间的时间间隔 |
| 关系 | 单位时间内事件总数 | 相邻事件间隔 |
| 分布公式 | $P(X=k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!}$ | $f(t) = \lambda e^{-\lambda t}$ |

### 例题

??? example "排队"
    排队：两个服务窗口, 设一段时间前来访问人数 $X\sim \pi(1)$

    出现排队等候概率为

    $$
    P\{X>2\}=1-P\{X\leq2\}=1-e^{-1}(1+1+\frac{1}{2})=1-\frac{5}{2e}.
    $$

??? example "患病"
    疾病: 假设某种疾病的发病人数 $X\sim \pi(\lambda)$，其中$\lambda$未知，且已知某人患病的概率为 0.001。

    解释：这里的“病概率 0.001”可以理解为“至少有一人患病的概率为 0.001”。对于泊松分布，$P(X=0)=e^{-\lambda}$，即没有人患病的概率。因此，至少有一人患病的概率为 $1 - e^{-\lambda}$。

    设 $1 - e^{-\lambda} = 0.001$，则 $e^{-\lambda} = 0.999$，两边取对数得 $\lambda = -\ln(0.999) = \ln\left(\frac{1}{0.999}\right) = \ln\left(\frac{1000}{999}\right)$。

    总结：$\lambda = \ln\left(\frac{1000}{999}\right)$

    故分布律为

    $$
    P\{X = k\} = 0.999 \frac{(\ln \frac{1000}{999})^k}{k!}, k = 0, 1, \cdots
    $$

## 齐次泊松过程

定义 $N(t)$ 表示 $(0,t\,]$ 内发生的"事件"数。

若计数过程 { $N(t);t\leq0$ } 是强度为 $\lambda$ 的**齐次泊松过程**，则

- $N(0)=0$

- 独立增量过程${ N(t);t\leq0}$

- 对于 $\forall\;0\leq s<t$ ，有
  - 若$s > 0$，则
  
    $$
    \begin{aligned}
    P\left[N(t)-N(s)=k\right]&\sim\pi(\lambda(t-s))\\
    &=\frac {[\lambda(t-s)]^k·e^{-\lambda(t-s)}}{k!},\quad k=0,1,2,\dots
    \end{aligned}
    $$

  - 若$s = 0$，则

    $$
    P\left[N(t)=k\right]=\frac {[\lambda t]^k·e^{-\lambda t}}{k!},\quad k=0,1,2,\dots
    $$

- 对于 $\forall\quad t>s\quad n\leq m$

$$
P(N_s=m\mid N_t=n)=C_n^m(\frac st)^m\cdot(1-\frac st)^{n-m}
$$

$$
\begin{aligned}
P(N_t = n | N_s = m) &= \frac{P(N_s = m, N_t - N_s = n - m)}{P(N_s = m)}\\
&= P(N_t - N_s = n - m)\\
&= \frac{(\lambda(t-s))^{n-m}}{(n-m)!} e^{-\lambda(t-s)}
\end{aligned}
$$

### 齐次泊松过程的性质

- 均值函数：$\mu_N(t)=E[N(t)]=\lambda t$
- 方差函数：$D_N(t)=D[N(t)]=\lambda t$

- 自相关函数：$R_N(t_1,t_2)=E[N(t_1)·N(t_2)]=\lambda min(t_1,t_2)$

- 自协方差函数：$C_N(t_1,t_2)=Cov[N(t_1),N(t_2)]=\lambda min(t_1,t_2)+\lambda^2t_1t_2$

## 合成与分解

### 泊松过程的合成

若 { $X(t);t\leq0$ } 与 { $Y(t);t\leq0$ } 是相互独立的分别具有强度 $\lambda_1$ 和 $\lambda_2$ 的泊松过程，

则 { $N(t)=X(t)+Y(t);t\leq0$ } 是强度为 $\lambda_1+\lambda_2$ 的泊松过程。

### 泊松过程的分解

若计数过程 { $N(t);t\leq0$ } 是强度为 $\lambda$ 的**泊松过程**

且对于事件 $N$ ，其中类型 $X$ 发生的概率为 $p$ ，类型 $Y$ 发生的概率为 $1-p$ ，则 { $X(t);t\leq0$ } 与 { $Y(t);t\leq0$ } 是相互独立的分别具有强度 $\lambda p$ 和 $\lambda (1-p)$ 的泊松过程。且相互独立

??? note "证明"

    显然 $N_1(0) = N_2(0)$。对任意 $t > s \geq 0$，

    $$
    \begin{aligned}
    P\{N_1(t) - N_1(s) = m,\, N_2(t) - N_2(s) = n\}
    &= P\{N_1(t) - N_1(s) = m,\, N(t) - N(s) = m+n\} \\
    &= P\{N_1(t) - N_1(s) = m \mid N(t) - N(s) = m+n\} \cdot P\{N(t) - N(s) = m+n\} \\
    &= \binom{m+n}{m} p^m (1-p)^n e^{-\lambda(t-s)} \frac{(\lambda(t-s))^{m+n}}{(m+n)!} \\
    &= \left[ e^{-\lambda p(t-s)} \frac{(\lambda p(t-s))^m}{m!} \right] \cdot \left[ e^{-\lambda(1-p)(t-s)} \frac{(\lambda(1-p)(t-s))^n}{n!} \right]
    \end{aligned}
    $$

    于是：

    $$
    \begin{aligned}
    P\{N_1(t) - N_1(s) = m\}
    &= \sum_n P\{N_1(t) - N_1(s) = m,\, N_2(t) - N_2(s) = n\} \\
    &= \sum_n \left[ e^{-\lambda p(t-s)} \frac{(\lambda p(t-s))^m}{m!} \cdot e^{-\lambda(1-p)(t-s)} \frac{(\lambda(1-p)(t-s))^n}{n!} \right] \\
    &= e^{-\lambda p(t-s)} \frac{(\lambda p(t-s))^m}{m!} \cdot \sum_n e^{-\lambda(1-p)(t-s)} \frac{(\lambda(1-p)(t-s))^n}{n!} \\
    &= e^{-\lambda p(t-s)} \frac{(\lambda p(t-s))^m}{m!}
    \end{aligned}
    $$

    因此：

    $$
    N_1(t) - N_1(s) \sim \pi(\lambda p(t-s))
    $$

    同理：

    $$
    N_2(t) - N_2(s) \sim \pi(\lambda (1-p)(t-s))
    $$

    且 $N_1(t) - N_1(s)$ 与 $N_2(t) - N_2(s)$ **相互独立**。

    --- 

    下面证这两个过程是相互独立的独立增量过程。

    由于$\{N(t)\}$是独立增量过程，且各事件属于哪种类型相互独立，所以对任何$0=t_{0}<t_{1}<\cdots<t_{n}$, $(N_{1}(t_{1})-N_{1}(t_{0}),N_{2}(t_{1})-N_{2}(t_{0}))$, $\cdots$, $(N_{1}(t_{n})-N_{1}(t_{n-1}),N_{2}(t_{n})-N_{2}(t_{n-1}))$这$n$个二维随机变量相互独立。

    又对所有$0\leq i<n$, $N_{1}(t_{i+1})-N_{1}(t_{i})$与$N_{2}(t_{i+1})-N_{2}(t_{i})$相互独立
    
    所以$N_{1}(t_{1})-N_{1}(t_{0})$, $N_{2}(t_{1})-N_{2}(t_{0})$, $\cdots$, $N_{1}(t_{n})-N_{1}(t_{n-1})$, $N_{2}(t_{n})-N_{2}(t_{n-1})$这$2n$个随机变量相互独立。

    $\{N_{1}(t)\}$和$\{N_{2}(t)\}$是独立增量过程

    对任何$0=t_{0}<t_{1}<\cdots<t_{n}$

    $(N_{1}(t_{1}),\ldots,N_{1}(t_{n}))$与$(N_{2}(t_{1}),\ldots,N_{2}(t_{n}))$相互独立

    这两个过程是相互独立的独立增量过程。

## 与泊松分布相关的若干分布

### 发生时刻

$W_n$ 是第 $n$ 个事件发生的时刻。

$$
W_n\sim \Gamma(n,\lambda)
$$

$W_{n}$的分布函数

$$
\begin{aligned}
F_{W_{n}}(t)&=P(W_{n} \leq t)=P(N(t) \geq n)\\
&=\left\{\begin{array}{ll}
\sum_{k=n}^{\infty} P(N(t)=k)=\sum_{k=n}^{\infty} \frac{(\lambda t)^{k}}{k!} e^{-\lambda t} & t \geq 0 \\
0 & t<0
\end{array}\right.
\end{aligned}
$$

因此，$W_{n}$的概率密度为：

$$
\begin{aligned}
f_{W_{n}}(t)&=\frac{d F_{W_{n}}(t)}{d t}\\
&=\left\{\begin{array}{cc}
\sum_{k=n}^{\infty} \frac{k \lambda^{k} t^{k-1}}{k!} e^{-\lambda t}-\sum_{k=n}^{\infty} \frac{\lambda^{k+1} t^{k}}{k!} e^{-\lambda t}=\frac{\lambda(\lambda t)^{n-1}}{(n-1)!} e^{-\lambda t}, & t>0 \\
0, & t \leq 0
\end{array}\right.
\end{aligned}
$$

### 时间间隔

$T_i=W_i-W_{i-1}$ 为第 $i$ 个事件和第 $i-1$ 个事件发生的时间间隔，则 $\forall\;i\quad T_i$ 均服从均值为 $\frac1\lambda$ 的指数分布。

$$
\begin{aligned}
F_{T_i}(t)&=P(T_i\leq t)=1-P(T_i>t)\\
&=1-P(N(t)<1)\\
&=1-P(N(t)=0)\\
&=1-e^{-\lambda t}\\
f_{T_i}(t)&=\begin{cases}
\lambda e^{-\lambda t}, & t>0\\
0, & t\leq0
\end{cases}
\end{aligned}
$$

!!! note "定理"

    $\{N(t)\}$是强度为$\lambda$的泊松过程
    
    当且仅当其时间间隔 $T_1,T_2,...$独立同分布，且服从均值$\frac1\lambda$的指数分布.

### 条件分布

若已知 $(0,t\,]$ 内恰好有一事件发生，则此事件的发生时刻在 $(0,t\,]$ 内均匀分布。

$$
P(T_1\leq s\mid N(t)=1)=\frac st\qquad 0<s\leq t
$$

$$
\begin{aligned}
F_{T_1|N(t)=1}(s)&=P(T_1\leq s|N(t)=1)\\
&=\frac{P(T_1\leq s,N(t)=1)}{P[N(t)=1]}=\frac{P[N(s)=1,N(t)-N(s)=0]}{P[N(t)=1]}\\
&=\frac{\lambda se^{-\lambda s}\times e^{-\lambda(t-s)}}{\lambda te^{-\lambda t}}\\
&=\frac{s}{t}\\
f_{T_1|N(t)=1}(s)&=\frac{1}{t},0<s<t
\end{aligned}
$$

## 非齐次泊松过程

!!! note "$\lambda$ 不再为常数，而是 $t$ 的函数"

若计数过程 { $N(t);t\leq0$ } 是强度为 $\lambda(t)$ 的**非齐次泊松过程**，则

**①** $N(0)=0$

**②** { $N(t);t\leq0$ } 为独立增量过程

**③** 对于 $\forall\;0\leq s<t$ ，有

$$
\begin{aligned}
P(N(t)-N(s)=k)&\sim \pi(\int_s^{t} \lambda(u) du)\\
&=\frac {[\int_s^t\lambda(u)du]^k·e^{-\int_s^t\lambda(u)du}}{k!},\quad k=0,1,2,\dots,\\
\end{aligned}
$$

## 例题解答

### 泊松过程计算

!!! example "顾客依泊松过程到达某商店，速率为 4 人/小时。已知商店上午 9:00 开门。"

    **(1) 求到 9:30 时仅到一位顾客，而到 11:30 时时间的已到 5 位顾客的概率？**

    解：以上午九点作为 0 时刻，以 1 小时作为单位时间。以$N(t)$表示$(0,t]$内来到的顾客数，则$\{N(t)\}$是$\lambda=4$的泊松过程。

    $$
    \begin{aligned}
    P\{N(0.5)&=1,N(2.5)=5\}\\
    &=P\{N(0.5)=1\}P\{N(2.5)-N(0.5)=4\}\\
    &=(2e^{-2})(\frac{e^{-8}8^4}{4!})=0.0155
    \end{aligned}
    $$

    **(2) 求第 2 位顾客在 10 点前到达的概率？**

    $$
    \begin{aligned}
    P[W(2)\leq1]&=P[N(1)\geq2]\\
    &=1-e^{-4}-4e^{-4}\\
    &=1-5e^{-4}
    \end{aligned}
    $$


    **(3) 求第一位顾客在 9:30 前到达且第二位顾客在 10:00 前到达的概率？**

    $$
    \begin{aligned}
    P[W_1\leq0.5,W_2\leq1]&=P[N(0.5)\geq1,N(1)\geq2]\\
    &=P[N(0.5)=1,N(1)-N(0.5)\geq1]+P[N(0.5)\geq2]\\
    &=0.5\lambda e^{-0.5\lambda}(1-e^{-0.5\lambda})+1-e^{-0.5\lambda}-0.5\lambda e^{-0.5\lambda}\\
    &=1-e^{-2}-2e^{-4}
    \end{aligned}
    $$

!!! example "例题：短信分类的泊松过程"

    用 $N(t)$ 表示在 $(0, t\,]$ 小时内收到的短信数目。设 $\{N(t); t \geq 0\}$ 是强度为 $\lambda = 5$ 条/小时的泊松过程，且每条短信独立地以概率 $0.6$ 是垃圾短信。

    设垃圾短信的数目为 $N_1(t)$，正常短信的数目为 $N_2(t)$。

    则：
    - $\{N_1(t); t \geq 0\}$ 是强度为 $\lambda_1 = \lambda p = 5 \times 0.6 = 3$ 的泊松过程；
    - $\{N_2(t); t \geq 0\}$ 是强度为 $\lambda_2 = \lambda (1-p) = 5 \times 0.4 = 2$ 的泊松过程。

    ---

    **（1）1 小时内收到 2 条短信的概率**

    $$
    P(N(1) = 2) = \frac{5^2 \cdot e^{-5}}{2!} = \frac{25}{2} e^{-5}
    $$

    ---

    **（2）1 小时内收到的垃圾短信数目为 2 条的概率**

    $$
    P(N_1(1) = 2) = \frac{3^2 \cdot e^{-3}}{2!} = \frac{9}{2} e^{-3}
    $$

    ---

    **（3）若已知 3 小时内恰好收到一条短信，则这条短信是在第 2 个小时内收到的概率**

    $$
    \begin{aligned}
    P(N(2) - N(1) = 1 \mid N(3) = 1)
    &= \frac{P(N(3) - N(2) = 0) \cdot P(N(2) - N(1) = 1) \cdot P(N(1) = 0)}{P(N(3) = 1)} \\
    &= \frac{e^{-5} \cdot 5e^{-5} \cdot e^{-5}}{15e^{-15}} \\
    &= \frac{1}{3}
    \end{aligned}
    $$

    ---

    **（4）1 小时内至少收到 1 条短信，且在 3 小时内恰好收到两条短信的概率**

    $$
    \begin{aligned}
    &\quad\; P(N(3) - N(1) = 1,\, N(1) = 1) + P(N(3) - N(1) = 0,\, N(1) = 2) \\
    &= 10e^{-10} \cdot 5e^{-5} + e^{-10} \cdot \frac{5^2}{2!} e^{-5} \\
    &= 62.5 e^{-15}
    \end{aligned}
    $$

    ---

    **（5）若已知 1 小时内至多收到 2 条短信，则至少有 1 条垃圾短信的概率**

    $$
    \begin{aligned}
    P(N_1(1) \geq 1 \mid N(1) \leq 2)
    &= \frac{P(N_1(1) = 1, N_2(1) = 1) + P(N_1(1) = 1, N_2(1) = 0) + P(N_1(1) = 2, N_2(1) = 0)}{P(N(1) \leq 2)} \\
    &= \frac{e^{-5} \cdot (3 \times 2 + 3 + \frac{3^2}{2})}{e^{-5} \cdot (1 + 5 + 12.5)} \\
    &= \frac{27}{37}
    \end{aligned}
    $$

### 相关分布

!!! example "上午 8 点开始某台取款机开始工作，此时有一大堆人排队等待取款，设每人取款时间独立且都服从均值为 10 分钟的指数分布，记 A 为事件“到上午 9 点钟为止恰有 10 人完成取款”，B 为事件“到上午 8:30 为止恰有 4 人完成取款”，求$P(A)$，$P(B|A)$。"

    解：以上午8点作为0时刻，以1小时作为单位时间，以$Nt$表示$\left(0,t\right]$中完成取款的人数，则$\{Nt,t\geq0\}$是$\lambda=6$的泊松过程。

    $A=\{N_1=10\}$，$B=\{N_{0.5}=4\}$

    $P(A)=e^{-6}\frac{6^{10}}{10!}$

    $P(B|A)=P(N_{0.5}=4|N_1=10)=C_{10}^4(0.5)^4(1-0.5)^6=\frac{105}{512}$

!!! example "设{$N(t),t\geq0$}是强度为$\lambda$的泊松过程，$0\leq s<t$,$T_i$和$W_i$分别表示点间间距和等待时间。"

    (1)$P(T_1\leq s|N(t)=2)$;

    $$
    \begin{align*}
    P(T_1\leq s|N(t)=2)&=P(N(s)\geq1|N(t)=2)\\
    &=P(N(s)=1|N(t)=2)+P(N(s)=2|N(t)=2)\\
    &=C^1_2\frac{s}{t}(1-\frac{s}{t})+C^2_2(\frac{s}{t})^2\\
    &=\frac{s(2t-s)}{t^2}
    \end{align*}
    $$

    ---

    (2)$P(W_2\leq s|N(t)=2)$;

    $$
    \begin{aligned}
    P(W_2\leq s|N(t)=2)&=P(N(s)\geq2|N(t)=2)\\
    &=P(N(s)=2|N(t)=2)\\
    &=\frac{s^2}{t^2}
    \end{aligned}
    $$

    --- 

    (3)$P(W_1\leq s,W_2\leq t)$

    $$
    \begin{aligned}
    P(W_1\leq s,\, W_2\leq t) 
    &= P(N(s)\geq 1,\, N(t)\geq 2) \\
    &= P(N(s)=1,\, N(t)-N(s)\geq 1) + P(N(s)\geq 2) \\
    &= \underbrace{P(N(s)=1)\cdot P(N(t)-N(s)\geq 1)}_{\text{第一种情况}} + \underbrace{P(N(s)\geq 2)}_{\text{第二种情况}} \\
    &= \left[ e^{-\lambda s} \cdot \lambda s \cdot (1 - e^{-\lambda (t-s)}) \right] + \left[ 1 - e^{-\lambda s} - \lambda s e^{-\lambda s} \right] \\
    &= \lambda s e^{-\lambda s} (1 - e^{-\lambda (t-s)}) + 1 - e^{-\lambda s} - \lambda s e^{-\lambda s} \\
    &= 1 - e^{-\lambda s} - \lambda s e^{-\lambda t}
    \end{aligned}
    $$

!!! example "有一大堆灯泡，它们的寿命都服从均值为 30 分钟的指数分布且相互独立。上年 5 点第一个灯泡开始工作，坏掉后马上换上第二个灯泡，再坏掉就马上换上第三个灯泡，...,以此类推。求"
    (1) 到上午 6 点为止共用坏 1 个灯泡，而到上午 9 点为止共用坏 3 个灯泡的概率；
    (2)第 1 个灯泡在上午 6 点到 7 点之间用坏的概率；
    (3)已知到上午 7 点为止共用坏 4 个灯泡，问第二个灯泡在上午 6 点到 7 点之间用坏的概率。

    以 $N(t)$表示到 5点加 t小时为止灯泡坏掉的数目，则$\{N(t);t\geq0\}$是强度为
    2 的泊松过程。

    (1) $P( N_{1}= 1, N_{4}= 3) = P( N_{1}= 1) P( N_{4}- N_{1}= 2) = 36e^{- 8}$

    (2) $P( N_{1}= 0) P( N_{2}- N_{1}\geq 1) = e^{- 2}( 1- e^{- 2})$

    (3) $P( 1< W_{2}< 2\mid N_{2}= 4) = \frac {P( N_{1}= 0, N_{2}= 4) + P( N_{1}= 1, N_{2}= 4) }{P( N_{2}= 4) }= \frac 5{16}$

### 合成与分解题目

!!! example "例题"
    设$\{N_{1}(t);t\geq0\}$和$\{N_{2}(t);t\geq0\}$是相互独立的泊松过程，强度分别为1和2。则$P(N_{1}(1)+N_{2}(1)>0)=$ __________, $P(N_{1}(1)=1|N_{1}(1)+N_{2}(1)=1)=$ __________。

    - $1-e^{-3}$ 
    - $\frac13$

!!! example "相似例题"
    设 $\{N_i(t);\, t \geq 0\},\, i=1,2$ 是两个相互独立、强度均为 $\lambda$ 的泊松过程，则

    $P(N_1(1) + N_2(2) = 2) =$ __________

    $P(N_1(2) = 2\,|\, N_1(1) + N_2(2) = 2) =$  __________

!!! example "例题"
    设 $\{N_i(t);\, t \geq 0\},\, i=1,2$ 是两个相互独立、强度分别为 $1$ 和 $2$ 的泊松过程，求：

    $$
    P\left\{N_1(1) = 1 \mid N_1(2) + N_2(2) = 2\right\} =\; \underline{\hspace{2cm}}
    $$
    
    - (A) $\dfrac{5}{18}$
    - (B) $\dfrac{1}{3}$
    - (C) $\dfrac{5}{9}$
    - (D) $\dfrac{2}{9}$

    ---
    答案选 A，条件可以使用 possion 合成

    再使用分类讨论

!!! example "某银行有两个窗口可以接受服务。上午九点钟，小王到达这个银行，此时两个窗口分别有一个顾客在接受服务，另外有 2 个顾客排在小王的前面等待接受服务，一会儿又来了很多顾客。假设服务的规则是先来先服务。也就是说一旦有一个窗口顾客接受完服务，那么排在队伍中的第一个顾客就马上在此窗口接受服务。假设各个顾客接受服务的时间独立同分布，而且服从均值为 20 分钟的指数分布。"

    ![](https://img.philfan.cn/Math__StochasticProcess__assets__03-Possion.assets__20250526095634.webp)

    ---

    **问：小王在十点钟之前能够接受服务的概率？**

    解：以上午九点钟作为 0 时刻，以 1 小时作为单位时间。对$i=1,2$, 令$N_i(t)$表示$(0,t]$内第$i$个窗口完成服务的顾客数。则$\{N_i(t);t\geq0\}$ 是强度为 3 的泊松过程，且$\{N_1(t)\}$ 和$\{N_2(t)\}$ 相互独立。

    令$N(t)$表示$(0,t]$内这两个窗口完成服务的顾客总数

    则$N(t)=N_1(t)+N_2(t)$，且$\{N(t)\}$ 是强度为 6 的泊松过程

    当且仅当第 3 个顾客服务完成时，小王才去接受服务。

    用$W_i$表示第$i$个顾客服务完成的时刻，所以所求的概率是：

    $$
    \begin{aligned}
    P(W_3\leq1)&=P(N(1)\geq3)\\&=1-e^{-6}-6e^{-6}-18e^{-6}=0.938
    \end{aligned}
    $$


    **2. 在等待的顾客中，排在第一位的顾客平均要等待多长时间才轮到接受服务？**

    $$
    \mathrm{EW}_{1}=\mathrm{ET}_{1}=\frac{1}{6}
    $$

    --- 

    **3. 小王等待接受服务的平均时间是多少？**

    $$
    T_{i}=W_{i}-W_{i-1} \quad i=1,2, \cdots \quad W_{0}=0
    $$

    $$
    \mathrm{EW}_{3}=\mathrm{E}\left(T_{1}+T_{2}+T_{3}\right)=\frac{1}{2}
    $$

    --- 

    **4. 排在第一位的顾客是在第一个窗口服务的概率是多少？**

    记$T_{1}^{k}, k=1,2$表示$\{N_{k}(t), k=1,2\}$第 k 个窗口首个顾客完成的时刻，则$T_{1}^{k}, k=1,2$相互独立，且分别服从参数为$\lambda_{1}、\lambda_{2}$的指数分布。

    $T_{1}=\min\left\{T_{1}^{1}, T_{1}^{2}\right\}$的分布函数为：

    当$x>0$时，$\mathrm{F}_{T_{1}}(x)=1-\left(1-\mathrm{F}_{T_{1}^{1}}(x)\right)\left(1-\mathrm{F}_{T_{1}^{2}}(x)\right)=1-\mathrm{e}^{-\left(\lambda_{1}+\lambda_{2}\right) x}$

    $$
    \therefore \mathrm{ET}_{1}=\frac{1}{\lambda_{1}+\lambda_{2}}
    $$

    (2) $\mathrm{P}\left\{T_{1}^{1}<T_{1}^{2}\right\}=\int_{0}^{+\infty} \mathrm{d} x \int_{x}^{+\infty} \lambda_{1} \mathrm{e}^{-\lambda_{1} x} \times \lambda_{2} \mathrm{e}^{-\lambda_{2} y} \mathrm{~d} y=\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}}$

!!! example "购物"
    以 $N(t)$ 表示 $(0, t]$ 内到达某商场的顾客数，设 $\{N(t); t \geq 0\}$ 是强度为 $\lambda = 5$ 的泊松过程，进商场的各顾客独立地以概率 0.4 购物，以概率 0.6 不购物。计算
    (1) 在 $(0,1]$ 内至少有 1 个顾客到达，且在 $(0,3]$ 内恰有两个顾客到达的概率；
    (2) 若已知在 $(0,3]$ 内恰有 1 个顾客到达，求他到达的时间在 $(1,2)$ 之间的概率；
    (3) 若已知在 $(0,1]$ 内至多有 2 个顾客到达，求至少有 1 个顾客购物的概率

    $N_1(t), N_2(t)$ 分别表示 $(0, t]$ 内购物的顾客数和不购物的顾客数。

    (1) $P\{N(1) = 1, N(3) - N(1) = 1\} + P\{N(1) = 2, N(3) - N(1) = 0\} = 62.5e^{-15} = 1.91 \times 10^{-5}$

    (2) 

    $$
    \begin{align*}
    P(N(1) = 0, N(2) = 1 | N(3) = 1) &= \frac{P(N(1) = 0, N(2) - N(1) = 1, N(3) - N(2) = 0)}{P(N(3) = 1)} \\
    &= \frac{1}{3}
    \end{align*}
    $$

    (3) 

    $$
    \begin{align*}
    P(N_1(1) \geq 1 | N(1) \leq 2) =& P(N_1(1) = 1 | N(1) \leq 2) + P(N_1(1) = 2 | N(1) \leq 2)\\
    =& \frac{20}{37}
    \end{align*}
    $$

!!! example "例题"
    某人在钓鱼，假设他钓到鱼的规律服从强度为 $4$ 条/h 的泊松过程，且每条鱼的质量（单位：kg）独立同分布，服从 $(0,2)$ 上均匀分布。请回答下列问题：

    1. 此人在 $1$h 内钓到 $2$ 条鱼的概率为（ ）
        
        A. $2e^{-4}$  B. $4e^{-4}$  C. $8e^{-4}$  D. $16e^{-4}$

    2. 此人每小时平均能钓到重达 $1.5$kg 以上的鱼几条？（ ）
        
        A. $4$  B. $3$  C. $2$  D. $1$

    3. 此人在第 $1$h 后才钓到重达 $1.5$kg 以上的鱼的概率为（ ）
        
        A. $1-e^{-3}$  B. $1-e^{-1}$  C. $e^{-3}$  D. $e^{-1}$

    4. 若已知此人在 $1$h 内钓到两条鱼，则这两条都是不足 $1$kg 鱼的概率为（ ）
        
        A. $1/2$  B. $1/4$  C. $1/8$  D. $3/4$

    5. 此人先钓到不足 $0.5$kg 鱼的概率为（ ）
        
        A. $1/4$  B. $3/8$  C. $1/2$  D. $1/3$

    ---
    **答案：** C D D B A

!!! note "合成"

    四、涟水高师是一所著名的高等研究院，为我国数学事业发展做出了杰出贡献。其中， Jumpton 爵士早在 1624 年就于涟水高师开始了关于随机过程的研究。一天，Jumpton 爵士在苹果树下召集了Gauss，Euler、RunAutumn、Yau、Riemann 等学生进行数学方面的研讨。在此期间，祂观察到树叶落下与苹果落下的规律分别符合强度为2(个/小时)与3(个/小时)的泊松过程，并以此提出了著名的上帝均衡(Lord Equilibrium)。(15 分)
    (1)第一个小时内掉落物总数符合什么分布。
    (2)已知在 1h 内有四个物品掉落，求其中最多一个是树叶的可能性。
    (3)第一个掉下的物品为苹果的概率。
    (4)求第二个苹果在[1,2]时间范围内落下的概率。

### 非齐次

!!! example "例题"
    设$\{\mathcal{N}(t),t\geq0\}$是强度为$\lambda(t)=2t$的非齐次泊松过程，则$\mathcal{R}_{\mathcal{N}}(1, 2) =$ ( )

    $$
    \begin{aligned}
    \text{(A)}\ 1 \qquad
    \text{(B)}\ 5 \qquad
    \text{(C)}\ 3 \qquad
    \text{(D)}\ 2
    \end{aligned}
    $$

    **选 B。**

    **分析：**

    方法一：  
    非齐次泊松过程的自相关函数为

    这里使用了**拆分 + 独立增量的性质**，是一个常用的技巧（在 brown 中也经常用）

    $$
    \begin{aligned}
    \mathcal{R}_{\mathcal{N}}(1, 2) &= E[\mathcal{N}(1)\mathcal{N}(2)] \\
    &= E[\mathcal{N}(1)^2] + E[\mathcal{N}(1)](E[\mathcal{N}(2)] - E[\mathcal{N}(1)]) \\
    &= \left(\operatorname{Var}[\mathcal{N}(1)] + (E[\mathcal{N}(1)])^2\right) + E[\mathcal{N}(1)]\left(E[\mathcal{N}(2)] - E[\mathcal{N}(1)]\right) \\
    &= (1 + 1^2) + 1 \times (4 - 1) \\
    &= 2 + 3 = 5
    \end{aligned}
    $$

    ---


    但更常用的公式是

    $$
    \mathcal{R}_{\mathcal{N}}(s, t) = E[\mathcal{N}(s)] + E[\mathcal{N}(s)]E[\mathcal{N}(t)]
    $$

    
    其中 $E[\mathcal{N}(t)] = \int_0^t \lambda(u) du$。

    这里 $\lambda(t) = 2t$，所以
    
    $$
    E[\mathcal{N}(1)] = \int_0^1 2t\,dt = [t^2]_0^1 = 1 \\
    E[\mathcal{N}(2)] = \int_0^2 2t\,dt = [t^2]_0^2 = 4
    $$

    所以

    $$
    \mathcal{R}_{\mathcal{N}}(1, 2) = E[\mathcal{N}(1)] + E[\mathcal{N}(1)]E[\mathcal{N}(2)] = 1 + 1 \times 4 = 5
    $$

!!! example "设$\{N(t), t \geq 0\}$是非齐次泊松过程，强度为$\lambda(t) = t^2$"

    计算(1)$E(N(2))$;

    $$
    \begin{aligned}
    E(N(2)) &= \int_{0}^{2} \lambda(t) dt = \int_{0}^{2} t^2 dt = \frac{8}{3}
    \end{aligned}
    $$

    ---

    (2)$P(N(1) = 1, N(2) = 2)$;

    $$
    \begin{aligned} 
    \int_{0}^{1} \lambda(t) dt &= \int_{0}^{1} t^2 dt = \frac{1}{3}\\
    \int_{1}^{2} \lambda(t) dt &= \frac{8}{3} - \frac{1}{3} = \frac{7}{3}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    P(N(1) = 1, N(2) = 2) &= P(N(1) = 1)P(N(2) - N(1) = 1)\\
    &= (\frac{1}{3} e^{-1/3})(\frac{7}{3} e^{-7/3}) = \frac{7}{9} e^{-8/3}
    \end{aligned}
    $$

    ---

    (3)$P(N(2) = 2 | N(1) = 1)$;


    $$
    \begin{aligned}
    P(N(2) = 2 | N(1) = 1) &= P(N(2) - N(1) = 1) \\
    &= \frac{7}{3} e^{-7/3}
    \end{aligned}
    $$

    ---

    (4)$P(N(1) = 1 | N(2) = 2)$.

    $$
    \begin{aligned}
    P(N(1) = 1 | N(2) = 2) &= \frac{P(N(1) = 1, N(2) = 2)}{P(N(2) = 2)} \\
    &= \frac{\frac{7}{9} e^{-8/3}}{(\frac{8}{3})^2 e^{-8/3} / 2} = \frac{7}{32}
    \end{aligned}
    $$

## 习题

### 4.2 - 独立增量

!!! example "设 $\{X(t);t\geqslant0\}$ 是正态过程$,\mu_X(t)=1,C_X(s,t)=2\min\{s,t\}.$"

    (1)对$t>s\geqslant0$,求$X(t)-X(s)$的分布； 
    (2)问$\{X(t);t\geqslant0\}$是平稳增量过程吗？ 
    (3)问$\{X(t);t\geqslant0\}$是独立增量过程吗？

    我们来逐问分析：



    ${X(t); t \geq 0}$ 是一个**正态过程**，即任意有限维随机变量 $(X(t_1), X(t_2), ..., X(t_n))$ 服从多元正态分布。
    给出：

    * 均值函数：$\mu_X(t) = 1$
    * 协方差函数：$C_X(s, t) = 2 \min{s, t}$

    这相当于是一个带常数漂移项的布朗运动的缩放版本。

    ---

    **(1) 对 $t > s \geq 0$，求 $X(t) - X(s)$ 的分布**

    由于是正态过程，差值 $X(t) - X(s)$ 也服从正态分布，其分布完全由均值和方差决定：

    均值：

    $$
    \mathbb{E}[X(t) - X(s)] = \mathbb{E}[X(t)] - \mathbb{E}[X(s)] = 1 - 1 = 0
    $$

    方差：

    $$
    \begin{aligned}
    \mathrm{Var}[X(t) - X(s)] &= \mathrm{Var}[X(t)] + \mathrm{Var}[X(s)] - 2\mathrm{Cov}[X(t), X(s)] \\
    &= C_X(t,t) + C_X(s,s) - 2C_X(s,t) \\
    &= 2t + 2s - 2 \cdot 2 \cdot \min\{s, t\} \\
    &= 2t + 2s - 4s \quad (\text{因为 } s < t) \\
    &= 2(t - s)
    \end{aligned}
    $$

    所以，

    $$
    X(t) - X(s) \sim \mathcal{N}(0, 2(t - s))
    $$

    ---

    **(2) 过程 $\{X(t)\}$ 是平稳增量过程吗？**

    一个过程有**平稳增量**，如果对于任意 $h > 0$，增量 $X(t+h) - X(t)$ 的分布与 $X(s+h) - X(s)$ 相同，且与 $t$ 无关，仅与 $h$ 有关。

    我们来检查：

    * 对于 $t > s$，我们已经有：

    $$
    X(t) - X(s) \sim \mathcal{N}(0, 2(t-s))
    $$
    * 所以增量的分布只取决于差值 $t - s$

    **结论**：是的，增量分布只依赖于时间间隔长度，**过程 $\{X(t)\}$ 是平稳增量过程**。

    ---

    **(3) 过程 $\{X(t)\}$ 是独立增量过程吗？**


    独立增量过程：任意不重叠时间段的增量是相互独立的。即，对任意 $0 \leq t_1 < t_2 < \dots < t_n$，增量：

    $$
    X(t_2) - X(t_1),\ X(t_3) - X(t_2),\ \dots,\ X(t_n) - X(t_{n-1})
    $$

    相互独立。

    来检查是否满足独立性。我们取 $0 < s < t$，考察 $X(s)$ 和 $X(t) - X(s)$ 是否独立。

    我们看它们的协方差：

    $$
    \begin{aligned}
    \mathrm{Cov}(X(t) - X(s), X(s)) &= \mathrm{Cov}(X(t), X(s)) - \mathrm{Cov}(X(s), X(s)) \\
    &= C_X(s,t) - C_X(s,s) = 2s - 2s = 0
    \end{aligned}
    $$

    由于是正态过程，**零协方差 ⇒ 独立**，所以两个正态变量线性无关就独立。因此两个增量是独立的。

    进一步，任意不重叠时间段的增量由线性组合得出，都相互独立。

    **结论**：是的，**过程 $\{X(t)\}$ 是独立增量过程**。

    ✅ 总结：

    1. $X(t) - X(s) \sim \mathcal{N}(0, 2(t - s))$
    2. 是平稳增量过程 ✅
    3. 是独立增量过程 ✅

### 4.3 - 泊松过程计算

!!! example "设 $\{N(t);t\geqslant0\}$ 是强度为 $\lambda$ 的泊松过程，求"

    (1) $P(N(3)-N(1)\geqslant2)$;

    (2) $P(N(3)\geqslant2\mid N(1)=1)$;

    (3) $P(N(1)=1\mid N(3)\geqslant2).$


    ---

    (1) $P(N(3) - N(1) \geq 2)$

    $$
    \begin{aligned}
    N(3) - N(1) &\sim \text{Poisson}(2\lambda) \\
    P(N(3) - N(1) \geq 2) &= 1 - P(0) - P(1) \\
    &= 1 - e^{-2\lambda} - (2\lambda)e^{-2\lambda} \\
    &= 1 - e^{-2\lambda}(1 + 2\lambda)
    \end{aligned}
    $$

    ---

    (2) $P(N(3) \geq 2 \mid N(1) = 1)$

    $$
    \begin{aligned}
    P(N(3) \geq 2 \mid N(1) = 1) &= P(N(3) - N(1) \geq 1 \mid N(1) = 1) \\
    &= P(N(3) - N(1) \geq 1) \quad (\text{独立增量}) \\
    &= 1 - P(N(3) - N(1) = 0) \\
    &= 1 - e^{-2\lambda}
    \end{aligned}
    $$

    ---

    (3) $P(N(1) = 1 \mid N(3) \geq 2)$

    $$
    \begin{aligned}
    &P(N(1) = 1 \mid N(3) \geq 2) \\
    &= \frac{P(N(1) = 1,\, N(3) \geq 2)}{P(N(3) \geq 2)} \\
    &= \frac{P(N(1) = 1) \cdot P(N(3) - N(1) \geq 1)}{P(N(3) \geq 2)} \qquad \text{（独立增量，贝叶斯公式）} \\
    &= \frac{[e^{-\lambda} \lambda] \cdot [1 - e^{-2\lambda}]}{1 - e^{-3\lambda}(1 + 3\lambda)}
    \end{aligned}
    $$

### 4.11 - 泊松过程计算

!!! example "设电话总机在 $(0,t]$ (单位：min) 内接到的呼叫数为 $N(t),\{N(t)\}$ 是强度为 $\lambda$ 的泊松过程。求："

    (1)2分钟到3次呼叫的概率；

    (2)第2分内接到第3次呼叫的概率.

    --- 
    **(1) 2 分钟内接到 3 次呼叫的概率**

    设泊松过程的强度为 $\lambda$，则：

    * 呼叫数在时间 $t$ 内满足：

    $$
    N(t) \sim \text{Poisson}(\lambda t)
    $$

    * 所以在 2 分钟内：

    $$
    N(2) \sim \text{Poisson}(2\lambda)
    $$

    我们要求的是：

    $$
    P(N(2) = 3) = \frac{(2\lambda)^3}{3!} e^{-2\lambda} = \frac{4\lambda^3}{3} e^{-2\lambda}
    $$

    ---

    **(2) 第 2 分钟内接到第 3 次呼叫的概率**

    即：

    $$
    P(1 \leq W_3 \leq 2)
    $$

    其中 $W_3$ 是第 3 次呼叫到达的时刻，满足：$W_3 \sim \Gamma(3, \lambda)$（即 Erlang 分布）

    伽马分布累积分布函数为：

    $$
    F_{W_3}(x) = 1 - e^{-\lambda x} \left(1 + \lambda x + \frac{(\lambda x)^2}{2} \right)
    $$

    所以：

    $$
    \begin{aligned}
    P(1 \leq W_3 \leq 2) &= F_{W_3}(2) - F_{W_3}(1) \\
    &= \left[1 - e^{-2\lambda} \left(1 + 2\lambda + 2\lambda^2\right)\right] - \left[1 - e^{-\lambda} \left(1 + \lambda + \tfrac{1}{2}\lambda^2\right)\right] \\
    &= e^{-\lambda} \left(1 + \lambda + \tfrac{1}{2}\lambda^2 \right) - e^{-2\lambda} \left(1 + 2\lambda + 2\lambda^2 \right)
    \end{aligned}
    $$

    ---

    也可以把问题转化为

    $$
    \begin{aligned}
    P(1 \leq W_3 \leq 2)&= P\{N(1)\leqslant2,N(2)\geqslant3\} \\
    &= P\{N(1)=0,N(2)-N(1)\geqslant3\} + P\{N(1)=1,N(2)-N(1)\geqslant2\} + P\{N(1)=2,N(2)-N(1)\geqslant1\} \\
    &= (1+\lambda+\frac{1}{2}\lambda^2)e^{-\lambda}-(1+2\lambda+2\lambda^2)e^{-2\lambda}
    \end{aligned}
    $$

### 4.10 - 相关分布

!!! example "设 $\{N(t)\}$ 是强度为 $\lambda$ 的泊松过程，$0 \leqslant s < t, k \leqslant n$, 其中 $W_k$ 表示第 $k$ 个事件发生的时刻，求"

    (1) $P(N(s)=k \mid N(t)=n)$

    $$
    \begin{aligned}
    &\text{已知泊松过程在 } [0,t] \text{ 内有 } n \text{ 个事件，} \\
    &\text{则这些事件在区间 } [0,t] \text{ 上服从均匀分布} \\
    &\Rightarrow N(s) \mid N(t) = n \sim \text{Binomial}(n, \tfrac{s}{t}) \\
    &\Rightarrow P(N(s)=k \mid N(t)=n) = \binom{n}{k} \left( \frac{s}{t} \right)^k \left( 1 - \frac{s}{t} \right)^{n-k}
    \end{aligned}
    $$

    ---

    (2) $P(W_2 \leq 3 \mid W_1 = 1)$

    $$
    \begin{aligned}
    &W_2 = W_1 + \text{下一次事件间隔} \sim W_1 + \text{Exp}(\lambda) \\
    &\Rightarrow W_2 \leq 3 \iff \text{Exp}(\lambda) \leq 2 \\
    &\Rightarrow P(W_2 \leq 3 \mid W_1 = 1) = P(\text{Exp}(\lambda) \leq 2) = 1 - e^{-2\lambda}
    \end{aligned}
    $$

    ---

    (3) $P(W_k \leq s \mid N(t) = n)$


    $$
    P(W_k \leq s \mid N(t)=n) = \sum_{i=k}^{n} \binom{n}{i} \left( \frac{s}{t} \right)^i \left( 1 - \frac{s}{t} \right)^{n-i}
    $$



    这表示：在 $n$ 个事件中，至少有 $k$ 个落在 $[0, s]$ 区间的概率。每个事件独立落在 $[0,t]$ 上，概率为 $\frac{s}{t}$。

### 4.14 - 合成与分解 - 应用题

!!! example "某人有两个邮箱，A 邮箱和 B 邮箱。用 $N_1(t)$ 和 $N_2(t)$ 分别表示 $(0,t]$ 内这两个邮箱收到的邮件数目。设 $\{N_1(t); t \geqslant 0\}$ 和 $\{N_2(t); t \geqslant 0\}$ 是相互独立的泊松过程，强度分别为 2 和 3, 且每封邮件独立地以概率 0.1 为垃圾邮件。计算："

    (1) 在 $(0,1]$ 内 A 邮箱没有收到邮件、B 邮箱收到 1 封邮件的概率;

    (2) 在 $(0,1]$ 内共收到 2 封邮件的概率;

    (3) 在 $(0,2]$ 内此人收到 1 封垃圾邮件、2 封有用邮件的概率;

    (4) 第 2 封垃圾邮件在 $(1,2]$ 内收到的概率.

    解：


    ---

    已知条件：

    * $N_1(t) \sim \text{Poisson}(2t)$，A 邮箱的邮件数；
    * $N_2(t) \sim \text{Poisson}(3t)$，B 邮箱的邮件数；
    * 两个过程独立；
    * 每封邮件独立地以概率 $p = 0.1$ 是垃圾邮件。

    ---

    ✅ **(1) 在 $(0,1]$ 内 A 邮箱没有收到邮件、B 邮箱收到 1 封邮件的概率：**

    $$
    P(N_1(1) = 0,\, N_2(1) = 1) = e^{-2} \cdot 3e^{-3} = 3e^{-5}
    $$

    --- 

    ✅ **(2) 在 $(0,1]$ 内共收到 2 封邮件的概率：**

    由于两个过程独立相加，总邮件数也是泊松过程，强度为 $2+3=5$，即：

    $$
    N(1) = N_1(1) + N_2(1) \sim \text{Poisson}(5)
    $$

    $$
    P(N(1)=2) = \frac{5^2}{2!} e^{-5} = \frac{25}{2} e^{-5}
    $$

    ---

    ✅ **(3) 在 $(0,2]$ 内此人收到 1 封垃圾邮件、2 封有用邮件的概率：**

    总邮件数为泊松过程，强度为 $5$，则：

    $$
    N(2) \sim \text{Poisson}(10)
    $$

    我们要计算：

    * 共收到 3 封邮件（1 垃圾 + 2 有用）；
    * 垃圾邮件服从二项分布：$\text{Binomial}(3, 0.1)$

    $$
    \begin{aligned}
    P(\text{2 内收到 1 封垃圾、2 封有用邮件})
    &= P(N(2) = 3) \cdot P(\text{3 封中恰 1 封为垃圾}) \\
    &= \underbrace{P(N(2) = 3)}_{\text{总邮件数}} \times \underbrace{P(\text{Binomial}(3,\,0.1) = 1)}_{\text{垃圾邮件分布}} \\
    &= \left[ \frac{10^3}{3!} e^{-10} \right] \cdot \left[ \binom{3}{1} (0.1)^1 (0.9)^2 \right] \\
    &= \frac{1000}{6} e^{-10} \cdot 3 \cdot 0.1 \cdot 0.81 \\
    &= \frac{1000}{6} e^{-10} \cdot 0.243 \\
    &= \frac{243000}{6000} e^{-10} \\
    &= 40.5\, e^{-10}
    \end{aligned}
    $$

    ---

    ✅ **(3) 在第 2 分钟内接到第 3 次呼叫的概率**

    设电话呼叫过程为强度 $\lambda$ 的泊松过程 $\{N(t)\}$，设 $W_3$ 表示**第 3 次呼叫的到达时间**，则：

    $$
    W_3 \sim \text{Gamma}(3, \lambda)
    $$

    我们要求：

    $$
    P(1 \leq W_3 \leq 2) = F_{W_3}(2) - F_{W_3}(1)
    $$

    伽马分布的累积分布函数为：

    $$
    F_{W_3}(x) = 1 - e^{-\lambda x} \left(1 + \lambda x + \frac{(\lambda x)^2}{2} \right)
    $$

    所以：

    $$
    \begin{aligned}
    P(1 \leq W_3 \leq 2) &= F_{W_3}(2) - F_{W_3}(1) \\
    &= \left[1 - e^{-2\lambda} \left(1 + 2\lambda + 2\lambda^2\right)\right] - \left[1 - e^{-\lambda} \left(1 + \lambda + \tfrac{1}{2}\lambda^2\right)\right] \\
    &= e^{-\lambda} \left(1 + \lambda + \tfrac{1}{2} \lambda^2 \right) - e^{-2\lambda} \left(1 + 2\lambda + 2\lambda^2 \right)
    \end{aligned}
    $$

    ---

    ✅ **等价表示（使用泊松过程性质）：**

    考虑事件：

    $$
    P(1 \leq W_3 \leq 2) = P\{N(1)\leqslant 2, N(2)\geqslant 3\}
    $$

    分解为三种情形：

    $$
    \begin{aligned}
    P(1 \leq W_3 \leq 2) 
    &= P\{N(1)\leqslant 2,\, N(2)\geqslant 3\} \\
    &= \color{red}{P\{N(1)=0,\, N(2)-N(1)\geq 3\}} + \color{green}{P\{N(1)=1,\, N(2)-N(1)\geq 2\}} + \color{blue}{P\{N(1)=2,\, N(2)-N(1)\geq 1\}} \\
    &= \color{red}{P(N(1)=0)\cdot P(N(1,2]\geq 3)} + \color{green}{P(N(1)=1)\cdot P(N(1,2]\geq 2)} + \color{blue}{P(N(1)=2)\cdot P(N(1,2]\geq 1)} \\
    &= \color{red}{e^{-\lambda} \left[1 - (1+\lambda+\tfrac{1}{2}\lambda^2)e^{-\lambda}\right]} + \color{green}{\lambda e^{-\lambda} \left[1 - (1+\lambda)e^{-\lambda}\right]} + \color{blue}{\tfrac{1}{2}\lambda^2 e^{-\lambda} (1 - e^{-\lambda})} \\
    &= e^{-\lambda} \left(1 + \lambda + \tfrac{1}{2}\lambda^2\right) - e^{-2\lambda} \left(1 + 2\lambda + 2\lambda^2\right)
    \end{aligned}
    $$

### 4.17 - 合成与分解 - 应用题

!!! example "某人在钓鱼，他只可能钓到鲫鱼或鳙鱼。他钓到鲫鱼的规律服从强度为 2 条/h 的泊松过程，钓到鳙鱼的规律服从强度为 1 条/h 的泊松过程，且这两个过程相互独立。假设每条鱼的质量（单位：kg）独立同分布，且服从 $\mathcal{U}(0, 2)$ 上均匀分布。"

    - (1) 计算此人在 1h 内钓到 2 条鱼的概率；
    - (2) 计算此人在 1h 内钓到 4 条鱼，其中 2 条不足 1kg 的概率；
    - (3) 计算此人在第 1h 内和第 2h 内各钓到 1 条鱼，且都重达 1kg 以上鲫鱼的概率；
    - (4) 若已知此人在 2h 内各钓到两条鱼，求这两条都是重达 1kg 以上鲫鱼的概率。


    翻译一下题目

| 鱼类 | 不足 1kg | 重达 1kg | 总条数 |
| -------- | ------------------------- | ------------------------- | ------------------ |
| 鲫鱼 | $N_{11}(t)_{\lambda=1}$ | $N_{12}(t)_{\lambda=1}$ | $N_1(t)_{\lambda=2}$ |
| 鳊鱼 | $N_{21}(t)_{\lambda=0.5}$ | $N_{22}(t)_{\lambda=0.5}$ | $N_2(t)_{\lambda=1}$ |
| 总条数 | $N_1^*(t)_{\lambda=1.5}$ | $N_2^*(t)_{\lambda=1.5}$ | $N(t)_{\lambda=3}$ |

    **(1) 计算此人在 1h 内钓到 2 条鱼的概率：**

    $$
    P\{N(1) = 2\} = \frac{9}{2} e^{-3}
    $$

    **(2) 计算此人在 1h 内钓到 4 条鱼，其中 2 条不足 1kg 的概率：**

    $$
    \begin{align*}
    P\{N(1) = 4,\, N_1^*(1) = 2\} 
    &= P\{N_1^*(1) = 2,\, N_2^*(1) = 2\} \\
    &= \left[\frac{9}{8} e^{-3/2}\right] \times \left[\frac{9}{8} e^{-3/2}\right] \\
    &= \frac{81}{64} e^{-3}
    \end{align*}
    $$

    **(3) 计算此人在第 1h 内和第 2h 内各钓到 1 条鱼，且都重达 1kg 以上鲫鱼的概率：**

    $$
    \begin{align*}
    &P\{N(1)=N(2)-N(1)=1,\, N_{12}(1)=N_{12}(2)-N_{12}(1)=1\} \\
    &= P\{N_1^*(1)=0,\, N_1^*(2)-N_1^*(1)=0,\, N_{22}(1)=0,\, N_{22}(2)-N_{22}(1)=0,\, N_{12}(1)=1,\, N_{12}(2)-N_{12}(1)=1\} \\
    &= e^{-\frac{3}{2}} \times e^{-\frac{3}{2}} \times e^{-\frac{1}{2}} \times e^{-\frac{1}{2}} \times e^{-1} \times e^{-1} \\
    &= e^{-6}
    \end{align*}
    $$

    或者

    $$
    \begin{align*}
    &P\{N(1)=N(2)-N(1)=1,\, N_{12}(1)=N_{12}(2)-N_{12}(1)=1\} \\
    &= P\{N(1)-N_{12}(1)=0,\, (N(2)-N(1))-(N_{12}(2)-N_{12}(1))=0,\, N_{12}(1)=1,\, N_{12}(2)-N_{12}(1)=1\} \\
    &= e^{-2} \times e^{-2} \times e^{-1} \times e^{-1} \\
    &= e^{-6}
    \end{align*}
    $$

    **(4) 若已知此人在 2h 内各钓到两条鱼，求这两条都是重达 1kg 以上鲫鱼的概率：**

    由泊松过程的性质，有

    $$
    \begin{align*}
    P\{N_{12}(2)=2\,|\,N(2)=2\}
    &= \frac{P\{N(2)-N_{12}(2)=0,\, N_{12}(2)=2\}}{P\{N(2)=2\}} \\
    &= \frac{e^{-4} \times 2e^{-2}}{18e^{-6}} \\
    &= \frac{1}{9}
    \end{align*}
    $$

    还有一种理解方法

    $$
    \begin{align*}
    P\{N_{12}(2)=2\,|\,N(2)=2\} 
    &= \frac{P\{N_{2}(2) =0, N_{12}(2)=2\,N_{11}(2) = 0\}}{P\{N(2)=2\}} \\
    &= \frac{e^{-2} \times 2e^{-2} \times e^{-2}}{18e^{-6}} \\
    &= \frac{1}{9}
    \end{align*}
    $$

### 4.18 - 非齐次

!!! example "设 $\{N(t); t \geqslant 0\}$ 是强度为 $\lambda(t) = t$ 的非齐次泊松过程，求："

    (1) $P(N(2) = 3)$

    $$N(t) - N(s) \sim \pi(\int_s^t \lambda(h) \mathrm{d}h)$$


    $$
    P(N(2) = 3) = \frac{2^3 e^{-2}}{3!} = \frac{4}{3} e^{-2}
    $$

    --- 

    (2)$P(N(1) = 2, N(2) = 4)$

    $$
    \begin{aligned}
    P(N(1) = 2, N(2) = 4) &= P(N(1) = 2) P(N(2) = 4 | N(1) = 2) \\
    &=P(N(1) = 2)P(N(2)-N(1) = 2)\\
    &= \frac{(1/2)^2 e^{-1/2}}{2!} \cdot \frac{(3/2)^2 e^{-3/2}}{2!} \\
    &= \frac{9}{64} e^{-2}
    \end{aligned}
    $$

    --- 

    (3)$P(N(1) = 2 | N(2) = 4)$

    $$
    \begin{align*}
    P(N(1) = 2 | N(2) = 4) &= \frac{P(N(1) = 2, N(2) = 4)}{P(N(2) = 4)}\quad \text{previous question}\\
    &=\frac{\frac{9}{64}e^2}{\frac{2^4}{4!}e^{2}}= \frac{27}{128}
    \end{align*}
    $$
