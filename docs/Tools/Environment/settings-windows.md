
# Windows

!!! note "前言"
    这一篇的目的是记录一些常用的软件的安装与使用，以及一些常见的问题的解决方案。遇到重复的问题不至于反复搜索。
    另外也是为了在特殊环境下，可以迅速的切换到另一台设备进行工作，不至于项目停滞。

## 终端 & Powershell

快捷打开终端

1. `win + R`，输入`cmd`
2. `win + X`，选择`Windows Terminal`

常用命令

1. 删除文件：`del` 文件名
2. 查看 ip 命令：`ipconfig`
3. 清屏：  `clear`    (cmd 窗口清屏用 cls)
4. 查看列表 (list)：`ls`  （cmd 窗口用 dir）
5. 切换目录：`cd xxx`    直接切换到 xxx 文件夹
6. 切换盘符：`d:`    切换到 D 盘；`cd /d D:\Code`直接切换到 D 盘下的 Code 文件夹；但要注意，如果是在 C 盘下，直接输入`cd /d`是无法切换的

??? failure "无法加载 WindowsPowerShell\profile.ps1"
    [完美解决无法加载文件 WindowsPowerShell\profile.ps1系统编译问题-CSDN博客](https://blog.csdn.net/weixin_41194129/article/details/140538410)
    1. 按`Win + X` 键,`Windows PowerShell (Admin)`
    2. 使用命令 `Get-ExecutionPolicy -List`
    3. 更改执行策略：为了允许运行脚本，你可以将执行策略更改为 RemoteSigned 或 Unrestricted。
    ```shell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    如果你需要为所有用户设置执行策略，可以使用 -Scope LocalMachine 参数：
    ```shell
    Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
    ```
    4. 选择`Y`确认更改
    5. 重新打开终端
    6. 验证执行策略是否更改成功
    ```shell title="路径改为本地报错时候显示的路径"
    Get-Item "C:\Users\Administrator\Documents\WindowsPowerShell\profile.ps1" | Format-List * -Force
    ```

### 修改、查看、清除文件信息

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20241115001953.webp)

有时候想要修改文件信息，但是 GUI 界面没有这样的操作

打开终端界面

[Get-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Management/get-itemproperty?view=powershell-5.1)

```shell title="查看文件信息"
Get-ItemProperty -Path <path> -Name <property_name>

Get-ItemProperty -Path <path> | Format-List * -Force
```

[Set-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Management/Set-ItemProperty?view=powershell-5.1)

```shell title="修改文件信息"
Set-ItemProperty -Path <path> -Name <property_name> -Value <value>
```

- `CreationTime` 创建时间
- `LastWriteTime` 最后修改时间
- `LastAccessTime` 最后访问时间

[Remove-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Management/remove-itemproperty?view=powershell-5.1)

```shell title="清除文件信息"
Clear-ItemProperty -Path <path> -Name <property_name>
```

### 查看 MAC/机器码

cmd 打开终端

```shell
ipconfig/all
```

### 查看用户

```shell
net user
```

### wget

[GNU Wget 1.21.4 for Windows](https://eternallybored.org/misc/wget/)

放在`c:/Windows/System32`文件夹下

### nc (netcat)

[netcat 1.11 for Win32/Win64](https://eternallybored.org/misc/netcat/)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20241118214327.webp)

### 查看系统架构

`win+R`输入`cmd`，输入`wmic os get osarchitecture`查看系统架构

或者输入`dxdiag`查看系统信息

或者输入`systeminfo`查看，系统类型字段就可以看出来了

### 环境变量

#### python

如果设置了环境变量，却打不开 python，可以尝试将 python 的路径放在最前面

#### 如何用命令行直接打开软件

省流：建立一个文件夹保存快捷方式，将文件夹路径添加到 PATH 环境变量

首先你要创建一个文件夹，存储程序的快捷方式

- 右键点击计算机图标，选择属性，选择高级系统设置，高级->选择环境变量

- 编辑用户变量下的 PATH 复制存储快捷方式文件夹的路径

备注：快捷方式可以自定义名称，在 CMD 中输入名称就行了

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20201221085949893.webp)

高级系统设置 - 环境变量

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__image-20240422084315579.webp)

## windows 系统设置

### win+G 录屏

xGameBar 对我来说没什么用，但是虚拟机中需要使用到这个快捷键，所以将 win 下这个快捷键禁用

`win+I`进入设置，搜索 Game Bar

关闭里边选项即可。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240706192241.webp)

### 驯服自带输入法

[词库转换工具下载 imewlconverter](https://github.com/studyzy/imewlconverter/releases/tag/v3.1.1)

[词库搜索 - 搜狗输入法词库](https://pinyin.sogou.com/dict/search/)

[打造最强「Windows 10」微软拼音输入法 + 600 万词库下载 - 小羿](https://xiaoyi.vc/win10-pinyin-diy.html)

- **自定义短语**

输入法内置了大多数常用的短语，但我们依然可以进行自定义导入，以满足自身行业的特殊词汇需求。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240816114002.webp)

- **专业词典**

专业词典选项会被大部分人忽略——因为它看起来默认开启，但没有完全启用。

- **「V 模式」**
  
颇有意思，v 键进入后，可快速输入中文年月日时间以及公式运算等。

例如，你输入“`v123`”，在按 a 选择，呈现的结果就是“一百二十三”

`v12:55`，对应：十二时五十五分/ 12 时 55 分 / 十二分五十五秒 等

`v1989.08.12`，对应：1989 年 08 月 12/  一九八九年八月十二日 等
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240816114019.webp)

- **「U 模式」**

则方便用户输入一些特殊符号。如 win 笔记本键盘上并不存在的「」，就可以在输入 uubd 后找到。

- **其他**
  
输入 sjx，可以得到三角形 △ ▲
输入 slh，可以得到省略号
输入 pzh，可以得到中文破折号

- **emoji、颜文字与符号面板**
  
微软内置了 emoji 方案、颜文字、符号面板，使用 `Ctrl + Shift + B` 即可唤出。
[一些小技巧，让你的 Win 10 内置输入法更好用 - 少数派](https://sspai.com/post/52101#!)

### 如何让你的 win11 不再智障

- 驯化 windows 的软件**dism++** ，内置了很多小功能  [Releases · Chuyu-Team/Dism-Multi-language](https://github.com/Chuyu-Team/Dism-Multi-language/releases)

#### 右键菜单调整

[【Windows】Win11 右键恢复完整右键菜单\_windows 11 classic context menu-CSDN 博客](https://blog.csdn.net/u012153104/article/details/130195590)

使用快捷键`Win+X`，然后点击`Windows终端（管理员）`以打开管理员权限的命令提示符。

第一步

```shell
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

如果操作成功，命令提示符会显示“操作成功完成”消息。

第二步，重启资源管理器进程。

```shell
taskkill /f /im explorer.exe
```

```shell
start explorer.exe
```

#### 恢复 win10 开始菜单风格

从任务栏中选择搜索按钮并输入`regedit`。

当注册表编辑器出现时，选择打开。

通过从左窗格中展开文件夹来导航至此处：

`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`

右键单击左窗格中的高级，然后选择新建> DWORD（32 位）值。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240722095029.webp)

