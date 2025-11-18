# 8051 实验

## 汇编编程

### 基本指令

### 延时

### 定时

### 中断

### 串口

### LCD

## C51 编程

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051-experiment.assets__image-20240508102042152.webp" alt="image-20240508102042152" style="zoom:40%;" />

以 main 函数为主体

C51 片内空间有限，运算能力有限

特殊功能寄存器都定义好了

| 数据类型 | 长度 (位)        | 取值范围 |                            |
| -------- | --------------- | -------- | -------------------------- |
| 字符型   | `signed char`   | 8        | -128~127                   |
|          | `unsigned char` | 8        | 0~255                      |
| 整   型  | `signed int`    | 16       | -32768~32767               |
|          | `unsigned int`  | 16       | 0~65535                    |
| 长整型   | `signed long`   | 32       | -21474883648~21474883647   |
|          | `unsigned long` | 32       | 0~4294967295               |
| 浮点型   | `float`         | 32       | ±1.75494E-38~±3.402823E+38 |
| 位   型  | `bit`           | 1        | 0，1                       |
|          | `sbit`          | 1        | 0，1                       |
| 访问 SFR  | `sfr`           | 8        | 0~255                      |
|          | `sfr16`         | 16       | 0~65535                    |

存储器分类

| 存储器类型 | 长度（位） | 对应单片机存储器                                |
| ---------- | ---------- | ----------------------------------------------- |
| `bdata`    | 1          | 片内 RAM，位寻址区，共 128 位。（亦能字节访问）    |
| `data`     | 8          | 片内 RAM，直接寻址，共 128 字节。                  |
| `idata`    | 8          | 片内 RAM，间接寻址，共 256 字节。                  |
| `pdata`    | 8          | 片外 RAM，分页间址，共 256 字节。（`MOVX ＠Ri`）   |
| `xdata`    | 16         | 片外 RAM，间接寻址，共 64k 字节。（`MOVX ＠DPTR`） |
| `code`     | 16         | ROM 区域，间接寻址，共 64k 字节。（`MOVC ＠DPTR`） |

​    访问片内 RAM 比访问片外 RAM 的速度要快得多，所以对于经常使用的变量应该置于片内 RAM 中，即用`bdata`、`data`、`idata`来定义；对于不经常使用的变量或规模较大的变量应该置于片外 RAM 中，即用`pdata`、`xdata`来定义。

```c
bit bdata flags；  /* 位变量 flags 定位在片内 RAM 的位寻址区 */
char data var；   /* 字符变量 var 定位在片内 RAM 区 */
float idata x,y,z； /* 实型变量 x，y，z 定位在片内间址 RAM 区 */
sfr  P1=0x90；      /* 定义 P1 口地址为 90H */
```

默认 data 低 128 位上

特殊功能寄存器的定义

​       80C51 单片机内部有 21 个特殊功能寄存器

`sfr 特殊功能寄存器名 = 地址常数;`

`sbit 位变量名 = 特殊功能寄存器名^位的位置（0~7）`

```c
sfr SCON = 0x90；/*定义串行口控制寄存器，地址为 0x90 */
sfr P0 = 0x80;  /*定义 P0 口，地址为 0x80 */
sfr16 T2 = 0xCC;/*定义 80C52 的 T2L 地址为 0xCC，T2H 地址为 0xCD*/   


sfr PSW=0xD0;/* 定义 PSW 寄存器地址为 0xD0 */
sbit OV=PSW^2; /* 定义 OV 位为 PSW.2，地址为 0xD2 */
sbit CY=PSW^7; /* 定义 CY 位为 PSW.7，地址为 0xD7 */
```

### 运算与控制

与 c 语言一致

- 加减乘除 mod
- 自增自减
- 关系运算
- 逻辑运算 `&&` `!` `||`
- 位运算符：单符号对位进行操作，双符号对字节进行操作
- 类型转换：`bit→char→int→long→float,signed→unsigned`

### 指针

一般指针占用 3 个字节：

