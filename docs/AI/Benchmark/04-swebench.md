# SWE-bench

仓库级软件工程基准：给一个真实 GitHub Issue，要求模型产出能通过单元测试的 patch。是 Coding Agent 最重要的评测。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | 2023-10（arXiv），ICLR 2024 oral |
| 论文 | [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)（Princeton NLP，Jimenez et al.） |
| 官网 | [swebench.com](https://www.swebench.com/) |

## Bench 结构

- **规模**：2,294 个实例，来自 12 个流行 Python 仓库（django、scikit-learn、matplotlib、sympy 等）的真实 Issue–PR 对。
- **任务形式**：输入 `problem_statement`（Issue 文本）+ 仓库在 `base_commit` 处的代码，输出一个 git patch。
- **评测**：在对应 commit 的 Docker 环境中应用 patch 并跑测试：

    - `FAIL_TO_PASS`：必须从失败变为通过的测试；
    - `PASS_TO_PASS`：必须保持通过的测试（防回归）。

    全部满足记为 resolved，指标为 **Resolve Rate**。

| 变体 | 规模 | 说明 |
|------|------|------|
| Full | 2,294 | 完整集 |
| Lite | 300 | 快速迭代子集 |
| Verified | 500 | OpenAI 2024-08 发布，人工验证可解、无歧义 |
| Multimodal | 517 | 含截图 / 前端 UI 类任务 |
| Pro | 1,865 | Scale AI 2025，防污染（copyleft + 私有代码）、更难 |

## 重点测试能力

- **仓库级代码理解**：在数万行陌生代码中定位问题。
- **需求 → 修复的端到端工程能力**：读懂 Issue、设计修复、不破坏既有行为。
- **Agent 系统能力**：检索、编辑、执行测试的循环（scaffold 影响巨大——同一模型配不同 agent 框架分数差距可达数倍）。

!!! info "深入笔记"
    数据字段细节、sb-cli 提交流程、SWE-bench Pro 结果分析见 [Agents/03-benchmark](../Agents/03-benchmark.md)。

## 举例

```text
instance_id: scikit-learn__scikit-learn-10508
problem_statement:
  "Is it possible to use GridSearchCV with
   precomputed sparse distance matrices?
   I get the following error: ..."
→ 模型需定位 sklearn 中相关校验逻辑并修改，
  使 FAIL_TO_PASS 中的新增测试通过。
```

## 参考

- [arXiv 2310.06770 — SWE-bench](https://arxiv.org/abs/2310.06770)
- [SWE-bench 官网](https://www.swebench.com/)
- [princeton-nlp/SWE-bench（GitHub）](https://github.com/princeton-nlp/SWE-bench)
- [SWE-bench Pro — Scale AI](https://scale.com/blog/swe-bench-pro)
