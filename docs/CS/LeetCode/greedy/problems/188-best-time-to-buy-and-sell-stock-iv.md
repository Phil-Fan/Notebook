# 188. 买卖股票的最佳时机 IV

!!! abstract "题单坐标"
    **Hot 20 · 第 12 类「贪心 / 股票」** ｜ 难度：困难 ｜ 标签：`数组` `动态规划`

    一句话套路：`dp[t][i]` 记「前 i 天、最多 t 笔」，用 running max 把买入日枚举压成 $O(1)$；$k \ge n/2$ 时限制失效，直接累加所有正价差。

## 题干

> [力扣 188. 买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/)

给你一个整数数组 `prices` 和一个整数 `k`，其中 `prices[i]` 是某支给定的股票在第 `i` 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 `k` 笔交易。也就是说，你最多可以买 `k` 次，卖 `k` 次。

**注意**：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1**

```text
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2。
```

**示例 2**

```text
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出，这笔交易所能获得利润 = 6-2 = 4。
随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出，这笔交易所能获得利润 = 3-0 = 3。
```

**提示**

- `1 <= k <= 100`
- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 1000`

## 思路

### 朴素 dp：把「最后一笔」单独拆出来

定义 `dp[t][i]` = 只考虑前 `i` 天（第 `0..i-1` 天）、最多做 `t` 笔交易的最大利润；`dp[0][i] = dp[t][0] = 0`。

看最后一笔。若它在第 `i-1` 天卖出、买入日在 `j`：买入必须**严格早于**卖出，所以 `j <= i-2`；第 `j` 天之前只能做 `t-1` 笔，利润是 `dp[t-1][j]`；这一笔赚 `prices[i-1] - prices[j]`。再算上「第 `i-1` 天不卖」的情况：

$$dp[t][i] = \max\left(dp[t][i-1],\ \max_{0 \le j \le i-2}\left(dp[t-1][j] + prices[i-1] - prices[j]\right)\right)$$

逐格枚举 `j` 就是 $O(k n^2)$。

### running max：把内层枚举压成 O(1)

把第二项按 `j` 拆开，与 `j` 有关的只有 `dp[t-1][j] - prices[j]`，记它的前缀最大值为 `best`。`i` 每右移一天，候选集只多一个 `j = i-2`，于是 `best = max(best, prev[i-2] - prices[i-2])` 就能 $O(1)$ 更新，总时间降到 $O(k n)$。

### k >= n//2 时退化成贪心（这里最容易含糊）

`n` 天最多只做得成 $\lfloor n/2 \rfloor$ 笔「真正有意义」的交易：一笔交易要占「买入日 < 卖出日」两个不同的日子，交易之间又不能重叠。而如果前一笔在 `a` 天买、`b` 天卖，后一笔同一天 `b` 买、`c` 天卖，两笔可以直接合并成「`a` 买、`c` 卖」——利润 $(p_b-p_a)+(p_c-p_b)=p_c-p_a$ 不变，交易数更少。所以 `k >= n//2` 时笔数上限形同虚设，答案就是「不限次数」的最大利润：

$$\sum_{i=1}^{n-1} \max(0,\ prices[i] - prices[i-1])$$

道理是：只要明天涨，今天手里就该有货；把一条上涨路径切成若干段，每段的价差恰好等于逐日正价差之和。此时 $O(n)$。这也是很多实现在一开始就 `k = min(k, n // 2)` 的依据——既避免 `k` 很大时开巨表，也让 `k >= n//2` 的分支能直接短路。

### 另外两种写法

- **hold / free 滚动**：按天推进，`hold[t]` 表示「第 `t` 笔进行中」的最大利润，`free[t]` 表示「第 `t` 笔已完成」，空间压到 $O(k)$。
- **状态机**：把「第几笔 × 是否持股」摊平成 `2k+1` 个状态做一维滚动，代码更机械，本质相同。

## 代码（带注释）

> 按力扣提交格式写。只用内置类型。

=== "主推：running max 的 dp（O(k·n)）"

    ```python
    class Solution:
        def maxProfit(self, k: int, prices: list[int]) -> int:
            n = len(prices)
            if n < 2 or k <= 0:
                return 0
            k = min(k, n // 2)
            neg = -(10**18)
            dp = [[0] * (n + 1) for _ in range(k + 1)]
            for t in range(1, k + 1):
                prev, cur = dp[t - 1], dp[t]
                best = neg
                for i in range(2, n + 1):
                    best = max(best, prev[i - 2] - prices[i - 2])
                    cur[i] = max(cur[i - 1], prices[i - 1] + best)
            return dp[k][n]
    ```

