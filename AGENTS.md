# Notebook Repository Agent Guide

MkDocs Material 个人知识库。笔记在 `docs/`，导航在 `mkdocs.yml`，钩子在 `hooks/`，主题覆盖在 `overrides/`。

## 技术栈

| 项 | 规范 |
|----|------|
| Python | 3.12（`<3.13`），**uv** + `pyproject.toml` |
| 框架 | MkDocs + Material |
| 命令 | `uv run mkdocs serve` / `build`；格式化用 pre-commit |
| 质量 | **pre-commit** + CI `Quality Check` |
| 钩子 | autocorrect、ruff / pyrefly（`hooks/`） |
| CI | `.github/workflows/check.yml`（`pre-commit/action` + `uv sync`） |
| 部署 | Cloudflare Pages 项目 `notebook`（连 GitHub，push `main` 自动构建）；仓库内**不再**保留部署 workflow |

- 勿迁到 VitePress/Next；**不使用 Makefile**，统一用 `uv` / pre-commit。
- **提交前必须**通过 pre-commit / lint（见下节）；改结构后再 `uv run mkdocs build`。


## 常用命令

```bash
uv sync
uv run mkdocs serve   # 开发
uv run mkdocs build                           # 构建
pre-commit run --all-files                    # 格式化 + lint（与 CI 对齐）
uv run ruff check --fix hooks/               # 仅 Python hooks
rm -rf site                                   # 清理构建产物
```


## 笔记分类规则

- 内容**只**放在 `docs/` 对应主题目录，不写在仓库根。
- 大类：`AI` / `Math` / `CS` / `Robotics` / `Class`；其下再分子主题目录。
- 每个文件夹优先提供 `index.md`，索引该目录下笔记。
- 系列笔记可用编号前缀：`00-intro.md`、`01-xxx.md`。
- 图片与附件就近放（同目录或 `assets/`）；站点级样式用 `docs/style/`。
- 自动化只放 `hooks/`；主题模板只放 `overrides/`。
- Markdown：`#` 一级标题、代码块标语言、标题层级不跳级。

新增笔记：落盘 → 注册 nav → 更新 index → `uv run mkdocs serve` 自检。

## 目录文档同步（强制）

**更改本仓库目录/主题时，必须同步更新下列「目录文件」：**

| 变更 | 必更文件 |
|------|----------|
| 增删/移动 `docs/` 下目录或页面 | 本文件 **「目录 / docs/ 结构」** |
| 导航可见性 | `mkdocs.yml` → `nav` |
| 主题/子目录索引 | 对应 `docs/**/index.md` |
| AI 等分区 TOC | 如 `docs/AI/index.md` 的 TOC 块 |
| 工作区级说明（若从 websites 根管理） | 上级 `websites/AGENTS.md` 总览 |

未更新目录文件即视为改动未完成。

## 提交前质量检查（强制）

克隆后安装钩子（一次）：

```bash
pre-commit install
```

提交前在仓库根执行（与 CI 对齐；失败则禁止提交，勿默认 `--no-verify`）：

```bash
pre-commit run --all-files
```

| 检查 | 工具 | 范围 |
|------|------|------|
| 中文排版 | autocorrect | 全仓文本 |
| Python lint + format | ruff | `hooks/` |
| Python 类型 | pyrefly（`uv run`） | `hooks/` |

CI：push / PR 到 `main` 触发 `.github/workflows/check.yml`（`uv sync` + pre-commit）。

部署：由 Cloudflare Pages（项目名 `notebook`）在 push `main` 后自动构建并发布 `note.philfan.cn`；仓库内不再有部署 workflow，GitHub Pages 已关闭（`gh-pages` 分支已删除），勿再加回。

**CI 要求（强制）**：所有推送必须通过 Quality Check。若 CI 失败，必须立即修复后重新推送。严禁跳过或忽略 CI 错误。

提交前执行 `pre-commit run --all-files` 并与 CI 完全对齐：

- autocorrect：中文排版修正（中英文空格、标点规范等）
- ruff：`hooks/` 下 Python 代码 lint + format
- pyrefly：`hooks/` 下 Python 类型检查

## Conventional Commits

```text
<type>(<scope>): <subject>
```

`docs` / `fix` / `feat` / `refactor` / `chore` / `ci` 等。  
scope 示例：`llm`、`math`、`hooks`、`nav`。一次提交一事；祈使句。

```text
docs(llm): add speculative decoding notes
fix(hooks): handle empty toc headings
ci: align pre-commit with Quality Check workflow
```

## Agent

- 最小改动；不回滚无关用户改动。
- 改结构必做 **目录文档同步**（上节）；如果更改了文件目录，需要对应更改 mkdocs.yml 以及其他文件
- **提交前跑 pre-commit / lint**，通过后再 commit。
- 说明如何验证；`CLAUDE.md` → 软链到本文件；只维护 `AGENTS.md`。
