# Linux

!!! note "这一篇主要记录在配置 linux 时候遇到的一些问题和解决方案"

## 常见操作

### 压缩

```shell title="递归压缩"
zip -r examples.zip examples   # examples 为目录
```

```shell title="解压缩"
unzip name.zip
```

```shell title="目录路径来指明压缩包所在的位置"
unzip name.zip -d 当前目录
```

```shell title="如果是压缩包是.tar 后缀"
tar xvf name.tar 
```

```shell title="如果是压缩包是.tar.gz 后缀"
tar -xzvf name.tar.gz -C /path/to/destination
```

### 复制 scp

[关于 scp 传输文件踩过的坑 (最全!linux 与 windows 相互传输文件，连接失败，免密登录，连接超时) - 知乎](https://zhuanlan.zhihu.com/p/542926236)

#### 基本语法

```shell
scp [可选参数] 源文件 目标文件
```

```shell
# 复制文件
scp local_file remote_username@remote_ip:remote_folder
scp local_file remote_username@remote_ip:remote_file

# 复制目录
scp -r local_folder remote_username@remote_ip:remote_folder
```

- `-r`: 递归复制整个目录
- `-P port`: 指定远程主机的端口号
- `-p`: 保留原文件的修改时间和访问权限
- `-q`: 不显示传输进度条
- `-C`: 允许压缩
- `-v`: 详细方式显示输出

#### 示例

```shell
# 复制本地文件到远程服务器
scp file.txt user@192.168.1.100:/home/user/

# 复制远程文件到本地
scp user@192.168.1.100:/home/user/file.txt ./

# 复制整个目录
scp -r local_folder user@192.168.1.100:/home/user/

# 使用特定端口
scp -P 2222 file.txt user@192.168.1.100:/home/user/
```

### nano 编辑器

常见操作

|操作 | 快捷键|
|---|---|
|保存|`Ctrl + O`|
|退出|`Ctrl + X`|
|删除|`Ctrl + K`|

### 蓝牙操作

打开系统蓝牙

```shell
systemctl status bluetooth
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20240914224410.webp)

```shell
sudo service bluetooth start
```

```shell
sudo /etc/init.d/bluetooth restart
```

```shell title="管理界面"
bluetoothctl
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20240914224418.webp)
输入以下命令

```shell
list 
scan on 
devices
power on
agent on 
default-agent
pair yourDeviceMAC
```

其中 pair 后面跟上扫描出的键盘的 MAC 地址，根据提示输入密码，显示配对成功，此时，在桌面的设置界面"我的设备"中可以看到蓝牙中键盘为已配对状态，但此时可能依然无法成功连接。

### 查看系统信息

查看 cpu 信息

```bash
cat /proc/cpuinfo
```

查看系统架构

```bash
uname - a
```

