<h1 align="center">Welcome to PhilFan's NoteBook 👋</h1>

<p align="center">
  <a href="https://github.com/Phil-Fan/Phil-Fan.github.io">
    <img alt="Contributions welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg" />
  </a>
  <a href="https://github.com/Phil-Fan/Phil-Fan.github.io/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-CC4.0-blue.svg" />
  </a>
  <a href="https://github.com/Phil-Fan/Phil-Fan.github.io/actions/workflows/static.yml">
    <img alt="deploy" src="https://github.com/Phil-Fan/Phil-Fan.github.io/actions/workflows/static.yml/badge.svg?branch=master" />
  </a>
</p>

## Quick Start

第一步，克隆仓库

```bash title="Clone the repository"
git clone --single-branch --branch master https://github.com/Phil-Fan/Notebook.git --depth 1
```

第二步，[安装 uv](https://docs.astral.sh/uv/getting-started/installation/)

```bash title="Install uv"
# 方法1: 使用 Homebrew（推荐）
brew install uv

# 方法2: 使用 wget 安装
wget -qO- https://astral.sh/uv/install.sh | sh
```

第三步，安装依赖

```bash title="Install dependencies"
cd Phil-Fan.github.io
uv sync
```

第四步，启动网站

```bash title="Serve the website"
make serve
```

打开`http://127.0.0.1:8000`即可查看网站

## Makefile 命令

项目提供了 Makefile 来简化常用操作：

| 命令 | 说明 |
| ------ | ------ |
| `make help` | 显示所有可用命令 |
| `make serve` | 启动 Mkdocs 开发服务器 |
| `make format` | 格式化所有文件（Markdown + Python） |
| `make format-md` | 格式化 Markdown 文件 |
| `make format-py` | 格式化 Python 文件 |
| `make install-dev` | 安装开发依赖 |
| `make build` | 构建 Mkdocs 站点 |
| `make clean` | 清理构建文件 |
| `make check-tools` | 检查格式化工具是否已安装 |

**示例：**

```bash
# 查看帮助
make help

# 格式化所有文件
make format

# 启动开发服务器
make serve

# 构建静态站点
make build
```

## Claude Code Slash Commands

项目配置了 Claude Code 的自定义 slash commands，可以在使用 Claude Code 时快速执行常见任务。

### 可用命令

| 命令 | 说明 |
| ------ | ------ |
| `/add [内容]` | 添加内容到知识库 |
| `/check-markdown [路径]` | 检查 Markdown 文件格式 |
| `/understand` | 理解这个知识库仓库的结构 |

**示例：**

```text
# 添加新知识点到知识库
/add 在 Python 中使用 async/await 处理并发

# 检查特定文件的格式
/check-markdown docs/AI/LLM/Engineer/01-LLMs.md

# 检查整个项目的格式
/check-markdown

# 了解仓库结构
/understand
```

### 自动格式化

配置了 PostToolUse hook，每次使用 `Write` 或 `Edit` 工具后会自动运行格式化：

- **markdownlint**：Markdown 语法检查和修复
- **autocorrect**：中英文格式自动修正
- **ruff**：Python 代码检查和修复

### 知识库归档规则

`/add` 命令会按照以下规则自动归档内容：

1. **目录分类**：自动判断内容所属的知识分类（AI/Math/Robotics/CS/Tools/Project/Class/Interest）
2. **文件定位**：搜索现有文件或创建新文件
3. **格式化**：按照项目规范格式化内容
4. **索引更新**：自动更新 index.md 和 mkdocs.yml
5. **格式检查**：运行 formatter 确保格式正确

## Contributing

欢迎贡献！欢迎贡献！欢迎贡献！

> 经过重构以后，仓库变小了很多，现在只有 20MB 左右，应该不会对大家的使用造成影响

## Star History

Give a ⭐️ if this notebook helps you!

[![Star History Chart](https://api.star-history.com/svg?repos=Phil-Fan/Phil-Fan.github.io&type=Date)](https://www.star-history.com/#Phil-Fan/Phil-Fan.github.io&Date)
