# 对抗搜索

双方轮流行动，任何一方都不能单独决定整局。形式化需要：初始局面、后继（招法，新局面）、终局判断、终局得分。

## Minimax

零和，且双方都会选对自己最好的招。叶子的分数按我方视角：赢 1、平 0、输 -1，或者任意估值，越大对我方越好。

奇数层是 MAX，取孩子的最大值；偶数层是 MIN，取孩子的最小值。

```text
            MAX 15
         /     |     \
     MIN 3   MIN 15   MIN 1
     / \      / \      / \
    3  12   15  25    1  22
```

左边最差是 3，中间最差是 15，右边最差是 1。对方会把我方的赢面压到该分支的最小值，所以根选中间。右边一旦看到 1，就已经不可能超过中间的 15，后面的 12、20、22 不用再看。

```python
def minimax(node: int, children: list[list[int]], value: list[int], is_max: bool) -> int:
    if not children[node]:
        return value[node]
    scores = [minimax(child, children, value, not is_max) for child in children[node]]
    return max(scores) if is_max else min(scores)
```

有限博弈树上完备且最优。时间 \(O(b^m)\)，空间 \(O(bm)\)。

## Alpha-Beta 剪枝

结果和 Minimax 相同。MAX 维护目前能保证的下界 \(\alpha\)，MIN 维护目前能保证的上界 \(\beta\)。某个节点更新后若 \(\alpha \geqslant \beta\)，这条分支再搜也不会被祖先采纳，直接停。

```python
def alpha_beta(
    node: int,
    children: list[list[int]],
    value: list[int],
    alpha: int,
    beta: int,
    is_max: bool,
) -> int:
    if not children[node]:
        return value[node]
    if is_max:
        for child in children[node]:
            alpha = max(alpha, alpha_beta(child, children, value, alpha, beta, False))
            if alpha >= beta:
                break
        return alpha
    for child in children[node]:
        beta = min(beta, alpha_beta(child, children, value, alpha, beta, True))
        if alpha >= beta:
            break
    return beta
```

剪枝多少取决于孩子的顺序。最好的孩子排在前面时，时间可以从 \(O(b^m)\) 降到大约 \(O(b^{m/2})\)。

流程详见 [OI Wiki · Alpha-Beta](https://oi-wiki.org/search/alpha-beta/)。
