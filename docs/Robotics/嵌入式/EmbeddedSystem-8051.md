# 80C51

!!! note "学习路线"
 上课不要听，花两到三次课或者整块的空闲时间把[这一套课程](https://www.bilibili.com/video/BV1WK411W7HP)听完。讲的简洁易懂特别好。
 看完视频之后直接把作业做掉，实验做了，可以结合实验对所学知识有一个更深的了解。
    期末的时候再结合课件做补充。

- 重点理解
  - C51 资源分布：CPU 里边有哪些东西，代码放在哪里？变量放在哪里？怎么取出来
  - PC 指针及其作用
  - 存储器的分布，各个部分都是放什么的。SFR 中的各个寄存器可以控制单片机的各种资源
  - 最后了解汇编

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__8051.svg)

## 简介

- 什么是单片机

一台能够工作的计算机要有这样几个部份构成：**CPU（进行运算、控制）、RAM（数据存储）、ROM（程序存储）、输入/输出设备（例如：串行口、并行输出口等）**。

而在单片机中，这些部份全部被做到**一块集成电路芯片**中了，所以就称为单片机（单芯片）

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620231200675.webp" alt="image-20240620231200675" style="zoom:50%;" />

- 8 位 CPU
- 4K ROM 存放程序
- 128B RAM 存放数据
- IO 接口
- 2 个 16 位定时计数器
- 1 个全双工可编程串行口

数据总线、地址总线、控制总线：

## 结构

[单片机应用原理篇之 80C51 的 CPU_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1p54y1D7Ys)

### 引脚

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620231616616.webp)

> 缺口左侧是 1 号口

单片机的 40 个引脚大致可分为 4 类：

**电源、时钟、控制和 I/O 引脚。**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240228113806275.webp" alt="51单片机引脚图" style="zoom: 33%;" />

**电源引脚**：`Vcc` 40 脚:5V；`Vss` 20 GND

**控制引脚**：`RST` 9 高电平复位；`ALE`；

80C51 共有 4 个 8 位并行 I/O 端口：**P0,P1,P2,P3 口**,共 32 个引脚。

### CPU

**CPU 的位数**：8 位

**CPU 的作用**：取指令，译码，执行

CPU 的构成：

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620232832045.webp)

- 运算器

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620232944582.webp)

寄存器 B：乘除法

累加器 A：最繁忙的寄存器

PSW 程序状态字寄存器

- 控制器

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620233446761.webp)

- **程序计数器 PC**（16 位，24K），控制读取的代码；一开始指向 0000H，跳转到 30H 开始执行

```assembly
;30H开始放代码
MOV A,20H
MOV B,20H
MOV C,20H
```

- **数据指针寄存器 DPTR**（data pointer）;16 位，可寻址范围 64KB;指向外部 ROM 或 RAM 的地址指针

### **存储器构造**

看总线区分哈佛和冯诺依曼：数据总线和地址总线

- **哈佛结构** RAM 和 ROM 是分开的；独立结构；可以同时获得数据和代码

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620235824661.webp)

- **冯诺依曼结构** RAM 和 ROM 是相邻的，统一编址（分时）

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240620235816288.webp)

51 单片机是**改进哈佛结构**，分时复用，一套数据地址总线，通过指令的方式区分

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621000834024.webp" alt="image-20240621000834024" style="zoom:50%;" />

4 个物理存储空间，实际是 3 个逻辑存储空间；
地址总线是 16 位的，最大不可以超过 64K

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621002809377.webp" alt="image-20240621002809377" style="zoom:50%;" />

### 程序存储器 ROM | `READ ONLY MEMORY`

在 89C51 中的 ROM 是一种电可擦除的 ROM，称为 FLASH ROM

存放程序、表格常数；

在运行过程中只读不可写，掉电不丢失数据。

> EA 引脚，EA=1 方案 1，EA=0 方案 2
>
>- 方案 1:4K 以内地址在片内 ROM，大于 4K 的在片外 ROM
>- 方案 2：片内 ROM 禁用，全部存放在片外

| | |
| ----- | ---------------------------- |
| 0023H | RI/TI中断跳转 |
| 001BH | T1 中断跳转 |
| 0013H | INT1 中断跳转 |
| 000BH | T0 跳转 |
| 0003H | INT0 中断跳转 |
| 0000H | 主程序跳转指令 (只有三个 Byte) |

### 数据存储器 RAM | `READ RANDOM MEMORY`

所谓随机存取存储器，即随时能改写，也能读出里面的数据，它类似于我们的黑板，我能随时写东西上去，也能用黑板擦擦掉重写。

空间分配

**低 128 字节 real RAM** `00H-7FH`

- 1 工作寄存器区：4x8bytes 每个区域都是 R0-R7;只能选一组

- 2 可位寻址区：对 00H-7FH 进行位编址，通过指令区分

- 3 用户 RAM 区

1 和 3 只能字节寻址，只有 2 可以位寻址

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621002147037.webp" alt="image-20240621002147037" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621001638481.webp" alt="image-20240621001638481" style="zoom:50%;" />

**高 128 字节 `SFR` 特殊功能寄存器 `80H-FFH`**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621002609930.webp" alt="SFR寄存器" style="zoom:50%;" />

以 0 或 8 结尾的可以容许位寻址

### 复位

复位——使单片机回复原始默认状态的操作

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621190646898.webp" alt="image-20240621190646898" style="zoom:50%;" />

复位 RES

- A = 0
- PSW = 0
- PC = 0
- DPTR = 0
- **SP = 07H**

RST（9pin）：出现 2 个机器时间的高电平状态

### I/O

先易后难，所以 P1-P3-P0-P2

!!! note "可能的作用"
    - 外部设备连接：存储器扩展
        - 并行 IO 输入
        - 串行通信

80C51 共有 4 个 8 位并行 I/O 端口：**P0,P1,P2,P3 口**,共 32 个引脚。

