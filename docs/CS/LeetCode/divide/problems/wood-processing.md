# 木材加工

[P2440](https://www.luogu.com.cn/problem/P2440)。给定若干根木头的长度，要切出至少 `k` 段等长的小段（不要求用完），求最长的小段长度。切不出时答案是 0。

```python
class Solution:
    def max_length(self, logs: list[int], k: int) -> int:
        def pieces(length: int) -> int:
            if length == 0:
                return 0
            return sum(log // length for log in logs)

        left, right = 0, max(logs)
        while left < right:
            mid = (left + right + 1) // 2
            if pieces(mid) >= k:
                left = mid
            else:
                right = mid - 1
        return left
```
