# 复变函数

## 解析函数

复解析函数

1. 复变函数 $f(z)$ 是全纯函数 (即复解析函数);
2. 复变函数的导数 $f'(z)$ 存在，并且连续;
3. 复变函数 $f(z)$ 满足 Cauchy-Riemann 条件

    $$
    \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{和} \quad \frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}
    $$

4. 复变函数 $f(z)$ 的所有导数存在，并且具有一个收敛的幂级数。

形式偏导定义：

$$
\begin{aligned}
\frac{\partial}{\partial z} &= \frac{1}{2}\left(\frac{\partial}{\partial x}-\mathrm{j}\frac{\partial}{\partial y}\right) \quad z=x+\mathrm{j}y \\
\frac{\partial}{\partial z^{*}} &= \frac{1}{2}\left(\frac{\partial}{\partial x}+\mathrm{j}\frac{\partial}{\partial y}\right)
\end{aligned}
$$

实部与虚部的独立性假设：

$$
\begin{aligned}
\frac{\partial x}{\partial y} &= 0 \quad\text{和}\quad \frac{\partial y}{\partial x} = 0 \\[1em]
\frac{\partial z}{\partial z^*} &= \frac{\partial x}{\partial z^*}+\mathrm{j}\frac{\partial y}{\partial z^*} \\
&= \frac{1}{2}\left(\frac{\partial x}{\partial x}+\mathrm{j}\frac{\partial x}{\partial y}\right)+\mathrm{j}\frac{1}{2}\left(\frac{\partial y}{\partial x}+\mathrm{j}\frac{\partial y}{\partial y}\right) \\
&= \frac{1}{2}(1+0)+\mathrm{j}\frac{1}{2}(0+\mathrm{j}) \\[1em]
\frac{\partial z^*}{\partial z} &= \frac{\partial x}{\partial z}-\mathrm{j}\frac{\partial y}{\partial z} \\
&= \frac{1}{2}\left(\frac{\partial x}{\partial x}-\mathrm{j}\frac{\partial x}{\partial y}\right)-\mathrm{j}\frac{1}{2}\left(\frac{\partial y}{\partial x}-\mathrm{j}\frac{\partial y}{\partial y}\right) \\
&= \frac{1}{2}(1-0)-\mathrm{j}\frac{1}{2}(0-\mathrm{j})
\end{aligned}
$$

因此：

$$
\frac{\partial z}{\partial z^*} = 0 \quad\text{和}\quad \frac{\partial z^*}{\partial z} = 0
$$

即 $z$ 和 $z^*$ 是两个相互独立的变量。

## 复积分

## 级数

### 泰勒展开

### Talor 定理

## 留数

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=305213390&bvid=BV1iP411g7J3&cid=891588515&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=450px></iframe>

复合闭路定理的具体体现

### 奇点类型判断

- 可去奇点：洛必达
- 本性奇点：洛朗展开
- m 级极点：

!!! example "例 1.1：求$f(z)=\frac{z^{2}}{e^{z}-1}$的奇点，并指出奇点类型"

    解：令$e^{z}-1=0$，即$e^{z}=1$，即$z=\mathrm{Ln}1=2k\pi i$。
    故$f(z)$的奇点为$z=2k\pi i$($k=0,\pm 1,\pm 2,\dots$)。

    ①对$e^{z}-1$:
    $(e^{z}-1)'|_{z=2k\pi i}=e^{z}|_{z=2k\pi i}=1\neq 0$，
    故$z=2k\pi i$为$e^{z}-1$的1级零点;

    ②对$z^{2}$:
    当$k=0$时，$z=0$显然是$z^{2}$的2级零点;
    当$k\neq 0$时，$z=2k\pi i$不是$z^{2}$的零点。

    故:
    $z=0$是$f(z)$的可去奇点,
    $z=2k\pi i$($k=\pm 1,\pm 2,\dots$)是$f(z)$的1级极点。