输入`Start_ShowClassicMode`作为新值的名称，然后按 Enter 保存它。双击并将数据更改为 1，然后选择确定。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240722095039.webp)

重启。

#### 任务栏自定义

[如何调整 Windows 11 任务栏位置、对齐方式，及自定义任务栏](https://www.sysgeek.cn/windows-11-taskbar-customize/)

### 电脑蓝屏

查看错误原因

蓝屏以后先重启

#### 排查方法———WinDBG 查看.dmp 文件

[查找/分析 Windows 蓝屏 DMP 文件\_蓝屏文件在哪个文件夹-CSDN 博客](https://blog.csdn.net/pzhier/article/details/102593562#)

下载 WinDBG[64 位](https://link.csdn.net/?target=https%3A%2F%2Fdownload.microsoft.com%2Fdownload%2FA%2F6%2FA%2FA6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D%2Fsetup%2FWinSDKDebuggingTools_amd64%2Fdbg_amd64.msi)

1. 运行 Windbg，然后按 Ctrl+S 或从文件菜单中打开符号表设置窗；
2. 将符号表地址：`SRV*C:\Symbols*http://msdl.microsoft.com/download/symbols` 粘贴在输入框中，确定。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240720005545.webp)

可使用`Ctrl+D`快捷键来打开一个 dmp 文件，或者点击 WinDbg 界面上的`File=>Open Crash Dump`按钮，来打开一个 dmp 文件。第一次打开 dmp 文件时，可能会收到如下提示，出现这个提示时，勾选`Don’t ask again in this WinDbg session`，然后点否即可

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240720005606.webp)

!!! tip "打开第二个 DMP 文件"
    如果在打开第二个DMP文件时，可能因为上一个分析记录未清除，导致无法直接分析下一个dmp文件，可以使用快捷键`Shift+F5`来关闭上一个DMP的分析记录。

打开之后首先查看两点

- 第一个关键信息：`Probably caused by:`
- 第二个关键信息：找到并点击`！analyze –v`，从弹出的内容中查找 `BUGCHECK_STR:`
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240720010134.webp)

