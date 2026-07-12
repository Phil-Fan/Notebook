# Contributing Guide

首先，感谢你对我的个人笔记项目感兴趣！❤️

这是一个个人知识库项目，主要用于记录和分享学习笔记。虽然这是一个个人项目，但我非常欢迎各种形式的贡献和建议。如果你发现任何错误或有改进建议，都可以帮助让这个知识库变得更好。

如果你喜欢这个项目，但没有时间贡献，也可以通过以下方式支持：

- 给项目点个 Star
- 分享这个项目给其他人
- 在你的项目中引用这个知识库
- 向你的朋友/同学推荐这个项目

## Table of Contents

- [Contributing Guide](#contributing-guide)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [Questions](#questions)
  - [Contributing](#contributing)
    - [Bug Reports](#bug-reports)
    - [Content Contribution](#content-contribution)
  - [Style Guide](#style-guide)
  - [Join the Project](#join-the-project)

## Code of Conduct

请保持友善和专业的交流态度。任何形式的骚扰或冒犯性言论都是不被接受的。

## Questions

在提出问题之前，建议你：

1. 查看项目的 [Documentation](https://phil-fan.github.io/)
2. 搜索已有的 [Issues](/issues) 看是否有类似问题
3. 进行 Google Search

如果以上方法都无法解决你的问题，你可以：

- 创建新的 [Issue](/issues/new)
- 提供尽可能多的上下文信息，提供必要的错误位置，错误信息，以及建议的修复方案（如果有）

## Contributing

### Bug Reports

如果你发现了文档中的错误或问题：

1. 搜索已有的 [Issues](/issues) 看是否有类似问题
2. 收集信息：
   - 文件路径 & 章节
   - 错误信息
   - 建议的修复方案（如果有）

### Content Contribution

如果你想贡献内容：

1. 确保内容符合项目的主题和范围
2. 遵循现有的文档结构和格式
3. 使用 Markdown 格式编写
4. 注意文档的可读性和准确性

## Style Guide

### Commit 格式

建议使用 Conventional Commits，便于后续检索和自动化处理：

```text
<type>(<scope>): <subject>
```

常用 `type`：

- `docs`: 文档内容新增或修改
- `fix`: 修复错误（如链接、脚本、构建问题）
- `feat`: 新增功能（如新工具、新自动化能力）
- `refactor`: 重构（不改变行为）
- `chore`: 维护性改动（依赖、配置、流程）

示例：

- `docs(ai): add CLIP notes and update evaluation section`
- `fix(hooks): handle empty toc anchors in toc_manager`
- `chore(ci): update upload workflow for docs deploy`

编写建议：

1. `subject` 使用祈使句，简洁明确（如 `add`, `update`, `fix`）
2. 首行尽量控制在 72 字符以内
3. 一次 commit 聚焦一个主题，避免混杂无关改动

### 文档格式

所有文档使用 Markdown，并通过 pre-commit 自动检查/格式化（`markdownlint-cli2` + `autocorrect`）。

推荐约定：

1. 标题层级连续，不跳级（`#` -> `##` -> `###`）
2. 文件开头保留一级标题，语义清晰（如 `# BERT`）
3. 代码块必须标注语言（如 ` ```python `、` ```bash `）
4. 列表风格保持一致，避免同一层级混用符号
5. 链接使用相对路径（仓库内）或完整 URL（外部）
6. 术语首次出现时给出中文/英文对照，提升可读性

提交前建议执行：

```bash
make format
```

## Join the Project

这是一个个人笔记项目，主要由我个人维护。

但如果你对某个特定领域特别感兴趣并希望长期贡献，欢迎通过 Issue 联系我讨论合作方式。

Feel free to contribute!
