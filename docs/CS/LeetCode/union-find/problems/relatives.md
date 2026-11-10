# 亲戚

[P1551](https://www.luogu.com.cn/problem/P1551)。`n` 个人，`m` 对亲戚关系，再回答 `q` 次「这两人是不是亲戚」。亲戚的亲戚也是亲戚。

```python
class Solution:
    def relatives(self, n: int, edges: list[tuple[int, int]], queries: list[tuple[int, int]]) -> list[bool]:
        parent = list(range(n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            parent[find(a)] = find(b)
        return [find(a) == find(b) for a, b in queries]
```