- 第一个字节存放该指针的存储器类型编码（由编译模式的默认值确定）
- 第二和第三个字节分别存放该指针的高位和低位地址偏移量。

| 存储器类型 | `bdata/ data / idata` | `xdata` | `pdata` | `code` |
| ---------- | ----------------------- | ------- | ------- | -------- |
| 编码       | 0x00                    | 0x01    | 0xfe    | 0xff     |

> 例如：`xdata` 类型，地址为`0x1234`的指针表示为：第一字节为`0x01`，第二字节为`0x12`，第三字节为`0x34`。

一般指针可用于存取任何变量而不必考虑变量在 80C51 单片机存储空间的位置，许多 C51 库函数采用了一般指针。例如：

```c
char *xdata strptr； /* 位于 xdata 空间的一般指针 */
int *data number；/* 位于 data 空间的一般指针 */
```

### 函数

参数表有改造

函数的一般定义形式为：

```text
返回值类型 函数名（形式参数列表）[编译模式][reentrant][interrupt n][using n]
{
 函数体
}
```

**`interrupt`区分中断函数和普通函数；**

`reentrant`用于定义可重入函数。

`interrupt n`用于定义中断函数，n 为中断号，可以为 0~31，通过中断号可以决定中断服务程序的入口地址。

`using n`用于确定中断服务函数所使用的工作寄存器组，n 为工作寄存器组号，取值为 0~3。

| 中断源 | 外中断 0 | 定时器 0 | 外中断 1 | 定时器 1 | 串行口 |
| :----: | :-----: | :-----: | :-----: | :-----: | :----: |
| 中断号 |    0    |    1    |    2    |    3    |   4    |

**参数传递**

C 语言和汇编语言的相互调用

| 传递的参数 | char、1 字节指针 | int、2 字节指针 | long、float | 一般指针   |
| ---------- | --------------- | -------------- | ----------- | ---------- |
| 参数 1      | R7              | R6、R7         | R4~R7       | R1、R2、R3 |
| 参数 2      | R5              | R4、R5         | R4~R7       | R1、R2、R3 |
| 参数 3      | R3              | R2、R3         |             | R1、R2、R3 |

**库函数**

`reg51.h`

`reg52.h`

!!! note "实例"
    在一80C51单片机应用系统中，**外中断0**引脚接一个开关，**并行端口线P1.0**接一个发光二级管。<br>要求系统的功能是，开关闭合一次，发光二极管的状态改变一次。相应的程序为：<br>

    ```c
    #include “reg51.h”
    #include “intrins.h”
    sbit P10 = P1^0
    Sbit INT0= P3^2
    void delay(void) //延时操作
    {
        int a = 5000;
        while(a--)
            _nop_( );
    }
    void int_srv (void) interrupt 0 
    {
        delay( );
        if(INT0 == 0){
            P10 = ! P10;
            while(INT0 == 0);//按下后等待，而不会一直切换
        }
    }
    void main()
    {
        P10 = 0;
        EA = 1;//中断使能
        EX0 = 1;
        while(1);
    } 
    ```

!!! note "定时计数器编程示例"
    例  利用定时/计数器`T0`的方式1，产生10ms的定时，并使`P1.0`引脚上输出周期为20ms的方波，采用中断方式，设系统时钟频率为`12 MHz`。<br><br>
    1、计算计数初值X：<br>
    由于晶振为`12 MHz`，所以机器周期$T_{cy}$​为$1\mu s$​。因此：
    $N＝\frac{t}{T_{cy}} =10\times10-3/1\times10-6=10000$​​<br>
    因计数器是向上计数，计数到10000时溢出，所以计数器初值为-10000。应将`-(10000/256)`送入`TH0`中，`-(10000%256)`送入`TL0`中。<br>
    2、求`T0`的方式控制字`TMOD`：<br>
    M1M0=01，GATE=0，C/    =0，可取方式控制字为`01H`；<br>

    ```c
    #include “reg51.h”
    sbit P10 = P1^0;
    void timer0(void) interrupt 1
    {
        P10 = ! P10;
        TH0 = -(10000/256);//重新初始化
        TL0 = -(10000%256);
    }
    void main(void)
    {
        TMOD = 0x01;   //定时器初始化
        P10 = 0;
        TH0 = -(10000/256);
        TL0 = -(10000%256);  //初始值
        EA = 1;     //中断使能
        ET0 = 1;
        TR0 = 1;    //启动计时器
        while(1);
    } 
    ```

