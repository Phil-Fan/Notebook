# 启发式搜索

\(g(n)\) 是从起点到 \(n\) 的已付代价，\(h(n)\) 是从 \(n\) 到目标的估计代价。

## 贪婪最佳优先

只看 \(f(n) = h(n)\)，每次扩展看起来离目标最近的节点。快，但不保证最优。

## A*

\[
f(x) = g(x) + h(x)
\]

每次从优先队列取出 \(f\) 最小的节点，再松弛邻居。\(h(x) \leqslant h^*(x)\)（不高估真实剩余代价）时能找到最优解。再满足三角不等式时，不必把重复节点重新入队。

\(h = 0\) 时 A\* 变成 Dijkstra；边权再都是 1 时变成 BFS。

[八数码 P1379](https://www.luogu.com.cn/problem/P1379)：\(3 \times 3\) 棋盘，0 是空格，目标是

```text
1 2 3
8 0 4
7 6 5
```

\(h\) 可以取「不在目标位置上的棋子个数」。它不高估步数，可以用 A\*。

```python
import heapq


def astar(
    start: str,
    goal: str,
    neighbors,
    heuristic,
) -> int | None:
    heap = [(heuristic(start), 0, start)]
    best = {start: 0}
    while heap:
        _, cost, state = heapq.heappop(heap)
        if cost != best.get(state):
            continue
        if state == goal:
            return cost
        for nxt, step in neighbors(state):
            new_cost = cost + step
            if new_cost < best.get(nxt, 10**18):
                best[nxt] = new_cost
                heapq.heappush(heap, (new_cost + heuristic(nxt), new_cost, nxt))
    return None
```

`heapq` 是 Python 标准库里的堆，不是第三方包。

## 爬山

只和相邻状态比，选更好的那个走。不维护整棵搜索树。

会停在局部最优：改成按概率接受差一点的邻居，好的邻居概率更大。步长太大容易跳过峰顶，可以让步长随「温度」变小。起点不好就多撒几个随机起点，各自爬完再取最好的。

## 模拟退火

新解更好就接受；更差则以概率 \(e^{-\Delta f / T}\) 接受。温度按 \(T \leftarrow \lambda T\) 下降，\(\lambda\) 常取 0.8 到 0.99。温度高时几乎什么都接受，温度低时只接受改进。

目标函数（Six-hump camel）：

\[
f(x, y) = 4x^2 - 2.1x^4 + \frac{x^6}{3} + xy - 4y^2 + 4y^4, \quad |x|,|y| \leqslant 5
\]

最小值约 \(-1.0316\)，出现在 \((0.0898, -0.7126)\) 和它的相反数。

```python
import math
import random


def camel(x: float, y: float) -> float:
    return 4 * x**2 - 2.1 * x**4 + x**6 / 3 + x * y - 4 * y**2 + 4 * y**4


def anneal(steps: int = 20000) -> tuple[float, float, float]:
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    best = (camel(x, y), x, y)
    temperature = 100.0
    for _ in range(steps):
        nx = min(5, max(-5, x + random.uniform(-1, 1) * temperature))
        ny = min(5, max(-5, y + random.uniform(-1, 1) * temperature))
        cur, nxt = camel(x, y), camel(nx, ny)
        if nxt < cur or random.random() < math.exp((cur - nxt) / temperature):
            x, y = nx, ny
            if nxt < best[0]:
                best = (nxt, nx, ny)
        temperature *= 0.995
    return best
```

降温曲线不必画出来：把每一代的 `(temperature, best_value)` 记在列表里即可。`random.random()` 返回 \([0, 1)\)。要均匀取 \([-5, 5]\)，用 `random.uniform(-5, 5)`，不要再用 `random() * 11 - 5` 那种会越界的写法。

## 遗传算法

这一节原来的图讲的是蚁群：蚂蚁在路上留信息素，短路径来回更快，信息素更高，后面的蚂蚁更倾向于走它。遗传算法是另一套：用一组候选解（种群），按适应度挑选，交叉、变异出下一代。两者都是「局部信息加正反馈」，不要把信息素公式直接套进交叉变异。
