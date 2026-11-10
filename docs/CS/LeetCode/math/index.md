# 数论

参考：[OI Wiki · 数论基础](https://oi-wiki.org/math/number-theory/basic/)。下面的函数都可以直接交到力扣风格的题里，不依赖第三方库。

## 快速幂

把指数写成二进制。\(3^{10} = 3^{1010_2} = 3^{8} \cdot 3^{2}\)。指数每次右移一位，底数平方；当前位是 1 就把底数乘进答案。

```python
def pow_mod(a: int, b: int, mod: int) -> int:
    ans = 1
    a %= mod
    while b:
        if b & 1:
            ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans
```

64 位整数乘法 \(a \cdot b \bmod m\) 同样按二进制拆，只是「平方」换成「乘 2」。Python 的整数没有溢出，日常直接写 `a * b % mod` 即可。

```python
def mul_mod(a: int, b: int, mod: int) -> int:
    ans = 0
    a %= mod
    while b:
        if b & 1:
            ans = (ans + a) % mod
        a = (a * 2) % mod
        b >>= 1
    return ans
```

## 整除与最大公约数

\[
\gcd(a, b) = \gcd(b, a \bmod b)
\]

若 \(a = kb + r\)，则 \(a\) 与 \(b\) 的公约数和 \(b\) 与 \(r\) 的公约数相同。

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)
```

\(\gcd(a, b) = 1\) 时称 \(a\) 与 \(b\) 互质。大于 3 的素数都是 \(6n \pm 1\)。

## 素数筛

朴素判断从 2 试到 \(\sqrt{x}\)。

```python
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
```

埃氏筛把每个素数的倍数划掉，合数可能被划多次，时间 \(O(n \log \log n)\)。欧拉筛让每个合数只被它的最小质因子划一次，时间 \(O(n)\)。`i % p == 0` 时 `p` 已经是 `i` 的最小质因子，再乘更大的素数会重复，所以停下来。

```python
def euler_sieve(n: int) -> list[int]:
    is_composite = [False] * (n + 1)
    primes: list[int] = []
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_composite[i * p] = True
            if i % p == 0:
                break
    return primes
```

[P3383 线性筛素数](https://www.luogu.com.cn/problem/P3383) 就是先筛，再回答「第 \(k\) 个素数」或「\(x\) 是不是素数」。`0` 和 `1` 不是素数。

## 同余与逆元

\(a \equiv b \pmod n\) 表示 \(a\) 和 \(b\) 除以 \(n\) 的余数相同。

若存在 \(b\) 使 \(ab \equiv 1 \pmod n\)，则 \(b\) 是 \(a\) 模 \(n\) 的逆元。逆元存在的充要条件是 \(\gcd(a, n) = 1\)。

费马小定理：\(p\) 是素数且 \(p \nmid a\) 时，\(a^{p-1} \equiv 1 \pmod p\)，所以逆元是 \(a^{p-2} \bmod p\)，用快速幂即可。模数不是素数时要用扩展欧几里得。

## 裴蜀定理与扩展欧几里得

存在整数 \(x, y\) 使 \(ax + by = \gcd(a, b)\)。

```python
def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """返回 (g, x, y)，满足 ax + by = g = gcd(a, b)。"""
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def mod_inverse(a: int, mod: int) -> int | None:
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        return None
    return x % mod
```

`extended_gcd(56, 15)` 给出一组满足 \(56x + 15y = 1\) 的系数。

## 中国剩余定理

模数两两互质时，同余方程组 \(x \equiv a_i \pmod {m_i}\) 在模 \(M = \prod m_i\) 下有唯一解。令 \(M_i = M / m_i\)，\(t_i\) 为 \(M_i\) 模 \(m_i\) 的逆元，则 \(x = \sum a_i M_i t_i\)。

```python
def crt(remainders: list[int], mods: list[int]) -> int | None:
    prod = 1
    for mod in mods:
        prod *= mod
    x = 0
    for a, mod in zip(remainders, mods):
        mi = prod // mod
        inv = mod_inverse(mi, mod)
        if inv is None:
            return None
        x += a * mi * inv
    return x % prod
```

## 欧拉函数与欧拉定理

\(\varphi(n)\) 是 \(1 \ldots n\) 里与 \(n\) 互质的个数。\(n = \prod p_i^{k_i}\) 时

\[
\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right)
\]

```python
def euler_phi(n: int) -> int:
    result = n
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result = result // p * (p - 1)
        p += 1
    if x > 1:
        result = result // x * (x - 1)
    return result
```

欧拉定理：\(\gcd(a, n) = 1\) 时 \(a^{\varphi(n)} \equiv 1 \pmod n\)。费马小定理是 \(n\) 为素数、\(\varphi(n) = n - 1\) 的特例。