!!! example "例 1.2：求$f(z)=\frac{\cot(\pi z)}{2z-3}$在$|z-i|=2$内的奇点"

    解：$f(z)=\frac{\cot(\pi z)}{2z-3}=\frac{\cos(\pi z)}{\sin(\pi z)(2z-3)}$.
    令$\sin(\pi z)=0$，则$z=k$($k=0,\pm 1$),
    令$2z-3=0$，则$z=\frac{3}{2}$.

    ①$z=\frac{3}{2}$是$2z-3$的1级零点，不是$\sin(\pi z)$的零点，是$\cos(\pi z)$的1级零点，则其是$f(z)$的可去奇点;

    ②$z=k$不是$2z-3$的零点，是$\sin(\pi z)$的1级零点，不是$\cos(\pi z)$的零点，则其是$f(z)$的1级极点。

    故在$|z-i|=2$内，
    $z=\frac{3}{2}$是$f(z)$的可去奇点，$z=0,\pm 1$是$f(z)$的1级极点。

!!! note "例题"

    对于函数 $\frac{1}{z}e^{zt-\frac{1}{z}}=\frac{1}{z}e^{zt}\cdot e^{-\frac{1}{z}}$，$z=0$ 是函数的本性奇点，函数在 $z=0$ 的去心邻域 $\{z;0<|z|<+\infty\}$ 中的罗朗展开式为

    $$
    \begin{align*}
    \frac{1}{z}e^{zt-\frac{1}{z}}&=\frac{1}{z}e^{zt}\cdot e^{-\frac{1}{z}}\\
    &=\frac{1}{z}\left[1+zt+\frac{1}{2!}(zt)^2+\cdots+\frac{1}{n!}(zt)^n+\cdots\right]\\
    &\quad\cdot\left[1-\frac{1}{z}+\frac{1}{2!}\frac{1}{z^2}+\cdots+\frac{(-1)^n}{n!}\frac{1}{z^n}+\cdots\right]\\
    &\quad(0<|z|<+\infty)
    \end{align*}
    $$

    所以相乘后的级数 $\frac{1}{z}$ 的系数 $C_{-1}$ 为

    $$
    C_{-1}=\text{Res}\left[\frac{1}{z}e^{zt-\frac{1}{z}};0\right]
    $$

### 留数计算

基础方法：洛朗展开式

- **有理分式函数**，1 级极点：

若$f(z)=\frac{P(z)}{Q(z)}$，且$z_0$不是$P(z)$的零点，是$Q(z)$的 1 级零点，则