=== "空间更省：hold / free 滚动（O(k)）"

    ```python
    def max_profit_hold_free(prices: list[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k <= 0:             # 同上：不足两天做不成一笔交易
            return 0
        k = min(k, n // 2)
        neg = -(10**18)
        hold = [neg] * (k + 1)
        free = [neg] * (k + 1)
        free[0] = 0                     # 0 笔交易且空仓：利润 0 是唯一合法的起点
        for p in prices:                # 按天推进，数组里只留上一状态
            for t in range(1, k + 1):   # 第 t 笔：只能从「已完成 t-1 笔」的状态转过来
                hold[t] = max(hold[t], free[t - 1] - p)   # 用第 t 笔买入
                free[t] = max(free[t], hold[t] + p)       # 第 t 笔卖出
        return free[k]
    ```

=== "k 大时走贪心（O(n)）"

    ```python
    def max_profit_greedy(prices: list[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k <= 0:                     # 同上：不足两天做不成一笔交易
            return 0
        if k >= n // 2:                       # 交易上限形同虚设
            # 每段上涨都吃满：相邻正价差之和，等于一次低买高卖的利润
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))
        return max_profit_hold_free(prices, k)  # 上限真有约束时退回滚动 dp
    ```

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 朴素 dp（枚举买入日） | $O(k n^2)$ | $O(k n)$ | 只用来推导递推式，不要交 |
| running max | $O(k n)$ | $O(k n)$ | 主推，递推关系最清楚 |
| hold / free 滚动 | $O(k n)$ | $O(k)$ | 想省空间、代码也短 |
| 状态机 | $O(k n)$ | $O(k)$ | 习惯状态机模板时 |
| k 大时贪心 | $O(n)$ | $O(1)$ | `k >= n//2`（含无限笔的同类题） |

LC 188 的约束是 $k \le 100$、$n \le 1000$，$O(k n)$ 完全够用；真正要防的是 `k` 无脑建表。

## 教学动画（HTML）

<iframe src="188-best-time-to-buy-and-sell-stock-iv-demo.html" title="dp 表" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

动画用 `prices = [3,2,6,5,0,3]、k = 2` 逐格填 `dp[t][i]`：黄色是当前卖出日/当前格，青色标出 `best` 对应的买入日 `j`（argmax），蓝色是参考的上一层 `dp[t-1][·]`，虚线格是「今天不卖」时的 `dp[t][i-1]`。每格只做两件事——先把新买入日 `j = i-2` 吸收进 `best`，再用 `prices[i-1] + best` 与 `dp[t][i-1]` 取 max。空格播放/暂停，`←` `→` 单步，`R` 复位。

## 易错点

- **买入日写成 `j <= i-1`（同日进出）**：结果不会错，但白白多出一批「同一天买入又卖出」的 0 利润状态，把常数抬高；干净写法是 `j <= i-2`，`best` 的新候选也从 `i-2` 起。
- **`best` 的更新时序反了**：正确顺序是「先把 `j = i-2` 吸收进 `best`，再算 `dp[t][i]`」。若先算后吸收，就漏掉 `j = i-2` 这个唯一的新候选，答案偏小。
- **用了同层 `dp[t][j]` 而不是上层 `dp[t-1][j]`**：第 `j` 天要用来买入，之前只能做 `t-1` 笔；写成同层会把这笔和之前的交易算到一起，笔数限制失效。
- **`k` 大时硬建表**：表有 `k` 行，既慢又占内存。先 `k = min(k, n // 2)`；已经超过 $n/2$ 就直接走贪心分支。
- **以为必须恰好做 `k` 笔**：题面是「最多 `k` 笔」，`dp[t][i]` 天然允许少做、且对 `t` 单调不减，答案直接取 `dp[k][n]`，不用再对 `t` 取 max。
- **hold / free 用 0 初始化**：`hold` 从 0 起等于允许「没买就卖」，会凭空多出利润；不可达状态必须用 `NEG` 占位。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：贪心](../index.md)
- 去掉 `k` 的版本：[121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)（只能一笔）· [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)（无限笔，就是这里的贪心分支）
- `k = 2` 的特例：[123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/)
