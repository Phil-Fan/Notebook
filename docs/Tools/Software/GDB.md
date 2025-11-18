# gdb

[【Linux】GDB 保姆级调试指南（什么是 GDB？GDB 如何使用？）\_linux gdb 标准输入-CSDN 博客](https://blog.csdn.net/weixin_45031801/article/details/134399664)

## 原理

### 调试模式

○ 调试器执行模式
○ attach 模式
○ remote 模式

## 安装

```shell
sudo apt install gdb
```

### 20.04 安装`gdb 10.2`

注意 gdb10.2 需要 c++11 语法，需要安装 g++

```shell title="下载安装包"
wget https://ftp.gnu.org/gnu/gdb/gdb-10.2.tar.xz
```

```shell title="解压缩"
tar -xvzf gdb-10.2.tar.xz
```

!!! question "我这里报了`gzip: stdin: not in gzip format tar: Child returned status 1 tar: Error exit delayed`"
    ```shell title="解压缩换成这个命令"
    tar -vxf gdb-10.2.tar.xz
    ```
    tar包压缩的时候用`-cvf`参数，解压的时候用`-xvf`参数（用此命令解决了）

    或压缩的时候用`-czvf`参数，解压的时候用`-xzvf`参数（常用，这次报了这个错）

    ** 解决方法二** (未验证)

    对压缩包进行重命名，再解压：

    ```shell
    mv memcached-1.4.34.tar.gz memcached-1.4.34.tar
    ```

    ```shell title="再进行解压"
    tar -zvxf gdb-10.2.tar
    ```

    因为后缀名可能原来就是 memcached-1.4.34.tar，被改过~

进入解压之后的目录

```shell
cd gdb-10.2
```

```shell title="配置"
mkdir build
cd build
```

```shell title="配置"
../configure --enable-tui
```

!!! question "可能会提示你没有相关库 `configure: WARNING: no enhanced curses library found; disabling TUI`"
    查阅官方发现：Build GDB with the text-mode full-screen user interface (TUI).Requires a curses library (ncurses and cursesX are also supported).

    你需要安装ncurses库，才能安装tui。[参考 configure: WARNING: no enhanced curses library found; disabling TUI](https://www.linuxquestions.org/questions/linux-newbie-8/configure-warning-no-enhanced-curses-library-found%3B-disabling-tui-4175443971/)

    
    [Index of /pub/gnu/ncurses](https://ftp.gnu.org/pub/gnu/ncurses/)

    ```shell title="下载"
    wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.2.tar.gz
    ```

    ```shell title="解压缩"
    tar xzf ncurses-6.2.tar.gz
    ```

    ```shell title="进入目录"
    cd ncurses-6.2
    ./configure --prefix=/opt/ncurses
    make
    sudo make install
    ```

!!! question "`‘makeinfo‘ is missing on your system.`"
    ```shell
    sudo apt-get install texinfo
    ```

```shell title="编译"
make
```

```shell title="安装"
sudo make all install
```

退出这个 shell

```shell title="查看版本"
gdb -v
```

## gdb 插件

### pwndbg

[github.com/pwndbg/pwndbg](https://github.com/pwndbg/pwndbg)

```shell title="安装 pwndbg 插件"
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

这里可能会冒出一些安装上的错误，一般都是网络问题，调整网络后即可

```shell
cat .gdbinit
```

不仅有 pwndbg，还有 pwngdb！！！
有一些指令需要两个都安装

[Pwngdb/README.md at master · scwuaptx/Pwngdb](https://github.com/scwuaptx/Pwngdb/blob/master/README.md#features)

```shell
cd ~/
git clone https://github.com/scwuaptx/Pwngdb.git 
cp ~/Pwngdb/.gdbinit ~/ 
```

[gdb 与 peda、pwngdb、pwndbg 组合安装与使用\_gdb peda-CSDN 博客](https://blog.csdn.net/whbing1471/article/details/112410599)

### gef

[hugsy/gef: GEF (GDB Enhanced Features)](https://github.com/hugsy/gef)

[gdb exhanced features(GEF) 工具的使用](https://www.cnblogs.com/liulianzhen99/articles/17824258.html)

```shell
# 安装
git clone https://github.com/hugsy/gef
cp gef/gef.py ~/.gdbinit-gef.py
echo source ~/.gdbinit-gef.py >> ~/.gdbinit
# 调用 gef，直接通过 gdb 命令就会默认加载 gef 插件
gdb
# 就会出现带 gef>的界面了
gef➤
```

## 使用方法

○ 执行断点
○ 硬件断点
○ 查看寄存器 / 内存
○ set 修改寄存器 / 内存

```shell
run
start 在main之前临时断点

continue

step / s #单步

info register
info proc mapping

disassemble main/ disass main #反汇编

breakpoint *0x4005a0 #断点
b *0x4005a0
```

### 快捷指令

**enter 重复指令**

### 断点

`b(breakpoint) + 行号`—— 在那一行打断点

`b funcname` —— 在该函数的第一行打上断点

`b file_name:func_name`

`b +0x10`  //在程序当前停住的位置下 0x10 的位置下断点，同样可以 -0x10，就是前 0x10

`d(delete) + number` —— 删除一个断点【不可以 d + 行号】

`d + breakpoints` —— 删除所有的断点

`clear` //不加参数默认清除当前函数所在行的所有断点

- `clear function`//删除该函数内的所有断点
- `clear line`//删除该行的所有断点

`disable 5`//常用，禁用 5 号断点
`enable 5` //启用 5 号断点

### 查看类

l(list) 行号/函数名 —— 显示对应的 code，每次 10 行

`i` //info，查看一些信息，只输入 info 可以看可以接什么参数，下面几个比较常用

`i b` //常用，info break 查看所有断点信息（编号、断点位置）

`i r` //常用，info registers 查看各个寄存器当前的值

`i f` //info function 查看所有函数名，需保留符号

breakpoint already hit 1 time【此断点被命中一次】

bt —— 看到底层函数调用的过程【函数压栈】

undisplay + 变量名编号 —— 取消对先前设置的那些变量的跟踪

`show` //和 info 类似，但是查看调试器的基本信息，如：
`show args` //查看参数

`rdi` //常用，+寄存器名代表一个寄存器内的值，用在地址上直接相当与一个十六进制变量

### 打印类指令

```shell
# 打印函数名地址
p fun_name 

# 计算表达式
p 0x10-0x08

# 查看变量地址
p &a 

# 查看指定内存地址的值
p *(0x123456)

# 显示寄存器值
p $rdi

# 显示寄存器指向的值 
p *($rdi)
```

### 反汇编指令

```shell
# 显示指定地址前后的汇编代码
disass 0x123456

# 显示 10 条汇编指令
x /10i $pc
```

display —— 跟踪查看一个变量，每次停下来都显示它的值【变量/结构体…】

### 修改数据指令

```shell
# 修改寄存器值
set $rdi=0x10

# 修改指定内存地址的值
set *(0x123456)=0x10

# 设置程序运行参数
set args "abc" "def" "gh"

# 使用 python 设置包含不可见字符的参数
set args "python -c 'print "1234\x7f\xde"'"
```

### 运行类

`r(run)` —— F5【无断点直接运行、有断点从第一个断点处开始运行】

`n(next)` —— 逐过程，遇到调用函数要跟进【相当于 F10，为了查找是哪个函数出错了】

`s(step)`—— 逐语句，遇到调用函数不跟进【相当于 F11】

`c(continue)` —— 运行至下一个断点处【VS 下不断按 F5】

set var —— 修改变量的值

## 自动化脚本

[GDB 自动化脚本编写笔记一\_gdb 脚本-CSDN 博客](https://blog.csdn.net/kelxLZ/article/details/112411761)

[用 gdb 脚本进行自动化调试\_gdb 本来就支持自定义脚本辅助调试-CSDN 博客](https://blog.csdn.net/nirendao/article/details/105910753)

1. 井号 # 表示注释

2. set

执行方法

- interactive 界面

```shell
(gdb) file test.exe 
(gdb) source mycmd.gdb 
```

- 在命令行中运行 gdb 的 batch 模式命令

```shell
gdb --batch --command=cmd.gdb --args test.exe <add necessary parameters here> 
```

### `.gdb`脚本

使用`.gdb`脚本进行自动调试

`run`命令可以接受输入重定向
`run < input.txt`

```shell
set logging file output.log
set $i = 0
while $i < 100
  run < count.txt
  set logging enabled on
  p $eax
  set logging enabled off
  set $i = $i + 1
end
```

函数声明语法

```shell
define func_name
    <body>
end
```

```shell
document func_name
# write documents here 
end
```

1> 设置 gdb 的一些选项的值，如前面提及的 pagination 等

如果要查看当前的值，可以使用 show 命令，比如：show pagination

2> 创建调试使用的变量

```shell
set $a = i 
```

不带$的变量是被调试程序中的变量，如这里的 i；带$的变量为调试过程中定义的变量，如这里的$a
所有在 gdb 中创建的变量都是全局的

其他的例子还有：

```shell
(gdb) set $i = (char *)("Hello")

(gdb) print $i
$1 = 0x7ffff7fddf00 "Hello"

(gdb) printf "%s\n", $i
Hello
```

3> 访问寄存器

```shell
set $a = $eax
p $a
```

4> 修改寄存器

```shell
set $eax = 5
```

5> 修改内存

```shell
set *(unsigned char *)$addr = 0x90
```

打印语句

```shell
echo Hello\n

printf "a=%d\n", 10
```

条件语句

```shell
# e.g. if i == 10
if <condition>
    # do something 
else 
    # do other things 
end 
```

循环语句

```shell
while <condition> 
    # do something 
end
```

```shell
set $i = 10
while $i > 0
    printf "%d\n", $i 
    set $i = $i - 1
end
```

在 breakpoint 处执行调试语句
这一点是很常用的，尤其是在调试 for 循环的时候。
先看一个最简单的实例

```shell
break function_name
    command 1
    backtrace
    continue
end
```

### python
