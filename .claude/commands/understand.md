---
description: 理解这个知识库仓库的结构
allowed-tools: Read, Bash, Glob, Grep
---

<!-- markdownlint-disable-next-line MD041 -->
理解这个知识库仓库的结构和组织方式。

## 项目概述

这是一个使用 Mkdocs Material 主题构建的个人知识库，包含多个学科领域的学习笔记和实践记录。

## 目录结构

```text
Note-Mkdocs/
├── docs/                 # 主要文档目录
│   ├── AI/              # 人工智能相关
│   ├── Math/            # 数学基础
│   ├── Robotics/        # 机器人学
│   ├── CS/              # 计算机科学
│   ├── Tools/           # 工具手册
│   ├── Project/         # 项目记录
│   ├── Class/           # 课程笔记
│   ├── Interest/        # 兴趣爱好
│   └── blog/            # 博客
├── hooks/               # Mkdocs hooks
├── .claude/             # Claude Code 配置
│   └── commands/        # Slash commands
├── formatter.sh         # 格式化脚本
├── pyproject.toml       # Python 项目配置
└── mkdocs.yml           # Mkdocs 配置文件
```

## 文件命名规范

1. **序号 - 主题.md**：如 `05-3-SGlang.md`，序号两位起步
2. **中文编号**：如 `1 空间描述与变换`
3. **英文缩写**：如 `LLM | Engineer Roadmap`

## 格式化工具

1. **markdownlint**：Markdown 语法检查
2. **autocorrect**：中英文格式自动修正
3. **ruff**：Python 代码格式化

运行格式化：

```bash
./formatter.sh
```

## 相关文件

- @mkdocs.yml - Mkdocs 配置和导航
- @pyproject.toml - Python 依赖和工具配置
- @AGENTS.md - 知识库归档 Agent 详细配置
- @formatter.sh - 格式化脚本
- @.github/.markdownlint.json - Markdownlint 配置

请根据需要探索具体目录和文件。
