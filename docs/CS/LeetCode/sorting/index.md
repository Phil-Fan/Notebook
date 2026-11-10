# 排序

比较排序里，只靠交换相邻元素的算法（冒泡、插入）下界是 \(\Omega(n^2)\)，因为 \(n\) 个互异元素的平均逆序数是 \(n(n-1)/4\)。

## \(O(n^2)\)

```python
def bubble_sort(nums: list[int]) -> list[int]:
    a = nums[:]
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def selection_sort(nums: list[int]) -> list[int]:
    a = nums[:]
    n = len(a)
    for i in range(n):
        small = i
        for j in range(i + 1, n):
            if a[j] < a[small]:
                small = j
        a[i], a[small] = a[small], a[i]
    return a


def insertion_sort(nums: list[int]) -> list[int]:
    """第 i 趟把 a[i] 插进前面已经有序的一段。"""
    a = nums[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def shell_sort(nums: list[int]) -> list[int]:
    a = nums[:]
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            key = a[i]
            j = i - gap
            while j >= 0 and a[j] > key:
                a[j + gap] = a[j]
                j -= gap
            a[j + gap] = key
        gap //= 2
    return a
```

## \(O(n \log n)\)

快速排序平均 \(O(n \log n)\)，最坏 \(O(n^2)\)（枢纽每次都切出 0 和 \(n-1\)）。

```python
def quick_sort(nums: list[int]) -> list[int]:
    a = nums[:]

    def partition(left: int, right: int) -> int:
        pivot = a[left]
        i, j = left + 1, right
        while i <= j:
            while i <= j and a[i] < pivot:
                i += 1
            while i <= j and a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        a[left], a[j] = a[j], a[left]
        return j

    def sort(left: int, right: int) -> None:
        if left < right:
            mid = partition(left, right)
            sort(left, mid - 1)
            sort(mid + 1, right)

    if a:
        sort(0, len(a) - 1)
    return a
```

归并排序把数组对半切开，各自排好，再线性合并。合并过程：

```text
左 [1, 4, 6]    右 [2, 3, 5]
        \        /
         [1, 2, 3, 4, 5, 6]
```

```python
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums[:]
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    out: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
```

堆排序：先建成大顶堆 \(O(n)\)，再把堆顶换到末尾并下滤，共 \(n\) 次，总时间 \(O(n \log n)\)。堆的下滤见 [队列](../DS/queue/index.md)。

```python
def heap_sort(nums: list[int]) -> list[int]:
    a = nums[:]

    def sift(n: int, i: int) -> None:
        while True:
            large = i
            left, right = 2 * i + 1, 2 * i + 2
            if left < n and a[left] > a[large]:
                large = left
            if right < n and a[right] > a[large]:
                large = right
            if large == i:
                return
            a[i], a[large] = a[large], a[i]
            i = large

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        sift(n, i)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift(end, 0)
    return a
```

## 非比较排序

桶排序：按值域划成若干桶，桶内再排序，最后按桶顺序拼起来。值分布均匀时接近 \(O(n)\)。

计数排序按「这一位是几」计数，再用前缀和决定位置。从后往前填可以保持稳定。

基数排序把整数按位对齐（短的补 0），从低位到高位各做一次稳定的计数排序。

```python
def counting_sort_digit(nums: list[int], exp: int) -> None:
    base = 10
    counts = [0] * base
    for value in nums:
        counts[(value // exp) % base] += 1
    for i in range(1, base):
        counts[i] += counts[i - 1]
    out = [0] * len(nums)
    for value in reversed(nums):
        digit = (value // exp) % base
        counts[digit] -= 1
        out[counts[digit]] = value
    nums[:] = out


def radix_sort(nums: list[int]) -> list[int]:
    a = nums[:]
    if not a:
        return a
    exp = 1
    while max(a) // exp:
        counting_sort_digit(a, exp)
        exp *= 10
    return a
```
