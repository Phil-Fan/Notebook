# 04 | 瞬时运动学

这一章主要讲的是关节空间和笛卡尔空间之间的桥梁——雅可比矩阵

从运动学方程微分、向量积构造法、速度向外传递、力向内传递逐步认识到雅可比矩阵这一强大的工具

!!! note "Acknowledgement"
    特别鸣谢以下文章

    - [机器人学导论---第五章 速度和静力（一）5.1-5.11（好难） - 知乎](https://zhuanlan.zhihu.com/p/155829972)
    - [干货 | “瞬时运动学”——还是从关节空间到操作空间（雅可比矩阵上篇） - 知乎](https://zhuanlan.zhihu.com/p/341804875)
    - [干货 | 机械臂的雅可比矩阵这么厉害，怎么把它求出来呢？（雅可比矩阵中篇） - 知乎](https://zhuanlan.zhihu.com/p/341805201)
    - [干货 | 力的传递关系、奇异、冗余——从雅可比矩阵你还能得到什么？（雅可比矩阵下篇） - 知乎](https://zhuanlan.zhihu.com/p/341806737)

## 前置知识

- 向量叉乘
- 矩阵求微分
- 向量求导、矩阵求导

$$
\frac{d\vec{x}}{d\vec{q}}=\frac{d\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}}{d\begin{bmatrix}q_1\\q_2\end{bmatrix}}=\begin{bmatrix}\frac{dx_1}{dq_1}&\frac{dx_1}{dq_2}\\\frac{dx_2}{dq_1}&\frac{dx_2}{dq_2}\\\frac{dx_3}{dq_1}&\frac{dx_3}{dq_2}\end{bmatrix}
$$

- 矩阵求逆（逆矩阵、伪逆）
- 二次型
- 奇异值分解

## 时变位姿

!!! abstract "本节内容：角速度的表示、线速度的表示、如何在不同连杆之间传递速度"
    由理论力学知：刚体（其联体坐标系为$B$）在参考坐标系{A}中的任何运动都可以分解为点 $^A \!O_B$ 的运动和刚体绕 $^A \!O_B$ 的定点转动

    所以这一节先研究如何表示运动

!!! note "本节的一些符号表示"

| 符号 | 含义 | 注意点 |
| --- | --- | --- |
| ${}^B\mathbf{V}_Q$ | 线速度向量 | |
| $\mathbf{v}_C$ | 相对于世界坐标系 | $\mathbf{v}_C = {}^U\mathbf{V}_{\text{CORG}}$ |
| ${}^A\Omega_B$ | 角速度向量 | 在{A}中描述{B}的定点转动 |
| $\mathbf{\omega}_C$ | 相对于世界坐标系角速度 | $\mathbf{\omega}_C = {^U_C}\mathbf{\Omega}_C$ |

### 坐标系的平移

同维矢量的微分表示

若 \( {}^B\mathbf{Q} \) 是描述某个点的位置矢量，该点关于{B}的速度是 \( {}^B\mathbf{V}_Q \)。

$$
{}^B\mathbf{V}_Q = \frac{d}{dt} {}^B\mathbf{Q} = \lim_{\Delta t \to 0} \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t}
$$

速度矢量 \( {}^B\mathbf{V}_Q \) 可在任意坐标系中描述 (相当于在 B 的原点建立一个和 B 固连的，与 A 姿态相同的坐标系)

$$
{}^A({}^B\mathbf{V}_Q) = {}^A_B\mathbf{R} {}^B\mathbf{V}_Q = ^A(\frac{d}{dt} {}^B\mathbf{Q}) = \lim_{\Delta t \to 0} {}^A_B\mathbf{R}(t) \left( \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t} \right)
$$

坐标系原点相对于世界坐标系{U}的速度:$\mathbf{v}_C = {}^U\mathbf{V}_{\text{CORG}}$

!!! note "需要注意，${}^A({}^B\mathbf{V}_Q)$ 不同于 ${}^A\mathbf{V}_Q$"

    $$
    \begin{align*}
    {}^A\mathbf{V}_Q &= \lim_{\Delta t \to 0} \frac{{}^A\mathbf{Q}(t + \Delta t) - {}^A\mathbf{Q}(t)}{\Delta t}\\
    &= \lim_{\Delta t \to 0} \frac{{}^A\mathbf{P}_{BORG}(t + \Delta t) + {}^A_B\mathbf{R}(t + \Delta t) {}^B\mathbf{Q}(t + \Delta t) - {}^A\mathbf{P}_{BORG}(t) - {}^A_B\mathbf{R}(t) {}^B\mathbf{Q}(t)}{\Delta t}
    \end{align*}
    $$
    
    特别注意符号的意义
    ${}^A\mathbf{v}_C = {}^A_U\mathbf{R} \mathbf{v}_C = {}^A_U\mathbf{R} {}^U\mathbf{V}_{\text{CORG}} \neq {}^A\mathbf{V}_{\text{CORG}}$

### 坐标系的转动

在 $\{A\}$ 中描述 $\{B\}$ 的定点转动可用角速度向量 $^A\mathbf{\Omega}_B$ 表示

- $^A\mathbf{\Omega}_B$的方向是瞬轴在 $\{A\}$ 中的方向
- $^A\mathbf{\Omega}_B$的大小表示在 $\{A\}$ 中 $\{B\}$ 绕瞬轴的旋转速度。
- 在任意坐标系中描述：$^C(^A\mathbf{\Omega}_B) = {^C_A}\mathbf{R}{^A\mathbf{\Omega}_B}$
- 世界坐标系：$\mathbf{\omega}_C = {^U_C}\mathbf{\Omega}_C$

特别要注意下列符号的意思

$$
\begin{align*}
^A\mathbf{\omega}_C &= {^U_C}\mathbf{R}\mathbf{\omega}_C = {^A_U}\mathbf{R}{^U_C}\mathbf{\Omega}_C \neq {^A\mathbf{\Omega}_C}\\
^C\mathbf{\omega}_C &= {^C_U}\mathbf{R}\mathbf{\omega}_C = {^C_U}\mathbf{R}{^U_C}\mathbf{\Omega}_C
\end{align*}
$$

### 刚体线速度

$$
^A\mathbf{V}_Q = {^A\mathbf{V}_{BORG}} + {^A_B}\mathbf{R}{^B\mathbf{V}_Q} + {^A\mathbf{\Omega}_B} \times {^A_B}\mathbf{R}{^B\mathbf{Q}}
$$

$Q$ 点对 ${A}$ 的线速度为坐标系 ${B}$ 原点的线速度、$Q$ 点在坐标系 ${B}$ 中的线速度和坐标系 ${B}$ 针对坐标系 ${A}$ 旋转形成的 $Q$ 点切向线速度三者的向量合成

### 角速度关系

$$
{^A\mathbf{\Omega}_C} = {^A\mathbf{\Omega}_B} +   {^A_B}\mathbf{R}{^B_C}\mathbf{\Omega}_C
$$

在同一坐标系中，角速度可以相加

角速度矩阵$S(\mathbf{\omega})$

$$
S(\mathbf{\omega}) = \begin{bmatrix}
0 & -\omega_z & \omega_y \\
\omega_z & 0 & -\omega_x \\
-\omega_y & \omega_x & 0
\end{bmatrix}
$$

- 反对称矩阵
- $S = \dot{R}R^T$

### 连杆间速度传递（向外迭代法）

!!! note "规律"
    - 前一个关节的线速度和角速度都要转换到后一个关节上面
    - 转动型关节会增加角速度的项，平动型关节会增加线速度的项。

转动型关节

角速度：连杆 i+1 针对世界坐标系角速度在{i+1}坐标系的表示

$$
^{i+1}\!\omega_{i+1} = ^{i+1}_i\!R {^i\omega_i} + \dot{\theta}_{i+1} {}^{i+1}\!\hat{Z}_{i+1}\\
$$

> 其中，$\hat{Z}_{i+1}$ 是轴 $i+1$在 ${i+1}$ 中的表示；${\theta}_{i+1}$ 是转动型关节 $i+1$ 的关节转速。

线速度：连杆 i+1 针对世界坐标系线速度在{i+1}坐标系的表示

$$
{}^{i+1}\!v_{i+1} = {^{i+1}_iR} (^iv_i + ^i\omega_i \times {^iP_{i+1}})
$$

> 连杆的长度隐含在了 $^iP_{i+1}$ 叉乘项当中

平动型

角速度：不变

$$
^{i+1}\omega_{i+1} = _i^{i+1}R {^i\omega_i}
$$

线速度：要加一个在轴线上的速度

$$
^{i+1}v_{i+1} = _i^{i+1}R (^iv_i + ^i\omega_i \times ^iP_{i+1}) + \dot{d_{i+1}} \hat{Z}_{i+1}
$$

## 静力学

### 力学基本概念

**力的大小：** 衡量力对平动的作用效果

**力矩：** 衡量力对转动的作用效果

**力偶：** 等大反向不共线的力，所有旋转都可以等效看作是力偶的作用。也就是说，力形成力偶，才使得物体发生了旋转。

**力偶矩：** 用来描述物体力偶的作用效果

**物体平衡的条件：** 合力为 0，合力矩为 0

> 参考资料<br>
> [力矩、力偶矩、弯矩的区别是什么？ - 知乎](https://www.zhihu.com/question/23371844?sort=created)<br>
> [力矩的本质是什么？与力偶有什么关系？ - 知乎](https://www.zhihu.com/question/398334639/answer/1258696609)<br>

### 力的平移原理

- 引理 1：作用在刚体上的力沿着其作用线移动后，力对刚体作用效应不变
- 引理 2：在刚体上增加一组平衡力系，不改变原力系对刚体的作用效应

所以如果想将力平移，那么可以在 B 点增加一组平衡力系，使得 B 点的力和 A 点的力相同，方向相反。这个时候把$F$和$F_2$视为一组力偶。

可以看作力$F$平移到$F_1$之后，刚体受到$F_1$和力偶矩$M = F \times r_{AB}$

![image](https://img.philfan.cn/Robotics__Model__assets__4-Mechanics.assets__20250313095306008.webp)
> 图源 [力平移定理与平衡 - CSDN 博客](https://blog.csdn.net/weixin_43989965/article/details/120471367)

### 操作臂的静力传递（向内迭代法）

> 要解决的问题是：如果机械臂末端抓着一个重物，为了保持末端位置不动，各个关节需要输出多大的力矩呢？或者如果机械臂末端要对工件施加一个固定的加工力，各个关节又需要输出多大的力矩呢？

- 传递方向：从末端向下传递
- 方式：先固定，写出各连杆的平衡关系，再加外力，写出各关节轴需要加多少力

> 忽略重力

![image](https://img.philfan.cn/Robotics__Model__assets__4-Mechanics.assets__20250313114049005.webp)

$$
\begin{align*}
^i f_i = ^i f_{i+1}\\
^i n_i = ^i n_{i+1} + ^{i}P_{i+1} \times ^{i}f_{i+1}
\end{align*}
$$

加上坐标系变换后

$$
\begin{align*}
^i f_i = ^{i}_{i+1}R ^{i+1} f_{i+1}\\
^i n_i = ^{i}_{i+1}R^{i+1} n_{i+1} + ^{i}P_{i+1} \times ^{i}f_{i+1}
\end{align*}
$$

!!! note "转动型关节需要考虑施加多少力矩，平动型关节需要考虑施加多少力。需要对 (力，力矩) 向量进行正交分解"

**转动型关节$i$**

$f_i$ 不是主动力而是约束力，它阻止连杆 $i$ 作直线运动；$n_i$ 阻止连杆 $i$ 作旋转运动。在 $\{i\}$ 中对 $n_i$ 进行正交分解，可得到 1 个沿 $\hat{z}_i$ 的力矩向量和 1 个垂直于 $\hat{z}_i$ 的力矩向量，垂直于 $\hat{z}_i$ 的力矩向量是约束力矩，沿 $\hat{z}_i$ 的力矩向量是主动力矩，主动力矩需由关节 $i$ 的旋转驱动器提供，主动力矩可表示为 $\tau_i \hat{z}_i$，其中

$$
\tau_i = |n_i| \cos \theta = |n_i| |\hat{z}_i| \cos \theta = n_i^{\mathrm{T}} \hat{z}_i
$$

**平动型关节$i$**

$n_i$ 是约束力矩。在 $\{i\}$ 中对 $f_i$ 进行正交分解，得到 1 个主动力和 1 个约束力，需由关节 $i$ 的直线驱动器提供的主动力表示为 $\tau_i \hat{z}_i$，其中

$$
\tau_i = f_i^{\mathrm{T}} \hat{z}_i
$$

!!! example "例子"
    ![image](https://img.philfan.cn/Robotics__Model__assets__4-Mechanics.assets__20250313112419504.webp)
    ![image](https://img.philfan.cn/Robotics__Model__assets__4-Mechanics.assets__20250313112444810.webp)
    > 课本习题

## 雅可比

**雅可比矩阵的作用**：

1. 雅可比将关节空间的速度转化为末端空间的速度：$\dot{\mathbf{x}}=J(\mathbf{q})\dot{\mathbf{q}}$

2. 雅可比将关节空间的位移转化为末端空间的位移：$\delta\mathbf{x}=J(\mathbf{q})\delta\mathbf{q}$

3. 雅可比将末端空间的速度转化为关节空间的速度：$\dot{\mathbf{q}}=J(\mathbf{q})^{-1}\dot{\mathbf{x}}$

4. 雅可比将末端空间的位移转化为关节空间的位移：$\delta\mathbf{q}=J(\mathbf{q})^{-1}\delta\mathbf{x}$

5. 雅可比将末端空间的力转化为关节空间的力 (扭矩)：$\tau=J^T\mathbf{F}$

### 直观理解

复杂变换在某个局部点可以看作线性变换

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=79626296&bvid=BV1NJ411r7ja/?share_source=copy_web&vd_source=1ce3320d605852426ce5ccfc9b31eb50&t=233&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=80% height=auto></iframe>

!!! note "雅可比矩阵由来"

    关节速度 $\dot{q}$ 末端速度$\dot{x}$

    速度描述的是短时间的位置变化，即位置关于时间的导数

    $$
    \frac{d\vec{x}}{dt}=\frac{df(\vec{q})}{dt}=\frac{df(\vec{q})}{d\vec{q}}\cdot\frac{d\vec{q}}{dt}
    $$

    $$
    \dot{x}=\frac{d\vec{x}}{d\vec{q}}\cdot\dot{q} = J(q)\dot{q}
    $$

    - 第$i$行第$j$列表示的物理意义就是当第$j$个关节运动时，操作空间的第$i$个平动/转动方向会如何运动
    - 雅可比矩阵表明 end effector 的速度与关节速度 joint velocity 之间是线性关系

$$
J=\begin{bmatrix}(J_v)_ {3\times n}\\(J_\omega)_ {3\times n}\end{bmatrix}
$$

$J_v$表示的含义是一个机械臂的关节移动多少角度，它的 end effector 就会相应地移动多少距离（速度）

$J_\omega$表示的含义是一个机械臂的旋转关节绕某个轴转多少角度，它的 end effector 就会相应地绕这个轴转多少角度

- 雅可比矩阵的行数是操作空间的自由度，列数是关节数量（关节自由度）。
- 雅可比矩阵是时变的
- 雅可比矩阵可以看作 x 的速度空间向 y 的速度空间做映射$\dot{x} = J(q) \dot{q}$

### 几何雅可比

!!! note "课本上面描述的方法求解的都是几何雅可比"

以机器人每个关节均为转动型关节为例构造几何雅可比矩阵。

定义笛卡尔速度向量 $v_N = \begin{pmatrix} v_N \\ \omega_N \end{pmatrix} \in \mathbb{R}^6$ 和关节空间角速度向量 $\dot{\Phi} = \begin{pmatrix} \dot{\theta}_1 \\ \dot{\theta}_2 \\ \vdots \\ \dot{\theta}_N \end{pmatrix} \in \mathbb{R}^N$，则：

$$
v_N = \begin{pmatrix} \hat{Z}_1 \times (O_N - O_1) & \hat{Z}_2 \times (O_N - O_2) & \cdots & \hat{Z}_{N-1} \times (O_N - O_{N-1}) & 0 \\ \hat{Z}_1 & \hat{Z}_2 & \cdots & \hat{Z}_{N-1} & \hat{Z}_N \end{pmatrix} \dot{\Phi}\\
= \mathbf{J(\Phi)}\dot{\Phi}
$$

此处，$J(\Phi) \in \mathbb{R}^{6 \times N}$ 即为雅可比矩阵。

### 分析雅可比

令$X=\begin{pmatrix}\boldsymbol{P}(\boldsymbol{\Phi})\\\boldsymbol{\psi}(\boldsymbol{\Phi})\end{pmatrix}$表示机器人末端执行器的位置与姿态，其中$\boldsymbol{P}(\boldsymbol{\Phi})$为基座坐标系原点到末端执行器坐标系原点的一般向量，$\Psi(\boldsymbol{\Phi})$为末端执行器坐标系相对于基座坐标系姿态的最小表示 (如固定角表示或欧拉角表示)。分析雅可比矩阵满足以下形式

$$\dot{\boldsymbol{X}}=\begin{pmatrix}\dot{\boldsymbol{P}}\\\dot{\boldsymbol{\psi}}\end{pmatrix}=\boldsymbol{J}_a(\boldsymbol{\Phi})\dot{\boldsymbol{\Phi}}$$

!!! tip "空间中确定一个旋转至少需要 3 个参数"
    SO(3)群有6个约束：两个单位向量（范数为1），两个单位向量正交，叉乘得到第三个单位向量

    所以自由度是3

    因为固定角/欧拉角有3个自由度（3个参数），所以又称之为最小表示运动学方程

### 几何雅可比和分析雅可比

| 符号 | 含义 |
| ------ | ------ |
| $q$ | 关节角度向量，表示机器人各个关节的角度值 |
| $\dot{q}$ | 关节速度向量，表示关节变量的时间变化率 |
| $p_e$ or $x$ | 末端执行器的位置向量 |
| $\dot{p}_e$ or $\dot{x}$ | 末端执行器的位置变化率（平移速度） |
| $\phi_e$ | 末端执行器的姿态（通常用欧拉角表示） |
| $\dot{\phi}_e$ | 末端执行器的**姿态变化率（旋转速度）** |
| $\omega$ | 角速度向量，表示**绕各个轴**的旋转速度 |
| $v$ | 线速度向量，表示在笛卡尔空间中的平移速度 |

> 参考文献：[机械臂的几何雅可比和分析雅可比有什么区别？ - 知乎](https://www.zhihu.com/question/67687838)

**Analytical Jacobians**：

- 在笛卡尔坐标系下，它得到的“角速度”是选择的表示末端方向的角度的时间导数。
- 表示的是机器人姿态的变化。这个姿态是自己定义的，它取决于你的坐标系。

$$
\begin{align*}
\dot{x} &= \frac{d}{dt}(x, y, z, \phi, \theta, \psi) = \begin{bmatrix} \frac{dx}{dt} & \frac{dy}{dt} & \frac{dz}{dt} & \frac{d\phi}{dt} & \frac{d\theta}{dt} & \frac{d\psi}{dt} \end{bmatrix}^T\\
&= \begin{bmatrix}
\dot{P} \\
\dot{\phi}
\end{bmatrix}= J_A(q) \dot{q}
\end{align*}
$$

**Geometrical Jacobians**：

- 获得的“角速度”是绕旋转轴的速度。得到的是关节空间速度与末端力矩之间的映射关系。

$$
\begin{align*}
\dot{x} &= \begin{bmatrix} \frac{dx}{dt} & \frac{dy}{dt} & \frac{dz}{dt} & \omega_x & \omega_y & \omega_z \end{bmatrix}^T\\
&= \begin{bmatrix}
\dot{P} \\
\dot{\omega}
\end{bmatrix}= J(q) \dot{q}
\end{align*}
$$

其中，$\omega_x$、$\omega_y$、$\omega_z$ 表示绕 $x$、$y$、$z$ 轴的角速度。

转化关系

$$
J(\Phi) \dot{\Phi} = \begin{pmatrix} v \\ \omega \end{pmatrix} = \begin{pmatrix} \dot{P} \\ B_a(\Psi)\dot{\Psi} \end{pmatrix} = \begin{pmatrix} I & 0 \\ 0 & B_a(\Psi) \end{pmatrix} \begin{pmatrix} \dot{P} \\ \dot{\Psi} \end{pmatrix}= \begin{pmatrix} I & 0 \\ 0 & B_a(\Psi) \end{pmatrix} J_a(\Phi) \dot{\Phi}
$$

所以，分析雅可比矩阵 $J_a(\Phi)$ 与几何雅可比矩阵 $J(\Phi)$ 的关系为：

$$
J_a(\Phi) = \begin{pmatrix} I & 0 \\ 0 & B_a^{-1}(\Psi) \end{pmatrix} J(\Phi) = T_a J(\Phi)
$$

刚体角速度$\omega$和欧拉角速率$\dot{\Psi}$之间的关系

$$
\omega = \begin{pmatrix}
0 & -s\alpha & c\alpha s\beta \\
0 & c\alpha & s\alpha s\beta \\
1 & 0 & c\beta
\end{pmatrix} \dot{\Psi} = B_a(\Psi) \dot{\Psi}
$$

??? note "证明"

    若刚体姿态矩阵为 $R = \begin{pmatrix}    r_{11} & r_{12} & r_{13} \\    r_{21} & r_{22} & r_{23} \\    r_{31} & r_{32} & r_{33}\end{pmatrix}$ ,刚体角速度 $\omega$ 为：$\omega = \begin{pmatrix}    \omega_x \\    \omega_y \\    \omega_z    \end{pmatrix}$

    $$
    \dot{R} R^T = S\\
    \begin{pmatrix}
    \dot{r}_{11} & \dot{r}_{12} & \dot{r}_{13} \\
    \dot{r}_{21} & \dot{r}_{22} & \dot{r}_{23} \\
    \dot{r}_{31} & \dot{r}_{32} & \dot{r}_{33}
    \end{pmatrix}
    \begin{pmatrix}
    r_{11} & r_{21} & r_{31} \\
    r_{12} & r_{22} & r_{32} \\
    r_{13} & r_{23} & r_{33}
    \end{pmatrix}=\begin{pmatrix}
    0 & -\omega_z & \omega_y \\
    \omega_z & 0 & -\omega_x \\
    -\omega_y & \omega_x & 0
    \end{pmatrix}
    $$

    对应元素相等可以得到

    $$
    \omega_x = \dot{r}_{31} r_{21} + \dot{r}_{32} r_{22} + \dot{r}_{33} r_{23}\\
    \omega_y = \dot{r}_{11} r_{31} + \dot{r}_{12} r_{32} + \dot{r}_{13} r_{33}\\
    \omega_z = \dot{r}_{21} r_{11} + \dot{r}_{22} r_{12} + \dot{r}_{23} r_{13}
    $$


    以 $z-y-z$ 欧拉角表示刚体在基坐标系中的姿态为例，此时：

    $$
    R = R_{z'y'z'}(\alpha, \beta, \gamma) = R_z(\alpha) R_y(\beta) R_z(\gamma)= \begin{pmatrix}
    c\alpha & -s\alpha & 0 \\
    s\alpha & c\alpha & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
    c\beta & 0 & s\beta \\
    0 & 1 & 0 \\
    -s\beta & 0 & c\beta
    \end{pmatrix}
    \begin{pmatrix}
    c\gamma & -s\gamma & 0 \\
    s\gamma & c\gamma & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    $$



    记 $z-y-z$ 欧拉角表示为 $\Psi = (\alpha, \beta, \gamma)^T$，欧拉角速率为 $\dot{\Psi} = (\dot{\alpha}, \dot{\beta}, \dot{\gamma})^T$，

    $$
    \begin{align*}
    \omega_x &= \dot{r}_{31} r_{21} + \dot{r}_{32} r_{22} + \dot{r}_{33} r_{23}\\
    &= \left( \frac{\partial r_{31}}{\partial \alpha} \dot{\alpha} + \frac{\partial r_{31}}{\partial \beta} \dot{\beta} + \frac{\partial r_{31}}{\partial \gamma} \dot{\gamma} \right) r_{21} + \left( \frac{\partial r_{32}}{\partial \alpha} \dot{\alpha} + \frac{\partial r_{32}}{\partial \beta} \dot{\beta} + \frac{\partial r_{32}}{\partial \gamma} \dot{\gamma} \right) r_{22} + \left( \frac{\partial r_{33}}{\partial \alpha} \dot{\alpha} + \frac{\partial r_{33}}{\partial \beta} \dot{\beta} + \frac{\partial r_{33}}{\partial \gamma} \dot{\gamma} \right) r_{23}\\
    &= \begin{pmatrix} 0 & -s\alpha & c\alpha s\beta \end{pmatrix} \dot{\Psi}
    \end{align*}
    $$

    同理可得：

    $$
    \begin{align*}
    \omega_y = \dot{r}_{11} r_{31} + \dot{r}_{12} r_{32} + \dot{r}_{13} r_{33} = \begin{pmatrix} 0 & c\alpha & s\alpha s\beta \end{pmatrix} \dot{\Psi}\\
    \omega_z = \dot{r}_{21} r_{11} + \dot{r}_{22} r_{12} + \dot{r}_{23} r_{13} = \begin{pmatrix} 1 & 0 & c\beta \end{pmatrix} \dot{\Psi}
    \end{align*}
    $$

### 坐标变换

[极坐标和直角坐标的雅克比矩阵推导\_直角坐标到极坐标的雅可比矩阵-CSDN 博客](https://blog.csdn.net/subtitle_/article/details/133185018)

如果雅可比矩阵不是表示在 frame{0}下面，需要进行坐标变换，需要左乘一个转换矩阵就可以了。

> 回想一下微积分中变量替换，替换变量的时候需要乘以雅可比矩阵行列式

!!! example "柱坐标"
    例如，如果你的end effector位置是由柱坐标表示的，即$(\rho, \theta, z)$，而柱坐标转换为笛卡尔坐标是：

    $$
    x = \rho \cos \theta\\
    y = \rho \sin \theta\\
    z = z
    $$

    那么转换矩阵$T_p$（这里的p表示position）就由笛卡尔坐标对柱坐标的向量求导得出：

    $$
    T_p = \frac{\partial \begin{bmatrix} x \\ y \\ z \end{bmatrix}}{\partial \begin{bmatrix} \rho \\ \theta \\ z \end{bmatrix}} = \begin{bmatrix} \cos \theta & -\rho \sin \theta & 0 \\ \sin \theta & \rho \cos \theta & 0 \\ 0 & 0 & 1 \end{bmatrix}
    $$

    $$
    \frac{\partial(x_1,x_2,\cdots,x_n)}{\partial(y_1,y_2,\cdots,y_m)}=\begin{bmatrix}\frac{\partial x_1}{\partial y_1}&\frac{\partial x_1}{\partial y_2}&\cdots&\frac{\partial x_1}{\partial y_m}\\\frac{\partial x_2}{\partial y_1}&\frac{\partial x_2}{\partial y_2}&\cdots&\frac{\partial x_2}{\partial y_m}\\\vdots&\vdots&&\vdots\\\frac{\partial x_n}{\partial y_1}&\frac{\partial x_n}{\partial y_2}&\cdots&\frac{\partial x_n}{\partial y_m}\end{bmatrix}
    $$

而新的雅可比矩阵的上半部分就等于基本雅可比矩阵的$J_v$左乘上这个$T_p$。对于旋转也类似

$$
^i\boldsymbol{J}(\boldsymbol{\Phi})=\begin{pmatrix}{}_0^i\boldsymbol{R}&0\\0&{}_0^i\boldsymbol{R}\end{pmatrix}\boldsymbol{J}(\boldsymbol{\Phi})
$$

### 力域中的雅可比

笛卡尔力映射到关节上的力矩，不需要求解逆运动学

$$
\tau = J^T F
$$

- 是操作空间向关节空间的映射（与$\dot{x} = J \dot{\Phi}$是相反的）

!!! note "证明方法 - 虚功原理"
    以机器人在末端笛卡儿空间所做的功与在关节空间所做的功相等，即

    $$ 
    F^T \delta x = \tau^T \delta \Phi 
    $$
    
    > **注：力矩做功是力矩和角位移的积分**
    
    式中，$F$ 是末端作用于外部的 $6 \times 1$ 维笛卡儿力-力矩向量；$\delta x$ 是末端的 $6 \times 1$ 维无穷小笛卡儿位移向量；$\tau$ 是 $6 \times 1$ 维关节力矩向量；$\delta \Phi$ 是 $6 \times 1$ 维无穷小关节位移向量。
    
    由雅可比矩阵的定义有（速度空间的映射）
    
    $$ 
    \delta x = J \delta \Phi 
    $$


    $$ 
    F^T J \delta \Phi = \tau^T \delta \Phi 
    $$


    上式对所有的 $\delta \Phi$ 均成立，因此有
    
    $$ 
    F^T J = \tau^T 
    $$
    
    同取转置
    
    $$ 
    \tau = J^T F 
    $$

## 奇异性

### 奇异性理解

- **运动角度理解**：机械臂处在特定的关节位置组合（奇异位形）的时候，末端执行器会丢掉某个方向的自由度

> 完全伸直手臂之后，手无法沿着手臂方向移动

- **雅可比矩阵角度**：关节的运动速度乘以雅可比矩阵即得到 end effector 的运动速度。而 end effector 失去某个方向的自由度即意味着在机械臂到达那个 configuration 的瞬间，不管关节怎么运动，end effector 在这个方向的速度总为 0（雅可比矩阵的分量为 0）

- **从线性代数的角度来说**：此时的 J 矩阵有这样的特性：对所有任意向量 a，Ja 相乘得到向量 b，则所有向量 b 组成的线性空间维度将比正常情况下少至少一个自由度（**降秩**）

### 奇异位形求解

奇异位形：无法通过关节变量速度实现要求的末端速度

对于一般机器人，奇异位形为令雅可比矩阵 $J$ 不满秩的 $\Phi$ 值所构成的位形，（$N$是机器人关节数目）时

$$
\text{rank}(J(\Phi) < \min(m, N)
$$

不同情况下的奇异点的判断条件为：

1. **无冗余 ($m = N$)**: 在此 $\Phi$ 时 $J(\Phi)$ 不可逆，即 $\det(J(\Phi)) = 0$。
2. **冗余 ($m < N$)**: 在此 $\Phi$ 时 $J(\Phi)$ 不行满秩，即 $\text{rank}(J(\Phi)) < m$。（可能有最小范数解）
3. **欠驱动 ($m > N$)**: 在此 $\Phi$ 时 $J(\Phi)$ 不列满秩，即 $\text{rank}(J(\Phi)) < N$。（可能有最小二乘解）

- 奇异位形是机器人的构型决定的，是机器人的固有特征
- 接近奇异位形的时候，存在机器人末端在工作空间中的微小速度导致关节空间产生过大速度：从线性方程的角度看，当机器人接近 Singularity 时，雅可比矩阵也越来越“病态”（ill-conditioned），很小的 dx 可能求得很大的 dq，方程对数值误差也更加敏感；而当机器人处于 Singularity 时，线性方程可能无解、也可能有无数多个解。

**边界奇异性**: 工作空间边界的奇异位形。出现在机器人完全展开或者收回使得末端执行器处于或非常接近工作空间边界的情况。

**内点奇异性**: 工作空间内部的奇异位形。出现在远离工作空间的边界，通常是由于两个或两个以上的关节轴线共线引起的。

### 可操作度

!!! note "二次型与椭圆"

    二次型对应椭球体。 椭球的轴沿着$A$的特征向量，半长轴长度是$A$特征值倒数的开方


    **椭圆的标准方程：** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$。其中，椭圆的长轴长度为 $2a$，短轴长度为 $2b$。

    **矩阵形式：**

    $$
    \begin{bmatrix} x \\ y \end{bmatrix}^T \begin{bmatrix} \frac{1}{a^2} & 0 \\ 0 & \frac{1}{b^2} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = x^T A x = 1
    $$


    **特征值与特征向量：**

    矩阵 $A$ 的特征值为：$\lambda_1 = \frac{1}{a^2}, \quad \lambda_2 = \frac{1}{b^2}$，特征值则表示了半长轴和半短轴长度平方的倒数。 


    对应的归一化特征向量为：$\mu_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \mu_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$，表示了椭圆的长轴和短轴的方向

假设机器人有 $N$ 个关节，末端速度空间的维数为 $m$，要求 $N \geq m$，则 $m \times N$ 维雅可比矩阵 $J$ 的奇异值分解为：

$$
J = U \Sigma V^T
$$

其中，$\Sigma$ 是 $m \times N$ 维矩阵，其主对角线外的元素均为零，主对角线上的每个元素为 $J$ 的奇异值 $\sigma_i = \sqrt{\lambda_i(JJ^T)} (i = 1, \cdots, m)$，且 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_m \geq 0$；$U$ 和 $V$ 分别为 $m$ 维和 $N$ 维正交矩阵，且 $U$ 由矩阵 $JJ^T$ 的特征向量 $u_i (i = 1, \cdots, m)$ 张成，$V$ 由矩阵 $J^TJ$ 的特征向量 $v_i (i = 1, \cdots, N)$ 张成。由此得到：

$$
v_e^T (J J^T)^{-1} v_e = (U^T v_e)^T \Sigma^{-2} (U^T v_e)
$$

此时，$\Sigma^{-2} = \text{diag}(\sigma_1^{-2}, \sigma_2^{-2}, \cdots, \sigma_m^{-2})$ 为 $m$ 维对角矩阵。记 $\alpha = U^T v_e$

$$
v_e^T (J J^T)^{-1} v_e - \alpha^T \Sigma^{-2} \alpha = \sum_{i=1}^m \frac{\alpha_i^2}{\sigma_i^2} \leq 1
$$

是一个标准的椭球体方程，表明机器人此位形的可操作椭球体的轴由向量 $\sigma_i u_i$ 给出。

机器人关节速度取单位速度时，可操作椭球体轴的长度越大，在该轴方向上，所得到的末端速度可以越大，表明在该方向上运动能力越强；反之，轴的长度越小，在该轴方向上，所得到的末端速度被限制得越小，表明在该方向上运动能力越弱。因此，机器人位形的可操作椭球体描述了机器人改变末端位姿的能力。

定义可操作度，用来衡量机器人位形与奇异位形之间的距离

$$
\kappa(\boldsymbol{\Phi})=\sigma_1\sigma_2\cdots\sigma_m=\sqrt{\det(\boldsymbol{J}(\boldsymbol{\Phi})\boldsymbol{J}^\mathrm{T}(\boldsymbol{\Phi}))}
$$

特别的，当雅可比矩阵可逆的时候 $\kappa(\boldsymbol{\Phi})=\mid\det(\boldsymbol{J}(\boldsymbol{\Phi}))\mid$

![image](https://img.philfan.cn/Robotics__Model__assets__4-Mechanics.assets__20250314222953648.webp)

## 冗余

“又矮又胖的矩阵”：关节自由度特别多的时候

这意味着，可以实现关节空间运动，而末端执行器不动，即

$$
\exists \dot{q} \neq 0, \quad J \dot{q} = 0
$$

> 指尖保持不动，只动手肘手腕

假如 J 是一个方阵，那么$J\dot{q}=0$有非零解的充分必要条件是 J 是一个奇异矩阵——也就是说，如果没有冗余自由度，一个机械臂关节运动而 end effector 不动的情况只有在它处于 singularity 时才能出现。

但是，如果 J 是一个矮胖矩阵，那么$J\dot{q}=0$必然有无数个非零解，这些解组成的空间即称为"零空间"（nullspace）。

## 题型

### 基础公式记忆

**z-y-x 欧拉角** 公式

$$
\begin{align}
R_{z,y,x}(\alpha,\beta,\gamma) = \begin{pmatrix}
c\alpha c\beta & c\alpha s\beta s\gamma-s\alpha c\gamma & c\alpha s\beta c\gamma+s\alpha s\gamma \\
s\alpha c\beta & s\alpha s\beta s\gamma+c\alpha c\gamma & s\alpha s\beta c\gamma-c\alpha s\gamma \\
-s\beta & c\beta s\gamma & c\beta c\gamma
\end{pmatrix}
\end{align}
$$

MDH 建模下，坐标系**齐次变换矩阵**

$^{i-1}_i \!T$ 表示坐标系 $\{i-1\}$ 到坐标系 $\{i\}$ 的变换矩阵，i 从 1 开始

$$
^{i-1}_i \!T = \begin{pmatrix}
\cos \theta_i & -\sin \theta_i & 0 & a_{i-1} \\
\sin \theta_i \cos \alpha_{i-1} & \cos \theta_i \cos \alpha_{i-1} & -\sin \alpha_{i-1} & -\sin \alpha_{i-1} d_i \\
\sin \theta_i \sin \alpha_{i-1} & \cos \theta_i \sin \alpha_{i-1} & \cos \alpha_{i-1} & \cos \alpha_{i-1} d_i \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

> 使用基向量表出的方法快速列写/检查矩阵写的对不对

几种方法对比

!!! note "推荐方法"
    - 首选运动学方程微分方法，计算$J_v$
    - 然后列写各个坐标系下$^{0} z$轴向量，计算$J_\omega$；平动关节直接为 0
    - 这两个方法只要 DH 参数表和${}^0_NT$计算正确即可

| 方法 | 计算量 | 需要求解 | 注意点 |
| -------------------- | ---------------------------------- | ----------------------------- | ---------------------------------------------------------------------- |
| **运动学方程微分** | 中等 | 正运动学方程 $^0_nT$ | 确保正确求导，注意矩阵维度一致性 |
| **向量积构造法** | 较低 | 各关节轴的单位向量 $\hat{Z}_i$ 和原点位置 $O_i$ | $\hat{Z}_i$ 和 $O_i$ 必须在世界坐标系下表示，注意叉乘方向 |
| **速度传递** | 较高 | 各连杆的旋转矩阵 $^{i+1}_iR$ 和位置向量 $^iP_{i+1}$ | 确保旋转矩阵和位置向量的正确性，注意旋转矩阵的转置操作 |
| **力传递** | 较高 | 各连杆的旋转矩阵 $^{i+1}_iR$ 和位置向量 $^iP_{i+1}$ | 求解的雅可比需要转置，需要乘 R 转回全局坐标系下 |

### 求雅可比矩阵 - 运动学方程微分 $J_v$

由正运动学，求解 $^0_nT$

$$
^0_nT = \begin{pmatrix} ^0_nR & ^0_nP \\ 0 & 1 \end{pmatrix}
$$

对上式求导，得到

$$
P' = \frac{d P}{d t} = J(\theta) \dot{\theta}
$$

即可得到雅可比矩阵

### 求雅可比矩阵 - 向量积构造法 $J_v$ $J_\omega$

计算每一个关节对于连杆 N 速度的贡献

![image](https://img.philfan.cn/Robotics__Model__assets__4-Mechanics.assets__20250314234911486.webp)

#### 平动型关节

若第 $i$ 个关节为平动型关节，则：

$$
v_N^{(i)} = d_i \hat{Z}_i \quad \omega_N^{(i)} = 0
$$

#### 转动型关节

若第 $i$ 个关节为转动型关节，则：$v_N^{(i)} = \dot{\theta}_i \hat{Z}_i \times (O_N - O_i) \quad \omega_N^{(i)} = \dot{\theta}_i \hat{Z}_i$

> 为什么要叉乘：**类似于“力矩”中“矩”的概念**

!!! note "$O_i$是坐标系${i}$的原点位置，$\hat{Z}_i$是**转轴单位向量**"
    这里要特别注意，$\hat{Z}_i$需要在世界坐标系下表出，且需要是**单位向量**

在三维空间里，角速度定义为一个指向旋转轴的向量，其方向由右手定则确定。

每个旋转关节都是绕自身的 z 轴旋转的，所以当一个旋转关节转速为$\omega$时，它所 contribute 的 end effector 的角速度向量以这个旋转关节本身的坐标系为参照系必然为$[0, 0, \omega]$。

但是由于基础雅可比矩阵是以 frame{0}为参照系的，所以需要将$[0, 0, \omega]$转换到 frame{0}下。

### 求雅可比矩阵 - 速度传递 - 向外迭代法

知道了这样的变换方法，就可以从连杆 0，变换到连杆 N，一个个地计算速度和角速度

向外迭代法是计算机器人几何雅可比矩阵的方法之一

#### 转动型关节求解

角速度：连杆 i+1 针对世界坐标系角速度在{i+1}坐标系的表示

$$
^{i+1}\!\omega_{i+1} = ^{i+1}_i\!R {^i\omega_i} + \dot{\theta}_{i+1} {}^{i+1}\!\hat{Z}_{i+1}\\
$$

> 其中，$\hat{Z}_{i+1}$ 是轴 $i+1$在 ${i+1}$ 中的表示；${\theta}_{i+1}$ 是转动型关节 $i+1$ 的关节转速。

线速度：连杆 i+1 针对世界坐标系线速度在{i+1}坐标系的表示

$$
{}^{i+1}\!v_{i+1} = {^{i+1}_iR} (^iv_i + ^i\omega_i \times {^iP_{i+1}})
$$

> 连杆的长度隐含在了 $^iP_{i+1}$ 叉乘项当中

!!! attention "公式不要记错，这里要注意 $^{i+1}_i\!R$ 需要使用 $(^{i}_{i+1}\!R)^T$ 进行求解"

#### 平动型关节求解

角速度：不变

$$
^{i+1}\omega_{i+1} = _i^{i+1}R {^i\omega_i}
$$

线速度：要加一个在轴线上的速度

$$
^{i+1}v_{i+1} = _i^{i+1}R (^iv_i + ^i\omega_i \times ^iP_{i+1}) + \dot{d_{i+1}} \hat{Z}_{i+1}
$$

### 求雅可比矩阵 - 力传递 - 向内迭代法

$$
\begin{align*}
^i f_i = ^{i}_{i+1}R ^{i+1} f_{i+1}\\
^i n_i = ^{i}_{i+1}R^{i+1} n_{i+1} + ^{i}P_{i+1} \times ^{i}f_{i}
\end{align*}
$$

转动型关节需要考虑施加多少力矩，平动型关节需要考虑施加多少力。需要对 (力，力矩) 向量进行正交分解

**转动型关节$i$**

$$
\tau_i = |n_i| \cos \theta = |n_i| |\hat{z}_i| \cos \theta = n_i^{\mathrm{T}} \hat{z}_i
$$

**平动型关节$i$**

$$
\tau_i = f_i^{\mathrm{T}} \hat{z}_i
$$

将式子写成矩阵的形式，即可得到

$$
\tau = J^T F
$$

取转置，得到 $\boldsymbol{^iJ}$，是末端坐标系下的雅可比矩阵

但是要注意到，这里的雅可比矩阵需要转到全局下

$$
\boldsymbol{J}(\boldsymbol{\Phi})= ^0_i\boldsymbol{R} \boldsymbol{^iJ}(\boldsymbol{\Phi})
$$

### 末端给出力/力矩，求解关节力矩

写出完整的$6\times n$的雅可比矩阵

列写末端$\begin{pmatrix}f_x&f_y&f_z&n_x&n_y&n_z\end{pmatrix}^T$

解方程，得到关节力矩

$$
\tau=J^T F
$$

## 例题

### 5-3

若$R\in\text{SO}(3)$，$a\in\mathbb{R}^3$，$B\in\mathbb{R}^{3\times3}$，证明$R(a^\wedge B)=(Ra)^\wedge(RB)$

证明：证明很多，提供其中一种：

因为$\det(x,a,b)=\langle x,a\times b\rangle$，$\forall x\in\mathbb{R}^3$

令$R\in\text{RO}(3)$，利用性质$R^T=R^{-1}$可以得到
$$\langle x,R(a\times b)\rangle=\langle R^Tx,a\times b\rangle=\langle R^{-1}x,a\times b\rangle=\det(R^{-1},a,b)$$
由于$\det(R)=1$，可以得到：

$$
=\det(R)\det(R^{-1}x,a,b)=\det(x,Ra,Rb)=\langle x,Ra\times Rb\rangle
$$

最后由于$\langle x,R(a\times b)\rangle=\langle x,Ra\times Rb\rangle$对于所有$x\in\mathbb{R}^3$成立，因此

$$
R(a\times b)=Ra\times Rb，\text{即}R(a^\wedge b)=(Ra)^\wedge(Rb)
$$

由$B\in\mathbb{R}^{3\times3}$，令$B=\begin{pmatrix}b_1&b_2&b_3\end{pmatrix}$，则

$$
\begin{aligned}R(a^\wedge B)&=R\left(a^\wedge\begin{pmatrix}b_1&b_2&b_3\end{pmatrix}\right)=R\left(\begin{pmatrix}a^\wedge b_1&a^\wedge b_2&a^\wedge b_3\end{pmatrix}\right)\\&=\begin{pmatrix}R(a^\wedge b_1)&R(a^\wedge b_2)&R(a^\wedge b_3)\end{pmatrix}=\begin{pmatrix}Ra^\wedge Rb_1&Ra^\wedge Rb_2&Ra^\wedge Rb_3\end{pmatrix}\\&=Ra^\wedge\begin{pmatrix}Rb_1&Rb_2&Rb_3\end{pmatrix}=Ra^\wedge R\begin{pmatrix}b_1&b_2&b_3\end{pmatrix}=Ra^\wedge RB\end{aligned}
$$

### 5-4

!!! note "注意这个角速率的公式"

角速率的关系为$\omega=B(\Psi)\dot{\Psi}$，求出$B(\Psi)$的具体表达式

$$\begin{aligned}
&\Psi=\begin{bmatrix}\alpha\\\beta\\\gamma\end{bmatrix},\dot{\Psi}=\begin{bmatrix}\dot{\alpha}\\\dot{\beta}\\\dot{\gamma}\end{bmatrix},R=\begin{bmatrix}c\alpha c\beta&c\alpha s\beta s\gamma-s\alpha c\gamma&c\alpha s\beta c\gamma+s\alpha s\gamma\\s\alpha s\beta&s\alpha s\beta s\gamma+c\alpha c\gamma&s\alpha s\beta c\gamma-c\alpha s\gamma\\-s\beta&c\beta s\gamma&c\beta c\gamma\end{bmatrix},\dot{R}R^T=\begin{bmatrix}0&-Q_Z&Q_Y\\\Omega_Z&0&-Q_X\\-\Omega_Y&\Omega_X&0\end{bmatrix}\\
\end{aligned}
$$

$$
\begin{aligned}
\Omega_{X}&=\dot{r}_{31}r_{21}+\dot{r}_{32}r_{22}+\dot{r}_{33}r_{33}\\&=-s\alpha c\beta c\beta\dot{\beta}+(s\alpha s\beta s\gamma+c\alpha c\gamma)\left(c\beta c\gamma\dot{\gamma}-s\beta s\gamma\dot{\beta}\right)+(s\alpha s\beta c\gamma-c\alpha s\gamma)\left(-s\beta c\gamma\dot{\beta}-c\beta s\gamma\dot{\gamma}\right)=-s\alpha c\beta c\beta\dot{\beta}-s\alpha s\beta s\beta\dot{\beta}+c\alpha c\beta\dot{\gamma}=-s\alpha\dot{\beta}+c\alpha c\beta\dot{\gamma}\\
\Omega_Y&=\dot{r}_{11}r_{31}+\dot{r}_{12}r_{32}+\dot{r}_{13}r_{33}=c\alpha\dot{\beta}+c\beta s\alpha\dot{\gamma}\\
\Omega_Z&=\dot{r}_{21}r_{11}+\dot{r}_{22}r_{12}+\dot{r}_{23}r_{13}=\dot{\alpha}-s\beta\dot{\gamma}\\
\end{aligned}
$$

$$
B(\Psi)=\begin{bmatrix}0&-s\alpha&c\alpha c\beta\\0&c\alpha&c\beta s\alpha\\1&0&-s\beta\end{bmatrix}
$$
