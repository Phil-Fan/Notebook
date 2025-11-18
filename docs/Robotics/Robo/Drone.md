# 空中机器人

!!! note "课程简介"
 === "课程要求"
        - 试验课程报告 40%
        - 期末考试 30%
        - MOOC 20%
        - 平时点到 10%
 === "回忆卷"
        [控院《空中机器人》2022-2023春 期末回忆卷 - CC98论坛](https://www.cc98.org/topic/5587505)<br>
        [空中机器人 2023-2024春 回忆卷 - CC98论坛](https://www.cc98.org/topic/5870695)<br>
        [空中机器人期末考试 - CC98论坛](http://www-cc98-org/topic/4961864)

 === "课程资料"
  [空中机器人_高飞_智云课堂 (zju.edu.cn)](https://classroom.zju.edu.cn/coursedetail?course_id=59917&tenant_code=112)

## 概论

期望有自制和自主能力，遥控飞机也算的

### Lab

MIT、ETH、ZJU、HKUST

### 分类

!!! note "关于“飞翔”"
 代达罗斯和伊卡洛斯
 ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20241102205126.webp)

#### 固定翼

#### 旋翼

操控简单、可靠性高、模块易替换

- 旋翼：对称分布集体前后左右
- 支架
- 电机：对称安装
- 飞控：支架中间控制计算机和外部设备

[科普｜直升机是靠旋翼转速控制升降的？原来我们的认知是错的](https://m.thepaper.cn/newsDetail_forward_13664241)
[【科普】十分钟就能读懂的直升机飞行原理，值得收藏的干货\_网易订阅](https://www.163.com/dy/article/D52IUJ1G0511A347.html)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__857.gif)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__866.gif)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__881.gif)

旋翼的升力

飞机，直升机和旋翼机三种起飞原理是不同的。飞机依靠助跑来提供速度以达到足够的升力，而直升机依靠旋翼的控制旋转在不进行助跑的条件下实现垂直升降，直升机的旋转是动力系统提供的，而旋翼旋转会产生向上的升力和空气给旋翼的反作用力矩，在设计中需要提供平衡旋翼反作用扭矩的方法，通常有单旋翼加尾桨式（尾桨通常是垂直安装）、双旋翼纵列式（旋转方向相反以抵消反作用扭矩）等；而旋翼机则介于飞机和直升机之间，旋翼机的旋翼不与动力系统相连，由飞行过程中的前方气流吹动旋翼旋转产生升力（像大风车一样），即旋翼为自转式，传递到机身上的扭矩很小，无需专门抵消。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240914105319.webp)

!!! note "四旋翼有十字和 x 两种，采用正反桨，对侧一致"
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240914104903.webp)

#### 扑翼型

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911134640.webp)

#### 气囊型

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911134634.webp)

!!! note "为什么气囊型戛然而止？"
    1. 载重量和体积效益十分不经济。
    2. 储存，运输，制造大量轻于空气的气体存在十足的危险性。
    3. 航速慢，十分容易受自然条件影响

### 名词解释

#### 速度表示

- 真空速 TAS：飞机相对于空气的运动速度，是考虑了空气密度影响的速度
- 指示空速 IAS：折算到海平面高度的真空速，忽略了空气密度的变化，又称表速，是空速管测出的速度，也是表征飞机升力的速度
- 地速 飞机相对于地面运动速度的水平分量，是真空速与风速水平分量的矢量和
- 垂直速度 飞机相对于地面运动速度的垂直分量，即升降速度

#### 马赫数

马赫是表示速度的量词。一马赫即一倍音速 音波可以在固体、液体或是气体介质中传播，介质密度愈大，则音速愈快 所以马赫的大小不是固定的

马赫数小于 1 者为亚音速，马赫数大于 5 左右为超高音速

马赫锥
超音速飞行时，激波后的空气压力和温度急剧下降，导致水汽冷凝，形成雾化现象
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20241102205256.webp)

#### 激波

飞机飞行--> 对空气产生扰动，扰动以扰动波的形式 以音速传播 积聚

