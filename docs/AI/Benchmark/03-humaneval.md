# HumanEval

OpenAI 随 Codex 发布的手工编写代码生成基准，`pass@k` 指标的出处，函数级代码评测的事实标准。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2021-07（arXiv） |
| 论文 | [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)（OpenAI，Chen et al.，即 Codex 论文） |
| 代码 | [openai/human-eval（GitHub）](https://github.com/openai/human-eval) |

## Bench 结构

- **规模**：164 道手写 Python 编程题（非网络爬取，人工编写以保证质量与原创性）。
- **格式**：每题包含

    - `task_id`（如 `HumanEval/0`）
    - `prompt`：函数签名 + docstring（含输入输出说明）
    - `canonical_solution`：参考实现
    - `test`：单元测试（平均每题约 7.7 个断言）
    - `entry_point`：函数名

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two
    numbers closer to each other than given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
```

- **评测方式**：模型补全函数体，把 `prompt + 生成代码 + test` 放进沙箱执行，全部断言通过即算正确。
- **指标 `pass@k`**：采样 n 个候选（如 n=200），无偏估计「k 个样本中至少 1 个通过」的概率。常用 `pass@1`（单次生成能力）与 `pass@10` / `pass@100`（配合验证器 / 重排的上限）。

## 重点测试能力

- **函数级代码补全**：从 docstring 理解需求并实现。
- **基础算法与边界处理**：字符串、列表、数值处理为主，难度约等于入门算法题。
- 不测仓库级理解、调试、重构——这些由 SWE-bench 等覆盖。

!!! note "现状"
    前沿模型 `pass@1` 已 >90%，基本饱和且污染严重。衍生版本：

    - **HumanEval+**：把测试用例扩充约 80 倍，减少「过拟合少量断言」的假阳性。
    - **MultiPL-E**：翻译成 18+ 种语言（C++、Rust、Go…）。
    - **MBPP**（Mostly Basic Python Problems）：974 题，更简单，常与 HumanEval 搭配报告。

## 举例

```python
# prompt
def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string out of the given list.
    If no string is present, return None.
    """

# canonical_solution
if not strings:
    return None
return max(strings, key=len)
```

## 参考

- [arXiv 2107.03374 — Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)
- [openai/human-eval](https://github.com/openai/human-eval)
- [EvalPlus（HumanEval+）](https://github.com/evalplus/evalplus)
