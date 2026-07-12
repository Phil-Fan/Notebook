# Reverse

| 序号 | 架构 | 特点 | 代表性的厂商 | 运营机构 | 发明时间 |
| ---- | ------- | -------------------- | --------------------- | ------------- | -------- |
| 1 | X86 | 性能高，速度快，兼容性好 | 英特尔，AMD | 英特尔 | 1978 年 |
| 2 | ARM | 成本低，低功耗 | 苹果，谷歌，IBM，华为 | 英国 ARM 公司 | 1983 年 |
| 3 | RISC-V | 模块化，极简，可拓展 | 三星，英伟达，西部数据 | RISC-V 基金会 | 2014 年 |
| 4 | MIPS | 简洁，优化方便，高拓展性 | 龙芯 | MIPS 科技公司 | 1981 年 |

!!! note "笔记来源：短学期课程 ppt，可能有转写错误，请注意鉴别"

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240714181857.webp)

[智云链接](https://interactivemeta.cmc.zju.edu.cn/#/replay?course_id=63047&sub_id=1213368&tenant_code=112)

## 程序？可“执行”文件

为什么计算机可以执行给定的程序呢？
因为任何程序都将最终转化为「指令」的形式由计算机执行

1 word = 2 Bytes
Dword = 4 Bytes = int

!!! bug "寄存器有哪些"
    eax
    edx

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707201856.webp)

AST：抽象代码树
IR：中间表达式

=== "编译执行"
    上述通过编译器 (compiler) 将代码转化为机器指令格式的程序，进而执行
    ![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707202333.webp)

=== "解释执行"
    通过解释器 (interpreter) 将代码转化为 VM 格式的程序（如字节码），进而在 VM上执行；更安全，但更慢
    ![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707202320.webp)

可执行文件

- Windows: PE/PE32+ (Port Executable)

- Mac: Mach-O (Mach Object)

- Linux: ELF (Executable and Linkable Format)

## ELF

[ELF 文件头](https://www.cnblogs.com/jiqingwu/p/elf_explore_2.html)

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20241118193116.webp)

```text
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x1050
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14768 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         11
  Size of section headers:           64 (bytes)
  Number of section headers:         29
  Section header string table index: 28
```

!!! note "通过命令行工具静态检视 ELF 文件"
    - file:输出文件的基本信息
    ```
file xxx
    ```
    - objdump:看指令代码
    ```shell title="看汇编代码"
    objdump -d xxx
    ```
    - readelf

## ELF 的编译 Complier

[详解三大编译器：gcc、llvm 和 clang - 知乎](https://zhuanlan.zhihu.com/p/357803433)

[GCC - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/GCC#%E4%BC%98%E5%8C%96)

[GNU 计划 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/GNU%E8%A8%88%E5%8A%83)

GCC(GNU Compiler Collection) 即 GNU 编译器套件，属于一种编程语言编译器，其原名为 GCC（GNU C Compiler）即 GNU c 语言编译器

gcc（GUN C Compiler）是 GCC 中的 c 编译器，而 g++（GUN C++ Compiler）是 GCC 中的 c++ 编译器。

gcc 和 g++ 两者都可以编译 c 和 cpp 文件，但存在差异。gcc 在编译 cpp 时语法按照 c 来编译但默认不能链接到 c++ 的库（gcc 默认链接 c 库，g++ 默认链接 c++ 库）。g++ 编译.c 和.cpp 文件都统一按 cpp 的语法规则来编译。所以一般编译 c 用 gcc，编译 c++ 用 g++。

```shell
gcc/clang hello.c
```

保留所有中间文件

```shell
clang -save-temps hello.c -o hello.elf
```

!!! note "常用参数"
    - `-o <file>`: 指定输出的文件名。
    - `-c`: 只编译不链接，生成目标文件 (.o)。
    - `-S`: 只编译不链接，生成汇编代码。
    - `-E`: 只进行预处理，不进行编译、汇编和链接。
    - `-g`: 生成调试信息。
    - `-Wall`: 开启所有警告信息。
    - `-O, -O1, -O2, -O3`: 设置不同的优化级别，-O2 为默认值。
    - `-I <dir>`: 添加头文件搜索目录。
    - `-L <dir>`: 添加库文件搜索目录。
    - `-l<library>`: 链接指定的库文件。
    - `-static`: 使用静态链接。
    - `-shared`: 生成共享库。
    - `-m32` / `-m64`: 指定生成代码的目标平台是 32 位还是 64 位。
    - `-std=<standard>`: 指定使用的 C/C++ 标准，如`-std=c99`或`-std=c++11`。

AST：抽象代码树

```shell
clang -Xclang -ast-dump -S hello.c 
```

IR：中间表达式

```shell
clang -Xclang -emit-llvm -S hello.c -o hello.ll
```

```shell
gcc -fdump-tree-all -S hello.c
```

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707210444.webp)

Assemble

编译后端

- 从 LLVM IR 生成目标代码
  
```shell
llc hello.ll -o hello.s
```

- 从汇编文件到目标文件

```shell
llvm-mc -filetype=obj hello.s -o hello.o
```

- 一步到位

```shell
llc -filetype=obj hello.ll -o hello.o
```

```bash
as [options] -o outputfile inputfile
```

!!! note "代码和数据分开存放"
    并且设置为只读状态

## ELF 链接

把已有的目标文件和库目标文件或别的目标文件链接在一起，生成一个可执行文件

使用`file`指令查看`.o` 文件，会发现是 reallocatable，是需要重定向的，需要把程序中留白的部分补充上

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707210812.webp)

