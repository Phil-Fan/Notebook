# 食物链

[P2024](https://www.luogu.com.cn/problem/P2024)。动物 `x` 的同类、猎物、天敌分别放在 `x`、`x + n`、`x + 2n`。

说「`x` 与 `y` 同类」时，若 `x` 的猎物或天敌已经和 `y` 同类，这句话是假话；否则把三组对应关系各自合并。说「`y` 是 `x` 的猎物」时，对称地检查并合并 `x+n` 与 `y`、`x+2n` 与 `y+n`、`x` 与 `y+2n`。编号超出 `1..n` 的话也算假话。

```python
class Solution:
    def food_chain(self, n: int, statements: list[tuple[int, int, int]]) -> int:
        parent = list(range(3 * n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            parent[find(a)] = find(b)

        lies = 0
        for kind, x, y in statements:
            if x > n or y > n:
                lies += 1
                continue
            if kind == 1:
                if find(x + n) == find(y) or find(x + 2 * n) == find(y):
                    lies += 1
                else:
                    union(x, y)
                    union(x + n, y + n)
                    union(x + 2 * n, y + 2 * n)
            else:
                if find(x) == find(y) or find(x + 2 * n) == find(y):
                    lies += 1
                else:
                    union(x + n, y)
                    union(x + 2 * n, y + n)
                    union(x, y + 2 * n)
        return lies
```