1. P0 口既可以作为普通 I/O 口，又可以作为外部扩展时的数据总线和地址总线的低 8 位，分时复用；作为普通 I/O 口时，外部要接上拉电阻。
2. P1 口可以作为普通 I/O 口使用，内部带上拉电阻。
3. P2 口可以作为普通 I/O 口使用，又可作为外部扩展时地址总线的高 8 位，作为普通 I/O 时，内部带上拉电阻。
4. P3 口作为普通 I/O 时，内部带上拉电阻。第二功能，用于特殊信号输入输出和控制信号（属控制总线）

P1:

具有通用 IO 口的方式，可实现输出，读引脚、读锁存器三种功能

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621192857719.webp" alt="image-20240621192857719" style="zoom:50%;" />

外部电平跟随内部总线上的电平

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621193410016.webp" alt="image-20240621193410016" style="zoom:50%;" />

- 读取外部操作的时候，读引脚（最下边）高电平，可以读入
- 读内部的锁存器：如对总线进行取反等操作的时候，

注意：

- 内部总线先写 1，使得场效应管先处于截止的状态，不然可能中间有回路导通，一直读取的是 0
- 最高带 4 个 LSTTL
- 拉电流与灌电流区别

P3:

- 通用 IO 口：可实现输出、读引脚、读锁存器三种功能
- 准双向通用口，作为通用输入口之前应显示 P3.n 置 1，通用输出口应该使第二输出端置 1
- 普通 IO 第二输出为 1，完全由锁存器 Q 端决定，即由内部总线决定

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240619111616506.webp)

输入功能的时候，内部引脚也要置 1

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621195519916.webp" alt="image-20240621195519916" style="zoom:50%;" />

P0，P2:

## 中断

### 流程

**中断系统是为使 CPU 具有对外界紧急事件的实时处理能力而设置的**,当中央处理机 CPU 正在处理某件事的时候外界发生了紧急事件请求，要求 CPU 暂停当前的工作，转而去处理这个紧急事件，处理完以后，再回到原来被中断的地方，继续原来的工作，这样的过程称为中断。

CPU 执行程序过程中，在每个机器周期的**S5P2**期间，中断系统对各个中断源进行采样。

!!! note "可能会有一些滞后"
    当前指令执行完之后,双周期<br>
    正在执行的指令为RET、RETI或任何访问IE或IP寄存器的指令。即只有在这些指令后面至少再执行一条指令时才能接受中断请求。<br>
    执行一条硬件`LCALL`指令<br>

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240327115545079.webp" alt="image-20240327115545079" style="zoom:40%;" /><img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508113216330.webp" alt="image-20240508113216330" style="zoom:50%;" />

`RETI`中断函数返回，清除中断状态的标志位，否则如果来了一个小于等于当前中断优先级的中断事件不会响应

具体流程可以看[这个视频](https://www.bilibili.com/video/BV17v41167Zw)，很清楚。

> 核心逻辑
> 通过程序代码和中断机制控制程序计数器 PC，让 PC 来回在不同代码段之间切换。
> 在 0000H-0030H 中有很多个中断地址，每个有 8 个字节，保存中断函数的位置地址

| 环节 | 作用 |
| :-------: | :----------------------------------------------- |
| ①中断源 | 申请中断的来源 |
| ②中断申请 | 中断源发出信号提出申请 |
| ③中断控制 | 中断系统判断是否要响应申请 |
| ④保护现场 | 安排好当前的工作）`b=a,a=c`,保护当前 PC 指针的位置 |
| ⑤中断服务 | 响应中断源的申请 |
| ⑥恢复现场 | 完事后，回去…… |
| ⑦中断返回 | 继续做打断前的工作 |

中断响应与子程序调用的区别

- **函数的执行**是由程序员事先安排好的（由一条调用函数指令来转入）,而中断服务程序是由随机的中断事件引起的;

- **函数的调用**受到主调函数控制<br>而中断服务程序一般与被中断的程序毫无关系 (没有从属关系);

- 有可能发生多个中断事件同时请求 CPU 服务的情况。

- **地址**中断响应程序的入口地址固定，而函数或者子程序调用中的子函数可以放在程序空间的任意位置。

- 中断返回指令`RETI`,子程序返回指令`RET`

- 有两种保护方式：外部保护再进子程序;进入子程序后再保护。中断事件保护现场只能放在中断服务当中，不能提前保护现场

### 中断系统结构

!!! note "中断源、中断标志位、中断开关、中断优先级、中断入口地址"

> EA 虚线代表几个开关是联动的

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508114105761.webp)

#### 中断源

| 中断源 | TCON | 中断向量（入口地址） | 中断号 | 优先级 |
| :-------------------------: | :----: | :------------------: | :----: | :----: |
| $\overline{INT0}$ 外部中断 | IE0 | `0003H-000AH` | 0 | 高 |
| T0 定时计数器 0 | TF0 | `000BH-0012H` | 1 | |
| $\overline{INT1}$ 外部中断 1 | IE1 | `0013H-001AH` | 2 | |
| T1 定时计数器 1 | TF1 | `001BH-0022H` | 3 | |
| TX/RX 串行口 | RI 或 TI | `0023H-002AH` | 4 | 低 |

5+1 = 6 个中断源：两个外部中断，两个定时中断，两个串行中断

- $\overline{INT0}$（P3.2）。可由`IT0(TCON.0)`选择其为低电平有效还是下降沿有效。当 CPU 检测到`P3.2`引脚上出现有效的中断信号时，中断标志`IE0(TCON.1)`置 1，向 CPU 申请中断。
- $\overline{INT1}$（P3.3）。可由`IT1(TCON.2)`选择其为低电平有效还是下降沿有效。当 CPU 检测到`P3.3`引脚上出现有效的中断信号时，中断标志`IE1(TCON.3)`置 1，向 CPU 申请中断。
- **TF0**（`TCON.5`）,片内定时/计数器`T0`溢出中断请求标志。当定时/计数器`T0`发生溢出时，置位`TF0`,并向 CPU 申请中断。
- **TF1**（`TCON.7`）,片内定时/计数器`T1`溢出中断请求标志。当定时/计数器 T1 发生溢出时，置位`TF1`,并向 CPU 申请中断。
- **RI**（`SCON.0`）或**TI**（`SCON.1`）,串行发送/接受<br>串行口中断请求标志。当串行口接收完一帧串行数据时置位`RI`或当串行口发送完一帧串行数据时置位`TI`,向 CPU 申请中断。

