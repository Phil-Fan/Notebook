# 贪心 · 股票 | Greedy

!!! abstract "Hot 20 · 第 12 类"
    **什么时候想到它**：每一步都能做「局部最优且不后悔」的选择，并且能说清为什么它不破坏全局最优。
    **核心动作**：维护一个就够了的状态（最远可达下标 / 历史最低价 / 正价差之和），一次扫描出答案。

## 套路

- **可达性（跳跃游戏）**：维护 `reach = max(reach, i + nums[i])`，一旦 `i > reach` 就失败。
- **股票 · 不限笔数**：只要明天涨，今天就该有货 → 答案 = 所有正价差之和，$O(n)$。
- **股票 · 笔数上限 k**：写成「第 t 笔 × 空仓/持股」的状态机（即 `dp[t][i]`）；当 $k \ge n/2$ 时笔数上限形同虚设，直接退化成上面的贪心。

贪心的证明方式一般是**交换论证**：把任意一个最优解逐步换成贪心解，并说明每一步都不变差。证不出来就老实写 dp。

## 题目

| 题目 | 难度 | 状态 | 一句话 |
|:-----|:-----|:-----|:-------|
| [188 买卖股票的最佳时机 IV](problems/188-best-time-to-buy-and-sell-stock-iv.md) | 困难 | ✔ 已整理 | `dp[t][i]` + running max，笔数上限失效时退化成贪心 |
| [55 跳跃游戏](https://leetcode.cn/problems/jump-game/) | 中等 | ☐ 待补 | 维护最远可达下标 |
| [121 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | 简单 | 相关 | 只能一笔：维护历史最低价 |
| [122 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) | 中等 | 相关 | 不限笔数：累加正价差 |
| [123 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) | 困难 | 相关 | k = 2 的股票 dp |

## 易错点

- 贪心必须有证明，别把「看起来对」当结论。
- 股票题一律「先买后卖、不同日进出」：`j <= i-2`，写成同日进出不会错但多出 0 利润状态。
- 跳跃游戏：`reach` 的判断和更新顺序要写清，`i > reach` 就立刻失败。

## 相关

- [← 返回 Hot 20 题单](../index.md)
- 同属「一次扫描维护一个状态」：[子串](../substring/index.md) 的滑动窗口是最长/最短版的同类结构。
