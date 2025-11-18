# Loss

损失为什么求平均：更好调学习率，相当于学习率之和梯度有关，和 batch size 没有关系

每次算梯度的时候要记得清零，不然会做累加

## l1 loss

不常用绝对差值而用平方损失：不好求导

有不平滑性，可能不稳定

离远点较远的时候，不一定希望有一个很大的梯度

## l2 loss (MSE)

$$
\mathcal{L}_{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2
$$

- 优点：
  - 求导容易
- 缺点：
  - 梯度下降开始很慢

### Huber Robust loss

## softmax

$$
P(y=i) = y_i = softmax(\vec{x})_i = \frac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}}
\quad\text{for } i=1,\dots,n
$$

### 为什么使用

什么是 max 我们都很清楚，那什么是 soft 呢？在梯度下降当中，直接使用 max（hardmax）产生的问题是不可导。

所以我们希望使用 softmax 来解决这个问题。

所谓 soft，就是通过 exp 让大数变得更大，让小数变得更小，再通过归一化让大数更接近于 1。即我们不仅对硬分类感兴趣，还对软分类（概率）感兴趣

- 线性有可能有负数，概率应该是非负的 -> 使用指数的方式实现
- 概率之和需要为 1 -> 使用求和的方式实现

**输入**：一个向量（例如全连接层的输出）

**输出**：概率分布

**约束**：分类互斥，不能是多标签分类

### 代码实现

```python
import torch 
x = torch.Tensor([1,2,3]) 
x_softmax = torch.exp(x) / torch.sum(torch.exp(x))

>>> x
tensor([1., 2., 3.])
>>> x_softmax
tensor([0.0900, 0.2447, 0.6652])
```

```python title="内置函数"
import torch.nn as nn 

x = torch.Tensor([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
softmax_layer = nn.Softmax(dim=1) 
output = softmax_layer(x)

>>> output
tensor([[0.0900, 0.2447, 0.6652], 
        [0.0900, 0.2447, 0.6652], 
        [0.0900, 0.2447, 0.6652]])
```

### 梯度推导

给定输入 $\mathbf{x} = [x_1, x_2, \dots, x_n]$，softmax 输出为：

$$
\hat{y}_i = softmax(\vec{x})_i = \frac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}}
\quad\text{for } i=1,\dots,n
$$

分两种情况讨论：

$$
\begin{aligned}
i = j \; \text{时}\qquad&
\frac{\partial \hat{y}_i}{\partial x_i}
= \frac{d}{d x_i} \left( \frac{e^{x_i}}{\sum_k e^{x_k}} \right)=\frac{e^{x_i}\sum_k e^{x_k}-e^{x_i}e^{x_i}}{(\sum_k e^{x_k})^2}
= \hat{y}_i \left(1 - \hat{y}_i\right)\\
i \ne j \; \text{时}\qquad&
\frac{\partial \hat{y}_i}{\partial x_j}
= \frac{d}{d x_j} \left( \frac{e^{x_i}}{\sum_k e^{x_k}} \right)=-\frac{e^{x_i}e^{x_j}}{(\sum_k e^{x_k})^2}
= - \hat{y}_i \hat{y}_j\\
\end{aligned}
$$

综上

$$
\frac{\partial \hat{y}_i}{\partial x_j} = \begin{cases}\hat{y}_i(1 - \hat{y}_i) & \text{if } i = j \\
-\hat{y}_i \hat{y}_j & \text{if } i \ne j\end{cases}
$$

**写成矩阵形式（Jacobian）：**

记 softmax 输入为$\mathbf{X} = [x_1, \dots, x_n]^\top$，输出为 $\mathbf{\hat{Y}} = [\hat{y}_1, \dots, \hat{y}_n]^\top$，则：

$$
\begin{aligned}
\mathbf{J}=\frac{\partial\mathbf{\hat{y}}}{\partial\mathbf{x}}&=\begin{bmatrix}\frac{\partial \hat{y}_1}{\partial x_1}&\frac{\partial \hat{y}_1}{\partial x_2}&\cdots&\frac{\partial \hat{y}_1}{\partial x_n}\\\frac{\partial \hat{y}_2}{\partial x_1}&\frac{\partial \hat{y}_2}{\partial x_2}&\cdots&\frac{\partial \hat{y}_2}{\partial x_n}\\\vdots&\vdots&\ddots&\vdots\\\frac{\partial \hat{y}_n}{\partial x_1}&\frac{\partial \hat{y}_n}{\partial x_2}&\cdots&\frac{\partial \hat{y}_n}{\partial x_n}\end{bmatrix}_{n\times n}\\
&=\begin{bmatrix}\hat{y}_1-\hat{y}_1\hat{y}_1&-\hat{y}_1\hat{y}_2&\cdots&-\hat{y}_1\hat{y}_n\\-\hat{y}_2\hat{y}_1&\hat{y}_2-\hat{y}_2\hat{y}_2&\cdots&-\hat{y}_2\hat{y}_n\\\vdots&\vdots&\ddots&\vdots\\-\hat{y}_n\hat{y}_1&-\hat{y}_n\hat{y}_2&\cdots&\hat{y}_n-\hat{y}_n\hat{y}_n\end{bmatrix}\\
&=diag(\hat{Y})-\hat{Y} \hat{Y}^T
\end{aligned}
$$

$$
\boxed{
\mathbf{J}_{\text{softmax}} = \text{diag}(\mathbf{\hat{Y}}) - \mathbf{\hat{Y}} \mathbf{\hat{Y}}^\top
}
$$

