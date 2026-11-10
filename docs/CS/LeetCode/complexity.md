# 复杂度

## 定义

存在正常数 \(c\) 和 \(n_0\)，当 \(n \geqslant n_0\) 时：

| 记号 | 含义 |
|:-----|:-----|
| \(T(n) = O(f(n))\) | \(T(n) \leqslant c\, f(n)\)，上界 |
| \(T(n) = \Omega(g(n))\) | \(T(n) \geqslant c\, g(n)\)，下界 |
| \(T(n) = \Theta(h(n))\) | 同时是 \(O\) 和 \(\Omega\) |
| \(T(n) = o(p(n))\) | 比 \(p\) 严格更慢增长的上界 |

\(O(1)\) 表示 \(f(n)\) 有与 \(n\) 无关的上界。分析时同时看最坏情况和平均情况。

## 加减与乘法

若 \(T_1(n) = O(f(n))\)，\(T_2(n) = O(g(n))\)，则

\[
T_1(n) + T_2(n) = O(f(n) + g(n)), \quad T_1(n) \cdot T_2(n) = O(f(n) \cdot g(n))
\]

循环套循环时，把每一层的次数乘起来。例如下面这段是 \(O(n^2)\)：

```python
def pairs(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count
```

## 等价类

把「属于同一集合」看成等价关系。用一棵树表示一个集合：节点只记父亲，`find` 沿父亲走到根，`union` 把一棵树的根挂到另一棵树的根上。合并时按大小或按高度挂，避免退化成一条链。

```python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
```

题目见 [并查集](union-find/index.md)。
