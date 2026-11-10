# 146. LRU 缓存

!!! abstract "题单坐标"
    **Hot 20 · 第 6 类「链表」** ｜ 难度：中等 ｜ 标签：`设计` `哈希表` `链表`

    一句话套路：哈希表负责 $O(1)$ 按 key 找到节点，双向链表负责 $O(1)$ 把节点挪到「最新」或从尾部删掉「最久」。

## 题干

> [力扣 146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)

请你设计并实现一个满足 LRU (最近最少使用) 缓存约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以正整数作为容量 `capacity` 初始化 LRU 缓存。
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1`。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value`；如果不存在，则向缓存中插入该组 `key-value`。如果插入操作导致关键字数量超过 `capacity`，则应该逐出最久未使用的关键字。

函数 `get` 和 `put` 必须以 $O(1)$ 的平均时间复杂度运行。

**示例**

```text
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

**提示**

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- 最多调用 `2 * 10^5` 次 `get` 和 `put`

## 思路

「最近最少使用」要的是两件事同时 $O(1)$：按 key 找到条目，以及按使用时间插入、删除。

| 结构 | 找 key | 删最旧 / 挪到最新 | 单独够不够 |
|:-----|:-------|:------------------|:-----------|
| 数组 / 单链表 | $O(n)$ | 删已知节点 $O(n)$（要找前驱） | 不够 |
| 哈希表 | $O(1)$ | 不知道谁最旧 | 不够 |
| 双向链表 | $O(n)$ | 已知节点时 $O(1)$ | 不够 |
| 哈希表 + 双向链表 | $O(1)$ | $O(1)$ | 够 |

约定链表**头部是最新、尾部是最久**。再加两个哨兵 `head`、`tail`，这样「插到最新」和「删掉最久」都不用判断空表：

- `get` 命中：把节点从原位置摘下，插到 `head` 后面，返回值。
- `put` 已存在：改值，同样挪到头部。
- `put` 不存在：新建节点插到头部；若 `len(map) > capacity`，删掉 `tail.prev`，并在哈希表里删掉它的 key。

摘节点之前，节点的 `prev` 和 `next` 都还在，所以双向链表才能 $O(1)$ 把前后接上。单链表做不到这一点。

**走一遍容量为 2 的示例。** 括号里从左到右是「最新 → 最久」。

| 操作 | 链表 | 返回 |
|:-----|:-----|:-----|
| `put(1,1)` | 1 | — |
| `put(2,2)` | 2 → 1 | — |
| `get(1)` | 1 → 2 | 1 |
| `put(3,3)` | 3 → 1，2 被逐出 | — |
| `get(2)` | 3 → 1 | -1 |
| `put(4,4)` | 4 → 3，1 被逐出 | — |
| `get(1)` | 4 → 3 | -1 |
| `get(3)` | 3 → 4 | 3 |
| `get(4)` | 4 → 3 | 4 |

## 代码（带注释）

> 这题的类名是 `LRUCache`，不是 `Solution`。`OrderedDict` 能交过，但面试要自己把双向链表写出来。

```python
class Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.nodes: dict[int, Node] = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _detach(self, node: Node) -> None:
        assert node.prev is not None and node.next is not None
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_newest(self, node: Node) -> None:
        assert self.head.next is not None
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._detach(node)
        self._insert_newest(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.nodes.get(key)
        if node is not None:
            node.value = value
            self._detach(node)
            self._insert_newest(node)
            return
        node = Node(key, value)
        self.nodes[key] = node
        self._insert_newest(node)
        if len(self.nodes) > self.capacity:
            oldest = self.tail.prev
            assert oldest is not None and oldest is not self.head
            self._detach(oldest)
            del self.nodes[oldest.key]
```

`get` 未命中不能把 key 插进去。容量判断用 `>` 而不是 `>=`：插入之后再看，刚好等于容量时什么都不用删。

## 复杂度

| 操作 | 时间 | 空间 |
|:-----|:-----|:-----|
| `get` | $O(1)$ | — |
| `put` | $O(1)$ | — |
| 整体 | — | $O(\text{capacity})$ |

调用次数到 $2 \times 10^5$，任何一次线性扫描都会超时。哈希表和链表节点数都不超过 `capacity`。

## 教学动画（HTML）

<iframe src="146-lru-cache-demo.html" title="LRU · 哈希表加双向链表" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

按示例的 9 次调用往下走。链表从左到右是「最新 → 最久」，被 `get` 命中的节点会挪到最左，超容量时最右边的节点消失。空格播放 / 暂停，`←` `→` 单步，`R` 重置。

## 易错点

- **只在 `put` 新 key 时更新顺序**：`get` 和「更新已有 key」也是一次使用，不挪到头部的话，下一轮会把刚刚用过的条目当最久未使用删掉。示例里 `get(1)` 之后再 `put(3,3)`，该删的是 2 不是 1。
- **用单链表**：知道节点也找不到前驱，删除是 $O(n)$。
- **哨兵没接上**：`head.next = tail`、`tail.prev = head` 漏一个，第一次插入就会在空指针上停住。
- **先删再判断容量**：`capacity = 1` 时如果在插入前就把尾节点删了，缓存会空一拍，新节点还没放进去。
- **`get` 未命中时执行 `put`**：题目要求返回 `-1`，不能把缺的 key 写成 0 塞进去。

## 延伸

- [← 返回 Hot 20 题单](../../index.md) · [本类总览：链表](../index.md)
- 同类题：[460. LFU 缓存](https://leetcode.cn/problems/lfu-cache/)（再按频次分层）· [706. 设计哈希映射](https://leetcode.cn/problems/design-hashmap/)
