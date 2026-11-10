# 力扣 LeetCode

按一份流传很广的「**Hot 20 题单**」整理的题解库：14 类高频题型、20 道题。

- **按考察点分文件夹**：数据结构在 `DS/` 下再分子目录（链表、栈、队列、树、图、哈希）。每个题型目录里，`index.md` 写识别标志和模板，题目放在 `problems/`，一题一个 Markdown。
- **每题一页**：文件名是 `题目号-英文名.md`。讲解动画是同目录下的 HTML，题解页里用 iframe 直接嵌出来，例如 [49 的讲解](DS/hash/problems/49-group-anagrams-demo.html)。
- 代码用 Python，按力扣的 `class Solution` 来写，只用内置类型。
- 题解来自实际刷题记录，不是抄题解：代码都在本地跑过样例，每道题都配了可以单步播放的**教学动画**（哈希入桶、双指针结算、滑动窗口、链表掉头、dp 表填格）。
- Hot 20 的 **20 题**都已整理成页（✔），每题都有可以单步播放的教学动画。

!!! tip "一页纸速记（A4 · 20 题全）"

    20 道题各一句话思路（带关键公式），压在一页里；★ 表示站内已有完整题解：

    [速记 PDF](assets/hot20-cheatsheet.pdf) · [网页版](assets/hot20-cheatsheet.html)

!!! tip "怎么用"

    - **第一次刷**：先只看「题干」自己动手，卡住了再读「思路」和动画，最后对代码。
    - **二刷复习**：只看每页的「易错点」和复杂度表，能在 3 分钟内复述出做法就算过。
    - **面试前**：从下面总表的「题型」点进对应目录，先把那一类的套路和模板骨架过一遍。

## 进度总览

题单共 **14 类 / 20 题**，20 题都已写进对应题型目录。带链接的「题型」是本库的分类目录。

| # | 题型 | Hot 20 题目 | 核心套路（一句话） |
|:--|:--|:--|:--|
| 1 | [哈希](DS/hash/index.md) | ✔ [49 字母异位词分组](DS/hash/problems/49-group-anagrams.md) | 造「只依赖字母构成」的规范形当键：排序 / 计数向量 |
| 2 | [双指针](two-pointers/index.md) | ✔ [42 接雨水](two-pointers/problems/42-trapping-rain-water.md) · ✔ [15 三数之和](two-pointers/problems/15-3sum.md) | 数组两端各站一个指针，每次结算「已经确定」的那一侧；三数之和靠排序 + 固定一个数 + 左右夹逼去重 |
| 3 | [滑动窗口](substring/index.md) | ✔ [3 无重复字符的最长子串](substring/problems/3-longest-substring-without-repeating-characters.md) | 右指针负责扩张，左指针负责在「违规」时收缩，窗口内永远维护一个合法状态 |
| 4 | [子串](substring/index.md) | ✔ [76 最小覆盖子串](substring/problems/76-minimum-window-substring.md) | 滑窗 + 「还欠多少」计数：欠账归零就收缩左边界并记录最短答案 |
| 5 | [矩阵](matrix/index.md) | ✔ [48 旋转图像](matrix/problems/48-rotate-image.md) | 原地操作拆两步：先转置再左右翻转（顺时针），等价于四格轮换 |
| 6 | [链表](DS/linked-list/index.md) | ✔ [25 K 个一组翻转链表](DS/linked-list/problems/25-reverse-nodes-in-k-group.md) · ✔ [146 LRU 缓存](DS/linked-list/problems/146-lru-cache.md) | 哨兵 `dummy` 让第一组和后面共用一套逻辑；LRU = 哈希表 + 双向链表 |
| 7 | [二叉树](DS/tree/index.md) | ✔ [199 二叉树的右视图](DS/tree/problems/199-binary-tree-right-side-view.md) | 层序遍历取每层最后一个，或 DFS 按「深度首次到达」记录 |
| 8 | [图论](DS/graph/index.md) | ✔ [200 岛屿数量](DS/graph/problems/200-number-of-islands.md) | 网格当图：每碰到一个陆地就 DFS/BFS 淹掉整块，计数即连通块个数 |
| 9 | [回溯](backtrack/index.md) | ✔ [22 括号生成](backtrack/problems/22-generate-parentheses.md) | 只往下走「合法」的分支：左括号不超上限、右括号不超左括号 |
| 10 | [栈](DS/stack/index.md) | ✔ [20 有效的括号](DS/stack/problems/20-valid-parentheses.md) | 左括号入栈，右括号查栈顶是否配对，最后栈必须为空 |
| 11 | [堆](DS/queue/index.md) | ✔ [215 数组中的第 K 个最大元素](DS/queue/problems/215-kth-largest-element-in-an-array.md) | 大小为 k 的小顶堆，或快速选择（平均 O(n)）；别全排序 |
| 12 | [贪心](greedy/index.md) | ✔ [188 买卖股票的最佳时机 IV](greedy/problems/188-best-time-to-buy-and-sell-stock-iv.md) · ✔ [55 跳跃游戏](greedy/problems/55-jump-game.md) | 维护「能到达的最远下标」，走不到下一个就失败；股票题每类交易数是一维 dp |
| 13 | [动态规划](dynamic-programming/index.md) | ✔ [139 单词拆分](dynamic-programming/problems/139-word-break.md) | `dp[i]` = 前缀 `s[:i]` 能否拆出，转移看字典里每个词的尾巴 |
| 14 | [多维动态规划](dynamic-programming/index.md) | ✔ [300 最长递增子序列](dynamic-programming/problems/300-longest-increasing-subsequence.md) · ✔ [1143 最长公共子序列](dynamic-programming/problems/1143-longest-common-subsequence.md) · ✔ [64 最小路径和](dynamic-programming/problems/64-minimum-path-sum.md) · ✔ [72 编辑距离](dynamic-programming/problems/72-edit-distance.md) | 两个维度至少就开二维 `dp[i][j]`：先定「前 i / 前 j 个」的含义，再写转移和边界。300 是这一类里的一维特例，`tails` 可以把复杂度降到 $O(n \log n)$ |

