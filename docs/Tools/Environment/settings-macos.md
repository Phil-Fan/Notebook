# :fontawesome-brands-apple: MacOS

## 快捷键

同时重命名多个文件

- 拆字法打字

### System

- ++space++ 预览文件
- ++command+space++ 打开聚焦
- ++ctrl+arrow-up++ mission control
- ++command+control+q++ 锁屏

### Folder

- ++command+bracket-left++ 返回上一级
- ++command+bracket-right++ 前往下一级

### Apps

- ++command+q++ 退出应用程序

把鼠标移动到 另一个显示器屏幕底部，然后继续往下推一点（类似“顶到屏幕边缘”再往下挤的动作）。

几秒钟后，Dock 就会跳到你鼠标所在的那个显示器。

### Typing

- ++fn+backspace++ 在 mac 中等于 ++del++
- ++command+control+space++  emoji
- ++shift+option+b++ 颜文字
- ++tab++ 使用声调打字

## 系统设置

- 三指拖移：设置 - 辅助功能 - 指针控制 - 触控板选项 - 拖移样式
- 触控板轻点：设置 - 触控板 - 轻点来点按

```shell title="open Finder in terminal"
open .
```

## 开发配置

### 软件已损坏？怎么解决

```shell title="信任开发者"
sudo spctl --master-disable
```

```shell title="放行 picgo"
xattr -cr /Applications/xxx.app
```

### 科学上网

下载[clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)，安装后配置好代理，然后就可以开始安装 homebrew 了

### homebrew

首先需要配置好 vpn

```shell title="安装 homebrew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```shell title="系统会跳出三个指令让你执行，类似于"
echo >> /Users/philfan/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/philfan/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

```shell title="验证安装"
brew help
```

```shell title="wget 安装"
brew install wget
```

### python

```shell title="安装 uv"
brew install uv
```

```shell title="验证安装"
uv --version
```

```shell title="安装 miniconda"
brew install miniconda
```

```shell title="验证安装"
conda -V
```

### node

```shell title="安装 node"
brew install node
```

```shell title="验证安装"
node -v
```

### 编程软件

