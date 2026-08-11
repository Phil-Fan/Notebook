# Agent Benchmark

Agent 评测基准，聚焦 SWE-bench 系列。

## SWE-bench

### 概述

SWE-bench（Software Engineering Benchmark）由 Princeton NLP 提出，用于评估 LLM 在**真实软件工程任务**上的能力。核心思路：从 GitHub 热门 Python 仓库中收集已解决的 Issue 与对应 PR，要求模型根据 Issue 描述修改代码并通过单元测试。

| 属性 | 说明 |
|------|------|
| 任务来源 | 12+ 流行 Python 仓库的真实 Issue / PR |
| 数据规模 | 2000+ 实例（SWE-bench Full） |
| 评估方式 | 生成 patch → 应用到对应 Git commit → 运行测试（PASS_TO_PASS + FAIL_TO_PASS） |
| 数据获取 | HuggingFace `princeton-nlp/SWE-bench` |

### 数据格式

每条样本包含：

- **instance_id**：唯一标识
- **repo**：所属仓库
- **base_commit**：目标 Git commit
- **problem_statement**：Issue 描述（即 prompt）
- **hints_text**：可选提示
- **patch**（gold）：官方开发者修复
- **test_patch**：使 FAIL_TO_PASS 测试通过的测试变更
- **FAIL_TO_PASS / PASS_TO_PASS**：需要从失败变为通过的测试 & 必须保持通过的测试

### 变体

| 变体 | 规模 | 特点 |
|------|------|------|
| SWE-bench Full | 2000+ | 完整集 |
| SWE-bench Lite | 300 | 子集，快速迭代 |
| SWE-bench Verified | 500 | 人工验证的高质量子集 |
| SWE-bench Multimodal | — | 含多模态任务（截图 / UI 相关） |

### 评估流程

1. **生成预测**：Agent 接收 problem_statement + 代码上下文，输出 patch
2. **格式化**：写入 `predictions.json`（含 `instance_id`、`patch`、`model_name_or_path`）
3. **执行评估**：在对应 Docker 环境中应用 patch，运行测试
4. **计算指标**：Resolve Rate = 通过全部 FAIL_TO_PASS + PASS_TO_PASS 的实例占比

本地评估需要大量资源（每个实例独立 Docker 容器），推荐使用官方 `sb-cli` 远程评估。

### sb-cli 提交流程

```bash
# 1. 安装 & 认证
pip install sb-cli
sb-cli auth login --email <your_email>
# 邮箱验证码确认

# 2. 提交预测
sb-cli submit --split <dataset_split> --predictions <path_to_file> --run-id <unique_id>

# 3. 查看结果
sb-cli report --run-id <unique_id>
```

提交到排行榜需要在 [SWE-bench/experiments](https://github.com/SWE-bench/experiments) 仓库：

1. 创建目录，包含描述 `.md` 和 `metadata.yaml`（系统名称、是否开源、URL）
2. 开 PR，描述中注明联系邮箱和 run_id
3. 维护者附加结果、review、merge 后更新排行榜

## SWE-bench Pro

### 动机

SWE-bench 系列存在两个问题：

- **数据泄露**：流行开源库代码可能已在训练集中
- **难度不足**：头部模型在 Verified 上已超过 70%，区分度下降

### 设计

Scale AI 于 2025 年推出 SWE-bench Pro，核心改进：

| 维度 | SWE-bench Pro |
|------|---------------|
| 规模 | 1,865 实例，41 个仓库 |
| 防泄露 | 使用 copyleft 许可代码 + 私有企业代码，模型未见过 |
| 难度 | 平均修改 107.4 行代码、跨 4.1 个文件 |
| 任务多样性 | 每仓库 50-100 题，防止过拟合 |
| Prompt | 人工专家精炼，提供清晰需求但不暗示实现 |

### 结果

性能大幅下降，区分度显著提升：

| 模型 | SWE-bench Verified | SWE-bench Pro（开源） | SWE-bench Pro（私有） |
|------|-------------------|---------------------|---------------------|
| GPT-5 | >70% | 23.3% | 14.9% |
| Claude Opus 4.1 | >70% | 23.1% | 17.8% |
| GPT-4o | — | — | 4.9% |

语言差异显著：Python / Go 通过率 >30%，JavaScript / TypeScript 远低于此。头部模型跨语言和跨仓库表现更稳定，小模型波动大。

## 参考

- [SWE-bench 官网](https://www.swebench.com/)
- [SWE-bench Pro — Scale AI Blog](https://scale.com/blog/swe-bench-pro)
- [SWE-bench GitHub](https://github.com/princeton-nlp/SWE-bench)
- [SWE-bench/experiments](https://github.com/SWE-bench/experiments)
- [Use SWE-bench 教程](https://rugdmlsy.github.io/posts/Use-SWE-bench/)
