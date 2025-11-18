# 数电

## 逻辑电路

[真值表与逻辑表达式](https://zhuanlan.zhihu.com/p/154529095)

| 符号 | LaTeX 表示 | 公式示例       | 说明           |
|------|------------|----------------|----------------|
| 与（AND） | `\land`  | \(A \land B\)  | 逻辑与运算符   |
| 或（OR）  | `\lor`   | \(A \lor B\)   | 逻辑或运算符   |
| 非（NOT） | `\neg`   | \(\neg A\)     | 逻辑非运算符   |
| 蕴含（IMPLIES） | `\rightarrow` | \(A \rightarrow B\) | 逻辑蕴含运算符 |
| 等价（EQUIVALENT） | `\leftrightarrow` | \(A \leftrightarrow B\) | 逻辑等价运算符 |
| 全称量词（FOR ALL） | `\forall` | \(\forall x \, P(x)\) | 全称量词 |
| 存在量词（THERE EXISTS） | `\exists` | \(\exists x \, P(x)\) | 存在量词 |

=== "与 AND"

    $$
    Y = A\quad AND\quad B = A\&B = A\cdot B = AB
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240228121552683.webp" alt="与关系" style="zoom:33%;" />

=== "或 OR"

    $$
    Y = A \quad OR \quad B = A+B
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240228121833879.webp" alt="或关系" style="zoom:33%;" />

=== "非 NOT"

    $$
    Y = A' = NOT \quad A
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240228122022442.webp" alt="非关系" style="zoom:33%;" />

=== "异或——杂合子"

    不同则为1，相同则为0

    **不进位的加法**

    $$
    Y = A \oplus B = \bar{A}B + A\bar{B}
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240228122336850.webp" alt="异或关系" style="zoom:33%;" />

=== "同或——纯合子"

    **不同则为 0，相同则为 1;**


    $$
    Y = A \odot B
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240228122444834.webp" alt="同或关系" style="zoom:33%;" />

### 基本公式

[B 站讲解](https://www.bilibili.com/video/BV1jP411G7Wd)

#### 常量与常量

$$
\begin{align*}
1 + 1 = 1\\
0\cdot0 = 0
\end{align*}
$$

#### 常量与变量

$$
\begin{align*}
A \cdot 0 = 0\\
A+1 = 1\\
\end{align*}
$$

#### 变量和变量

分配律

$$
A+BC = (A+B)(A+C)
$$
<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240301144447212.webp" alt="公式 17 的证明" style="zoom: 50%;" />

同一律

$$
\begin{align*}
A+\bar{A} = 1\\
A\cdot \bar{A} = 0\\
\\
A\cdot A = A\\
A + A = A
\end{align*}
$$

反演律（**De Morgan's laws**）

**并项法**

$$
AB + A\bar{B} = A
$$

**吸收法**（**短项吸收长项**）

$$
\begin{align*}
A + AB = A(1+B)= A\\
AB + \bar{A}C + BC = AB + \bar{A}C
\end{align*}
$$

消因子（**短项能够消去 长项中 的 相反项**）

$$
\begin{align*}
A+\bar{A}B = A+B\\
A\cdot (1+B) = A+AB+A’B = A+B
\end{align*}
$$

配项法

$$
\begin{align*}
A + \bar{A} = 1\\
A \cdot A = 0
\end{align*}
$$

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__image-20240306113302112.webp)

### 逻辑函数化简

[逻辑函数 (表示方法、形式转换、化简、最小项、最大项)](https://blog.csdn.net/qq_44431690/article/details/104587163)

逻辑式、逻辑图、波形图

#### 规则

1.反演规则：与或互换，01 互换；原变量变成反变量，反变量变成原变量

2.对偶规则：与或互换，01 互换

3.标准与或式：$n$个变量，共有$2^n$种可能 eg.三变量逻辑函数$Y = A+BC$的最小项表示为$\Sigma m(3,4,5,6,7)$

4.与非 - 与非表达式：化成与或式；两次取反；德摩根定律

#### 公式化简

[数字电路 - 逻辑式化简公式](https://zhuanlan.zhihu.com/p/392457877)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__v2-8dc1606574d995edbc843fb019b38fad_1440w.webp" alt="img" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__v2-61355c6b4a7dba5e2e887c17d8e480a8_1440w.webp" alt="img" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__v2-55a64baa868c2fd6676c3369c66ea3ff_r.webp" alt="img" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__v2-939bf95fd46b11c990a59657ff7bc67f_r.webp" alt="img" style="zoom:50%;" />

#### 真值表

由真值表写逻辑表达式

第一步：从真值表内找输出端为“1”的各行，把每行的输入变量写成乘积形式;遇到“0”的输入变量上加非号。

第二步：把各乘积项相加，即得逻辑函数的表达式。

#### 卡诺图

用几何相邻表示逻辑相邻（两个最小项只有一个变量不同）

所以顺序是 00，01，11，10

化简：相邻、相对（偶数个），**$2^n$个相邻的最小项合并可以消去$n$个因子**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__4c32c787711a908076a7ec169f077d0.webp" alt="4c32c787711a908076a7ec169f077d0" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__c6677b612f12342788a479c941fda79.webp" alt="c6677b612f12342788a479c941fda79" style="zoom: 50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__dcc7e633252e1c0e39d94c11fa69557.webp" alt="dcc7e633252e1c0e39d94c11fa69557" style="zoom:50%;" />

最简与或：包含的乘积项已经最少，每个乘积项的因子也最少，称为最简的与 - 或逻辑式

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Digital.assets__v2-06ac3268bb0d79aea7786e0d763dc2cd_1440w.webp" alt="img" style="zoom:50%;" />