#### 飞行包线

以速度作为横坐标，以高度作为纵坐标，把各个高度下的速度上限和下限画出来，这样就构成了一条边界线，称为飞行包线，飞机只能在这个线确定的范围内飞行。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911135732.webp)

#### 气动布局

飞机外部总体形态布局与位置安排称作气动布局

=== "常规布局"
    特点是有主机翼和水平尾翼，大的主机翼在前，小机翼也就是水平尾翼在后，有一个或者两个垂直尾翼
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911135816.webp)
=== "变后掠翼布局”
    主翼的后掠角度可以改变，高速飞行可以加大后掠角，相当于飞鸟收起翅膀，低速飞行时减小后掠角，展开翅膀。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911135845.webp)
=== "无尾布局"
    没有水平尾翼，无尾布局大大减少了空气阻力，无尾布局的缺点是低速性能不好，这影响到飞机的低速机动性能和起降能力。另外无尾布局因为只能依靠主翼控制飞行，所以稳定性也不理想。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20241102205328.webp)
=== "鸭式布局"
    这种气动布局其实就是无尾布局加个鸭翼。有了这个鸭翼，无尾布局的缺点得到明显改善，高速飞行时更加稳定，起降距离明显缩短，甚至机动性能比常规布局更加出色。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20241102205428.webp)
=== "飞翼布局"
    只有飞机翅膀的布局，看上去只有机翼，没有机身，机身和机翼融为一体。
    无疑这种布局是空气动力效率最高的布局，因为所有机身结构都是机翼，都是用
    于产生升力，而且最大程度低降低了阻力。空气阻力最小所以雷达波反射自然也
    是最小，所以飞翼布局是隐身性能最好的气动布局。飞翼布局的最大缺陷是操控
    性能极差，完全依赖电子传感控制机翼和发动机的矢量推力。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20241102205518.webp)

## 动态模型

### 坐标系

=== "惯性参考系"
    $O_g$为地面任意点，$O_g x_g$ 为水平面任意方向，$O_g z_g$垂直地面指向地心，xyz轴右手坐标系
=== "地面坐标系"
    常用于指示飞机的方位近距离导航和航迹控制
=== "地球中心坐标系 ECEF"
    $ECEF$ 坐标系与地球固联且随着地球转动。图中 $O$ 即为坐标原点，位置在地球质心 。
    $X$ 轴通过格林尼治线（0度经线）和赤道线的交点，正方向为原点指向交点方向。$Z$ 轴通过原点指向北极。$Y$ 轴与 $X$,$Z$轴构成右手坐标系。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911141806.webp)
=== "WGS84 坐标系"
    WGS84 坐标系的 X 轴指向 BIH(国际时间服务机构)1984.和协议地球极(CTP)赤道的交点。
    Z 轴指向CTP方向。 Y轴与X、Z轴构成右手坐标系。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911142242.webp)
=== "NED 坐标系"
    NED 坐标系是在导航计算时使用的坐标系，向量分别指向北，东，地，因此 NED 坐标系也经常称为**北东地坐标系**![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240918134709.webp)
=== "机体坐标系"
    原点在飞行器重心处 $X$ 轴指向飞行器机头前进方向,$Y$ 轴由原点指向飞行器右侧,$Z$ 轴方向根据 $X$,$Y$轴由右手法则确定。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20241224104346.webp)

!!! note "为什么有了 GPS 输出的海拔高度，我们还是要用气压计等其它设备来辅助定高呢？"
    GPS地貌不精确；
    但是传感器误差仍是实机实验的难点之一

### 坐标变换（详见机器人建模与控制）

常见飞行器可以抽象为 一个刚体。描述任意时刻的空间运动需要
六个自由度：三个质心运动和三个角运动。

!!! note "角运动"
    **Roll:翻滚；Pitch:俯仰；Yaw:偏航**

    一个比较容易的记法是根据字母的排列顺序 PRY 分别对应 XYZ 轴进行旋转得到的角

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911140313.webp)

