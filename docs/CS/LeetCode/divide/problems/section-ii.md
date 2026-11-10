# 数列分段

[P1182](https://www.luogu.com.cn/problem/P1182)。把长度为 `n` 的正整数数列切成不超过 `m` 段，使「段和的最大值」最小。

段和的上界越小，需要的段数越多。对这个上界做二分：`need(limit) > m` 说明上限太小，往右找。

```python
class Solution:
    def split_array(self, nums: list[int], m: int) -> int:
        def need(limit: int) -> int:
            parts = 1
            total = 0
            for value in nums:
                if total + value > limit:
                    parts += 1
                    total = value
                else:
                    total += value
            return parts

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if need(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left
```

段数从 1 开始，是因为第一段在遇到超限之前已经存在。
