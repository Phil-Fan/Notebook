# Gated Delta Net

> 线性注意力的状态更新默认只加不删：同一个键写两次，两个值直接叠加，谁也覆盖不了谁。DeltaNet 把这一步换成 delta rule——先用当前 key 从旧状态里**读**出已经存的值，再按「新值 − 旧值」的误差改写；Gated DeltaNet 在这之上加一个每头标量衰减。这篇只拆状态更新的几行式子，混合层的配比与工程影响见 [07-混合注意力](./07-混合注意力.md)。

## 从线性注意力说起

沿用本目录的符号：第 $t$ 个 token 的输入是 $x_t\in\mathbb{R}^{d}$，一个头的状态 $S_t\in\mathbb{R}^{d_v\times d_k}$，三个投影给出

$$
q_t = W_Q x_t,\qquad k_t = W_K x_t,\qquad v_t = W_V x_t
$$

线性注意力把历史压进固定大小的状态，递推只做外积累加：

$$
S_t = S_{t-1} + v_t k_t^{\top},\qquad o_t = S_t q_t
$$

（[07](./07-混合注意力.md) 里把 $S$ 写成 $d_k\times d_v$、输出写 $S_t^\top q_t$，只是转置约定，这里统一用 $d_v\times d_k$。）

这个更新不只是「装不下精确历史」，还有一个更隐蔽的问题：**同一个键写两次，两个值会相加，而不是覆盖。** 状态里没有「删除」这个动作，旧值永远留在那里，读到的总是历年写入的混合。DeltaNet 就是来补这个动作的。

## 一次更新：读 → 混 → 写

$S_{t-1}$ 是截至上一步的状态，DeltaNet 每一步做四件事：

$$
\begin{aligned}
v_t^{old} &= S_{t-1} k_t \\
v_t^{new} &= \beta_t\, v_t + (1-\beta_t)\, v_t^{old} \\
S_t &= S_{t-1} - v_t^{old} k_t^{\top} + v_t^{new} k_t^{\top} \\
o_t &= S_t q_t
\end{aligned}
$$

其中写入门 $\beta_t = \sigma(W_\beta x_t)$ 是一个标量（$\sigma$ 就是 sigmoid）。

- 第一行是**读**：拿当前 key 去旧状态里查值。
- 第二行是**混**：新值和旧值按 $\beta_t$ 做凸组合，$\beta_t=1$ 表示完全覆盖，$\beta_t=0$ 表示完全不写。
- 第三行是**写**：先减掉旧值对应的外积，再加上新值的外积。所以「不仅能写新值，还能删除旧值」是字面意思。
- 第四行是**输出**：用 query 再读一次，读出更新后的记忆，作为这一层的输出。

## $v_t^{old}$ 到底是怎么算的

这是最容易卡住的一行，因为它看起来像个未知量，其实它只是一次普通的矩阵乘：

$$
v_t^{old} = S_{t-1}k_t
$$

- $S_{t-1}$ 的形状是 $d_v\times d_k$，$k_t$ 是 $d_k$ 维，乘出来是 $d_v$ 维，和 $v_t$ 同维——这才谈得上做凸组合。
- 语义上是**用当前的键去查过去的记忆**：$S_{t-1}$ 是所有历史写入的外积之和，拿 $k_t$ 去乘它，等于按相似度把「和这个键相关的那些写入」加权取回来。
- 所以它**不是额外参数、不是新变量，也不需要回看历史 KV**：$v_t^{old}$ 完全由旧状态和当前 key 决定，是前向计算的一部分。整个机制里它只是一次 $O(d_vd_k)$ 的乘加，和输出那一步 $o_t = S_t q_t$ 是同一种运算，区别只是用 key 还是 query 去查。

名字里的「old」来自一个直觉：键归一化且近似正交时，$S_{t-1}k_t$ 近似等于这个键上次被写入的值。多个键不严格正交时，它只是相似度加权的近似——这也正是 delta rule 只能近似删除的原因。

## 为什么长这样：一步梯度下降

把记忆看成一个线性模型 $Sk \approx v$，每一步的在线损失是

$$
L_t(S) = \frac{1}{2}\left\|S k_t - v_t\right\|_2^2
$$

对 $S$ 求梯度得 $\nabla_S L_t = (S k_t - v_t)k_t^{\top}$，以 $\beta_t$ 为学习率走一步：

$$
S_t = S_{t-1} - \beta_t\left(S_{t-1}k_t - v_t\right)k_t^{\top}
    = S_{t-1} + \beta_t\left(v_t - v_t^{old}\right)k_t^{\top}
$$

代入 $v_t^{new} - v_t^{old} = \beta_t(v_t - v_t^{old})$，就是上面第三行。所以整件事可以读成：**每来一个 token，就对「这个键值对」做一次一步 SGD，把误差方向写进状态。**

## 写完再读：旧值确实被覆盖

若 key 归一化，$\|k_t\|_2 = 1$：

$$
S_t k_t = S_{t-1}k_t + \left(v_t^{new}-v_t^{old}\right)\left(k_t^{\top}k_t\right) = v_t^{new}
$$