!!! note "A/D 转换接口编程示例"
    ADC0809与单片机的接口电路如图所示。采用查询方式采集数据的应用程序为：<br><img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051-experiment.assets__image-20240508112233118.webp" alt="image-20240508112233118" style="zoom:50%;" /><br>
    ```c
    # include “reg51.h”
    # include “absacc.h”
    # define uchar unsigned char
    # define IN0 XBYTE[0x7ff8]
    sbit ad_busy = P3^3;
    void main(void)
    {
        uchar data ad[10];
        while(1)
        {
            ad0809(ad);
        }
    }
    void ad0809(uchar idata *x)
    {
        uchar i;
        uchar xdata * ad_adr;
        ad_adr = & IN0;
        for(i = 0；i < 8；i ++)
        {
            * ad_adr = 0;    /*启动转换*/
            i = i;               /*延时等待*/
            i = i;
            while(ad_busy == 0);
            x[i] = * ad_adr;    /*存转换结果*/
            ad_adr ++;             /*下一通道*/
        }
    }
    ```

## 交通灯

交通灯实验代码，改了部分端口

整理了一下才发现还是需要读懂代码到底干了什么

### C 语言程序实现

下面的代码大概有三个功能

1. 端口的定义和映射，要和连线一一对应
2. 数码管的赋值和显示
3. 中断函数与定时器的设置

