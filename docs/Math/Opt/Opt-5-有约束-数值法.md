# 05 | 有约束 数值解法

## 可行方向 —— Zoutendijk 可行方向法

$$
\begin{array}{l}
\nabla f\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p}<0 \\
-\nabla g_{j}\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p}<0, \quad j \in J\left(\boldsymbol{x}^{(k)}\right)
\end{array}
$$

$$
\begin{align}
\min \eta \\
s.t.
\left\{
 \begin{array}{lr}  
    \nabla f\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p} \leq \eta \\
    -\nabla g_{j}\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p} \leq \eta, \quad j \in J\left(\boldsymbol{x}^{(k)}\right)\\
    -1 \le p \le 1
 \end{array}
\right.
\end{align}
$$

- $\eta<0$：可行下降方向
- $\eta=0$：迭代结束！
- $\eta>0$：不会出现

## 制约函数

- 外点：启动点要求低，收敛满
- 内点：启动点要求高，收敛快

### 外点法 —— 罚函数，罚外点

**思想：构造罚函数，惩罚可行域外的迭代点**

#### 罚函数

=== "加性罚函数"

    $$
    \begin{align*}
    L(x) = \begin{cases}
    f(x) & x \in \mathbb{F} \\
    f(x) + Mp(x) & x \notin \mathbb{F} \quad p(x) >0
    \end{cases}
    \end{align*}
    $$

=== "乘性罚函数"

    $$
    \begin{align*}
    L(x) = \begin{cases}
    f(x) & x \in \mathbb{F} \\
    f(x)\cdot p(x) & x \notin \mathbb{F} \quad p(x) >1
    \end{cases}
    \end{align*}
    $$

$x \in \mathbb{F} \in \mathbb{S} \in \mathbb{R}^n$

- $\mathbb{F}$: feasible region
- $\mathbb{S}$: search region
- $M>0$ 为罚因子，当$M$趋向无穷时，$x^{*}$为原问题约束极值解。

#### 罚函数设计

$$
\begin{align*}
\min P(x,M)=f(x)+M\sum_{i=1}^{m}h_{i}^{2}(x)+M\sum_{j=1}^{l}[\min (0,g_{j}(x))]^{2}
\end{align*}
$$

Courant 罚函数

- **等式约束**：$h_i^2(x)=0$是罚函数，因为在可行域内$h(x)=0$，可行域外$h(x)\ne 0$
- **不等式约束**：$[\min (0,g_{j}(x))]^{2}$是罚函数，因为在可行域内$g(x)\ge 0$，$\min (0,g_{j}(x))=0$，可行域外$g(x)<0$ ，$\min (0,g_{j}(x))=g_{j}(x)$，所以相当于用一个二次函数来拟合。

!!! attention "这里要关注不等式的方向，方向不同，罚函数的形式也不同"

#### 外点法收敛性分析

$$
\nabla f(X^{*})-\sum_{i=1}^{m}\gamma_{i}^{*}\nabla h_{i}(X^{*})-\sum_{g_{j}(X^{*})=0}\mu_{j}^{*}\nabla g_{j}(X^{*})=0
$$

罚函数

$$
P(x, M_k) = f(x) + M_k \sum_{i=1}^{m} h_i^2(x) + M_k \sum_{j=1}^{l} [\min(0, g_j(x))]^2
$$

第 k 步罚函数的局部极小值满足

$$
\begin{align*}
\nabla P(x^{(k)}, M_k) &= \nabla f(x^{(k)}) + 2 M_k \sum_{i=1}^{m} h_i(x^{(k)}) \nabla h_i(x^{(k)}) + 2 M_k \sum_{g_j(x^{(k)}) \leq 0} g_j(x^{(k)}) \nabla g_j(x^{(k)}) = 0\\
\nabla P(x^{(k)}, M_k) &= \nabla f(x^{(k)}) - \sum_{i=1}^{m} {\color{red}{\lambda_i(k)}} \nabla h_i(x^{(k)}) - \sum_{g_j(x^{(k)}) \leq 0} {\color{green}{\mu_j(x^{(k)})}}  \nabla g_j(x^{(k)}) = 0\\
&where\quad \color{red}{\lambda_i(k) = -2 M_k h_i(x^{(k)})} \quad \color{green}{\mu_j(k) = -2 M_k g_j(x^{(k)}) \geq 0}
\end{align*}
$$

$x^{(k)}$迭代收敛时

$$
\nabla P(x^*, M) = \nabla f(x^*) - \sum_{i=1}^{m} \lambda_i^* \nabla h_i(x^*) - \sum_{g_j(x^*) \rightarrow 0} \mu_j^* \nabla g_j(x^*) = 0
$$

KKT 条件！

如果$x^{(k)}$是 min$P(x, M_k)$的全局极小值，则外点法收敛到全局最优解！

