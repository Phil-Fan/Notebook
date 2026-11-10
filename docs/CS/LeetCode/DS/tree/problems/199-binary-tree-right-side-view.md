# 199. 二叉树的右视图

!!! abstract "题单坐标"
    **Hot 20 · 第 7 类「二叉树」** ｜ 难度：中等 ｜ 标签：`树` `深度优先搜索` `广度优先搜索` `二叉树`

    一句话套路：层序遍历时每层的最后一个节点就是从右边能看见的那个；DFS 按「先右后左」，每个深度第一次到达的节点也是它。

## 题干

> [力扣 199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/)

给定一个二叉树的根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**示例 1**

```text
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]

    1
   / \
  2   3
   \   \
    5   4
```

**示例 2**

```text
输入：root = [1,null,3]
输出：[1,3]
```

**示例 3**

```text
输入：root = []
输出：[]
```

右视图是每一层最靠右的节点，不是「一直走右孩子」。下面这棵只有左孩子的树，从右边看下去仍然能看见整条左链，答案是 `[1,2,4,5]`：

```text
    1
   /
  2
 /
4
/
5
```

**提示**

- 二叉树的节点个数的范围是 `[0, 100]`
- `-100 <= Node.val <= 100`

## 思路

「从右边能看见」等于：每一层恰好贡献一个节点，就是该层最右端。

**层序（BFS）。** 队列按层存放。处理一层时，这一层的最后一个元素就是右视图，然后把下一层的左孩子、右孩子依次入队。右孩子排在该层队尾，下一轮它就是「最后一个」。

**DFS。** 先走右子树，再走左子树，`depth` 表示当前层。`depth == len(ans)` 说明这一层还没记过，当前节点就是该层第一次被访问到的——右边先走，所以它是最右的。之后再走到同一层时不再记录。

两种写法看到的节点相同。BFS 和「一层一层看」的叙述一致；DFS 不需要队列，额外空间是递归栈 $O(h)$。

**走一遍示例 1。** BFS：

| 层 | 队列（左 → 右） | 追加 |
|:---|:----------------|:-----|
| 0 | `[1]` | 1 |
| 1 | `[2, 3]` | 3 |
| 2 | `[5, 4]` | 4 |

DFS 的访问顺序是 `1 → 3 → 4 → 2 → 5`。深度 0、1、2 第一次到达的是 1、3、4。走到 2、5 时对应深度已经有记录。

只有左链的那棵树，DFS 的右子树全是空，每一层的第一次到达就是左孩子自己，答案 `[1,2,4,5]`。如果只收集右孩子，会漏掉 2、4、5。

## 代码（带注释）

> 按力扣提交格式写：一个 `Solution` 类。`TreeNode` 由判题器提供，这里一并写出，方便本地跑。

=== "主推：层序，取每层最后一个"

    ```python
    class TreeNode:
        def __init__(self, val: int = 0) -> None:
            self.val = val
            self.left: TreeNode | None = None
            self.right: TreeNode | None = None


    class Solution:
        def rightSideView(self, root: TreeNode | None) -> list[int]:
            if root is None:
                return []
            ans: list[int] = []
            level = [root]
            while level:
                ans.append(level[-1].val)
                nxt: list[TreeNode] = []
                for node in level:
                    if node.left is not None:
                        nxt.append(node.left)
                    if node.right is not None:
                        nxt.append(node.right)
                level = nxt
            return ans
    ```

    先左后右入队，`level[-1]` 才是这一层最右边。空树在进循环之前返回。节点数不超过 100，用列表当队列即可。

=== "对照：先右后左的 DFS"

    ```python
    class Solution:
        def rightSideView(self, root: TreeNode | None) -> list[int]:
            ans: list[int] = []

            def dfs(node: TreeNode | None, depth: int) -> None:
                if node is None:
                    return
                if depth == len(ans):
                    ans.append(node.val)
                dfs(node.right, depth + 1)
                dfs(node.left, depth + 1)

            dfs(root, 0)
            return ans
    ```

    先左后右也能做，但记录条件要改成「这一层的最后一个」，必须等整层结束才知道是谁，反而更绕。先右后左才能在第一次到达时下结论。

## 复杂度

| 写法 | 时间 | 空间 | 什么时候用 |
|:-----|:-----|:-----|:-----------|
| BFS | $O(n)$ | $O(w)$，$w$ 是最大层宽 | 默认，和「每层最后一个」直接对应 |
| DFS | $O(n)$ | $O(h)$ | 想少写队列时 |

$n$ 是节点数。每个节点入队、出队各一次，或被访问一次。答案长度等于树高加一，最多 $n$。

## 教学动画（HTML）

<iframe src="199-binary-tree-right-side-view-demo.html" title="右视图 · 层序取每层最后一个" width="100%" height="960" style="border:0;border-radius:12px;" loading="lazy"></iframe>

示例 1 的树按层点亮。当前层最右边的节点标成绿色并写入答案，下一层的左右孩子按顺序进入队列。空格播放 / 暂停，`←` `→` 单步，`R` 重置。

## 易错点

- **只收集右孩子**：左链上的节点从右边一样看得见。示例 1 的 5 被 4 挡住，但 4 自己在右子树的更深层，要单独占一层。
- **BFS 先右后左入队还取 `level[-1]`**：队尾变成了最左边，答案会是 `[1,2,5]`。入队顺序和「取哪一端」必须配套。
- **DFS 先左后右，却用 `depth == len(ans)`**：记下来的是左视图。
- **空树返回 `[None]`**：根是空时应返回 `[]`，不要把空节点的值追加进去。

## 延伸

- [← 返回 Hot 20 题单](../../../index.md) · [本类总览：树](../index.md)
- 同类题：[102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) · [103. 二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
