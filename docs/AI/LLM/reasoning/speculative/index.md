# 投机采样

用便宜的草稿先猜若干 token，再由大模型一次验证。猜对就能一次前进一步以上，接受规则保证分布仍与直接从目标模型采样等价。

| 笔记 | 内容 |
|------|------|
| [Speculative Decoding](speculative-decoding.md) | 草稿、验证、无损接受，以及 Medusa / EAGLE / MTP |
| [DFlash](dflash.md) | 用块扩散做投机解码 |