- [Cursor](https://cursor.com/home)
- [Windsurf](https://windsurf.com/download/editor)
- [VSC](https://code.visualstudio.com/Download)
- [gemini-cli](https://github.com/google-gemini/gemini-cli)
- [Codex](https://github.com/openai/codex)
- [Claude Code](https://code.claude.com/docs/zh-CN/overview#homebrew)

```shell title="安装"
brew install --cask codex
brew install --cask claude-code
brew install gemini-cli
```

### paragon：NTFS 读写

在使用硬盘传数据的时候，老是报`错误代码 -50`，搜了一下才发现 mac 原生是不支持 NTFS 文件系统的

!!! info "什么是 NTFS"
    NTFS（New Technology File System）是由微软开发的一种文件系统，最早在 Windows NT 操作系统中引入。它是 Windows 系统的默认文件系统，用于存储和检索硬盘上的数据。

官网地址

[Microsoft NTFS for Mac | Paragon Software](https://www.paragon-software.com/home/ntfs-mac/)

搜了一下发现希捷的官网有一个免费的版本

[Paragon 驱动程序 | Seagate 中国](https://www.seagate.com/cn/zh/support/software/paragon/)

### WPS

zju 有企业账号，SSO 登陆输入 ZJU，验证登陆即可

### qq 音乐歌单导入 apple music

1. 获取 qq 音乐的歌单 id
2. 通过 id 获取歌单曲目
3. 通过 [Tune My Music](https://www.tunemymusic.com/zh-CN/transfer) 向 apple music 导入歌单曲目

> 参考文章：[将 QQ 音乐的歌单导入 apple music - 知乎](https://zhuanlan.zhihu.com/p/666443150)

## Apple Script

- 系统自带的“脚本编辑器”
- vscode 中`code runner`插件

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=887179224&bvid=BV1NK4y1T7wA&cid=311009872&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=600px></iframe>

> 参考资料
> [AppleScript 入门：探索 macOS 自动化 - 少数派](https://sspai.com/post/46912)
> [kevin-funderburg/AppleScripts: My collection of AppleScripts I've developed or acquired over the years.](https://github.com/kevin-funderburg/AppleScripts)

## conda 环境

[Miniconda — Anaconda documentation](https://docs.anaconda.com/miniconda/)
[miniconda 下载 m1/m2](https://repo.anaconda.com/minpiconda/Miniconda3-latest-MacOSX-arm64.sh)
[MAC OS m2 安装和卸载 miniconda - 知乎](https://zhuanlan.zhihu.com/p/619566718)
安装

```shell
# 文件名是自己下载的 sh 文件，-p 后面填安装路径
# -b 表示将环境变量自动写入到～/.bash 文件中
sh Miniconda3-latest-MacOSX-arm64.sh -b -p ~/miniconda3
```

前往安装地址，打开终端

```shell
source /bin/activate
```

执行

```shell
conda init zsh #zsh 执行这个命令
或者
conda init bash #bash 执行这个命令
```

```shell title="加入路径"
vim ~/.zshrc
export PATH=/yourpath/anaconda3/bin:$PATH
source ~/.zshrc
```

注意：上面的”/yourpath”要替换成你自己的 Anaconda 安装目录。
按 esc 退出编辑模式，保存文件并退出（输入”:wq”回车）

### 换 conda 源

=== "THU"
    ```shell
    conda config --add channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/>
    conda config --add channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/>
    conda config --add channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/>
    conda config --append channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/fastai/>
    conda config --append channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/>
    conda config --append channels <https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/>

    # 搜索时显示通道地址
    conda config --set show_channel_urls yes
    ```

=== "ustc 源"
    ```shell
    conda config --add channels <https://mirrors.ustc.edu.cn/anaconda/pkgs/main/>
    conda config --add channels <https://mirrors.ustc.edu.cn/anaconda/pkgs/free/>
    conda config --add channels <https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/>
    conda config --add channels <https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/>
    conda config --add channels <https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/>
    conda config --add channels <https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/>

    conda config --set show_channel_urls yes
    ```

### 换 pip 源

解决方案：将配置好国内源的`pip.conf`文件，放在 `~/Library/Application Support/pip` 中。

可能有的新用户发现自己的文件夹中没有 pip 文件夹，不慌，新建就行！

```shell
command + 空格            #  打开聚焦搜索
输入 ~/Library/Application Support       # 找到 Application Support 文件夹
```

在`Application Support`这个文件夹里面建一个 pip 文件夹;
在新建的 pip 文件夹下建一个`pip.conf`文件。

在`pip.conf`文件中输入以下内容，保存并退出。

```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
```

### 卸载

（1）使用 Anaconda-Clean 包删除所有与 conda 相关的文件和目录

```shell
conda activate your_conda_env_name
conda install anaconda-clean
anaconda-clean # add `--yes` to avoid being prompted to delete each one

#注：如果这一步之行不成功，可以直接跳过
```

（2）删除整个目录（直接删掉安装文件就可）

```shell
rm -rf ~/miniconda3
```

（3）删除将 conda 路径添加到 PATH 环境变量的行（或者注释掉）

注：其实只之行第二步就可，后边这两步为了再次安装时，环境冲突，所以删干净

```shell
vi ~/.bashrc
# -> Search for conda and delete the lines containing it
# -> If you're not sure if the line belongs to conda, comment it instead of deleting it just to be safe
source ~/.bashrc
```

```shell
vi ~/.zshrc
# -> Search for conda and delete the lines containing it
# -> If you're not sure if the line belongs to conda, comment it instead of deleting it just to be safe
source ~/.zshrc
```

（4）删除配置文件

```shell
rm -rf ~/.condarc
#注：自己找一下~/.conda 开头的文件，删掉
```
