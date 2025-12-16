# 如何复制 Phil Fan 的工作环境

## 效率软件

- 浏览器：Safari，[Edge](https://www.microsoft.com/zh-cn/edge/download)
- 日程：苹果自带日历，[滴答清单](https://dida365.com/download?language=zh_CN)
- 多媒体：[VLC media player](https://www.videolan.org/vlc/index.zh_CN.html),[PicGo（图床）](https://github.com/Molunerfinn/PicGo/releases)
- 思维导图：[Xmind](https://xmind.cn/download/)；首选项设置 深色主题 `alt+s`:概要 `ctrl + l`:方程
- 即时通讯：[TIM](https://tim.qq.com/download.html)，[WeChat](https://weixin.qq.com/)，[飞书](https://www.feishu.cn/download/)，[腾讯会议](https://meeting.tencent.com/download/)，[钉钉](https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownload#/),[微信文件传输网页版](https://filehelper.weixin.qq.com/)
- PDF 阅读：Adobe Acrobat(adobe 处下载)
- Markdown: [Typora](https://typoraio.cn/)
- 云同步 (付费)：[百度网盘](https://pan.baidu.com/download#win)、[阿里网盘](https://www.alipan.com/)，坚果云 WebDav
- 音乐：[QQ 音乐](https://y.qq.com/download/index.html), Apple Music
- 远程：[ToDesk](https://www.todesk.com/)、无影云电脑
- 压缩：[Bandzip](https://www.bandisoft.com/bandizip/)
- 其他：[logi option+](https://www.logitech.com/zh-cn/setup/ergosetup/logi-options.html)
- 公式识别：[SimpleTex](https://simpletex.cn/)  优化得不错
- RSS 阅读器：[Folo](https://folo.is/?new_locale=zh-cn)
- LLM: [Cherry Studio](https://www.cherry-ai.com/)
- 邮件：Gmail
- 密码管理：Apple 密码管理
- 翻译：[欧陆词典](https://www.eudic.net/v4/en/app/download),欧陆词典文件[词典下载网站](https://forum.freemdict.com/tag/%EF%BB%BF英语/l/hot)
- 录屏：[OpenScreen](https://openscreen.vercel.app)

### :fontawesome-brands-apple: MacOS

- 开发工具 iTerm2：[iTerm2 - macOS Terminal Replacement](https://iterm2.com/)
  - 教程：[iTerm2 安装配置使用指南——保姆级 - 知乎](https://zhuanlan.zhihu.com/p/550022490)
  - oh my zsh
  - 设置启动热键
    - 第一步：`preference -> keys ->Create a Dedicated Hotkey Window`
    - 第二步骤：设置 Hotkey，我设置和 Linux 差不多布局的 `command（Ctrl+Alt+T）`
- [Raycast - Your shortcut to everything](https://www.raycast.com/) 替代聚焦
  - command +k 显示
  - [能少一个是一个：我用 Raycast 替代了这些应用 - 少数派](https://sspai.com/post/72540)
  - 软件卸载
  - 快速打开应用：[URL Schemes | Drafts User Guide](https://docs.getdrafts.com/docs/automation/urlschemes#append)[Raycast 小技巧之 Quicklink 二三事 - 少数派](https://sspai.com/post/72951)
  - 窗口管理
- [ibar](https://apps.apple.com/cn/app/ibar/id6443843900?mt=12): 菜单栏隐藏
- [Pixea](https://apps.apple.com/cn/app/pixea/id1507782672?mt=12)
- [clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev): VPN
- [Downie](https://www.downie.cn/): 下载工具
- [Bandzip](https://www.bandisoft.com/bandizip.mac/): 压缩工具
  - [如何在 Mac 上更改默认应用程序](https://www.bandisoft.com/bandizip.mac/howto/default-app-changer/)
  - 设置为访达扩展

    ```shell title="设置为访达扩展"
    pluginkit -e "use" -i "com.bandisoft.mac.bandizip.findersyncextension"
    ```

- [Scroll Reverser for macOS](https://pilotmoon.com/scrollreverser/): 反向滚动鼠标和触控板
- [Typora](https://typoraio.cn/): Markdown

    ```shell
    echo 'alias typora="open -a Typora"' >> ~/.zshrc
    ```

- windows 虚拟机 [Parallels Desktop](https://www.parallels.cn/products/desktop/trial/)，可以找一个 tb 店解锁
- [waydabber/BetterDisplay](https://github.com/waydabber/BetterDisplay?tab=readme-ov-file)：没钱上 4K 显示器的解决方案，Unlock your displays on your Mac! Flexible HiDPI scaling
- $\LaTeX$ 环境

    ```shell
    brew install mactex --cask
    ```

- [Piclist](https://piclist.cn/): 图床

    ```shell title="安装 piclist"
    brew install piclist --cask
    ```

!!! note "注意 macos 没有签名时候需要手动信任"
    ```shell
    xattr -cr /Applications/zju-learning-assistant.app
    ```

!!! note "资源站"
    尽量还是支持正版

    1. [xclient](https://xclient.info/)
    2. [macked](https://macked.app/)
    3. [digit77](https://www.digit77.com/)
    4. [xmac](https://xmac.app/)
    5. [macwk](https://macwk.cn/)

### :fontawesome-brands-windows: windows

- 图片： [bandView](https://www.bandisoft.com/bandiview/)，[honeycam(动图)](https://www.bandisoft.com/honeycam/)
- 网络相关：[Clash for windows](https://www.clash.la/archives/748/),[v2rayN](https://github.com/2dust/v2rayN/releases),[下载 .NET 8.0 Desktop Runtime (v8.0.8) - Windows x64 Installer](https://dotnet.microsoft.com/zh-cn/download/dotnet/thank-you/runtime-desktop-8.0.8-windows-x64-installer?cid=getdotnetcore)
- 下载：[utorrent](https://file.cc98.org/v2-upload/il0glpvw.zip)
- 卸载工具[Geek Uninstaller - Download](https://geekuninstaller.com/download),磁盘扫描[WizTree - Download](https://www.diskanalyzer.com/download)
- 使用时长统计：[ManicTime](https://www.manictime.com/download/windows)
- 系统插件：三指拖移插件 [Three Finger Drag - Windows 官方下载 | 微软应用商店 | Microsoft Store](https://apps.microsoft.com/detail/9msx91wqcm2v?hl=zh-CN&gl=US)

## 专业软件

- Coding: [VSC](https://code.visualstudio.com/Download),[Cursor](https://cursor.com/home), [Windsurf](https://windsurf.com/download/editor)
- Environment:
  - Python:uv/[miniconda(smaller)](https://docs.anaconda.com/miniconda/)/[anaconda](https://www.anaconda.com/download)
  - Git: [git](https://git-scm.com/download/win)
  - Node: [node](https://nodejs.org/en/download/)
- 文献：[Zotero](https://www.zotero.org/download/)
- latex：texlive,[overleaf](https://www.overleaf.com)
- 绘图：ppt,Draw.io, ai,ps,Geogebra,python
- 数据：excel，Tableau
- word，[小恐龙公文助手](https://xkonglong.com/xkl_wordaddin/)
- 驯化 windows dism++ [Releases · Chuyu-Team/Dism-Multi-language](https://github.com/Chuyu-Team/Dism-Multi-language/releases)
- 音乐：[Sibelius(西贝柳斯) 打谱软件](https://sibelius.mairuan.com/)
- Matlab

## 设计软件

- [Adobe](https://www.adobe.com/cn/):AI,PS,PR,[剪映](https://www.capcut.cn/)
- powerpoint,okplus,[Canva](https://www.canva.cn/)

## edge/chorme 插件

**更好体验**

- global speed：最好用的倍速
- Vimium C：使用 vim 全键盘操作浏览器; tutorial:[vimium 成神之路 - 键盘党的胜利 - 知乎](https://zhuanlan.zhihu.com/p/64533566)
- ADguard：去除广告
- Circle 阅读助手：沉浸式阅读，纯净阅读
- 油猴/篡改猴：更多脚本/插件
- Octotree

**资源类**

- Copy as Markdown: 复制成为 markdown 格式的链接
- Simple Allow Copy: 解除网站的禁用复制
- Image Downloader：下载网站上出现过的图片
- Zotero Connector: 链接 Zotero
- 哔哔君：b 站字幕下载

**翻译**

- 沉浸式翻译：好用的网页翻译
- Grammarly：AI writing and grammar checker

**其他**

- HackBar
- Cookie-Editor

## vscode

### 使用

- F1 打开命令面板
- `ctrl + P` 搜索文件名打开文件
- `ctrl + F` 搜索内容
- 搜索工作区内容的快捷键是`Ctrl + Shift + F`，或者在菜单栏中选择 `查看 (View)` -> `搜索 (Search)`

### 配置

#### 自动换行

- F1，输入 `Open User Settings`
- 搜索 `word wrap`
- 修改为 `on`
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-software.assets__20241211133345.webp)

#### 内存占用过大问题

1. 找到文件 - 首选项 - 设置：禁用自动保存
2. 找到文件 - 首选项 - 设置，搜索`git.enabled`,禁用 git
3. 禁用`search.followSymlinks`：控制是否在搜索中跟踪符号链接
4. 按`f1`，输入`developer: open process explorer`，会打开一个任务管理器一样的窗口，查看里面 cpu 和内存占用最高的进程，然后一个个禁用你的扩展插件，直到 cpu 和内存占用正常，这样就可以找出耗内存的扩展然后按照你的开发需求更换或者禁用

#### 安装`code`命令

把 vscode 安装路径下的`bin\`文件夹添加到环境变量中，就可以实现命令行操作

- `code .` 打开当前文件夹
- `code filename` 打开文件

#### 自动补全设置

设置界面 - 文本编辑器 - 建议

- 找到 `share suggest selections` 画钩
- Editor：sugggest selection 中把`first`改成`recentlyUsed`
- 打开`settings.json`文件，添加

```json
  "editor.suggest.snippetsPreventQuickSuggestions": false,
     "files.associations":{
                "*.html":"html"
        },
```

### 插件

#### project manager

#### copy as markdown

**copy as markdown**

[chorme 下载地址](https://microsoftedge.microsoft.com/addons/detail/copy-as-markdown/cbbdkefgbfifiljnnklfhnhcnlmpglpd)

#### markdown 插件

- Markdown Preview Enhanced
- Markdown emoji
- paste image

设置一个`picgo`的快捷键，我这里设置的是`ctrl + alt + P`

截图之后直接按就可以将图片上传到图床，并将连接复制到剪贴板

#### vim

#### 基础功能

- chinese
- edit csv
- error lens
- path intellisense
- image preview
- Prettier: code formatter
- doxygen documentation generator
- hungry delete

#### jupyter

#### Remote - SSH

#### latex workshop