- $\mathbf{J}$是转置对称矩阵
- $\text{diag}(\mathbf{\hat{Y}})$ 是对角矩阵，对角线为 $\hat{y}_i$
- $\mathbf{\hat{Y}} \mathbf{\hat{Y}}^\top$ 是外积，得到一个 rank1 矩阵

!!! note "梯度消失的推导"

    然后我们来看softmax的梯度。不妨简记softmax函数为 $g(\cdot)$，softmax得到的分布向量 $\hat{\mathbf{y}} = g(\mathbf{x})$ 对输入 $\mathbf{x}$ 的梯度为：
    
    $$
    \frac{\partial g(\mathbf{x})}{\partial \mathbf{x}} = \text{diag}(\hat{\mathbf{y}}) - \hat{\mathbf{y}} \hat{\mathbf{y}}^\top \quad \in \mathbb{R}^{d \times d}
    $$
    
    把这个矩阵展开：
    
    $$
    \frac{\partial g(\mathbf{x})}{\partial \mathbf{x}} = \begin{bmatrix}
    \hat{y}_1 & 0 & \cdots & 0 \\
    0 & \hat{y}_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \hat{y}_d
    \end{bmatrix} - \begin{bmatrix}
    \hat{y}_1^2 & \hat{y}_1 \hat{y}_2 & \cdots & \hat{y}_1 \hat{y}_d \\
    \hat{y}_2 \hat{y}_1 & \hat{y}_2^2 & \cdots & \hat{y}_2 \hat{y}_d \\
    \vdots & \vdots & \ddots & \vdots \\
    \hat{y}_d \hat{y}_1 & \hat{y}_d \hat{y}_2 & \cdots & \hat{y}_d^2
    \end{bmatrix}
    $$
    
    根据前面的讨论，当输入 $\mathbf{x}$ 的元素均较大时，softmax会把大部分概率分布分配给最大的元素，假设我们的输入数量级很大，最大的元素是 $x_1$，那么就将产生一个接近one-hot的向量 $\hat{\mathbf{y}} \approx [1, 0, \cdots, 0]^{\top}$，此时上面的矩阵变为如下形式：
    
    $$
    \frac{\partial g(\mathbf{x})}{\partial \mathbf{x}} \approx \begin{bmatrix}
    1 & 0 & \cdots & 0 \\
    0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & 0
    \end{bmatrix} - \begin{bmatrix}
    1 & 0 & \cdots & 0 \\
    0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & 0
    \end{bmatrix} = \mathbf{0}
    $$
    
    也就是说，在输入的数量级很大时，梯度消失为0，造成参数更新困难。

### 交叉熵 + softmax 的梯度推导

- 交叉熵损失函数定义为：

$$
\mathcal{L}(\hat{\mathbf{y}}, \mathbf{y}) = -\sum_{i=1}^n y_i \log \hat{y}_i
$$

其中，$y_i$是真实的标签，而$\hat{y}_i$是预测的标签。

如果$y$使用 one-hot 标签，相当于$y$是$n$维向量，其中只有$y_i$为 1，其他为 0，那么就可以把求和符合拿掉

$$
\frac{\partial \mathcal{L}}{\partial \hat{\mathbf{y}}} = \left( -\frac{y_i}{\hat{y}_i} \right)
$$

根据链式法则，有

$$
\begin{aligned}
\frac{\partial \mathcal{L}(g(\mathbf{x}))}{\partial x_j} &= \sum_i \frac{\partial \mathcal{L}}{\partial \hat{y}_i} \cdot \frac{\partial \hat{y}_i}{\partial x_j}\\
&=  \sum_i \left( -\frac{y_i}{\hat{y}_i} \right) \cdot \left( \hat{y}_i (\delta_{ij} - \hat{y}_j) \right)\\
&= \sum_i \left( -y_i (\delta_{ij} - \hat{y}_j) \right)\\
&= \underbrace{-y_j +{\color{blue}y_j \hat{y}_j}}_{i=j} +\underbrace{{\color{blue}\sum_{i} y_i \hat{y}_j}}_{i\neq j} \\
&= -y_j + {\color{blue}\sum_i y_i \hat{y}_j} \quad \because\text{合并两项}\\
&= -y_j + \hat{y}_j \sum_i y_i \\
&= -y_j + \hat{y}_j \\
&= \hat{y}_j - y_j
\end{aligned}
$$

即

$$
\frac{\partial \mathcal{L}(g(\mathbf{x}))}{\partial x_j} = \hat{y}_j - y_j
$$

写成矩阵形式

$$
\boxed{
\nabla_{\mathbf{x}} \mathcal{L}(g(\mathbf{x})) = \hat{\mathbf{y}} - \mathbf{y}
}
$$

### mini-batch softmax

- one single softmax 计算量太大
- 批处理
- mini batch

### safe-softmax

$$
\boxed{softmax(X + c) = softmax(X)}
$$

这里$\mathbf{X}$是向量，$c$是一个常数。

$$
softmax(X + c)_i = \frac{e^{x_i + c}}{\sum_k e^{x_k + c}} = \frac{e^{x_i} \cdot e^c}{\sum_k e^{x_k} \cdot e^c} = \frac{e^{x_i}}{\sum_k e^{x_k}} = softmax(X)_i
$$

实际应用：为了防止溢出，事先把$\mathbf{X}$减去最大值。最大值是有效数据，其他值溢不溢出可管不了，也不关心。

### parallel-softmax

## Acknowledgement

[反向传播之一：softmax 函数 - 知乎](https://zhuanlan.zhihu.com/p/37740860)

[详解 softmax 函数以及相关求导过程 - 知乎](https://zhuanlan.zhihu.com/p/25723112)