$$
\text{Res}[f(z),z_0]=\frac{P(z)}{Q'(z)}
$$

> 注：只能用于「非零点/1 级零点 = 1 级极点」的情况。

- **m 级极点**$(m=1,2,3...)$

若$z_0$是$f(z)$的 m 级极点，则

$$
\text{Res}[f(z),z_0]=\frac{1}{(m-1)!}\lim_{z\to z_0}\frac{\mathrm{d}^{m-1}}{\mathrm{d}z^{m-1}}[(z-z_0)^mf(z)]
$$

注：意思是，先作函数$G(z)=(z-z_0)^mf(z)$，然后求其$m-1$阶导数$G^{(m-1)}(z)$，再求它趋于$z\to z_0$的极限，最后乘上系数$\frac{1}{(m-1)!}$。

请留意，极点级数为$m$，乘上的多项式次数为$m$，但求导次数和系数都是$m-1$。

!!! example "例 2.1：求$\oint_{C}\frac{e^{z}}{z(z+1)^{2}}dz$，其中$C$为正向圆周$|z|=2$"

    解：$f(z)=\frac{e^{z}}{z(z+1)^{2}}$的奇点为$z=0$，$z=-1$；显然$z=0$是它的1级极点，$z=-1$是它的2级极点。

    则$\text{Res}[f(z),0]=\lim_{z\to 0}zf(z)=\lim_{z\to 0}\frac{e^{z}}{(z+1)^{2}}=1$；

    $\text{Res}[f(z),-1]=\lim_{z\to -1}[(z+1)^{2}f(z)]'=\lim_{z\to -1}\left[\frac{e^{z}}{z}\right]'=\lim_{z\to -1}\frac{(z-1)e^{z}}{z^{2}}=\frac{-2}{e}$。

    则$\oint_{C}\frac{e^{z}}{z(z+1)^{2}}dz=2\pi i\{\text{Res}[f(z),0]+\text{Res}[f(z),-1]\}=2\pi i(1-\frac{2}{e})$。

!!! example "例 2.2：求$\oint_{C}\frac{z-\sin z}{z^{6}}dz$，其中$C$为正向圆周$|z|=1$"

    解：$f(z)=\frac{z-\sin z}{z^{6}}$的奇点为$z=0$，这是它的3级奇点。*故此题用求留数的规则较繁琐

    将$f(z)$在$0<|z|<1$上洛朗展开，则
    $$
    \begin{align*}
    f(z)&=\frac{z}{z^{6}}-\frac{1}{z^{6}}\sin z\\
    &=\frac{z}{z^{6}}-\frac{1}{z^{6}}\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}z^{2n+1}\\
    &=\frac{1}{z^{5}}-\sum_{n=0}^{\infty}\frac{(-1)^{n}}{(2n+1)!}z^{2n-5}
    \end{align*}
    $$

    则$c_{-1}=-\frac{(-1)^{2}}{(2\times 2+1)!}=\frac{1}{120}$。

    则$\oint_{C}\frac{z-\sin z}{z^{6}}dz=2\pi i\text{Res}[f(z),0]=-\frac{1}{60}\pi i$。

!!! example "例 3.3：用留数计算定积分 $I = \int_{-\infty}^{+\infty} \frac{x^2}{(x^2+1)(x^2+4)} dx$"

    解：$f(z) = \frac{z^2}{(z^2+1)(z^2+4)}$ 在上半复平面上的奇点为 $z=i, z=2i$，且均为其1级极点，
    故 $I = 2\pi i \{ \text{Res}[f(z), i] + \text{Res}[f(z), 2i] \} = 2\pi i \left[ \lim_{z \to i} \frac{z^2}{(z+i)(z^2+4)} + \lim_{z \to 2i} \frac{z^2}{(z^2+1)(z+2i)} \right] = 0$。

!!! example "例 3.4：用留数计算定积分 $I = \int_{0}^{+\infty} \frac{x^2}{x^4+1} dx$"

    解：显然 $f(x) = \frac{x^2}{x^4+1}$ 为偶函数，则 $I = \frac{1}{2} \int_{-\infty}^{+\infty} f(x) dx$。
    $f(z) = \frac{z^2}{z^4+1}$ 在上半复平面上的奇点为 $z = \pm \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} i$，且均为其1级极点，
    故 $I = 2\pi i \left\{ \text{Res} \left[f(z), \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} i \right] + \text{Res} \left[f(z), -\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} i \right] \right\} = \pi i \left[ \frac{1-i}{4\sqrt{2}} - \frac{1+i}{4\sqrt{2}} \right] = \frac{\sqrt{2}}{4} \pi$。

!!! example "例 3.5：用留数计算定积分$I=\int_{0}^{+\infty}\frac{\cos x}{(x^{2}+1)(x^{2}+9)}dx$"

    解：显然$f(x)=\frac{\cos x}{(x^{2}+1)(x^{2}+9)}$为偶函数，则$I=\frac{1}{2}\int_{-\infty}^{+\infty}f(x)dx$。

    而$F(z)=\frac{e^{iz}}{(z^{2}+1)(z^{2}+9)}$在上半复平面上的奇点为$z=i,z=3i$，且均为其1级极点，

    故$I=\frac{1}{2}\text{Re}\left(2\pi i\left\{\text{Res}[F(z),i]+\text{Res}[F(z),3i]\right\}\right)=\frac{1}{2}\text{Re}\left(2\pi i\left\{\frac{e^{-1}}{16i}-\frac{e^{-3}}{48i}\right\}\right)=\left(\frac{e^{-1}}{16}-\frac{e^{-3}}{48}\right)\pi$。

