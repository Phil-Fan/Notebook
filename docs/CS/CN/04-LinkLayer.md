---
comments: true
---
# 链路层与局域网 | `Link Layer`

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets___E9_93_BE_E8_B7_AF_E5_B1_82_E4_B8_8E_E5_B1_80_E5_9F_9F_E7_BD_91.svg)

## 链路层服务原理

> 链路层：一个节点把**帧**通过链路传送到另外一个节点
>
> 网络层：端到端
>
> 传输层：区分进程、不可靠变成可靠
>
> 应用层：交换报文，形成网络应用

**广域网使用单点连接**

**局域网使用多点连接**

在子网的内部实现点到点 point to point

**网卡 NIC**实现链路层和相应物理层的功能

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217114915691.webp)

### 服务 1：成帧

- 节点 `node`
- 链路 `link`
- 帧 `frame`PDU

在帧头部使用“MAC”（物理）地址来标示源和目的

### 服务 2：EDC 检错和纠错

 Error Detection and Correction 差错检测和纠正位**在相邻两个节点之间完成可靠数据传递**

- 低差错率，不控制

- 高差错率，上层代价大所以要控制

### 服务 3：链路接入

MAC 协议规定了帧在链路上传输的规则。用于协调多个节点的帧传输

### 服务 4：全双工、半双工

半双工：双向传输，一次一个方向

全双工：双向传输，同时收发

## 差错检测 | EDC

### 奇偶检验

单 bit 奇偶校验：检测单个 bit 级错误

偶检验，加上一个冗余位，使得整行 1 的个数是偶数个，可以检验出奇数个 bit 错误

2 维奇偶校验：检测和纠正单个 bit 错误，可以定位到行列，进而进行纠正

无法检验对偶错误

### 检验和

更多用于传输层

软件层实现，所以需要更快的速度

### CRC（循环冗余校验）

> 此部分参考了[[CRC 校验\]手算与直观演示动画](https://www.bilibili.com/video/BV1V4411Z7VA/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

1. 模二运算（异或）

2. 使用位串的方式约定一个多项式，r 次方，r+1 位

3. 发送方 sender 有 D 位，向左移动 R 位补零

   接收方用位串除以（从左往右按位异或）多项式得到余数 R，即为校验

$$
&D\cdot 2^r\oplus R = n\cdot G\\
&\Rightarrow D\cdot 2^r\oplus R \oplus R = n\cdot G \oplus R\\
&\Rightarrow D\cdot 2^r = n\cdot G \oplus R\\
&\therefore R= remainder[\frac{D\cdot 2^r}{G}]\\
$$

例子：

$$
&D = 101110\\
&G = 1001(r=3)\\
&R = D<<3/G = remainder[\frac{101110000}{1001}] = 011
$$

CRC 检错性能描述

- 能够检查出所有的 1bit 错误
- 能够检查出所有的双 bits 的错误
- 能够检查出所有长度$=r$或者$<r $位的错误
- 出现长度为$r+1$的突发错误，检查不出的概率是$\frac{1}{2^{r-1}}$
- 现长度大于`r+1`的突发错误，检查不出的概率$\frac{1}{2^r}$

## 多点接入 | MAP

 MAC `media access control`

设计一个分布式算法，协调各个节点对信道访问和使用

**存在问题**：碰撞问题，广域网多点连接碰撞代价特别大

2 个或更多节点同时传送：冲突（`collision`）

必要条件：

1. 当一个节点要发送时，可以 R 速率发送。
2. 当 M 个节点要发送，每个可以以 R/M 的平均速率发送
3. 完全分布的：没有特殊节点协调发送；没有时钟和时隙的同步
4. 简单

### 信道划分

- 把信道划分成小片（时间、频率、编码）
- 分配片给每个节点专用

TDMA: time division multiple access 分时

FDMA: frequency division multiple access 分频（类似鲸鱼蝙蝠不同频率

CDMA (code division multiple access) 分码（类似方言

### 随机访问

- 信道不划分，允许冲突
- **如何检测冲突**
- **冲突后恢复**

#### 时隙 ALOHA

时隙`slot`

所有节点在信 道上保持同步

在有限信道发，检测冲突，如果有碰撞，下一时隙按照概率 p 进行发送（服从二项分布）

信道状态：**碰撞的 C、空闲的 E、成功的 S**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217123812413.webp" alt="image-20240217123812413" style="zoom:50%;" />

##### 优点

- 节点可以以信道带宽全速连续传输
- 高度分布：仅需要节点之间在时隙上的同步
- 简单

##### 缺点

- 存在冲突，浪费时隙

- 即使有帧要发送，仍然有可能存在空闲的时隙

- 节点检测冲突的时间<帧传输的时间；必须传完

  > 鸡蛋坏了也要吃完

- 需要时钟上同步

##### 效率分析

当有很多节点，每个节点有很多帧要发送时，x%的时隙是成功传输帧的时隙

最大效率

$$
f(N,P) = N\cdot P (1-P)^{N-1}\\
f_{max} = 37.5\%
$$

#### Pure ALOHA

任何时间有帧形成，就将帧放出去

- 简单，无需时间同步

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217124359578.webp)

