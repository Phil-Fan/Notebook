# 强化学习 | Reinforcement Learning

## 基本概念

[强化学习 brian](https://www.bilibili.com/video/BV1o14y1a7FL)

find the best sequence of actions to maximize the reward

![image](https://img.philfan.cn/AI__RL__assets__RL-01.assets__20241107093547.webp)

![image](https://img.philfan.cn/AI__RL__assets__RL-01.assets__20241107095354.webp)

数学性较强；
系统性较强；

fancy trial & error

if we choose RL: we have to set up the controller structure

what success is (reward function)

we have to learn efficiently (RL algorithms)

model-free RL
model-based RL: provide knowledge about the environment

Hyperparameters:

- learning rate
- discount factor
- exploration vs exploitation

$$
E = <X,A,P,R>
$$

- $X$: state
- $A$: action
- $P$: transition probability
- $R$: reward function

- $V(x)$: state value function
- $Q(x,a)$: state-action value function
- $\pi(x,a)$: policy function

缺点

### 手动调整策略

环境变化时，需要重新调整策略

explainable AI

黑盒模型，不清楚哪里出错了

### robustness

how to verify:

with a learned policy, it's hard to predict how the system will behave from one state to another

RL 的测试次数是更多的

### verification is also difficult

### formal verification

稳定裕度这样的指标是不存在的；无法确定鲁棒性和安全性

### 方法

- set up learning  to b e more robust
- increase the safety
- solve a different problem

### Exploration & Exploitation

exploration: explore new areas in the environment

exploitation: collect the most reward you already know

tricky to balance exploration and exploitation

#### $\epsilon$-greedy 策略

即以$\epsilon$的概率进行探索，以$1-\epsilon$的概率进行利用；所以概率分布较宽的时候，$\epsilon$应该取大一些

递推求解即可，仅需记忆次数$n-1$以及平均奖赏$Q_{n-1}(k)$

$$
\begin{aligned}
Q(k) &= \frac{1}{n} \sum_{i=1}^{n} v_i \\
&= \frac{1}{n} ((n-1)Q(k) + v_n) \\
&= Q_{n-1}(k) + \frac{1}{n} (v_n - Q_{n-1}(k))
\end{aligned}
$$

#### Softmax 策略

基于 Boltzmann 分布，选择概率与奖赏成正比

$$
P(a) = \frac{e^{Q(a) /\tau}}{\sum_{i=1}^{k} e^{Q(i) / \tau}}
$$

$\tau$ 是温度参数，控制探索的强度；当$\tau \to 0$时，Softmax 退化为仅利用；当$\tau \to \infty$时，Softmax 退化为仅探索

### k 摇臂赌博机 | k-armed bandit

### Deploy & verify

![image](https://img.philfan.cn/AI__RL__assets__RL-01.assets__20241107112543.webp)

## Bellman Equation

![image](https://img.philfan.cn/AI__RL__assets__RL-01.assets__20241107112014.webp)

$$
Q(s, a) = r(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V(s')
$$

DDPG: 深度确定性策略梯度

- 连续的动作空间
- 估计确定性策略，训练更快

critic 是帮助 actor 进行训练的，actor 是决定策略选择的

## Policy

!!! note "state → action"

Q-function

- curse of dimensionality

设计一个高自由度的 funtion 很困难，所以需要一个函数逼近的方法，使用神经网络来逼近

得有一定复杂度，能够拟合大部分函数

policy gredient

- execute current policy
- collect reward
- increase probability of good action

### Policy-function

### Value-function

### Actor-Critic

## 有模型学习

Reward function:

- make a reward function is easy
- make a good reward function is hard

智能体很难随机生成得到稀疏奖励的动作序列

但是如果奖励函数有一个内置的倾向的话，学习过程可能会直接向这个倾向收敛

!!! bug "策略评估公式推导"

### bellman optimal equation | 贝尔曼最优方程 BOE

模型已知的情况下，强化学习任务可以归结为基于动态规划的求优问题

!!! note "bellman 与动态规划"

## 蒙特卡罗学习 | Monte Carlo Learning

## 时序差分学习 | Temporal Difference Learning

## Value Function Approximation

## Policy Gradient
