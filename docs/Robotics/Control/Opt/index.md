---
comments: true
---
# 最优控制

什么是最优控制：

- 在一定约束条件下，达到的最优的系统表现

什么是最优？

- 人为设计惩罚函数
- 系统表现
- 控制系统中的最优是综合分析的结果

=== "SISO 系统"

    $$
    e = y-r
    $$


    假设一个轨迹跟踪过程

    令 

    $$
    J = \int_{0}^{t} q *(e)^2 + r *(u)^2 dt
    $$

    - $q$和$r$是人为设计的惩罚系数。
    - $\int_{0}^{t} q *(e)^2$ 表示跟踪误差的惩罚
    - $\int_{0}^{t} r *(u)^2$ 表示控制量的惩罚。

    我们的目的就是设计一个控制器，使得$J$最小。

=== "MIMO 系统"

对于 MIMO 系统，最优控制问题可以表示为：

$$
\min_{u(t)} J = \int_{0}^{\infty} \mathbf{E}^T \mathbf{Q} \mathbf{E} + \mathbf{U}^T \mathbf{R} \mathbf{U} dt
$$

- $\mathbf{E} = \begin{pmatrix} e_1 & e_2 & \cdots & e_n \end{pmatrix}^T$ 是跟踪误差
- $\mathbf{Q}  = diag(q_1, q_2, \cdots, q_n)$ 是跟踪误差的惩罚矩阵
- $\mathbf{U} = \begin{pmatrix} u_1 & u_2 & \cdots & u_n \end{pmatrix}^T$ 是控制量
- $\mathbf{R} = diag(r_1, r_2, \cdots, r_n)$ 是控制量的惩罚矩阵

如果要关心输入，那么需要提高$r$的值，如果关心输出，那么需要提高$q$的值。
