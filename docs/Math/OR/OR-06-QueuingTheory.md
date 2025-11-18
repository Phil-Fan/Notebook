# 排队论 | Queuing Theory

排队论主要研究各种系统的排队队长，排队的等待时间及所提供的服务等各种参数，以便求得更好的服务。它是研究系统随机聚散现象的理论。

应用：电话接线、机器管理、陆空交通、网络管理

## 主要参数

对于常见的大部分模型，我们均假设顾客抵达时间的分布，服务台服务时间的分布为独立同分布(independent and identically distributed), 通用队列模型表达式如下:

| 参数 | 含义 |
|------|------|
|A|顾客抵达的概率分布|
|B|服务时间的概率分布|
|X|服务台的数量|
|Y|服务台的容量|
|Z|排队机制|

| Characteristic                         | Symbol     | Explanation                  |
| ---- | ---- | ---- |
| A & B | $M$        | Exponential                  |
| A & B| $D$  | Deterministic  |
| A & B  | $E_k$ | Erlang type $k$ ($k = 1, 2, \dots$) |
| A & B | $H_k$      | Mixture of $k$ exponentials  |
| A & B | $PH$       | Phase type                   |
|  A & B | $G$        | General                      |
| X | $1, 2, \dots, \infty$ | Number of servers |
| Y | $1, 2, \dots, \infty$ | Maximum jobs in system |
| Z  | $\text{FCFS}$ | First come, first served |
| Z | $\text{LCFS}$ | Last come, first served |
| Z | $\text{RSS}$  | Random selection for service |
| Z | $\text{PR}$   | Priority |
| Z | $\text{GD}$   | General discipline |

## A/B 概率分布类型

### Exponential（指数分布）

- **概率密度函数 (PDF)**  
  
  $$
  f(t)=\lambda e^{-\lambda t},\quad t\ge 0,\ \lambda>0
  $$

- **内涵**  
  指数分布描述“无记忆”的随机现象：过去等待的时间不影响未来剩余等待时间的分布。在排队论中，它常被用来刻画顾客到达间隔或服务时间，因为假设事件以恒定速率 $\lambda$ 独立发生。

### Deterministic（确定性分布）

- **概率密度函数 (PDF)**  
  
  $$
  f(t)=\delta(t-c),\quad c>0
  $$

- **内涵**  
  所有样本都取固定值 $c$，方差为零。适用于服务时间或到达间隔完全可控、无波动的理想化场景，如定时发车的班车或固定处理时间的机器。

### Erlang type $k$（埃尔朗分布）

- **概率密度函数 (PDF)**  
  
  $$
  f(t)=\frac{\lambda^k t^{k-1} e^{-\lambda t}}{(k-1)!},\quad t\ge 0,\ k\in\mathbb N^+,\ \lambda>0
  $$

- **内涵**  
  埃尔朗分布是 $k$ 个独立同分布的指数随机变量之和的分布。形状参数 $k$ 控制变异程度：$k=1$ 退化为指数分布；$k\to\infty$ 趋近于确定性分布。常用于模拟多阶段串联服务或批量到达/服务过程。

### Mixture of $k$ exponentials（$k$ 指数混合分布）

- **概率密度函数 (PDF)**  
  
  $$
  f(t)=\sum_{i=1}^k w_i \lambda_i e^{-\lambda_i t},\quad t\ge 0,\ w_i>0,\ \sum_{i=1}^k w_i=1
  $$

- **内涵**  
  由 $k$ 条不同速率的指数分布加权叠加而成，可灵活刻画具有多类顾客或多类服务模式的系统。其变异系数可大于 1，适合描述重尾或异质到达/服务行为。

### Phase type（相位型分布，PH 分布）

- **概率密度函数 (PDF)**  
  设初始概率向量 $\boldsymbol{\alpha}$，子生成元矩阵 $\mathbf{T}$，则  
  
  $$
  f(t)=\boldsymbol{\alpha} e^{\mathbf{T}t}(-\mathbf{T}\mathbf{1}),\quad t\ge 0
  $$

- **内涵**  
  PH 分布描述在有限状态连续时间马尔可夫链中，从初始状态到吸收状态的首次通过时间。它可逼近任意非负分布，兼具解析可解性与建模灵活性，是现代排队分析中处理复杂到达/服务过程的核心工具。

## 主要模型

## 应用领域

## 主要文章、书籍、论文