!!! example "罚函数示例"

    最小化函数 $f(x) = -\frac{1}{3}(x_1+1)^3 + x_2$，满足以下条件：

    $$
    \begin{aligned}
    x_1 - 1 &\geq 0 \\
    x_2 &\geq 0
    \end{aligned}
    $$

    其中，$\nabla f(x) = \left[-\frac{(x_1+1)^2}{3}, 1\right]$​。

    构造罚函数:

    $$
    P(x, M)=\frac{1}{3}(x_{1}+1)^{3}+x_{2}+M[\min (0, x_{1}-1)]^{2}+M[\min (0, x_{2})]^{2}
    $$

    根据一阶驻点条件, 有

    $$
    \begin{align*}
    \frac{\partial P}{\partial x_{1}} & =(x_{1}+1)^{2}+2 M[\min (0, x_{1}-1)]=0 \\
    \frac{\partial P}{\partial x_{2}} & =1+2 M[\min (0, x_{2})]=0
    \end{align*}
    $$

    如果$x_{1} \geq 1 \Rightarrow x_{1}=1$ ，矛盾

    如果$x_{2} \geq 0 \Rightarrow 1=0$ ，不成立

    所以考虑$x_{1}<1, x_{2}<0$区域的驻点。(可行域外的点)

    $$
    \begin{align*}
    \frac{\partial P}{\partial x_{1}}  =(x_{1}+1)^{2}+2 M(x_{1}-1)=0 \\
    \frac{\partial P}{\partial x_{2}}  =1+2 M x_{2}=0
    \end{align*}
    $$

    可得:

    $$
    \begin{align*}
    & x_{1}^{*}=-1-M \pm \sqrt{M^{2}+4 M}\\
    & x_{2}^{*}=-\frac{1}{2 M} \\
    &\quad M \rightarrow+\infty \\
    & \nabla^{2} P(x)=\left[\begin{array}{cc}
    2\left(x_{1}+1\right)+2 M & 0 \\
    0 & 2 M
    \end{array}\right]>0 \\
    & 故为极小值
    \end{align*}
    $$

### 内点法 —— 障碍函数，阻止内点离开

**构造障碍函数，阻止迭代点离开可行域。**

#### 障碍函数

$$
\phi(x) = \begin{cases}
0 & x \in int(\mathbb{F}) \\
\infty & x \rightarrow \partial \mathbb{F} \\
\end{cases}
$$

- $int(\mathbb{F})$：可行域的内部
- $\partial \mathbb{F}$：可行域的边界

#### 如何构建

$$
p(x, r)=r \sum_{j=1}^{l} \frac{1}{g_{j}(x)}
$$

$$
p(x, r)=\sum_{j=1}^{l} \log g_{j}(x)
$$

$$
p(x,r) = \sum_{j=1}^{l} exp\left[\frac{1}{g_{j}(x)}\right]
$$

统一：

$$
\min_{x\in R_0} \quad f(x) + M_1\sum_{i=1}^{m}|h_{i}(x)|^2+M_2\sum_{j=1}^{l}\frac{1}{g_{j}(x)}\log g_{j}(x)
$$

其中 $R_{0}=\left\{x \mid g_{j}(x) > 0, j=1,2, \cdots, l\right\}$ 严格内点

$r>0$ 为障碍因子，其在迭代中的取值会不断减小，趋向于 0，使$x$​可趋向于边界。

!!! example "障碍函数示例"

    最小化函数 $f(x) = x_1 + x_2$，满足以下条件：

    $$
    \begin{aligned}
    -x_1^2 + x_2 &\geq 0 \\
    x_1 &\geq 0
    \end{aligned}
    $$



    构造障碍函数:

    $$
    \begin{align}
    \bar{P}(x, r)=x_{1}+x_{2}-r \cdot\left[\log \left(-x_{1}^{2}+x_{2}\right)+\log \left(x_{1}\right)\right]
    \end{align}
    $$

    根据驻点一阶条件, 有

    $$
    \begin{array}{l}
    \frac{\partial \bar{P}}{\partial x_{1}}=1-r \cdot \frac{-2 x_{1}}{-x_{1}^{2}+x_{2}} \cdot r \cdot \frac{1}{x_{1}}=0 \\
    \frac{\partial \bar{P}}{\partial x_{2}}=1-r \cdot \frac{1}{-x_{1}^{2}+x_{2}}=0
    \end{array}
    \text { 求解得到: }
    $$

    $$
    \begin{array}{l}
    x_{1}=\frac{\sqrt{1+8 r}-1}{4} \\
    x_{2}=\frac{3}{2} r-\frac{\sqrt{1+8 r}-1}{8}
    \end{array}
    $$

    $r \rightarrow 0$ 时, 有

    $$
    \left\{\begin{array}{l}
    x_{1}^{*}=0 \\
    x_{2}^{*}=0
    \end{array}\right.
    $$

#### 收敛性分析

障碍函数

$$
\bar{P}(x, r)=f(x)-r_k \sum_{j=1}^{l} \log g_{j}(x)
$$

第 k 步障碍函数局部极小值满足

$$
\begin{align*}
\nabla \bar{P}\left(x^{(k)}, r_k\right)  =\nabla f\left(x^{(k)}\right)-r_k \sum_{j=1}^{l} \frac{1}{g_{j}\left(x^{(k)}\right)} \nabla g_{j}\left(x^{(k)}\right)=0 \\
\nabla P\left(x^{(k)}, r_k\right)  =\nabla f\left(x^{(k)}\right)-\sum_{j=1}^{l} \mu_{j}\left(k\right) \nabla g_{j}\left(x^{(k)}\right)=0 \\
\mu_{j}(k)=\frac{r}{g_{j}\left(x^{(k)}\right)} \geq 0
\end{align*}
$$

$x_{k}^{*}$迭代收敛时

$$
\begin{align*}
 \nabla P\left(x^{*}, r\right)=\nabla f\left(x^{*}\right)-\sum_{j=1}^{l} \mu_{j}^{*} \nabla g_{j}\left(x^{*}\right)=0 \\
 \mu_{j}^{*}=\frac{r}{g_{j}\left(x^{*}\right)} \geq 0 \\
 \mu_{j}^{*} g_{j}\left(x^{*}\right)=r \rightarrow 0
\end{align*}
$$

**KKT 条件！**

**如果$x(k)$是$\min \bar{P}(x ; r)$的全局极小值，则内点法收敛到全局最优解！**

### 混合法

- 内点法不能处理等式约束问题
- 外点法不能处理目标函数在可行域外不存在的问题
- 对等式约束和当前不被满足的不等式约束，使用罚函数法，对满足的不等式约束，使用障碍函数法。
