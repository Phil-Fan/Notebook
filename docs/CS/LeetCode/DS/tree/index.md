# 树

树有 \(n\) 个节点和 \(n-1\) 条边，无环且连通。

- 节点的**深度**：根到该节点的路径长度。
- 节点的**高度**：该节点到某片叶子的最长路径长度。树高等于根的高度。
- \(m\) 叉树第 \(i\) 层最多 \(m^{i-1}\) 个节点，高度为 \(h\) 时节点总数最多 \(\frac{m^h-1}{m-1}\)。

二叉树每个节点最多两个孩子。遍历顺序：

| 名称 | 顺序 |
|:-----|:-----|
| 先序 | 根、左、右 |
| 中序 | 左、根、右 |
| 后序 | 左、右、根 |

```python
class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def preorder(node: TreeNode | None, out: list[int]) -> None:
    if node is None:
        return
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)
```

## 二叉查找树

每个节点的左子树都更小，右子树都更大。查找、最小、最大都是沿着一条路走。

```python
def contains(node: TreeNode | None, target: int) -> bool:
    while node is not None:
        if target == node.val:
            return True
        node = node.left if target < node.val else node.right
    return False


def find_min(node: TreeNode) -> TreeNode:
    while node.left is not None:
        node = node.left
    return node


def insert(node: TreeNode | None, value: int) -> TreeNode:
    if node is None:
        return TreeNode(value)
    if value < node.val:
        node.left = insert(node.left, value)
    elif value > node.val:
        node.right = insert(node.right, value)
    return node


def remove(node: TreeNode | None, value: int) -> TreeNode | None:
    if node is None:
        return None
    if value < node.val:
        node.left = remove(node.left, value)
    elif value > node.val:
        node.right = remove(node.right, value)
    elif node.left is None:
        return node.right
    elif node.right is None:
        return node.left
    else:
        succ = find_min(node.right)
        node.val = succ.val
        node.right = remove(node.right, succ.val)
    return node
```

删除分三种：叶子直接摘掉；只有一个孩子就用那个孩子顶上；两个孩子时用右子树的最小值替换自己，再递归删掉那个最小值。

## AVL

每个节点左右子树高度差不超过 1，查找是 \(O(\log n)\)。插入比普通 BST 贵，查询多的时候划算。

失衡时看从失衡点往下的三个节点，把中间值提升为根：

```text
右右（单旋，左旋）左右（先左旋再右旋）
    z                        z
   /                        /
  y                        x
   \                      /
    x                    y

左旋 y：先把 x 左旋成直线，再对 z 右旋
  y                        y
 / \                      / \
z   x                    z   x
```

```python
def height(node: TreeNode | None) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def rotate_left(z: TreeNode) -> TreeNode:
    y = z.right
    assert y is not None
    z.right = y.left
    y.left = z
    return y


def rotate_right(z: TreeNode) -> TreeNode:
    y = z.left
    assert y is not None
    z.left = y.right
    y.right = z
    return y
```

平衡因子是左高减右高。大于 1 且左孩子偏左，做一次右旋；大于 1 且左孩子偏右，先左旋左孩子再右旋自己。小于 -1 时对称处理。

## 红黑树

根是黑的，插入的新节点是红的。最长路径不超过最短路径的 2 倍，旋转比 AVL 少。

叔叔是红色：父、叔、祖父颜色取反，继续向上看。叔叔是黑色：按 AVL 的方式旋转，再改颜色。

查找路径会比严格平衡的 AVL 略长。连续插入时更稳。

## 伸展树

一个节点被访问后，近期很可能再被访问。每次访问后把它转到根上。输入法候选、缓存适合这种局部性。

## B 树与 B+ 树

多路平衡查找树，所有叶子在同一层。一个节点可以放很多键，适合磁盘页。

```text
B 树：内部节点既有键也有记录
        [10 | 20]
       /    |    \
   [5]    [15]   [25 30]

B+ 树：内部节点只做索引，数据全在叶子，叶子之间串成链表
        [10 | 20]
       /    |    \
   [5] -> [15] -> [25 30]
```

B+ 树把内部节点的空间让给索引，范围扫描沿叶子链表走。

## 题目

| 题目 | 难度 | 状态 | 一句话 |
|:-----|:-----|:-----|:-------|
| [199 二叉树的右视图](problems/199-binary-tree-right-side-view.md) | 中等 | ✔ 已整理 | 层序取每层最后一个，或先右后左的 DFS |

[← 返回数据结构](../index.md)
