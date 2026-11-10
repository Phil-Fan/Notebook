# On Policy Distill

## 参考资料

- [OPSD：通过自蒸馏提升 LLM 推理能力 - 知乎](https://zhuanlan.zhihu.com/p/2003773186135831026)
- [Thinking Machines 新文章：On-Policy Distillation | TML 最近两个月连续发了几篇文章，终于有点 AI 实验室… - 知乎](https://www.zhihu.com/pin/1968462515513062544)
- [On-Policy Distillation - Thinking Machines Lab](https://thinkingmachines.ai/blog/on-policy-distillation/)

## 对比

RL：能够训练模型的行为特征，但是奖励信号过于稀疏，用 Karpathy 的话说，就是“sucking supervision through a straw”，效率太低。

SFT：本文主要讲蒸馏训练，它 Supervision 信号密集，能让 Student 较好模拟 Teacher 的语言特征，但是对于蒸馏数据分布之外的情形，则容易出错。这种情形叫做 Exposure Bias

On-policy Distillation 就是把二者结合起来：用 Teacher 模型作为奖励模型，让 Student 模型自己做推理，在 Token 级别提供奖励信号 - 对比 Teacher 模型和 Student 模型的 prediction，用 Reverse KL 做损失函数。

用学开车类比一下的话，传统的 Distillation（off-policy）就像是你坐在副驾驶，看教练开车，拿小本本记录教练的每个动作，然后自己模仿；而 On-policy Distillation，是你自己握着方向盘开，教练坐在副驾看，你每做错一个动作，教练就骂你一句，告诉你他自己会怎么做。off-policy 是人教人，on-policy 是事教人。

| 特性        | Forward KL                                                 | Reverse KL                                  |
| --------- | ---------------------------------------------------------- | ------------------------------------------- |
| 数学形式      | $D_{KL}(P\mid Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}$          | $D_{KL}(Q\mid P)=\sum_x Q(x)\log\frac{Q(x)}{P(x)}$                          |
| 期望是谁取的    | Teacher（$P$）                                               | Student（$Q$）                                |
| 谁决定样本权重   | Teacher                                                    | Student                                     |
| 优化目标      | 覆盖 Teacher 的整个分布（covering）                                 | 优化 Student 当前最可能生成的部分（mode-seeking）         |
| 典型应用      | 传统 Knowledge Distillation、Maximum Likelihood、Cross Entropy | On-Policy Distillation、RL 中的策略约束、变分推断中的部分优化 |
| 对 LLM 的含义 | 学习 Teacher 的完整输出分布                                         | 在 Student 自己的生成轨迹上，尽量让预测分布接近 Teacher        |

**一句话概括：Forward KL 的视角是“Teacher 希望你学什么”，Reverse KL 的视角是“Student 实际会做什么，就重点把它纠正成 Teacher 的样子”。这正是 On-Policy Distillation 选择 Reverse KL 的根本原因。**

!!! note "KL 散度"
    KL 散度衡量的是两个分布的差异,

    $$
    D_{KL}(P|Q)\ge 0
    $$

    并且当且仅当$P=Q$

    $$
    D_{KL}(P|Q)=0
    $$

    Reverse KL 越小越好，值越小，说明 Student 的预测分布越接近 Teacher。
    
    On-Policy Distillation 选择 Reverse KL，只是因为它把比较的重点放在 Student 自己实际会生成的 token 上，这与 on-policy rollout 的训练方式天然一致。


    用 **Jensen 不等式** 可以很快证明。

    设 $P,Q$ 是两个离散分布，且 $P(x)>0$ 时 $Q(x)>0$。

    $$
    D_{KL}(P\mid Q) = \sum_x P(x)\log\frac{P(x)}{Q(x)}
    $$

    改写成：

    $$
    D_{KL}(P\mid Q) = -\sum_x P(x)\log\frac{Q(x)}{P(x)}
    $$

    因为 $\log x$ 是凹函数，所以 Jensen 给出：

    $$
    \sum_x P(x)\log\frac{Q(x)}{P(x)}
    \le
    \log\left(
    \sum_x P(x)\frac{Q(x)}{P(x)}
    \right)
    $$

    右边化简：

    $$
    \log\left(
    \sum_x Q(x)
    \right)
    =
    \log 1
    =
    0
    $$

    所以：

    $$
    \sum_x P(x)\log\frac{Q(x)}{P(x)} \le 0
    $$

    两边乘以 $-1$：

    $$
    D_{KL}(P\mid Q)\ge 0
    $$

    等号成立当且仅当：

    $$
    \frac{Q(x)}{P(x)}
    $$

    在所有 $P(x)>0$ 的地方都是常数。

    又因为：

    $$
    \sum_x P(x)=\sum_x Q(x)=1
    $$

    所以这个常数只能是 $1$，即：

    $$
    P(x)=Q(x)
    $$

    因此：

    $$
    D_{KL}(P\mid Q)\ge 0
    $$

    且当且仅当 $P=Q$ 时取等号。

## 步骤

1. Student 自己生成一条回答（on-policy rollout）。
2. Teacher 不生成答案，只是在 Student 的轨迹上计算每个 token 的概率。
3. 用 Student 和 Teacher 的 log 概率之差估计 Reverse KL，并把它取负作为奖励（advantage）。
4. 将这个奖励交给标准的 RL（如 PPO/Importance Sampling）算法，更新 Student，使它更倾向于生成 Teacher 认为概率更高的 token。

```python
# Initialize teacher client (main):
teacher_client = service_client.create_sampling_client(
    base_model=teacher_config.base_model,
    model_path=teacher_config.load_checkpoint_path,
)

# Sample trajectories (main):
trajectories = do_group_rollout(student_client, env_group_builder)
sampled_logprobs = trajectories.loss_fn_inputs["logprobs"]

# Compute reward (compute_teacher_reverse_kl):
teacher_logprobs = teacher_client.compute_logprobs(trajectories)
reverse_kl = sampled_logprobs - teacher_logprobs
trajectories["advantages"] = -reverse_kl

# Train with RL (train_step):
training_client.forward_backward(trajectories, loss_fn="importance_sampling")
```

## 效果

实验证明，这个方法的效果好到难以置信。训练效率提升了，SFT 需要 200 万 prompts 才能达到的效果，用 On-policy Distillation 只要 77K 就能达到。另外，对于持续学习有意外的帮助：训练模型吸收新知识，会导致灾难性遗忘，比如指令遵循的表现严重下降。但如果在知识训练完成后，用原模型做 Teacher 进行 on-policy distill，会发现遗忘的能力又恢复了，而且刚学的知识也没有什么损失。似乎在模型内，知识和行为是存储在不同的参数中，而 On-policy Distill 刚好只影响那些行为参数。

## OPSD

看到小抄的学生自己充当老师
