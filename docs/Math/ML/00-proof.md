# 关键证明总结

## Bias-Variance 分解

- $y_D$训练标签
- $x$ 样本
- $f(x,D)$训练结果
- $y$ 真实标签

$$
f(\boldsymbol{x}) = \mathbb{E}_D[f(\boldsymbol{x}; D)]
$$

- 使用样本数相同的不同训练集产生的方差为：

    $$
    \text{var}(\boldsymbol{x}) = \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))^2\right]
    $$

- 期望输出与真实标记的差别称为偏差（bias），即

    $$
    \text{bias}^2(\boldsymbol{x}) = (\bar{f}(\boldsymbol{x}) - y)^2
    $$

- 噪声为：

    $$
    \epsilon^2 = \mathbb{E}_D \left[(y_D - y)^2\right]
    $$

  - 为便于讨论，假定噪声期望为零，即 $\mathbb{E}_D[y_D - y] = 0$。

---

通过简单的多项式展开合并，可对算法的期望泛化误差进行分解：

$$
\begin{aligned}
E(f; D) &= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - y_D)^2\right] \\
&= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}) + \bar{f}(\boldsymbol{x}) - y_D)^2\right] \\
&= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))^2\right] + \mathbb{E}_D \left[(\bar{f}(\boldsymbol{x}) - y_D)^2\right] + \mathbb{E}_D \left[2(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))(\bar{f}(\boldsymbol{x}) - y_D)\right] \quad (\epsilon = y - y_D 噪声和其他一次项独立，均值为 0)\\
&= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))^2\right] + \mathbb{E}_D \left[(\bar{f}(\boldsymbol{x}) - y_D)^2\right]  \\
&= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))^2\right] + \mathbb{E}_D \left[(\bar{f}(\boldsymbol{x}) - y + y - y_D)^2\right] \\
&= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))^2\right] + \mathbb{E}_D \left[(\bar{f}(\boldsymbol{x}) - y)^2\right] + \mathbb{E}_D \left[(y - y_D)^2\right] + 2\mathbb{E}_D \left[(\bar{f}(\boldsymbol{x}) - y)(y - y_D)\right] \\
&= \mathbb{E}_D \left[(f(\boldsymbol{x}; D) - \bar{f}(\boldsymbol{x}))^2\right] + \mathbb{E}_D \left[(\bar{f}(\boldsymbol{x}) - y)^2\right] + \mathbb{E}_D \left[(y_D - y)^2\right]
\end{aligned}
$$

$$
E(f; D) = \text{var}(\boldsymbol{x}) + \text{bias}^2(\boldsymbol{x}) + \epsilon^2
$$

## Kernel Method

## 贝叶斯分类
