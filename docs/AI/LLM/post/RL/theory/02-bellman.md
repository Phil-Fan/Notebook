# 02 | Bellman Equation

![image](https://img.philfan.cn/AI__RL__assets__RL-01.assets__20241107112014.webp)

$$
Q(s, a) = r(s, a) + \gamma \sum_{s' \in S} P(s' | s, a) V(s')
$$

DDPG: 深度确定性策略梯度

- 连续的动作空间
- 估计确定性策略，训练更快

critic 是帮助 actor 进行训练的，actor 是决定策略选择的