起始地址开始的 8 个地址：

在第 2 章中已经讲过，地址为 0003H-002AH 的共 40 个单元是单片机 5 个中断源的中断服务程序存放地址区，它被分为 5 段，每段 8 个单元，分别分配给 5 个中断源，具体分配如下：

#### 开关（都在 SFR）

**`TCON`（定时/计数器控制寄存器）**

触发：低电平 or 下降沿

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508115812183.webp" alt="image-20240508115812183" style="zoom: 33%;" />

- `IT0（TCON.0）`,外部中断 0 触发方式控制位。<br>当 IT0=0 时，为电平触发方式。<br>当 IT0=1 时，为边沿触发方式（下降沿有效）。

- `IE0（TCON.1）`,外部中断 0 中断请求标志位。

- `IT1（TCON.2）`,外部中断 1 触发方式控制位。

- `IE1（TCON.3）`,外部中断 1 中断请求标志位。

- `TF0（TCON.5）`,定时/计数器`T0`溢出中断请求标志位。

- `TF1（TCON.7）`,定时/计数器`T1`溢出中断请求标志位。

**`SCON`(串行口控制寄存器)**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621212044659.webp" alt="image-20240621212044659" style="zoom:33%;" />

**`IP`（2 个人为优先级）**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621210918383.webp" alt="image-20240621210918383" style="zoom:33%;" />

**`IE`（中断使能寄存器）**
响应需要总开关打开且子开关打开

### 优先级

- **CPU 总是先响应优先级别最高的中断请求。**

- 不能被新的同级或低优先级的中断请求所中断

- 能被高优先级中断请求所中断

> 打印机发送打印任务，中断，CPU 处理其他任务

### 实例

- 中断源有中断请求

- 此中断源的中断允许位为 1

- CPU 开中断（即 EA=1）

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508122502143.webp" alt="image-20240508122502143" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508122506367.webp" alt="image-20240508122506367" style="zoom:50%;" />

中断程序标准写法：

```assembly
    ORG 0000H
START:
    LJMP MAIN                ;跳转到主程序
    ORG 0003H
    LJMP INT0                ;转向中断服务程序
    ORG 0030H                ;主程序
MAIN:
    CLR IT0                      ;设为电平触发方式
    SETB EA                     ;CPU开放中断
    SETB EX0                   ;允许中断
    MOV  DPTR,#1000H   ;设置数据区地址指针
    AJMP $
    ORG 0200H                  ;中断服务程序
INT0:
    PUSH PSW                  ;保护现场
    PUSH ACC
    CLR P3.0                     ;由P3.0输出0
    NOP;
    NOP;
    SETB P3.0     ;由P3.0输出1,撤除       
    MOV A,P1     ;输入数据
    MOVX   @DPTR,A    ;存入数据存储器
    INC   DPTR     ;修改数据指针,指向下一个单元
    ... ... 
    POP ACC                     ;恢复现场
    POP PSW
    RETI                              ;中断返回
```

#### 外部中断的扩展

多外部中断源的系统示例。

设有 5 个外部中断源，中断优先级排队顺序为：XI0、XI1、XI2、XI3、XI4。试设计它们与 80C51 单片机的接口。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508133213756.webp" alt="image-20240508133213756" style="zoom:50%;" />

```assembly
    ORG  0003H
    LJMP INSE0       ;转外部中断0服务程序入口
    ORG  0013H
    LJMP INSE1  ;转外部中断1服务程序入口
    … …
    … …
INSE0:  
 PUSH PSW ;XI0中断服务程序
    PUSH ACC
    … …
    … …
    POP  ACC
    POP  PSW
    RETI 
INSE1:
 PUSH PSW         ;中断服务程序
    PUSH ACC
    JB P1.0,DV1    ;P1.0为1,转XI1中断服务程序
    JB P1.1,DV2     ;P1.1为1,转XI2中断服务程序
    JB P1.2,DV3     ;P1.2为1,转XI3中断服务程序
    JB P1.3,DV4     ;P1.3为1,转XI4中断服务程序
INRET:
 POP ACC
    POP PSW
    RETI
DV1:
    … …             ;XI1中断服务程序
    AJMP INRET
DV2:
 … …             ;XI2中断服务程序
    AJMP INRET
DV3:
 … …             ;XI3中断服务程序
 AJMP INRET
DV4:
 … …             ;XI4中断服务程序
 AJMP INRET
```

## 定时 / 计数

### 时序

时序是对象（事件、信息）按照时间顺序组成的序列关系

时序图最为常用。

纵轴表示电平

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240621192004419.webp)

晶振`fosc`

机器周期、指令周期、振荡周期、状态周期：

1 状态 = 2 振荡

1 机器 = 12 振荡

1 指令 = 1~4 个机器周期

1 个指令周期=N 个机器周期=6N 个状态周期=12N 个节拍=12N 个时钟周期=12N 个振荡周期

- 如果晶振频率  $f_{osc} = 12 MHz$,则时钟周期 $T_{clock}$  为：
  $T_{clock} = \frac{1}{12 \times 10^6 Hz} = 83.33 ns$

- 如果某个微处理器的一个机器周期需要 12 个时钟周期完成，则机器周期 $T_{machine}$为：
  $T_{machine} = 12 \times 83.33 ns = 1\mu s$