```c
#include "reg52.h" 
typedef unsigned int u16;
typedef unsigned char u8;

sbit LSA=P2^5;//这里端口随便改都行，和实际接口一致就可以
sbit LSB=P2^6;
sbit LSC=P2^7;

//定义灯的映射关系
#define GPIO_DIG   P0
#define GPIO_TRAFFIC P1
sbit RED10   = P1^0;
sbit GREEN10 = P1^1;
sbit RED11   = P1^2;
sbit YELLOW11= P1^3;
sbit GREEN11 = P1^4;
sbit RED00   = P3^0;
sbit GREEN00 = P3^1;
sbit RED01   = P1^5;
sbit YELLOW01= P1^6;
sbit GREEN01 = P1^7;

u8 code smgduan[50]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,
                    0x77,0x7c,0x39,0x5e,0x79,0x71,0x3d,
                    0x76,0x0f,0x0e,0x75,0x38,0x37,0x54,
                    0x5c,0x73,0x67,
                    0x31,0x49,0x78,
                    0x3e,0x1c,0x7e,0x64,0x6e,0x59};

u8 DisplayData[8];
u8 Second;

void delay(u16 i)
{
 while(i--); 
}

void DigDisplay()
{
 u8 i;
 for(i=0;i<8;i++)
    //这个循环的意思是：对于 8 位数码管的每一位，先通过译码器选择对应位，再赋对应的数值
 {
  switch(i)
  {
   case(0):
    LSA=0;LSB=0;LSC=0; break;
   case(1):
    LSA=1;LSB=0;LSC=0; break;
   case(2):
    LSA=0;LSB=1;LSC=0; break;
   case(3):
    LSA=1;LSB=1;LSC=0; break;
   case(4):
    LSA=0;LSB=0;LSC=1; break;
   case(5):
    LSA=1;LSB=0;LSC=1; break;
   case(6):
    LSA=0;LSB=1;LSC=1; break;
   case(7):
    LSA=1;LSB=1;LSC=1; break;
  }
  GPIO_DIG=DisplayData[i];
  delay(100);
  GPIO_DIG=0x00;
 }
}

void Timer0Init() //定时器的初始化和开关
{
 TMOD|=0X01;
 TH0 = 0XFC;
 TL0 = 0X18; //计算中断条件
 ET0 = 1;//打开定时器 0 中断开关
 EA = 1;//打开中断总开关
 TR0 = 1;//打开定时器 0
}


void main()
{ 
 Second = 1;
 Timer0Init(); //这里打开定时器

 while(1)
 {
        DisplayData[4] = 0x71;//F
  DisplayData[5] = 0x3e;//U
  DisplayData[6] = 0x39;//C
  DisplayData[7] = 0x75;//K
        //可以删掉上边四行
  if(Second == 30)
  {
   Second = 1;
  }

  if(Second < 11)
  {
   DisplayData[0] = 0x00;
   DisplayData[1] = 0x00;
   DisplayData[2] = smgduan[(10 - Second) % 100 / 10];
   DisplayData[3] = smgduan[(10 - Second) %10];

   DigDisplay();
   GPIO_TRAFFIC = 0xFF;
   RED00 = 1;
   GREEN00 = 1;
   GREEN11 = 0;   
   GREEN10 = 0;
   RED01 = 0; 
   RED00 = 0;
  }

  else if(Second < 16) 
  {
   DisplayData[0] = 0x00;
   DisplayData[1] = 0x00;
   DisplayData[2] = smgduan[(15 - Second) % 100 / 10];
   DisplayData[3] = smgduan[(15 - Second) %10];
   DigDisplay();
            
   GPIO_TRAFFIC = 0xFF;
   RED00 = 1;
   GREEN00 = 1;
   YELLOW11 = 0;   
   RED10 = 0;
   YELLOW01 = 0;
   RED00 = 0;
  }
  else if(Second < 26) 
  {
   DisplayData[0] = 0x00;
   DisplayData[1] = 0x00;
   DisplayData[2] = smgduan[(25 - Second) % 100 / 10];
   DisplayData[3] = smgduan[(25 - Second) %10];
   DigDisplay();
            
   GPIO_TRAFFIC = 0xFF;
   RED00 = 1;
   GREEN00 = 1;
   RED11 = 0; 
   RED10 = 0;
   GREEN01 = 0;
   GREEN00 = 0;
  }

  else 
  {
   DisplayData[0] = 0x00;
   DisplayData[1] = 0x00;
   DisplayData[2] = smgduan[(30 - Second) % 100 / 10];
   DisplayData[3] = smgduan[(30 - Second) %10];
   DigDisplay();
   GPIO_TRAFFIC = 0xFF;
   RED00 = 1;
   GREEN00 = 1;

   YELLOW11 = 0;  
   RED10 = 0;

   YELLOW01 = 0;
   RED00 = 0;      
  }
 }     
}

void Timer0() interrupt 1
{
 static u16 i;
 TH0=0XFC; 
 TL0=0X18;
 i++;
 if(i==1000)
 {
  i=0;
  Second ++; 
 } 
}
```

### **汇编程序参考**

