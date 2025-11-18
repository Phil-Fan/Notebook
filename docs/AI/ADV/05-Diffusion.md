# Diffusion Model

- [ ] 梳理论文表格
- [ ] 梳理证明过程

<div class="card file-block" markdown="1">
<div class="file-icon"><img src="/style/images/pdf.svg" style="height: 3em;" alt="pdf"></div>
<div class="file-body">
<div class="file-title"> Diffusion 课堂展示 ppt</div>
<div class="file-meta"> 1.9MB / Version: 22 Apr, 2025</div>
</div>
<a class="down-button" target="_blank" href="https://philfan-pic.oss-cn-beijing.aliyuncs.com/pdf/05-DiffusionModelSlides.pdf" markdown="1">:fontawesome-solid-download: 下载</a>
</div>

## Background

当下很多图片需要去码去噪，还原本身的图像性质。或者当下 AI 绘画很火热，许多算法通过输入文字描述，最终便可以得到一张生成图像。

## 与几种生成式模型的区别

## 正向加噪

## 反向去噪

1) 每个时间步通过 $x_{t}$ 和 $t$ 来预测高斯噪声 $z_{\theta}(x_{t},t)$，随后根据 (9) 得到均值 $\mu_{\theta}(x_{t},t)$。

2) 得到方差 $\Sigma_{\theta}(x_{t},t)$，DDPM 中使用 untrained $\Sigma_{\theta}(x_{t},t) = \widetilde{\beta}_{t}$，且认为 $\widetilde{\beta}_{t} = \beta_{t}$ 和 $\widetilde{\beta}_{t} = \frac{1-\overline{\alpha}_{t-1}}{1-\overline{\alpha}_{t}} \cdot \beta_{t}$ 结果近似，在 GLIDE 中则是根据网络预测 trainable 方差 $\Sigma_{\theta}(x_{t},t)$。

3) 根据 (5-2) 得到 $q(x_{t-1}|x_{t})$，利用重参数得到 $x_{t-1}$。

## 总结

ForwardProcess:

$$
q(x_{t}|x_{t-1})=N(x_{t};\sqrt{a_{t}}x_{t-1},(1-a_{t})I)
$$

ReverseProcess:

$$
p(x_{t-1}|x_{t})=N(x_{t-1};\frac{1}{\sqrt{a_{t}}}(x_{t}-\frac{1-a_{t}}{\sqrt{1-\bar{a}_{t}}} \bar{z}(x_{t},t)),\frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_{t}}\beta_{t}I)
$$

## 训练模型预测噪声