frame time

bit time

**效率低于时隙 ALOHA**

$$
\begin{align}
f(N,P) &= N\cdot P (1-P)^{N-1} \cdot(1-P)^{N-1}
\\
&= N  \cdot P\cdot (1-P)^{2(N-1)} \\
f_{max} &= 17.5\%
\end{align}
$$

#### CSMA

> 说之前听一下别人是否再说话，不要打断别人正在进行的说话！

`carrier sense`

监听信道直至信道空闲位置

如果侦听到信道空闲，传送整个帧；如果侦听到信道忙，推迟传送

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217125439610.webp" alt="image-20240217125439610" style="zoom:50%;" />

- **仍然会发生冲突**(局部探知全局情况不可靠)

各个节点通过局部 sense 得到全局状态，最远两个节点的时间越长，冲突可能性就越大

整个冲突帧的传输时间都被浪费了，是无效的传输 (红黄区域)

#### CSMA/CD（Ethernet）

`collision detection` 冲突检测

> 一边发送，一边监听，检测到冲突就停止发送

**过程分析**

1. 适配器获取数据报，创建帧

2. 发送前：侦听信道 CS<br>

   1) 闲：开始传送帧<br>
   2) 忙：一直等到闲再发送<br>

3. 发送过程中，冲突检测 CD<br>
   1) 没有冲突：成功<br>
   2) 检测到冲突：放弃，之后尝试重发<br>
4. 发送方适配器检测到冲突，除放弃外，还**发送一个 Jam 信号**，所有听到冲突的适配器也是如此；防止冲突太短听不到；

5. `exponential backoff`二进制指数退避算法<br>

  如果放弃，适配器进入指数退避状态在第 m 次失败后，适配器随机选择一个${0,1,2,\dots,2^m-1}$中选择 K<br>

  等待$K*512$位时，然后转到步骤 2<br>碰撞窗口最大是 1024

  等待时间增加了<br>

> "了不得啦，这里有冲突啊啊啊啊"
>
> 强化冲突：让所有站点都知道冲突
>
> 第一次碰撞：在$\{0,1\}$中选择 K，延时$K*512$位时
>
> 第二次：在$\{0,1,2,3\}$中选择 K，延时$K*512$位时

**效率分析**

| 量          | 含义                           |
| ----------- | ------------------------------ |
| $T_{prop}$  | LAN 上 2 个节点的最大传播延迟     |
| $t_{trans}$ | 传输最大长度的以太网的帧的时间 |

$$
efficiency = \frac{1}{1+5T_{prop}/t_{trans}}
$$

效率变为 1

- 当$T_{prop}$ 变成 0 时
- 当$t_{trans}$​ 变成无穷大时 (某个节点 800T，一旦抓住信道就不放手了)
- 比 ALOHA 更好的性能，而且简单，廉价，分布式！

#### CSMA/CA(WLAN)

`collision avoidance` 冲突避免

有基础设施`infrastructure`

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240418000656125.webp)

802.11: **没有冲突检测，做不了 CD**

- 无法检测冲突：自身信号远远大于其他节点信号；有衰减
- 即使能 CD：不冲突 != 成功<br>
  - 无法 CD，一旦发送一股脑全部发送完毕，不 CD<br>
  - 为了避免无 CD 带来的信道利用率低的问题，事前进行冲突避免<br>

- 冲突也有可能是成功的

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240418001217281.webp)

无线链路特性，需要每帧确认；例如：由于隐藏终端问题，在接收端可能形成干扰，接收方没有正确地收到。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240418001048962.webp" alt="image-20240418001048962" style="zoom:33%;" />

??? +note "2 个站点有数据帧需要发送，第三个节点正在发送"
    === "WLAN CA"

        - 无法 CD，一旦发送就必须发完，如冲突信道浪费严重，代价高昂<br>
        - 思想：尽量事先避免冲突（抛骰子），而不是在发生冲突时放弃然后重发<br>
        - 听到发送的站点，分别选择随机值，回退到 0 发送<br>
          - 不同的随机值，一个站点会胜利<br>
          - 失败站点会冻结计数器，当胜利节点发完再发<br>
    
    === "LAN CD"
        让 2 者听完第三个节点发完，立即发送<br>
            冲突：放弃当前的发送，避免了信道的浪费无用于冲突帧的发送<br>
            代价不昂贵<br>

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217160017462.webp" alt="image-20240217160017462" style="zoom:50%;" />

