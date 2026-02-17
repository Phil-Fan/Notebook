# 05 | 轨迹规划

为每个关节计算连续的运动轨迹，使末端执行器在空间中从点 A 移动到点 B

难点：

- 求解方程;公式理解
- 列写方程之后，检查未知数个数和方程个数是否匹配

| 特性 | 关节空间规划 | 笛卡尔空间规划 |
| --- | --- | --- |
| **定义** | 在关节空间中规划每个关节的运动轨迹，使末端执行器达到目标位置。 | 在笛卡尔空间中直接规划末端执行器的运动轨迹。 |
| **优点** | 计算简单，适合大多数机器人控制器。 | 轨迹直观，便于控制末端执行器的运动路径。 |
| **缺点** | 末端执行器的路径可能不直观，可能出现不必要的绕行。 | 计算复杂，可能需要逆运动学求解，增加计算负担。 |
| **适用场景** | 对路径形状要求不高的任务，例如点到点的运动。 | 对路径形状有严格要求的任务，例如绘图或焊接。 |
| **插值方法** | 直接对关节角度进行插值。 | 需要对末端位置或姿态进行插值，可能涉及旋转矩阵或四元数的处理。 |
| **运动平滑性** | 关节运动平滑，但末端执行器路径可能不平滑。 | 末端执行器路径平滑，但可能导致关节运动不平滑。 |

## 关节空间规划

任务描述：给定末端工具坐标系的位置和姿态，逆运动学求解出各个位姿对应的关节角，然后利用插值计算每个关节的运动轨迹。

| 方法 | 平滑性 | 计算复杂度 | 加速度连续性 | 适用场景 |
| --- | --- | --- | --- | --- |
| **线性插值** | 低（速度突变） | 低 | 不连续 | 简单、低速 |
| **抛物线过渡** | 中（速度连续） | 中 | 不连续 | 中等速度，允许加速度突变 |
| **分段三次多项式** | 高（速度/加速度连续） | 中高 | 连续 | 平滑加减速的中高速运动 |
| **五次多项式** | 极高（全局连续） | 高 | 连续 | 高精度、高动态性能需求 |

### 线性插值

线性插值是一种简单的轨迹规划方法，通过在起点和终点之间进行线性插值来计算中间点的位置。其公式如下：

$$
\phi(t) = \phi_0 + (\phi_f - \phi_0) \cdot \frac{t}{T}
$$

其中：

- $\phi_0$ 为起始位置，
- $\phi_f$ 为终止位置，
- $t$ 为当前时间，
- $T$ 为总时间。

线性插值的优点是计算简单，适用于对路径平滑性要求不高的场景，但其缺点是速度和加速度可能会出现突变。

```python title="linear_interpolation"
import numpy as np

def linear_interpolation(start, end, t, duration):
    """
    线性插值轨迹规划
    :param start: 起始点坐标
    :param end: 终点坐标
    :param t: 当前时间
    :param duration: 总时长
    :return: 当前时刻的位置
    """
    if t < duration:
        x_array = start * (1 - t / duration) + end * (t / duration)
        x_angles = inverse_kinematics(x_array)
    else:
        x_angles = inverse_kinematics(end)
    return x_angles
```

### 三次多项式：规划位置&速度

$$
\phi(t) = a_0 + a_1t + a_2t^2 + a_3t^3
$$

这里有四个未知数，所以需要四个约束条件，选择初始位置、初始速度、终止位置、终止速度（一般都是给定的）

用给定的数据求解方程，得到四个系数，然后就可以得到轨迹方程。

!!! note "多项式规划的思想可以用在指定导数的题目上面，不一定是轨迹的规划"

### 三次 + 中间点

指定中间点速度

每一段都使用三次多项式进行规划。

- 前后两段斜率符号相同：速度取平均值
- 前后两段斜率符号不同：速度取 0

不指定中间点速度

$$
\phi_{ij}(t) = a_0 + a_1t + a_2t^2 + a_3t^3\\
\phi_{jk}(t) = b_0 + b_1t + b_2t^2 + b_3t^3
$$

有八个未知数，所以需要八个约束条件，一种方式是

- 位置约束：第一段起点终点，第二段起点终点
- 速度约束：第一段起点速度，第二段终点速度，中间点速度相等
- 加速度联系约束：中间点加速度相等

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250416154011.webp)