```assembly
S_OK    BIT 20H.0          ; 定义一个位变量 S_OK，在 20H 寄存器的第 0 位
ORG     0000H              ; 程序从地址 0000H 开始
SJMP    MAIN               ; 在复位时跳转到 MAIN 函数
ORG     000BH              ; 定义中断向量地址 000BH (定时器 0 中断)
AJMP    SECOND             ; 在定时器 0 中断时跳转到 SECOND 函数
ORG     0030H              ; 程序代码从地址 0030H 开始


TAB2: DB 03FH,06H,05BH,04FH,66H,6DH,7DH,07H,7FH,6FH

//主程序
MAIN:
    MOV     SP,#60H      ; 设置堆栈指针 SP 的起始地址为 60H
    CLR     EA           ; 关闭所有中断
    MOV     TMOD,#01H    ; 定时器 0 设置为模式 1（16 位定时器）
    MOV     TL0,#0B0H    ; 设定定时器初值 TL0 为 0B0H
    MOV     TH0,#3CH     ; 设定定时器初值 TH0 为 3CH
    SETB    ET0          ; 使能定时器 0 中断
    SETB    PT0          ; 设置定时器 0 中断优先级
    SETB    EA           ; 使能全局中断
    SETB    TR0          ; 启动定时器 0
    MOV     R0,#10       ; 初始化 R0 为 10

Light:
    ACALL   GREEN     ; 南北绿灯，东西红灯
    ACALL   YELLOW    ; 南北黄灯，东西黄灯
    ACALL   RED       ; 南北红灯，东西绿灯
    ACALL   YELLOW    ; 南北黄灯，东西黄灯
    AJMP    Light         ; 循环执行上述指令


//中断程序
SECOND:
    CLR     EA           ; 关闭所有中断
    CLR     S_OK         ; 清除标志位 S_OK
    DEC     R0           ; R0 减 1
    MOV     A,R0         ; 将 R0 的值移动到累加器 A
    JZ      SECOND_1     ; 如果 R0 为 0 跳转到 SECOND_1
    ACALL   LED          ; 调用 LED 子程序，更新显示
SECOND_2:
    MOV     TH0,#3CH     ; 重新装载定时器初值
    MOV     TL0,#0BFH
    SETB    EA           ; 使能全局中断
    RETI                 ; 返回中断
SECOND_1:
    MOV     R0,#25       ; 如果 R0 为 0，将 R0 重置为 25
    SETB    S_OK         ; 设置标志位 S_OK
    SJMP    SECOND_2     ; 跳转到 SECOND_2


//信号灯控制程序;
;注意这里要注意板子上的连接
;LED的控制是高位暗，低位（0）灭
GREEN:
    MOV     DPTR,#06H    ; 设置 DPTR 寄存器
    MOV     A,#01111001B ; 南北方向绿灯，东西方向红灯
    MOV     P1,A         ; 输出到端口 P1
 MOV  A,#11111110B
 MOV  P3,A
    MOV     R1,#10       ; 设置 R1 为 10
TLP:
    JNB     S_OK,TLP     ; 等待 S_OK 标志位
    CLR     S_OK         ; 清除 S_OK 标志位
    DJNZ    R1,TLP       ; R1 减 1，如果不为 0，跳回 TLP
    RET                  ; 返回

YELLOW:
    MOV     A,#10110111B ; 南北方向黄灯，东西方向黄灯
    MOV     P1,A         ; 输出到端口 P1
 MOV  A,#11111111B
 MOV  P3,A
    MOV     R1,#5        ; 设置 R1 为 5
TLP1:
    JNB     S_OK,TLP1    ; 等待 S_OK 标志位
    CLR     S_OK         ; 清除 S_OK 标志位
    DJNZ    R1,TLP1      ; R1 减 1，如果不为 0，跳回 TLP1
    RET                  ; 返回

RED:
    MOV     A,#11001110B ; 南北方向红灯，东西方向绿灯
    MOV     P1,A         ; 输出到端口 P1
 MOV  A,#11111101B
 MOV  P3,A
    MOV     R1,#10       ; 设置 R1 为 10
TLP2:
    JNB     S_OK,TLP2    ; 等待 S_OK 标志位
    CLR     S_OK         ; 清除 S_OK 标志位
    DJNZ    R1,TLP2      ; R1 减 1，如果不为 0，跳回 TLP2
    RET                  ; 返回

//LED显示程序
LED:
    MOV     DPTR,#TAB2   ; 设置 DPTR 指向查找表
    MOV     A,R1         ; 将 R1 的值移动到累加器 A
    DEC     A            ; A 减 1
    MOVC    A,@A+DPTR    ; 取查找表中的值
    MOV     P0,A         ; 输出到端口 P0
    RET                  ; 返回


END 
```

在程序中，`S_OK` 的作用是：

1. **在定时器中断中**：
   - 当定时器达到设定的计数值时，会触发中断，在中断服务程序 `SECOND` 中，`S_OK` 被设置（`SETB S_OK`）以通知主程序定时已经到期。
