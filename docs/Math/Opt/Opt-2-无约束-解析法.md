# 02 | 无约束 解析解法

## 单变量问题定义

### 邻域

开邻域：

$$
B_o(c;r)=\{x\mid x\in\mathcal{D}, |x-c|<r\}
$$

闭邻域：

$$
B_o(c;r)=\{x\mid x\in\mathcal{D}, |x-c|\leq r\}
$$

### 极值点

**全局极小点**：对于定义域内的所有点，都满足：

$$
f(x^*) \leq f(x), \forall x\in D, x\neq x^*
$$

**严格全局极小点**：对于定义域内的所有点，都满足：

$$
f(x^*) < f(x), \forall x\in D
$$

**局部极小点**：点 $c$ 称为函数 $f(x)$ 的一个局部极小 (或极大) 点，若对于满足 $0<|\Delta x|\leq r$ 的所有 $\Delta x$，均有：

$$
f(c) \leqslant f(c+\Delta x) \text{ 或 } f(c) \geqslant f(c+\Delta x)
$$

## 向量变元问题定义

### 闭合邻域

$$
B(\bar{x}; r) = \{x \mid \|x - \bar{x}\|_2 \leqslant r\}
$$

$$
B(c; r) = \{x \mid x \in \mathbb{R}^n, \|x - c\|_2 < r\}
$$

内点：

给定一集合$S$,点$\bar{x}$称为集合$S$的内点 (interior point),若$\bar{x}\in S$,并且存在$\bar{x}$的一邻域，该邻域完全包含在集合$S$内。集合$S$的内集 (interior) 记作 $int(S)$,它是$S$的所有内点的合集

边界点：

给定一集合$S$,点$x$是$S$的边界点 (boundary point),若$x$的每一个邻域至少有一个点在$S$ 内，并且至少有一个点不在$S$内。集合$S$的边界记作 $bnd(S)$,是$S$的所有边界点的合集一个闭集包含其所有边界点。

## 矩阵变元问题定义

## 平稳点与极值点

$$
\nabla f\left(x^{*}\right)=\left[\frac{\partial f(x)}{\partial x}\right]_{x=x^{*}}^{T}=0
$$

### 实变量函数条件

| 实变量函数 | $f(x) : \mathbb{R} \rightarrow \mathbb{R}$ | $f(x) : \mathbb{R}^n \rightarrow \mathbb{R}$ | $f(X) : \mathbb{R}^{m \times n} \rightarrow \mathbb{R}$ |
| ------------ | ------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------- |
| 平稳点 | $\frac{df(x)}{dx} = 0$ | $\nabla f(x) = 0$ | $\frac{\partial f(X)}{\partial X} = O_{m \times n}$ |
| 局部极小点 | $\frac{d^2f(x)}{dx^2} \geq 0$ | $\nabla^2 f(x) \succeq 0$ | $\frac{\partial^2f(X)}{d\text{vec}(X)^T(\text{vec}X)^T} \preceq 0$ |
| 严格局部极小点 | $\frac{d^2f(x)}{dx^2} > 0$ | $\nabla^2 f(x) \succ 0$ | $\frac{\partial^2f(X)}{d\text{vec}(X)^T(\text{vec}X)^T}  \prec 0$ |
| 局部极大点 | $\frac{d^2f(x)}{dx^2} \leq 0$ | $\nabla^2 f(x) \preceq 0$ | $\frac{\partial^2f(X)}{d\text{vec}(X)^T(\text{vec}X)^T}  \succeq 0$ |
| 严格局部极大点 | $\frac{d^2f(x)}{dx^2} < 0$ | $\nabla^2 f(x) \prec 0$ | $\frac{\partial^2f(X)}{d\text{vec}(X)^T(\text{vec}X)^T}  \succ 0$ |
| 鞍点 | $\frac{d^2f(x)}{dx^2}$ 不定 | $\nabla^2 f(x)$ 不定 | $\frac{\partial^2f(X)}{d\text{vec}(X)^T(\text{vec}X)^T}$ 不定 |

!!! note "这里$\succ,\succeq$的意思是半正定和正定"