```python title="三次 + 两个中间点" linenums="1" hl_lines="7"
clc;clear;
%定义时间节点和位置（包含起点、两个中间点、终点）
t_points=[0,1,2,3];%时间参数
y_points=[0,1,-1,2];%Y坐标：起点(0),中间点1(1),中间点2(-1),终点(2)

%拟合三次多项式（4个点需要3次多项式）
poly_y=polyfit(t_points,y_points,3);%Y方向多项式系数

%生成密集插值点
t_dense=linspace(0,3,100);
y_traj=polyval(poly_y,t_dense);%Y轨迹

%绘制结果
figure;
plot(t_dense,y_traj,'b-','LineWidth',1.5);
hold on;
plot(t_points,y_points,'ro','MarkerSize',8,'MarkerFaceColor','r');
xlabel('t');
ylabel('y');
title('多项式轨迹（含两个中间点）');
legend('多项式轨迹','控制点','Location','SouthEast');
grid on;
```

$\begin{cases}
a_{10} = \phi_0 \\
a_{11} = 0 \\
a_{12} = -\frac{3(\phi_0t_{\textrm{f2}}^2 + \phi_gt_{\textrm{f1}}^2 - \phi_vt_{\textrm{f1}}^2 - \phi_vt_{\textrm{f2}}^2 + 2\phi_0t_{\textrm{f1}}t_{\textrm{f2}} - 2\phi_vt_{\textrm{f1}}t_{\textrm{f2}})}{2t_{\textrm{f1}}^2t_{\textrm{f2}}(t_{\textrm{f1}} + t_{\textrm{f2}})} \\
a_{13} = \frac{\phi_0t_{\textrm{f2}}^2 + 3\phi_gt_{\textrm{f1}}^2 - 3\phi_vt_{\textrm{f1}}^2 - \phi_vt_{\textrm{f2}}^2 + 4\phi_0t_{\textrm{f1}}t_{\textrm{f2}} - 4\phi_vt_{\textrm{f1}}t_{\textrm{f2}}}{2t_{\textrm{f1}}^3t_{\textrm{f2}}(t_{\textrm{f1}} + t_{\textrm{f2}})} \\
a_{20} = \phi_v \\
a_{21} = -\frac{3(\phi_0t_{\textrm{f2}}^2 - \phi_gt_{\textrm{f1}}^2 + \phi_vt_{\textrm{f1}}^2 - \phi_vt_{\textrm{f2}}^2)}{2t_{\textrm{f1}}t_{\textrm{f2}}(t_{\textrm{f1}} + t_{\textrm{f2}})} \\
a_{22} = \frac{3(\phi_0t_{\textrm{f2}} + \phi_gt_{\textrm{f1}} - \phi_vt_{\textrm{f1}} - \phi_vt_{\textrm{f2}})}{t_{\textrm{f1}}t_{\textrm{f2}}(t_{\textrm{f1}} + t_{\textrm{f2}})} \\
a_{23} = -\frac{3\phi_0t_{\textrm{f2}}^2 + \phi_gt_{\textrm{f1}}^2 - \phi_vt_{\textrm{f1}}^2 - 3\phi_vt_{\textrm{f2}}^2 + 4\phi_gt_{\textrm{f1}}t_{\textrm{f2}} - 4\phi_vt_{\textrm{f1}}t_{\textrm{f2}}}{2t_{\textrm{f1}}t_{\textrm{f2}}^3(t_{\textrm{f1}} + t_{\textrm{f2}})}
\end{cases}$

### 五次多项式：规划位置&速度&加速度

思路比较类似。

$$
\phi(t) = a_0 + a_1t + a_2t^2 + a_3t^3 + a_4t^4 + a_5t^5
$$

六个未知数，就可以指定起点终点的位置、速度、加速度，然后求解方程。

