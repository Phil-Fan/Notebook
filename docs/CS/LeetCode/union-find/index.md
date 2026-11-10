# 并查集

用 `parent[i]` 表示 `i` 的父亲。一个集合是一棵树，根的父亲是自己。

路径压缩：查找时把沿途节点直接挂到根上。按大小合并：把小树挂到大树下面。两者一起用时，单次操作近似常数。

```python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)
```

下标如果从 1 开始，把数组长度开成 `n + 1`，第 0 位空着。

## 题库

| 题目 | 要点 |
|:-----|:-----|
| [亲戚](problems/relatives.md) | 合并亲属，再回答是否同一家族 |
| [并查集模板](problems/template.md) | 合并与查询两种操作 |
| [食物链](problems/food-chain.md) | 每个动物拆成同类、猎物、天敌三个点 |
| [关押罪犯](problems/prisoners.md) | 按怒气从大到小，把两人分到两个监狱 |
| [银河英雄传说](problems/galaxy.md) | 边上再记「到根有几艘船」 |
