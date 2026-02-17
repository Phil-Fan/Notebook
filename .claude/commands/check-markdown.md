---
description: 检查 Markdown 文件格式
argument-hint: [文件路径或目录]
allowed-tools: Bash(markdownlint:*), Bash(autocorrect:*), Bash(ruff:*), Bash(./formatter.sh:*), Read
---

<!-- markdownlint-disable-next-line MD041 -->
检查并修复 Markdown 文件格式。

## 检查项目

1. **markdownlint 检查**
   - 使用 `.github/.markdownlint.json` 配置
   - 关闭的规则：line-length, MD033, MD036, MD046

2. **autocorrect 检查**
   - 自动修复中文标点、空格等格式问题
   - 统一中英文之间空格

3. **Python 代码格式**（如果存在）
   - 使用 ruff 检查和格式化
   - 配置：line-length = 100, target-version = py312

## 执行

检查整个项目：

```bash
./formatter.sh
```

$ARGUMENTS