```python title="quintic_polynomial"
def quintic_polynomial(start, end, t, duration):
    """
    五次多项式轨迹规划
    :param start: 起始点坐标
    :param end: 终点坐标
    :param t: 当前时间
    :param duration: 总时长
    :return: 当前时刻的位置
    """
    if t < duration:
        t_matrix = np.matrix([
            [0, 0, 0, 0, 0, 1],
            [duration ** 5, duration ** 4, duration ** 3, duration ** 2, duration, 1],
            [0, 0, 0, 0, 1, 0],
            [5 * duration ** 4, 4 * duration ** 3, 3 * duration ** 2, 2 * duration, 1, 0],
            [0, 0, 0, 2, 0, 0],
            [20 * duration ** 3, 12 * duration ** 2, 6 * duration, 2, 0, 0]
        ])
        x_matrix = np.matrix([[start[i], end[i], 0, 0, 0, 0] for i in range(len(start))]).T
        k_matrix = np.linalg.inv(t_matrix) @ x_matrix
        time_vector = np.matrix([t ** 5, t ** 4, t ** 3, t ** 2, t, 1]).T
        x = (k_matrix.T @ time_vector).T.A[0]
    else:
        x = end
    return x
```

### 直线段 + 抛物线过渡

两段形状相同的抛物线，中间连接的直线段是公切线

- 过渡段：抛物线段
- 直线段：顾名思义

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250325090130.webp)

给定：起点$\phi_0$、终点$\phi_{final}$、总时间$t_{final}$、加速度$\ddot\phi$
需要求解：**过渡时间（抛物线段）$t_b$**、速度（直线段）$k_b$

$$
t_b=\frac{\ddot{\phi}t_f-\sqrt{\ddot{\phi}^2t_f^2-4\ddot{\phi}(\phi_f-\phi_0)}}{2\ddot{\phi}}
$$

> 过渡段的时间间隔，二次方程求根公式求解。舍掉 + 号的解是因为$t_b < t_{f}$

$$
k_b=\ddot \phi \cdot t_b
$$

> 这里相当于初速度为 0 的平抛

```python title="parabolic_transition"
def parabolic_transition(start, end, t, duration):
    """
    抛物线过渡插值
    :param start: 起始点坐标
    :param end: 终点坐标
    :param t: 当前时间
    :param duration: 总时长
    :return: 当前时刻的位置
    """
    if t < duration:
        tx = t / duration
        if t < 0.5 * duration:
            tx = 2 * (tx ** 2)
        else:
            tx = 0.5 + 2 * (tx - 0.5) - 2 * (tx - 0.5) ** 2
        x_array = start * (1 - tx) + end * tx
        x_angles = inverse_kinematics(x_array)
    else:
        x_angles = inverse_kinematics(end)
    return x_angles
```

### 中间点 + 抛物线过渡

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250325091125.webp)

**给定：** 系列点$\phi_0, \phi_1,\dots,\phi_{final}$、各段时间$t_{dij}$、加速度$\ddot\phi$

**需要求解：** 各段的速度$k_{ij}$，以及过渡段的时间$t_{i}$，直线段的时间$t_{ij}$

#### 中间段计算

**过渡段 \( j \) 加速度**

$$
\ddot{\phi}_j = \text{SGN}(\dot{\phi}_{jk} - \dot{\phi}_{ij}) \cdot |\ddot{\phi}_j|
$$

**过渡段 \( j \) 时间间隔**

$$
t_j = \frac{\dot{\phi}_{jk} - \dot{\phi}_{ij}}{\ddot{\phi}_j}
$$

**直线段 \( jk \) 速度**

$$
\dot{\phi}_{jk} = \frac{\phi_k - \phi_j}{t_{djk}}
$$

**直线段时间 \( jk \) 间隔**

$$
t_{jk} = t_{djk} - \frac{1}{2} t_j - \frac{1}{2} t_k
$$

??? info "为什么是$\frac{1}{2}t$"
    这里可以联想到高中平抛运动当中的知识，速度角和位置角有一个$\frac{1}{2}$的关系。

    这个其实很容易推导：

    1. 速度角：$\tan \alpha = \frac{v_y}{v_x}=  \frac{g\cdot t}{v_0}$
    2. 位置角：$\tan \theta = \frac{y}{x} = \frac{\frac{1}{2}g\cdot t^2}{v_0\cdot t} = \frac{1}{2}\cdot \tan \alpha$

    也就是说，任意给定抛物线上的点，找到位移中点，连线即可得到速度方向
    
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250324205542.webp)

#### 起始段计算

过渡段 1 加速度

