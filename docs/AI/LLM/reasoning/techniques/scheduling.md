# 架构调度加速

## Prefix Caching

!!! note "KV Cache 的跨请求复用"
    是prefill阶段的优化策略

## Chunked Prefill

把长 prompt 的 prefill 切成小块，和 decode 混在同一个 iteration 里，用 token 预算给单步计算量封顶。完整原理、成本模型与调参见 [分块预填充](chunked-prefill.md)。

### Continuous Batching

## PD 分离架构

## FastChat 负载均衡

## Acknowledgement

- [cr7258/ai-infra-learning: This repository organizes materials, recordings, and schedules related to AI-infra learning meetings.](https://github.com/cr7258/ai-infra-learning/tree/main)
