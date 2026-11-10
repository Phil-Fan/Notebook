# 并查集模板

[P3367](https://www.luogu.com.cn/problem/P3367)。两种操作：`1 a b` 把 `a` 和 `b` 所在集合合并；`2 a b` 询问是否在同一集合。

```python
class Solution:
    def process(self, n: int, ops: list[tuple[int, int, int]]) -> list[str]:
        parent = list(range(n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        answer: list[str] = []
        for kind, a, b in ops:
            if kind == 1:
                parent[find(a)] = find(b)
            elif find(a) == find(b):
                answer.append("Y")
            else:
                answer.append("N")
        return answer
```
