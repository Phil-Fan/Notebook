# 推理加速常用技术

跨引擎都会用到的推理加速手段：缓存、注意力实现，以及请求如何被切分和调度。引擎怎么落地见 [推理加速引擎](../engines/index.md)；用草稿多猜 token 见 [投机采样](../speculative/index.md)。

| 笔记 | 内容 |
|------|------|
| [KV Cache](kv-cache.md) | KV Cache 的原理、显存占用与动态性 |
| [Paged Attention](paged-attention.md) | 分页 KV Cache：碎片、共享与按块写入 |
| [Flash Attention](flash-attention.md) | IO-aware 的精确注意力实现 |
| [架构调度](scheduling.md) | Prefix Caching、Continuous Batching、PD 分离 |
| [分块预填充](chunked-prefill.md) | Chunked Prefill：为什么切、怎么切、切多大、和谁配合 |
