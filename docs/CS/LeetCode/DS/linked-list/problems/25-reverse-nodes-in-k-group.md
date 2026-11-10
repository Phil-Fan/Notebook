# 25. K 个一组翻转链表

!!! abstract "题单坐标"
    **Hot 20 · 第 6 类「链表」** ｜ 难度：困难 ｜ 标签：`链表` `指针` `递归`

    一句话套路：套一层哨兵 `dummy`，每轮从「上一组尾巴」先走 `k` 步探路，够长才把整段原地掉头。

## 题干

> [力扣 25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

给你链表的头节点 `head`，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1**

```text
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2**

```text
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

**提示**

- 链表中的节点数目为 `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

**进阶**：你可以设计一个只用 $O(1)$ 额外内存空间的算法解决此问题吗？

## 思路

**不变量**：`group_prev` 永远指向「已翻转部分的最后一个节点」。在它左边，链表已经是最终形态；在它右边，还是本轮待处理的原始链段。这个不变量让第一组和后面所有组共用同一套逻辑——哨兵 `dummy` 就充当「第 0 组」的尾巴。

每轮四步：

1. **探路**：从 `group_prev` 往后走 `k` 步，第 `k` 个节点记为 `kth`。中途走到 `None`，说明剩余不足一组，直接返回 `dummy.next`，尾巴保持原序、一个指针都不动。这一步必须在翻转**之前**做——先掉头再发现不够长，就得再翻回去。
2. **记下一组起点**：`next_group = kth.next`。
3. **原地掉头（in-place）**：把 `[组头, kth]` 这一段逐个把 `next` 指向自己的前驱。技巧是把 `prev` 初始化成 `next_group`，这样组尾处理完时自然指向下一组，省掉一次单独的接尾操作。
4. **接回**：`group_prev.next = kth`（新组头接上前半段），旧的组头翻转后变成组尾，把它赋给 `group_prev`，进入下一轮。

**为什么是 $O(1)$ 空间**：全程只用 `dummy`、`group_prev`、`kth`、`next_group`、`prev`、`cur`、`nxt` 这几个指针变量，没有数组也没有递归栈。时间上每个节点恰好被「探路」和「掉头」各扫常数次，总计 $O(n)$。

**另外两种写法一句话对比**：

- **栈**：把 `k` 个节点压栈，弹栈的顺序天然逆序，最好理解；代价是 $O(k)$ 额外空间，并且每组要重新接一遍 `next`。
- **递归**：先确认够 `k` 个，翻转前 `k` 个后递归处理 `cur`，再把 `head.next` 接上递归结果。代码最短，但递归深度约 $n/k$，`k` 小时会撞到 Python 默认的递归上限（约 1000）。

## 代码（带注释）

> 按力扣提交格式写。`ListNode` 由判题器提供，这里留一份定义，方便本地看。

=== "主推：迭代 + dummy（O(1) 空间）"

    ```python
    from typing import Optional


    class ListNode:
        """单链表节点（LeetCode 的节点定义）。"""

        def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
            # 节点只有「值」和「指向下一个节点」两个字段
            self.val, self.next = val, next


    def build_list(values: list[int]) -> Optional[ListNode]:
        # 按数组顺序建出整条链表，返回真正的头节点
        dummy = ListNode()          # 哨兵：省掉「第一个节点」的特殊判断
        tail = dummy                # tail 恒指向当前链表的最后一个节点
        for v in values:
            tail.next = ListNode(v) # 把新节点挂到链尾
            tail = tail.next        # tail 前移，继续指向新的链尾
        return dummy.next           # 哨兵之后才是真正的头节点


    def to_values(head: Optional[ListNode]) -> list[int]:
        # 把链表转回数组，方便打印和断言
        out, node = [], head        # node 是遍历指针，从表头开始
        while node is not None:     # 走到 None 说明链表结束
            out.append(node.val)    # 收集当前节点的值
            node = node.next        # 指针后移一格
        return out


    class Solution:
        def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if head is None or k <= 1:
                return head
            dummy = ListNode(0, head)
            group_prev = dummy
            while True:
                kth = group_prev
                for _ in range(k):
                    kth = kth.next
                    if kth is None:
                        return dummy.next
                next_group = kth.next
                prev, cur = next_group, group_prev.next
                while cur is not next_group:
                    nxt = cur.next
                    cur.next = prev
                    prev, cur = cur, nxt
                old_head = group_prev.next
                group_prev.next = kth
                group_prev = old_head
    ```

=== "栈（O(k) 额外空间，最好懂）"

    ```python
    def reverse_k_group_stack(head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """复用上面的 ListNode / build_list / to_values。"""
        if head is None or k <= 1:      # 空链表 / k 无效：原样返回
            return head

        dummy = ListNode()
        tail = dummy                # 已处理部分的最后一个节点
        stack: list[ListNode] = []  # 每组临时借用的栈，弹出顺序天然是逆序
        cur = head                  # 遍历指针，从表头开始
        while cur is not None:      # 沿原链表逐节点前进
            stack.append(cur)       # 当前节点先压栈
            nxt = cur.next          # 先存后继：出栈时 next 会被改写
            if len(stack) == k:     # 满 k 个：弹栈顺序就是逆序
                while stack:        # 把这 k 个节点按逆序接进结果链表
                    node = stack.pop()
                    tail.next = node
                    tail = node
            cur = nxt               # 处理下一个节点
        for node in stack:          # 不足 k 个的尾巴保持原序
            tail.next = node
            tail = node
        tail.next = None            # 收尾，防止连回旧链表成环
        return dummy.next           # 跳过哨兵，返回真正的头节点
    ```

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 迭代 + dummy | $O(n)$ | $O(1)$ | 默认，面试首选 |
| 显式栈 | $O(n)$ | $O(k)$ | 想一次写对、不介意额外空间 |
| 递归 | $O(n)$ | $O(n/k)$ 递归栈 | 链表熟练时可写；`k` 小要防递归上限 |

$n$ 是链表节点数。三种写法都要把每个节点扫常数次，时间没有优化空间；差别只在额外空间的常数和出错风险上。

## 教学动画（HTML）

<iframe src="25-reverse-nodes-in-k-group-demo.html" title="K 个一组翻转" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

动画用 `[1..7]、k = 3` 跑迭代法：`D` 是 dummy，蓝色 `groupPrev` 站在上一组尾巴上，先走 3 步锁定 `kth`、亮一下 `nextGroup`，再逐个掉头（组内出现弯向下的弧线），最后把新组头接回 `groupPrev`。注意看最后只剩 `[7]` 的那一步——探路失败，链表就此停下。弱化色是未处理的 `next`，主色是正在翻转的组，强调色是已完成的组，浅色是凑不满的尾巴。空格播放/暂停，`←` `→` 单步，`R` 复位。

## 易错点

- **先翻转、后判断够不够长**：不足 `k` 个时已经把一段改乱了，还得再翻回来；更糟的情况是忘了还原。正确顺序是先用 `kth` 探路、走不到就 `return dummy.next`。
- **组尾没接回、或接成环**：掉头时若把 `prev` 初始化成 `None`，组尾就断了；初始化成 `next_group` 才能顺势接上。调试时打印成数组，如果死循环就是指针成环了。
- **返回了 `head` 而不是 `dummy.next`**：第一组翻转后头节点已经变了，返回旧 `head` 会丢掉前半段。
- **漏了 `k <= 1` 的提前返回**：`k = 1` 只是白转一圈；`k = 0` 会死循环（走 0 步后 `kth == group_prev`，组内永远翻不完）。开头判掉 `head is None or k <= 1`。
- **只交换值不改指针**：题目要求原地改 `next`；把值拷进数组反转再写回去，遇到共享节点就会改错别处，面试也直接判不合格。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：链表](../index.md)
- 同类题：[206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/) · [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/) · [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/)