$$
\begin{aligned}
L_\text{VLB}
&= \mathbb{E}_{q(\mathbf{x}_{0:T})} \Big[ \log\frac{q(\mathbf{x}_{1:T}\vert\mathbf{x}_0)}{p_\theta(\mathbf{x}_{0:T})} \Big] \\
&= \mathbb{E}_q \Big[ \log\frac{\prod_{t=1}^T q(\mathbf{x}_t\vert\mathbf{x}_{t-1})}{ p_\theta(\mathbf{x}_T) \prod_{t=1}^T p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t) } \Big] \\
&= \mathbb{E}_q \Big[ -\log p_\theta(\mathbf{x}_T) + \sum_{t=1}^T \log \frac{q(\mathbf{x}_t\vert\mathbf{x}_{t-1})}{p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t)} \Big] \\
&= \mathbb{E}_q \Big[ -\log p_\theta(\mathbf{x}_T) + \sum_{t=2}^T \log \frac{q(\mathbf{x}_t\vert\mathbf{x}_{t-1})}{p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t)} + \log\frac{q(\mathbf{x}_1 \vert \mathbf{x}_0)}{p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1)} \Big] \\
&= \mathbb{E}_q \Big[ -\log p_\theta(\mathbf{x}_T) + \sum_{t=2}^T \log \Big( \frac{q(\mathbf{x}_{t-1} \vert \mathbf{x}_t, \mathbf{x}_0)}{p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t)}\cdot \frac{q(\mathbf{x}_t \vert \mathbf{x}_0)}{q(\mathbf{x}_{t-1}\vert\mathbf{x}_0)} \Big) + \log \frac{q(\mathbf{x}_1 \vert \mathbf{x}_0)}{p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1)} \Big] \\
&= \mathbb{E}_q \Big[ -\log p_\theta(\mathbf{x}_T) + \sum_{t=2}^T \log \frac{q(\mathbf{x}_{t-1} \vert \mathbf{x}_t, \mathbf{x}_0)}{p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t)} + \sum_{t=2}^T \log \frac{q(\mathbf{x}_t \vert \mathbf{x}_0)}{q(\mathbf{x}_{t-1} \vert \mathbf{x}_0)} + \log\frac{q(\mathbf{x}_1 \vert \mathbf{x}_0)}{p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1)} \Big] \\
&= \mathbb{E}_q \Big[ -\log p_\theta(\mathbf{x}_T) + \sum_{t=2}^T \log \frac{q(\mathbf{x}_{t-1} \vert \mathbf{x}_t, \mathbf{x}_0)}{p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t)} + \log\frac{q(\mathbf{x}_T \vert \mathbf{x}_0)}{q(\mathbf{x}_1 \vert \mathbf{x}_0)} + \log \frac{q(\mathbf{x}_1 \vert \mathbf{x}_0)}{p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1)} \Big]\\
&= \mathbb{E}_q \Big[ \log\frac{q(\mathbf{x}_T \vert \mathbf{x}_0)}{p_\theta(\mathbf{x}_T)} + \sum_{t=2}^T \log \frac{q(\mathbf{x}_{t-1} \vert \mathbf{x}_t, \mathbf{x}_0)}{p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t)} - \log p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1) \Big] \\
&= \mathbb{E}_q [\underbrace{D_\text{KL}(q(\mathbf{x}_T \vert \mathbf{x}_0) \parallel p_\theta(\mathbf{x}_T))}_{L_T} + \sum_{t=2}^T \underbrace{D_\text{KL}(q(\mathbf{x}_{t-1} \vert \mathbf{x}_t, \mathbf{x}_0) \parallel p_\theta(\mathbf{x}_{t-1} \vert\mathbf{x}_t))}_{L_{t-1}} \underbrace{- \log p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1)}_{L_0} ]
\end{aligned}
$$

把上限 VLB 拆成三部分

$$
\begin{aligned}
L_\text{VLB} &= L_T + L_{T-1} + \dots + L_0 \\
\text{where } L_T &= D_\text{KL}(q(\mathbf{x}_T \vert \mathbf{x}_0) \parallel p_\theta(\mathbf{x}_T)) \\
L_t &= D_\text{KL}(q(\mathbf{x}_t \vert \mathbf{x}_{t+1}, \mathbf{x}_0) \parallel p_\theta(\mathbf{x}_t \vert\mathbf{x}_{t+1})) \text{ for }1 \leq t \leq T-1 \\
L_0 &= - \log p_\theta(\mathbf{x}_0 \vert \mathbf{x}_1)
\end{aligned}
$$

我们的目的：

训练一个模型

$$
p_\theta(\mathbf{x}_{t-1} \vert \mathbf{x}_t) = \mathcal{N}(\mathbf{x}_{t-1}; \boldsymbol{\mu}_\theta(\mathbf{x}_t, t), \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t))
$$

让$\mu_\theta$ 估计

$$
\tilde{\boldsymbol{\mu}}_t = \frac{1}{\sqrt{\alpha_t}} \Big( \mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}} \boldsymbol{\epsilon}_t \Big)
$$

在

$$
\begin{aligned}
\boldsymbol{\mu}_\theta(\mathbf{x}_t, t) &= \color{red}{\frac{1}{\sqrt{\alpha_t}} \Big( \mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}} \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t) \Big)} \\
\text{Thus }\mathbf{x}_{t-1} &= \mathcal{N}(\mathbf{x}_{t-1}; \frac{1}{\sqrt{\alpha_t}} \Big( \mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}} \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t) \Big), \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t))
\end{aligned}
$$

已知求两个高斯分布 KL 散度的公式

