# 无权搜索

|  | BFS | DFS | 深度受限 | 迭代加深 |
|:--|:----|:----|:---------|:---------|
| 做法 | 先扩展最浅的节点，队列 | 一条路走到底再回溯，栈 | DFS，深度超过 \(l\) 就停 | 深度上限从 0 往上加 |
| 完备 | 是 | 无限深时不是 | \(l \geqslant d\) 时是 | 是 |
| 最优 | 边权都是 1 时是 | 否 | 否 | 边权都是 1 时是 |
| 时间 | \(O(b^{d+1})\) | \(O(b^m)\) | \(O(b^l)\) | \(O(b^d)\) |
| 空间 | \(O(b^{d+1})\) | \(O(bm)\) | \(O(bl)\) | \(O(bd)\) |

\(b\) 是分支因子，\(d\) 是解的深度，\(m\) 是状态空间的最大深度。

一个良定义的问题要有：初始状态、可行动作、转移、目标测试、路径代价。解是从初始状态到目标状态的一条路径。

搜索过程里用 OPEN 表放待扩展节点，CLOSED 表放已经扩展过的节点。图搜索比树搜索多一个「见过就不再进队」的集合。

## BFS

队列保证先扩展浅层。可以回答「有没有路」和「边权为 1 时的最短路」。

```python
def bfs(graph: dict[int, list[int]], start: int, goal: int) -> list[int] | None:
    queue = [start]
    parent = {start: None}
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for nxt in graph.get(node, []):
            if nxt not in parent:
                parent[nxt] = node
                queue.append(nxt)
    return None
```

一致代价搜索把队列换成按 \(g(n)\) 排序的优先队列。每步代价都至少是某个正数时，它是完备且最优的。边权都是 1 时它就是 BFS；一般边权时它就是 Dijkstra。

## DFS

栈，或者递归用的系统栈。空间是当前路径那么长，找到的不一定最短。无限深的图上可能不终止。

```python
def dfs(graph: dict[int, list[int]], start: int, goal: int) -> bool:
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        if node == goal:
            return True
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return False
```

深度受限：递归时多传一个剩余深度，到 0 就返回。上限小于解的深度就会漏解。

迭代加深：深度上限从 0、1、2… 增加，每一轮做一次深度受限搜索。空间仍是 \(O(bd)\)，边权为 1 时能找到最短解。

## 全排列

这是 DFS 的典型题：当前位置试每一个还没用过的数，递归到下一层，回来时撤销选择。

```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        used = [False] * len(nums)
        path: list[int] = []

        def dfs() -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i, value in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(value)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return result
```

## 双向搜索

从起点和终点各做一次 BFS，在中间相遇。相当于把半径 \(d\) 的圆换成两个半径 \(d/2\) 的圆，节点数从 \(O(b^d)\) 降到 \(O(b^{d/2})\)。
