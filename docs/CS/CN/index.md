---
comments: true
---
# Introduction

???+note "各学院开课信息"
    === "电气学院"
        [2023-2024冬 计算机网络与通信（电院） 期末考试回忆 - CC98论坛](https://www.cc98.org/topic/5799608)<br>
  [控院计网 计算机网络原理 学习心得](https://www.cc98.org/topic/5877551/2#1)<br>
        [【教程】推荐一个计算机网络小白向视频 - CC98 论坛](https://www.cc98.org/topic/5793620)<br>

        [大鹏鸟 - 杨春节老师视角](https://www.cc98.org/topic/5671695)<br>
     **复习优先级：HW、Quiz、Project、slides、textbook**
    
     考题部分来自于top-down课本后原题，考前瞄了一眼这个系列[CSDN计网课后题整理](https://blog.csdn.net/weixin_46183779/category_11204556.html)
        
     有几道题明显是HW的题改编的，所以要好好看一下老师发的课后题答案。总体感觉会偏理解，一些给到的公式和计算方法也没有进行考察。但是考试还是暴露了很多没有掌握的知识点，比如802.11部分的一些CSMA/CA的细节就没有注意到。
    
    === "光电   - 《数据通信与计算机网络》"
    
        [22-23期末回忆卷](https://www.cc98.org/topic/5596764)<br>
    
        [21-22春回忆卷](https://www.cc98.org/topic/5301579)<br>
    
        [知识点整理](https://www.cc98.org/topic/5301549)<br>
    
        [20-21回忆卷](https://www.cc98.org/topic/5069360)<br>
    
        [21-22春回忆卷](https://www.cc98.org/topic/5301512)<br>
    
        [22春-管院回忆卷](https://www.cc98.org/topic/5300823)<br>


         期末40<br>
         大作业30<br>
         小作业交两次：第三周第五周交，占30<br>
    
    === "计院"
    
        高分刷王道<br>
        [朋辈辅学 - 计算机网络速成](https://www.bilibili.com/video/BV1Xr4y1r7gM)<br>
        [咸鱼喧笔记](https://www.yuque.com/xianyuxuan/coding/gez9yl)<br>
        [计算机网络（计网） 2023-2024 回忆卷 - CC98论坛](https://www.cc98.org/topic/5799341)<br>
        [计算机网络1-OSI模型 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/Networking/计算机网络1-OSI模型/)<br>
        [大三上cs课程经验和资料分享（操作系统、计算机网络、计算机体系结构、汇编与接口、数值分析） - CC98论坛](https://www.cc98.org/topic/5807213)<br>
        [计院《计算机网络》复习笔记和选课排雷 - CC98论坛](https://www.cc98.org/topic/5031095)<br>
        [《计算机网络》的习题、实验内容、习题和实验的成绩、参考资料 请看本帖子-new - CC98论坛](https://www.cc98.org/topic/4987967)<br>
    === "USTC"
    
    === "CS144"
        [计算机网络学习总结（中科大计网 & Stanford CS144） - CC98论坛](https://www.cc98.org/topic/5686337)<br>

!!! abstract
 本笔记基于 USTC 郑烇老师《计算机网络》课程<br>
 USTC 计网 + 头歌实践平台<br>
 电院计网 + 光电计网<br>

<div class="card file-block" markdown="1">
<div class="file-icon"><img alt="xmind" src="/style/images/xmind.svg" style="height: 3em;"></div>
<div class="file-body">
<div class="file-title">计网复习思维导图</div>
<div class="file-meta">132KB / 2025-01-28</div>
</div>
<a class="down-button" target="_blank" href="CN.xmind" markdown="1">:fontawesome-solid-download: 下载</a>
</div>

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__Intro.webp)

## 基本概念

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240122233225413.webp)

网络：节点、边的拓扑结构

主机 host=端系统 end system

通信链路：传输速率=带宽 bps

分组交换设备：转发 packets

### 指标

Bit 信息论中信息量的单位

bit rate 性能指标

单位 b/s kb/s Mb/s Gb/s

???+note "存储单位和传输速率单位换算"
    === "存储单位（基于1024"

    - **KB (Kilobyte)**: 1 KB = 1024 Bytes <br>
    - **MB (Megabyte)**: 1 MB = 1024 KB = 1,048,576 Bytes <br>
    - **GB (Gigabyte)**: 1 GB = 1024 MB = 1,073,741,824 Bytes <br>
    
    === "网络传输速率单位（基于 1000"
    注意！！！1 Byte = 8 bits<br>
    注意换算时的基数差异（存储通常基于 1024，而网络速率基于 1000）<br>
    - **Kbps (Kilobit per second)**: 1 Kbps = 1000 bits/s<br> 
    - **Mbps (Megabit per second) = Mb/s (Megabit per second)**: 1 Mbps = 1000 Kbps = 1,000,000 bits/s <br>
    - **Gbps (Gigabit per second)**: 1 Gbps = 1000 Mbps = 1,000,000,000 bits/s <br>

`bandwidth` 带宽：信号具有的频带宽度，数字信道能传送的最高数据率

> 高速公路的车道有多宽

`throughput` 吞吐量：单位时间内成功地传送数据的数量

> 高速上现在的车流量

### Internet 内涵

- 一个角度

互联网是通过互联设备连在一起的网络的网络

- 另一个角度

互联网是分布式的互联网进程 + 为分布式应用提供服务的基础设施

### Internet 结构和 ISP

ISP: internet service provider

全连接 scalibity 可扩展性差

ICP: internet content provider ;ex:谷歌

数据中心机房 离 isp 较近

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123235809673.webp" alt="image-20240123235809673" />

internet 结构

tier1 + tier2 + regional isp + local isp

delay 时延

时延带宽积

信道利用率 - 某信道有多少被利用

排队论，信道利用率增大，时延就增大

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240122214414552.webp)

### 延时

$总时延 = 发送时延 + 传播时延 + 处理时延 + 排队时延$​

在这里要注意理解一下书上这个定义，是以 Node A 作为研究节点的，着重注意一下每种延时的定义和区别

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240307194432836.webp)

#### 节点处理延时 processing delay

The time required to examine the packet’s header and determine where to direct
the packet is part of the processing delay.

#### 排队延时 queueing delay

At the queue, the packet experiences a queuing delay as it waits to be transmitted
onto the link.

流量强度$I = \frac{L\cdot a}{R}$

L(bits) a 到达平均速率，R 链路带宽（bps）

流量强度为 1，延时无穷大

 延时的原因：输出能力小于到达速率

> 用火车过桥来理解

#### 传输延时 transmission delay

This is the amount of time required to transmit all of the packet’s bits into the link.

$T = \frac{L}{R}$,L 是分组长度，R 是链路带宽

$传播时延 = \frac{信道长度}{信道传播速率}$

#### 传播延时 propagation delay

Once a bit is pushed into the link, it needs to propagate to router B. The time required
to propagate from the beginning of the link to router B is the propagation delay.

$t = \frac{d}{s}$

`d`链路长度 `s`媒体传播速度

AB 距离很远的话，传播延时不能忽略

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240125175620523.webp" alt="image-20240125175620523" />

> 上面例子只计算了 transmission delay 和 propagation delay

#### 分组丢失原因

缓冲区有限

满队列后，分组会丢失

丢失可能重传也可能不重传

丢失以后，如果链路是可靠的会由上层重传  

#### 吞吐量 Throughtput

源端和目标端传输速率（有效的 d

??? note **definition**
 If the file consists of F bits and the transfer takes T seconds for Host B to receive all F bits, then the average throughput of the file transfer is F/T bits/sec.
 the rate at which the sending process can deliver bits to the receiving process.

- the throughput is $min\{Rc, Rs\}$​, that is, it is the transmission rate of **the bottleneck link.**
- Applying the same analysis as for the two-link network, we find that the throughput for a file transfer from server to client is $min\{R_1, R_2,\dots, R_N\}$​
- Therefore, the constraining factor for throughput in today’s Internet is
  typically the access network.

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240306104410654.webp" alt="image-20240306104410654" style="zoom:50%;" />

- 如果共同链路速率很快，那么就是短板效应

$$
if \quad R>> R_s,R_c\\
then \quad throughput = min\{R_s,R_c\}
$$

- 但如果公用链路限制速率的话，吞吐量就是共同链路的速率了

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240306105533244.webp" alt="image-20240306105533244" style="zoom:33%;" />

### 历史

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240129003408237.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129003507022.png)![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240129003519604.webp)

网景

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240129113040843.webp)

## 网络边缘 edge

网络应用是网络存在的理由

分布式的应用

- CS 模式 client-server（主从模式）可扩展性 非线性下降

- 对等模式 peer-peer  请求和提供资源的端变多了、分布式的、迅雷

面向连接的交互方式：交互前分配资源

## 网络核心 core

数据交换开关

### 电路交换

电话网

独享资源、不共享；可以保证性能

没有数据发送资源就会浪费

线路建立的时间长

可靠性不高

#### 切分方法

频分 FDM frequency division multiplexing

时分 TDM time division multiplexing 时隙 slot

波分 光纤通讯 WDM wave division multiplexing

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123105422145.webp" alt="image-20240123105422145" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123105704164.webp" alt="image-20240123105704164" />

 每个 bit 到达接收端都需要有传播延时

### 分组交换

分成一个个单位 packet，传到相邻路由器 hop；

经过每一个节点，**存储转发**，使用链路全部带宽

资源是按需使用、共享性（支持用户多）

适合通信具有很强突发性

延时：排队时间、存储时间

排队：到达速度》输出速率

缓存用完了会抛弃分组，过度使用会造成网络拥塞

没有固定模式 统计多路复用

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123113304652.webp" alt="image-20240123113304652" />

流量强度为 1 的网络不可行，所以是 0-9

#### 分类

- 数据报网络 datagram - 无连接

不需要握手，每次跳跃都携带目标完整地址，

- 虚电路网络

需要维护呼叫状态，信令

## 网络接入 access

边缘接到核心上

带宽`bps`——`bits per second`

共享/专用

### 有线接入

#### modem

将数据调制在音频信号上、要解调

调幅度、频率、相位

带宽太窄

不需要重新铺基础设施

#### DSL: digital subscriber line

#### 有线电视公司

双向改造，共享带宽

同轴电缆，带宽非对称

#### 电力线可以调制上网

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123122045769.webp" alt="image-20240123122045769" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123122830511.webp" alt="image-20240123122830511" />

### 无线接入

WAN(Wide Area Network)

LAN(Local Area Network)

MAN(Metropolitan Area Network)

PAN(Personal Area Network)

### 物理媒体

#### 导引型媒体

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123123058357.webp" alt="image-20240123123058357" />

两根铜线螺旋绞在一块，抗干扰效果好；空间上保持平行且间距不变

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123123111306.webp" alt="image-20240123123111306" />

光纤优点：光信号不会受到电磁的干扰

缺点：不能折，容易断

**有型介质传的远**

#### 非导引型媒体

**强度 平方反比，迅速衰减**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240123123348917.webp" alt="image-20240123123348917" />

## 协议层次`network protocol`

### 内容

计算机采取分层的方式，下层实现功能，每一层通过层间接口向上层服务

本层协议实现需要依靠下层服务，是为了给上层提供更好的服务

#### 服务 垂直层面 vertical

底层实体向上层实体提供通信的能力

通过原语`primitive` 来操作

提供什么服务 告诉要使用什么服务

#### 协议 水平层面 horizontal

对等层的实体`peer entity`在通信过程中遵守的规则集合

报文格式语法、语义、次序、采取的动作

??? note "一些术语与英文对照"
    `DU: data unit` 数据单元 <br>
    `SAP`服务访问点 区分是哪个上层用户 <br>
    `IDU:interface data unit`<br>
    `SDU: service data unit`上层传的数据<br>
    `PDU: protocol data unit` 协议数据单元 SDU + head<br>
    `ICI: interface control information` <br>

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240125201420011.webp" alt="image-20240125201420011" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240125201113691.webp" alt="image-20240125201113691" />

### 模型

#### Internet

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240125202826044.webp" alt="image-20240125202826044" />

Transport Layer: Process to Process

Network Layer: Node to Node

Link Layer: adjacent Node

Physical Layer

**封装与解封装**

交换机 决定到哪个端口 两层的解封装

路由：全局找路 三层的解封装

**五层结构**

**物理层**`bit` 就是 0101 物理信号或者光信号

**链路层**`frame`以帧为单位，相邻两点（查询网络层携带的端口信息）

​ 网卡：帧的头部形成链路层的帧

**网络层**：端到端传输，源主机到目标主机，以分组为单位

​ `packet`有链接；`datagram`无连接

**传输层**`segment`，进程到进程区分，把网络层不可靠服务变成可靠的服务

**应用层**`message`报文

#### TCP/IP

应用层、运输层、网际层、网络接口层

#### OSI

应用层、表示层、会话层、运输层、数据链路层、物理层

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240125202836339.webp" alt="image-20240125202836339" />

## Top-Down 的实例

以一个 web 页面请求的例子：学生在校园启动一台笔记本电脑：请求和接受 <www.google.com>

### 建立连接

笔记本需要一个 IP 地址，第一跳路由器的 IP 地址，DNS 的地址：采用 DHCP
 DHCP 请求被封装在 UDP 中，封装在 IP, 封装在 802.3 以太网帧中
 以太网的帧在 LAN 上广播 (dest: FFFFFFFFFFFF), 被运行中的 DHCP 服务器接收到
 以太网帧中解封装 IP 分组，解封装 UDP，解封装 DHCP

DHCP 服务器生成 DHCP；ACK 包括客户端 IP 地址，第一跳路由器 IP 地址和 DNS 名字服务器地址

在 DHCP 服务器封装，帧通过 LAN 转发 (交换机学习) 在客户端段解封装

客户端接收 DHCP ACK 应答

客户端有了 IP 地址，知道了 DNS 域名服务器的名字和 IP 地址、第一跳路由器的 IP 地址
<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240217181035891.webp" alt="image-20240217181035891" style="zoom:50%;" />

### ARP

- 在发送 HTTP request 请求之前，需要知道 <www.google.com> 的 IP 地址：DNS
- DNS 查询被创建，封装在 UDP 段中，封装在 IP 数据报中，封装在以太网的帧中。将帧传递给路由器，但是需要知道路由器的接口：MAC 地址：ARP
- ARP 查询广播，被路由器接收，路由器用 ARP 应答，给出其 IP 地址某个端口的 MAC 地址
- 客户端现在知道第一跳路由器 MAC 地址，所以可以发送 DNS 查询帧了

包含了 DNS 查询的 IP 数据报通过 LAN 交换机转发，从客户端到第一跳路由器

### 使用 DNS

IP 数据报被转发，从校园到达 comcast 网络，路由（路由表被 RIP，OSPF，IS-IS 和/或 BGP 协议创建）到 DNS 服务器

- 被 DNS 服务器解封装
- DNS 服务器回复给客户端：www.google.com 的 IP 地址

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240217181241937.webp" alt="image-20240217181241937" style="zoom:50%;" />

### TCP 连接

为了发送 HTTP 请求，客户端打开到达 web 服务器的 TCP socket

TCP SYN 段 (3 次握手的第 1 次握手) 域间路由到 web 服务器

web 服务器用 TCP SYNACK 应答 (3 次握手的第 2 次握手)

TCP 连接建立了！

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__index.assets__image-20240217181349495.webp)

### HTTP 请求与响应

HTTP 请求发送到 TCPsocket 中

IP 数据报包含 HTTP 请求，最终路由到 <www.google.com>

web 服务器用 HTTP 应答回应 (包括请求的页面)

IP 数据报包含 HTTP 应答最后被路由到客户端

**浏览器接收响应并渲染页面**：
    - 浏览器接收到服务器返回的 HTTP 响应后，会解析响应的头信息和内容。
    - 如果内容是 HTML 文件，浏览器会解析 HTML 并根据其中的指令（如加载 CSS 文件、执行 JavaScript 脚本等）进行渲染。
    - 浏览器会逐步构建 DOM 树和 CSSOM 树，并根据它们生成渲染树，最后将内容绘制到屏幕上。

**加载资源**：
    - 如果 HTML 文件中包含了其他资源（如图片、CSS、JavaScript 等），浏览器会根据需要发送额外的 HTTP 请求来加载这些资源。
    - 这些资源加载完成后，浏览器会继续渲染页面，更新显示内容。
