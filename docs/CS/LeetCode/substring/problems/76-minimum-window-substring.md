# 76. 最小覆盖子串

!!! abstract "题单坐标"
    **Hot 20 · 第 4 类「子串」** ｜ 难度：困难 ｜ 标签：`哈希表` `字符串` `滑动窗口`

    一句话套路：右指针负责把 `t` 的字符账「凑满」，左指针负责凑满之后「尽量多扔」，窗口每合法一次就记一次最短答案。

## 题干

> [力扣 76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

给你一个字符串 `s`、一个字符串 `t`。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""`。

**注意**

- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。

**示例 1**

```text
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2**

```text
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3**

```text
输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。
```

**提示**

- `m == s.length`，`n == t.length`
- `1 <= m, n <= 10^5`
- `s` 和 `t` 由英文字母组成

**进阶**：你能设计一个在 $O(m+n)$ 时间内解决此问题的算法吗？

## 思路

**为什么可以用滑动窗口（单调性）。** 记窗口为 `[left, right]`：

- **合法性对扩张单调**：窗口变大只会多字符、不会少字符，所以 `[left, right]` 合法时，`[left, right']`（`right' > right`）一定也合法。这意味着「右端点固定时，越长的窗口越没用」，最优解一定出现在「刚凑满就停手」的位置。
- **左端点可以贪心右移**：一旦窗口合法，就尽量把左端点往右推，直到推坏为止——推坏之前的最后一个合法状态，就是以当前右端点结尾的最短覆盖。
- 由此得到「右扩 → 凑满 → 左缩 → 记录」的双指针扫描：右指针只前进、左指针也只前进，每个字符最多进窗口一次、出窗口一次，所以是 $O(|s| + |t|)$ 而不是 $O(|s|^2)$。

**正确性的一句话证明。** 设真正的最短解是 `[l*, r*]`。当右指针扫到 `r*` 时，窗口 `[left, r*]` 必合法（因为 `left ≤ l*`，窗口只会更大）；左指针会一直右移，但不会越过 `l*`——越过就意味着 `[l*+1, r*]` 也合法，与 `[l*, r*]` 最短矛盾。所以这一轮左指针恰好停在 `l*`，答案被记录，长度不会漏。

**怎么把「是否覆盖」判成 O(1)。** 不要每次都去比一遍计数数组。维护三个量：

- `need[c]`：`t` 里字符 `c` 要几个；`required`：`t` 里不同字符的种数。
- `window[c]`：当前窗口里字符 `c` 有几个。
- `formed`：已经「刚好达标」（`window[c] == need[c]`）的字符**种数**。`formed == required` 就是窗口合法。

只有 `window[c]` 从 `need[c]-1` 加到 `need[c]` 时 `formed` 才 +1；左缩时只有 `window[c]` 从 `need[c]` 降到 `need[c]-1` 时 `formed` 才 -1。这样每次移动指针都是常数时间。

**扫描步骤。**

1. 预处理 `t`：填 `need`，统计 `required`。
2. 右指针扩张：`window[c] += 1`，若恰好追平 `need[c]` 则 `formed += 1`。
3. 只要 `formed == required` 就循环：**先**更新答案（当前窗口长度更短才更新），**再**把左端字符移出窗口、必要时 `formed -= 1`、`left += 1`。
4. 扫完返回记录的窗口，没记过就返回 `""`。

**走一遍示例。** 只列「凑齐」的时刻：

| 右指针到 | 窗口 | 发生了什么 |
|:---------|:-----|:-----------|
| 5 | `[0..5] = "ADOBEC"` | 第一次凑齐 A/B/C，记录长度 6 |
| 10 | `[1..10] = "DOBECODEBA"` | 凑齐，但缩到最短也只有 6（`"CODEBA"`），不更新；再缩就丢 C |
| 12 | `[6..12] = "ODEBANC"` | 凑齐，缩到 `"EBANC"` 记 5，再缩到 `"BANC"` 记 4 |
| 结束 | — | 返回 `s[9:13] = "BANC"` |

## 代码（带注释）

> 按力扣提交格式写：一个 `Solution` 类。只用内置类型。

=== "主推：128 桶 + formed"

    ```python
    class Solution:
        def minWindow(self, s: str, t: str) -> str:
            """need 记欠账，window 记窗口，formed 记已达标的字符种数。"""
            if not s or not t or len(s) < len(t):
                return ""

            need = [0] * 128
            window = [0] * 128
            required = 0
            for ch in t:
                c = ord(ch)
                if need[c] == 0:
                    required += 1
                need[c] += 1

            left = 0
            formed = 0
            best_len = len(s) + 1
            best_left = 0
            for right, ch in enumerate(s):
                c = ord(ch)
                window[c] += 1
                if window[c] == need[c]:
                    formed += 1
                while formed == required:
                    if right - left + 1 < best_len:
                        best_len = right - left + 1
                        best_left = left
                    lc = ord(s[left])
                    window[lc] -= 1
                    if window[lc] < need[lc]:
                        formed -= 1
                    left += 1
            if best_len == len(s) + 1:
                return ""
            return s[best_left:best_left + best_len]
    ```

    只支持 ASCII：`ord(ch)` 直接当下标，题目给的是英文字母所以够用。若输入可能含中文或 emoji，会 `IndexError`，把定长数组换成 `dict`、`ord(ch)` 换成 `ch` 即可（结构不变，见下方「复杂度」）。

=== "更省：单数组 + missing"

    ```python
    class Solution:
        def minWindow(self, s: str, t: str) -> str:
            """一个数组：正数表示还欠，负数表示多了。missing 归零即窗口合法。"""
            if not s or not t or len(s) < len(t):
                return ""
            need = [0] * 128
            for ch in t:
                need[ord(ch)] += 1
            missing = len(t)
            left = start = end = 0
            for right, ch in enumerate(s, 1):
                c = ord(ch)
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
                if missing == 0:
                    while need[ord(s[left])] < 0:
                        need[ord(s[left])] += 1
                        left += 1
                    if end == 0 or right - left < end - start:
                        start, end = left, right
                    need[ord(s[left])] += 1
                    missing += 1
                    left += 1
            return s[start:end]
    ```

    一个数组同时当「欠账表」和「窗口计数」用：正数是还欠、负数是多余。代价是 `right` 改成从 1 开始计数，窗口边界容易写错。

    字符集不限的写法不用单独写一版：把两个定长数组换成 `dict`、把 `ord(ch)` 换成 `ch`，结构一模一样。中文也验过：`min_window("小明小红小明", "红明")` 返回 `"明小红"`。

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 128 桶 + formed | $O(\vert s\vert + \vert t\vert)$ | $O(128)$ | 默认，ASCII 输入最快最稳 |
| 单数组 + missing | $O(\vert s\vert + \vert t\vert)$ | $O(128)$ | 想少一个计数数组、背模板 |
| dict + formed | $O(\vert s\vert + \vert t\vert)$ 期望 | O(字符集大小) | 字符集不是 ASCII 时用它 |

三种写法时间同阶：右指针把 `s` 扫一遍，左指针总共也只移动 `|s|` 步，每步常数操作，所以是 $O(|s| + |t|)$。空间只跟字符集有关，与字符串长度无关——这就是滑窗比「枚举所有子串」($O(|s|^2)$ 个窗口) 强的地方。实现的差别只在常数：128 桶预分配两个定长数组，访问无哈希开销。

## 教学动画（HTML）

[讲解动画：滑动窗口](76-minimum-window-substring-demo.html)

动画用 `s = "ADOBECODEBANC"`、`t = "ABC"` 把整个扫描过程拆成 38 步：

- `s` 的每个字符一格，当前窗口 `[left, right]` 高亮，橙色箭头指着右指针，绿色框是当前最优窗口 `"BANC"`；
- 下方三个计数块是 `t` 的每个字符「窗口里有几个 / 需要几个」，凑齐会变绿；
- 进度条就是 `formed / required`，一眼看出窗口什么时候合法；
- 右侧同步高亮对应代码行，能看到「右扩 → 凑齐 → 记录 → 左缩」的循环怎么转。

空格播放 / 暂停，`←` `→` 单步，`R` 重置。重点看 `formed` 从 2 变 3（凑齐）、从 3 掉回 2（左缩踢掉了必需字符）的那几个瞬间。

## 易错点

- **`window[c] += 1` 和 `if window[c] == need[c]` 的顺序反了**：必须先加再比。写成先比的话，窗口里第一个新字符恰好 `window[c] == 0 == need[c]`（当 `c` 不在 `t` 里时）会被误判成达标，`formed` 虚高，`while` 提前进不去或提前退出。
- **`formed` 统计的不是「种数」**：`formed` 只在 `window[c] == need[c]` 这一瞬间 +1，代表「这个字符的配额刚好齐了」。如果改成「窗口里出现过的所有字符都计入」，`t` 之外的字符也会污染 `formed`，`formed == required` 永远凑不准。
- **左缩时先移指针再更新答案**：若写成 `left += 1` 之后才 `if right - left + 1 < best_len`，长度会少 1，算出来的答案比真实最短解短一格（甚至切出错误的子串）。必须在窗口仍合法时先记录、再移左指针。
- **`best_len` 的哨兵与返回值的判断不一致**：初值写 `len(s) + 1`，末尾就必须用同一个表达式判断「没更新过」并返回 `""`；顺手写成 `if best_len == len(s): return ""` 时，长度恰好等于 `|s|` 的合法答案会被吞掉。
- **单数组版的 off-by-one**：`for right, ch in enumerate(s, 1)` 的 `right` 是 1-based，窗口长度是 `right - left`，切片是 `s[start:end]`（`end` 开区间）。混进 0-based 的直觉就会整体错一位，或者多切一个字符。
- **单数组版忘了「恢复左端并右移一格」**：`while need[...] < 0` 结束、记录完答案后，必须把左端字符加回去、`missing += 1`、`left += 1`，强制踢掉一个必需字符，否则下一轮 `missing` 仍为 0，会反复处理同一个窗口，甚至死循环。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：子串](../index.md)
- 同类题：[3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)（窗口里维护「无重复」，另一类滑窗）· [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)（固定长度窗口 + 计数键）· [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)（同一套计数 + 定长滑窗）
- 对照 [讲解动画](76-minimum-window-substring-demo.html) 看 `formed` 从 2 变 3、从 3 变 2 的那几个瞬间。