螺旋桨拉力模型
多旋翼的拉力与力矩模型
多旋翼空中机器人运动模型

!!! note "扭矩和力矩"
    [什么叫做扭矩？ - 知乎](https://www.zhihu.com/question/27154686)
    杠杆定理告诉我们，要给一个物体施加某个大小的旋转力，可以在离轴心较近的位置（小半径）施加较大的力，也可以在离轴心较远的位置（大半径）施以较小的力。只要力和力臂的乘积相同，二者的效果是相等的。<br>
    反过来也一样，对于同一个旋转力，不同位置（半径/力臂）表现出的力大小不同，只有力与力臂的乘积是始终不变的。<br>
    牛·米中间的 $\cdot$（有时被省略）表示乘号 $\times$。在离旋转物体轴心1米半径处，施以1牛顿大小的力，作用于这个物体的旋转力即为1牛·米；反过来，在1牛·米的旋转力作用下，离旋转轴心1米半径处，力大小为1牛顿。
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240911151007.webp)

## ⚙️控制

=== "遥控飞行（Remote Control Flying）"
    航向、速度、高度等参数由地面操作人员通过通信数据链路遥控控制
=== "程控飞行（Autopilot Flying）"
    航向、速度、高度等参数根据预先制定的规划航线由机载计算机控制系统计算获得并实施控制
=== "自主飞行（Autonomous Flying）"
    机载计算机控制系统能够感知环境的变化自动进行实时路径规划，并进行相应的姿态、航向、速度、高度等参数控制

!!! note "3 个重要因素"
    **桨叶直径** ：桨叶直径增大，一方面增加了桨叶面积，另一方面增大了桨尖的切向速度，增加了桨叶的空气动力。直升机一般旋翼少，桨叶直径就会很大，会远超飞机机体的覆盖范围。多旋翼旋翼数量 4 个起步（3 个的也有），桨叶直径就可以做的比较小；

    **桨叶迎角** ：桨叶迎角增加，增加桨叶的迎风面积，从而增加桨叶的空气动力；
    
    **桨速** ：桨速自然是越大，越能提供更强的升力；

■ 垂直升降

这个很好理解，当飞机需要升高高度时，四个螺旋桨同时加速旋转，升力加大，飞机上升。当飞机需要降低高度时，同理，四个螺旋桨会同时降低转速，飞机下降。

■原地旋转： **核心是反扭矩**

当多旋翼飞机的各个电机转速相同时，电机产生的反扭力会互相抵消，飞机不会发生转动。

但是当需要飞机原地旋转时，我们就可以利用这种反扭矩，M2、M4 两个顺时针旋转的电机转速增加，M1、M3 号两个逆时针旋转的电机转速降低，由于反扭矩影响，飞机就会产生逆时针方向的旋转。同时由于是“X”型结构对侧的电机同时增加或者降低转速，也保证了飞机的平衡。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240914105652.webp)

■ 水平移动：垂直方向平衡，水平方向力指向运动方向

以四旋翼为例，当需要按照三角箭头方向前进时，M3、M4 电机螺旋桨会提高转速，同时 M1、M2 电机螺旋桨降低转速，由于飞机后部的升力大于飞机前部，飞机的姿态会向前倾斜。这时螺旋桨产生的升力除了在竖直方向上抵消飞机重力外，还在水平方向上有一个分力，这个分力就让飞机有了水平方向上的加速度，飞机也因而能向前飞行。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240914105702.webp)

向其他方向的移动，实现方法亦然。

!!! tip "奇数旋翼也是可以控制的"

### 平面四旋翼模型

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone.assets__20240925150048.webp)

$u_1$ 表示推力，$u_2$ 表示力矩。

- Y:$\sum F_y = -u_1 \sin(\phi) = m\ddot{y}$
- Z：$\sum F_z = -mg + u_1 \cos(\phi) = m\ddot{z}$
- 力矩：$M = u_2 = I_{xx}\ddot{\phi}$

**线性化**

- 平衡悬停态： $(\phi_0 \sim 0, \theta_0 \sim 0, u_{1,0} \sim mg)$

