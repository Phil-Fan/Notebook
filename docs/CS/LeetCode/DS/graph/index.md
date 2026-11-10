# 图

图是一组顶点和连接它们的边。无向图里一条边没有方向；有向图里边从一端指向另一端。

\(n\) 个顶点的树恰好有 \(n-1\) 条边，并且连通、无环。多一条边就出现环，少一条边就不连通。

邻接表用「顶点 → 邻居列表」表示，适合稀疏图：

```python
def add_undirected(graph: dict[int, list[int]], u: int, v: int) -> None:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
```

遍历见 [无权搜索](../../search/uninformed.md)。岛屿数量这类网格题，把每个格子当成顶点，四连通的边连起来，每发现一块没走过的陆地就做一次搜索。

## 题目

| 题目 | 难度 | 状态 | 一句话 |
|:-----|:-----|:-----|:-------|
| [200 岛屿数量](problems/200-number-of-islands.md) | 中等 | ✔ 已整理 | 碰到 `'1'` 就计数，并 DFS/BFS 淹掉整块 |

[← 返回数据结构](../index.md)
