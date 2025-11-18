# GANS

## 简介

Generative adversarial networks

Catch Me If You Can

## Acknowledgement

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=634089974&bvid=BV1rb4y187vD&cid=439574005&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height=450px></iframe>

[理解生成对抗网络 (GANs) - 知乎](https://zhuanlan.zhihu.com/p/97015788)

[一文看尽深度学习中的生成对抗（GAN）网络\_energy-basedgan-CSDN 博客](https://blog.csdn.net/qq_23981335/article/details/118332773)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__ADV__assets__03-GAN.assets__20240924092601.webp)

[图解 生成对抗网络 GAN 原理 超详解\_gan 原理图-CSDN 博客](https://blog.csdn.net/DFCED/article/details/105175097)

## 算法原理

### 损失函数

### 训练过程

## 评价

### 优点

### 缺点

## Variants

### Wasserstein GANs

Critics: the discriminator is called a critic,it tells how real the data is

### Conditional GANs | cGANs

### cycle GANs

replace the main object but keep the main features

### StyleGANs

seperate different style of the images

## Challenges

- Vanishing gradients: the generator gradients vanish, making it impossible to train the generator
- Mode collapse: the generator collapses to a single point in the data space(一张图片效果好就一直生成)
- Convergence

## 代码实战
