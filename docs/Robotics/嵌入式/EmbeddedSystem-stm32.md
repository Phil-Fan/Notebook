# STM32

## history

- 成立于 1990 年，总部在英国剑桥，目前拥有员工 2000 多名，分布在全球的 32 个分支机构。全称是 Advanced RISC Machines Limited。
- ARM 是全球领先的半导体知识产权 (IP，intellectual property) 提供商，没有硬件，没有软件，只有图纸上的知识产权，设计了大量高性能、廉价、低耗能的 RISC 处理器。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619124444437.webp" alt="产品线" style="zoom:50%;" />

## 内核

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619124512255.webp" alt="image-20240619124512255" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619124829730.webp" alt="image-20240619124829730" style="zoom:67%;" />

1. 处理器内核

2. 与处理器内核紧密结合的嵌套向量中断控制器（NVIC）以实现低延迟的中断处理
3. 存储器保护单元（MPU），可选部件 MPU 实现存储器保护
4. 总线接口
5. 调试接口

### 3 级流水线

- 取指令 (fetch)、译码 (decode) 和执行 (execute)

- 为什么可以用：三部分需要的资源是不一样的

在执行一条指令的同时对下一条指令进行译码，并将第三条指令从存储器中取出。可以显著提高效率

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619140056526.webp)

!!! note "联想到计网中的发送端的流水线机制"

PC 指向正在取址命令的地址，以正在执行的代码为参考点，则 PC 一直指向第三条指令

PC = 当前指令位置 +8（两个指令）

| 流水线上各指令的地址 | 流水线工位 | 描述 | |
| :---: | :---: | :---: | :--- |
| ARM 指令集 | Thumb 指令集 | | |
| PC | PC | 取指 | 指令从存储器中取出 |
| PC-4 | PC-2 | 译码 | 对指令使用的寄存器进行译码 |
| PC-8 | PC-4 | 执行 | 从寄存器组中读出寄存器，执行移位和 ALU 操作，寄存器被写回到寄存器组中 |

支持指令集：thumb2 不支持 arm

### 工作模式

- 线程模式和处理模式

普通应用程序（线程模式）和中断服务程序（处理模式）；

- 特权级和用户级

用于**存储器访问的保护机制**。普通的用户程序不能意外地，甚至是恶意地执行涉及到要害的操作

- 在 CM3 运行主程序（后台程序）时是线程模式，既可以使用特权级，也可以使用用户级；
- 中断 (异常) 服务程序必须在处理模式（始终特权级）下执行；
- 复位后，mcu 默认进入线程模式，特权极访问。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619125625515.webp" alt="image-20240619125625515" style="zoom:50%;" />

特权级：该级别的程序可以访问所有范围的存储器，并且可以执行所有指令；

用户级：用户级程序不能直接改写 CONTROL 寄存器，需执行一条系统调用指令 (SVC)，由异常服务例程修改 CONTROL 寄存器，才能在用户级的线程模式下重新进入特权级。

- **存储器保护单元 MPU**：MPU 是保护内存的一个组件

### 存储器与映射

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619125720483.webp" alt="image-20240619125720483" style="zoom:50%;" />

其中，**R13 R14 R15 比较重要**

- R14 连接寄存器：用于存放子程序的返回地址调用

程序 B 执行最后，将 R14 寄存器的内容放入 PC，返回程序 A

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619130728693.webp)

- R15：程序计数器

​    正常操作时，从 R15 读取的值是处理器正在取指的地址，即当前正在执行指令的地址加上 8 个字节（两条 ARM 指令的长度）。由于 ARM 指令总是以字为单位，所以 R15 寄存器的最低两位总是为 0。

CPSR（当前程序状态寄存器）

- 条件标志
- 中断使能标志
- 当前处理器的模式
- 其它的一些状态和控制标志

哈佛结构，但是统一编址，共享同一个逻辑地址空间

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619131822340.webp)

字节：8 位

半字：16 位（必须分配为占用两个字节）

字：32 位（必须分配为占用 4 各字节）

在小端格式中，高位数字存放在高位字节中。因此存储器系统字节 0 连接到数据线 7～0。