> 需要知道 printf 函数在哪里，才能正确的调用 printf 函数

GNU linker

```shell
ld hello.o -o hello
```

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707215122.webp)

- 静态链接：处理更快，但文件更大

> 把所有需要的文件都链接到一个 elf 当中，不存在外部符号

- 动态链接：处理更慢，文件小

> 电脑上只存一个 printf，需要的时候去链接

- PLT: Procedure Linkage Table

> 动态链接中的实现细节

- GOT: Global Offset Table
- lazy binding optimization 以及 full-relro 保护

!!! tip "保护技术 1"
    lazy binding 比较危险，可能会被劫持

程序的执行

```shell title="查看链接了什么东西"
ldd hello.elf
```

- libc:linux 中最重要的库函数（类似于 stdio.h）
- ld 程序的加载器

> 编译执行的程序不需要一个解释器，但需要一个加载器

```text
linux-vdso.so.1 (0x00007fff45b18000) #虚拟动态共享对象
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9bddd66000) #libc
/lib64/ld-linux-x86-64.so.2 (0x00007f9bddf69000) #动态链接器
```

通过指定 loader 来执行程序

```shell title="真正执行的指令 "
/lib64/ld-linux-x86-64.so.2 ./hello
```

libc 及其版本
糟糕的不向前兼容

## ELF 的装载、运行

程序 to 进程

进程有自己的 pid 号

```shell
pidof xxx
```

我们就可以进入到`\proc\'pidof xxx'\maps`这个文件下看它的内存映射

???+note "内存映射"
    动态链接程序需要把自己的loader和libc都映射好
    可以看到，既有这里相当于创建了一些映射，包括libc和ld

    真正地址 + 权限 + 内存

    静态链接把自己链接到内存就可以了

    ```shell
    55f232470000-55f232471000 r--p 00000000 08:01 919328                     /root/Desktop/CTF/Rev/echo
    55f232471000-55f232472000 r-xp 00001000 08:01 919328                     /root/Desktop/CTF/Rev/echo
    55f232472000-55f232473000 r--p 00002000 08:01 919328                     /root/Desktop/CTF/Rev/echo
    55f232473000-55f232474000 r--p 00002000 08:01 919328                     /root/Desktop/CTF/Rev/echo
    55f232474000-55f232475000 rw-p 00003000 08:01 919328                     /root/Desktop/CTF/Rev/echo
    55f23369b000-55f2336bc000 rw-p 00000000 00:00 0                          [heap]
    7fd593c36000-7fd593c39000 rw-p 00000000 00:00 0 
    7fd593c39000-7fd593c5f000 r--p 00000000 08:01 4065513                    /usr/lib/x86_64-linux-gnu/libc.so.6
    7fd593c5f000-7fd593db6000 r-xp 00026000 08:01 4065513                    /usr/lib/x86_64-linux-gnu/libc.so.6
    7fd593db6000-7fd593e0b000 r--p 0017d000 08:01 4065513                    /usr/lib/x86_64-linux-gnu/libc.so.6
    7fd593e0b000-7fd593e0f000 r--p 001d1000 08:01 4065513                    /usr/lib/x86_64-linux-gnu/libc.so.6
    7fd593e0f000-7fd593e11000 rw-p 001d5000 08:01 4065513                    /usr/lib/x86_64-linux-gnu/libc.so.6
    7fd593e11000-7fd593e1e000 rw-p 00000000 00:00 0 
    7fd593e35000-7fd593e37000 rw-p 00000000 00:00 0 
    7fd593e37000-7fd593e38000 r--p 00000000 08:01 4065507                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    7fd593e38000-7fd593e5d000 r-xp 00001000 08:01 4065507                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    7fd593e5d000-7fd593e67000 r--p 00026000 08:01 4065507                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    7fd593e67000-7fd593e69000 r--p 00030000 08:01 4065507                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    7fd593e69000-7fd593e6b000 rw-p 00032000 08:01 4065507                    /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
    7ffd9ca1d000-7ffd9ca3e000 rw-p 00000000 00:00 0                          [stack]
    7ffd9cb5f000-7ffd9cb63000 r--p 00000000 00:00 0                          [vvar]
    7ffd9cb63000-7ffd9cb65000 r-xp 00000000 00:00 0                          [vdso]
    ```

