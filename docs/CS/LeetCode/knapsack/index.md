# 0-1 背包

有容量 `capacity`，`n` 件物品，第 `i` 件重量 `weight[i]`、价值 `value[i]`，每件最多放一次。求能装下的最大价值。

`dp[i][c]` 表示只考虑前 `i` 件、容量为 `c` 时的最大价值：

\[
dp[i][c] = \max(dp[i-1][c],\ dp[i-1][c-w_i] + v_i)
\]

第二项只在 `c >= w_i` 时存在。当前行只依赖上一行，所以可以压成一维数组。内层必须从大到小枚举容量，否则同一件物品会被用两次。

```python
class Solution:
    def knapsack(self, capacity: int, weight: list[int], value: list[int]) -> int:
        dp = [0] * (capacity + 1)
        for w, v in zip(weight, value):
            for c in range(capacity, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[capacity]
```

样例：容量 10，物品 `(3, 4), (4, 6), (5, 7)`，答案是 13（后两件）。

要求恰好装满时，除了 `dp[0] = 0`，其余容量初始化成一个很小的数，表示「还没凑出这个容量」。最后 `dp[capacity]` 仍是那个很小的数，就说明装不满。

```python
class Solution:
    def knapsack_exact(self, capacity: int, weight: list[int], value: list[int]) -> int:
        neg = -(10**18)
        dp = [neg] * (capacity + 1)
        dp[0] = 0
        for w, v in zip(weight, value):
            for c in range(capacity, w - 1, -1):
                dp[c] = max(dp[c], dp[c - w] + v)
        return dp[capacity] if dp[capacity] > neg // 2 else 0
```

完全背包（每件可以拿无限次）只改枚举方向：容量从小到大，这样 `dp[c - w]` 已经是「本轮可以再用一次」的结果。

```python
def complete_knapsack(capacity: int, weight: list[int], value: list[int]) -> int:
    dp = [0] * (capacity + 1)
    for w, v in zip(weight, value):
        for c in range(w, capacity + 1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]
```

要输出选了哪些物品时，用二维 `dp` 从后往前看：若 `dp[i][c] == dp[i - 1][c]`，第 `i` 件没选；否则选了它，容量减去它的重量。
