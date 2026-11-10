# 72. 编辑距离

!!! abstract "题单坐标"
    **Hot 20 · 第 14 类「多维动态规划」** ｜ 难度：中等 ｜ 标签：`字符串` `动态规划`

    一句话套路：`dp[i][j]` 是把 `word1` 前 `i` 个变成 `word2` 前 `j` 个的最少操作数。末字符相同就免费沿用左上；否则在替换、删除、插入里取最小再加 1。

## 题干

> [力扣 72. 编辑距离](https://leetcode.cn/problems/edit-distance/)

给你两个单词 `word1` 和 `word2`，请返回将 `word1` 转换成 `word2` 所使用的最少操作数。

你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符

**示例 1**

```text
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse（替换 'h' → 'r'）
rorse -> rose（删除 'r'）
rose -> ros（删除 'e'）
```

**示例 2**

```text
输入：word1 = "intention", word2 = "execution"
输出：5
```

**提示**

- `0 <= word1.length, word2.length <= 500`
- `word1` 和 `word2` 由小写英文字母组成

## 思路

`dp[i][j]`：`word1[:i]` 变成 `word2[:j]` 的最少操作数。三个操作对应三个相邻格子：

| 操作 | 含义 | 从哪来 |
|:-----|:-----|:-------|
| 替换 | 把 `word1[i-1]` 改成 `word2[j-1]` | `dp[i-1][j-1]`，末字符不同才付 1 |
| 删除 | 删掉 `word1[i-1]`，剩下的去匹配 `word2[:j]` | `dp[i-1][j]`，付 1 |
| 插入 | 在 `word1` 末尾插入 `word2[j-1]`，相当于 `word2` 少看一个字符 | `dp[i][j-1]`，付 1 |

末字符相同的时候，替换的代价是 0，而且不会比「先删再插」更贵，所以直接等于左上角。否则：

$$dp[i][j] = 1 + \min(dp[i-1][j-1],\ dp[i-1][j],\ dp[i][j-1])$$

边界是空串：`dp[i][0] = i`（删掉 `i` 个字符），`dp[0][j] = j`（插入 `j` 个字符）。

**走一遍 `"horse"` → `"ros"`。**

|  | ε | r | o | s |
|:--|:--|:--|:--|:--|
| ε | 0 | 1 | 2 | 3 |
| h | 1 | 1 | 2 | 3 |
| o | 2 | 2 | 1 | 2 |
| r | 3 | 2 | 2 | 2 |
| s | 4 | 3 | 3 | 2 |
| e | 5 | 4 | 4 | 3 |

`(1,1)`：`h` 和 `r` 不同，min(0, 1, 1)+1 = 1，一次替换。`(2,2)`：两个 `o` 相同，直接拿左上的 1。右下角 3，和示例的三步一致。

## 代码（带注释）

> 按力扣提交格式写：一个 `Solution` 类。只用内置类型。

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )
        return dp[m][n]
```

两个空串的距离是 0，循环体不执行。只比其中一个空，边界循环会把整列或整行填成下标。

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 二维 dp | $O(mn)$ | $O(mn)$ | 默认 |
| 滚动一行 | $O(mn)$ | $O(\min(m,n))$ | 只要距离、要省空间。左上角得先存下来 |
| 递归不记忆化 | 指数 | $O(m+n)$ | 会超时 |

两条串最长 500，$O(mn) = 2.5 \times 10^5$，完整二维表足够。

## 教学动画（HTML）

<iframe src="72-edit-distance-demo.html" title="编辑距离 · horse → ros" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

表从边界开始逐格填。末字符相同就抄左上，否则在左上、上、左三个数里取最小再加 1，格子上标出选了哪一种操作。空格播放 / 暂停，`←` `→` 单步，`R` 重置。

## 易错点

- **相同字符也加 1**：`"a" → "a"` 会得到 1。相同应该直接等于左上，代价是 0。
- **边界填 0**：空串变成 `"ros"` 需要 3 次插入。第 0 行如果全是 0，后面每一格都会偏小。
- **插入和删除的方向记反**：从「word1 变成 word2」来看，删的是 word1 的字符（往上走，少看 word1），插的是 word2 的字符（往左走，少看 word2）。数值上两个方向都在 `min` 里，记反了故事，代码只要三个邻居都在就不会错。
- **和 LCS 的「相等就加 1」搞混**：编辑距离在相等时是**不加代价**，把左上原样拿下来。LCS 才是左上加 1。两题的表长得很像，转移的那一笔正好相反。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：动态规划](../index.md)
- 同类题：[1143. 最长公共子序列](1143-longest-common-subsequence.md) · [583. 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/)（只允许删除，距离是 `m + n - 2·LCS`）
