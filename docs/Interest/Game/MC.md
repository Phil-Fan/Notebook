# MineCraft

## 历史

## 玩法

## 合成表

## 游戏 mod

- Twlight Forest
-

## Linux 平台

### HCML

需要首先下载 java sdk

首先[下载 - Hello Minecraft! Launcher](https://hmcl.huangyuhui.net/download/)

使用 HCML 下载游戏版本和插件版本

```shell title="linux 下载"
git clone https://github.com/Minecraft4Pi/Minecraft1.12.2.git && sudo chmod +x ~/Minecraft1.12.2/executeme.sh
```

```shell
./executeme.sh
```

> [Full Minecraft for Jetson Nano - Jetson & Embedded Systems / Jetson Nano - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/full-minecraft-for-jetson-nano/80320/2)
> [How to setup Minecraft 1.12.2 on a Raspberry pi - Raspberry Pi Forums](https://forums.raspberrypi.com/viewtopic.php?t=219438)
> [Dragonboard 410c 上的 Minecraft 完整 PC 版 - 96Boards](https://www.96boards.org/blog/minecraft-dragonboard/)

可以指定 java 的路径

## use diffusion to make houses

[timothy-barnes-2357/Build-with-Bombs](https://github.com/timothy-barnes-2357/Build-with-Bombs)

Required packages and programs

CMake: <https://cmake.org/download/>
Java 21 JDK: <https://www.oracle.com/java/technologies/downloads/#jdk21-windows>
CUDA 12.6: <https://developer.nvidia.com/cuda-12-6-0-download-archive>
TensorRT 10.5: <https://developer.nvidia.com/tensorrt/download/10x>

```shell
make --version
```

```shell
java --version
```

```shell
nvcc --version
```

```shell
dpkg -l | grep nvinfer
```

[Get started with LWJGL 3 - LWJGL](https://www.lwjgl.org/guide#build-instructions)

```shell
ant -Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=7890 \
    -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=7890
```

```shell
export LWJGL_BUILD_ARCH=arm64
export LWJGL_BUILD_OUTPUT=/home/user/
```

### Related Resource

- [mcbench.ai](https://mcbench.ai)
- [Benchmarking Minecraft AI Agents: a Study on Memory, Planning, and Behavior](https://arxiv.org/abs/2406.08751)
- [Minecraft Agentic Agents](https://ojs.aaai.org/index.php/AAAI/article/view/28865)
- [Minecraft Agents](https://arxiv.org/abs/2208.04202)
