# 42. 接雨水

!!! abstract "题单坐标"
    **Hot 20 · 第 2 类「双指针」** ｜ 难度：困难 ｜ 标签：`数组` `双指针` `动态规划` `单调栈`

    一句话套路：每个位置的水位由「左侧最高」和「右侧最高」里较矮的那根决定，双指针每轮只结算**更矮的那一侧**。

## 题干

> [力扣 42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例 1**

```text
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
```

**示例 2**

```text
输入：height = [4,2,0,3,2,5]
输出：9
```

**提示**

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## 思路

**先写出公式。** 记 $L_i = \max(height[0..i])$、$R_i = \max(height[i..n-1])$（含自身），位置 `i` 的积水为

$$w_i = \min(L_i, R_i) - height[i]$$

因为水面只会被两侧中最矮的那道「墙」卡住，而含自身的写法保证 $\min(L_i, R_i) \ge height[i]$，所以减完天然非负，不用再套 $\max(0, \cdot)$。所有 $w_i$ 相加就是答案。

**为什么直接双指针就能对（关键不变量）。** 公式要用两侧的 max，但双指针根本不去求另一侧的 max——这靠的是「左区间已结算的柱子都不高于右区间最大值」这个不变量：

- 初始 `left = 0`、`right = n-1`、`leftMax = rightMax = 0`。
- 若 `height[left] < height[right]`：右区间最大值满足 `rightMax ≥ height[right] > height[left]`；而此前每一个从左结算的位置 `i` 都满足 `height[i] < height[right_i]`（`right_i` 是当时的右指针），且 `right_i ≥ right`，故 `height[i] ≤ rightMax`。合起来 `leftMax < rightMax`，所以 $\min = leftMax$，位置 `left` 的水位被 `leftMax` 唯一确定，可以立即结算。
- 对称地，若 `height[left] >= height[right]`，则 `rightMax ≤ leftMax`，$\min = rightMax$，结算右侧。
- 两侧相等时走哪一支都对，因为此时两条不变式同时成立；但**不能在同一轮把两边都结算掉**，那样会跳过指针相遇的检查。

指针相遇时每个位置恰好被结算一次，累加值就是答案。也就是说，「更矮的一侧」这个直觉背后的严格理由，是它保证了正在使用的那一侧的 max 就是两侧 max 中较矮的那个。

**怎么做。**

1. 两个指针分别夹住数组两端，`leftMax` / `rightMax` 各记「各自一侧已经见过的最高柱」。
2. 每轮比较 `height[left]` 与 `height[right]`，谁更矮就结算谁：**先**用 max 更新这一侧的 max，**再**累加 `max - 当前高度`，然后把该侧指针向内移一格。
3. 指针相遇即结束，返回累加值。

结算顺序必须是「先更新 max 再累加」：当前柱子的水位要用包含它自己的最高值算，新高的柱子自身贡献 0 格，而不是负数。

**走一遍示例。** `height = [0,1,0,2,1,0,1,3,2,1,2,1]`，括号里是当轮左右指针指向的高度：

| 轮次 | 指针位置 | 比较 | 结算 | leftMax | rightMax | water |
|:-----|:---------|:-----|:-----|:--------|:---------|:------|
| 1 | left=0(0), right=11(1) | 0 < 1 | 左，+0 | 0 | 0 | 0 |
| 2 | left=1(1), right=11(1) | 1 ≥ 1 | 右，+0 | 0 | 1 | 0 |
| 3 | left=1(1), right=10(2) | 1 < 2 | 左，+0 | 1 | 1 | 0 |
| 4 | left=2(0), right=10(2) | 0 < 2 | 左，+1 | 1 | 1 | 1 |
| 5 | left=3(2), right=10(2) | 2 ≥ 2 | 右，+0 | 1 | 2 | 1 |
| 6 | left=3(2), right=9(1) | 2 ≥ 1 | 右，+1 | 1 | 2 | 2 |
| 7 | left=3(2), right=8(2) | 2 ≥ 2 | 右，+0 | 1 | 2 | 2 |
| 8 | left=3(2), right=7(3) | 2 < 3 | 左，+0 | 2 | 2 | 2 |
| 9 | left=4(1), right=7(3) | 1 < 3 | 左，+1 | 2 | 2 | 3 |
| 10 | left=5(0), right=7(3) | 0 < 3 | 左，+2 | 2 | 2 | 5 |
| 11 | left=6(1), right=7(3) | 1 < 3 | 左，+1 | 2 | 2 | 6 |

11 轮后 `left = right = 7`，循环结束，`water = 6`。看第 9~11 轮：右侧只剩一根高度 3 的柱子，`rightMax` 稳定在 2，左侧连续结算的 1、0、1 全靠它兜底——这就是「只结算更矮一侧」在画面上的样子。

**几种方案的取舍。**

| 方案 | 时间 | 空间 | 一句话 |
|:-----|:-----|:-----|:-------|
| 暴力：每格左右各扫一遍 | $O(n²)$ | $O(1)$ | 面试起步用，n = 2×10⁴ 会超时 |
| 前后缀最高数组 | $O(n)$ | $O(n)$ | 最好理解，适合当对照/验算 |
| 双指针 | $O(n)$ | $O(1)$ | 本题最优，主推 |
| 单调栈 | $O(n)$ | $O(n)$ | 按「层」算水，思路另类，见延伸 |

## 代码（带注释）

> 按力扣提交格式写：一个 `Solution` 类。只用内置类型。

=== "主推：双指针（O(1) 空间）"

    ```python
    class Solution:
        def trap(self, height: list[int]) -> int:
            left, right = 0, len(height) - 1
            left_max = right_max = 0
            water = 0
            while left < right:
                if height[left] < height[right]:
                    left_max = max(left_max, height[left])
                    water += left_max - height[left]
                    left += 1
                else:
                    right_max = max(right_max, height[right])
                    water += right_max - height[right]
                    right -= 1
            return water
    ```

    每个位置只被左、右指针中的一根处理一次，共 $n-1$ 轮、每轮 $O(1)$。空数组、单柱子天然返回 0，不需要特判；`height[left]` 与 `height[right]` 相等时走 `else` 分支也是正确的。

=== "对照：前后缀最高数组"

    ```python
    class Solution:
        def trap(self, height: list[int]) -> int:
            n = len(height)
            if n < 3:
                return 0
            left_max = height[:]
            right_max = height[:]
            for i in range(1, n):
                left_max[i] = max(left_max[i - 1], height[i])
            for i in range(n - 2, -1, -1):
                right_max[i] = max(right_max[i + 1], height[i])
            return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
    ```

    先把两侧最高值都求出来，再逐格套公式，正确性一眼可见，但多花一个 $O(n)$ 的数组。写双指针时可以留着它做对拍：随机高度数组跑几千组，两版结果一致才敢交。注意这里的 max 数组是**含自身**的，所以减完不会为负，不需要再套 `max(0, ...)`。

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 双指针 | $O(n)$ | $O(1)$ | 默认，面试写这一版 |
| 前后缀数组 | $O(n)$ | $O(n)$ | 讲解、验算、对拍 |
| 暴力 | $O(n²)$ | $O(1)$ | 只用于说明公式 |

其中 $n$ 为柱子数。双指针共 $n-1$ 轮、每轮常数操作，所以是 $O(n)$；**不是** $O(n \cdot \text{max height})$——高度只参与比较和加减，与数值范围无关。题目给到 2×10⁴ 根柱子，$O(n²)$ 的暴力会超时，$O(n)$ 两版都能过。

## 教学动画（HTML）

[讲解动画：双指针接雨水](42-trapping-rain-water-demo.html)

橙色虚线是 `leftMax`（左侧已见最高）、紫色虚线是 `rightMax`、蓝色是已接的雨水。每一步先比较 `height[left]` 与 `height[right]`，再结算更矮那一侧、把该侧指针往里挪一格，右侧面板同步高亮对应代码行并累加水量。空格播放 / 暂停，`←` `→` 单步，`R` 重置——盯着看「谁矮结算谁」以及 `leftMax`/`rightMax` 只增不减。

## 易错点

- **无条件先结算左侧（或右侧）**：只有更矮那一侧的水位才被确定。反例 `height = [3,0,4,0,2]`，正确答案是 5，但固定从左结算会得到 9——下标 3、4 的水本应由右侧最高的 2 兜住，却被左侧的 4 抬高了。判据只有一个：`height[left]` 与 `height[right]` 谁矮结算谁。
- **先累加再更新 max**：写成 `water += left_max - height[left]` 之后才 `left_max = max(...)`，遇到比左侧历史最高还高的柱子时会加一个负数，把前面攒的水扣掉。必须先更新再累加，这样 `max - height` 恒 ≥ 0。
- **「含自身」与「不含自身」的 max 混用**：前后缀数组若定义成 `left_max[i] = max(height[0..i-1])`（不含自身），`min(...) - height[i]` 就会在边缘位置为负，必须再套 `max(0, ...)` 或把初值设成 0。两种约定都能对，但同一份代码里只用一种。
- **以为高度 0 的位置可以跳过**：0 高度处往往积水最多（示例里 `height[2] = 0`，积 1 格；`height[5] = 0`，积 2 格）。不能写 `if height[i] == 0: continue`。
- **漏掉 `if n < 3: return 0`**：后缀数组版在 `n = 1` 时 `sum(min(0, 0) - height[0])` 会得到负数；双指针版则不需要这个特判，因为 `while left < right` 直接不进循环。换写法时容易把特判丢了。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：双指针](../index.md)
- 同类题：[11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)（双指针每次移动更矮的挡板，同一套「矮的一侧是瓶颈」直觉）· [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/)（接雨水的姊妹题，用的是单调栈）
