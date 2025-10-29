# Thor


## 系统安装

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Jetson_Thor.assets__Jetson-ISO-KV_dark.webp)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Jetson_Thor.assets__jetson-iso_etcher-flash-start.gif)

[Quick Start Guide — Jetson AGX Thor Developer Kit - User Guide](https://docs.nvidia.com/jetson/agx-thor-devkit/user-guide/latest/quick_start.html#bsp-install-troubleshoot)

### 安装顺序


```shell
sudo apt update
sudo apt install nvidia-jetpack
```

```shell
echo "export PATH=/usr/local/cuda/bin:$PATH" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH" >> ~/.bashrc
source ~/.bashrc
```
## 使用

### Pytorch

```shell title="Install uv"
curl -LsSf https://astral.sh/uv/install.sh | sh
```
```shell title="Create environment"
uv venv .venv --python 3.12
```
```shell title="Activate environment"
source .venv/bin/activate
```
```shell title="Install Pytorch"
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```
### vllm

[vllm container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/vllm?version=25.09-py3)

```shell
sudo docker run --runtime=nvidia --gpus all -it --rm nvcr.io/nvidia/vllm:25.09-py3
```


[在Jetson上安装vLLM](https://www.mikeshi.me/posts/vllm-on-jetson/)

## Trouble Shooting


1. `nvidia-smi` 报错没有设备名称

```shell
sudo jetson_clocks
```
[Jetson thor: nvidia-smi show Nvidia thor off - Jetson & Embedded Systems / Jetson Thor - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/jetson-thor-nvidia-smi-show-nvidia-thor-off/344413/4)