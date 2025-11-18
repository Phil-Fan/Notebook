# 数字

## 快速幂

```python
def fast_power(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        return fast_power(a, b // 2, n) ** 2 % n
    else:
        return fast_power(a, b // 2, n) ** 2 * a % n
```

矩阵快速幂
