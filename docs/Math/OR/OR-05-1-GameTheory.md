# 博弈论 | GameTheory

## 分类

- 局中人是否允许合作：非合作博弈、合作博弈
- 策略的数目：有限策略博弈 - 无限策略博弈
- 策略选择是否具有概率随机性：纯策略博弈、混合策略博弈
- 策略与时间的关系：静态博弈、动态博弈
- 参与人对问题信息结构的了解程度：完全信息博弈、不完全信息博弈
- 数学模型：矩阵博弈、连续博弈、微分博弈、阵地博弈、凸博弈、随机博弈

## 问题与基本概念

局中人 (Players)

**策略集（Strategies）**: 完整性、多样性、不可观察性

赢得函数/支付函数 (Payoff function)

信息 (infomation)

action:variable

**outcome**
**equilibrium**:均衡，所有参与者最优策略组合
**rules**:players,action&outcome

- 矩阵博弈：研究有限零和博弈的最优策略。
- 理性博弈原则：决策主体追求自身利益最大化。
- 最优策略对极大极小值和极小极大值：通过求解极大极小值和极小极大值来找到最优策略。
- 纳什均衡解的意义：研究解的可能性，包括单个解、多个解或无纯策略解等情况

在众多对策模型中，占有重要地位的是二人有限零和对策，即在对策只有两个局中人，各自的策略集只含有限个策略，每局中两个局中人的得失总和为零（即一个局中人的赢得恰为另一个局中人所输掉的值），这类对策又称为`矩阵对策`。

## 矩阵——纯策略博弈

博弈模型 $G=\{I, II, S_1, S_2, A\}$

- 局中人 $I、II$
- 策略集
  $S_1=\{a_1, a_2, \cdots, a_m\}$
  $S_2=\{b_1, b_2, \cdots, b_n\}$
- 局中人 $I$ 的赢得矩阵：$A$

$$
A=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]
$$

- 局中人 $II$ 的赢得矩阵：$-A^T$

### 共许原则

双方均无改变策略的意愿

### 自身利益最大化原则

!!! note "自身的赢得值尽可能大"

- 问题：不确定对方决策情况下的最优决策
- 准则：从最坏的预期中选则最好的（悲观准则）一种保守而贪心的准则
  “做最坏的打算，争取最好的结果”

> 局中人 $I$​ 最大预期赢得（赢得指自身最小收益）
>
> 极大极小值：$\max \limits_{i} \min \limits_{j} a_{i j}$
> 局中人 $II$​ 最小预期损失（损失指对手最大收益）
>
> 极小极大值：$\min \limits_{j} \max \limits_{i} a_{i j}$​

!!! note "极大极小值与极小极大值"
    $\max _{i} \min _{j} a_{i j} \leq \min _{j} \max _{i} a_{i j}$<br>
    证明：对于 $\forall j$，有<br>

    $$
    \min _{j} a_{i j} \leq a_{i j}
    $$
    
    $$
    \max _{i} \mathop{\min _{j} a_{i j}}\limits_{第i行最小值} \leq  \mathop{\max _{i}a_{i j}}\limits_{第j列最大值}
    $$
    
    故
    
    $$
    \max _{i} \min _{j} a_{i j} \leq \min _{j} \max _{i} a_{i j}
    $$

### 均衡解

!!! note "矩阵鞍点"
 鞍点指的是矩阵中的一个元素，它是所在行的最大值，并且是所在列的最小值<br>
 **判断鞍点的一个充分条件是：函数在一阶导数为零处（驻点）的黑塞矩阵为不定矩阵。**

如果存在

$$
\max _{i} \min _{j} a_{i j}=\min _{j} \max _{i} a_{i j}=a_{i^{*} j^{*}} \triangleq V_{G}
$$

则 $\left(a_{i^{*}}, b_{j^{*}}\right)$ 为矩阵博弈的**最优纯策略对，也称为最优局势。**$V_{G}$ 称为博弈值。

!!! note "矩阵博弈最优纯策略对存在的充要条件是存在鞍点"
    非常强的条件
    证明：

1、必要性

