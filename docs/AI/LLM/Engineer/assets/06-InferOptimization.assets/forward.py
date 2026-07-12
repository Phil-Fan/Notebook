import torch

NEG_INF = -1e10  # -infinity
EPSILON = 1e-10

Q_LEN = 6
K_LEN = 6
Q_BLOCK_SIZE = 2
KV_BLOCK_SIZE = 3
P_DROP = 0.2

Tr = Q_LEN // Q_BLOCK_SIZE
Tc = K_LEN // KV_BLOCK_SIZE

Q = torch.randn(1, 1, Q_LEN, 4, requires_grad=True).to(device="cpu")
K = torch.randn(1, 1, K_LEN, 4, requires_grad=True).to(device="cpu")
V = torch.randn(1, 1, K_LEN, 4, requires_grad=True).to(device="cpu")

# (1, 1, Q_LEN, 4)：
# - 1 → batch size（只有一个批次）
# - 1 → attention head 数（这里只有一个 head）
# - Q_LEN → 序列长度（Query 的 token 数）
# - 4 → embedding 维度（每个 token 表示成 4 维向量）
# requires_grad=True：让这些张量参与反向传播（梯度计算）。

O = torch.zeros_like(Q, requires_grad=True)
l = torch.zeros(Q.shape[:-1])[..., None]
# 初始化归一化因子 l（softmax 分母），初值全是 0。
m = torch.ones(Q.shape[:-1])[..., None] * NEG_INF
# 初始化每个位置的最大 logit（用于数值稳定的 softmax）

# step 4
Q_BLOCKS = torch.split(Q, Q_BLOCK_SIZE, dim=2)
K_BLOCKS = torch.split(K, KV_BLOCK_SIZE, dim=2)
V_BLOCKS = torch.split(V, KV_BLOCK_SIZE, dim=2)
# 作用：把 Q、K、V 在 序列维度（dim=2）上切分成若干个小块。
# Q_BLOCK_SIZE、KV_BLOCK_SIZE：每个小块的长度。
# 结果是一个元组（tuple），每个元素是一个子张量。


# step 5
O_BLOCKS = list(torch.split(O, Q_BLOCK_SIZE, dim=2))
l_BLOCKS = list(torch.split(l, Q_BLOCK_SIZE, dim=2))
m_BLOCKS = list(torch.split(m, Q_BLOCK_SIZE, dim=2))

print("Q shape:", Q.shape)
print("Q data:", Q)
print("\nK shape:", K.shape)
print("K data:", K)
print("\nV shape:", V.shape)
print("V data:", V)
print("\nO shape:", O.shape)
print("O data:", O)
print("\nl shape:", l.shape)
print("l data:", l)
print("\nm shape:", m.shape)
print("m data:", m)

print(len(l_BLOCKS), "\n\n")
print(m_BLOCKS)
# step 6
for j in range(Tc):
    # step 7
    Kj = K_BLOCKS[j]
    Vj = V_BLOCKS[j]
    # step 8
    for i in range(Tr):
        # step 9
        Qi = Q_BLOCKS[i]
        Oi = O_BLOCKS[i]
        li = l_BLOCKS[i]
        mi = m_BLOCKS[i]

        # step 10
        S_ij = torch.einsum("... i d, ... j d -> ... i j", Qi, Kj)

        # step 11
        mask = S_ij.ge(0.5)
        S_ij = torch.masked_fill(S_ij, mask, value=0)

        # step 12
        m_block_ij, _ = torch.max(S_ij, dim=-1, keepdims=True)
        # values, indices = torch.max(...) 最大值张量，最大值所在的索引
        # S_ij.shape = [B, H, I, J] ——》 m_block_ij.shape = [B, H, I, 1]

        P_ij = torch.exp(S_ij - m_block_ij)  # 这里有广播机制
        l_block_ij = torch.sum(P_ij, dim=-1, keepdims=True) + EPSILON
        P_ij_Vj = torch.einsum("... i j, ... j d -> ... i d", P_ij, Vj)

        # step 13
        mi_new = torch.maximum(m_block_ij, mi)

        li_new = torch.exp(mi - mi_new) * li + torch.exp(m_block_ij - mi_new) * l_block_ij

        # step 14
        m = torch.nn.Dropout(p=P_DROP)
        P_ij_Vj = m(P_ij_Vj)

        # Step 15
        O_BLOCKS[i] = (li / li_new) * torch.exp(mi - mi_new) * Oi + (
            torch.exp(m_block_ij - mi_new) / li_new
        ) * P_ij_Vj
        print(f"-----------Attention : Q{i}xK{j}---------")
        print(O_BLOCKS[i].shape)
        print(O_BLOCKS[0])
        print(O_BLOCKS[1])
        print("\n")

        # step 16
        l_BLOCKS[i] = li_new
        m_BLOCKS[i] = mi_new

        exit(0)

O = torch.cat(O_BLOCKS, dim=2)
l = torch.cat(l_BLOCKS, dim=2)
m = torch.cat(m_BLOCKS, dim=2)