$$
\ddot{\phi}_1 = \text{SGN}(\phi_2 - \phi_1) \cdot |\ddot{\phi}_1|
$$

过渡段 1 时间间隔

根据切点速度相等列写方程

$$
\frac{\phi_2 - \phi_1}{t_{d12} - \frac{1}{2} t_1} = \ddot{\phi}_1 t_1
$$

求根公式解得：

$$
t_1 = t_{d12} - \sqrt{t_{d12}^2 - \frac{2(\phi_2 - \phi_1)}{\ddot{\phi}_1}}
$$

直线段 12 速度

$$
\dot{\phi}_{12} = \frac{\phi_2 - \phi_1}{t_{d12} - \frac{1}{2} t_1}
$$

直线段 12 时间间隔

$$
t_{12} = t_{d12} - t_1 - \frac{1}{2} t_2
$$

!!! note "这里因为抛物线对轨迹进行了圆滑处理，相当于先用直线连接起来，再用抛物线做一个圆角，所以并不能真正到达对应的点"
    解决方案：设置两个伪关节，连线经过给定点，则可以保证经过给定点

    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250325093447.webp)

## 笛卡尔空间规划

旋转矩阵和欧拉角不可以插值的原因：插值得到的 R 矩阵不一定属于 SO(3)

### 等效轴角插值

等效轴角的表示：$(\hat{k}_{x},\hat{k}_{y},\hat{k}_{z})^{\mathrm{T}}$为等效单位转动轴，$\theta$为绕该轴的转动量（这里单位为°）

$$
\boldsymbol{K}=\left(\begin{array}{c} k_{x} \\ k_{y} \\ k_{z} \end{array}\right)=\theta\left(\begin{array}{c} \hat{k}_{x} \\ \hat{k}_{y} \\ \hat{k}_{z} \end{array}\right)
$$

??? note "等效轴角表示并不唯一"

    $$
    \left(\begin{array}{c} k_{x} \\ k_{y} \\ k_{z} \end{array}\right)=\left(\begin{array}{c} 450° \\ 900° \\ 1350° \end{array}\right)/\sqrt{14}
    $$

    可以表示围绕空间$(1,2,3)^{\mathrm{T}}/\sqrt{14}$轴旋转450°获得的姿态，该最终姿态也等于绕同一轴旋转$450°+360°n$的结果，这里$n$为任意整数。

    并且注意等效轴角在$\theta =0$的时候无法表示，所以需要特殊处理。

对两个等效轴角表示的姿态

$$
\boldsymbol{K}_{0}=\left(\begin{array}{c} k_{0x} \\ k_{0y} \\ k_{0z} \end{array}\right) \text { 和 } \boldsymbol{K}_{1}=\left(\begin{array}{c} k_{1x} \\ k_{1y} \\ k_{1z} \end{array}\right)
$$

插值时，通常应该选择使得$\left\|\left(\begin{array}{c} k_{0x} \\ k_{0y} \\ k_{0z} \end{array}\right)-(\theta_{1}+360n)\left(\begin{array}{c} \hat{k}_{1x} \\ \hat{k}_{1y} \\ \hat{k}_{1z} \end{array}\right)\right\|$最小的$n$，然后对$\left(\begin{array}{c} k_{0x} \\ k_{0y} \\ k_{0z} \end{array}\right) \text { 和 } \left(\theta_{1}+360n\right)\left(\begin{array}{c} \hat{k}_{1x} \\ \hat{k}_{1y} \\ \hat{k}_{1z} \end{array}\right)$运用前面的多项式或带抛物线过渡直线段等插值方法。

#### 代码实现

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__rotation_animation.gif)