[x86-64、amd64、arm、aarch64 都是些什么？-CSDN 博客](https://blog.csdn.net/qq_24433609/article/details/125991550)

```shell
sudo !4
```

执行历史记录中第 4 条命令

### 更改密码

```shell
passwd
```

更改其他用户密码

```shell
sudo passwd username
```

更改 root 密码

```shell
sudo passwd root
```

### 打开文件夹

```shell
open .
```

```shell title="安装"
sudo apt-get install nautilus
```

```shell
nautilus .
```

### 截图

- 使用 screen
- 使用键盘上面的 print screen

[如何在 Ubuntu 中截取屏幕截图（5 种简单方法）](https://techblik.com/%E5%A6%82%E4%BD%95%E5%9C%A8-ubuntu-%E4%B8%AD%E6%88%AA%E5%8F%96%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%EF%BC%885-%E7%A7%8D%E7%AE%80%E5%8D%95%E6%96%B9%E6%B3%95%EF%BC%89/)

## 系统管理 - 网络

### VPN

[linux install clash](https://zhuanlan.zhihu.com/p/2852384493)

uname -a

如果输出包含 x86_64 使用下面命令安装：

```shell
wget https://github.com/clashdownload/Clash_for_Windows/releases/download/0.20.39/Clash.for.Windows-0.20.39-x64-linux.tar.gz
```

如果输出包含 aarch64 使用下面命令安装：

```shell
wget https://github.com/clashdownload/Clash_for_Windows/releases/download/0.20.39/Clash.for.Windows-0.20.39-arm64-linux.tar.gz
```

```shell title="使用代理下载"
wget "https://gh-proxy.com/https://github.com/clashdownload/Clash_for_Windows/releases/download/0.20.39/Clash.for.Windows-0.20.39-arm64-linux.tar.gz"
```

如果 wget 下载不了，到 Windows 把这两个链接输进去下载好，再用 u 盘拷贝到你的 Linux 系统也是一样的。

找到你下载的安装包，解压提取，打开文件夹，里面有一个 `cfw` 文件，双击就是 Clash 了。如果不行，请在该文件夹内打开终端，使用`./cfw`命令执行它。

进入网络设置，把 proxy 改成这个样子

```shell title="终端走代理"
export http_proxy=http://your_proxy_server:your_proxy_port
export https_proxy=http://your_proxy_server:your_proxy_port
```

!!! question "could not connect to the clash core"
    检查一下网络是否能够正常连接，有可能是防火墙的规则的问题

    ```bash title="允许所有入站流量"
    sudo iptables -A INPUT -j ACCEPT
    ```

### 连接 wifi

```shell
sudo vim /etc/netplan/50-cloud-init.yaml
```

```yaml
network:
  ethernets:
    enp2s0:
      dhcp4: true
  wifis:
    wlan0:
      dhcp4: true
      access-points:
        "<ssid>":
          password: "<passowrd>"
  version: 2
```

设置好之后退出，重启网络

```shell
sudo netplan apply
```

1.该编辑文件中**不能出现制表符**，要不然会有问题；在执行后面的命令会报错；

2.改文件的编辑必须严格按照格式来，**是分层的**，用空格来退格

[启动 netplan-wpa-wlan0.sevice 失败：未找到单元 netplan-wpa-wlan0.service - ubuntu](https://askoverflow.dev/ubuntu/question/1291424/failed-to-start-netplan-wpa-wlan0-sevice-unit-netplan-wpa-wlan0-service-not-fou/)
!!! tip "注意事项"
    出现类似错误：`line8 column 6:cloud not find expected` 提示是**冒号：后面没加空格**

    出现类似错误：`netplan found character that cannot start any token`，提示是没有按五个层次写配置文档，一定要**下一层比上一层多空一格或以上。**

    出现类似错误： `Invalid YAML: inconsistent indentation:`  #缩进不对，就是**每一层没有严格缩进**

```shell
sudo apt install net-tools wireless-tools network-manager
```

### 校网验证

Wifi 连接
`net2.zju.edu.cn`

有线网 - [QSCTech/zjunet: Command Line Scripts for ZJU (VPN / WLAN / DNS)](https://github.com/QSCTech/zjunet)

```shell
curl https://mirrors.zju.edu.cn/openzjunet/zjumirrors.pgp | sudo tee /etc/apt/trusted.gpg.d/zjumirrors.asc
curl https://mirrors.zju.edu.cn/openzjunet/zjunet.list | sudo tee /etc/apt/sources.list.d/zjunet.list
sudo apt-get update
sudo apt-get install zjunet
```

[比较简单的 ubuntu 18.04 有线连接校园网的方法 - CC98 论坛](https://www.cc98.org/topic/4899317/1#1)

### 路由

```shell title="查看路由表"
route -n 
```

可以找到默认网关

```shell title="编辑路由表"
sudo vi /etc/resolv.conf
```

添加

```shell
nameserver xxx.xxx.xxx.xxx
```

[静态路由](https://blog.csdn.net/u010521062/article/details/114067036)

[Linux 配置静态 IP](https://www.cnblogs.com/chy18883701161/p/12396035.html)

### 防火墙 - iptables

#### 启用

```bash
sudo systemctl start iptables
sudo systemctl enable iptables
```

#### 查看防火墙规则

```bash
sudo iptables -L -n
```

查看所有防火墙规则，包括入站和出站规则。

#### 添加防火墙规则

- **原因**：在系统安装后，默认情况下可能没有添加任何`iptables`规则。
- **解决方法**：您可以手动添加所需的规则。例如，如果您想：

```bash title="允许所有入站流量"
sudo iptables -A INPUT -j ACCEPT
```

```bash title="允许所有出站流量"
sudo iptables -A OUTPUT -j ACCEPT
```

如果规则列表为空，您可以添加所需的规则。例如：

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

#### 保存防火墙规则

```bash
sudo iptables-save > /etc/sysconfig/iptables
```

然后保存规则：

```bash
sudo iptables-save > /etc/sysconfig/iptables
```

### 防火墙 - firewalld

```shell title="停止 firewalld"
sudo systemctl stop firewalld
```

```shell title="禁用 firewalld"
sudo systemctl mask firewalld
```

```shell title="查看防火墙状态"
sudo systemctl status firewalld
```

```bash title="查看防火墙规则"
sudo firewall-cmd --list-all
```

```bash title="检查端口是否开放"
sudo firewall-cmd --query-port=<端口号>/tcp
```

```bash title="检查80端口是否开放"
sudo firewall-cmd --query-port=80/tcp
```

### 端口占用 - lsof

```shell
sudo lsof -i :<port>
```

这个命令可以查看端口被哪个进程占用

```shell title="杀死进程"
kill -9 <pid>
```

### 端口占用 - netstat

```shell
netstat -ano | find "端口号"
```

例如，检查 80 端口：

```shell
netstat -ano | find "80"
```

```shell title="查看占用"
sudo netstat -tulpen | grep <port>
```

```shell title="解除占用"
sudo kill -9 <pid>
```

### 搭建局域网

```shell
apt-get install -y cifs-utils
```

#### windows 做服务器

[在 windows 上共享文件夹](https://zhuanlan.zhihu.com/p/402820328)
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20241026225133.webp)
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20241026225143.webp)

#### windows 作客户端

如果你是没有打开 smb 服务，那么继续往下看，打开控制面板进入

点击"启用或关闭 windows 功能"

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20241123092300.webp)

把 smb 的几个都点开，然后点击确定，立即重启

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20241123092342.webp)

然后直接在 explorer 中输入 ip 地址即可。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20241123092550.webp)

注意输入的格式：

- 不是`smb://156.26.51.55`
- 而是应该直接`双斜杠+ip地址`，如果有具体的共享的文件夹的话就把路径跟在后面。不需要加 smb 前缀，也不能用 `//` ，要用 `\\`,然后输入对应的账户和密码就完事了。

> [window10 使用 smb 连接远程电脑的文件夹 [打开 smb 服务和连接巨坑]-CSDN 博客](https://blog.csdn.net/qq_44079295/article/details/120201515)
>
#### linux 做服务器——samba

```shell title="安装"
sudo apt install samba
```

```shell title="启动服务"
systemctl start smbd.service

systemctl enable smbd.service

systemctl start nmbd.service

systemctl enable nmbd.service
```

```shell
systemctl status smbd.service
systemctl status nmbd.service
```

```shell title="设置共享文件夹"
net usershare add "共享名" /home/Desktop/文件名 "备注名" Everyone:R guest_ok=y
```

|参数 | 含义|
|---|---|
|Everyone:R |设置 Everyone 用户为只读权限|
|Everyone:F |设置 Everyone 用户为可写权限|
|Everyone:D |设置 Everyone 用户为拒绝权限|
|guest_ok=y |允许匿名访问|
|guest_ok=n |不允许匿名访问|

```shell title="客户端侧安装"
sudo apt install smbclient
```

```shell title="使用命令登录"
smbclinet //ip/name -U xxx
```

> [Linux 上挂载 Samba（Windows & macOS 共享文件夹）的正确姿势 - 知乎](https://zhuanlan.zhihu.com/p/26763026)

!!! tip "注意权限问题"
    1. 设置了当前共享文件夹有可写权限的话，那么需要增加当前文件夹的 other 的写权限

    2. 设置了匿名访问的话需要设置当前目录以及这个目录的父目录的 other 的可执行权限

    不然的话，不管使用命令访问还是使用图形界面访问都是会导致**报错没有权限**的问题

#### linux 作客户端——挂载文件系统

```shell title="举例"
smbclient -L 192.168.1.70 -U lab

Enter lab's password:   #输入密码，不回显
Domain=[WIN7] OS=[Windows 7] Server=[Windows 7]
   #共享点名称#      #类型#      #描述# 
    Sharename       Type      Comment
    ---------       ----      -------
    ADMIN$          Disk      远程管理
    Share               Disk      
    C$              Disk      默认共享
Connection to 192.168.1.70 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND) 
NetBIOS over TCP disabled -- no workgroup available #可能会出现一些错误警告，不过可以列出的话就不用管
```

将 `//<ip>/test` 挂载到 `/mnt/` 目录上，如果不需要认证，则无需指定用户名和密码。

```shell
sudo mount -t cifs //<ip>/test /mnt/test_shared -o dir_mode=0777,file_mode=0777
```

[linux mount 挂载文件夹设置权限 - 秋声梧叶 - 博客园](https://www.cnblogs.com/sctrkb/articles/15407736.html)

开机自动挂载（修改 `/etc/fstab` 文件）：

将`//192.168.xx.xx/sharedir`挂载到`/mnt/cifs`上，并指定了用户名和密码;如果不需要认证，可以不指定用户名和密码。

```shell
//192.168.3.4/sharedir /mnt/cifs cifs username=demo,password=demo 0 0
```

然后可以把`/mnt/folder`直接当作 linux 中的文件夹进行文件的操作

```shell title="解除挂载"
umount /dev/hda2
```

> pywin32 库没有安装好 [Python 如何通过 Python 访问 Windows 网络上的共享文件夹 | 极客教程](https://geek-docs.com/python/python-ask-answer/311_python_using_python_how_can_i_access_a_shared_folder_on_windows_network.html)

## 系统管理 - 用户和组

### 新建用户

```shell title="创建 root 用户"
sudo passwd root
```

```shell title="创建普通用户"
sudo adduser username
```

```shell title="删除用户"
sudo userdel -r username
```

```shell title="查看密码"
sudo grep bash /etc/passwd
```

### 用户权限

```shell title="给新用户 root 权限"
sudo usermod -a -G adm username
sudo usermod -a -G sudo username
```

```shell title="删除用户 sudo 权限"
sudo deluser username sudo
```

### 更改文件所属

```shell title="更改文件所属"
sudo chown username:groupname filename
```

```shell title="更改文件所属"
sudo chown -R username:groupname folder
```

[Linux chown 命令教程：如何改变文件或目录的所有者和组 (附案例详解和注意事项)\_chown 修改文件所有者-CSDN 博客](https://blog.csdn.net/u012964600/article/details/135845447)

## Q & A

### 注意删除不可恢复，所以删除尽可能谨慎

```shell
mv ./file_need_to_delete ./file_need_to_delete_backup
touch ./file_need_to_delete
```

### sudo 下的 PATH 环境变量
>
> 摘自[修改或定义 sudo 下的 PATH 环境变量 - ItsukiFujii](https://www.cnblogs.com/YukiNote/p/11375292.html)

Linux 在普通用户权限下，可以使用 sudo 去执行相关的命令，但是有时候会提示：`Command not found`

这是因为由于安全考虑，sudo 执行用一个程序时会在新的，最小化环境中执行，即使在环境变量`PATH`中设置了路径也找不到，因为在 sudo 执行下，采用默认的`PATH`变量使用。

```shell title="解决方法 1"
export PATH="/path/to/your/command:$PATH"
```

将`/etc/sudoers`文件，中的`Defaults env_reset`改为`Defaults !env_reset`取消采用默认 PATH 变量，然后在.bashrc 中最后添加`alias sudo='sudo env PATH=$PATH'`，这样 sudo 执行命令是就会使用系统的 PATH 变量，而不是默认 PATH 变量

```shell title="解决方法 2"
sudo vim /etc/sudoers
Defaults !env_reset
```

```shell
vim ~/.bashrc
alias sudo='sudo env PATH=$PATH'
```

### sh: 0: getcwd() failed: No such file or directory

    一般来说是因为你 cd 到了某个目录之后 rm 了这个目录，这时去执行某些 service 脚本的时候就会报 get cwd 错误。 只需要 cd 到任何一个实际存在的目录下再执行就好了

### Could not load the Qt platform plugin “xcb“

经过一番深入的探索，最终找到了一个有效的解决方案，即通过以下命令安装所有与 libxcb 相关的库：

```shell
sudo apt install libxcb-*
```

这条命令会安装所有以 libxcb 为前缀的库，确保系统中所有与 XCB 相关的依赖项都被正确安装。这一步成功解决了 Qt 无法加载 xcb 插件的问题，程序也顺利启动并运行。这表明，问题的根源在于某些关键的 XCB 依赖项缺失，而通过这种“一网打尽”的方式，我们可以确保所有相关的依赖项都得到满足。

### sudo: 无法解析主机：xxxxxx

原因：修改了主机的 ubuntu 设备名称，后面没有配置好 hosts 文件，导致 linux 无法解析到您的主机地址

解决方案：就是配置一下 hosts 文件就可以解决，具体操作如下：

```shell
sudo vim /etc/hosts
```

把下面的数字后面的 xxxx 修改成你现在的设备名称保存就可以了。

```text
127.0.1.1       xxxx
```

### dpkg: error processing package ***

[原文链接](https://blog.csdn.net/dou3516/article/details/105120221)

```text title="报错信息"
dpkg: error processing package ***

subprocess installed post-installation script returned error exit status 127
```

这主要是由于不完全安装导致的。解决方式是删除或编辑安装信息文件。

```shell title="粗暴方法一：删除所有信息之后 update" hl_lines="1-2"
sudo mv /var/lib/dpkg/info/ /var/lib/dpkg/info_old/
sudo mkdir /var/lib/dpkg/info/
sudo apt-get update
```

```shell
sudo apt-get install ***
```

## 装机 - 系统配置

### 换源

```shell
lsb_release -a
uname -a
```

```shell
vim /etc/apt/sources.list
```

!!! tip "注意换源的时候注意备份之前的"
    ```shell
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
    ```

=== "鱼香 ros"
    ```shell
    wget http://fishros.com/install -O fishros && bash fishros
    ```

=== "清华源"
    [ubuntu | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

    ```shell
    estricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    ```

=== "aliyun 源"
    [ubuntu镜像\_ubuntu下载地址\_ubuntu安装教程-阿里巴巴开源镜像站](https://developer.aliyun.com/mirror/ubuntu)

    ```shell
    deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
    ```

=== "ustc 源"

    ```
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted univ# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main rerse multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
    ```

=== "zju"

    ```shell
    deb https://mirrors.zju.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.zju.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.zju.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.zju.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    ```
    

```shell
sudo apt-get update
sudo apt-get upgrade
```

!!! failure "404"
    [Ubuntu 换源后仍然报错：404、没有 Release 文件\_没有release文件所以禁用-CSDN博客](https://blog.csdn.net/ys743276112/article/details/127436835)
    [sudo apt-get update 命令出现没有Release文件问题解决\_debian apt get update 没有release 文件-CSDN博客](https://blog.csdn.net/A18040554844/article/details/110099737)

    另外的解决方法，拉取https问题
    ```shell
    sudo apt install apt-transport-https
    sudo apt install ca-certificates
    ```

### 中文系统

在系統中添加中文語言，既可以顯示中文，也可以輸入中文。

Fcitx：谷歌拼音、搜狗拼音、搜狗五笔拼音
IBus：智能拼音，五笔（86 版）
XIM：略 (现在用的相对比较少)

```shell
sudo apt-get update
sudo apt-get install fcitx-bin

sudo apt-get install fcitx-table 
sudo apt-get install fcitx-table-all
```

[在 Ubuntu20.04 中安装中文输入法 - 知乎](https://zhuanlan.zhihu.com/p/529892064)

### PS1 修改

```shell
vim ~/.bashrc
```

## 装机 - 开发环境

- tldr：简易版 man 手册
- fd-find：人性化的 find
- rg(ripgrep)：快速搜索
- fzf：模糊搜索

### git

```shell
apt-get install git
```

### vim

```shell
apt-get install vim
```

### 安装软件的一些常见命令

```shell
sudo dpkg -i xxx.deb
```

```shell
tar -xzvf xxxx.tar.gz
```

### terminator

[terminator](https://blog.csdn.net/learning_tortosie/article/details/102581261)

```shell
sudo apt-get install terminator
```

!!! bug "设置为默认终端"

|开启 or 关闭快捷键 | 作用|
|---|---|
|`Ctrl + Shift + O`| 水平分割终端（分成上下两个窗口）|
|`Ctrl + Shift + E`| 垂直分割终端（分成左右两个窗口）|
|`Ctrl + Shift + W`| 关闭当前终端|
|`Ctrl + Shift + X`| 放大（还原）当前终端|
|`Ctrl + Shift + G`| 清屏|
|`Ctrl + Shift + Q`| 关闭所有终端（退出程序）|
|`Ctrl + Shift + T`| 开一个新终端|

|快捷键 | 作用|
|---|---|
|`alt+方向键` or `ctrl+TAB`|切换窗口|
|`ctrl shift +`|加字号|
|`F11`|全屏|
|`super(win) + g`|group，将不同窗口打包，指令可以广播|
|`Super+Shift+g`|取消分组|
|`ctrl+shift+f`|搜索命令|
|`Ctrl+Shift+c`|复制指令|
|`Ctrl+Shift+v`|粘贴指令|
|`Ctrl+Shift+X`|    将分割的某一个窗口放大至全屏使用|
|`Ctrl+Shift+Z`|    从放大至全屏的某一窗口回到多窗格界面|

### SSH

```shell
sudo apt install net-tools
```

```shell
ifconfig
```

```shell
sudo apt-get install openssh-server
ssh user@remote
ssh -X ldz@192.168.0.1  # 带图形化界面
ssh -p 1234 ldz@192.168.0.1 # 指定端口
```

```shell
vim /etc/ssh/sshd_config
```

- 第 33 行：将 PermitRootLogin without-password（第 33 行）改为 PermitRootLogin yes 并去掉前面的注释符号（#）
- 第 57 行:#PasswordAuthentication yes(第 57 行) 的注释去掉，如果是 no 就改为 yes
- 保存

```shell
service ssh restart
```

**验证安装**

```shell
service ssh status
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__settings-linux.assets__20240711175232.webp)

**开机自启动**

```shell
update-rc.d ssh enable
```

**配置免密登陆**

```shell
ssh-keygen -t rsa
```

然后根据提示一步步的按 enter 键即可（其中有一个提示是要求设置私钥口`passphrase`，不设置则为空，这里看心情吧，如果不放心私钥的安全可以设置一下）

执行结束以后会在`/home/当前用户` 目录下生成一个 `.ssh` 文件夹，其中包含私钥文件 `id_rsa` 和公钥文件 `id_rsa.pub`。

ssh-copy-id 会将公钥写到远程主机的 `~/.ssh/authorized_key` 文件中

```shell
ssh-copy-id name@ip
```

注意，windows 的 cmd 中不能直接执行 ssh-copy-id 命令，可以使用 git bash 或者其他 linux 终端工具

当出现
> Number of key(s) added: 1
> Now try logging into the machine, with:   "ssh 'HAHA@127.0.0.1'" and check to make sure that only the key(s) you wanted were added.

说明配置成功！

[深入理解\~/.ssh/config 和/etc/ssh/ssh\_config 配置文件 - 百度开发者中心](https://developer.baidu.com/article/details/2922032)

!!! failure "错误与解决方法"
    === "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!"
        警告：远程主机标识已更改！

        此报错是由于远程的主机的公钥发生了变化导致的。 ssh服务是通过公钥和私钥来进行连接的，它会把每个曾经访问过计算机或服务器的公钥（public key），记录在~/.ssh/known_hosts 中，当下次访问曾经访问过的计算机或服务器时，ssh就会核对公钥，如果和上次记录的不同，OpenSSH会发出警告。

        ```shell title="解决方法"
        ssh-keygen -R XX.XX.XX.XX 
        ```
    
    === "连接IPV6地址"
        ```shell
        ssh -6 user@ipv6
        ```

### X11 设置 GUI

1.修改配置文件：

```shell title="修改配置文件"
sudo vim /etc/ssh/sshd_config
```

添加或者取消注释以下两行代码

```shell
X11Forwarding yes
X11DisplayOffset 10
```

2.安装 xauth：

```shell title="安装 xauth"
sudo apt install xauth
```

3.重启 ssh 服务：

```shell title="重启 ssh 服务"
sudo service ssh restart
```

!!! note "-X 和-Y 的区别"
    [xorg - What is the difference between \`ssh -Y\` (trusted X11 forwarding) and \`ssh -X\` (untrusted X11 forwarding)? - Ask Ubuntu](https://askubuntu.com/questions/35512/what-is-the-difference-between-ssh-y-trusted-x11-forwarding-and-ssh-x-untrusted-x11-forwarding)

    if you use `ssh -X remotemachine` the remote machine is treated as an untrusted client. So your local client sends a command to the remote machine and receives the graphical output. If your command violates some security settings you'll receive an error instead.

    But if you use `ssh -Y remotemachine` the remote machine is treated as a trusted client. This last option can open security problems. Because other graphical (X11) clients could sniff data from the remote machine (make screenshots, do keylogging and other nasty stuff) and it is even possible to alter those data.

### conda

[conda 换地址](https://blog.csdn.net/chengjinpei/article/details/119835339)

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

如果出现了错误，有可能是因为使用的是‵sh`的原因。

进入

```shell
vi Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```

把第一行从 ‵#!/bin/sh`改成

```shell
#!/bin/bash
```

### node

使用 fishros 进行安装

```shell
npm install --global yarn
```

```shell
yarn --version
```

## 装机 - 通用软件

### chorme

```shell title="installment"
sudo apt install chromium-browser
```

```shell title="verify"
chromium-browser --version
```

### vscode

可以使用 fishros 进行安装

[vscode on Kali](https://blog.csdn.net/CM_STC89C52/article/details/127296320)

1. 用内嵌的浏览器搜索 vscode，下载 vscode 的.deb 格式的安装包
2. 在终端中输入 `sudo dpkg -i code_1.72.1-1665423861_amd64.deb` 进行解压包
3. 在 vscode 软件上点击鼠标右键，点击 `Edit Application`
4. 有个 Command 选项，输入 `/usr/share/code/code --unity-launch %F --no-sandbox` 即可，再点击保存。

### wechat

[Weixin for Linux](https://linux.weixin.qq.com/en)

### typora
>
> 参考[Ubuntu22.04 环境下使用 Typora\_typora ubuntu-CSDN 博客](https://blog.csdn.net/weixin_73546177/article/details/132033297)
> [WittonBell/typoraCracker: A patch and keygen tools for typora.](https://github.com/WittonBell/typoraCracker)

```shell title="官网教程"
wget -qO - https://typora.io/linux/public-key.asc | sudo tee /etc/apt/trusted.gpg.d/typora.asc
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt update
# install typora
sudo apt install typora
```

我下载的二进制文件，没有用这个

### picgo

[Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo?tab=readme-ov-file):rocket:A simple & beautiful tool for pictures uploading built by vue-cli-electron-builder

```shell
cd Picgo
```

```shell
npm i @vue/cli-service
```

[ubuntu PicGo 安装和腾讯云图床配置，超详细！！！-CSDN 博客](https://blog.csdn.net/qq_42584874/article/details/116534328)

### todesk

[ToDesk 远程桌面软件 - 免费安全流畅的远程连接电脑手机](https://www.todesk.com/linux.html)

- arm [download](https://dl.todesk.com/linux/todesk-v4.7.2.0-arm64.deb)

```shell
sudo apt-get install libappindicator3-1

sudo apt-get install ./todesk-v4.7.2.0-arm64.deb
```

```shell
todesk
```

### jupyter

```shell
pip install jupyter jupyterlab
sudo reboot
```

```shell title="生成配置文件"
jupyter lab --generate-config
```

设置开机启动

```shell
sudo vim /etc/systemd/system/jupyter-lab.service
```

```shell
[Unit]
Description=Jupyter Lab Server
After=network.target

[Service]
Type=simple
User=usslab
WorkingDirectory=/home/<name>/
ExecStart=/<path>/jupyter-lab --port 8888 --no-browser

[Install]
WantedBy=multi-user.target
```

```shell title="启动服务"
sudo systemctl enable jupyter.service
sudo systemctl start jupyter.service
```

```shell title="检查服务"
sudo systemctl status jupyter.service
```

访问 `localhost:8888`即可看到，如果有公网的 ip 也可以访问到

### 坚果云
>
> 参考帖子 [记录 Ubuntu22.04 安装坚果云](https://blog.csdn.net/weixin_45788868/article/details/140736624) 感谢

```shell
wget https://www.jianguoyun.com/static/exe/installer/nutstore_linux_src_installer.tar.gz
```

```shell
sudo tar zxf nutstore_linux_src_installer.tar.gz
```

```shell
cd nutstore_linux_src_installer
```

```shell
sudo ./update-toolchain.sh
```

!!! question "这里我报错了，少一个库"
    没搞明白，就全装了

    ```shell
    sudo aptitude install libnautilus-extension4
    sudo aptitude install libnautilus-extension1a
    sudo aptitude install libnautilus-extension-dev
    ```     

```shell
sudo ./configure
```

```shell
sudo make
```

```shell
sudo make install
```

```shell title="download other things"
./runtime_bootstrap
```

直接按 1

[坚果云 linux 命令行 • Worktile 社区](https://worktile.com/kb/ask/422312.html)

webDAV 的使用

[用命令行在 Linux 同步坚果云 | Practice](https://tobyqin.cn/posts/2019-05-06/jianguoyun-command-line/)

```shell title="登录坚果云账号"
nutstore login
```

```shell title="退出坚果云账号"
nutstore logout
```

```shell title="查看当前已经同步的文件和文件夹"
nutstore list sync
```

```shell title="同步指定的文件或文件夹"
nutstore sync <文件或文件夹路径>
```

```shell title="取消同步指定的文件或文件夹"
nutstore unsync <文件或文件夹路径>
```

```shell title="查看同步状态"
nutstore status
```

```shell title="上传文件或文件夹到坚果云"
nutstore upload <文件或文件夹路径>
```

```shell title="下载文件或文件夹"
nutstore download <文件或文件夹路径>
```

```shell title="删除坚果云上的文件或文件夹"
nutstore delete <文件或文件夹路径>
```

```shell title="创建文件夹"
nutstore mkdir <文件夹路径>
```

```shell title="查看文件或文件夹的详细信息"
nutstore info <文件或文件夹路径>
```

```shell title="查看账号信息"
nutstore account
```

```shell title="查看帮助信息"
nutstore help
```

## VMware

!!! warning "VMware Workstation v17.x 永久许可证激活密钥："

    不知道能不能用
    ```
    MC60H-DWHD5-H80U9-6V85M-8280D
    4A4RR-813DK-M81A9-4U35H-06KND
    NZ4RR-FTK5H-H81C1-Q30QH-1V2LA
    JU090-6039P-08409-8J0QH-2YR7F
    4Y09U-AJK97-089Z0-A3054-83KLA
    ```

### 安装 VMware Tools 选项显示灰色的正确解决办法  

1.关闭虚拟机；  

2.在虚拟机设置分别设置 CD/DVD、CD/DVD2 和软盘为自动检测三个步骤；  

3.再重启虚拟机，灰色字即点亮。

4.重新安装 vmware-tools  

- 虚拟机无法打开

> 虚拟机使用的是此版本 [VMware](https://so.csdn.net/so/search?q=VMware&spm=1001.2101.3001.7020) Workstation 不支持的硬件版本。
> 模块"Upgrade"启动失败。

打开`.vmx`文件，修改`virtualHW.version = "19"`一行至`virtualHW.version = "16"`
