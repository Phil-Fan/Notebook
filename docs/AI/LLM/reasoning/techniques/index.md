# 推理加速常用技术

跨引擎都会用到的推理加速手段：缓存、注意力实现，以及请求如何被切分和调度。引擎怎么落地见 [推理加速引擎](../engines/index.md)；用草稿多猜 token 见 [投机采样](../speculative/index.md)。

| 笔记 | 内容 |
|------|------|
| [推理优化](infer-optimization.md) | Prefill / Decode、KV Cache、PagedAttention、FlashAttention、StreamLLM |
| [架构调度](scheduling.md) | Prefix Caching、Chunked Prefill、Continuous Batching、PD 分离 |
