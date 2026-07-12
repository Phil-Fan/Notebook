# 07 | ViT 视觉 Transformer

## 核心思想

Transformer 在 NLP 扩展的很好，越大的模型就会产出越好的效果，一直上升
如何把 NLP 当中的技术用到 CV 当中来呢

- 直接用像素点的话，序列长度太长
- 控制窗口大小，控制长度；轴注意力

用标准 Transformer 来做，但是图片的序列长度太长，所以需要把图片分成 patch，然后做自注意力。

提出了一个新模型的任务，用在图像分类任务。

在 ViT 之上，

## 难点

## 相关工作

## 代码解析

## 对于 ViT 的改进

## 参考

- [深度学习 CV 之相知 VIT（附面试题）_vit 面试题-CSDN 博客](https://blog.csdn.net/2403_87956061/article/details/148696428)
- [速通 Vision Transformer (ViT) | 烈烈风中、的博客](https://achilles-10.github.io/posts/tech/vit/)
- [transformer、bert、ViT 常见面试题总结 - 简书](https://www.jianshu.com/p/55b4de3de410)