!!! note "短时延时函数"
    ```assembly
    ;简单
    DELAY:
        MOV R7,#TIME
    LOOP:
        NOP
        NOP
        DJNZ R7,LOOP
        RET

    ;定时较长
    DELAY:
        MOV R5,#TIME1
    LOOP2:
        MOV R7,#TIME2
    LOOP1:
        NOP
        NOP
        DJNZ R7,LOOP1
        DJNZ R5,LOOP2
        RET
    ```

### 定时器/计数器结构

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508135706335.webp)

2 个 16 位定时器、计数器：

- T0 由两个 8 位 SFR TH0（high）TL0（low）构成
- T1 由两个 8 位 SFR TH1 TL1 构成

!!! note "实质是 +1 计数器"
 定时器在单片机内部就像一个小闹钟一样，根据时钟的输出信号，每隔“一秒”,计数单元的数值就增加一，当计数单元数值增加到“设定的闹钟提醒时间”时，计数单元就会向中断系统发出中断申请，产生“响铃提醒”,使程序跳转到中断服务函数中执行
    - 定时器：机械周期，晶振已知；对片内时钟进行计数;计数值 N 乘以机器周期$T_{cy}$就是定时时间$t$ 。
    - 计数器：例如光电码盘测量电机转速；对 Tx 引脚输入的脉冲进行计数

    加1计数器输入的计数脉冲有两个来源,一个是由系统的时钟振荡器输出脉冲经12分频后送来;一个是T0或T1引脚输入的外部脉冲源。

### 寄存器

#### **控制寄存器`TCON`**

TR0 TR1 控制定时计数器的启动停止：

TF0 TF1 溢出中断请求标志位

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508115812183.webp" alt="image-20240508115812183" style="zoom:50%;" />

#### 工作方式寄存器`TMOD`

低四位 T0，高四位 T1

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240508140054318.webp" alt="image-20240508140054318" style="zoom:50%;" />

- M0M1：工作方式设置位工作在 4 种模式

| M1M0 | 工作方式 | 说明 |
| ---- | -------- | ------------------------------ |
| 00 | 方式 0 | 13 位定时计数器 |
| 01 | 方式 1 | 16 位定时计数器 |
| 10 | 方式 2 | 8 位自动重装定时计数器 |
| 11 | 方式 3 | T0 两个独立 8 位计数器，T1 停止计数 |

- CT：定时控制器选择位：工作在定时模式（0）还是计数模式（1）

- GATE：启停模式

#### 中断允许控制寄存器 IE

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240511233252243.webp" alt="image-20240511233252243" style="zoom:33%;" />

开启 ET1,ET0 才能中断

### 工作方式

兼容 48 芯片，所以有 4 种工作状态

#### 方式 0

方式 0 为 13 位计数，由 TL0 的低 5 位（高 3 位未用）和 TH0 的 8 位组成

定时模式 Gate = 0,CT = 0

Gate = 1：由 INT0 进行控制

Gate = 0：或门让右侧一直是 1 ,完全由 TR 决定

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240511234311556.webp" alt="image-20240511234311556" style="zoom:50%;" />

分析上图可以得出设置规律

- 计数外部脉冲个数： **$1～8192(2^{13})$**

- 定时时间：     $T～8192T$

- $f_{osc}=12MHz$,$T=1\mu s$时，最大定时时间：$8.19ms$

控制不同初始值来控制定时时间：溢出后会中断

初始化定时/计数器时，初值 N 计算:<br>

- 定时机器周期数：$N=\frac{t}{T}$ ——定时时间/机器周期<br>
- 计数初值：$X=2^{13}-N $​——计数最大值与计数值之差<br>

!!! note "测量周期/频率"
 设置 TR = 1,CT = 0,GATE = 1;<br>INT0 输入，高电平时候，计时开始;就可以记录高电平有多少个机械周期

!!! note "方式 0，查询方式"
    选用定时/计数器1**工作方式0**   产生$500\mu s$定时,在P1.1输出周期为$1ms$的方波,设晶振频率=$6MHz$。
 === "TMOD 进行初始化"

    - GATE=0（用 TR1 位控制定时的启动和停止）<br>
    - C/T =0（置定时功能）<br>
    - M1M0=00（置方式 0）<br>
    - 因定时/计数器 0 不用，可将其置为方式 0（不能置为工作方式 3）<br>
    - 这样可将 TMOD 的低 4 位置 0，所以（TMOD）＝00H。<br>
    
    === "计算定时初值"
    
        $[2^{13}- X]\times 2=500 X=7942D=1111100000110B$
        将低 5 位送 TL1，高 8 位送 TH1 得：$(TH1)＝F8H$,$(TL1)=06H$
    
    === "代码实现"
        ```assembly
            ORG 0000H
            LJMP MAIN
            ORG 0300H
        MAIN:
            MOV TMOD,#00H    ;TMOD 初始化
            MOV TH1,#0F8H    ;设置计数初值
            MOV TL1,#06H
            MOV IE,#00H      ;禁止中断
            SETB TR1         ;启动定时
        LOOP: 
            JBC TF1,ZCZ      ;查询计数溢出
            AJMP LOOP
        ZCZ:  
            MOV TL1,#06H     ;重新置计数初值
            MOV TH1,#0F8H
            CPL P1.1          ;输出取反
            AJMP LOOP         ;重复循环
        ```

#### 方式 1

**16 位**计数 65536

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240622004345473.webp" alt="image-20240622004345473" style="zoom: 50%;" />

GATE 为 1 的时候，由 INT0 决定

可以用来测量脉宽

!!! note "定时时间超过最大定时时间"
    例如,要求延时100ms,最大65536个机械周期<br>
    可以设置成50ms延时并执行两次<br>