$$
L_t=\mathbb{E}_q\left[\frac{1}{2||\Sigma_\theta(x_t,t)||_2^2}||\tilde{\mu}_t(x_t,x_0)-\mu_\theta(x_t,t)||^2\right]+C
$$

$$
\begin{aligned}
L_t
&= \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}} \Big[\frac{1}{2 \| \boldsymbol{\Sigma}_\theta(\mathbf{x}_t, t) \|^2_2} \| \color{blue}{\tilde{\boldsymbol{\mu}}_t(\mathbf{x}_t, \mathbf{x}_0)} - \color{green}{\boldsymbol{\mu}_\theta(\mathbf{x}_t, t)} \|^2 \Big] \\
&= \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}} \Big[\frac{1}{2  \|\boldsymbol{\Sigma}_\theta \|^2_2} \| \color{blue}{\frac{1}{\sqrt{\alpha_t}} \Big( \mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}} \boldsymbol{\epsilon}_t \Big)} - \color{green}{\frac{1}{\sqrt{\alpha_t}} \Big( \mathbf{x}_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}} \boldsymbol{\boldsymbol{\epsilon}}_\theta(\mathbf{x}_t, t) \Big)} \|^2 \Big] \\
&= \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}} \Big[\frac{ (1 - \alpha_t)^2 }{2 \alpha_t (1 - \bar{\alpha}_t) \| \boldsymbol{\Sigma}_\theta \|^2_2} \|\boldsymbol{\epsilon}_t - \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\|^2 \Big] \\
&= \mathbb{E}_{\mathbf{x}_0, \boldsymbol{\epsilon}} \Big[\frac{ (1 - \alpha_t)^2 }{2 \alpha_t (1 - \bar{\alpha}_t) \| \boldsymbol{\Sigma}_\theta \|^2_2} \|\boldsymbol{\epsilon}_t - \boldsymbol{\epsilon}_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0 + \sqrt{1 - \bar{\alpha}_t}\boldsymbol{\epsilon}_t, t)\|^2 \Big]
\end{aligned}
$$

**推导依据**：

1. **贝叶斯定理**：

    $$
    q(x_{t-1} | x_t, x_0) = \frac{q(x_t | x_{t-1}, x_0) \cdot q(x_{t-1} | x_0)}{q(x_t | x_0)}
    $$

2. **前向过程的马尔可夫性**：

    $$
    q(x_t | x_{t-1}, x_0) = q(x_t | x_{t-1})
    $$

### UNet 介绍

UNet 是一种常用于图像分割任务的卷积神经网络架构，在扩散模型中也被广泛使用。它的主要特点是：

1. U 型对称结构
   - 由编码器 (下采样路径) 和解码器 (上采样路径) 组成
   - 形状像字母"U"，因此得名 UNet

2. 编码器部分
   - 通过卷积和池化逐步降低特征图的空间维度
   - 提取图像的高级语义特征
   - 每一层的通道数通常翻倍

3. 解码器部分  
   - 通过上采样和卷积逐步恢复特征图的空间维度
   - 还原细节信息
   - 每一层的通道数通常减半

4. Skip Connection
   - 编码器和解码器之间有跳跃连接
   - 将编码器的特征直接连接到解码器对应层
   - 帮助保留细节信息，缓解梯度消失

5. 在扩散模型中的应用
   - 输入为噪声图像
   - 预测每一步的噪声
   - 通过时间嵌入来调节不同时间步的去噪过程

UNet 的这种结构设计使其能够很好地处理图像生成任务，既能捕获全局语义信息，又能保留局部细节特征。这也是它被广泛应用于扩散模型的重要原因。

### 代码实现

```bash
pip install denoising_diffusion_pytorch
```