无法完全避免冲突；只有单向冲突，通过预约和管理解决冲突

**CSMA/CA 协议工作原理 :**

> 参考博文<https://blog.csdn.net/shulianghan/article/details/108116406>

① 检测信道 : 发送数据前 , 检测信道是否空闲 ;

② 信道空闲 : 发出 RTS ( Request To Send ) , RTS 包括 发射端地址 , 接收端地址 , 发送持续时间 等信息 ;

③ 信道忙 : 等待 ;

④ 接收端收到 RTS : 发送 CTS ( Clear To Send ) 响应 ;

⑤ 发送端收到 CTS : 同时执行以下两个操作 ;

- 发送数据 : 开始发送数据帧 ;
- 预约信道 : 告知其它站点 , 自己要传输数据 , 并给出传输时间 ;

⑥ 接收方接收到数据后 , 使用 CRC 循环冗余校验码 校验 数据是否正确 , 如果数据正确 , 返回 ACK 确认帧 ;

⑦ 发送方接收到 ACK 确认帧 后 , 才进行下一帧的发送 , 如果没有收到 , 则一直重传 , 直到 16 1616 次失败为止 ; ( 二进制指数退避算法 )

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217160450274.webp" alt="image-20240217160450274" style="zoom:50%;" />

#### 线缆接入网络

下行 CMTS 一个

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217160813735.webp" alt="image-20240217160813735" style="zoom:50%;" />

多个 40Mbps 下行 (广播) 信道，FDM
 下行：通过 FDM 分成若干信道，互联网、数字电视等<br>
 互联网信道：只有 1 个 CMTS 在其上传输<br>
多个 30 Mbps 上行的信道，FDM
 多路访问：所有用户使用；接着 TDM 分成微时隙<br>
 部分时隙：分配；部分时隙：竞争；<br>

`DOCSIS: data over cable service interface spec`

### 依次轮流 Taking Turns

- 节点依次轮流
- 有很多数据传输的节点可以获得较长的信道使用权

#### 论询

主节点邀请从节点依次传送

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217161518137.webp" alt="image-20240217161518137" style="zoom:25%;" />

**缺点：**

- 轮询开销：轮询本身消耗信道带宽
- 等待时间：每个节点需等到主节点轮询后开始传输，即使只有一个节点，也需要等到轮询一周后才能够发送
- **单点故障**：master 故障，整个系统失效

#### 令牌传递

> 击鼓传花

控制令牌 (`token`) 循环从一个节点到下一个节点传递

令牌报文：**特殊的帧**，1 是令牌，0 是数据

当一个节点收到令牌，仅当其有帧要传输才接受，否则向下一个节点转发

**优点：**分散的、效率较高

**缺点：**

- 令牌开销：本身消耗带宽
- 延迟：只有等到抓住令牌，才可传输
- 单点故障 (token)：令牌丢失系统级故障，整个系统无法传输
- 复杂机制重新生成令牌

## LAN `Local Area Network`

### MAC `medium access control`

前 n-1 跳：用于使数据报到达目的 IP 子网；

最后一跳：到达子网中的目标节点

LAN（MAC/物理/以太网）地址：

MAC 地址，6 字节 48bit；**FF-FF-FF-FF 广播地址**

MAC 地址由 IEEE 管理和分配，制造商购入 MAC 地址空间（固定前 24bit，后 24bit 公司自己生成）

??? note "IP 地址分层，mac 地址在一个平面"
    网卡在生产时不知道被用于哪个网络，因此给网卡一个唯一的标示，用于区分一个网络内部不同的网卡即可<br>
    === "分离好处"
        a) 网卡坏了，ip不变，可以捆绑到另外一个网卡的mac上<br>
        b) 物理网络还可以除IP之外支持其他网络层协议，链路协议为任意上层网络协议， 如IPX等<br>

    === "捆绑的问题"
        a) 如果仅仅使用IP地址，不用mac地址，那么它仅支持IP协议<br>
        b) 每次上电都要重新写入网卡IP地址；<br>
        c) 另外一个选择就是不使用任何地址；不用MAC地址，则每到来一个帧都要上传到IP层次，由它判断是不是需要接受，干扰一次<br>

LAN 中，“不碰” = 成功

条件是 $帧>= 2\tau$

### ARP: `Address Resolution Protocol`

> 完成 IP 地址到 MAC 地址的转换；
>
> 从而完成把分组封装帧，从一个网卡发送到另一个网卡

#### 向子网内

ARP 只为在同一个子网上的主机和路由器接口解析 IP 地址

> 云南节点试图用 ARP 解析美国的节点的 IP 地址，将返回错误

**ARP 表：**

