# 放苹果

[P2386](https://www.luogu.com.cn/problem/P2386)。`m` 个相同的苹果放到 `n` 个相同的盘子里，允许空盘，求方案数。

盘子有空的：方案数等于 `f(m, n - 1)`。每个盘子至少放一个：先每个盘子放一个，剩下 `f(m - n, n)`。

```python
def put_apples(m: int, n: int) -> int:
    if m < 0:
        return 0
    if m == 0 or n == 1:
        return 1
    return put_apples(m, n - 1) + put_apples(m - n, n)
```