不同的映射是不同的权限，比如说代码段是只读的，堆是可读可写的

!!! tip "保护技术 2"
    写和执行不能同时有，否则会有注入漏洞

execve 系统调用：特别的 libc 函数

- 先把程序 fork 一下，再通过 execve 替换

```shell
int execve(const char *filename, char *const argv[], char *const envp[]);
```

程序执行的起点和终点并不是 main 函数，c++ 有 construct 等特性可以在 main 之前就调用
[Function Attributes - Using the GNU Compiler Collection (GCC)](https://gcc.gnu.org/onlinedocs/gcc-4.1.2/gcc/Function-Attributes.html)

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240707223320.webp)

内核以可执行文件 e_entry 位置 (即_start) 作为起点

!!! note "_start"
    <https://codebrowser.dev/glibc/glibc/sysdeps/x86_64/start.S.html#_start>
    - glibc 代码 (汇编构筑)
    - 携带 *main* 符号跳转 *__libc_start_main* 函数

!!! note "*__libc_start_main*"
    <https://codebrowser.dev/glibc/glibc/csu/libc-start.c.html#234>
    - 完成各类和目标 ELF 有关的初始化
    - 内联 *__libc_start_call_main*
    - 最终跳往 main 符号
    - main 结束后调用 exit

!!! tip "保护技术 3——基地址与 ASLR"
    程序开始的地方每次都是随机的

    动态链接程序可以通过ASLR，让内存映射随机化，每次都从不同的位置起始

## ELF 的交互、调试

- 绝对路径 / 相对路径
  - -h / --help
  - manual
  - PATH 路径

通过虚拟机或者沙箱进行交互

- <https://firejail.wordpress.com/>
- <https://github.com/google/nsjail>

通过编程与程序交互

- 重定向构建特殊字符作为输入
- C 管道编程
- python subprocess 库
- python pwntools 库

调试工具

- `strace`：追踪系统调用 (操作系统提供给程序的库)

- `ltrace`：追踪调用的库（只对动态链接程序有用）

### gdb: GNU debug

- 调试模式
  - 调试器执行模式
  - attach 模式
  - remote 模式

- 常用调试功能
  - 执行断点
  - 硬件断点
  - 查看寄存器 / 内存
  - set 修改寄存器 / 内存

● gdb 插件

```shell
run
start # 在 main 之前临时断点

continue

step / s # 单步

info register
info proc mapping

disassemble main/ disass main #反汇编

breakpoint *0x4005a0 #断点
b *0x4005a0
```

## ELF 的逆向

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240708181631.webp)

- Bad Aspect 外挂、注册机
- Good Aspect：未知攻，焉知防

### **反汇编**

机器指令 => 汇编指令（查表、准确）

- objdump

### **反编译**

汇编指令 => 编程语言（分析/特征匹配/启发式、往往不准确）