[zoubohao/DenoisingDiffusionProbabilityModel-ddpm](https://github.com/zoubohao/DenoisingDiffusionProbabilityModel-ddpm-):This may be the simplest implement of DDPM. You can directly run Main.py to train the UNet on CIFAR-10 dataset and see the amazing process of denoising.

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=469014590&bvid=BV1b541197HX&cid=721211471&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height="450" width="600"></iframe>

## 参考资料

### Thesis

- Denoising Diffusion Probabilistic Models
- Denoising Diffusion Implicit Models
- Improved Denoising Diffusion Probabilistic Models
- Diffusion Models Beat GANs on Image Synthesis
- Classifier-Free Diffusion Guidance
- GLIDE: Towards Photorealistic Image Generation and Editing withText-Guided Diffusion Models
- Hierarchical Text-Conditional Image Generation with CLIP Latents
- Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

### Video

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112707088943539&bvid=BV1xih7ecEMb&cid=500001601124266&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height="450" width="600"></iframe>

李宏毅老师视频
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112789431519714&bvid=BV1mLbQeRExa&cid=500001616001261&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height="450" width="600"></iframe>

### Blog

[What are Diffusion Models? | Lil'Log](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/#forward-diffusion-process)

[由浅入深了解 Diffusion Model - 知乎](https://zhuanlan.zhihu.com/p/525106459)

## Application - txt2img

- stable diffusion
- DALL·E

### Stable Diffusion

基于 LDM

<iframe src="https://arxiv.org/pdf/2112.10752" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>

**Latent Space**

- 潜在扩散模型”（Latent Diffusion Model）。顾名思义，Stable Diffusion 发生在潜在空间中。这就是它比纯扩散模型更快的原因。

VAE 由编码器​和解码器​两部分组成：编码器​负责将输入从一个空间映射到另一个空间，称为潜在空间（Latent Space），而解码器则负责将（Latent Space）变量转换回原来的空间。通常潜在空间都是一个相较于原空间更加低维的空间，这样可以起到数据压缩的作用。

Diffusion Model 本身在生成图片上已经能够取得很好的效果了，但是由于它无论是训练还是推导都需要大量的算力，无法生成高质量的的图像。因此 VAE 将图片压缩到潜在空间的操作对 SD 的成功是功不可没，正是由于 VAE 将复杂的像素空间压缩到了低维的潜在空间，大大降低了训练和生成的计算成本。

**Latent Diffusion**

正向扩散过程 → 向潜在数据添加噪声。
逆向扩散过程 → 从潜在数据中去除噪声

**调节机制**

- 对于文本输入，首先使用语言模型 $\tau_{\theta}$（例如 BERT、CLIP）将文本转换为嵌入（向量），然后通过（多头）注意力 $Attention(Q, K, V)$ 映射到 U-Net 层。
- 对于其他空间对齐的输入（例如语义映射、图像、修复），可以使用连接来完成调节。

text - tokenizier - embedding-  text transformer - noise predictor

#### 步骤

[How does Stable Diffusion work?](https://stable-diffusion-art.com/how-stable-diffusion-work/)

#### 部署 Stable Diffusion

[【保姆级教程】Linux 上部署 Stable Diffusion WebUI 和 LoRA 训练，拥有你的专属图片生成模型\_stable diffusion linux-CSDN 博客](https://blog.csdn.net/u010522887/article/details/138425635)

#### 使用 Stable Diffusion

- [Midjourney](https://www.midjourney.com/home)

- [Stable Diffusion Public Release — Stability AI](https://stability.ai/news/stable-diffusion-public-release)

### DALL·E

- [DALL·E](https://labs.openai.com/) - 2021
- [DALL·E 3 | OpenAI](https://openai.com/index/dall-e-3/) - 2024

论文 Hierarchical Text-Conditional
Image Generation with CLIP Latents

<iframe src="https://arxiv.org/pdf/2204.06125" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>

#### OpenAI API 实战

[Overview - OpenAI API](https://platform.openai.com/docs/overview)

## Application - LLaDA

Site:[Large Language Diffusion Models](https://ml-gsai.github.io/LLaDA-demo/)

GitHub:[ML-GSAI/LLaDA: Official PyTorch implementation for "Large Language Diffusion Models"](https://github.com/ML-GSAI/LLaDA)

[【论文解读】LLaDA：用扩散模型改变 LLM 的「自回归」范式 - 知乎](https://zhuanlan.zhihu.com/p/24738741479)

### 自回归模型

一种生成模型，通过预测序列中的下一个元素来生成整个序列。例如，给定 "The weather is"，自回归模型会预测下一个词是 "nice"，然后继续预测下一个词，直到生成完整的句子

### 方案

主要方案

Masked Diffusion Model (MDM)：LLaDA 的核心是 MDM，它通过随机 masking tokens 并训练模型预测被 mask 的 tokens 来学习语言表示。
前向过程：逐步 mask 序列中的 tokens，直到所有 tokens 都被 mask。
反向过程：通过 mask predictor 迭代预测被 mask 的 tokens，从而恢复原始序列。

主要技术：
Transformer：LLaDA 使用 Transformer 作为 mask predictor，但没有使用因果 mask，允许模型看到完整的输入序列。
Pre-training + SFT：LLaDA 采用预训练（Pre-training）和监督微调（Supervised Fine-Tuning, SFT）的标准流程。
可变的 Masking 比例：LLaDA 使用在 0 和 1 之间随机变化的 masking 比例，而 BERT 等模型使用固定的比例。

LLaDA 的核心思想是利用扩散模型进行语言建模。与传统的自回归模型不同，LLaDA 采用以下方式生成文本：

前向扩散过程：将原始文本逐步 mask，直到所有 tokens 都被 mask，变成一段随机噪声。
反向去噪过程：训练一个 mask predictor 来预测被 mask 的 tokens，逐步恢复原始文本。
这种方式与自回归模型的逐个 token 预测有本质的区别。自回归模型是顺序生成，而 LLaDA 是并行生成。此外，LLaDA 可以同时考虑上下文信息，而自回归模型通常只能利用单向的上下文信息。

Q3：论文中提到的「reversal curse」是什么意思？为什么 LLaDA 能够更好地解决这个问题？
Reversal curse（逆向诅咒）是指 LLM 在学习了 A is B 之后，却无法自然地推出 B is A。例如，模型学习了「巴黎是法国的首都」，却无法回答「法国的首都是哪里？」这个问题。

自回归模型之所以会出现 reversal curse，是因为它们是单向建模的，只能学习到 A -> B 的条件概率，而无法学习到 B -> A 的条件概率。

LLaDA 能够更好地解决 reversal curse，是因为它是双向建模的。在训练过程中，LLaDA 需要预测被 mask 的 tokens，这使得模型能够同时学习到 A -> B 和 B -> A 的关系。此外，LLaDA 没有使用因果 mask，允许模型看到完整的上下文信息，从而更好地理解 tokens 之间的双向依赖关系。

### pros & cons

对后续研究的启发和影响：
证明了扩散模型在 LLMs 上的可行性，为未来的研究开辟了新的方向。
提出了 LLaDA，一个具有竞争力的非自回归 LLM，为非自回归模型的探索提供了实践经验。
强调了生成建模原则在 LLMs 中的重要性，挑战了自回归模型是 LLM 唯一可行架构的观点。

计算资源限制：由于计算资源的限制，LLaDA 与自回归模型的直接比较（例如，在相同的数据集上训练）仅限于小于 10^23 FLOPs 的计算预算。
模型架构：没有为 LLaDA 设计专门的注意力机制或位置嵌入，也没有应用任何系统级的架构优化。
推理：对指导机制的探索仍处于初步阶段，LLaDA 目前对推理超参数敏感。
对齐：LLaDA 尚未经过强化学习的对齐，这对于提高其性能和与人类意图的对齐至关重要。

## Application - Robotics - Diffusion Policy

### 简介

- Site:[Diffusion Policy](https://diffusion-policy.cs.columbia.edu/)
- GitHub:[ML-GSAI/DiffusionPolicy: Official PyTorch implementation for "Diffusion Policy"](https://github.com/ML-GSAI/DiffusionPolicy)
论文：

<iframe src="https://arxiv.org/pdf/2303.04137v4" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112966850576938&bvid=BV1ZaeAe7EMu&cid=500001651025308&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" height="450" width="600"></iframe>

### Why Diffusion Policy

- 另一个解决的是**Action Space Scalability**的问题。与 Diffuser 类似，模型在进行策略预测时会生成多步的动作而不是仅关注眼前的一两步，使得动作更加具有连贯性（在时间上具有一致性）。作者指出，现在的动作预测主要有两种思路：一种是在连续空间中预测（类似回归任务），一种是将动作空间分成若干区间，进行离散预测（类似分类任务）。在进行 Multi-Modal Action Prediction 的任务时，人们倾向于将采用离散预测的方式。例如，继续沿用上述开车的例子，我们可以把方向盘的运动角度均匀划分为 100 个区间，这样就将连续的角度预测转换为一个 100 分类的问题。可以预见的是，这种方法会随着预测步数的增多维度会呈指数级增长，另外，在实际应用中，预测一个六自由度的机械臂的一步动作就已经有很高的维度了，因此，这种离散预测的方法无法胜任复杂的控制。Diffusion Policy 追求的是不仅可以预测每一步，而且可以在高维连续控制中实现。对于我们来说，我们可以直接预测未来每一步，无论是接下来的 20 步还是 100 步，是向左还是向右，而不是在每一步预测之后再执行，再决定下一步该怎么走。
- 最后是**Training Stability**的问题，作者指出 Diffusion 方法的强大之处在于，它的性能不逊色于 GAN，但其训练过程非常稳定。基本上，你可以随便调整参数，生成器就能够输出结果，可能效果不是最优的，但基本上都能 work。

### 公式详解

[Diffusion Policy 论文精读：从 Diffusion 到 Policy – Devon's Blog](https://devon018.github.io/Diffusion_Policy/)

### 本地训练步骤

1. **安装 Anaconda**

   网上有很多教程，这里不再赘述。最好在租用服务器时直接选择 Anaconda 环境，这样会方便很多。

2. **在 Anaconda 下安装 Mamba（Mamba 运行效率显著提升）**

   ```bash title="安装 Mamba"
   conda install mamba -n base -c conda-forge
   ```

3. **按照代码中的 README 文件一步一步配置**

   - **安装依赖**

     ```bash title="安装依赖"
     sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
     ```

   - **创建环境，环境名称为 robodiff**（这一步用时较长，需要耐心等待）

     ```bash title="创建 robodiff 环境"
     mamba env create -f conda_environment.yaml
     ```

   - **在主文件夹下，创建 data 文件夹**

     ```bash title="创建 data 文件夹"
     mkdir data && cd data
     ```

   - **在 data 文件夹里下载数据集**

     ```bash title="下载数据集"
     wget https://diffusion-policy.cs.columbia.edu/data/training/pusht.zip
     ```

   - **解压数据集并删除压缩包**

     ```bash title="解压数据集"
     unzip pusht.zip && rm -f pusht.zip
     ```

   - **下载实验相关参数的文件**

     ```bash title="下载实验参数文件"
     wget -O image_pusht_diffusion_policy_cnn.yaml https://diffusion-policy.cs.columbia.edu/data/experiments/image/pusht/diffusion_policy_cnn/config.yaml
     ```

4. **跑一个实例**

   - **进入环境**

     ```bash title="激活环境"
     conda activate robodiff
     ```

   - **下载 wandb**

     ```bash title="安装 wandb"
     pip install wandb
     ```

   - **在 wandb 中创建一个账号，并将 API_Key 复制下来，在命令行中输入指令登录 wandb**

     ```bash title="登录 wandb"
     wandb login
     ```

     回车后，将 API_Key 复制到指定位置，回车，登录。之后的训练数据就会显示在 wandb 中了。wandb 网址如下：Weights & Biases。在 wandb 中，home 中可以找到 API Key。

   - **训练**

     ```bash title="训练指令"
     python train.py --config-dir=. --config-name=image_pusht_diffusion_policy_cnn.yaml training.seed=42 training.device=cuda:0 hydra.run.dir='data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}'
     ```

以上就是关于 diffusion policy 的代码复现全部过程，详细文章及代码请看：[https://diffusion-policy.cs.columbia.edu](https://diffusion-policy.cs.columbia.edu)