??? note "编程实现等效轴角的插值，并比较不同 n 下的结果"

    ```python title="等效轴角插值" 
    clc;clear;
    %主程序
    %初始姿态示例：绕z轴旋转0和π/2
    K0 = [0,0,0]; %初始姿态（无旋转）
    n_values = [-1,0,1]; %不同n值测试

    % 创建3个子图
    figure('Position',[100 100 1200 400]);
    subplot_handles = zeros(1,3);
    h_x = zeros(1,3);
    h_y = zeros(1,3);
    h_z = zeros(1,3);

    % 初始化3个子图
    for j = 1:length(n_values)
        subplot_handles(j) = subplot(1,3,j);
        hold on;
        grid on;
        axis equal;
        xlabel('X');
        ylabel('Y');
        zlabel('Z');
        view(3);
        xlim([-1.5,1.5]);
        ylim([-1.5,1.5]);
        zlim([-1.5,1.5]);
        title(['n=',num2str(n_values(j))]);
        
        % 初始化动画对象
        origin = [0;0;0];
        h_x(j) = quiver3(origin(1),origin(2),origin(3),1,0,0,'r','LineWidth',2);
        h_y(j) = quiver3(origin(1),origin(2),origin(3),0,1,0,'g','LineWidth',2);
        h_z(j) = quiver3(origin(1),origin(2),origin(3),0,0,1,'b','LineWidth',2);
    end

    % 创建动画
    while true % 无限循环
        for t = 0:0.01:1 % 减小步长从0.02到0.01使动画更慢
            for j = 1:length(n_values)
                n = n_values(j);
                K1 = (pi/2+2*pi*n)*[0,0,1];
                
                %三次多项式插值
                kt = K0+(3*t^2-2*t^3)*(K1-K0);
                R = rotation_vector_to_matrix(kt);
                
                %更新坐标轴
                x_axis = R*[1;0;0];
                y_axis = R*[0;1;0];
                z_axis = R*[0;0;1];
                
                set(h_x(j),'UData',x_axis(1),'VData',x_axis(2),'WData',x_axis(3));
                set(h_y(j),'UData',y_axis(1),'VData',y_axis(2),'WData',y_axis(3));
                set(h_z(j),'UData',z_axis(1),'VData',z_axis(2),'WData',z_axis(3));
            end
            drawnow;
            pause(0.02); % 添加暂停使动画更慢
        end
    end

    %旋转向量到旋转矩阵的函数
    function R = rotation_vector_to_matrix(k)
        % 这个函数实现了罗德里格斯公式，将旋转向量转换为旋转矩阵
        % 输入k是旋转向量，包含了旋转轴方向和旋转角度(角度在向量的模长中)
        
        % 1. 计算旋转角度theta(弧度)，即旋转向量的模长
        theta = norm(k);
        
        % 2. 如果旋转角度为0，直接返回单位矩阵(不旋转)
        if theta == 0
            R = eye(3);
            return;
        end
        
        % 3. 计算单位旋转轴向量ne
        ne = k/theta;  % 归一化得到单位向量
        
        % 4. 构造ne的叉积矩阵K，用于后续计算
        % K = [ne]_× 是ne的叉积矩阵，满足K*v = ne × v
        K = [0,-ne(3),ne(2);
            ne(3),0,-ne(1);
            -ne(2),ne(1),0];
            
        % 5. 使用罗德里格斯公式计算旋转矩阵
        % R = I + sin(θ)[k]_× + (1-cos(θ))[k]_×^2
        % 其中I是单位矩阵，[k]_×是叉积矩阵，θ是旋转角度
        R = eye(3) + sin(theta)*K + (1-cos(theta))*(K*K);
    end
    ```

### Slerp ｜ 四元数球面线性插值

!!! note "Key Assumption: $r_t$从$r_0$到$r_1$匀速旋转"

$$
r_t = k_0 r_0 + k_1 r_1
$$

$$
\begin{align*}
k_0 = \frac{\sin((1-t)\theta)}{\sin\theta} \quad k_1 = \frac{\sin(t\theta)}{\sin\theta},\theta = \cos^{-1}(r_0 \cdot r_1)
\end{align*}
$$