- IDA Pro (<https://hex-rays.com/ida-pro/> )
- Binary Ninja (<https://binary.ninja> )with free version
- Ghidra (<https://github.com/NationalSecurityAgency/ghidra> )
- Cutter / radare (<https://github.com/rizinorg/cutter> )
- 大语言模型 ;D <https://mlm.lingyiwanwu.com/>

对于符号恢复的静态 or 动态链接目标

- 关注特定常量和字符串
- 关注输入和输出函数
- 关注分支、比较指令
- 关注可能涉及加密解密的特殊运算（位运算、异或、取余）

「可运行」和「可调试」是高效解决逆向问题的必备

- 许多逆向赛题都需要「纯静态」的方式解决，程序可能依赖特定的架构/设备
- “if it can run, it can be cracked”
- 通过运行时的结果解决静态逆向时的疑惑

!!! note "题目给到的 main 函数不一定是真正的 main 函数"

### 动态示例

```shell
file crackme-ext
```

因为 shuffle 这个函数是一对一映射的，所以可以定向爆破

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240715101015.webp)

这里 call shuffle 就是调用 shuffle 函数，那么 B6E 就是 shuffle 函数的结束地址

## IDA

### 安装

1.免费下载网址

[IDA Free (hex-rays.com)](https://hex-rays.com/ida-free/#download)点击即可跳转。若无法跳转则随便一个搜索引擎搜索 IDA 即可跳出。

2.安装步骤

打开下载网站如下图，选择 download。

之后选择一个适合你的版本安装即可，我选择的是第一个

注意`.run`文件需要自己加一个可执行权限

```shell
chmod +x software.run
./software.run
```

### 窗口

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__image-20240530083905812.webp)

如上图所示，左侧窗口为函数列表窗口，右侧窗口为 IDA 反汇编所得的汇编代码，最下侧窗口为文件在反汇编过程中的信息。

菜单介绍

首先，进入 IDA 界面则可以看到如下菜单栏：

File：用于打开、新建、装载、保存、关闭一个文件或是数据库

Edit：用于编辑反汇编代码

Jump：用于跳转到某个位置、地址或是一个窗口

Search：用于搜索代码段、数据、错误等等

View：用于显示文件内容的显示方式

Debugger：调试器，集成在 IDA 中

Lumina：对元数据进行各种操作

Options：可以进行一些个性化的设置

#### 函数窗口（Functions window）

左侧是函数窗口，会将程序中所有的函数显示出来

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__image-20240530084316587.webp)

我们分析一道题目的时候一般是先从主函数开始

但是 main 一般不会显示出来，我们这时可以先搜索，用 Ctrl+F 快捷键

然后点击 main，即可跳转到 main 函数里

#### 汇编窗口（IDA View）

现在可见的是汇编窗口，展示的汇编代码，如图所示的是图形模式

我们可以按右键 选择 Text view 或者点击 空格键 进入文本模式

展示了一些地址和汇编代码

#### “十六进制窗口”（Hex View）

习惯讲是“十六进制窗口”，但将这个窗口称做“十六进制窗口”其实是一种误称，因为 IDA 十六进制窗口可以配置为显示各种格式，并可作为十六进制编辑器使用。默认情况下，十六进制窗口显示程序内容和列表的标准十六进制代码，每行显示 16 个字节，以及其对应的 ASCII 字符。和在反汇编窗口中一样，用户也可以同时打开几个十六进制窗口

### 快捷键

#### F5 - 伪代码（Pseudocode）

对着函数点**F5**即可弹出伪代码窗口

是将汇编语言，变成伪代码，即展示了一些类 c 代码

#### Shift+F5 字符串窗口

![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__49f8f206fe404029855de10cce91e1c2.webp)

#### Ctrl+X（交叉引用）

我们可以通过这个操作，可以判断哪些函数引用了这个字符串或数据

点击 ok，便会跳转到相应地方

#### G（跳转地址）

前面说过汇编窗口界面，左边是一些地址，右边是汇编代码

我们在浏览这些代码的过程中，往下往上翻页，可能找不到原来的地方了，或者有时候，你清楚地知道你想要导航的目的地址，但反汇编窗口中并没有可供双击导航的名称。这时我们就可以通过该操作跳转到相应的位置。

#### Alt+T（文本搜索）

IDA 文本搜索相当于对反汇编列表窗口进行子字符串搜索。

它将搜索限制于仅查找完整的词，并且能够匹配反汇编行中的任何完整的词，包括操作码助记符或常量

选择 Find all occurences（查找所有结果），IDA 将在一个新的窗口中显示搜索结果，你可以根

据搜索条件轻松导航到任何一个匹配结果。

#### N（重命名）

对于一些函数名，我们可以改为方便我们理解的函数名

如果不小心改错了怎么办？

#### / （注释操作）

在方框内添加注释，程序员必备，不多讲

### R | 常量标注 char

可以把一些常用的可见字符标注成`char`

右键即可
![image](https://img.philfan.cn/CS__CTF__assets__04-reverse.assets__20240715100010.webp)