!!! example "例 3.6：用留数计算定积分$I=\int_{-\infty}^{+\infty}\frac{x\sin3x}{x^{2}+16}dx$"

    解：$F(z)=\frac{ze^{i3z}}{z^{2}+16}$在上半复平面上的奇点为$z=4i$，且为其1级极点，

    故$I=\text{Im}(2\pi i\text{ Res}[F(z),4i])=\text{Im}\left(2\pi i\lim_{z\to4i}\frac{ze^{3z}}{z+4i}\right)=\pi e^{-12}$。

### 留数的应用 —— 求解实函数定积分

实函数可以认为是复数仅在实轴上“活动”得到的。实函数的定积分也同样如此。
因此，将定积分与复变积分关联起来，再用留数定理求出复变积分，有时可以方便的求出一些不易计算的定积分。
这里我们不加证明的给出三种形式的定积分与复变积分的关系。

#### 有理三角函数全周期积分

$$
\int_{0}^{2\pi}R(\cos\theta,\sin\theta)d\theta
$$

令$z=e^{i\theta}$，则积分路径$|z|=1$

- $\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}=\frac{z^{2}-1}{2iz}$
- $\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2}=\frac{z^{2}+1}{2z}$
- $dz=ie^{i\theta}d\theta\quad\rightarrow\quad d\theta=\frac{1}{iz}dz$

#### 有理分式函数无穷广义积分

$$
\int_{-\infty}^{+\infty}R(x)dx
$$

直接将$R(x)$改为$R(z)$,上半平面奇点的留数之和

$$
\int_{-\infty}^{+\infty}R(x)dx=2\pi i\sum\text{Res}[R(z),z_{0}]
$$

#### 有理函数乘三角函数无穷广义积分

$$
\int_{-\infty}^{+\infty}R(x)\cos ax\,dx(a>0) \quad \text{或}R(x)\sin ax
$$

构造函数$R(z)e^{iaz}$，求留数

$$
\int_{-\infty}^{+\infty}R(x)\cos ax\,dx+i\int_{-\infty}^{+\infty}R(x)\sin ax\,dx=2\pi i\sum\text{Res}[R(z)e^{iaz},z_{0}]
$$

这个值是一个复数

- 实部对应含$\cos ax$的积分
- 虚部对应含$\sin ax$的积分

!!! example "例 27：计算积分 $I=\int_{0}^{+\infty}\frac{1}{x^{4}+1}dx$"

    解：$f(z)=\frac{1}{z^{4}+1}$ 在上半平面有单极点 $e^{\frac{\pi}{4}i},e^{\frac{3\pi}{4}i}$。

    由于被积函数为偶函数，则

    $$
    \begin{align*}
    I &= \int_{0}^{+\infty}\frac{1}{x^{4}+1}dx \\
    &= \frac{1}{2}\int_{-\infty}^{+\infty}\frac{1}{x^{4}+1}dx \\
    &= \frac{1}{2}\cdot2\pi i(\mathrm{Res}[\frac{1}{z^{4}+1};e^{\frac{\pi}{4}i}]+\mathrm{Res}[\frac{1}{z^{4}+1};e^{\frac{3\pi}{4}i}]) \\
    &= \pi i(\frac{1}{4e^{\frac{3\pi}{4}i}}+\frac{1}{4e^{\frac{9\pi}{4}i}}) \\
    &= \frac{\pi i}{4}\frac{1}{\sqrt{2}}(-1-i+1-i) \\
    &= \frac{\sqrt{2}}{4}\pi
    \end{align*}
    $$

## 保角映射

## Laplace 变换

[拉普拉斯变换与拉普拉斯逆变换的常用结论与经典公式-CSDN 博客](https://blog.csdn.net/wh_STUDY/article/details/126403817)
