# 银河英雄传说

[P1196](https://www.luogu.com.cn/problem/P1196)。每艘战舰一个节点。合并时把一列接到另一列后面，并记下这艘船前面有多少艘。查询时如果两船不在同一列，答案是 `-1`；否则两船到根的距离之差再减 1，就是它们之间的船数。

```python
class Solution:
    def galaxy(self, ops: list[tuple[str, int, int]]) -> list[int]:
        parent = list(range(30001))
        front = [0] * 30001
        size = [1] * 30001

        def find(x: int) -> int:
            if parent[x] != x:
                root = find(parent[x])
                front[x] += front[parent[x]]
                parent[x] = root
            return parent[x]

        answer: list[int] = []
        for kind, x, y in ops:
            rx, ry = find(x), find(y)
            if kind == "M" and rx != ry:
                parent[rx] = ry
                front[rx] = size[ry]
                size[ry] += size[rx]
            elif kind == "C":
                if rx != ry:
                    answer.append(-1)
                else:
                    answer.append(abs(front[x] - front[y]) - 1)
        return answer
```

`find` 返回之后，`front[x]` 才是压缩过的「前面有几艘」。比较距离前要对两艘船都调用一次 `find`。