!!! note "例子"
    例 1 利用定时/计数器T0的方式1,产生10ms的定时,并使P1.0引脚上输出周期为20ms的方波,采用中断方式,设系统时钟频率为12 MHz。

    === "1、计算计数初值X"
    
    由于晶振为12 MHz,所以机器周期$Tcy$为$1 ns$
    
    $N＝\frac{t}{T_{cy}}=\frac{10\times10^{-3}}{1\times10^{-6}}=10000$
    
    $X＝65536－10000＝55536＝D8F0H$
    
    即应将$D8H$送入$TH0$中,$F0H$送入$TL0$中
    
    === "2、求T0的方式控制字TMOD"
    
    M1M0=01,GATE=0,C/T=0,可取方式控制字为01H;
    
    ```assembly
    ORG   0000H  
    LJMP  MAIN                ;跳转到主程序
    ORG   000BH              ;T0的中断入口地址
    LJMP  DVT0                ;转向中断服务程序
    ORG   0100H
    
    MAIN：
        MOV   TMOD,#01H   ;置T0工作于方式1
        MOV   TH0,#0D8H   ;装入计数初值
        MOV   TL0,#0F0H          
        SETB  ET0    ;T0开中断
        SETB  EA    ;CPU开中断
        SETB TR0    ;启动T0
        SJMP $     ;等待中断,程序一直停在这里,直至中断。
    DVT0:
        CPL  P1.0                ;P1.0取反输出
        MOV  TH0,#0D8H          ;重新装入计数值
        MOV  TL0,#0F0H           
        RETI                            ;中断返回
        END
    
    ```

#### 方式 2

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240511235352718.webp" alt="image-20240511235352718" style="zoom:50%;" />

8 位自动重装定时计数器：

- 方式 0，方式 1，溢出后变成 0000，需要重新设置初始值

- 方式 2，可以自动将 TH0 中的值压入 TL0，不需要人工赋值

一般 C/T = 0,GATE =0

计数外部脉冲个数范围：1～256($2^8$)

定时时间范围：T～256T

!!! note "方式 2"
    例1：用定时/计数器1以工作方式2计数,要求每计满100次进行累加器加1操作。
 === "TMOD 初始化"

    - M1M0=10（方式 2）
    
    - CT=1（计数功能)
    
    - GATE=0（TR1 启动和停止）
    
    因此（TMOD）=60H。
    
    === "计算计数初值"
    
     $2^8-100=156D=9CH$  所以 $TH1=9CH$
    
    ```assembly
    ORG 0000H
    AJMP MAIN     ;跳转到主程序
    ORG 001BH     ;定时/计数器 1 中断服务程序入口地址
    INC A
    RETI
    ORG 0030H
    
    MAIN: 
     MOV TMOD #60H ;TMOD 初始化
     MOV TL1,#9CH ;首次计数初值
     MOV TH1,#9CH   ;装入循环计数初值
     SETB EA   ;开中断
        SETB ET1
        SETB TR1       ;启动定时/计数器 1
    HERE: SJMP $        ;等待中断
    ```

#### 方式 3

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240512000523646.webp" alt="image-20240512000523646" style="zoom:50%;" />

T0 分成两个 8 位定时/计数器 TL0 和 TH0 ;

**TL0**既可计数也可定时，是一个 8 位定时/计数器。占用了 T0;所有控制位：C/T,TR0,GATE,TF0 和 INT0、T0 引脚;

**TH0**只能作为定时器，因为 T0 已被 TL0 占用，TH0 用 T1 的控制位：TR1、TF1;

**如果定时/计数器 T0 工作在方式 3,T1 只能工作在 0、1、2 方式****。此时由于 T1 的运行控制位 TR1 及计数溢出标志位 TF1 已被定时/计数器 T0 借用，这时，****T1 作为串行口的波特率发生器使用。**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240512001740549.webp" alt="image-20240512001740549" style="zoom: 33%;" />

!!! note "欲用 80C51 产生两个方波，一个周期为 200μs，另一个周期为 400μs，该 80C51 同时使用串行口，用定时器／计数器作为波特率发生器。"
    用两个独立的定时计数器实现两个不同周期的定时

    这时`T0`采用方式3工作,其中,`TL0`产生$200\mu s$定时,由` P1.0`输出方波;
    
    `TH0`产生$400\mu s$定时,由`P1.1`输出方波;
    
    `T1`设置为方式2作波特率发生器用。$f_{OCC}=9.216MHz$​​ 
    
    === "定时常数计算"
      - `TLO`定时常数为`TL0`：$t_{10} = 100μs$,$TCL0 = 2^8 - 9.216×10^6×100×10^{-6} = 256 - 76.8 = 179.2$，单位$\mu s$，为十进制数值。十六进制数值为`TL0 = B3H`。
      
      - `TH0`定时常数为`TH0`：定时时间为$t10 = 200μs$，$TCH0 = 2^8 - 9.216×10^6×200×10^-6 = 256 - 153.6 = 102.4$，单位$\mu s$,为十进制数值。十六进制的值为`TH0 = 66 H`。
      
      - TH1的波特率（详细计算见串行口部分）：设波特率为`2400`,则定时常数为`TC2 = F6H`
    
    === "程序代码"
    
        ```assembly
        ; 定时器0初始化
        MOV TL0, #0B3H ; 设TL0初值(100us定时)
        MOV TH0, #66H ; 设TH0初值(200us定时)
        MOV TL1, #0F6H ; 设TL1初值(波特率为2400)
        MOV TH1, #0F6H ; 设TH1初值
        SETB TR0 ; 启动TL0
        SETB TR1 ; 启动TH0
        SETB ET0 ; 允许TL0中断
        SETB ET1 ; 允许TH0中断
        SETB EA ; CPU中断开放
        AJMP $
        
        ; 定时器0中断服务程序
        ORG 0200H
        ITL0: MOV TL0, #0B3H ; 重装定时常数
        CPL P1.0 ; 输出方波(200us)
        RETI
        ITH0: MOV TH0, #66H ; 重装定时常数
        CPL P1.1 ; 输出方波(400us)
        RETI
        
        ; 主程序
        ORG 0000H
        AJMP MAIN
        ORG 000BH ; TL0的中断入口
        AJMP ITL0
        ORG 001BH ; TH0的中断入口
        AJMP ITH0
        ORG 0100H
        MAIN: MOV SP, #60H ; 设栈指针
        MOV TMOD, #23H ; 设T0为方式3,T1为2
        ```