### 复变函数条件

1. 共轭梯度矩阵决定最小化问题的闭式解。
2. 共轭梯度矩阵与 Hessian 矩阵给出局部极小点辨识的必要条件或充分条件。
3. 共轭梯度向量的负方向决定求解最小化问题的最速下降迭代算法。
4. Hessian 矩阵给出求解最小化问题的 Newton 算法。

| 复变函数 | $f(z,z^{*}): \mathbb{C} \to \mathbb{R}$ | $f(z,z^{*}): \mathbb{C}^{n} \to \mathbb{R}$ | $f(Z,Z^{*}): \mathbb{C}^{m \times n} \to \mathbb{R}$ |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 平稳点 | $$\frac{\partial f(z,z^{*})}{\partial z^{*}} \mid_{z=c}=0$$ | $$\frac{\partial f(z,z^{*})}{\partial z^{*}}\mid_{z=c}=O_{n \times 1}$$ | $$\frac{\partial f(Z,Z^{*})}{\partial Z^{*}} \mid_{Z=C} = O_{m \times n}$$ |
| 局部极小点 | $H(f(c,c^{*})) \succeq 0$ | $H(f(c,c^{*})) \succeq 0$ | $H(f(C,C^{*})) \succeq 0$ |
| 严格局部极小点 | $H(f(c,c^{*})) \succ 0$ | $H(f(c,c^{*})) \succ 0$ | $H(f(C,C^{*})) \succ 0$ |
| 局部极大点 | $H(f(c,c^{*})) \preceq 0$ | $H(f(c,c^{*})) \preceq 0$ | $H(f(C,C^{*})) \preceq 0$ |
| 严格局部极大点 | $H(f(c,c^{*})) \prec 0$ | $H(f(c,c^{*})) \prec 0$ | $H(f(C,C^{*})) \prec 0$ |
| 鞍点 | $H(f(c,c^{*}))$ 不定 | $H(f(c,c^{*}))$ 不定 | $H(f(C,C^{*}))$ 不定 |

其中，平稳点需要求解共轭梯度

$$
H(f(c,c^{*}))=\begin{bmatrix}\frac{\partial^{2}f(z,z^{*})}{\partial z^{*}\partial z}&\frac{\partial^{2}f(z,z^{*})}{\partial z^{*}\partial z^{*}}\\\frac{\partial^{2}f(z,z^{*})}{\partial z\partial z}&\frac{\partial^{2}f(z,z^{*})}{\partial z\partial z^{*}}\end{bmatrix}_{z=c}\in\mathbb{C}^{2\times2}
$$

$$
H(f(c,c^{*}))=\begin{bmatrix}\frac{\partial^{2}f(z,z^{*})}{\partial z^{*}\partial z^{\mathrm{T}}}&\frac{\partial^{2}f(z,z^{*})}{\partial z^{*}\partial z^{\mathrm{H}}}\\\frac{\partial^{2}f(z,z^{*})}{\partial z\partial z^{\mathrm{T}}}&\frac{\partial^{2}f(z,z^{*})}{\partial z\partial z^{\mathrm{H}}}\end{bmatrix}_{z=\mathbf{c}}\in\mathbb{C}^{2n\times2n}
$$

$$
H(f(C,C^{*}))=\begin{bmatrix}\frac{\partial^{2}f(Z,Z^{*})}{\partial(\operatorname{vec}Z^{*})\partial(\operatorname{vec}Z^{*})^{\mathrm{T}}}&\frac{\partial^{2}f(Z,Z^{*})}{\partial(\operatorname{vec}Z^{*})\partial(\operatorname{vec}Z^{*})^{\mathrm{T}}}\\\frac{\partial^{2}f(Z,Z^{*})}{\partial(\operatorname{vec}Z)\partial(\operatorname{vec}Z)^{\mathrm{T}}}&\frac{\partial^{2}f(Z,Z^{*})}{\partial(\operatorname{vec}Z)\partial(\operatorname{vec}Z^{*})^{\mathrm{T}}}\end{bmatrix}_{Z=C}\in\mathbb{C}^{2mn\times2mn}
$$