**牛顿方程**：
$$
m\ddot{p} = \begin{bmatrix} 0 \\ 0 \\ -mg \end{bmatrix} + R \begin{bmatrix} 0 \\ 0 \\ F_1 + F_2 + F_3 + F_4 \end{bmatrix}
$$

$$
其中 R = \begin{bmatrix} c\psi c\theta - s\phi s\psi s\theta & -c\theta s\psi & c\psi s\theta + c\theta s\phi s\psi \\ c\theta s\psi + c\psi s\phi s\theta & c\phi c\psi & s\psi s\theta - c\theta c\phi s\phi \\ -c\theta s\theta & s\phi & c\theta c\phi \end{bmatrix}
$$

$$
在小角度近似的情况下，得到\begin{cases}
\ddot{p}_1 = \ddot{x} = g(\theta c\psi + \phi s\psi )\\
\ddot{p}_2 = \ddot{y} = g(\theta s\psi - \phi c\psi) \\
\ddot{p}_3 = \ddot{z} = -g + \frac{u_1}{m}
\end{cases}
$$

!!! note "线性化的方法"
    角度近似:
    $\sin \theta \approx \theta,\cos \theta \approx 1,when \quad \theta \rightarrow 0$

**欧拉角微分：**
$$
\begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix} = \begin{bmatrix} c\theta & 0 & -c\phi s\theta \\ 0 & 1 & s\phi \\ s\theta & 0 & c\phi s\theta \end{bmatrix} \begin{bmatrix} \dot{\phi} \\ \dot{\theta} \\ \dot{\psi} \end{bmatrix}
$$

线性化后

$$
\begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix} = \begin{bmatrix} \dot{\phi} \\ \dot{\theta} \\ \dot{\psi} \end{bmatrix}
$$

**欧拉方程**：

$$
I\cdot \begin{bmatrix} \ddot{\phi} \\ \ddot{\theta} \\ \ddot{\psi} \end{bmatrix} + \begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix} \times I \cdot \begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix} = \begin{bmatrix} l(F_2 - F_4) \\ l(F_3 - F_1) \\ M_1 - M_2 + M_3 - M_4 \end{bmatrix}
$$

### PID 控制

**位置控制**

$$
\ddot{p}_{i,c} = \ddot{p}_i^{des} + K_{d,i}(\dot{p}_i^{des} - \dot{p}_i) + K_{p,i}(p_i^{des} - p_i) \\
$$

- 由上述方程可以求出$p_{i,c}$
- 再带入牛顿方程的解的到预期的$\phi_c$、$\theta_c$和$u_1$
  - $\phi_c = \frac{1}{g}(\ddot{p}_{1,c}s\psi - \ddot{p}_{2,c}c\psi)$
  - $\theta_c = \frac{1}{g}(\ddot{p}_{1,c}c\psi + \ddot{p}_{2,c}s\psi)$
  - $u_1 = m(g + \ddot{p}_{3,c})$

!!! tip "注意：这些$\psi$是当前测量的 yaw，不是期望的 yaw"

- 鲁棒的东西往往简单

产生误差原因：模型 mismatch + 环境噪声
前馈：利用模型建模，相当于将初始值从 0 移动到某个值

### MPC 控制

!!! note "SLAM : Simultaneous Localization and Mapping"

- Localization: 定位
- Mapping: 建图

[四旋翼飞行器建模（一）— 动力学及运动学方程 - 知乎](https://zhuanlan.zhihu.com/p/349306054)
[Robotics:Aerial Robotics (空中机器人) (二) - 知乎](https://zhuanlan.zhihu.com/p/482780836)
[刚体动力学 - 牛顿欧拉方程（刚体旋转）\_刚体动力学方程-CSDN 博客](https://blog.csdn.net/subtitle_/article/details/133827121)
[【UAV】从单个螺旋桨到四旋翼无人机运动学分析\_无人机螺旋桨 升力-CSDN 博客](https://blog.csdn.net/weixin_36815313/article/details/121767869)