2. **在主程序中**：
   - 主程序会不断检测 `S_OK` 的状态。如果 `S_OK` 被设置，意味着一个时间段（例如 10ms）已经过去，主程序可以执行下一步操作。
   - 使用 `JNB S_OK, label` 指令来等待 `S_OK` 被设置。如果 `S_OK` 未被设置，程序会在当前循环等待；一旦 `S_OK` 被设置，程序将继续执行。

### **对应关系**

**初始化部分**

```assembly
MAIN:
    MOV SP,#60H 
    CLR EA ;关中断 
    MOV TMOD,#01H ;设定时钟方式 
    MOV TL0,#0B0H ;设定定时器/计数器T0为时钟常数(100ms) 
    MOV TH0,#3CH 
    SETB ET0 ;允许中断/计数器T0中断 
    SETB PT0 ;启动定时器/计数器T0 
    SETB EA ;开中断 
    SETB TR0 ;启动定时器/计数器T0
```

```c
void Timer0Init()
{
    TMOD |= 0x01; // 选择为定时器 0 模式，工作模式 1，设置 TR0 启动

    TH0 = 0xFC;  // 设置定时初值，使计时 1ms
    TL0 = 0x18;  
    ET0 = 1;     // 允许定时器 0 中断
    EA = 1;      // 使能总中断
    TR0 = 1;     // 启动定时器
}

void main()
{    
    Second = 1;

    Timer0Init();
    ...
}
```

**中断部分**

```assembly
SECOND:
    CLR EA
    CLR S_OK
    DEC R0
    MOV A,R0
    JZ SECOND_1
    JZ SECOND_2
SECOND_1:
    MOV RO,#10
    SETB S_OK
SECOND_2:
    MOV TH0,#3CH
    MOV TL0,#0BFH
    SETB    EA
    RETI
```

```c
void Timer0() interrupt 1
{
    static u16 i;
    TH0 = 0xFC;  // 设置定时初值，使计时 1ms
    TL0 = 0x18;
    i++;
    if(i == 1000)
    {
        i = 0;
        Second++;    
    }    
}
```

这段汇编代码是一个基于 8051 单片机的交通灯控制系统，代码中包含了许多常用的指令，以下是这些指令的含义和用法：

### 汇编指令解释

- `MOV dest, src`: 将源操作数 `src` 的值传送到目的操作数 `dest`。
  - 示例：`MOV SP,#60H` 将立即数 `60H` 装入堆栈指针 `SP`。
  
- `CLR bit`: 将指定位清零（置 0）。
  - 示例：`CLR EA` 将全局中断使能位清零。

- `SETB bit`: 将指定位置 1。
  - 示例：`SETB EA` 将全局中断使能位置 1。

- `JZ label`: 如果累加器 `A` 的值为零，则跳转到指定标签。
  - 示例：`JZ SECOND_1` 如果 `A` 为 0，则跳转到 `SECOND_1`。

- `SJMP label`: 无条件跳转到指定标签。
  - 示例：`SJMP MAIN` 无条件跳转到 `MAIN`。

- `JB bit, label`: 如果指定位为 1，则跳转到指定标签。
  - 示例：`JB ACC.2,EMERG` 如果累加器 `A` 的第 2 位为 1，则跳转到 `EMERG`。

- `DEC reg`: 将指定寄存器的值减 1。
  - 示例：`DEC R0` 将寄存器 `R0` 的值减 1。

- `DJNZ reg, label`: 将指定寄存器的值减 1，如果减 1 后的结果不为 0，则跳转到指定标签。
  - 示例：`DJNZ R1,TLP` 将 `R1` 减 1，如果 `R1` 不为 0，则跳转到 `TLP`。

- `RET`: 从子程序返回。
  - 在这段代码中未使用。

- `RETI`: 从中断服务程序返回。
  - 示例：`RETI` 返回主程序。

#### 中断和定时器

- `ORG address`: 设置程序起始地址。
  - 示例：`ORG 0000H` 设置程序起始地址为 `0000H`。

