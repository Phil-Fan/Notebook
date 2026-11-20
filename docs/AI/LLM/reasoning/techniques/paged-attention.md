
## Paged Attention

### 为什么需要

!!! note "操作系统"
    操作系统需要给进程预先分配内存吗

    每个页4K
    
    ![image](https://img.philfan.cn/AI__LLM__Engineer__assets__06-InferOptimization.assets__image-20250813000031813.webp)

### Paged Attention 原理

- 不预分配，按需调用
  
- 按块 Block 分配内存，碎片更小
    ![image](https://img.philfan.cn/AI__LLM__Engineer__assets__06-InferOptimization.assets__image-20250813000142399.webp)

- 虚拟内存：逻辑内存是连续的，通过映射表链接到物理内存（实际分配不连续）；方便调用

![image](https://img.philfan.cn/AI__LLM__Engineer__assets__06-InferOptimization.assets__image-20250813000330631.webp)

## Share KV Cache

**copy on write**机制：引用大于 1 的时候，不能直接写入，必须拷贝一份，再写入

![image](https://img.philfan.cn/AI__LLM__Engineer__assets__06-InferOptimization.assets__image-20250813001125290.webp)

还可以优化 beam-search

![image](https://img.philfan.cn/AI__LLM__Engineer__assets__06-InferOptimization.assets__image-20250813001154648.webp)
