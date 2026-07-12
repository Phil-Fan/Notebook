# TODO — AI 笔记结构调整

## 1. Flow Matching (LLM | Models)

- [x] 新建 `docs/AI/LLM/Models/10-FlowMatching.md`
- [x] 在 `mkdocs.yml` 的 "LLM | Models" 导航中添加 `AI/LLM/Models/10-FlowMatching.md`

## 2. VLA（新建子分类）

- [x] 新建目录 `docs/AI/VLA/`
- [x] 新建 `docs/AI/VLA/index.md`
- [x] 在 `mkdocs.yml` AI 下新增 `"VLA | 视觉-语言-动作"` 导航节点

## 3. RL 强化学习新增 PPO / GRPO

- [x] 新建 `docs/AI/RL/method/01-ppo.md`
- [x] 新建 `docs/AI/RL/method/02-grpo.md`
- [x] 将 `docs/AI/RL/method/02-infra.md` 重命名为 `04-infra.md`

## 4. 将 OPD 从 LLM/Sci 移动到 RL

- [x] 移动 `docs/AI/LLM/Sci/OPD.md` → `docs/AI/RL/method/03-opd.md`
- [x] 删除原 `docs/AI/LLM/Sci/OPD.md`
- [x] 从 `mkdocs.yml` 的 "LLM | Scientist Roadmap" 中移除 OPD 条目
- [x] 在 `mkdocs.yml` 的 "RL | 强化学习" method 中添加新条目

## 5. 同步更新

- [x] 更新 `docs/AI/index.md` TOC（移除 SEC，添加 VLA）
- [x] 更新 `docs/AI/RL/index.md`（PPO/GRPO/OPD/infra）
- [x] 更新 `AGENTS.md` 目录结构（VLA + RL method）
- [x] `pre-commit run --all-files` 通过
- [x] `uv run mkdocs build` 构建成功