### 初始化

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240512001802295.webp" alt="image-20240512001802295" style="zoom:33%;" />

设置工作方式 TMOD:

确定用 T0 还是 T1：初始化 TMOD 高四位还是低四位<br>

定时模式还是计数模式：CT<br>

方式 0-3 使用哪一种：M1M0<br>

控制模式：GATE<br>

计算初始值：

计算加 1 计数器的计数初值 Count，并将计数初值 Count 送入 TH、TL 中

初始值 = 上限 - 计数值

**计数**方式时：  $X=M-计数值$

**定时**方式时：定时值$t(\mu s)=(M—X)\cdot T_M=\frac{12}{f_{osc}(M-X)}$,所以$X=M-t(\mu s)\times f_{osc}(MHz)_{12}$。

- M 为定时计数器溢出值：$2^N,N=13,16,8$

- $T_M$​单片机时钟周期

若采用中断方式，则应设置 IE:

TCON:

启动计数器工作 TCON，启动定时计数器使 TR0 或 TR1 置位

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240516202857183.webp)

```c
// 设置工作方式：GATE,C/T,M1M0→TMOD
TMOD = 0x01; // 定时器 0 工作在模式 1

// 设置加 1 计数器初值：Count→TH,TL
TH0 = 0xFC;  // 高 8 位初值
TL0 = 0x66;  // 低 8 位初值

// 启动定时/计数器：1→TRx (x=0,1)
TR0 = 1;     // 启动定时器 0

// 开中断：1→ETx (x=0,1),1→EA
ET0 = 1;     // 使能定时器 0 中断
EA = 1;      // 总中断使能
```

## 串口通信

> 数据通信 = 数据处理 + 数据传输

MCS-51 单片机的串行口——全双工的异步串行通信接口（即：通用异步收发器 UART）

它内部包括一个发送器和一个接收器，实现 CPU 并行输出→串行发送，串行接收→CPU 并行接收的转换功能。

### 概念

> 有部分内容其实是计网物理层的内容

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240622100805189.webp" alt="并行通信" style="zoom:33%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240622100827823.webp" alt="串行通信" style="zoom: 33%;" />

#### 物理接口

> 参考[串口、COM 口、UART 口，TTL、RS-232、RS-485 区别详解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/89240672)
>
> [单片机应用原理篇之串行通信基本概念_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1zK4y147qr/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

串口、UART 口、COM 口、USB 口是指的物理接口形式 (硬件)：

!!! note "概念"
    === "**UART接口**"
        通用异步收发器（Universal Asynchronous Receiver/Transmitter)，UART是串口收发的逻辑电路，这部分可以独立成芯片，也可以作为模块嵌入到其他芯片里，单片机、SOC、PC里都会有UART模块。
    === "**COM口**"
        特指台式计算机或一些电子设备上的D-SUB外形(一种连接器结构，VGA接口的连接器也是D-SUB)的串行通信口，应用了串口通信时序和RS232的逻辑电平。
    === "**USB口**"
        通用串行总线，和串口完全是两个概念。虽然也是串行方式通信，但由于USB的通信时序和信号电平都和串口完全不同，因此和串口没有任何关系。USB是高速的通信接口，用于PC连接各种外设，U盘、键鼠、移动硬盘、当然也包括“USB转串口”的模块。（USB转串口模块，就是USB接口的UART模块）

    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__v2-04217e1629bdb71c6fb0f598c1b4dd12_1440w.webp)

#### 电平标准（电信号）

TTL、RS-232、RS-485 是指的电平标准 (电信号)：

=== "TTL 电平"
    全双工（逻辑1: 2.4V--5V 逻辑0: 0V--0.5V）<br>距离：1m左右

=== "RS-232"
    电平：全双工（逻辑1：-15V--3V 逻辑0：+3V--+15V)<br>距离：15m左右，用232做中转可以做的更远；

    负逻辑
    
    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240516235636473.webp" alt="image-20240516235636473" style="zoom: 33%;" />

| 主要引脚 | 作用 |
| ---------- | -------- |
| TXD `P3.0` | 发送数据 |
| RXD `P3.1` | 接收数据 |
| SGND | 信号接地 |

    公头-针,母头-孔（2,3交换,5共地）
    
    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240516235207535.webp" alt="image-20240516235207535" style="zoom:50%;" />
    
    **不能过远的原因: 距离太远，电平衰减**

=== "RS485"
    RS485是一种串口接口标准，为了长距离传输采用差分方式传输，传输的是差分信号，抗干扰能力比RS232强很多。<br>半双工、（逻辑1：+2V-+6V 逻辑0： -6V- -2V）<br>可以实现主从机器的功能

!!! note "注意"
 COM 口一般是 RS232，只是把 UART 的高电平电压增大了，以便传得更远，而 RS485 又在此基础上把低电平改成了负电压，从而把信号改成了差分信号，增加了抗干扰能力。其实信号的本质并没有变化。

#### 通信方向

**全双工：** 通信双方可以在同一时刻互相传输数据

**半双工：** 通信双方可以互相传输数据，但必须分时复用一根数据线；

在发送时候不可以接收，在接收的时候不可以发送

> 对讲机

**单工：** 通信只能有一方发送到另一方，不能反向传输

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240622101003848.webp" alt="image-20240622101003848" style="zoom: 25%;" />

#### 同步异步

**异步：**

通信双方各自约定通信速率，

传输数据是以字符为单位的，待传送的字符串中的每个字符均加上**起始位、停止位、校验位**等控制信息位，构成一个字符帧。空闲的时候发送的是高电平 5V；起始位有低电平

帧与帧之间的时间间隔是任意的：

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240622103113909.webp" alt="帧格式" style="zoom:33%;" />

