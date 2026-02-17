# 08 | 集成学习

!!! note "好的集成，个体学习器应该“好而不同” "
> 君子和而不同

- 个体学习器强依赖关系，采用串行式的方法：boosting
- 个体学习期不存在强依赖关系，并行化的方法:bagging,RF

<!--more-->
## boosting - AdaBoost

[通俗易懂理解——Adaboost 算法原理 - 知乎](https://zhuanlan.zhihu.com/p/41536315)

### 📌Training Error Bound

Adaboost 的训练误差界：

$$
\text{Training Error} \leq \exp\left(-2 \sum_{t=1}^T \left(\frac{1}{2} - \epsilon_t\right)^2\right)
$$

体现了其"自适应性"和对弱分类器的强整合能力。这也是 Adaboost 能够从多个"弱"分类器中获得强大性能的理论基础。

设：

- 我们有 $m$ 个训练样本 ${(x_i, y_i)}_{i=1}^m$，其中 $y_i \in \{-1, +1\}$
- 使用 $T$ 轮 boosting，每轮产生一个弱分类器 $h_t(x)$ 和对应的权重 $\alpha_t$
- 最终分类器为加权投票：

  $$
  H(x) = \text{sign}\left(\sum_{t=1}^T \alpha_t h_t(x)\right)
  $$

---

训练误差上界公式

Adaboost 的训练误差满足如下上界：

$$
\frac{1}{m} \sum_{i=1}^m \mathbb{I}\left(H(x_i) \neq y_i\right) \leq \prod_{t=1}^T Z_t
$$

其中：

- $Z_t$ 是第 $t$ 轮的归一化因子（normalization factor）：

  $$
  Z_t = \sum_{i=1}^m D_t(i) \cdot e^{-\alpha_t y_i h_t(x_i)}
  $$

  它也可以用来表示该轮加权训练误差的"soft upper bound"。

更进一步，如果每一轮的弱分类器误差为：

$$
\epsilon_t = \Pr_{i \sim D_t}[h_t(x_i) \neq y_i]
$$

并且我们选择：

$$
\alpha_t = \frac{1}{2} \ln \left( \frac{1 - \epsilon_t}{\epsilon_t} \right)
$$

那么：

$$
Z_t = 2 \sqrt{\epsilon_t (1 - \epsilon_t)} \leq e^{-2\gamma_t^2} \quad \text{其中 } \gamma_t = \frac{1}{2} - \epsilon_t
$$

> 这里使用的是泰勒展开

因此，训练误差上界变为：

$$
\frac{1}{m} \sum_{i=1}^m \mathbb{I}\left(H(x_i) \neq y_i\right) \leq \prod_{t=1}^T Z_t \leq \exp\left(-2 \sum_{t=1}^T \gamma_t^2 \right)
$$

---
🔍 直观解释

- $\gamma_t$ 是 margin，表示弱分类器超出随机猜测的一点点优势。
- 即使每个 $\gamma_t$ 很小（每个分类器仅稍微优于随机），累积起来依然能让训练误差快速收敛到 0。
- 上界是**指数下降的**，这解释了 Adaboost 的"奇迹"：即使每一轮很弱，只要"稳定比随机好"，整体误差下降得非常快。

### 前向分步算法

Adaboost 看作：模型是加法模型、损失函数是指数函数、学习算法为前向分步算法的二分类学习方法

## bagging

使用 bootstrap 方法进行采样：$m$个样本的数据集，又放回的随机采样$m$次，初始训练集约有$63.2\%$的样本出现在采样集合

采样出$T$个这样的数据集合，训练出$T$个基学习器，使用简单平均/投票法进行集成。
1️

[机器学习中的 bootstrap 到底是什么？ - 知乎](https://zhuanlan.zhihu.com/p/261387233)

[从 0 开始机器学习-Bagging 和 Boosting - 知乎](https://zhuanlan.zhihu.com/p/37730184#:~:text=%E6%9C%AC%E6%96%87%E5%B0%86%E4%BB%8B%E7%BB%8DBaggi)

### Random Forest

放在 Decision Tree 一节

## 结合策略

## 多样性分析
