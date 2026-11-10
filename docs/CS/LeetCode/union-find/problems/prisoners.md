# 关押罪犯

[P1525](https://www.luogu.com.cn/problem/P1525)。每条边是两个罪犯之间的怒气。两个监狱，求一种分配，使「被分在同一监狱、怒气最大的那一对」的怒气尽量小。

按怒气从大到小看。两人还没被强制分到两边，就把他们分进不同监狱：`union(x, y + n)` 且 `union(x + n, y)`。如果他们已经在同一监狱，当前这条怒气就是答案。

```python
class Solution:
    def min_anger(self, n: int, edges: list[tuple[int, int, int]]) -> int:
        parent = list(range(2 * n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            parent[find(a)] = find(b)

        for anger, x, y in sorted(edges, reverse=True):
            if find(x) == find(y):
                return anger
            union(x, y + n)
            union(x + n, y)
        return 0
```

`edges` 的每一项是 `(怒气, 罪犯甲, 罪犯乙)`。
