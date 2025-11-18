---
comments: true
authors:
  - Phil-Fan
categories:
  - Meeting
tags:
  - meeting
date:
  created: 2025-11-08
nostatistics: true
---

# Note

1. 另一个推理框架 sglang 的分享
2. Aibrix 火山的开源端到端推理框架，主要在集群
3. Elastic EP 支持容错的一个设计，更灵活的扩缩容：mooncake 和 mooncake-pytorch 后端
4. dgx spark 打广告
5. Nvidia 的一个根据需求计算 PD 分离配置的工具 aiconfigurator（github 百星）
6. 在大规模分布式编译器／框架 triton-distributed

## Main Takeaway

1. 小规模的自己玩的系统确实不需要注意可观测，可观测是为了面向服务，更好上线
2.

## sglang 社区

### 一些新的 feature

- Hierachical KV Caching
  - backend support: mooncake, 3FS, NIXL
- Piecewise CUDA Graph and Torch Compile
- what is 推理 backend，常见的有哪些
- 通信源语有哪些 all reduce 是什么
- overlap scheduling with spec decoding

- milestone & roadmap
  - wanna to support more features zhengjiaode
  - turn these methods into a callable library so that everyone can use

Dynamo pd planner
Slang model gateway
Vllm semetic router

## AIbrix

AIbrix 火山引擎 性能与成本

优势

1. 面向生产环境，经过大规模线上环境检验：生产中部署大模型比较复杂：限流容错弹性
2. 开源、可扩展
3. 推理全栈

分布式/分离式：

- 为什么需要分离式的部署

并行方式：TP DP EP

model 的 -》资源的异质性 -〉

dense - sparse 分离

- KVCache 的架构
- 支持多种存储

大模型部署优化
K8s 控制面 + 数据面

搜广推按照流程而不是 model 拆分

分离方法：中心式；p2p

- 面向 pd 分离的请求路由
- Pd 请求的编排

Kvcache 的卸载 交给第三方的 management
远端 rdma 降低 ttft

- 不同的策略支持 plugin

### 成本问题

弹性伸缩：cpu 利用率
latency

传统指标是有局限性的

Qps 没有升高 latency / utils 都升高

特定伸缩的 metrics 2508.19559

Lora 微调的降本
长尾模型的支持，70 模型承担 30% 的流量 vllm 的模型恭喜爱过你

如何使用 serverless 的方式中

## aibrix

## elastic EP

多模型 serving

更灵活的扩缩容

支持部分 rank 偶发故障的 ep 并行方案
计算通信计算通信

card lost

qps=16

mooncake EP 故障感知的通讯库：动过点对点 GPU RDMA
mooncake pytorch 后端 具备容错的通信源语

部分 rank 失效的 EPLB 算法’

个人开发者在桌面的 AI 对于大模型开发的

- 大内存
- AI 软件
- 支持 cuda

RDMA
双机可以实现 FP4 405B

Ai Configurator

[Welcome to AIBrix — AIBrix](https://aibrix.readthedocs.io/latest/)

痛点 1: PD 是否更优
痛点 2: PD 如何配置

## 并行的方式

Triton-distributed

## vlm 优化

Vlm 数据缓存：多图重复场景，computer use agent；具身智能：T 时刻 1 张传感器+n 张低分辨率

结合具体场景

多模态数据序列化

zmq

pytorch 底层 安全角度

算子库选择很多

多模态模型 decode 次数很少 所以 ll 上的配置可能需要重新设置

## SGlang on hopper -96G

机内通信快 机间通信慢 算力的瓶颈

TP8 方式部署

SLO 要求

token 到达无序。Down gemm

EPLB：应该同时激活的 expert 放到两个机器上，开销会高很多，高概率激活的两个专家在一个卡上面激活 5%

专家 LB 有权重迁移 毛刺会影响服务

Async rebalance 缓解这个 问题

EP16 50% 走机内通信

flashMLA backend 艳吗机制
导致 topk 必须是 1

算力不高的卡 batchsize 比较小

如何做优化

SBO & TPO
