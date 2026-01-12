# LLM + RL 后训练

## 1. 后训练在干什么

目标：把“会说话的基础模型”变成“更符合人类偏好/任务指标/安全策略的助手”。

核心方法（RL 路线）：

* **采样（rollout）**模型输出 → **打分（reward）** → 构造 **advantage** → 用 **受约束的策略优化（PPO/GRPO）**更新模型输出分布
* 同时用 **KL / clip / reference policy** 控制更新不要偏离太远，避免训练不稳定或能力退化

一句话：

> 后训练不是在学“标准答案 token 标签”，而是在学“什么样的输出更值得更常出现”。

---

## 2. 两条主线：控制流 vs 计算流

### 控制流（算法主逻辑 / 调度）

负责把 RL 过程串起来：

1. rollout（生成样本）
2. reward 打分（含 KL/规则等整形）
3. advantage / return 计算
4. update actor/critic（调度训练步数、mini-batch、同步权重、记录指标、保存 ckpt）

### 计算流（重计算 / 分布式）

负责把模型推理/训练跑稳跑快：

* 推理：高吞吐 generate（vLLM/SGLang 等）
* 训练：forward/backward/optimizer（FSDP/Megatron 等）
* 分布式通信、显存优化、容错

---

## 3. 名词解释：actor / critic / reward / ref / logprob 都是什么

### Actor（策略模型）

* 负责 **生成 token** 的 LLM（你要优化的主模型）
* 训练时更新它的参数（全参 / LoRA / 部分层）

### Critic（价值模型）

* 不负责生成文本，只输出 **value 标量** (V(s_t))
* 用来当 baseline，降低方差，帮助算 advantage（PPO 常用；GRPO 往往不需要）

对比：

* actor：输出词表分布（用于生成/算 logprob）
* critic：输出 value（用于 baseline/advantage）

### Reward（奖励）

* 对一条回答打分（来源：RM、规则、judge 等）
* 可做整形：长度惩罚、格式惩罚、KL 惩罚等

### Ref（reference policy，参考模型）

* 通常是 **SFT 模型快照**
* 作用：作为“锚点”做 KL 约束，防止策略跑飞
* 一般 **冻结不训练**

### logprob / old_logprob / ref_logprob

* logprob：当前 actor 对“实际生成 token”的对数概率
* old_logprob：rollout 时保存的旧策略 logprob（PPO 需要新旧比值）
* ref_logprob：reference policy 对同一 token 的 logprob（用于 KL 约束/惩罚）

---

## 4. rollout 是什么（LLM 语境）

rollout = 用当前 actor 对 prompt 采样回答，并记录训练所需证据：

输出通常包含：

* `prompt`、`response_tokens`
* `old_logprobs`（PPO 必需）
* `ref_logprobs`（常用于 KL）
* （可选）`values`（如果有 critic）
* `reward`（来自 RM/规则）

直觉：

> rollout 就像“用模型写答案 + 把它怎么写的也记下来”。

---

## 5. advantage 是什么意思（为什么要它）

advantage 表示：

> 这次选择（这条回答/这个 token）比“平均水平 baseline”好多少/差多少。

* advantage > 0：提高这些 token 序列出现概率
* advantage < 0：降低这些 token 序列出现概率

为什么需要：

* reward 波动大，直接用 reward 更新会很不稳
* baseline（critic 或组内均值）能降方差，让学习信号更稳定

---

## 6. PPO vs GRPO（重点差异）

### PPO（常见：有 critic）

* 用 critic 的 value 作为 baseline，算 advantage（如 GAE）
* 更新时用 **新旧策略概率比值** + **clip/KL** 控制步子别太大
* 通常包含：actor update + critic update

### GRPO（常见：无 critic）

* 对同一 prompt 采样一组回答（group）
* 用组内 mean/std 做 baseline，构造相对 advantage
* 省掉训练 critic 的开销，常用于推理型任务的偏好优化

一句话对比：

* PPO：baseline 来自 critic
* GRPO：baseline 来自“同题多答的组内对比”

---

## 7. 有了 advantage 怎么更新 LLM（更新哪些参数、如何更新）

更新的是 actor 的可训练参数（全参/LoRA/部分层）：

1. 用 batch 做一次 forward 得到 `new_logprob`
2. 结合 `old_logprob` 得到概率比值（PPO）
3. 用 advantage 加权构造策略损失（并加 clip / KL / entropy 等项）
4. `loss.backward()` → `optimizer.step()` 更新参数
5. 同步最新权重到 rollout 侧（推理引擎）

备注：

* PPO 中 critic 还会用 return 拟合 value（MSE / huber 等）更新 critic 参数
* ref 与 reward model 通常冻结不更新

---

## 8. 映射到 verl：rollout engine / model engine / checkpoint 的正确理解

你提出的三段理解需要这样“对齐”到 verl 的分工：

### ✅ Rollout engine（可接 vLLM）

* 负责 rollout/generation（高吞吐推理）
* 接收训练侧同步的 actor 权重
* “更新权重”一般是：在 rollout worker 内 **reload / load_weights / 更新 LoRA**（具体实现依赖后端）
* 不一定要“新建另一个 engine”，可能是原地 reload，也可能是双缓冲/重启（取决于工程策略）

### ✅ Model engine（训练后端：FSDP/Megatron）

* 负责训练：forward/backward/optimizer step
* 负责保存/加载训练状态的接口（与 checkpoint 系统联动）
* **不是**专门“计算 advantage 的引擎”

  * advantage 更多是 trainer/controller 的算法逻辑（把 reward、value、logprob 拼起来算）

### ✅ Checkpoint（持久化/恢复）

* 作用：保存模型参数 + 优化器 + 训练进度等，用于容错与恢复
* **不是**“用于更新模型”的引擎

  * 真正的更新发生在 model engine 的 optimizer step

---

## 9. 一张“数据流”速查图（最常用的理解方式）

```
prompt
  │
  ▼
[Rollout Engine / vLLM]  生成 response_tokens
  │   产出: tokens, old_logprobs, (可选 values), ref_logprobs
  ▼
[Reward / Rule / RM]     产出 reward（可含 KL shaping）
  │
  ▼
[Trainer/Controller]     计算 advantage / return（PPO:用 critic；GRPO:组内对比）
  │
  ▼
[Model Engine / FSDP/Megatron]  用 advantage 更新 actor（+ critic）
  │
  ├── (可选) save checkpoint
  ▼
同步权重到 Rollout Engine（reload / load_weights / LoRA update）
```
