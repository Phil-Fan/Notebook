# 链表 | Linked List

!!! abstract "Hot 20 · 第 6 类"
    **什么时候想到它**：题目给 `ListNode`，要求改指针、翻转区间、删除节点、合并/拆分、找环。
    **核心动作**：`dummy` 哨兵 + 三指针 `prev / cur / nxt`，**永远先存 `next` 再断链**。

## 套路

1. 头节点可能被换掉 → 一律先加 `dummy.next = head`，最后返回 `dummy.next`。
2. 断链前先 `nxt = cur.next`，否则后面的节点就找不回来了。
3. 区间操作（翻转、删除、合并）用「组前驱」指针站在区间左侧，第一组和后面所有组的逻辑就能统一。
4. 需要「O(1) 随机访问 + O(1) 增删」→ 哈希表 + 双向链表（LRU）。

## 题目

| 题目 | 难度 | 状态 | 一句话 |
|:-----|:-----|:-----|:-------|
| [25 K 个一组翻转链表](problems/25-reverse-nodes-in-k-group.md) | 困难 | ✔ 已整理 | dummy + 走 k 步探路 + 组内掉头 |
| [146 LRU 缓存](https://leetcode.cn/problems/lru-cache/) | 中等 | ☐ 待补 | 哈希表 + 双向链表 |
| [206 反转链表](https://leetcode.cn/problems/reverse-linked-list/) | 简单 | 相关 | 三指针掉头的基础动作 |
| [92 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/) | 中等 | 相关 | 区间翻转 + 组前驱 |
| [24 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) | 中等 | 相关 | 25 的 k = 2 特例 |

## 易错点

- **先翻转再判断够不够长**：不足 k 个时已经把一段改乱，还得翻回来；必须先探路。
- 忘记收尾（`tail.next = None`），链表会连回旧节点成环，表现为死循环。
- 返回 `head` 而不是 `dummy.next`：第一组翻完头节点已经变了。
- 只交换节点里的值不改指针——这题就白做了，共享节点还会改错别处。

## 相关

- [← 返回 Hot 20 题单](../../index.md)
- 链表怎么存：[数组与链表](list.md)