??? note "证明方法：线性表出 &  两个欧拉参数内积等于夹角 cos 值"

    $S^3$中的单位四元数 $\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3$ 与 $\mathrm{U}$ 中的欧拉参数 $(\eta, \varepsilon_1, \varepsilon_2, \varepsilon_3)^T$ 一一对应。考虑两个用欧拉参数（等价于用单位四元数）表示的不同姿态：

    $$
    \mathbf{r}_0 = (\eta, \varepsilon_1, \varepsilon_2, \varepsilon_3)^T
    $$

    $$
    \mathbf{r}_1 = (\xi, \delta_1, \delta_2, \delta_3)^T
    $$

    式中，$\mathbf{r}_0 \neq \mathbf{r}_1$ 且 $\mathbf{r}_0 \neq -\mathbf{r}_1$。四元数插值的目的是找出中间姿态 $\mathbf{r}_t$，$t \in [0, 1]$（注意这里的起止时间作了归一化），使得 $\mathbf{r}_0$ 平滑过渡到 $\mathbf{r}_1$。显然，$\mathbf{r}_0$ 和 $\mathbf{r}_1$ 这两个四维单位向量确定了 $\mathbb{R}^4$ 中的一个平面，该平面上的任何一个元素（四维向量）都可以表示为 $\mathbf{r}_0$ 和 $\mathbf{r}_1$ 的线性组合。在该平面中，向量 $\mathbf{r}_0$、$\mathbf{r}_1$ 和 $\mathbf{r}_0 - \mathbf{r}_1$ 构成一个三角形，对于 $\mathbf{r}_0$ 和 $\mathbf{r}_1$ 的夹角 $\theta$，由余弦定理，有

    $$
    2\|\mathbf{r}_0\|\|\mathbf{r}_1\|\cos\theta = \|\mathbf{r}_0\|^2 + \|\mathbf{r}_1\|^2 - \|\mathbf{r}_0 - \mathbf{r}_1\|^2
    $$

    注意到 $\|\mathbf{r}_0\| = \|\mathbf{r}_1\| = 1$。

    $$
    \begin{align*}
    \|\mathbf{r}_0 - \mathbf{r}_1\|^2 &= (\eta - \xi)^2 + (\varepsilon_1 - \delta_1)^2 + (\varepsilon_2 - \delta_2)^2 + (\varepsilon_3 - \delta_3)^2\\
    &= (\eta^2 + \varepsilon_1^2 + \varepsilon_2^2 + \varepsilon_3^2) + (\xi^2 + \delta_1^2 + \delta_2^2 + \delta_3^2) - 2(\eta\xi + \varepsilon_1\delta_1 + \varepsilon_2\delta_2 + \varepsilon_3\delta_3)\\
    &= \|\mathbf{r}_0\|^2 + \|\mathbf{r}_1\|^2 - 2\mathbf{r}_0 \cdot \mathbf{r}_1
    \end{align*}
    $$

    于是，两个欧拉参数的内积等于它们夹角的余弦值

    $$
    \mathbf{r}_0 \cdot \mathbf{r}_1 = \cos\theta
    $$

    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250325102316.webp)

    如图所示，将中间姿态 $\mathbf{r}_t$ 限制在 $\mathbf{r}_0$ 和 $\mathbf{r}_1$ 确定的平面中并假设匀速旋转，可以使四元数插值问题化为一个简单的平面几何问题：$\mathbf{r}_0$、$\mathbf{r}_1$ 和 $\mathbf{r}_t$ 都在平面单位圆上，$\mathbf{r}_t$ 从 $\mathbf{r}_0$ 匀速旋转到 $\mathbf{r}_1$。

    由于匀速旋转，对于 $t \in [0, 1]$，$\mathbf{r}_0$ 与 $\mathbf{r}_t$ 的夹角是 $t\theta$，$\mathbf{r}_1$ 与 $\mathbf{r}_t$ 的夹角是 $(1-t)\theta$，则由欧拉参数内积与夹角余弦值的关系，有

    $$
    \begin{align*}
    \mathbf{r}_0 \cdot \mathbf{r}_t = \cos(t\theta)\\
    \mathbf{r}_t \cdot \mathbf{r}_1 = \cos((1-t)\theta)
    \end{align*}
    $$

    同时，$\mathbf{r}_t$ 可以表示为 $\mathbf{r}_0$ 和 $\mathbf{r}_1$ 的线性组合，即

    $$
    \mathbf{r}_t = k_0\mathbf{r}_0 + k_1\mathbf{r}_1
    $$

    最后，求解线性方程组

    $$
    \begin{cases}
    k_0 + k_1\cos\theta = \cos(t\theta) \\
    k_0\cos\theta + k_1 = \cos((1-t)\theta)
    \end{cases}
    $$

    联立两式，可求得

    $$
    k_0 = \frac{\sin((1-t)\theta) - k_1\sin\theta}{\sin\theta}, k_1 = \frac{\sin(t\theta) - k_0\sin\theta}{\sin\theta}
    $$

    式中，$\theta = \cos^{-1}(\mathbf{r}_0 \cdot \mathbf{r}_1)$。

