# Notebook Repository Agent Guide

MkDocs Material 个人知识库。笔记在 `docs/`，导航在 `mkdocs.yml`，钩子在 `hooks/`，主题覆盖在 `overrides/`。

## 技术栈

| 项 | 规范 |
|----|------|
| Python | 3.12（`<3.13`），**uv** + `pyproject.toml` |
| 框架 | MkDocs + Material |
| 命令 | `uv run mkdocs serve` / `build`；格式化用 pre-commit |
| 质量 | **pre-commit** + CI `Quality Check` |
| 钩子 | markdownlint-cli2、autocorrect、ruff / pyrefly（`hooks/`） |
| CI | `.github/workflows/check.yml`（`pre-commit/action` + `uv sync`） |

- 勿迁到 VitePress/Next；**不使用 Makefile**，统一用 `uv` / pre-commit。
- **提交前必须**通过 pre-commit / lint（见下节）；改结构后再 `uv run mkdocs build`。

## 目录

```text
Notebook/
├── .github/workflows/check.yml   # Quality Check CI
├── .pre-commit-config.yaml
├── docs/           # 文档源（docs_dir）
├── hooks/          # 构建钩子
├── overrides/      # Material 主题覆盖
├── mkdocs.yml      # 站点配置 + nav
├── pyproject.toml / uv.lock
└── AGENTS.md
```

## 常用命令

```bash
uv sync
uv run mkdocs serve   # 开发
uv run mkdocs build                           # 构建
pre-commit run --all-files                    # 格式化 + lint（与 CI 对齐）
uv run ruff check --fix hooks/               # 仅 Python hooks
rm -rf site                                   # 清理构建产物
```

### `docs/` 结构

```text
docs/
├── index.md                 # 首页
├── board.md                 # 简介
├── friends.md / friend.csv  # 友链
├── logo.ico
├── style/                   # 站点 css / js / images（一般不进 nav）
│   ├── css/
│   ├── images/
│   └── javascripts/
│
├── AI/                      # 人工智能
│   ├── index.md
│   ├── Agents/              # 智能体（index / 开源框架 / 01-base / 02-system / accelerate）
│   ├── CV/                  # 计算机视觉
│   ├── DL/                  # 深度学习（含 06-GAN）
│   ├── LLM/
│   │   ├── index.md         # 概述
│   │   ├── 开源框架.md      # 训练/推理等开源清单
│   │   ├── Models/          # Attention…LLaVA…TTT…FlowMatching
│   │   ├── Sci/             # 训练与对齐：SFT / RL / 评测…
│   │   └── Engineer/        # 工程：RAG / vLLM / 推理优化 / …
│   ├── MLSys/               # 机器学习系统（CUDA、NV、CMU10_414/）
│   ├── frontier/            # 前沿基座模型技术报告
│   │   ├── index.md
│   │   ├── 01-gpt3.md
│   │   ├── 02-gpt4.md
│   │   ├── 03-llama.md
│   │   ├── 04-deepseek.md
│   │   ├── 05-qwen.md
│   │   ├── 06-gemini.md
│   │   ├── 07-claude.md
│   │   └── labs.md
│   ├── VLA/                 # 视觉 - 语言 - 动作（VLA）
│   │   ├── index.md          # 总览与知识框架
│   │   ├── 01-Foundations.md # 基础概念
│   │   ├── 02-Architectures.md # 架构范式
│   │   ├── 03-Models.md      # 模型族详解
│   │   ├── 04-Techniques.md  # 关键技术
│   │   ├── 05-Training.md    # 训练范式
│   │   ├── 06-Datasets.md    # 数据集与评测
│   │   └── 07-Ecosystem.md   # 开源生态与趋势
│   └── RL/
│       ├── index.md
│       ├── theory/          # 理论
│       └── method/          # PPO / GRPO / OPD / infra
│
├── Math/                    # 数学
│   ├── index.md
│   ├── Calculus/            # 微积分
│   ├── LinearAlgebra/       # 线性代数
│   ├── Opt/                 # 凸优化
│   ├── Statistic/           # 概率统计 → 已迁至 statistics-notes 仓库
│   ├── StochasticProcess/   # 随机过程
│   ├── OR/                  # 运筹学
│   ├── ML/                  # 机器学习（数学向）
│   └── *.md                 # 公式、信息论、logic、ODE、复变、signal 等
│
├── CS/                      # 计算机科学
│   ├── index.md
│   ├── Language/
│   │   ├── C.md / C++.md
│   │   └── Python/          # 语法与工程笔记
│   ├── Algorithm/           # 算法
│   ├── DS/                  # 数据结构
│   ├── OS/                  # 操作系统
│   ├── CN/                  # 计算机网络
│   ├── CTF/
│   └── Web3/
│
├── Robotics/                # 机器人 / 控制 / 嵌入式
│   ├── index.md
│   ├── Model/               # 建模、运动学、动力学
│   ├── Control/
│   │   ├── BASE/            # 控制基础
│   │   ├── ADV/             # 进阶
│   │   ├── Method/          # PID / LQR / MPC / …
│   │   └── Opt/
│   ├── Robo/                # 建图、定位、导航、规划、检测、无人机
│   ├── 嵌入式/              # 8051 / STM32 / FPGA / Jetson / …
│   └── IOT/                 # 物联网与协议
│
└── Class/                   # 课程与通识
    ├── English/             # 英语（雅思等）
    ├── Fin/                 # 金融（含 micro/）
    ├── Physics/             # 物理（含 .xmind）
    └── *.md                 # 浙大课程、法商、马原、设计软件等
```

### nav 对应

| nav 一级 | 路径 |
|----------|------|
| Home | `index.md`、`board.md`（简介）、`friends.md` |
| Math | `Math/` |
| AI | `AI/` |
| Robotics | `Robotics/` |
| CS | `CS/` |
| Class | `Class/` |

nav 路径相对 `docs/`（如 `Math/LinearAlgebra/01-basic.md`）。`use_directory_urls: false`。

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
| Markdown lint / 自动修 | markdownlint-cli2 | `*.md` / `docs/**` |
| 中文排版 | autocorrect | 全仓文本 |
| Python lint + format | ruff | `hooks/` |
| Python 类型 | pyrefly（`uv run`） | `hooks/` |

CI：push / PR 到 `main` 触发 `.github/workflows/check.yml`（`uv sync` + pre-commit）。

**CI 要求（强制）**：所有推送必须通过 Quality Check。若 CI 失败，必须立即修复后重新推送。严禁跳过或忽略 CI 错误。

提交前执行 `pre-commit run --all-files` 并与 CI 完全对齐：

- markdownlint-cli2：`*.md` 格式检查（规则见 `.github/.markdownlint.yaml`）
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
- 改结构必做 **目录文档同步**（上节）；改笔记必对 nav / index。
- **提交前跑 pre-commit / lint**，通过后再 commit。
- 说明如何验证；`CLAUDE.md` → 软链到本文件；只维护 `AGENTS.md`。