$$
\begin{align}
    &\max_{i}\min_{j}a_{ij}=\min_{j}\max_{i}a_{ij}\\
    \Rightarrow &i^{*},j^{*},\min_{j}a_{ij*}=\max_{i}\min_{j}a_{ij}=\min_{j}\max_{i}a_{ij}=\max_{i}a_{ij*}\\
    \Rightarrow &a_{ij*}\geq\min_{j}a_{ij*}=\max_{i}\min_{j}a_{ij}=\min_{j}\max_{i}a_{ij}=\max_{i}a_{ij*}\\
    \Rightarrow&\max_{i}a_{ij*}=a_{i*j*}=\min_{j}a_{ij*}\\
    &a_{ij*}\leq a_{i*j*}\leq a_{i*j}
\end{align}
$$

2、充分性

$$
\Rightarrow\max_{i}a_{ij*}\leq a_{i*j*}\leq\min_{j}a_{i*j}\\
\Rightarrow\min_{j}\max_{i}a_{ij}\leq a_{i*j*}\leq\max_{i}\min_{j}a_{ij}\\
\max_{i}\min_{j}a_{ij}\leq\min_{j}\max_{i}a_{ij}\\
\max_{i}\min_{j}a_{ij}=\min_{j}\max_{i}a_{ij}
$$

鞍点解的博弈解释：没有一方愿意单方面改变策略，因为单方面改变策略均无法改善自身的赢得值，更多情况下反有损害。（共许原则）

### 性质

1、无差别性

若 $\left(a_{1 i}, b_{j 1}\right)$ 和 $\left(a_{2 i}, b_{j 2}\right)$ 是对策的两个解，

则

$$
a_{1 i j}=a_{2 i j}
$$

$$
A=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]
$$

---

2、可交换性

若 $\left(a_{1 i}, b_{j 1}\right)$ 和 $\left(a_{1 i}, b_{j 2}\right)$ 是对策的两个解，则 $\left(a_{1 i}, b_{j 2}\right)$ 和 $\left(a_{2 i}, b_{j 1}\right)$ 也是对策的解。

$$
A=\left[\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right]
$$

## 矩阵——混合策略博弈

### 模型

$G^{*}=\left\{S_{1}^{*}, S_{2}^{*} ; E\right\}$

混合策略集

$S_{1}^{*}=\left\{x \in R^{m} \mid x_{i} \geq 0, i=1,2, \cdots, m ; \sum_{i=1}^{m} x_{i}=1\right\}$

$x_{i}$ 为局中人 $I$ 执行纯策略 $a_{i}$​ 的概率

$S_{2}^{*}=\left\{y \in R^{n} \mid y_{j} \geq 0, j=1,2, \cdots, n ; \sum_{i=1}^{n} y_{j}=1\right\}$

$y_{j}$ 为居中人 $I I$ 执行纯策略 $b_{j}$ 的概率

局中人 $I$的赢得函数：$E(x, y)=x^{T} A y=\sum_{i=1}^{m} \sum_{j=1}^{n} a_{i j} x_{i} y_{j}$

局中人 $I I$ 的赢得函数：$-E(x, y)$

- 混合策略的取值在多次博弈中可看作概率，一次博弈中可看作偏好。
- 混合策略集是无穷集合，纯策略是混合策略的特例。
- 分析问题时，首先考虑纯策略博弈，当纯策略解不存在时，就考虑混合策略博弈。因此混合策略博弈也可以用 $G=\left\{S_{1}, S_{2} ; A\right\}$​​ 表示。

理性决策

- 局中人 $I$ 的最大预期赢得：$\max _{x \in S_{1}^{*}} \min _{y \in S_{2}^{*}} E(x, y)$
- 局中人 $I I$ 的最小预期损失：$\min _{y \in S_{2}^{*}} \max _{x \in S_{1}^{*}} E(x, y)$

两者关系：$\max _{x \in S_{1}^{*}} \min _{y \in S_{2}^{*}} E(x, y) \leq \min _{y \in S_{2}^{*}} \max _{x \in S_{1}^{*}} E(x, y)$

- 混合策略 $x=\left[x_{1}, x_{2}, \cdots, x_{m}\right]^{T} \quad y=\left[y_{1}, y_{2}, \cdots, y_{n}\right]^{T}$
- 混合局势 $(x, y)$

### 混合策略均衡解

- 最优混合策略对