包括一些 LAN 节点 IP/MAC 地址的映射`< IP address; MAC address; TTL >`

TTL 时间是指地址映射失效的时间；典型是 20min

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240426140148724.webp)

ARP 表中没有目标主机的项目：

- 发送方构造一个 ARP packet，有几个字段，包括发送和接受 IP 地址&MAC 地址

- 向适配器发送一个 ARP 查询分组，适配器用 MAC 广播地址（`FF-FF-FF-FF-FF-FF`）发送分组
- 每个适配器检查目标 IP 和自己是否匹配，匹配的发送一个响应 ARP 分组，更新源适配器的 ARP 表

!!! note "查询 ARP 报文是在广播帧发送的，响应 ARP 报文是在标准帧中发送的"

#### 向子网外查询

假如`111.111.111.111`想发送到`222.222.222.222`

- 创建帧，包含寻址到目标的数据包，发送到子网 1
- 子网 1 传输到网络层，根据路由器的转发表，转发到另一个接口
- 封装到新的帧当中，把帧发送到子网 2

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240426140231136.webp" alt="image-20240426140231136" style="zoom:50%;" />

### Ethernet

最主流的 LAN 技术：98% 占有率；廉价；带宽不断提升

#### Topology

使用同轴电缆链接

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240418090302357.webp)

**总线**

在上个世纪 90 年代中期很流行

- 所有节点在一个碰撞域内，**任意时刻只允许一个节点发送**，降低利用率
- 可靠性差，如果介质破损，形成反射，误认为是冲突，总是冲突

**星型**

目前最主流

连接选择：hub 或者 switch；现在一般是交换机在中心

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240418090518781.webp)

#### 以太帧类型

发送方适配器在以太网帧中封装 IP 数据报

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240426142902476.webp)

- 前导码：用来同步接收方和发送方的时钟，前 7 字节`10101010`，最后一字节`10101011`，用于警告目标适配器，重要信息要来了
- 数据字段：46-1500 字节。承载 IP 数据报。MTU 是 1500 字节，多余 1500 要进行分片。数据字段最小长度 46 字节，IP 数据报小于 46 字节，数据报必须被填充到 46 字节。
- 目的地址 6 字节：目的适配器的 MAC 地址
- 源地址 6 字节
- 类型字段 2 字节：除了 IP 之外的网络层协议，如 ARP，IPX。
- CRC 4 字节

- 无连接：帧传输前，发送方和接收方之间没有握手（本身可靠性较高
- 不可靠：接收方适配器不发送 ACKs 或 NAKs 给发送方

使用 MAC 协议：CSMA/CD 二进制指数退避算法

### 链路层的设备

#### Hub 集线器

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217173640472.webp" alt="image-20240217173640472" style="zoom:50%;" />

高负载下性能差

#### 交换机

**链路层设备**：扮演主动角色（端口执行以太网协议），对帧进行存储转发

**透明**：主机对交换机的存在可以不关心；通过交换机相联的各节点好像这些站点是直接相联的一样

**即插即用，自学习**：交换机无需配置

**交换表**

> **过滤 filtering** 决定一个帧应该转发到某个接口还是应当丢弃
>
> **转发 forwarding** 决定一个帧应该被导向那个接口，并移动到对应接口

MAC 地址 + 对应端口 + 时戳

| `MAC addr` | interface | TTL  |
| ---------- | --------- | ---- |
| A          | 1         | 60   |
|            |           |      |

目的地址为 A 的帧来自接口 x

- 没有这个表项：泛洪 flooding，向所有接口转发帧的副本<br>
- 表中有表项，目的地址和源接口一致（A-x），则这个帧直接过滤<br>
- 转发：知道目标 A 对应的接口（$A-y| y\ne x$​)：选择性发送到那个端口<br>

即插即用，**自学习**

- 交换表初始为空
- 当接收到帧，交换机学习到发送站点所在的端口（网段），记录源目标 MAC 和端口在交换表中（软状态维护机制
- 一段时间后，TTL 后，删除掉这个帧。

**交换机可以级联**：有生成树算法，每个时刻工作的只有一颗树，防止广播式传播

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217175712364.webp" alt="image-20240217175712364" style="zoom:50%;" />

### VLANS

带有 VLAN 功能的交换机（们）可以被配置成：一个物理 LAN 基础设施，虚拟成多个 LANs

如果有多个交换机，希望它们相连并且共享 VLANs 信息

- 方法 1：各交换机每个 VLAN 一个端口和另外交换机相应；VLAN 端口相连->扩展性问题
- `trunk port`干线端口：多个交换机共享定义的 VLAN，在它们之间传输帧

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__04-LinkLayer.assets__image-20240217180329788.webp" alt="image-20240217180329788" style="zoom:50%;" />
