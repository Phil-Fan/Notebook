# 栈

后进先出（LIFO）。`push` 放入，`pop` 取出最近放入的元素。

两种常见实现：

- 链表：在表头插入和删除。
- 数组：在尾部 `append` / `pop`。Python 的 `list` 就是这种。

```python
class Stack:
    def __init__(self) -> None:
        self.data: list[int] = []

    def push(self, value: int) -> None:
        self.data.append(value)

    def pop(self) -> int:
        return self.data.pop()

    def empty(self) -> bool:
        return not self.data
```

典型用途是算后缀表达式：遇到数字就入栈，遇到运算符就弹出两个数，算完再压回去。

```python
def eval_postfix(tokens: list[str]) -> int:
    stack: list[int] = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))
        else:
            stack.append(int(token))
    return stack[-1]
```

`eval_postfix(["2", "1", "+", "3", "*"])` 得到 `9`，对应 `(2 + 1) * 3`。

[← 返回数据结构](../index.md)