**同步：**

通信双方靠一根时钟线来约定通信速率

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240516233936771.webp" alt="image-20240516233936771" style="zoom:50%;" />

#### 通信速率

通信速率是以每秒传送多少个二进制位来度量的，这个速率称作波特率（Baud Rate）,其单位为 bps（bits per second，位/秒）

常用波特率：300,600,1200,2400,4800,9600,19200

总线：连接各个设备的数据传输线路（类似于一条马路，把路边各住户连接起来，使住户可以相互交流）

先确定波特率，让定时器产生波特率，约定波特率再通信：

### 串口通信结构

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240516235651266.webp" alt="image-20240516235651266" style="zoom:40%;" />

#### **串行数据缓冲寄存器 SBUF（99H）**

（逻辑地址只有一个，两个物理地址）

> 类似于一个教室有两个门

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517101614853.webp" alt="image-20240517101614853" style="zoom: 40%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240519232852513.webp" alt="image-20240519232852513" style="zoom:50%;" />

虽然接收和发送 SBUF 使用同一个逻辑地址，但物理是两个地址

接收移位寄存器，每收到一个位，就左移一个位，满载（8bit）以后就移到 SBUF 当中

接收最多 2Byte，主动发送最多 1Byte

接收方有两级缓存

#### 串行口控制寄存器 SCON

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517102324310.webp" alt="image-20240517102324310" style="zoom:50%;" />

- SM0、SM1——串行口工作方式选择位。

- SM2——多机通信控制位 (主要用于方式 2 和方式 3)

- **REN－允许/禁止串行口接收控制位**：REN=1，允许接收;REN=0，禁止接收。可通过软件对该位进行设置

- TB8－第 9 位发送数据：方式 0 中不使用 TB8。在方式 1 中，TB8 为停止位，在方式 2 和方式 3 时，TB8 的内容是要发送的数据格式中的第 9 位。

- RB8－第 9 位接收数据：方式 0 中不使用 RB8；方式 1 中 RB8 为接收到的停止位；方式 2 和方式 3 时，RB8 存放接收到的第 9 位数据，在双机通信中，作为奇偶校验;在多机通信中，用作区别地址帧/数据帧的标志。

- **TI ——发送结束和发送中断标志位**：串行发送停止位的开始时候，内部硬件置 1；注意要清零

- **RI——接收结束和接收中断标志位**

可以通过检验 TI RI 来判断是否接受、发送结束

#### 电源控制寄存器 PCON

PCON 的单元地址为 87H，其内部各位均不能进行位寻址

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517105934465.webp" alt="image-20240517105934465" style="zoom:50%;" />

SMOD 为串行口波特率倍增位，当串行口工作在方式 1 和方式 3 时，其波特率可调。调节手段之一便是利用 SMOD。

（1）若 SMOD=0，波特率不倍增;

（2）若 SMOD=1，则选定的波特率倍频 1 倍;

   系统复位时，SMOD 自动清零

### 串口工作方式

帧的结构和通信速率不同

| SM0 | SM1 | 工作方式 | 功能描述 | 波特率 |
| ---- | ---- | -------- | ----------------- | ------------------------------------- |
| 0 | 0 | 方式 0 | 8 位同步移位寄存器 | $\frac{fosc}{12} $ |
| 0 | 1 | 方式 1 | 10 位异步收发 | 由定时器控制 |
| 1 | 0 | 方式 2 | 11 位异步收发 | $\frac{fosc}{64}$或$\frac{fosc}{32} $ |
| 1 | 1 | 方式 3 | 11 位异步收发 | 由定时器控制 |

#### 工作方式 0

发送/接收过程：SBUF 中的串行数据由 RXD 逐位移出/移入

（**低位在先，高位在后**）;TXD 输出移位时钟，频率=  $\frac{fosc}{12} $   ;

每送出/接收 8 位数据 TI/ RI 自动置 1;需要用软件清零 TI/ RI。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517110554534.webp" alt="image-20240517110554534" style="zoom:50%;" />

发送完成后，TI 就置 1

串行口在方式 0 下的工作并非是一种同步通信方式，经常配合“串入并出”“并入串出”移位寄存器一起使用，以达到扩展一个并行口的目的。扩展电路如下图所示。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517110640047.webp" alt="image-20240517110640047" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517110648124.webp" alt="image-20240517110648124" style="zoom:50%;" />

51 的 RXD 传入有效信息位，TXD 机械周期放到时钟，对外展示并行输出

如要发送数据，查询方式的程序如下：

```assembly
MOV SCON,#00H ;串行口方式0
MOV SBUF,A  ;将数据送出
JNB TI,$         ;等待数据发送完毕,等待TI=1,即发送完成
CLR TI           ;为下次发送作准备，手动软件清零不要忘记
```

注意：复位时，SCON 已经被清零。

- 发送条件：TI=0。

- 接收条件：TI=0，置位 REN=1（允许接收数据）。

#### 工作方式 1

10 位的异步通信：1 位起始位 +8 位信息位 +1 位结束位

波特率可变，由定时器 1 的波特率决定

| 起始位 | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | 停止位 |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------ |

波特率设置：

- 波特率 = $(2^{SMOD}/32) \times (定时/计数器 1 的溢出率)$
- 定时/计数器 1 的溢出率 =$ \frac{f_{osc}}{12 \times (256 - 初值)}$；溢出率指的是 T1 溢出的频率，计算出 T1 溢出一次的时间$T$，那么$\frac{1}{T}$就是 T1 的溢出率
- 波特率 = $2^{SMOD}/32 \times \frac{f_{osc}}{12 \times (256 - 初值)}$
- 定时器初值 = $256 - \frac{f_{osc} \times 2^{SMOD}}{384 \times 波特率}$

为了能够被 384 整除

串行口工作时，$f_{osc}$常取 11.0592M 而非 12M，是因为 11.0592M 时能提供更精确的波特率。12M 晶振计算出的定时器 T1 初值不是整数，会产生累计误差

