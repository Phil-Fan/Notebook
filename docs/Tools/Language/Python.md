# Python 相关配置

## pip

查看某个包所有的版本

```shell
pip index versions <package>
```

安装指定版本的包

```shell
pip install <package>==<version>
```

!!! note "windows 使用命令行调用不同版本的 python"

    在系统路径path（高级系统系统设置——环境变量）中加入python.exe所在目录（打开文件所在位置——属性——打开文件所在位置）（因为是快捷方式，所以需要先找到快捷方式所在目录，再找到原exe文件所在位置）

    **注：应考虑到优先级的问题，将想要通过命令行直接进入的 python 版本所对应的路径放在上面**

### pip 换源

```shell title="临时换源"
pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

```shell title="清华源 永久换源"
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

!!! bug "WARNING: The repository located at mirrors.aliyun.com is not a trusted or secure host and is being ignored. If this repository is available via HTTPS we recommend you use HTTPS instead, otherwise you may silence this warning and allow it anyway with '--trusted-host mirrors.aliyun.com'."
    在大多数情况下，这个警告表示pip无法验证镜像源的SSL证书。可能的原因包括：

    SSL证书问题： 镜像源的SSL证书过期、自签名或存在其他问题。
    网络问题： 在某些网络环境中（特别是公司网络或学校网络），中间人攻击(MITM)防御机制可能会导致证书验证失败。
    
    [已解决WARNING: The repository located at mirrors.aliyun.com is not a trusted or secure host异常的正确解决方法，亲测\_the repository located at mirrors, aliyun, com is -CSDN博客](https://blog.csdn.net/FMC_WBL/article/details/136143632)

### pip 导出环境

1. 导出结果含有路径
导出结果会存在路径，生成的 requirements.txt 文件在当前目录下。

```shell
pip freeze > requirements.txt
```

1. 导出不带路径的
生成的 requirements.txt 文件在当前目录下。

```shell
pip list --format=freeze > requirement.txt
```

生成 requirements.txt，pip freeze 会将当前 PC 环境下所有的安装包都进行生成，再进行安装的时候会全部安装很多没有的包。此方法要注意。

安装 requirements 文件的 pip 源的包

```shell
pip install -r requirements.txt
```

## uv

[安装 | uv 中文文档](https://uv.doczh.com/getting-started/installation/#shell)

[uv：新一代 Python 虚拟环境管理工具 - CC98 论坛](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/6240772)

[Python 包管理工具 uv 使用教程 - 知乎](https://zhuanlan.zhihu.com/p/1888904532131575259)

[【保姆级喂饭教程】uv 教程一文讲透：安装，创建，配置，工具，命令-CSDN 博客](https://blog.csdn.net/AlienProgrammer/article/details/149743804)

### uv 简介

uv 是一个用 Rust 编写的 Python 包安装器和解析器，旨在提供比 pip 更快的包安装体验。它完全兼容 pip，但提供了显著的性能改进。

主要特点：

1. **极快的安装速度**
   - 比 pip 快 10-100 倍
   - 并行下载和安装
   - 优化的依赖解析

2. **完全兼容性**
   - 支持所有 pip 命令
   - 兼容 requirements.txt
   - 支持 wheel 和 source 分发

3. **现代化特性**
   - 原生支持虚拟环境
   - 内置缓存系统
   - 更好的错误处理

### 安装 uv

```shell title="linux"
wget -qO- https://astral.sh/uv/install.sh | sh
```

```shell title="windows"
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```shell
pip install uv
```

```shell
uv pip install -r requirements.txt
```

### 目录设置

```shell title="配置 uv 缓存目录"
vi ~/.bashrc
export UV_CACHE_DIR=/data/cache
```

### 更换 python 版本

```shell
uv python install 3.11
uv venv --python 3.11
```

- 可以按照 `uv venv --python 3.12` 的形式直接指定虚拟环境需要的 Python 版本，避免依赖系统默认版本。

### 换源

```shell title="换源"
export UV_DEFAULT_INDEX="https://mirrors.aliyun.com/pypi/simple"
```

!!! note "网络环境"
    ```shell
    unset http_proxy && unset https_proxy
    ```

```shell title="换源，修改 pyproject.toml"
[[tool.uv.index]]
url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"
default = true
 
[tool.uv.pip]
index-url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"
```

### uv 使用

```shell
# 查看 uv 版本
uv --version
```

```shell
uv init
```

```shell
uv venv
```

```shell
uv add <package>
uv add <package>==<version>
```

```shell
source .venv/bin/activate
```

### 工作空间

可以使用子文件夹的方式

比如采用 `src-layout` 的结构

```shell
.
├── README.md
├── main.py
├── pyproject.toml
├── src/
│   ├── service_a/
│   │   ├── README.md
│   │   └── main.py
│   └── service_b/
│       ├── README.md
│       ├── main.py
│       └── pyproject.toml
└── uv.lock
```

首先在根目录下

```shell
uv init
```

然后切换到子文件夹

```shell
cd src/service_a
uv init service_a
```

然后在对应的文件夹添加依赖即可

- 共享依赖管理：工作区内的所有子项目共享同一个虚拟环境和锁文件（uv.lock），确保依赖一致性。
- 独立配置：每个子项目可定义自己的 pyproject.toml，但通过工作区根目录的配置统一协调。

如果要运行的时候，先添加根目录的依赖

```shell
uv sync
```

```shell
uv run xxxx.py
```

这个时候会自动安装需要的依赖

### uv pip 管理

和 pip 是一样的

```shell
# 下载库
uv pip install <package>

# 下载库并指定版本
uv pip install <package>==<version>

# 卸载
uv pip uninstall <package>

# 查看已安装的库
uv pip list
```

```shell title="生成 requirements.txt"
uv pip freeze > requirements.txt
```

### 从 conda 迁移

```shell title="导出依赖文件 requirements.txt"
conda list -e > requirements.txt
```

```shell title="使用 uv pip 管理依赖"
uv pip install -r requirements.txt
```

```shell title="使用 uv 项目作为管理"
uv add -r requirements.txt
```

## conda

### 下载与安装

清华镜像地址：`https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/`

按照你系统的架构选择合适的下载

```shell
uname -m
```

```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```

下载后执行得到的文件

```shell
bash Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```

一路点 enter 和 yes，最后重启终端，得到带有`(base)`的提示符，说明安装成功

[conda 使用指南](https://blog.csdn.net/miracleoa/article/details/106115730)

!!! note " conda 和 pip 的区别"
    [Anaconda | Understanding Conda and Pip](https://www.anaconda.com/blog/understanding-conda-and-pip)

    ||conda|pip|
    |---|---|---|
    |manages|binaries| wheel or source|
    |can require compilers| no| yes|
    |package types| any |Python-only|
    |create environment|yes, built-in|no, requires virtualenv or venv|
    |dependency checks| yes|no|
    |package sources|Anaconda repo and cloud|PyPI|

### conda 的环境变量配置

在安装目录下的`\Scripts`文件夹下

### Conda 换源

[conda 换地址](https://blog.csdn.net/chengjinpei/article/details/119835339)

```shell title="conda 换源"
conda config --add channels conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/
conda config --set show_channel_urls yes
```

### 使用

激活

```shell
source ~/anaconda3/bin/activate
```

```shell
# 切换盘符
cd /d d:

conda --version
conda -V #获取版本号

# 1. 创建虚拟环境
conda create -n your_env_name(虚拟环境名称) python==xx(想要创建的虚拟环境的python版本号)
 
# 在指定的位置创建虚拟环境
conda create -p /PATH/TO/path
conda env list # 查看所有的 conda 虚拟环境  
conda list # 检查安装
 
# 2. 激活虚拟环境
conda activate name
conda deactivate
conda env remove -n flowers
 
# 5. 安装包
conda install package_name(包名)
conda install scrapy==1.3 # 安装指定版本的包
conda install -n 环境名 包名 # 在 conda 指定的某个环境中安装包
 
# 6. 跳过安装失败的包，继续安装
# conda 方式
while read requirement; do conda install --yes $requirement; done < requirements.txt
 
# pip 方式
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt

# 7. 卸载包
conda remove -n <package_name> --all
```

### `conda`环境导出与导入

导出

```bash
conda list -e > requirements.txt
```

导入安装

```bash
conda install --yes --file requirements.txt
```

导出 yml 文件方式

```bash
conda env export > freeze.yml
```

安装

```bash
conda env create -f freeze.yml
```

```bash
conda env update -f a.yaml --prune
```

## python 调试方法

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=631692904&bvid=BV1Yb4y1k7oR&cid=368901845&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="80%" height=640px></iframe>

### print

### pdb

```python
import pdb
pdb.set_trace()
```

### ide 调试

在 ide 中点击调试按钮，选择 python 文件，点击运行，即可进入调试模式。

需要写`.json`文件，在文件中写入调试的配置，在 ide 中点击调试按钮，选择 python 文件，点击运行，即可进入调试模式。

可以安装`vpdb`库自动生成

## Pytorch

### CUDA

!!! note "什么是 CUDA"
    通俗地说，CUDA是一种协助“CPU任务分发+GPU并行处理”的编程模型/平台，用于加速GPU和CPU之间的计算。

    也就是说CUDA通过CPU任务分发和GPU并行处理的方式，把计算任务通过CPU分发给GPU进行并行计算加速。而GPU并行计算的能力需要CUDA借助其自带的编程接口和工具，比如C/C++语言来编写并行计算程序，并通过CUDA编译器将程序转化为可以在英NVIDIA GPU上执行的机器码快速运行。

#### CUDA 版本的兼容性

[CUDA 版本兼容性问题](https://www.cnblogs.com/geekbruce/articles/18577150)

CUDA 是向前和向后兼容的：这意味着，安装较新版本的 CUDA 驱动（例如 CUDA 12.3）时，较旧的 CUDA 版本（如 CUDA 12.1）依然可以正常运行。然而，安装一个支持更高 CUDA 版本（如 CUDA 12.4）的 PyTorch，可能会遇到兼容性问题，尤其是如果驱动版本与 CUDA 版本不完全匹配时。

关键点：

- 你的驱动是 CUDA 12.3。
- 如果你安装的是 PyTorch 支持 CUDA 12.1（例如，cu121），这是完全兼容的，因为驱动版本向后兼容旧的 CUDA 版本。
- CUDA 12.4 是在 CUDA 12.3 之后的版本，如果你的驱动是 12.3，理论上可能存在问题，因为 CUDA 12.4 可能需要更高的驱动版本（例如，支持 CUDA 12.4 的驱动），而你的驱动是 CUDA 12.3。

查看 cuda 支持版本，`win+R`输入`cmd`输入`nvidia-smi.exe`

下载地址[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Language__assets__Python.assets__20240829195225.webp)

点击符合的版本选择下载，直接安装。注意安装路径要装在自己记得住的地方下，要预留好空间，最好不要装在 C 盘。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Language__assets__Python.assets__20240829195549.webp)

**安装验证方法：**

1. cmd 中输入`nvcc -V`，有信息说明成功
2. 安装路径下`\extras\demo_suite\deviceQuery.exe`，运行这个文件，有`PASS`说明成功（查询一下本机的 gpu 设备
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Language__assets__Python.assets__20240829200019.webp)
3. 安装路径下`\extras\demo_suite\bandwidthTest.exe`，运行这个文件，有`PASS`说明成功
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Language__assets__Python.assets__20240829200006.webp)

[Installation Guide Windows :: CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/archive/11.6.0/cuda-installation-guide-microsoft-windows/index.html#system-requirements)

### cuDNN 安装

cuDNN 是 NVIDIA CUDA®深度神经网络库，用于 GPU 加速的深度神经网络。它提供了高度优化的实现，包括前向和反向卷积、池化层、归一化和激活层等标准例程

安装网站[cuDNN Archive | NVIDIA Developer](https://developer.nvidia.com/rdp/cudnn-archive)

找到符合自己上面 CUDA 安装版本的 cuDNN 版本，下载解压，将解压后的文件夹中的`bin`、`include`、`lib\x64`文件夹中的文件复制到 CUDA 的安装目录中对应的文件夹中。

注意这一步需要注册一下 NVIDIA 的账号

### Pytorch 安装

```shell title="查看 CUDA 版本"
nvidia-smi
```

```shell title="查看 CUDA 的版本"
nvcc -V
nvcc --version
```

装了 python3.9，我的 CUDA 版本是 10.2，在[Previous PyTorch Versions | PyTorch](https://pytorch.org/get-started/previous-versions/)这个网站上可以找到各个版本对应的下载链接

```shell title="CUDA=10.2"
pip install torch==1.10.1+cu102 torchvision==0.11.2+cu102 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu102/torch_stable.html
```

!!! failure "numpy 报错"
    安装好torch之后，numpy会报错

    ```
    UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at  ..\torch\csrc\utils\tensor_numpy.cpp:68.)
    _dtype_to_storage = {data_type(0).dtype: data_type for data_type in _storages}
    ```

    **解决方法：** 将 numpy 版本降低为非>2.0.0 的版本，之后就能成功导入了。
    ```shell
    pip uninstall numpy
    pip install numpy==1.26
    ```

```python title="测试是否可用"
import torch # 如果 pytorch 安装成功即可导入
print(torch.cuda.is_available()) # 查看 CUDA 是否可用
print(torch.cuda.device_count()) # 查看可用的 CUDA 数量
print(torch.version.cuda) # 查看 CUDA 的版本号
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Language__assets__Python.assets__20240903112501.webp)

## Pycharm

### 申请学生权限

语言设置为中文

setting-plugin-chinese

### 远程服务器连接与配置

```shell
ssh -p 15821 root@connect.westb.seetacloud.com
```

[pycharm 打开远程项目_手把手教你 Pycharm 远程连接服务器端项目进行本地开发调试！...-CSDN 博客](https://blog.csdn.net/weixin_34345947/article/details/114909727)

## 报错与问题解决

### 'GLIBCXX_3.4.30' not found

> 参考文章[「已解决」anaconda 环境 version \`GLIBCXX\_3.4.30‘not found](https://blog.csdn.net/CCCDeric/article/details/129292944)

```shell title="查找 libstdc++.so.6"
sudo find / -name libstdc++.so.6
```

这里可以找到哪些位置有 libstdc++.so.6

```shell title="查看 libstdc++.so.6 中的 GLIBCXX_3.4，这里是我的系统中的路径"
strings /usr/lib/aarch64-linux-gnu/libstdc++.so.6 | grep GLIBCXX_3.4
```

```shell title="查看 conda 环境中的 libstdc++.so.6 中的 GLIBCXX_3.4"
strings /home/user/miniconda3/envs/environment_name/lib/libstdc++.so.6 | grep GLIBCXX_3.4
```

可以发现，conda 环境中的 libstdc++.so.6 中的 GLIBCXX_3.4 是 3.4.21，没有 3.4.30，而系统中的 libstdc++.so.6 中的 GLIBCXX_3.4 是 3.4.30，所以需要将 conda 环境中的 libstdc++.so.6 替换为系统中的 libstdc++.so.6

```shell
cd /home/user/miniconda3/envs/environment_name/lib
```

```shell
rm -rf libstdc++.so
rm -rf libstdc++.so.6
```

```shell title="把系统中的 libstdc++.so.6.0.30 链接到 conda 环境中的 libstdc++.so.6"
ln -s /usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.30 libstdc++.so
ln -s /usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.30 libstdc++.so.6
```

### ImportError: No module named parse

!!! bug "ImportError: No module named parse"
    python版本问题，在python 2.x中

    ```python
    from urlparse import urlparse
    ```

    在python 3.x

    ```python
    from urllib.parse import urlparse
    ```
