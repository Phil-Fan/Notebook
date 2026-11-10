# Iteration

## Exploration & Exploitation

exploration: explore new areas in the environment

exploitation: collect the most reward you already know

tricky to balance exploration and exploitation

### $\epsilon$-greedy 策略

即以$\epsilon$的概率进行探索，以$1-\epsilon$的概率进行利用；所以概率分布较宽的时候，$\epsilon$应该取大一些

递推求解即可，仅需记忆次数$n-1$以及平均奖赏$Q_{n-1}(k)$

$$
\begin{aligned}
Q(k) &= \frac{1}{n} \sum_{i=1}^{n} v_i \\
&= \frac{1}{n} ((n-1)Q(k) + v_n) \\
&= Q_{n-1}(k) + \frac{1}{n} (v_n - Q_{n-1}(k))
\end{aligned}
$$

### Softmax 策略

基于 Boltzmann 分布，选择概率与奖赏成正比

$$
P(a) = \frac{e^{Q(a) /\tau}}{\sum_{i=1}^{k} e^{Q(i) / \tau}}
$$

$\tau$ 是温度参数，控制探索的强度；当$\tau \to 0$时，Softmax 退化为仅利用；当$\tau \to \infty$时，Softmax 退化为仅探索