注意到单位四元数$r$和-$r$表示三维空间中的同一姿态。一般应该选取**最短路径**进行球面线性插值。

因此如果两四元数的夹角为钝角，则可通过将其中一个四元数取负，再对得到的两个夹角为锐角的四元数进行球面线性插值。

初始两个四元数如果是$\pi$的话，就说明两个四元数对应的是同一个姿态。

如果

#### 代码实现如下

```python title="slerp_interpolation"
def slerp(q1, q2, t):
    """
    球面线性插值（Slerp）
    :param q1: 起始四元数
    :param q2: 终止四元数
    :param t: 插值因子，范围 [0, 1]
    :return: 插值后的四元数
    """
    dot_product = np.dot(q1, q2)
    dot_product = np.clip(dot_product, -1.0, 1.0)
    theta_0 = np.arccos(dot_product)
    sin_theta_0 = np.sin(theta_0)
    
    if sin_theta_0 < 1e-6:
        return q1
    
    theta = theta_0 * t
    s1 = np.sin(theta) / sin_theta_0
    s0 = np.cos(theta) - dot_product * s1
    return s0 * q1 + s1 * q2
```

需要下载 matlab 的 robotics toolbox 和
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__quaternion_animation.gif)

```m title="slerp_interpolation，r0到r1和r0到-r1的对比" linenums="1"
%初始化
clear;clc;close all;
%定义初始和结束四元数（绕Y轴旋转90度）
theta=pi/3;%90度
r0=quaternion(1,0,0,0);%初始姿态（无旋转）
r1=quaternion(cos(theta/2),0,sin(theta/2),0);%绕Y轴旋转theta

% 创建两个子图
h = figure('Position',[100 100 1200 400]);
subplot_handles = zeros(1,2);
h_x = zeros(1,2);
h_y = zeros(1,2);
h_z = zeros(1,2);

% 初始化两个子图
for j = 1:2
    subplot_handles(j) = subplot(1,2,j);
    hold on;
    grid on;
    axis equal;
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    view(3);
    xlim([-1.5,1.5]);
    ylim([-1.5,1.5]);
    zlim([-1.5,1.5]);
    if j == 1
        title('r0到r1的四元数插值路径');
    else
        title('r0到-r1的四元数插值路径');
    end
    
    % 初始化动画对象
    origin = [0;0;0];
    h_x(j) = quiver3(origin(1),origin(2),origin(3),1,0,0,'r','LineWidth',2);
    h_y(j) = quiver3(origin(1),origin(2),origin(3),0,1,0,'g','LineWidth',2);
    h_z(j) = quiver3(origin(1),origin(2),origin(3),0,0,1,'b','LineWidth',2);
end

% 创建动画帧
filename = 'quaternion_animation.gif';
for t = 0:0.02:1
    % 第一个子图：r0到r1的插值
    q_r1 = slerp(r0,r1,t);
    x_r1 = quatrotate(compact(q_r1),[1,0,0]);
    y_r1 = quatrotate(compact(q_r1),[0,1,0]);
    z_r1 = quatrotate(compact(q_r1),[0,0,1]);
    
    set(h_x(1),'UData',x_r1(1),'VData',x_r1(2),'WData',x_r1(3));
    set(h_y(1),'UData',y_r1(1),'VData',y_r1(2),'WData',y_r1(3));
    set(h_z(1),'UData',z_r1(1),'VData',z_r1(2),'WData',z_r1(3));
    
    % 第二个子图：r0到-r1的插值
    q_neg_r1 = slerp(r0,-r1,t);
    x_neg_r1 = quatrotate(compact(q_neg_r1),[1,0,0]);
    y_neg_r1 = quatrotate(compact(q_neg_r1),[0,1,0]);
    z_neg_r1 = quatrotate(compact(q_neg_r1),[0,0,1]);
    
    set(h_x(2),'UData',x_neg_r1(1),'VData',x_neg_r1(2),'WData',x_neg_r1(3));
    set(h_y(2),'UData',y_neg_r1(1),'VData',y_neg_r1(2),'WData',y_neg_r1(3));
    set(h_z(2),'UData',z_neg_r1(1),'VData',z_neg_r1(2),'WData',z_neg_r1(3));
    
    drawnow;
    
    % 捕获当前帧并写入GIF
    frame = getframe(h);
    im = frame2im(frame);
    [imind,cm] = rgb2ind(im,256);
    if t == 0
        imwrite(imind,cm,filename,'gif','Loopcount',inf,'DelayTime',0.02);
    else
        imwrite(imind,cm,filename,'gif','WriteMode','append','DelayTime',0.02);
    end
end

function q_interp = slerp(q0,q1,t)
    %将四元数转换为数组格式
    q0_compact=compact(q0);
    q1_compact=compact(q1);
    %计算点积（四元数分量直接相乘）
    
    dot_prod=sum(q0_compact.*q1_compact);
    %限制点积范围
    dot_prod=min(max(dot_prod,-1),1);
    theta=acos(dot_prod);
    %处理θ为0的情况
    if theta<eps
        q_interp=q0;
        return;
    end
    %计算插值系数
    k0=sin((1-t)*theta)/sin(theta);
    k1=sin(t*theta)/sin(theta);
    %线性组合并重新构造四元数
    q_interp_compact=k0*q0_compact+k1*q1_compact;
    q_interp=quaternion(q_interp_compact);
    q_interp=normalize(q_interp);
end
```

