# 砍树

[P1873](https://www.luogu.com.cn/problem/P1873)。树木高度为 `heights`，锯片高度为 `h` 时，能得到的木头是 \(\sum \max(0, height - h)\)。求最高的 `h`，使得到的木头不少于 `need`。

锯得越高，木头越少。二分这个高度。

```python
class Solution:
    def max_height(self, heights: list[int], need: int) -> int:
        def wood(h: int) -> int:
            return sum(height - h for height in heights if height > h)

        left, right = 0, max(heights)
        while left < right:
            mid = (left + right + 1) // 2
            if wood(mid) >= need:
                left = mid
            else:
                right = mid - 1
        return left
```

中点要向上取整。如果写成 `(left + right) // 2` 并且满足时 `left = mid`，`left` 和 `right` 只差 1 时中点会停在 `left`，循环不会结束。
