# 量化

推理侧把权重、激活或 KV Cache 压到更低比特，换显存和吞吐。训练对齐里的量化备忘见 [Quantization](../05-Quantization.md)。

## 这个目录记什么

- 权重量化：GPTQ、AWQ、SmoothQuant
- 激活与 KV Cache 量化
- FP8 / INT8 / INT4 在推理引擎里的接法
- 精度回退：哪些层保持更高精度

具体算法笔记后续补在本目录。
