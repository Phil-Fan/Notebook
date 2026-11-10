# 215. 数组中的第 K 个最大元素

!!! abstract "题单坐标"
    **Hot 20 · 第 11 类「堆」** ｜ 难度：中等 ｜ 标签：`数组` `分治` `快速选择` `排序` `堆`

    一句话套路：维护一个大小为 `k` 的小顶堆，堆顶就是当前这 `k` 个数里最小的，也就是全体里的第 `k` 大；要平均线性就改用快速选择。

## 题干

> [力扣 215. 数组中的第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `k` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 $O(n)$ 的算法解决此问题。

**示例 1**

```text
输入：nums = [3,2,1,5,6,4], k = 2
输出：5
```

**示例 2**

```text
输入：nums = [3,2,3,1,2,4,5,5,6], k = 4
输出：4
```

**提示**

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## 思路

第 `k` 大是排序后下标 `n-k` 上的那个值（从 0 起、升序），允许重复。示例 2 降序是 `[6,5,5,4,...]`，第 4 个是 4，两个 5 各算一次。

**大小为 k 的小顶堆。** 堆里永远是「目前见过的最大的 k 个数」，小顶堆的堆顶是这 k 个里最小的。

1. 先把前 `k` 个数放进小顶堆。
2. 之后每个数如果比堆顶大，就替换堆顶。比堆顶小的不可能进入前 k 名。
3. 扫完，堆顶就是第 `k` 大。

大顶堆把全部元素都放进去再 `pop` k 次也能做，但堆的大小是 `n` 不是 `k`。`k` 远小于 `n` 时小顶堆更合适。Python 的 `heapq` 是小顶堆。

**快速选择。** 和第 `k` 小的划分一样：`partition` 把枢轴放到最终下标 `p`，若 `p == n-k` 就找到了；`p` 更小就只去右边，更大就只去左边。平均 $O(n)$，最坏 $O(n^2)$。题目写了「必须 $O(n)$」，指的是平均线性的这一种；堆的 $O(n \log k)$ 在 $n = 10^5$ 也能过。面试先写堆，追问线性再写划分。

**走一遍示例 1。** `nums = [3,2,1,5,6,4]`，`k = 2`，小顶堆：

| 读到 | 堆（堆顶在左） | 说明 |
|:-----|:---------------|:-----|
| 3, 2 | `[2, 3]` | 先装满 k 个 |
| 1 | `[2, 3]` | 1 < 2，丢掉 |
| 5 | `[3, 5]` | 5 替换 2 |
| 6 | `[5, 6]` | 6 替换 3 |
| 4 | `[5, 6]` | 4 < 5，丢掉 |

堆顶 5 就是第 2 大。

## 代码（带注释）

> 按力扣提交格式写：一个 `Solution` 类。堆这一版用标准库 `heapq`，快速选择只用列表。

=== "主推：大小为 k 的小顶堆"

    ```python
    import heapq


    class Solution:
        def findKthLargest(self, nums: list[int], k: int) -> int:
            heap = nums[:k]
            heapq.heapify(heap)
            for value in nums[k:]:
                if value > heap[0]:
                    heapq.heapreplace(heap, value)
            return heap[0]
    ```

    `heapreplace` 先弹出堆顶再放入新值，比「`heappop` 再 `heappush`」少一次上滤。`k = n` 时循环不执行，堆顶是最小值，也就是第 `n` 大。

=== "对照：快速选择"

    ```python
    class Solution:
        def findKthLargest(self, nums: list[int], k: int) -> int:
            target = len(nums) - k

            def partition(left: int, right: int) -> int:
                pivot = nums[right]
                store = left
                for i in range(left, right):
                    if nums[i] < pivot:
                        nums[store], nums[i] = nums[i], nums[store]
                        store += 1
                nums[store], nums[right] = nums[right], nums[store]
                return store

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_at = partition(left, right)
                if pivot_at == target:
                    return nums[pivot_at]
                if pivot_at < target:
                    left = pivot_at + 1
                else:
                    right = pivot_at - 1
            return nums[left]
    ```

    升序里第 `k` 大的下标是 `n-k`。划分之后只有包含这个下标的一侧还要看。枢轴固定取右端时，已排序数组会退化成 $O(n^2)$；把枢轴换成随机下标再和右端交换，可以避开这种输入。

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| 大小为 k 的小顶堆 | $O(n \log k)$ | $O(k)$ | 默认，实现短 |
| 全排序 | $O(n \log n)$ | $O(1)$ 或 $O(n)$ | `k` 接近 `n` 时差不多，但没利用「只找一个」 |
| 快速选择 | 平均 $O(n)$，最坏 $O(n^2)$ | $O(1)$ | 追问线性时间时 |

$n \le 10^5$。$O(n \log n)$ 和 $O(n \log k)$ 都能过；题目点名 $O(n)$，是在提醒不要停在排序。

## 教学动画（HTML）

<iframe src="215-kth-largest-element-in-an-array-demo.html" title="第 K 大 · 大小为 k 的小顶堆" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

示例 1 逐个读入。堆里只留 2 个数，比堆顶大才替换，最后堆顶标成答案。空格播放 / 暂停，`←` `→` 单步，`R` 重置。

## 易错点

- **用大顶堆还只留 k 个**：大顶堆的堆顶是最大的，丢掉堆顶会把第 1 大丢掉，剩下的不是第 `k` 大。小顶堆才是「踢掉当前前 k 名里最差的」。
- **第 k 大做成去重**：`[3,2,3,1,2,4,5,5,6]` 的第 4 大是 4，不是「第 4 个不同的数」3。重复元素各算一名。
- **`heapq` 当成大顶堆**：标准库只有小顶堆。要模拟大顶堆得存相反数，这题不需要。
- **快速选择的目标下标写成 `k`**：`k = 2` 时升序下标是 `n-2` 不是 2。示例 1 下标 2 上是 3，不是 5。
- **替换时不比较堆顶**：每个新元素都 `heapreplace`，堆里就不是最大的 k 个了。

## 延伸

- [← 返回 Hot 20 题单](../../../index.md) · [本类总览：队列与堆](../index.md)
- 同类题：[347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) · [703. 数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)（堆一直留着，来一个处理一个）
