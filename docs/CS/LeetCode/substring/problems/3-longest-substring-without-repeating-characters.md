# 3. 无重复字符的最长子串

!!! abstract "题单坐标"
    **Hot 20 · 第 3 类「滑动窗口」** ｜ 难度：中等 ｜ 标签：`哈希表` `字符串` `滑动窗口`

    一句话套路：右指针把字符推进窗口，窗口里一旦出现重复就把左指针收到「这个字符上一次出现位置的右边」，收缩完成后再记长度。

## 题干

> [力扣 3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

给定一个字符串 `s`，请你找出其中不含有重复字符的**最长子串**的长度。

**示例 1**

```text
输入：s = "abcabcbb"
输出：3
解释：因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2**

```text
输入：s = "bbbbb"
输出：1
```

**示例 3**

```text
输入：s = "pwwkew"
输出：3
解释：无重复字符的最长子串是 "wke"，长度为 3。请注意，"pwke" 是一个子序列，不是子串。
```

**提示**

- `0 <= s.length <= 5 * 10^4`
- `s` 由英文字母、数字、符号和空格组成

## 思路

合法窗口的判据只有一条：**每个字符在窗口里最多出现一次**。右指针负责扩张，左指针只在这条被打破时往右收。

记 `last[ch]` 为字符 `ch` 上一次出现的下标。扫到 `right` 时：

- 若 `ch` 曾经出现过，而且 `last[ch] >= left`，说明它还在当前窗口里，左边界直接跳到 `last[ch] + 1`。
- 然后把 `last[ch]` 更新成 `right`。
- 窗口 `[left, right]` 此时无重复，用 `right - left + 1` 更新答案。

记录时机在收缩**之后**。这和 [76 最小覆盖子串](76-minimum-window-substring.md) 相反：76 要的是最短覆盖，一合法就边缩边记；本题要的是最长无重复，必须先把重复赶出去，剩下的窗口才有资格参与比较。

左指针只会右移，每个字符进出窗口各一次。用「上次下标」直接跳，和用计数 `while` 一格一格收，答案一样；跳转少几次循环，计数版更贴近「窗口模板」。

**走一遍示例。** `s = "abcabcbb"`。

| right | 字符 | 动作 | 窗口 | 长度 | best |
|:------|:-----|:-----|:-----|:-----|:-----|
| 0 | a | 首次进入 | `a` | 1 | 1 |
| 1 | b | 首次进入 | `ab` | 2 | 2 |
| 2 | c | 首次进入 | `abc` | 3 | 3 |
| 3 | a | `last['a']=0` 仍在窗口内，left 跳到 1 | `bca` | 3 | 3 |
| 4 | b | left 跳到 2 | `cab` | 3 | 3 |
| 5 | c | left 跳到 3 | `abc` | 3 | 3 |
| 6 | b | left 跳到 5 | `cb` | 2 | 3 |
| 7 | b | left 跳到 7 | `b` | 1 | 3 |

答案是 3。`pwwkew` 里第二次 `w` 会把窗口从 `pw` 收成 `w`，再吃进 `k`、`e` 得到 `wke`，长度 3；再遇到 `w` 收到 `kew`，长度仍是 3。

## 代码（带注释）

> 按力扣提交格式写：一个 `Solution` 类。只用内置类型。

=== "主推：上次下标，左指针直接跳"

    ```python
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            last: dict[str, int] = {}
            left = best = 0
            for right, ch in enumerate(s):
                if ch in last and last[ch] >= left:
                    left = last[ch] + 1
                last[ch] = right
                best = max(best, right - left + 1)
            return best
    ```

    `last[ch] >= left` 这一句不能省。字符可能出现在已经移出的窗口左边，那种旧下标不能把 `left` 再往回拉。空串不进循环，返回 0。

=== "对照：计数窗口，重复就一格格收缩"

    ```python
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            window: dict[str, int] = {}
            left = best = 0
            for right, ch in enumerate(s):
                window[ch] = window.get(ch, 0) + 1
                while window[ch] > 1:
                    window[s[left]] -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best
    ```

    和「滑动窗口模板」逐行对应：右扩、`while` 不合法就收缩、收缩完再记答案。字符集很大时字典只存窗口里真正出现过的键，和 128 长度的计数数组等价。

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 上次下标 | $O(n)$ | $O(\Sigma)$ | 默认 |
| 计数 + while 收缩 | $O(n)$ | $O(\Sigma)$ | 想和 76 题共用一套模板时 |
| 暴力枚举子串 | $O(n^2)$ | $O(\Sigma)$ | 只用来对照 |

$n = |s|$，$\Sigma$ 是出现过的字符种类。左指针不回退，所以两个指针版都是 $O(n)$，不是 $O(n^2)$。$n$ 到 $5 \times 10^4$，暴力枚举所有子串会超时。

## 教学动画（HTML）

<iframe src="3-longest-substring-without-repeating-characters-demo.html" title="无重复字符的最长子串" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

字符串上浅蓝是当前窗口，主色是正在进入的 `right`。重复出现时左边界跳到上一次该字符的右边，右侧面板同步窗口内容和 `best`。空格播放 / 暂停，`←` `→` 单步，`R` 重置。

## 易错点

- **收缩之前就更新 best**：窗口里已经有两个相同字符，长度会把非法窗口算进去。`abcabcbb` 在下标 3 如果先记再收，会得到长度 4。
- **`left = last[ch]` 少加 1**：左边界停在重复字符自己身上，窗口里仍然有两个 `a`。
- **旧下标把 left 拉回去**：`last[ch]` 若已经小于 `left`，说明那个字符不在窗口里。写成 `left = last[ch] + 1` 而不判断 `>= left`，左指针会倒退，窗口重新变非法。`abba` 是经典反例：处理最后一个 `a` 时，`last['a']` 还是 0。
- **把子序列当子串**：`pwwkew` 的 `pwke` 不是连续区间，滑动窗口不会、也不该把它算进去。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：子串 / 滑动窗口](../index.md)
- 同类题：[76. 最小覆盖子串](76-minimum-window-substring.md)（合法就收缩，收缩中记最短）· [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)（定长窗口）