更新完立刻读回来，恰好是新值，旧值被减掉了——这就是「删除」的准确含义。若 $\|k_t\|^2 \ne 1$，读回来是 $v_t^{old} + (v_t^{new}-v_t^{old})\|k_t\|^2$，只是缩放过的插值，覆盖不精确。所以实现里都把 key 归一化，或者把 $\|k_t\|^2$ 吸收进 $\beta_t$。

## 一个标量小例子

取 $k=1$、$\beta=0.5$，同一个键先写 2、再写 4：

| 步 | $v_t$ | $v_t^{old}=S_{t-1}k$ | $v_t^{new}$ | 更新后的 $S$ |
|---|---|---|---|---|
| 1 | 2 | 0 | 1.0 | 1.0 |
| 2 | 4 | 1.0 | 2.5 | 2.5 |

第二步的 $v_t^{old}$ 就是第一步写进去的 1.0，新值是 $0.5\times4+0.5\times1=2.5$。同一个键反复出现时，读到的旧值就是最近写入值的指数滑动平均（EMA），$\beta$ 控制覆盖力度。

## 两个门：$\beta_t$ 和 $\alpha_t$

2021 年的 DeltaNet 只有标量写入门 $\beta_t$（可以固定为 1，也可以由投影学到）；2024 年的 Gated DeltaNet 再引入一个每头标量衰减 $\alpha_t$，把 GLA / Mamba2 那一路的遗忘也合进来：

$$
S_t = \alpha_t S_{t-1}\left(I - \beta_t k_t k_t^{\top}\right) + \beta_t v_t k_t^{\top}
$$

展开后等价于「先对旧状态打折，再按 $\beta_t$ 融合」：

$$
S_t = \alpha_t S_{t-1} + \beta_t\left(v_t - \alpha_t S_{t-1}k_t\right)k_t^{\top}
$$

两个门分工不同：$\alpha_t$ 与 key 无关，管「整体忘多快」，$\alpha_t\in(0,1)$ 由输入投影得到（常见实现取 $e^{g_t}$、$g_t\le 0$ 以保数值稳定）；$\beta_t$ 只作用于这一次写入，管「这条写多狠」。取 $\alpha_t=1$ 就退回上面那一版。

## 和 vanilla 线性注意力比

| | vanilla 线性注意力 | DeltaNet |
|---|---|---|
| 状态更新 | $S_{t-1} + v_t k_t^{\top}$ | 先读 $v_t^{old}$，再减旧加新 |
| 能否覆盖旧值 | 不能，只能叠加 | 能，同一键方向被改写 |
| 每步额外成本 | — | 一次 $S k_t$、两个外积 |
| 精确检索 | 弱，读到的是历史混合 | 强，键上的值被覆盖 |

代价是每步多两个外积、并行度更低。$S$ 的递推是一串矩阵变换 $I-\beta_t k_t k_t^{\top}$，块内可以把连乘用 WY 表示展开成矩阵乘、块间再串行递推，这样才上得了 GPU（2024 年那篇并行化工作）；Gated DeltaNet 建在这套 chunkwise 形式上，Kimi Linear 的 KDA 又把它推广到通道级门控。

## 常见误解

- **「$v_t^{old}$ 要遍历历史找那个 key。」** 不用，历史全压进 $S$ 了，只有一次矩阵乘。这也正是 $O(1)$ 缓存的前提。
- **「$k_t$ 是当前的，乘 $S_{t-1}$ 是不是看到未来了？」** 没有，状态是过去的、key 是当前的，就是「用现在的键查过去的记忆」。
- **「删除是精确的。」** 只在归一化且键近似正交时成立，一般情况是加权的近似覆盖。
- **「$\beta_t$ 和激活函数里的 sigmoid 是一回事吗？」** 同一个 $\sigma$，但这里它当门用，输出 0~1 的标量参与凸组合。

## 面试收束

> 线性注意力把「键 → 值」的写入做成外积累加，只能加不能改。DeltaNet 用 delta rule 把它变成先读旧值、再按误差改写：$v^{old}=S_{t-1}k_t$ 是一次矩阵乘，$v^{new}$ 是旧值与新值的凸组合，写回时减掉旧外积、加上新外积；归一化 key 下，更新后读回恰好是新值。整件事等价于对重建误差做一步梯度下降。Gated DeltaNet 再加每头标量衰减 $\alpha$，KDA 把衰减改成通道级——这就是 3 : 1 混合层里线性层的那一半。

## 参考

- Schlag, Irie, Schmidhuber, [Linear Transformers Are Secretly Fast Weight Programmers](https://arxiv.org/abs/2102.11174)（2021，DeltaNet 的 delta rule）
- Yang 等，[Parallelizing Linear Transformers with the Delta Rule over Sequence Length](https://arxiv.org/abs/2406.06484)（2024，chunkwise 并行）
- Yang, Kautz, Hatamizadeh, [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464)（2024，加门控）
- Kimi Linear 的 KDA，见 [07-混合注意力](./07-混合注意力.md)
