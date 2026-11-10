# 数组与链表

## 数组

按下标访问是 \(O(1)\)。在中间插入或删除要搬后面的元素，是 \(O(n)\)。

## 单链表

每个节点保存值和 `next`。最后一个节点的 `next` 是 `None`。已知前驱时，插入和删除是 \(O(1)\)；按下标查找是 \(O(n)\)。

在 `current` 后面插入 `val`：

```text
current -> next
        \-> [val] -/
```

```python
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def insert_after(current: ListNode, val: int) -> None:
    node = ListNode(val, current.next)
    current.next = node


def remove_after(current: ListNode) -> None:
    nxt = current.next
    if nxt is None:
        return
    current.next = nxt.next
```

## 双链表

单链表删除某个节点时，如果手里只有这个节点，就拿不到它的前驱。双向链表每个节点再记一个 `prev`，插入和删除都可以从当前节点出发。

插入 `node` 到 `prev` 和 `nxt` 之间：

```text
prev <-> node <-> nxt
```

```python
class DNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.prev: DNode | None = None
        self.next: DNode | None = None


def insert_between(prev: DNode, nxt: DNode, val: int) -> DNode:
    node = DNode(val)
    node.prev, node.next = prev, nxt
    prev.next = node
    nxt.prev = node
    return node


def remove_node(node: DNode) -> None:
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
```

题库：[25. K 个一组翻转链表](problems/25-reverse-nodes-in-k-group.md)。