### Slerp 拓展：对角速度有约束

!!! attention "这个题目与变式历年卷考察多次，一定要掌握"

!!! note "当匀速旋转的假设不成立的时候，需要应用多项式规划"

由于单位四元数球面线性插值方法 (Slerp) 的旋转角速度是定值，此时直接应用 Slerp 公式进行规划是不行的。结合 Slerp 公式，给出上述要求下相应的姿态

!!! example "若单位四元数插值时，要求在初始姿态$r_0$ 和最终姿态$r_1$ 时的角速度均为$0$,且转动过程中角速度连续。"

    **解答**

    设$r_0$与$r_1$的夹角为$\theta$，$r_0$与$r_t$的夹角为$\beta$,令$\beta = x(t)\theta$，$t \in [0,1]$

    $$
    \begin{cases}
    x(0) = 0 \\
    x(1) = 1 \\
    x'(0) = x'(1) = 0 \\
    \text{且} x(t) \text{在} (0,1) \text{连续}
    \end{cases}
    $$

    不妨假设$x(t) = a_1t^3 + a_2t^2 + a_3t + a_4$

    $$
    \begin{cases}
    x(0) = a_4 = 0 \\
    x(1) = a_1 + a_2 + a_3 = 1 \\
    x'(0) = a_3 = 0 \\
    x'(1) = 3a_1 + 2a_2 = 0
    \end{cases} 
    \Rightarrow
    \begin{cases}
    a_1 = -2 \\
    a_2 = 3 \\
    a_3 = a_4 = 0
    \end{cases}
    $$

    即$x(t) = -2t^3 + 3t^2$

    令$r_t = k_0r_0 + k_1r_1$，有

    $$
    \begin{cases}
    k_0 + k_1\cos\theta = \cos\beta \\
    k_0\cos\theta + k_1 = \cos(\theta - \beta)
    \end{cases}
    \Rightarrow k_0 = \frac{\sin(\theta - \beta)}{\sin\theta} \quad k_1 = \frac{\sin\beta}{\sin\theta}
    $$

    即

    $$
    r_t = \frac{\sin((1-x(t))\theta)}{\sin\theta}r_0 + \frac{\sin(x(t)\theta)}{\sin\theta}r_1
    $$

## 题型

解方程比较麻烦

### 多项式参数计算：时间、速度

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250325084857.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250325084926.webp)

### 抛物线过渡计算

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250324203708.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Model__assets__5-TrajectoryPlanning.assets__20250324203627.webp)

已知起点角度为 138°，中间点到达的点角度为 158°，时间为 5.5s，点角度为 10°，时间为 31.5s。需要计算中间点。中间点关于中点对称。采用带有抛物线过渡的线性规划来实现。过渡段（第二个中间点到第三个中间点）的持续时间为 16s。

### matlab 求解方程

- 方程写出来，丢给 gpt