在大端格式中，高位数字存放在低位字节中。因此存储器系统字节 0 连接到数据线 31～24。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619132014766.webp)

### 调试接口

1) JTAG: 6 线制接口
2) SWD: 2 线制接口

### 中断

- 中断优先级可动态重新设置

- 中断数目可配置为 1～240

- 中断优先级的数目可配置为 1～8 位（1～256 级）

  （0 优先级最高，255 优先级最低）

- 处理模式和线程模式具有独立的堆栈和特权等级

占先

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619131647576.webp)

末位连锁

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619131712088.webp)

   进程堆栈（process stack），`SP_process`为进程堆栈的`SP` 寄存器。线程模式在复位后使用主堆栈主堆栈，可以配置为使用进程堆栈。

   主堆栈（main stack），`SP_main` 为主堆栈的`SP` 寄存器。处理模式使用主堆栈，在将 8 个寄存器压栈之后，`ISR` 使用主堆栈，并且后面所有的抢占中断都使用主堆栈。

### 复位

系统复位、电源复位和后备域复位

**系统复位：**

1.NRST 引脚上的低电平 外部复位
2.窗口看门狗计数终止 (WWDG 复位
3.独立看门狗计数终止 (IWDG 复位
4.软件复位 (SW 复位
5.低功耗管理复位

**电源复位：**
1.上电 掉电复位 (POR/PDR 复位
2.从待机模式中返回

**后备域复位：**
1.软件复位，备份区域复位可由设置备份域控制寄存器
(RCC_ 中的 BDRST 位产生。

## Thumb-2 指令集

是加载/存储型的，指令集只能处理寄存器的数据，而且处理结果都要放回寄存器，而对数据的访问要通过专门的加载/存储指令来完成；

`<opcode>{<cond>}{S} <Rd>,<Rn> {, <shift_op2>}`

| | |
| ----------- | ------------------------------------------------------------ |
| ` opcode ` | 操作码，即指令助记符，如 BL，ADD |
| `cond` | 条件码，描述指令执行的条件 |
| `S` | 可选后缀，若在指令后加上“S”，在指令完毕后会自动更新 CPSR 中条件码标志位的值 |
| `Rd` | ARM 指令中的目标操作数总是一个寄存器，通常用 Rd 表示 |
| `Rn` | 存放第 1 操作数的寄存器 |
| `opcode2` | 第 2 操作数，它的使用非常灵活，不仅可以是寄存器，还能使用立即数，而且能够使用经过位移运算的寄存器和立即数。 |

### 9 种寻址方式

①寄存器寻址

```assembly
MOV  R1,R2       ;R1=R2
SUB  R0,R1,R2    ;R0=R1-R2
```

②立刻寻址

```assembly
MOV   R1,#0xff000    ;R1=0xff000
SUBS  R0,R0,#1            ;R0=R0-1
```

③寄存器偏移寻址

④寄存器间接寻址

⑤基址寻址

⑥多寄存器寻址

⑦堆栈寻址

⑧块拷贝寻址

⑨相对寻址

### 6 大类指令

①跳转指令

②数据处理指令

③加载/存储指令

④协处理指令

⑤程序状态寄存器访问指令

⑥异常产生指令

### 4 种伪指令

①符号定义伪指令

②数据定义伪指令

③汇编控制伪指令

④其它常用伪指令

## GPIO

引脚很多

1. 使能 IO 口时钟。调用函数为 `RCC_APB2PeriphClockCmd()`

2. 初始化 IO 参数。调用函数 GPIO_Init()。

3. 操作 IO。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619132657409.webp)

```c
void LED_Init(void)
{
    GPIO_InitTypeDef GPIO_InitStructure; //描述 GPIO 寄存器的结构
    GPIO_InitStructure.GPIO_Pin = PIN_LED; //选择 LED 控制的引脚 _2
    GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz; //速度 _3
    GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;//模式 _4
    RCC_APB2PeriphClockCmd(RCC_LED, ENABLE); //给引脚加时钟 _1
    GPIO_Init(GPIO_LED, &GPIO_InitStructure); //初始化设置
}
```

```c
void LED_Sets(uint8_t data)
{
    uint16_t setValue;
    setValue =GPIO_ReadOutputData( GPIO_LED); // 调用 API
    //((uint16_t)GPIOx--> ODR)---->setValue
    setValue &= 0x00ff;
    setValue |= (uint16_t)data << 8;//data ---->setValue
    GPIO_Write(GPIO_LED, setValue); //调用 API
    //setValue---->((uint16_t)GPIOx -->ODR) 等效的寄存器操作
}
```

## Timer

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619132752717.webp)

### 4 个通用 16 位定时器

- 计数模式：上升、下降、上升和下降；（对比 51，工作模式多）
- T1 为增强型，带互补输出，紧急停止等功能，可用于电机控制

- 中断产生条件：定时器溢出、比较值相等、扑获引脚有指定的跳变。（对比 51 定时器中断事件类型多）

### 1 个 24 位`systick timer`

为 OS 配置，产生 OS 的任务扫描节拍；

也可用作普通的减计数器；

特征：

- 24 位减计数器；
- 计数值可自动加载；

### 2 个看门狗定时器

> 看门狗：watch dog timer WDT

一个讲的非常好的视频 [十行代码，就能让你理解看门狗！](https://www.bilibili.com/video/BV1ko4y1s7E1/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

!!! note "**看门狗作用：溢出后自动复位 MCU，防止程序异常跑飞**，解决单片机死机的问题"

相当于中断时间到了以后，触发的不是中断，而是单片机复位

注意要把狗喂好，不然高频复位的影响不亚于死机。

> [ac01]
> 看门狗就是一条狗，单片机可以领养，也可以不领养，如果领养了，单片机就会发现一个问题，看门狗定期咬它，还只咬它的硬件复位问题，但是又发现，只要在规定时间内喂它就不咬了，所以单片机工作一直很勤奋，如果哪天忘了喂狗，狗会帮他想起来的

代码

```c
WDT time=50 ms;   //设置看门狗的定时时间为 50ms
WDT =1;  //开启看门狗

While (1)
{
    Clear WDT();  //喂狗，给看门狗清零
    LED1=1;  LED2=0;  LED3=0;  LED4=0;
    Delay (10 ms) ;
    LED1=0;  LED2=1;  LED3=0;  LED4=0;
    Delay (10 ms) ;
    LED1=0;  LED2=0;  LED3=1;  LED4=0;
    Delay (10 ms) ;
    LED1=0;  LED2=0;  LED3=0;  LED4=1;
    Delay (10 ms) ;
}
```

### 例程

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619143905175.webp)

```c
TIM_DeInit();// 函数将 Timer 设置为默认值；
TIM_InternalClockConfig();//选择 TIMx 来设置内部时钟源；
TIM_Prescaler();//来设置预分频系数
TIM_ClockDivision //来设置时钟分割
TIM_CounterMode //来设置计数器模式
TIM_Period //来设置自动装入的值
TIM_ARRPreloadConfig();//来设置是否使用预装载缓冲器
TIM_ITConfig //来开启 TIMx 的中断
```

TIM2 通用定时功能，1s 中断一次

```c
void TIMER_cfg()
{
    TIM_TimeBaseInitTypeDef TIM_TimeBaseStructure;//重新将 Timer 设置为缺省值
    TIM_DeInit(TIM2);//采用内部时钟给 TIM2 提供时钟源
    TIM_InternalClockConfig(TIM2);
    //预分频系数为 36000-1，这样计数器时钟为 72MHz/36000 = 2kHz
    TIM_TimeBaseStructure.TIM_Prescaler = 36000 - 1;//设置时钟分割
    TIM_TimeBaseStructure.TIM_ClockDivison = TIM_CKD_DIV1; 
    //设置计数器模式为向上计数模式
    TIM_TimeBaseStructure.TIM_CounterMode = TIM_CounterMode_Up
    //设置计数溢出大小，每计 2000 个数就产生一个更新事件
    TIM_TimeBaseStructure.TIM_Period = 2000-1
    //将配置应用到 TIM2 中
    TIM_TimeBaseInit(TIM2,&TIM_TimeBaseStructure);
    //清除溢出中断标志
    TIM_ClearFlag(TIM2, TIM_FLAG_Update);
    //禁止 ARR 预装载缓冲器
    TIM_ARRPreloadConfig(TIM2, DISABLE);
    //开启 TIM2 的中断
    TIM_ITConfig(TIM2,TIM_IT_Update,ENABLE);
}
```

PWM 控制

```c
void pwm_cfg(void)
{
    TIM_OCInitTypeDef TimOCInitStructure;
    //设置缺省值
    TIM_OCStructInit(&TimOCInitStructure);
    //PWM 模式 1 输出
    TimOCInitStructure.TIM_OCMode = TIM_OCMode_PWM1; 
    //TIM 输出比较极性高           
    TimOCInitStructure.TIM_OCPolarity =  TIM_OCPolarity_High;     
    //使能输出状态
    TimOCInitStructure.TIM_OutputState = TIM_OutputState_Enable; 
    //设置占空比，占空比=(CCRx/ARR)*100% 或 (TIM_Pulse/TIM_Period)*100%
    TimOCInitStructure.TIM_Pulse = 1000;
    //TIM1 的 CH2 输出
    TIM_OC1Init(TIM1, &TimOCInitStructure); 
    //设置 TIM1 的 PWM 输出为使能                 
 TIM_OC1PreloadConfig(TIM1,TIM_OCPreload_Enable);
 TIM_CtrlPWMOutputs(TIM1,ENABLE);     
}
```

## UART

UART | `Universal synchronous/asynchronous receiver transmitter`，通用同步/异步收发器

异步串行的字节帧

   UART 通信是以字节帧为单位的，常用的字节帧：

   1 个起始位＋8 个数据位＋1 个校验位＋1 个停止位

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133353142.webp)

通信参数

①波特率：pbs，每秒多少位，即每一位的时间宽度；

②数据区长度：8 位（常用），或 7 位

③数据区顺序：低位在先（常用），或高位在先

④奇偶校验位：无、奇校验、偶校验

⑤停止位：1 位、1.5 位、2 位

功能引脚

TX：发送数据输出引脚。

RX：接收。

### 工作流程

①接收过程：UART 监听总线，有下跳变时，启动数据采样，一个字节的数据收到后，如果奇偶校验正确，则把数据存到接收寄存器中，置状接收态标志位，并向 CPU 申请中断，让 CPU 及时读取；

②发送过程：UART 的发送寄存器接收到 CPU 写入的数据，立刻启动，按设定的参数逐位发送，发送完毕，置状发送态标志位，并向 CPU 申请中断，告诉 CPU 可以发送下一个字节。

### UART 例程

中断接收 1 个字节，马上发送该字节

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133525336.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133537387.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133540057.webp)

## A/D & D/A

- 每个 ADC 有多达 16 个外部通道；
- ADC 时钟是 PCLK2 经过预分频器得到；
- A/D 转换时间 1~1.5us

- ADC 工作电压：2.4 V to 3.6 V；
- 输入信号电压范围：VREF- ≤ VIN ≤ VREF+

电压转换公式：按照比例进行分配

[STM32 入门学习之 AD 转换](https://www.bilibili.com/video/BV1mp4y1e7Sf/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)18min 左右；

二、工作方式

1）单次转换模式：在每个通道上，只执行一次转换；

2）连续转换模式：在每个通道上，执行连续转换；

3）扫描转换模式：在一组选定的模拟输入通道上自动转换；

4）启动 A/D 转换

软件命令、定时器 (TIM1) 产生的事件、外部触发和 DMA 触发；其中外部触发和 DMA 触发，允许应用程序同步 AD 转换和时钟的操作；

5）A/D 转换结束后自动产生中断；

6）CPU 通过查询状态位、中断响应、DMA 方式获取 A/D 值。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133818837.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133821814.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619133837397.webp)

## D/A

- 外接参考电压 VREF+（与 ADC 共用）输入，可提高 DAC 分辨率；
- 输出电压计算：$ Vout = DA /4096\times (VREF^+- VREF^-)$

如果`TENx`位被置 1，DAC 转换可以由某外部事件触发 (定时器计数器、外部中断线)。

如果选择软件触发，一旦 SWTRIG 位置’1’，转换即开始。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619134100987.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619134104320.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__EmbeddedSystem-stm32.assets__image-20240619134107807.webp)