```assembly
;发送代码
    MOV SCON,#40H    ;串口工作在方式1下
    MOV A,P1
    MOV SBUF,A    ;启动串口发送
LP:   
    JNB TI LP    ;等待发送完成
    CLR TI           ;发送完成后清TI
```

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517112045860.webp" alt="image-20240517112045860" style="zoom:50%;" />

```assembly
;接收代码
     MOV SCON, #50H; 串口工作在方式1,启动接收
LP: 
     JNB RI LP        ;  等待接受完毕
     MOV A, SBUF ;把收到的数据保存下来
     MOV P1, A      ;接收到的数据送P1口
     CLR RI               ;  清接收中断标志
```

#### 工作方式 2

1 位起始位 +8 位数据 +1 位校验 +1 位终止

| 起始位 | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | 校验 | 停止位 |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ------ |

发送过程：

A、首先根据要传送的 8 位数据的特征 (如奇偶、地址/数据特征) 决定第 9 个信息位的状态。

B、启动串口发送（`MOV SBUF,A` 或 `MOV SBUF,#XXH`）。按起始位、数据位 D0～D7、校验位、停止位的顺序将该帧信息以规定的波特率逐一从 TXD 引脚移出。

 C、待发送完毕后自动将 SCON 中的 TI 位置 1，表示发送过程结束。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240519143852958.webp" alt="image-20240519143852958" style="zoom:50%;" />

接收过程：

A、软件将`REN`置 1，启动串行口在方式 2 下的接收过程;

B、UART 自动地按规定的波特率从引脚`RXD`上逐位接收信息，移入串口中的接收移位寄存器。

C、接收完毕后，将接收移位寄存器中的数据位 D0～D7 锁入`SBUF`。同时将校验位送入`SCON`中的`RB8`位，自动将`SCON`中的 RI 置 1，表示接收过程结束。编程时可通过查询和中断方式对下一步进行处理。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240519144526889.webp" alt="image-20240519144526889" style="zoom:50%;" />

波特率设置：

倍频：`SMOD = 1` 波特率 = $\frac{2^{SMOD}\times f_{osc}}{64} = \frac{f_{osc}}{32}$

不倍频：`SMOD = 0` 波特率 = $\frac{2^{SMOD}\times f_{osc}}{64} = \frac{f_{osc}}{64}$

#### 工作方式 3

多级通信 or 奇偶校验

在方式 3 下，串行口的结构、传送的帧格式、各位的定义皆与方式 2 相同，唯一的区别在于工作方式 3 通信的波特率是可编程的。

### 串口初始化

RITI 不会自动清零 必须软件清零

!!! note "先确定波特率，再找到溢出率，再计算定时器初值，让串口得到这个溢出率"

方式 0 的波特率 =$ \frac{fosc}{12}$

方式 2 的波特率 =$(\frac{2^{SMOD}}{64})\cdot fosc$

方式 1 的波特率 =$(2^{\frac{SMOD}{32}}) \times (T1 的溢出率)$

方式 3 的波特率 =$(2^{\frac{SMOD}{32}}) \times (T1 的溢出率)$

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240517113020751.webp" alt="image-20240517113020751" style="zoom:50%;" />

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__8f30c5e6ea7a025457568b080915e65.webp)

### 编程

#### 查询方式

指令查询标志位 TI 和 RI：

TI =1，一帧发送完，TI≠1，没有发送完

RI=1，一帧数据已送到，RI≠1，没有送到

#### **中断方式**

设置中断允许，以`TI`和`RI`作为中断请求标志位，`TI=1`或`RI=1`均可引发中断。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051.assets__image-20240519150922105.webp" alt="image-20240519150922105" style="zoom:50%;" />

??? note "串口方式 1"
 通过 MCS-51 串行口按模式 1 发送存放在片内`RAM 20H～3FH`中的数据，要求传送的波特率为`1200bps`。编写有关的通信程序。 `fosc=11.0592MHz`。

    === "计算"
        设串行口为方式1,定时器/计数器T1为方式2作为串行口的波特率发生器。可以避免计数溢出后用软件重装定时初值的工作。
        $波特率 = \frac{2^{SMOD}}{32}\times \frac{fosc}{12\times(2^8-TH1)}$
        取$SMOD＝0$
        $(TH1)＝232＝0E8H$
    
    === "程序代码"
        ```assembly
        ;A机发送程序
        MOV  TMOD,#20H ;设T1为方式2
        MOV  TL1,#0E8H ;T1定时常数
        MOV  TH1,#0E8H
        SETB TR1 ;启动T1
        MOV SCON,#01000000B;设串行口为方式1
        MOV  R0,#20H  ;设发送数据区首址
        MOV  R7,#32  ;发送32个ASCII码数据
        LOOP:
            MOV A,@R0 ;取ASCII码数据
            MOV SBUF,A ;带校验位发送
            JNB TI,$ ;发送等待
            CLR TI ;清TI标志 
            INC  R0 ;未发送完,则继续
            DJNZ R7,LOOP
        ```
    
    === "B机接收"
        采用查询方式，本例与上例相呼应，接收器把接收到的32个数据存放在20H－3FH单元内，波特率同上。
        ```
        MOV   SCON，#01010000B    ；设串口方式1，允许接收
        MOV   TMOD，#20H；设置定时器T1为方式2
        MOV   TL1，#0E8H                  ；初值，波特率为1200b/s
        MOV   TH1，#0E8H  
        SETB  TR1                               ；启动T1运行
        MOV   R0，#20H                       ；数据存放首地址
        MOV   R7，#32                        ；数据块长度
        LOOP: JNB   RI，$          ；RI由硬件置位
        CLR   RI             ；软件清除RI
        MOV  A，SBUF 
        MOV    @R0，A                    ；存放接收的数据
        INC      R0
        DJNZ   R7，LOOP
    
        ```
