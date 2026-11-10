# 139. 单词拆分

!!! abstract "题单坐标"
    **Hot 20 · 第 13 类「动态规划」** ｜ 难度：中等 ｜ 标签：`字符串` `动态规划` `哈希表` `字典树`

    一句话套路：`dp[i]` 记「前 i 个字符能否拆」，枚举**最后一段词**（或切点），把「整串能否拆」化成「更短前缀能否拆」。

## 题干

> [力扣 139. 单词拆分](https://leetcode.cn/problems/word-break/)

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 `s` 则返回 `true`。

**注意**：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

**示例 1**

```text
输入：s = "leetcode", wordDict = ["leet", "code"]
输出：true
解释：返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
```

**示例 2**

```text
输入：s = "applepenapple", wordDict = ["apple", "pen"]
输出：true
解释：返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
注意，你可以重复使用字典中的单词。
```

**示例 3**

```text
输入：s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出：false
```

**提示**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` 和 `wordDict[i]` 仅由小写英文字母组成
- `wordDict` 中的所有字符串互不相同

## 思路

### 按词尾枚举 dp

`dp[i]` = 前缀 `s[:i]` 能否拆成字典词；`dp[0] = True`，因为空串是 0 个词的空拼接。

**为什么这样定义对**（不变量）：任何合法切分的最后一段，一定是字典里的某个词 `w`，并且它前面的 `s[:i-|w|]` 自身也必须可拆。反过来，只要存在一个 `w` 同时满足这两点，`s[:i]` 就可拆。于是

`dp[i] = any(dp[i - len(w)] and s[i - len(w):i] == w for w in wordDict)`

答案即 `dp[n]`。**单词可重复使用不需要额外处理**：`dp` 只记录「前缀能否拆」的结论，不消耗字典；同一个词在前面用过，后面照样能再匹配。

两个实现细节：① 先过滤空词和长度超过 `n` 的词，再把单词按长度**升序**排列，这样内层遇到 `len(w) > i` 就能直接 `break`；② 一旦 `dp[i]` 置真立刻 `break`，不必试完所有词。

### 对比：同一道题的几种砍法

| 写法 | 时间 | 空间 | 取舍 |
|:-----|:-----|:-----|:-----|
| 按词尾枚举 dp（主推） | $O(n m L)$ | $O(n)$ | 直接对着「最后一段是哪个词」写，最好解释 |
| 按切点枚举 dp | $O(n L^2)$ | $O(n)$ | 用 `set` 哈希查 `s[j:i]`，配 `max_len` 剪枝；词短时更快 |
| BFS 求可达性 | $O(n m L)$ | $O(n)$ | 下标当图节点，`i -> i+\lvert w \rvert`；碰到 `n` 立即返回 |
| 记忆化 DFS | $O(n m L)$ | $O(n)$ | 从每个位置往后试，找到一条就返回；注意递归深度 |
| trie + dp | $O(nL)$ + 建树 | $O(\sum \lvert w \rvert)$ | 字典大、公共前缀多时最划算 |

其中 $n = |s|$、$m = |wordDict|$、$L$ = 最长单词长度。切片比较和 `startswith` 都要按 $O(L)$ 计，不能当成 $O(1)$ 糊过去——这是这类题最常见的复杂度误判。

### 为什么主推按词尾

按切点枚举要「先枚举所有 `j`，再看子串在不在字典里」，而字典中词的长度是离散的；按词尾枚举直接沿字典走，天然只在可能命中的位置停下，写出来就是「最后一词是哪个」这一句话。

## 代码（带注释）

> LeetCode 提交时把函数包进 `class Solution` 即可；下面的代码都能在本地直接跑。第二栏沿用第一栏的 `from typing import List`。

=== "主推：按词尾枚举 dp"

    ```python
    from typing import List


    def word_break(s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if n == 0:
            return True                     # 空串是 0 个词的空拼接

        # 过滤空词和超长词；按长度升序，短词先试、超长就能 break
        words = sorted((w for w in wordDict if w and len(w) <= n), key=len)
        if not words:                       # 过滤完一个词都不剩：非空 s 必然拆不开
            return False

        dp = [False] * (n + 1)              # dp[i] = 前缀 s[:i] 能否拆成字典词
        dp[0] = True                        # 空串（0 个词的空拼接）可以拆
        for i in range(1, n + 1):           # i 是「词尾」位置
            for w in words:                 # 逐个词试当「最后一段」
                lw = len(w)
                if lw > i:                 # 升序：后面的词只会更长，放弃这个 i
                    break
                if dp[i - lw] and s[i - lw:i] == w:   # 前半段可拆 且 最后一段正好是 w
                    dp[i] = True
                    break                   # 找到一种切法就够，不必试完所有词
        return dp[n]
    ```

=== "对比：按切点枚举 dp"

    ```python
    def word_break_dp_index(s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if n == 0:
            return True                     # 空串是空拼接
        word_set = {w for w in wordDict if w}   # 空词一律过滤，否则会原地踏步
        if not word_set:
            return False                    # 字典为空：非空 s 必然拆不开
        max_len = min(max(len(w) for w in word_set), n)   # 切点最多只需要回看 max_len 个字符

        dp = [False] * (n + 1)              # dp[i] = 前缀 s[:i] 能否拆成字典词
        dp[0] = True                        # 空串可以拆
        for i in range(1, n + 1):           # i 是「词尾」位置
            lo = max(0, i - max_len)        # 切点 j 只在 [i-max_len, i-1]
            for j in range(i - 1, lo - 1, -1):
                if dp[j] and s[j:i] in word_set:   # 前半段可拆 且 最后一段正好在字典里
                    dp[i] = True
                    break                   # 找到一种切法就够
        return dp[n]
    ```

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 按词尾枚举 dp | $O(n m L)$ | $O(n)$ | 默认，好写也好讲 |
| 按切点枚举 dp | $O(n L^2)$ | $O(n)$ | 词短、字典大时 |
| 记忆化 DFS / BFS | $O(n m L)$ | $O(n)$ | 想尽早退出，或变形题要输出路径 |
| trie + dp | $O(nL)$ | $O(\sum \lvert w \rvert)$ | 字典巨大、前缀重合多 |

$m$ 个词每个长度不同，所以 $O(n m L)$ 只是上界；按长度排序 + 命中即 `break` 会把实际常数压得很低。LC 139 的规模（$n \le 300$）下，主推写法绰绰有余。

## 教学动画（HTML）

[▶ 打开交互动画](../assets/word-break.html){target=_blank .md-button}

动画用 `s = "leetcode"、wordDict = ["leet","code"]`：橙色是当前 `i` 和正在尝试的词，方框标出正在匹配的区间 `s[i-lw:i]`；蓝色表示前缀 `dp[i-lw] = False`，粉色表示子串和单词对不上，绿色是判定为可拆的 `dp` 格。`dp` 填完后，动画顺着 `parent` 从 `n` 往回跳，把切分结果回溯成 `leet | code`。空格播放/暂停，`←` `→` 单步，`R` 复位。

## 易错点

- **把空串判成 `False`**：`s == ""` 是「0 个词的空拼接」，应返回 `True`（字典为空时也是 `True`）。写成 `dp[0] = False` 或漏掉 `n == 0` 的出口就会错。
- **空字典 / 空词没处理**：`wordDict` 为空、或单词都比 `s` 长时，非空 `s` 必须返回 `False`——过滤后 `words` 为空要提前返回。若字典里混进 `""`，BFS / 记忆化会原地踏步（`i -> i+0`）死循环，必须一律过滤。
- **以为单词只能用一次**：题目允许重复使用，不要在匹配后把词从字典删掉或标记已用；`dp` 只看前缀结论，天然支持重复。
- **切片方向写反**：按词尾枚举时当前词是 `s[i-lw:i]`（以 `i` 结尾的那一段），不是 `s[i:i+lw]`；写成后者会读到后面的字符，`i` 靠后时还会越界。
- **提前 `break` 前忘了按长度排序**：`if lw > i: break` 只在 `words` 升序时成立；不排序就 `break`，会漏掉后面的短词，把 `True` 判成 `False`。
- **`max_len` 没和 `n` 取 min**：按切点枚举时下界是 `i-max_len`，若 `max_len > n` 且不与 `n` 取 min，`lo` 会一直是 0，剪枝白做。

## 延伸

- [← 返回 Hot 20 题单](../index.md) · [本类总览：动态规划](index.md)
- 要输出所有切分方案：[140. 单词拆分 II](https://leetcode.cn/problems/word-break-ii/)
- 同族的搜索题：[79. 单词搜索](https://leetcode.cn/problems/word-search/)（二维网格上找词，DFS + 回溯）
