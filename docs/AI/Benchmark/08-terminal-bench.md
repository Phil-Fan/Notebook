# Terminal-Bench

真实命令行环境中的 Agent 基准：每个任务一个独立 Docker 环境 + 人工编写的测试，考察模型「像工程师一样用终端干活」的能力。

## 发行时间与论文

| 项 | 内容 |
|----|------|
| 发布时间 | v1.0 2025-04（arXiv）；v2.0 2025-10 发布、论文 [arXiv 2601.11868](https://arxiv.org/abs/2601.11868)（2026-01） |
| 机构 | Stanford / Laude Institute 等 |
| 官网 | [tbench.ai](https://www.tbench.ai/) |
| 代码 | [laude-institute/terminal-bench（GitHub）](https://github.com/laude-institute/terminal-bench) |

## Bench 结构

### 任务格式

每个任务是一个目录，包含：

- `Dockerfile`：独立、可复现的环境（装好对应软件栈）；
- `task.yaml` / `instructions.md`：自然语言任务说明；
- `solution.sh`：人工编写的 oracle 解法；
- `tests`（pytest）：验证任务是否完成的测试。

Agent 通过 bash 会话与环境交互，评测跑测试判定成败，指标为 **task success rate**。

### 规模与内容

- **v1.0**：89 个任务，覆盖软件工程（构建、调试、git 操作）、系统管理（配置服务、权限）、科学计算（跑实验、处理数据）、安全（CTF 式题目）等。
- **v2.0**：300+ 任务，配套改进：

    | 改进 | 说明 |
    |------|------|
    | 更严格验证 | 重写测试，堵住「测试作弊」（reward hacking）漏洞 |
    | Harbor 框架 | 标准化 agent ↔ 环境交互与评测 |
    | 污染控制 | 标注任务是否可能出现在训练数据中 |
    | Terminal-Bench Hard | 更难子集，头部模型仍 <65% |

## 重点测试能力

- **长程 bash 操作**：多命令组合、管道、环境变量、进程管理。
- **环境探索与调试**：读日志、查配置、定位错误，而非「一次写对」。
- **领域工具链**：编译器、包管理器、数据库、Docker、tmux 等真实工具。
- **指令精确遵循**：输出格式、文件位置等细节都要对，测试会严格检查。

!!! note "与 SWE-bench 的区别"
    SWE-bench 聚焦「读代码 → 出 patch」；Terminal-Bench 更宽，覆盖一切需要终端完成的工作（装环境、跑训练、改系统配置），且交互是持续 shell 会话而非单次 patch 输出。

## 举例

```text
任务示例（v1.0 风格）:
  "The nginx server in this container fails to start.
   Diagnose the issue, fix it, and ensure the service
   starts automatically on boot."

Agent 需要:
  systemctl status nginx → 读错误日志 → 发现配置语法错误
  → 修 /etc/nginx/nginx.conf → 重启并验证 → 配置开机自启
  → 通过 pytest 检查（服务运行中 + 配置正确）
```

## 参考

- [Terminal-Bench 官网与 Leaderboard](https://www.tbench.ai/)
- [arXiv 2504.11868 — Terminal-Bench v1](https://arxiv.org/abs/2504.11868)
- [arXiv 2601.11868 — Terminal-Bench 2.0](https://arxiv.org/abs/2601.11868)
- [laude-institute/terminal-bench](https://github.com/laude-institute/terminal-bench)
