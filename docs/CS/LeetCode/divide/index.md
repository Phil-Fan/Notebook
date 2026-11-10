# divide and conquer

- 分治法
- 分治法的核心思想是将一个问题分解为若干个子问题，然后递归地解决这些子问题，最后将这些子问题的解合并起来得到原问题的解。
- 分治法的核心思想是将一个问题分解为若干个子问题，然后递归地解决这些子问题，最后将这些子问题的解合并起来得到原问题的解。

## 二分

在有序范围上，每次丢掉一半。两种写法不要混用，否则 `left` 和 `right` 会停在同一点上死循环。

最小值最大（找左边界，`check(mid)` 为真时答案在左边，含 `mid`）：

```python
def lower_bound(left: int, right: int, ok) -> int:
    while left < right:
        mid = (left + right) // 2
        if ok(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

最大值最小的对偶是「答案越大越容易满足」时把中点向上取整，满足则 `left = mid`，否则 `right = mid - 1`。结束条件都是 `left == right`。

- 判断 mid 的算法==要不要加 1==!!  判断错误就会出现死循环；
（~~建议此步骤在草图画两个小圈圈代表最后两个数，把表达式带进去验证，就可以知道是要不要加 1 了~~ ）
- 二分终止条件是`l == r；`  也是答案所在的位置

- [数列分段](problems/section-ii.md)
- [砍树](problems/cut-trees.md)
- [木材加工](problems/wood-processing.md)

## 汉诺塔

把 `n` 个盘子从 `src` 挪到 `dst`，借助 `aux`：先把上面 `n-1` 个挪到辅助柱，再挪最大的，最后把 `n-1` 个从辅助柱挪到目标柱。

```python
def hanoi(n: int, src: str, dst: str, aux: str, moves: list[tuple[str, str]]) -> None:
    if n == 0:
        return
    hanoi(n - 1, src, aux, dst, moves)
    moves.append((src, dst))
    hanoi(n - 1, aux, dst, src, moves)
```

## 整数划分

`count_partitions(n, m)`：把正整数 `n` 拆成若干个不超过 `m` 的正整数之和，顺序不计。最后一项用了 `m`，剩下 `count_partitions(n - m, m)`；最后一项不超过 `m - 1`，则是 `count_partitions(n, m - 1)`。

```python
def count_partitions(n: int, m: int) -> int:
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    return count_partitions(n - m, m) + count_partitions(n, m - 1)
```

`count_partitions(6, 4)` 是 9。零钱问题是同一递归，只是面额不是连续整数，见 [零钱兑换的方案数](problems/count-dollars.md)。苹果问题见 [放苹果](problems/put-apples.md)。