$$
\max _{x \in S_{1}^{*}} \min _{y \in S_{2}^{*}} E(x, y)=\min _{y \in S_{2}^{*}} \max _{x \in S_{1}^{*}} E(x, y)=E\left(x^{*}, y^{*}\right) \triangleq V_{G}
$$

- 最优混合策略存在的充要条件：存在鞍点

$$
E\left(x, y^{*}\right) \leq E\left(x^{*}, y^{*}\right) \leq E\left(x^{*}, y\right)
$$

- 平衡局势 $\left(x^{*}, y^{*}\right)$

!!! note "定理：一定存在混合策略意义下的矩阵博弈均衡解"
    证明思路：鞍点条件一定有解。

    ![prove](https://img.philfan.cn/Math__OR__assets__OR-05-1-GameTheory.assets__image-20240606084717435.webp)

    ![prove](https://img.philfan.cn/Math__OR__assets__OR-05-1-GameTheory.assets__image-20240606084737444.webp)

### 均衡解的性质

#### 对称博弈性质

如果博弈问题具有如下对称性：

$$
A=-A^{T} \quad \text { 自身角度的赢得矩阵相同 }
$$

$$
\Rightarrow \quad T_{1}(G)=T_{\Pi}(G) \quad a_{ij}=\left\{\begin{array}{ll}
-a_{ij} & i \neq j \\
0 & i=j
\end{array}\right.
$$

$$
\Rightarrow V_{G}=E\left(x^{*}, y^{*}\right)=\sum_{j=1}^{n} \sum_{i=1}^{m} a_{i j} x_{i}^{*} y_{j}^{*}=-V_{G}=0 \quad \text { 最优策略时无赢家 }
$$

> 石头剪刀布问题

#### 解集不变性

- 赢得矩阵严格单调变换下的解集不变性

博弈：$G_{1}=\left\{S_{1}, S_{2} ; A_{1}\right\} \quad G_{2}=\left\{S_{1}, S_{2} ; A_{2}\right\}$

$$
A_{2}=A_{1}+L^{*} 1_{m \times n} \Rightarrow T\left(G_{1}\right)=T\left(G_{2}\right) \quad V_{G_{1}}=V_{G_{2}}+L
$$

$$
A_{2}=a A_{1}, \quad a>0 \Rightarrow T\left(G_{1}\right)=T\left(G_{2}\right) \quad V_{G_{1}}=a V_{G_{2}}
$$

- 解集 $T(G)$ : 博弈 $G$ 的均衡解集合。

证明：上述变换只改变了赢得矩阵元素的数值，不改变相对大小关系。

#### 互补松弛性

$$
x_{i}^{*}>0 \Rightarrow \sum_{j=1}^{n} a_{i j}^{*} y_{j}^{*}=v^{*}=E\left(x^{*}, y^{*}\right)\\
y_{j}^{*}>0 \Rightarrow \sum_{i=1}^{m} a_{i j}^{*} x_{i}^{*}=w^{*}=E\left(x^{*}, y^{*}\right)
$$

如果某条纯策略可能被选择，则该纯策略下对手的最优混合策略下的赢得值必为 $V_{G}$ 。

$$
\sum_{i=1}^{n} a_{i j} y_{j}<v^*=E\left(x^{*}, y^{*}\right) \Rightarrow x_{i}^{*}=0\\
\sum_{i=1}^{m} a_{i j} x_{i}^*>w^*=E\left(x^{*}, y^{*}\right) \Rightarrow y_{j}^{*}=0
$$

如果某条纯策略下对手的最优混合策略的赢得值比 $V_{G}$ 更好，则该纯策略无被选择可能。

## 矩阵——均衡解的求解

### 互补松弛性定理

### 对偶理论

### 线性规划解

## 双矩阵

（二人有限非零和博弈）

### Model

$$
G=\left\{S_{1}, S_{2} ; A, B\right\}
$$

- 局中人 I、II

- 策略集

$$
S_{1}=\left\{\alpha_{1}, \alpha_{2}, \cdots, \alpha_{m}\right\}
$$

$$
S_{2}=\left\{\beta_{1}, \beta_{2}, \cdots, \beta_{n}\right\}
$$

- 局中人 I 的赢得矩阵 $A$

- 局中人 II 的赢得矩阵 $B$

### 纯策略 Nash 均衡

满足以下条件的策略对 $\left(\alpha_{i^{*}}, \beta_{j^{*}}\right)$

$$
\begin{aligned}
&a_{i^{*}, j^{*}} \geq a_{i, j^{*}} \quad i=1,2, \cdots, m \\
&b_{i^{*}, j^{*}} \geq b_{i^{*}, j} \quad j=1,2, \cdots, n
\end{aligned}
$$

没有一个局中人愿意单方面改变策略

$$
A=\left[\begin{array}{cc}
-9 & 0 \\
-15 & -1
\end{array}\right] \quad B=\left[\begin{array}{cc}
-9 & -15 \\
0 & -1
\end{array}\right]
$$

> 例子：囚徒困境——占优策略 Nash 均衡

### 混合策略 Nash 均衡

- 赢得函数

$$
E_{1}(x, y)=x^{T} A y=\sum_{i=1}^{m} \sum_{j=1}^{n} a_{i j} x_{i} y_{j} \quad E_{2}(x, y)=x^{T} B y=\sum_{i=1}^{m} \sum_{j=1}^{n} b_{i j} x_{i} y_{j}
$$

- Nash 混合策略均衡点

满足以下条件的策略对 $(x *, y *)$

$$
\begin{aligned}
&E_{1}\left(x^{*}, y^{*}\right) \geq E_{1}\left(x, y^{*}\right) \quad x \in S_{1}^{*} \\
&E_{2}\left(x^{*}, y^{*}\right) \geq E_{2}\left(x^{*}, y\right) \quad y \in S_{2}^{*}
\end{aligned}
$$

如果纯策略均衡解存在，也是混合策略的均衡解。

!!! note "$n$ 人有限策略博弈至少存在一个 Nash 均衡点（包括纯策略和混合策略）（Nash, 1950）"

### Pareto 最优

允许合作下的博弈问题为多目标优化问题：

- 目标 1: $\max _{x_{i} \in S_{1}^{*}, y_{j} \in S_{2}^{*}} E_{1}(x, y)$
- 目标 2: $\max _{x_{i} \in S_{1}^{*}, y_{j} \in S_{2}^{*}} E_{2}(x, y)$

- Pareto 最优解 $\left(x^{*}, y^{*}\right)$ : 不存在超优 $\left(x^{*}, y^{*}\right)$ 的策略对。

$\left(x_{1}, y_{1}\right)$ 超优 $(\operatorname{dominate})\left(x_{2}, y_{2}\right)$ :

$$
\begin{align}
E_{1}\left(x_{1}, y_{1}\right) \ge E_{1}\left(x_{2}, y_{2}\right) \\E_{2}\left(x_{1}, y_{1}\right) \ge E_{2}\left(x_{2}, y_{2}\right) \\
\end{align}
$$

且至少有一个不等式严格成立。

纯策略 Nash 均衡解

| III | 坦白 | 抗拒 |
| ---- | ---- | ---- |
| 坦白 | (-9,-9) **Nash 均衡** | (0,-15) |
| 抗拒 | (-15,0) | (-1,-1)**Pareto 最优解** |

严格意义下的解：**满足可交换性和无差别性的 Pareto 最优均衡解**

Nash 均衡解的充要条件

- 定理：$\left(x^{*}, y^{*}\right)$ 是 $G=\left\{S_{1}, S_{2} ; A, B\right\}$ 的 Nash 均衡解的充要条件为：

$$
\begin{aligned}
&\sum_{j=1}^{n} a_{i j} y_{j}^{*} \leq E_{1}\left(x^{*}, y^{*}\right) \quad i=1,2, \cdots, m \Rightarrow A y^{*} \leq E_{1}\left(x^{*}, y^{*}\right) 1_{m} \\
&\sum_{i=1}^{m} b_{i j} x_{i}^{*} \leq E_{2}\left(x^{*}, y^{*}\right) \quad j=1,2, \cdots, n \Rightarrow B^{T} x^{*} \leq E_{2}\left(x^{*}, y^{*}\right) 1_{n} \\
&x \in S_{1}^{*} \quad y \in S_{2}^{*}
\end{aligned}
$$

![proof](https://img.philfan.cn/Math__OR__assets__OR-05-1-GameTheory.assets__image-20240606093544168.webp)
