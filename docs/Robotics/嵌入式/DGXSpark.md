# DGX Spark

[DGX Spark Quick Start Guide](https://www.nvidia.cn/content/dam/en-zz/Solutions/dgx-spark/DGX-Spark-Quick-Start-Guide.pdf)

## vLLM

[eelbaz/dgx-spark-vllm-setup: One-command vLLM installation for NVIDIA DGX Spark with Blackwell GB10 GPUs (sm_121 architecture)](https://github.com/eelbaz/dgx-spark-vllm-setup)

## SGlang

```shell title="Install uv"
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```shell title="Create environment"
uv venv .sglang --python 3.12
```

```shell title="Activate environment"
source .sglang/bin/activate
```

```shell title="Install Pytorch"
uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```

```shell title="Install flashinfer and triton"
uv pip install xgrammar triton flashinfer-python --prerelease=allow
```

```shell title="Clone sglang"
git clone --recursive https://github.com/sgl-project/sglang.git
cd sglang
uv pip install -e "python[cu130]" --prerelease=allow
```

```shell title="Export variables"
export TORCH_CUDA_ARCH_LIST=12.1a # Spark 12.1, 12.0f, 12.1a
export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

```shell title="Install sgl_kernel"
wget https://github.com/sgl-project/whl/releases/download/v0.3.16.post5/sgl_kernel-0.3.16.post5+cu130-cp310-abi3-manylinux2014_aarch64.whl#sha256=6624ea1afaff34010d8ff6096182f6ac9956c94d86b6d13f15ea962ae9995884
uv pip install sgl_kernel-0.3.16.post5+cu130-cp310-abi3-manylinux2014_aarch64.whl
```

```shell title="Clean memory"
sudo sysctl -w vm.drop_caches=3
```

```shell title="Install Python header"
sudo apt install python3-dev
```

```shell title="Run a model"
uv run python -m sglang.launch_server   --model-path google/gemma-3n-E4B-it --port 30000   --mem-fraction-static 0.8
```
