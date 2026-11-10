# 队列

先进先出（FIFO）。`enqueue` 从队尾进入，`dequeue` 从队头离开。

数组实现要记下 `head` 和 `tail`。为了不把弹出的位置浪费掉，下标按容量取模，这就是循环队列。

```python
class ArrayQueue:
    def __init__(self, capacity: int) -> None:
        self.data = [0] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value: int) -> None:
        if self.size == len(self.data):
            raise IndexError("queue is full")
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % len(self.data)
        self.size += 1

    def dequeue(self) -> int:
        if self.size == 0:
            raise IndexError("queue is empty")
        value = self.data[self.head]
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        return value
```

## 用数组模拟链表

`data[i]` 存值，`next[i]` 存后继下标，`-1` 表示结束。

```text
data = [5.5, 6.7, 7.2, 9.3, -1, 255, 3.1]
next = [  -1,   0,   4,   0,  0,   0,   2]
head = 6

3.1 -> 7.2 -> -1 -> 5.5
```

## 二叉堆

优先队列常用二叉堆：一棵完全二叉树，父节点不大于（小顶堆）或不小于（大顶堆）两个孩子。用数组存时，下标从 0 起：左孩子 `2i+1`，右孩子 `2i+2`，父亲 `(i-1)//2`。

插入：放到最后一个空位，再和父亲比较，该上升就交换，直到堆序恢复。

```text
插入 1 之前          上滤之后
      3                 1
    /   \             /   \
   5     4           5     3
  /               /     /
 8               8     4
```

删除堆顶：用最后一个元素填到根，再向下和较小的孩子交换，直到堆序恢复。

```python
class MinHeap:
    def __init__(self) -> None:
        self.data: list[int] = []

    def push(self, value: int) -> None:
        self.data.append(value)
        i = len(self.data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] <= self.data[i]:
                break
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent

    def pop(self) -> int:
        last = self.data.pop()
        if not self.data:
            return last
        root = self.data[0]
        self.data[0] = last
        i = 0
        n = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            small = i
            if left < n and self.data[left] < self.data[small]:
                small = left
            if right < n and self.data[right] < self.data[small]:
                small = right
            if small == i:
                break
            self.data[i], self.data[small] = self.data[small], self.data[i]
            i = small
        return root
```

[← 返回数据结构](../index.md)