- `AJMP address`: 绝对跳转到指定地址。
  - 示例：`AJMP SECOND` 绝对跳转到 `SECOND`。

- `MOV TL0,#value`: 将立即数装入定时器/计数器 0 的低 8 位。
  - 示例：`MOV TL0,#0B0H` 将 `0B0H` 装入 `TL0`。

- `MOV TH0,#value`: 将立即数装入定时器/计数器 0 的高 8 位。
  - 示例：`MOV TH0,#3CH` 将 `3CH` 装入 `TH0`。

- `MOV TMOD,#value`: 设置定时器/计数器模式寄存器 `TMOD` 的值。
  - 示例：`MOV TMOD,#01H` 设置 `TMOD` 为模式 1（16 位定时器/计数器）。

- `SETB TR0`: 启动定时器/计数器 0。
  - 示例：`SETB TR0` 启动定时器 0。

- `CLR TR0`: 停止定时器/计数器 0。
  - 在这段代码中未使用。

#### 位操作

- `S_OK BIT 20H.0`: 定义位变量 `S_OK` 在 `20H` 地址的第 0 位。
  - 示例：`S_OK BIT 20H.0` 定义 `S_OK`。

## 数码管

共阴极接法

对应表

```c
u8 code smgduan[50]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,
                    0x77,0x7c,0x39,0x5e,0x79,0x71,0x3d,
                    0x76,0x0f,0x0e,0x75,0x38,0x37,0x54,
                    0x5c,0x73,0x67,
                    0x31,0x49,0x78,
                    0x3e,0x1c,0x7e,0x64,0x6e,0x59};
```

## LED

LED 采用共阳接法

所以高电平是熄灭

拉电流——电流更大

灌电流——电流小，不足以驱动

## 串口通信

复制代码就行了，如果想玩，可以和你的队友连起来 P3.0 P3.1 互换连接

不想玩的话其实 1min 烧录一下例程代码就结束了

```c
//将波特率设置为 4800
//接受端口
#include "reg52.h"    //此文件中定义了单片机的一些特殊功能寄存器

typedef unsigned int u16;   //对数据类型进行声明定义
typedef unsigned char u8;


void UsartInit()
{
 SCON=0X50;   //设置为工作方式 1
 TMOD=0X20;   //设置计数器工作方式 2
 PCON=0X80;   //波特率加倍
 TH1=0XF3;    //计数器初始值设置，注意波特率是 4800 的
 TL1=0XF3;
 ES=1;      //打开接收中断
 EA=1;      //打开总中断
 TR1=1;     //打开计数器
}

void main()
{ 
 UsartInit();  // 串口初始化
 while(1);  
}

void Usart() interrupt 4
    
{
    u8 receiveData;
    receiveData=SBUF;//出去接收到的数据
    RI = 0;//清除接收中断标志位
}
```

```c
//发送端口
void Usart() interrupt 4
{
    u8 receiveData;
    receiveData=SBUF;//出去接收到的数据
    RI = 0;//清除接收中断标志位
    SBUF=receiveData*2;//将接收到的数据放入到发送寄存器
    while(!TI);    //等待发送数据完成
    TI=0;   //清除发送完成标志位
}
```

可以实现大概这个效果。如果两个同时发送的话，可能数字会越来越大（我设置的是翻倍发送）

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051-experiment.assets__image-20240531230036861.webp" alt="image-20240531230036861" style="zoom:50%;" />

## LCD & ADC

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-8051-experiment.assets__1717167497179.webp" alt="1717167497179" style="zoom:50%;" />

