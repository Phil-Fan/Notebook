# 02 | 性能分析

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Control__BASE__assets__02-Metrics.assets___E6_97_B6_E5_9F_9F_E5_88_86_E6_9E_90.svg)

## 微分方程

## 传递函数

## Laplace 变换

## 时域性能指标

二阶系统的特征多项式通常表示为：

$$
s^2 + 2\zeta\omega_ns + \omega_n^2
$$

其中：

- $s$ 是复数频率变量。
- $\zeta$ 是阻尼比。
- $\omega_n$ 是无阻尼系统的自然频率
  
**动态指标性能**

1. **上升时间（Rise Time）**: $T_r = \frac{\pi - \beta}{\omega_n \sqrt{1 - \zeta^2}}$
2. **峰值时间（Peak Time）**: $T_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$  ，峰值时间的等高线是一条射线，且等峰值线是虚轴相同。
3. **超调量（Overshoot）**: $\sigma = e^{-\frac{\zeta \pi}{\sqrt{1 - \zeta^2}}}$  ，超调量只由阻尼比 $\zeta$ 决定。
4. **调节时间（Settling Time）**:  

   - 5% 误差：$T_s \approx \frac{3}{\zeta \omega_n}$  
   - 2% 误差：$T_s \approx \frac{4}{\zeta \omega_n}$

5. **衰减比（Damping Ratio）**: $n = \frac{\sigma}{B'} = e^{-\frac{2\zeta \pi}{\sqrt{1 - \zeta^2}}}$

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Control__BASE__assets__02-Metrics.assets___E6_8E_A7_E5_88_B6_E7_B3_BB_E7_BB_9F_E6_80_A7_E8_83_BD.svg)

## Error Dynamics

如果期望关节位置为$\theta_d(t)$ ,实际关节位置为$\theta(t)$ ,那么关节误差就为：

$$
\theta_e(t)=\theta_d(t)-\theta(t)
$$

上面方程对应的微分方程就称为 error dynamics，那么反馈控制器控制的目标也很明显，就是让$\theta_e(t)$尽可能小，趋近于 0 或等于 0.

> 评价标准：稳（稳态误差很小），准（没有超调或者很小），快（调节时间很短）

$$
a_{p}\theta_{e}^{(p)}+a_{p-1}\theta_{e}^{(p-1)}+\cdots+a_{2}\ddot{\theta}_{e}+a_{1}\dot{\theta}_{e}+a_{0}\theta_{e}=c
$$

对于齐次线性误差动力学 ($c=0$)，就有：

$$
\begin{align*}
\theta_{e}^{(p)}&=-\frac{1}{a_{p}}(a_{p-1}\theta_{e}^{(p-1)}+\cdots+a_{2}\ddot{\theta}_{e}+a_{1}\dot{\theta}_{e}+a_{0}\theta_{e})\\
&=-a_{p-1}^{\prime}\theta_{e}^{(p-1)}-\cdots-a_{2}^{\prime}\ddot{\theta}_{e}-a_{1}^{\prime}\dot{\theta}_{e}-a_{0}^{\prime}\theta_{e}
\end{align*}
$$

$x_1 = \theta_e, x_2 = \dot{\theta}_e, x_3 = \ddot{\theta}_e$,转为能控标准型

得到

$$
\dot{x}_p = -a_0'x_1 - a_1'x_2 - a_2'x_3 \dots - a_{p-1}'x_p
$$

$$
\dot{x}(t) = Ax(t)
$$

$$
A=\begin{bmatrix}0&1&0&\cdots&0&0\\0&0&1&\cdots&0&0\\\vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\0&0&0&\cdots&1&0\\0&0&0&\cdots&0&1\\-a_0^{\prime}&-a_1^{\prime}&-a_2^{\prime}&\cdots&-a_{p-2}^{\prime}&-a_{p-1}^{\prime}\end{bmatrix}\in\mathbb{R}^{p\times p}
$$

要想让$x_p$趋近于 0，需要$A$的特征值在复平面左半平面，即$Re(\lambda_i) < 0$

### first order system

### second order system

$$
\mathfrak{m}\ddot{\theta}_{e}+b\dot{\theta}_{e}+k\theta_{e}=f
$$

如果 $m \neq 0$，那么二阶误差动力学就为：

$$
\ddot{\theta}_e(t) + \frac{b}{m} \dot{\theta}_e(t) + \frac{k}{m} \theta_e(t) = 0
$$

写成二阶形式：

$$
\ddot{\theta}_e(t) + 2\zeta \omega_n \dot{\theta}_e(t) + \omega_n^2 \theta_e(t) = 0
$$

$\omega_n = \sqrt{k/m}$ 就是熟悉的固有频率， $\zeta = b/2\sqrt{km}$ 就是阻尼比，那么特征多项式为：

$$
s^2 + 2\zeta \omega_n s + \omega_n^2 = 0
$$

两个根为：

$$
s_1 = -\zeta \omega_n + \omega_n \sqrt{\zeta^2 - 1} \\
s_2 = -\zeta \omega_n - \omega_n \sqrt{\zeta^2 - 1}
$$
