# Jetson Orin Nano

## 简介

NVIDIA Jetson Orin Nano 是 NVIDIA 推出的一款小型但功能强大的边缘 AI 和机器人计算设备。它是 Jetson 系列中最新的入门级产品，基于 NVIDIA 的 Ampere 架构。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__JetsonNano.assets__20250318091806079.webp)
> 图源 [NVIDIA Jetson Orin Nano 开发板](https://developer.nvidia.com/embedded/jetson-orin-nano-developer-kit)

主要特点：

- 计算性能：高达 40 TOPS 的 AI 性能
- CPU：6 核 Arm Cortex-A78AE
- GPU：NVIDIA Ampere 架构 GPU，具有 512 个 NVIDIA CUDA 核心
- 内存：8GB 64 位 LPDDR5
- 存储：支持 NVMe SSD
- 功耗：5W-15W，可配置

应用场景：

- 边缘 AI 计算
- 机器人控制
- 计算机视觉
- 自动驾驶
- 智能监控
- IoT 设备

Jetson Orin Nano 是 Jetson Nano 的升级版，算力提升了 80 倍，高达 40 TOPS（每秒万亿次）的计算性能，为曾经难以企及的复杂 AI 模型铺平了道路

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__JetsonNano.assets__20250318091411215.webp)

## 刷机与环境配置

官方教程：[🚀 初始设置指南 - Jetson Orin Nano](https://www.jetson-ai-lab.com/initial_setup_jon.html)

> 参考教程
> [Jetson 开发系列：Orin Nano 开箱！一款强大的嵌入式&物联网开发板\_jetson orin nano 算力-CSDN 博客](https://blog.csdn.net/u010522887/article/details/142677847)

### ssd 安装

M.2 80 尺寸的 ssd

### SDK Manager

[SDK Manager | NVIDIA 开发者](https://developer.nvidia.cn/sdk-manager)

遇到的问题：

- 烧录到中间一半，停止，failed
- 中间有几个包安装不上：

一些不算是经验的经验

- 保持耐心，不要急
- 不要提前连接显示器
- 可以给电脑和 nano 都连一下网线，可以的话给主机开一下梯子

[Jetson Zoo - eLinux.org](https://elinux.org/Jetson_Zoo)

### jtop

```shell title="jetpack jtop installment"
sudo apt update
sudo apt dist-upgrade
sudo reboot
sudo apt install nvidia-jetpack
```

安装 jtop，可以用来监控 jetson 的资源使用情况和查看 cuda 版本等。

```shell title="jtop usage"
sudo -H pip3 install -U pip
sudo -H pip install jetson-stats
```

```shell title="验证"
nvcc -V
```

### pytorch

根据官方的回答，jetpack 6.2 软件列表在[jp6/cu126 index](https://pypi.jetson-ai-lab.dev/jp6/cu126)

```shell title="安装 pytorch"
wget https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/6ef/f643c0a7acda9/torch-2.7.0-cp310-cp310-linux_aarch64.whl#sha256=6eff643c0a7acda92734cc798338f733ff35c7df1a4434576f5ff7c66fc97319
```

```shell title="安装 torchaudio"
wget https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/c59/026d500c57366/torchaudio-2.7.0-cp310-cp310-linux_aarch64.whl#sha256=c59026d500c573666ae0437c4202ac312ac8ebe38fa12dbb37250a07c1e826f9
```

```shell title="安装 torchvision"
wget https://pypi.jetson-ai-lab.dev/jp6/cu126/+f/daa/bff3a07259968/torchvision-0.22.0-cp310-cp310-linux_aarch64.whl#sha256=daabff3a0725996886b92e4b5dd143f5750ef4b181b5c7d01371a9185e8f0402
```

```shell title="安装"
pip install torch-2.7.0-cp310-cp310-linux_aarch64.whl
pip install torchaudio-2.7.0-cp310-cp310-linux_aarch64.whl
pip install torchvision-0.22.0-cp310-cp310-linux_aarch64.whl
```

!!! question "A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0"

    i fix this problem using the experience on [here](https://stackoverflow.com/questions/78641150/a-module-that-was-compiled-using-numpy-1-x-cannot-be-run-in-numpy-2-0-0)

    ```shell
    pip uninstall numpy
    pip install numpy==1.26.4
    ```