[Windows Bug Check Code Reference](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-code-reference2)

#### memory_management

[只要看直播或者 b 站视频就容易蓝屏 NGA 玩家社区](https://ngabbs.com/read.php?tid=36810975&rand=354)

[在看 B 站时突然蓝屏，报错 VIDEO\_xxx，蓝屏上面还有 B 站横幅。 - Microsoft Community](https://answers.microsoft.com/zh-hans/windows/forum/all/%E5%9C%A8%E7%9C%8Bb%E7%AB%99%E6%97%B6%E7%AA%81/1c6e5719-545b-4f6e-9f39-5dfa49e218dc)

### 显示器相关

#### 如何修复 Type-C 接口

当我的 type-c 接口插了一段时间以后，接口就会出现松动的情况

用针头将两侧的钩子撑开，就可以解决一定问题

> 以下图片来自[USB TYPE C 拆解以及 USB3.1 规范详解 (lulian.cn)](https://www.lulian.cn/news/88-cn.html)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__1540889232305758.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__1540889232965453.webp)

#### 盒盖不息屏

设置里搜“关闭盖子”

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__v2-debea2bfb9bc1c5d7449c2a6c7080dfd_720w.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__v2-79a54efe642a46bd24107b2a97f160d1_720w.webp)

#### 投屏方式

**Windows +A**进入消息中心

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__image-20240429090307137.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__image-20240429090336993.webp)

打开显示设置，调节分辨率

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__image-20240429090404258.webp)

### 网络相关

#### 查看 wifi 密码

#### clash 忘记关了解决方案

- `win+x` 点击网络连接
- 点击高级网络设置，“Internet 选项”
- 点击“连接”弹窗的“局域网设置”
- 取消代理服务器这里的对勾

### 账户相关

#### 密码

`win+x` - 设置 - 账户 - 登录选项 - 设置 PIN 和指纹登陆

### onedrive 账号解冻方法

超过系统的免费额度，账号会被封禁，被封禁后，桌面端会无法登录，显示错误代码`0x8004def7`
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240814121753.webp)

### C 盘爆了

#### c 盘扩容（开源）