## 教学动画（HTML）

每道题都配了一页可以单步播放的动画（各自页面里也有入口），用来把「指针怎么动、dp 表怎么填」看明白：

| 动画 | 讲什么 | 快捷键 |
|:--|:--|:--|
| [字母异位词分组 · 哈希入桶](DS/hash/problems/49-group-anagrams-demo.html) | 每个词：算签名 → 查表 → 入桶 | 空格播放，`←` `→` 单步 |
| [接雨水 · 双指针](two-pointers/problems/42-trapping-rain-water-demo.html) | 每次结算更矮的一侧，水位由已见最大值决定 | 空格播放，`←` `→` 单步 |
| [三数之和 · 排序后夹逼](two-pointers/problems/15-3sum-demo.html) | 固定 `i`，左右指针按和的大小内收，命中后跳过重复 | 空格播放，`←` `→` 单步 |
| [无重复字符的最长子串](substring/problems/3-longest-substring-without-repeating-characters-demo.html) | 重复时左边界跳到该字符上次出现位置的右边 | 空格播放，`←` `→` 单步 |
| [最小覆盖子串 · 滑动窗口](substring/problems/76-minimum-window-substring-demo.html) | 右扩凑齐 → 左缩记录 → `formed` 计数怎么变 | 空格播放，`←` `→` 单步 |
| [旋转图像 · 转置再翻转](matrix/problems/48-rotate-image-demo.html) | 上三角交换，然后每行左右翻转 | 空格播放，`←` `→` 单步 |
| [K 个一组翻转链表 · 迭代](DS/linked-list/problems/25-reverse-nodes-in-k-group-demo.html) | `dummy` + `groupPrev` 走 k 步找 `kth`，组内指针掉头 | 空格播放，`←` `→` 单步 |
| [LRU · 双向链表](DS/linked-list/problems/146-lru-cache-demo.html) | 命中挪到最新，超容量删掉最久 | 空格播放，`←` `→` 单步 |
| [右视图 · 每层最后一个](DS/tree/problems/199-binary-tree-right-side-view-demo.html) | 层序队列的队尾写入答案 | 空格播放，`←` `→` 单步 |
| [岛屿数量 · 淹岛](DS/graph/problems/200-number-of-islands-demo.html) | 新陆地计数加一，四连通整块改成水 | 空格播放，`←` `→` 单步 |
| [括号生成 · 合法分支](backtrack/problems/22-generate-parentheses-demo.html) | 左括号不超 `n`，右括号不超过左括号 | 空格播放，`←` `→` 单步 |
| [有效的括号 · 栈顶配对](DS/stack/problems/20-valid-parentheses-demo.html) | 左括号入栈，右括号对上才弹出 | 空格播放，`←` `→` 单步 |
| [第 K 大 · 小顶堆](DS/queue/problems/215-kth-largest-element-in-an-array-demo.html) | 堆里只留 k 个，堆顶即第 k 大 | 空格播放，`←` `→` 单步 |
| [跳跃游戏 · 最远可达](greedy/problems/55-jump-game-demo.html) | `reach` 盖住终点即成功，指针走出 `reach` 即失败 | 空格播放，`←` `→` 单步 |
| [买卖股票 IV · dp 表](greedy/problems/188-best-time-to-buy-and-sell-stock-iv-demo.html) | `dp[t][i]` 逐格填，`best` 随卖出日右移更新 argmax | 空格播放，`←` `→` 单步 |
| [单词拆分 · dp 推导](dynamic-programming/problems/139-word-break-demo.html) | 每个 `i` 试所有单词，命中就连出 `parent` 回溯分段 | 空格播放，`←` `→` 单步 |
| [最长递增子序列 · tails](dynamic-programming/problems/300-longest-increasing-subsequence-demo.html) | 二分替换第一个不小于当前值的结尾 | 空格播放，`←` `→` 单步 |
| [最长公共子序列 · dp 表](dynamic-programming/problems/1143-longest-common-subsequence-demo.html) | 相等走左上加一，否则取上或左的较大值 | 空格播放，`←` `→` 单步 |
| [最小路径和 · 逐格取较小来路](dynamic-programming/problems/64-minimum-path-sum-demo.html) | 当前格加上上方、左方的较小路径和 | 空格播放，`←` `→` 单步 |
| [编辑距离 · horse → ros](dynamic-programming/problems/72-edit-distance-demo.html) | 相同抄左上，否则替换 / 删除 / 插入取最小 | 空格播放，`←` `→` 单步 |

## 参考

- 题面与提交：[力扣中国站](https://leetcode.cn/problemset/)
- 本目录：[数据结构](DS/index.md) · [复杂度](complexity.md) · [数论](math/index.md) · [排序](sorting/index.md) · [分治](divide/index.md) · [背包](knapsack/index.md) · [并查集](union-find/index.md)