```c
#include "reg52.h"//此文件中定义了单片机的一些特殊功能寄存器
#include "lcd.h"
#include "XPT2046.h" 

typedef unsigned int u16;   //对数据类型进行声明定义
typedef unsigned char u8;
#define GPIO_DIG   P1
sbit LSA=P2^0;
sbit LSB=P2^1;
sbit LSC=P2^2;
//要非常注意 LCD 使用 P2.5,P2.6,P2.7 端口，不能混用，不然会有问题

u8 disp[5];
u8 isp[4];


u8 code smgduan[50]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,
            0x77,0x7c,0x39,0x5e,0x79,0x71,0x3d,
            0x76,0x0f,0x0e,0x75,0x38,0x37,0x54,
            0x5c,0x73,0x67,
            0x31,0x49,0x78,
            0x3e,0x1c,0x7e,0x64,0x6e,0x59};


/***
* 函 数 名：delay
* 函数功能：延时函数，i=1 时，大约延时 10us
***/
void delay(u16 i)
{
    while(i--); 
}


/***
* 函数名:datapros()
* 函数功能：数据处理函数
***/
void datapros()
{
    u16 temp;
    temp = Read_AD_Data(0x94);  //   AIN0 电位器
 
    disp[0]=smgduan[temp/1000];//千位
    disp[1]=smgduan[temp%1000/100];//百位
    disp[2]=smgduan[temp%1000%100/10];//个位
    disp[3]=smgduan[temp%1000%100%10]; 
    isp[0]=temp/1000+'0';
    isp[1]=temp%1000/100+'0';//百位
    isp[2]=temp%1000%100/10+'0';//个位
    isp[3]=temp%1000%100%10+'0'; 
}


/***
* 函数名:DigDisplay()
* 函数功能：数码管显示函数
***/
void DigDisplay()
{
    u8 i;
    for(i=0;i<4;i++)
    {
        switch(i)
        {
            case(0):
                LSA=0;LSB=0;LSC=0; break;
            case(1):
                LSA=1;LSB=0;LSC=0; break;
            case(2):
                LSA=0;LSB=1;LSC=0; break;
            case(3):
                LSA=1;LSB=1;LSC=0; break;
            case(4):
                LSA=0;LSB=0;LSC=1; break;
            case(5):
                LSA=1;LSB=0;LSC=1; break;
            case(6):
                LSA=0;LSB=1;LSC=1; break;
            case(7):
                LSA=1;LSB=1;LSC=1; break;
        }
        GPIO_DIG=disp[i];
        delay(100);
        GPIO_DIG=0x00;
    }  
}



void Timer0Init()
{
    TMOD|=0X01;
    TH0=0XFC;
    TL0=0X18; 
    ET0=1;
    EA=1;
    TR0=1;  
}


void main(void)
{
    Timer0Init();
    LcdInit();
    disp[4] = 0x5c;
    disp[5] = 0x5c;
    disp[6] = 0x5c;
    disp[7] = 0x75;
    while(1)
    {  
        DigDisplay();//数码管显示函数 
    }  
}

void Timer0() interrupt 1
{
    static u16 i;
    u16 j;
    TH0=0XFC;
    TL0=0X18;
    i++;
    if(i==1100)
    {
        i=0;
        datapros();  //数据处理函数
        LcdWriteCom(0x01);  //清屏
        for(j=0;j<4;j++)
        {   
            LcdWriteData(isp[j]);    
        }
    } 
}
```

这里使用定时中断完全是为了好玩，为了让显示刷新率不那么高设置的。

而且感觉使用循环的方法进行延时非常的蠢，所以定时$500-700ms$来完成任务。可以更改`if(i == 1000)`这个语句来设置延时的长短，这里还可以完成很多其他基于时间的操作。

还有需要注意到的是，每次刷新 LCD 的屏幕可以不使用`lcdinit()`函数，而可以直接使用`LcdWriteCom(0x01);`清屏函数。

```c
//---定义使用的 IO 口---//
sbit DOUT = P3^7;   //输出
sbit CLK  = P3^6;   //时钟
sbit DIN  = P3^4;   //输入
sbit CS   = P3^5;   //片选
```

要非常注意这段头文件中给出的引脚定义，因为之前我引脚是随便连的，就导致我的 LCD 和数码管其实是使用的同样的引脚，就会出现很多很多奇怪的问题，所以一个教训就是不要随意更改接口，如果需要更改，那么请弄清楚有没有接口是这次实验中已经用到的（可能通过板子进行连接的）