[DiskGenius – 正式版下载 | 免费下载](https://www.diskgenius.cn/download.php)

[Diskgenius 分区把 c 盘扩大操作方法 - 百度经验](https://jingyan.baidu.com/article/f7ff0bfc2b07076f26bb13bb.html)

#### 删除无用文件（节流）

- 依次点击：此电脑，右键 C 盘，属性，清理磁盘，清理系统文件（有时候电脑更新了，旧的安装包不会自动删除，就可能占用十几 G）；
- 清空回收站
- **geek 卸载软件** 下载 geek（[Geek Uninstaller - Download](https://geekuninstaller.com/download)
），找到不用的软件，删除卸载，它能很干净得删除软件，包括所有有关文件夹和注册表，very nice，强推，注意：geek 会删除该软件的所有文件夹，如果个人文件保存在这些文件夹里面，需要提前转移，否则将造成资料丢失！！；
- **ccleaner** 下载 ccleaner（认准官网，免费版就行），里面的清理注册表，扫描，修复，再扫描，修复，再扫描，修复，重复三次（无须备份）；然后自定义清理，运行清理程序（注意，该操作会导致你在浏览器里面登入的如哔哩哔哩账号这种，会给你下线从而需要重新登入，为了避免，可以仔细看看自定义清理里面勾选了哪些，然后选择性清理就行）；geek 卸载不了的软件如 VS，SW 等，用 cc 卸载；
- 找到**电脑管家**（无论是啥都行），找到里面的清理垃圾功能，扫描，清理；如果有系统修复啥的，漏洞修复啥的，全部来一遍；
- 下载**treesize**（一定要认准免费版，下载过程中会多次引诱你下载专业版，不要上当，下载的时候看仔细），每次用管理员身份运行，一个一个目录点开看看，是哪个文件夹占了空间，不知道是什么的就去百度一遍看看是什么，怎么删；

!!! note "常见占用内存"
    - wechat 聊天记录及缓存文件及下载的文件
    - 飞书缓存文件
    - conda 库文件

#### 移动各种文件（找补）

**移动系统文件夹**

移动桌面、文档、下载等文件夹到其他盘

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240923144021.webp)

**移动`.vscode`**

- `ctrl + x`选择以管理员身份运行 cmd
- 剪切原文件`.vscode`到`D:\.`vscode 文件夹。

```shell
cmd /c mklink /D "%USERPROFILE%\.vscode" "D:\.vscode\"
```

[vscode 修改默认扩展和用户文件夹目录到 D 盘\_.vscode 文件怎么换盘-CSDN 博客](https://blog.csdn.net/sg_knight/article/details/130258619)

**移动`TEMP`和`TMP`文件夹**

把`TEMP`和`TMP`文件夹移动到其他盘

**移动大软件**

找到电脑设置、系统、存储，去里面查看 C 盘安装了哪些大软件，用 geek 卸载了安装到其他盘。

## edge

### 快捷键

- ctrl+tab 切换下一个标签页
- ctrl+shift+tab 切换上一个标签页
- ctrl+H 历史记录
- ctrl+J 下载

<iframe src="https://support.microsoft.com/zh-cn/microsoft-edge/microsoft-edge-%E4%B8%AD%E7%9A%84%E9%94%AE%E7%9B%98%E5%BF%AB%E6%8D%B7%E6%96%B9%E5%BC%8F-50d3edab-30d9-c7e4-21ce-37fe2713cfad" width="100%" height="600px"></iframe>

## c 环境

[MSVC、MINGW，gcc、g++，qmake、cmake 的联系和区别是什么？ - 知乎](https://www.zhihu.com/question/333560253)

### MinGW 安装

[Download MinGW - Minimalist GNU for Windows](https://sourceforge.net/projects/mingw/files/latest/download)
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20241010103943.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20241010104231.webp)

勾选 base 和 g++ 两个，然后点击左上角的 Installation，选择 Apply Changes

设置 path 环境变量，将`....\MinGW\bin`添加到 path 中

验证安装

```shell
gcc -v
g++ -v

```

> [参考博客:MinGW 下载安装教程 傻瓜式操作](https://blog.csdn.net/qq_38196449/article/details/136125995)

### vscode 环境

[VS Code 配置 C/C++ 编程运行环境](https://blog.csdn.net/qq_42417071/article/details/137438374)

安装 c/c++ 插件：
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20241010110358.webp)

## excel

### 选择数据

- `ctrl + shift + ↓` 选择一列
- `ctrl + shift + →` 选择一行

## Mail

### 我使用的邮箱

- zju 邮箱
- 126 邮箱
- gmail
- qq 邮箱
- outlook 邮箱

### pop3

### IMAP

#### outlook 添加浙大邮箱

- “IMAP”则接收服务器： `imap.zju.edu.cn` 端口`143`，勾选 SSL 端口：993；
- “POP3”则接受服务器： `pop3.zju.edu.cn` 端口`110`，勾选 SSL 端口：995；
- 发送服务器都为：`smtp.zju.edu.cn` 端口：`25`，勾选 SSL 端口：994。
- 在“登录信息”的“用户名”填写完整邮箱地址，如`test@zju.edu.cn`
- 密码处填写邮箱密码

#### 添加 qq 邮箱

在 qq 邮箱设置处开启 IMAP/SMTP 服务，需要绑定手机号，然后手机发验证短信
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-windows.assets__20240814123902.webp)
发完验证短信后，会有一个授权码，这个授权码就是密码

## 模拟器

### 雷电模拟器

[雷电安卓模拟器 - 手游模拟器安卓版\_android 手机模拟器电脑版\_雷电模拟器官网](https://www.ldmnq.com/)

可以使用设置墨墨背单词

## ZJU

### 智云课堂

对于录播视频，这就很简单粗暴了，直接找到 div class = `cmc-base cmc-video`行并展开，下面有一个`https://vod.cmc.zju.edu.cn/`开头网址

[智云课堂加载不出来解决办法 - CC98 论坛](https://www.cc98.org/topic/5902398)

## VLC

将 VLC 目录加入系统环境变量 Path

**快捷键**

`[`减慢速度；`]`加快速度

```shell
vlc <address>
vlc -f <address> # 全屏播放
vlc --rate <speed> <address> # 倍速播放
```

[vlc 的命令行使用方式\_vlc 用控制台播放音频-CSDN 博客](https://blog.csdn.net/fengmm521/article/details/79596447)

<https://interactivemeta.cmc.zju.edu.cn/#/studentsrs?course_id=63546&sub_id=1393805&tenant_code=112>

<https://interactivemeta.cmc.zju.edu.cn/#/replay?course_id=63546&sub_id=1301338&tenant_code=112>

course_id 是课程 id
sub_id 是章节 id
tenant_code 是租户 id

sub_id  貌似是根据一定规则进行生成的，不清楚后台的 hash 算法

但观察发现，有连续

查询`https://classroom.zju.edu.cn/courseapi/v3/multi-search/get-course-detail?course_id=67855&student=<student_id>`即可获得课程详细信息
