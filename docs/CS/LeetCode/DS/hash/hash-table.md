# 散列表

`address = hash(key)`。查找、插入、删除的平均时间可以看成常数。冲突是两个不同的键被映射到同一个槽。

## 分离链

同一个槽上的键放进一条链表（或一个列表）。装填因子 \(\alpha = n / m\) 是元素个数除以槽数，也约等于链的平均长度。\(\alpha\) 变大，冲突变多。很多实现在 \(\alpha\) 超过 0.75 时把表扩大一倍再重新散列。

```text
槽 0: 10 -> 20
槽 1: 11
槽 2: (空)
槽 3: 3 -> 13
```

```python
class SeparateChain:
    def __init__(self, buckets: int = 8) -> None:
        self.buckets = buckets
        self.table: list[list[tuple[int, str]]] = [[] for _ in range(buckets)]
        self.count = 0

    def _index(self, key: int) -> int:
        return key % self.buckets

    def put(self, key: int, value: str) -> None:
        chain = self.table[self._index(key)]
        for i, (k, _) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))
        self.count += 1

    def get(self, key: int) -> str | None:
        for k, value in self.table[self._index(key)]:
            if k == key:
                return value
        return None
```

## 开放定址

冲突后按规则找下一个空槽。

- **线性探测**：依次看 `h, h+1, h+2, ...`。容易连成一段（一次聚集）。装填因子最好小于 0.5。
- **平方探测**：看 `h+1², h+2², ...`，减轻一次聚集。
- **双散列**：步长用第二个哈希。`hash2(x) = z - (x % z)`，`z` 是比表长小的质数。第 \(i\) 次探测位置是 `(hash1 + i * hash2) % m`。

删除不能直接留空，否则探测链会断。常见做法是做删除标记，或者干脆不删。

```python
def linear_probe_put(table: list[int | None], key: int) -> None:
    i = key % len(table)
    for step in range(len(table)):
        slot = (i + step) % len(table)
        if table[slot] is None or table[slot] == key:
            table[slot] = key
            return
    raise RuntimeError("table is full")
```

## 乘同余

把键乘一个常数再取高位，比单纯取模更均匀。对机器字长 \(w\)、表长 \(m = 2^p\)：

\[
h(k) = \left\lfloor m \cdot (k A \bmod 1) \right\rfloor
\]

Knuth 建议 \(A \approx (\sqrt{5}-1)/2\)。

```python
def mul_hash(key: int, bits: int = 10) -> int:
    a = 0.6180339887
    frac = (key * a) % 1
    return int(frac * (1 << bits))
```

## 全域散列

固定的哈希函数可以被针对：把恰好落到同一槽的键挑出来当输入，冲突率就是 100%。从一组函数里随机挑一个，并且任意两个不同键在这组函数里碰撞的比例不超过 \(1/m\)，精心构造的输入期望冲突率仍是 \(1/m\)。

## 用途

- 校验与摘要：MD5、SHA 把一大段数据收成短指纹。碰撞在密码学里要单独讨论，散列表只借用「看起来均匀」这一面。
- 去重、分组、计数：键相同就认为是同一类。题库里的写法见 [哈希题型](index.md)。
