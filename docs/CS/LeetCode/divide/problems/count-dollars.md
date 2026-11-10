# 零钱方案数

用面额 1、5、10、20、50、100，求凑出 `total` 的方案数。顺序不计，所以每一步要么继续用当前最大面额，要么改用更小的面额。

```python
def next_smaller(bill: int) -> int | None:
    order = {100: 50, 50: 20, 20: 10, 10: 5, 5: 1}
    return order.get(bill)


def count_with_top(total: int, top: int | None) -> int:
    if total == 0:
        return 1
    if total < 0 or top is None:
        return 0
    return count_with_top(total - top, top) + count_with_top(total, next_smaller(top))


def count_dollars(total: int) -> int:
    return count_with_top(total, 100)
```

`count_dollars(15)` 是 6，`count_dollars(10)` 是 4。
