---
comments: true
---
# 应用层 | Application Layer

> Perhaps what appeals the most to users is that the Web operates on demand. Users receive what they want, when they want it.

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets___E5_BA_94_E7_94_A8_E5_B1_82.svg)

| 对比 | HTTP | FTP | SMTP | POP3 | IMAP | DNS | BitTorrent |
| -------------- | ------ | --------- | ------ | ---- | ---- | ---- | ---------- |
| 中心/去中心 | | | | | | | |
| 有/无状态 | 无 | 有 | 有 | 无 | 有 | | |
| 可靠/不可靠 | | | | | | | |
| 使用传输层协议 | TCP:80 | TCP:21,20 | TCP:25 | TCP | TCP | UDP | TCP |

## 原理

### 传输层服务模型

#### 标示 寻址

SAP

- 唯一的 IP 地址（主机是哪个）
- 采用的传输层协议 TCP/UDP
- 端口号 Port Number（16bit 65536）

#### 层间的信息

- 层间接口

报文 SDU

谁发的：IP+port（TCP/UDP）

发给谁：IP+port

- 传输层实体对报文封装

源端口号，目标端口号，数据

IP 交给下方

### 网络应用体系架构

#### Client-Server

服务器在固定端口一直运行，固定 ip

服务器是中心，资源在服务器

可扩展性较差，CS 模式随连接数量断崖式下降

> the process that initiates the communication is labeled as the client
>
> the process that waits to be contacted to begin the session is the server

#### Peer-to-Peer

### 衡量指标

- reliable data transfer 可靠性的

- throughput

- timing:打电话、游戏

- security

### 传输层提供的服务

UDP：不可靠 无连接

TCP：可靠、流量控制、拥塞控制、面向连接

## 网络应用实例

协议：报文格式语法、语义、次序、采取的动作

### WEB & HTTP

URL `Uniform Resource Locator`统一资源定位符

HTTP stands for `HyperText Transfer Protocol`超文本传输协议

协议名 用户 口令 主机名 路径名 端口

![image](https://data.educoder.net/api/attachments/509266)

web 页有对象组成，通过 URL 对每个对象进行引用

HTTP 超文本传输协议

web 的应用层协议；TCP 之上；CS 模式

S1 属于守护进程（waiting socket），监视 80 端口，客户端有请求时候经过握手建立连接 socket

无状态服务器

#### 报文

请求、相应

参考文章：[HTTP 请求报文和响应报文格式](https://zhuanlan.zhihu.com/p/346408612)

请求行、请求头、空白行 (`\r\n`)、请求体

![image](https://data.educoder.net/api/attachments/579830)

##### 请求报文

one-to-one,one response for one request

- 请求行

由三部分构成：第一部分说明请求类型为 get 方法请求，第二部分（用/分开）是资源 URL，第三部分说明使用的是 HTTP1.1 版本。

```http
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
User-agent: Mozilla/4.0
Connection: close
Accept-language:fr
```

- 请求方法

`GET`和`POST`是最常见的 HTTP 方法，除此以外还包括`DELETE`、`HEAD`、`OPTIONS`、`PUT`、`TRACE`

<img src="https://data.educoder.net/api/attachments/510692" alt="预览大图" style="zoom:50%;" />

> get 和 post 的区别
>
> 1. get 直接在浏览器输入，post 需要工具发送请求；
> 2. get 用 url 或者 cookie 传参，post 将数据放在 body 中；
> 3. get 的 URL 有长度限制，post 数据可以非常大；
> 4. post 比 get 安全，因为 URL 看不到数据；
> 5. get 用来获取数据，post 用来发送数据。

- URL 地址
- 协议名称和版本号

???+abstract "请求报文头"
    - Accept：用于告诉服务器，客户机支持的数据类型（例如：`Accept:text/html,image/*`）；
    - Accept-Charset：用于告诉服务器，客户机采用的编码格式；
    - Accept-Encoding：用于告诉服务器，客户机支持的数据压缩格式；
    - Accept-Language：客户机语言环境；
    - Host：客户机通过这个头，告诉服务器想访问的主机名；
    - If-Modified-Since：客户机通过这个头告诉服务器，资源的缓存时间；
    - Referer：客户机通过这个头告诉服务器，它（客户端）是从哪个资源来访问服务器的（防盗链）；
    - User-Agent：客户机通过这个头告诉服务器，客户机的软件环境（操作系统，浏览器版本等）；
    - Cookie：客户机通过这个头，将 Coockie 信息带给服务器；
    - Connection：告诉服务器，请求完成后，是否保持连接；

- **Date**：header line indicates the time and date when the HTTP
     response was created and sent by the server. **Note that this is not the time when the object was created or last modified; it is the time when the server retrieves the object from its file system, inserts the object into the response message, and sends the response message.**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__v2-98df69e7e8fccd46bfe03cc473784766_1440w.webp" alt="img" style="zoom: 50%;" />

##### 响应报文

一个状态行，若干个消息头，以及实体内容

- 报文协议及版本；
- [状态码 (status code) 及状态描述 (status code description)](https://mp.weixin.qq.com/s/xxxS5qG244F6L10Y_ZxyGQ)

???+bug "注意"
 **谨记状态码和状态描述的区别**<br>
 状态码 (status code)<br>
 状态描述 (status code description)<br>

```HTTP
description:
200: OK
301: Moved Permanently
400: Bad Request
404: Not Found
505: HTTP Version Not Supported
502: Bad Gateway
```

| 状态码 | 类别 | 原因 |
| :----: | :-----------------------: | :----------------: |
| 1xx | `Informational`信息状态码 | 正在处理 |
| 2xx | `Success`成功状态码 | 正常处理 |
| 3xx | `Redirection`重定向 | 需要附加操作 |
| 4xx | `Client Error`客户端错误 | 请求出错，无法处理 |
| 5xx | `Server Error` | server 处理出错 |

- 响应报文头

???+abstract "响应报文头"
    响应头有若干个字段组合（根据具体情况选择），常见字段及其含义如下：<br>
    - `Content-Type`：服务器给客户端传回来的文件格式； <br>
    - `Content-Length`：这个是返回的实体在压缩之之后的长度为 8 byte； <br>
    - `Last-Modified`：文档的最后改动时间；<br>
    - `ETag`：这个响应头中有种<br>
    - `Weak Tag`，值为`W/“xxxxx”`。它声明`Tag`是弱匹配的，只能做模糊匹配，在差异达到一定阈值时才起作用； <br>
    - `Accept-Ranges`：表示该服务器是否支持文件的范文请求； <br>
    - `Server`：设置服务器名称； <br>
    - `Date`：当前 GMT 时间，这个就是你请求的东西被服务器创建的时间。<br>

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__v2-2f86d3626184a4fc8b8fed6008419055_1440w.webp)

!!! note
 TCP 不维护报文长度，需要 HTTP 自己去断句

#### `cookies`用户 - 服务器状态

[Session、Cookie、Cache、Token 分别是什么及区别](https://blog.csdn.net/xuhang1993/article/details/71164596)

`Cookie`就是这样的一种机制。让无状态的 HTTP 有一定记忆

在`Session`出现之前，基本上所有的网站都采用`Cookie`来跟踪会话。

`Cookie`实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用 response 向客户端浏览器颁发一个`Cookie`。客户端浏览器会把`Cookie`保存起来。当浏览器再请求该网站时，浏览器把请求的网址连同该`Cookie`一同提交给服务器。服务器检查该`Cookie`，以此来辨认用户状态。服务器还可以根据需要修改`Cookie`的内容。

作用：自动登录、进行统计

威胁：

第三方`cookie`：泄露隐私；广告营销；

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318152447148.webp" alt="image-20240318152447148" style="zoom:50%;" />

大多数门户网站使用

1) 在 HTTP 响应报文中有一个 cookie 的首部行<br>
2) 在 HTTP 请求报文含有一个 cookie 的首部行<br>
3) 在用户端系统中保留有一个 cookie 文件，由用户的浏览器管理<br>
4) 在 Web 站点有一个后端数据库<br>

##### **`Session`**

会话关系

Session 保存在服务器上。客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是 Session。客户端浏览器再次访问时只需要从该 Session 中查找该客户的状态就可以了

##### **Token**

token 就是令牌，比如你授权（登录）一个程序时，他就是个依据，判断你是否已经授权该软件。
当客户端请求页面时，服务器会生成一个随机数 Token，并且将 Token 放置到 session 当中，然后将 Token 发给客户端（一般通过构造 hidden 表单）。下次客户端提交请求时，Token 会随着表单一起提交到服务器端。

##### **Session 与 Cookie 的区别**

Cookie 和 Session 都是为了保存客户端和服务端之间的交互状态最大的区别就是 Cookie 是保存在客户端而 Session 就保存在服务端的。

- **Cookie**：存储在客户端的小型文本文件，通常用于存储用户的偏好设置、身份验证信息等。
  - **示例**：用户登录后，服务器发送一个包含用户 ID 的 Cookie 到客户端，客户端在后续请求中自动包含该 Cookie，以便服务器识别用户。
  - **Cookie 劫持**：攻击者通过 XSS 攻击或其他手段获取用户的 Cookie，从而冒充用户身份。
  - Cookie 是客户端请求服务端时服务器会将信息以键值给客户端，保存在浏览器中<br>用 Cookie 就可以方便的做一些缓存。
  - Cookie 缺点：是大小和数量都有限制；Cookie 是存在客户端的可能被禁用、删除、篡改，是不安全的；Cookie 如果很大，影响了传输效率。
- **Session**：存储在服务器端的临时数据存储区域，通常用于存储用户的会话状态信息。
  - **示例**：用户登录后，服务器创建一个 Session，并将 Session ID 通过 Cookie 发送给客户端。客户端在后续请求中包含该 Session ID，服务器根据 Session ID 查找对应的 Session 数据。
  - 如果服务器被攻破，Session 中就可能有一些敏感信息。
  - Session 是基于 Cookie 来实现的，不同的是 Session 本身存在于服务端，但是每次传输的时候不会传输数据，只是把代表一个客户端的唯一 ID（通常是 JSESSIONID）写在客户端的 Cookie 中传输。Session 的优势就是传输数据量小，比较安全。但是 Session 也有缺点，就是如果 Session 不做特殊的处理容易失效、过期、丢失或者 Session 过多导致服务器内存溢出

#### `cache` - Web 缓存

WEB 缓存一般分为浏览器缓存、代理服务器缓存以及网关缓存。

WEB 缓存就在服务器 - 客户端之间搞监控，监控请求，并且内容另存一份（统称为副本）；

然后，如果下一个请求是相同的  URL，则直接请求保存的副本，而不是再次访问资源服务器。

对用户：快 减小响应时间

服务器：减小 web 服务器载荷

网络：网络压力更小，减小传输成本

<img src="https://data.educoder.net/api/attachments/543498" alt="预览大图" style="zoom:50%;" /><img src="https://data.educoder.net/api/attachments/543499" alt="预览大图" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318152538396.webp" alt="image-20240318152538396" style="zoom:50%;" />

end2end delay with cache

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129160059732.webp)

解决办法

- 更快的接入链路：花钱多

- 安装本地缓存

  - 本地访问 $t_1$ 概率$P_1$

  - 远程访问$t_2$ 概率$P_2$

    总延时

    $$
    \begin{align}
    T &= P_1\cdot t_1 + P_2 \cdot t_2\\
    t &= \frac{I}{1-I}\frac{L}{R}\\
    I &= \frac{aL}{R}
    \end{align}
    $$

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129160659497.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129160713797.webp)

互联网上大家看的内容都是相似的，缓存的存在可以缓解流量压力

##### `conditional GET`

- 存在问题：如果本地缓存版本落后于远端

  解决：`If-modified-since: <date>`

  向主机请求最后修改，如果被修改再发送一遍；没有被修改则就发一个没有修改的头部即可

  Server

```http
HTTP/1.0 304 Not Modified
```

```http
HTTP/1.0 200 Modified
```

- 200 请求成功，浏览器会把响应回来的信息显示在浏览器端；
- 304 第一次访问一个资源后，浏览器会将该资源缓存到本地；第二次再访问该资源时，如果该资源没有发生改变或失效，那么服务器响应给浏览器 304 状态码，告诉浏览器使用本地缓存的资源。

HTTP 响应时，如何判断是该返回 200 还是 304 呢？与之相关的字段是：  

**Last-Modified：** 表示这个响应资源的最后修改时间

**If-Modified-Since**：当资源过期时（使用 Cache-Control 标识的 max-age），发现资源具有 Last-Modified 声明，则再次向 WEB 服务器请求时，带上 If-Modified-Since，表示请求时间。</br>WEB 服务器收到请求后发现有 If-Modified-Since 则与被请求资源的最后修改时间进行比对。HTTP200 说明改动过，重新发送，HTTP304 无需报体，直接发送，使用缓存

#### 嵌入对象

在网页中嵌入对象，实际上并不会在网页中插入对象，而是通过某种标签链接到指定的对象，标签创建的只是被引用对象的占位符而已。

- 嵌入图像

URL 可以使用完整的位置，如：    `<img src="assets/01-ApplicationLayer.assets/flower.jpg" alt="flower">`

也可以使用相对位置如：    `<img src="flower.jpg" alt="flower">`

- 嵌入声音
- 嵌入 flash 动画

连接方式

对网页进行请求外，需要对每一个嵌入对象进行请求；可以采用串行或者并行的方式；

<img src="https://data.educoder.net/api/attachments/579896" alt="预览大图" style="zoom:50%;" />

实际上并行不一定更快的。客户端的网络带宽不足时，大部分的时间可能都是用来传送数据的。在这种情况下，一个连接到速度较快服务器上的 HTTP 事务就会很容易地耗尽所有可用的 Modem 带宽。如果并行加载，每个对象可能会去竞争有限的带宽，每个对象都会以较慢的速度按比例加载，这样带来的性能提升就很小，甚至没有提升。

另外，打开大量连接会消耗很多内存资源，从而引发自身的性能问题。复杂的 WEB 页面可能会有数十或数百个内嵌对象。客户端可能可以打开数百个连接，但服务器通常要同时处理很多其他用户的请求，所以很少有 WEB 服务器希望出现这样的情况。这会造成服务器性能的严重下降，对高负荷的代理来说也同样如此。

#### 持久连接

- 非持久

Although HTTP uses persistent connections in its default mode HTTP clients and servers can be configured to use non-persistent connections instead.

HTTP has nothing to do with how a Web page is interpreted by a client.

Non persistent TCP connection transports exactly one request message and one response message

HTTP1.1

TCP 建立连接-》HTTP 请求-》连接不关闭可以多次请求

**An entire Web page can be sent over a single persistent TCP connection.**

Multiple Web pages residing **on the same server** can be sent from the server to the same client over a single persistent TCP connection.只要是在一个 web server 就可以持久连接

重用已对目标服务器打开的空闲持久连接，就可以避开缓慢的链接建立阶段。而且已经打开的链接还可以避免慢启动的拥塞适应阶段，以便更快速地进行数据传输。

除非特别指明，否则 HTTP/1.1 假定所有连接都是持久的。要在事务处理结束之后将连接关闭，HTTP/1.1 应用程序必须向报文中显示地添加一个 `Connection：close` 首部。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129150803208.webp)

持久连接有两种类型：比较老的 HTTP/1.0+"keep-alive" 连接，

以及现代的 HTTP/1.1“persistent”连接。

#### 时间分析

<img src="https://data.educoder.net/api/attachments/579897" alt="预览大图"  />

RTT `round trip time`

> RTT is the time it takes for a small packet to travel from client to server and then back to the client.

TCP 三次握手（前面 1 个 RTT+ 一个去程）

一个 RTT 发起 TCP 连接

一个 2RTT 发起 and 接受 HTTP 请求

文件传输时间：2RTT+ 传输文件

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318164420937.webp" alt="image-20240318164420937" style="zoom:50%;" />

Pipeline

流水线方式，一个请求还没有接受回复就发出下一个请求

所以使用时间是 = 1 个 RTT 建立连接 + 发送 n 个包的时间

没有 Pipeline：

1 个 RTT 建立连接，n 个 RTT 发送

#### HTTP/2

- Framing: The ability to break down an HTTP message into **independent frames**, interleave them, and then reassemble them on the other end is the single most important enhancement of HTTP/2.

- it can prioritize the responses it is requesting by assigning a weight between 1 and 256 to each message.当客户端请求网页时，服务器会一次性将多个数据流发送到客户端，而不是逐个依次发送。这种数据传输方法称为多路复用。开发人员可以为这些数据流分别分配一个不同的加权值，该值告诉客户端首先要呈现哪个数据流。

> 现在，假设鲍勃决定以 HTTP/2 方式将小说发送给爱丽丝：这时，他分开发送小说的各个章节（以保持在邮局的大小限制内），但一次性发送了所有章节。他还为每一章编号：第 1 章、第 2 章，等等。现在，爱丽丝同时收到整部小说，并可以按自己的时间以正确的顺序进行编排。

- **多路复用：** HTTP/1.1 依次加载各个资源，因此，如果无法加载某一资源，它将阻碍其后的所有其他资源。相比之下，HTTP/2 可以使用单个 TCP 连接来一次发送多个数据流，使得任何资源都不会会阻碍其他资源。为此，HTTP/2 将数据拆分为二进制代码消息并为这些消息编号，以便客户端知道每个二进制消息所属的流。

- **服务器推送：** 通常，服务器仅在客户端要求时才向客户端设备提供内容。但是，这种方法并不总是适用于现代网页，因为现代网页通常涉及客户端必须请求的数十个独立资源。HTTP/2 通过允许服务器在客户端请求之前向客户端“推送”内容来解决此问题。服务器还发送一条消息，让客户知道预期推送的内容是什么，就像 Bob 在发送整本书之前向 Alice 发送小说目录一样。

- **标头压缩：** 小文件的加载速度比大文件快。为了提高 Web 性能，HTTP/1.1 和 HTTP/2 都会压缩 HTTP 消息以使其更小。但是，HTTP/2 使用一种称为 HPACK 的更高级压缩方法，可以消除 HTTP 标头数据包中的多余信息。这样可以从每个 HTTP 数据包中消除几个字节。考虑到即使只加载一个网页时所涉及的 HTTP 数据包的数量，这些字节会迅速累加，从而加快了加载速度。

#### HTTP3

[HTTP & QUIC 简介](https://segmentfault.com/a/1190000045016079)
HTTP/3 将是自 2015 年 HTTP/2 获得批准以来对超文本传输协议的第一次重大升级。

HTTP/3 的一个重要区别是它在一种新的传输协议 QUIC 上运行。QUIC 专为移动密集型互联网使用而设计，在这种环境中，人们携带的智能手机会在一天中不断地从一个网络切换到另一个网络。开发第一个互联网协议时情况并非如此：当时设备的便携性较差，且不经常切换网络。

**QUIC 协议的设计目标是在高延迟和不稳定的网络环境下提高网络应用程序的性能和可靠性。**

QUIC（Quick UDP Internet Connections）是一种由 Google 开发的基于 UDP 的传输层协议，旨在提高网络通信的速度和效率。它通过实现低延迟的连接建立、多路复用的数据传输、网络路径迁移以及安全措施，确保了数据传输的保密性、完整性和可用性。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__20240705193308.webp)

- 开发一种方法来解决当智能手机从 WiFi 切换到蜂窝数据时（例如离开家或办公室时）性能缓慢的问题
- **减少丢包的影响**——当一个信息包没有到达目的地时，它不会再阻塞所有的信息流（称为“队头阻塞”的问题）

- **更快的连接建立**：QUIC 允许 TLS 版本协商与加密和传输握手同时发生
- **零往返时间 (0-RTT)**：对于它们已经连接的服务器，客户端可以跳过握手要求（互相确认和验证以确定它们将如何通信的过程）
- **更全面的加密：** QUIC 的新握手方式将默认提供加密，这是对 HTTP/2 的巨大升级，并将有助于减轻攻击的风险

!!! note "一个著名的用了都说好的下载器 IDM 可以加速你的网络下载速度，是什么原理？又是如何实现的？"
  [IDM 原理](https://wenku.csdn.net/column/4jy5mn0ays)
  如果网站不支持断点续传就没法加速了

### FTP

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129163627900.webp)

有状态、双通道

- 向远程主机上传输文件或从远程主机接收文件

- 客户/服务器模式

- ftp 服务器：端口号为 21

- 控制命令的发出和数据的传输在不同的 TCP 下进行。

  <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129165011533.webp" alt="image-20240129165011533" style="zoom:50%;" />

### Email

> SMTP 管‘发’，POP3/IMAP 管‘收’。
>
> POP3 是比较老的[protocol](https://www.zhihu.com/search?q=protocol&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A29039357})，主要为了解决本地机器和远程邮件服务器链接的问题，每次邮件会 download 到本地机器，然后从[远程邮件服务器](https://www.zhihu.com/search?q=远程邮件服务器&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A29039357})上删掉（当然特殊 config 除外），然后进行本地编辑。这样的问题是如果从多个终端链接服务器，只有第一个下载的能看到，现在[pop4](https://www.zhihu.com/search?q=pop4&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A29039357})正在讨论中
>
> IMAP 是比较新的（好吧，好像也是 80 年代的产物）protocol，可以将邮件分文件夹整理，然后这些信息也存在远程的邮件服务器上，读取邮件后，服务器上不删除。原理上 IMAP 应该是相当于 online 编辑，但现在的 mail client 基本都有在本地存 copy 的功能

#### **SMTP** | 发送邮件协议

用户代理 ——> 消息队列 ——>放到指定用户 mailbox 目录

使用 TCPport:25

传输三阶段：握手、传报文（ASCII 码）、关闭

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318153214952.webp)

特点

- 使用持久连接
- 要求报文均为 ASCII 编码
- SMTP 服务器使用`CRLF.CRLF`决定报文尾部
- 可以有多个附件

1. **发送与接收分离**：SMTP 专注于发送邮件，而 POP 和 IMAP 专注于邮件的接收和管理。这种分离使得邮件系统的设计更加灵活和高效。
2. **使用端口**：SMTP 通常使用 TCP 端口 25 进行通信，但为了安全起见，还可能使用端口 465（SMTPS）或 587（提交邮件用的 SMTP）。
3. **交互模式**：SMTP 使用命令/响应模式，其中客户端发送命令，服务器响应状态码和文本消息。这种模式支持灵活的交互和错误处理。

报文

- 首部：`To`,`From`,`Subject`
- 主体

**常见 SMTP 命令：**

- `HELO`/`EHLO`：标识客户端开始通信。
- `MAIL FROM`：指定发件人。
- `RCPT TO`：指定收件人。
- `DATA`：后跟邮件内容。
- `QUIT`：结束会话。

**响应格式：**

- 状态码：3 位数字，指示响应类型（如 2xx 为成功，5xx 为失败）。
- 文本消息：对状态码的文本描述，为人类可读。

!!! bug "具体报文字段的含义"

??? note "SMTP 实例"
    1. 客户端连接到 SMTP 服务器并发送`EHLO`命令。<br>
    2. 服务器响应 200 系列代码，表示准备就绪。<br>
    3. 客户端发送`MAIL FROM:<sender@example.com>`命令，指定发件人。<br>
    4. 服务器响应 250，表示命令成功。<br>
    5. 客户端发送`RCPT TO:<recipient@example.com>`命令，指定收件人。<br>
    6. 服务器再次响应 250。<br>
    7. 客户端发送`DATA`命令，进入邮件内容输入模式。<br>
    8. 客户端发送邮件正文，以单独一行`.`结束。<br>
    9. 服务器响应 250，表示邮件接受成功。<br>
    10. 客户端发送`QUIT`命令，结束会话。<br>

多媒体扩展 MIME(mitimedia mail extension)：base64 编码

#### 接收邮件协议

与邮箱服务器建立连接——>查询——>下载

##### POP3 `Post Office Protocol`

邮局访问协议

区分收件发件

下载并删除、下载并保留

无状态

##### IMAP `Internet Mail Access`

Protocol`

Internet 邮件访问协议

提供**远程目录维护**

有状态的

##### HTTP

可以用于文件上下载、收发邮件

### DNS | `Domain Name System`

- 运行在 UDP:53 应用服务

???+note "互联网的复杂性"
 互联网的核心内容建立在互联网边缘的端系统应用之上

#### 作用

- 提供域名到 IP 地址的转换
- 主机名到别名的转换 `host aliasing`
- 邮件服务器别名 `Mail server aliasing`
- 负载均衡`Load Distribution`:

> The DNS database contains this set of IP addresses. When clients make a DNS query for a name mapped to a set of addresses, the server responds with the entire set of IP addresses, but rotates the ordering of the addresses within each reply. Because a client typically sends its HTTP request message to the IP address that is listed first in the set, DNS rotation distributes the traffic among the replicated servers.

#### 分层 NS 实现的分布式数据库

分布式数据库、树状关系

??? note "域名和主机名"

- **域名**（domain name）是互联网上作为网站地址的一部分的一个易于记忆的名称，它映射到一个 IP 地址。域名系统（DNS）负责将域名转换为实际的 IP 地址，使得用户不需要记住复杂的数字序列就能访问网站。例如，`example.com`是一个域名。
- **主机名**（host name）是网络中某个设备的名称，用于标识网络中的计算机。它是一个标识符，用于在特定的网络环境中区分不同的设备。在很多情况下，主机名是解析为 IP 地址的一部分，它可以是域名的一部分或者单独存在于一个局部网络中。

1. 每一个域名（只讨论英文域名）都是一个标号序列（labels），用字母（A-Z，a-z，大小写等价）、数字（0-9）和连接符（-）组成；
2. 标号序列总长度不能超过 255 个字符，它由点号分割成一个个的标号（label）

baidu: 二级域名，指公司名；
www: 表示该公司的 WEB 服务器对应的主机

> IP 不是给人用的，是给其他应用提供的

![image](https://data.educoder.net/api/attachments/579702)

1. 根域名服务器`(Root DNS servers)`：最高层次的域名服务器，本地域名服务器解析不了的域名就会向其求助；、
2. 顶级域名服务器`(TLD Top-level domain servers)`：负责管理在该顶级域名服务器下注册的二级域名；（如`com`、`org`、`net`、`edu`；`uk`，`fr`，`ca`，`jp`）
3. 权限域名服务器`(Authoritative DNS servers)`：负责一个区的域名解析工作；
4. 本地域名服务器`local DNS servers`：当一个主机发出 DNS 查询请求时，这个查询请求首先发给本地域名服务器。

#### 主机能查询分布式数据库的协议

- 应用调用解析器 (resolver)；解析器作为客户向 Name Server 发出查询报文（封装在 UDP 段中）；Name Server 返回响应报文 (name/ip)

先向 Local Name Server(预先配置好的) 进行查询

- 目标名字在 Local Name Server 中：查询的名字在该区域内部或是缓存 (cashing)

- 当与本地名字服务器不能解析名字时，查询根服务器 - TLD - 权威服务器

<img src="https://data.educoder.net/api/attachments/579916" alt="预览大图" style="zoom:50%;" />

The query from the requesting host to the local DNS server is recursive, and the remaining queries are iterative.

##### 递归查询`recursive`

根服务器负担太重

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318153941376.webp" alt="image-20240318153941376" style="zoom:50%;" />

##### 迭代查询 `iterative`

根（及各级域名）服务器返回的不是查询结果，而是下一个 NS 的地址

最后由权威名字服务器给出解析结果

> “我不知道这个名字，但可以向这个服务器请求”

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318153924403.webp" alt="image-20240318153924403" style="zoom:50%;" />

#### DNS 记录与报文

##### 资源记录`resource records`

四元组：(domain_name,value,type,TTL)<br>

- `Domain_name`: 域名<br>
- `Value` 值：可以是数字，域名或 ASCII 串<br>
- `Type` 类别：资源记录的类型—见下页<br>
- `Ttl: time to live` : 生存时间 (权威，缓冲记录) 默认 2 天<br>

缓存为了性能，删除缓存为了和源端保持一致性<br>

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240129232745663.webp" alt="image-20240129232745663" style="zoom:80%;" />

报文

<img src="https://data.educoder.net/api/attachments/554296" alt="预览大图" style="zoom: 67%;" />

报文首部

- 标识符（ID）：16 位（订单编号）

- flags

  - 查询/应答

  - 希望递归

  - 递归可用

  - 应答为权威

#### 命令

[DNS 报文及抓包分析-CSDN 博客](https://blog.csdn.net/master_cui/article/details/112868443)

网卡绑定的 DNS

```shell
cat /etc/resolv.conf # 查看

vim /etc/resolv.conf # 修改

service networking restart
```

##### `nslookup`

nslookup 是一种网络管理命令行工具，可用于查询 DNS 域名和 IP 地址

```shell
nslookup domain # 直接查询
nslookup domain dns-server # 指定域名服务器查询
nslookup -type=type domain # 指定类型查询
```

- MX：邮件服务器记录；
- NS：名字服务器记录；
- PTR：反向记录。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__c371a6c6e767ead83d9a55d9cb809f13.webp" alt="img" style="zoom:50%;" />

### P2P

> 迅雷

每一个节点又可以充当服务器，又可以充当用户，请求节点增加的同时，提供服务的节点也在增加

**缺点**：管理困难的多

#### 时间

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240130004433432.webp)

线性增加

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240130004451304.webp)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240318154406618.webp" alt="image-20240318154406618" style="zoom:50%;" />

#### BitTorrent

`bitmap`,定期泛洪交换

`tracking server` 进行 peer 列表的维护

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240130101612770.webp)

问谁要

位图中全是 0，随机请求其他节点的块；

4 个 bit 后开始稀缺优先（rarest first）；

扰动`churn`: peer 节点可能会上线或者下线，一旦一个 peer 拥有整个文件，它会（自私的）离开或者保留（利他主义）在 torrent 中

给谁发

`tit for tat`原则；可以更有利于网络的维护，激励共享，防止搭便车

- 每 10s 计算：两个周期下载带宽大的排在前面（优先队列）；有限疏通：<br>

  for each of her neighbors, Alice continually measures the rate at which she receives bits and determines **the four peers** that are feeding her bits at the highest rate

- 每 30s 计算：第三个周期在请求中随机选择 (additional)

#### 非结构化 P2P

`overlay` peer 节点之间的覆盖网

- 集中化目录

上线时候向集中化目录进行注册，维护 peer 节点与资源列表

**问题**：单点故障、性能瓶颈、侵犯版权

- 完全分布式 - Gnutella

图式网络

建立`overlay`，泛洪`flooding`查询；BFS+ 记忆化搜索（TTL）

向所有邻居发出 ping，邻居返回 pong

- 混合体 KaZaA

组内集中式，组长分布式

| 文件 | 描述 | Hash |
| ---- | -------- | --------------------- |
| | 匹配描述 | vid，元信息的唯一标识 |

如何定位所需资源
如何处理对等方的加入与离开

#### 结构化 P2P（一致性哈希`consistent hash`）

参考了知乎网友写的[一致性哈希科普](https://zhuanlan.zhihu.com/p/129049724)

把`ip`地址 hash 值作为唯一标识

按照 hash 大小组成一个环；有序拓扑

每个用户维护和上一个 id 之间的文件

查询效率高，副本数量少

#### 混合式

Napster

P2P 分发 mp3 音乐

即时通信，服务器相当于做一个指挥

### `CDN:content distribution network`

如何保证超高数量并发服务，内容访问加速，`over the top` 在边缘系统实现

> China Cash 中国蓝讯

#### 视频与编码

视频：固定速度显示的图像序列

网络视频特点：

- 高码率：>10x 于音频，高的网络带宽需求
- 可以被压缩
- 90% 以上的网络流量是视频

数字化图像：像素的阵列每个像素被若干 bits 表示

编码：使用图像内和图像间的冗余来降低编码的比特数

- 空间冗余 (图像内)
- 时间冗余 (相邻的图像间)

`CBR`: (`constant bitrate`): 以固定速率编码
`VBR`: (`variable bitrate`): 视频编码速率随时间的变化而变化

#### 流化服务`streaming`

边下边看

##### `DASH: Dynamic,Adaptive Streaming over HTTP`

服务器：

- 将视频文件分割成多个块
- 每个块独立存储，编码于不同码率（8-10 种）
- 告示文件（`manifest file`）: 提供不同块的**URL**

客户端：

- 先获取告示文件
- 周期性地测量服务器到客户端的带宽
- 查询告示文件，在一个时刻请求一个块，HTTP 头部指定字节范围
- 根据带宽和缓冲选择编码块

`STB:set top box`机顶盒

#### CDN 部署

ISP 购买 CDN 服务

部署了很多的 cache 节点，云解析重定向后跳数较少

部署策略

- `enter deep`部署在`local ISP`

- `bring home`部署在关键位置，数据中心机房

点网页，CDN 重定向，由缓存节点提供服务

通过 DNS 实现选择最优的节点

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240130123254230.webp)

### `TLS:Transport Layer Security`

传输层安全协议`Transport Layer Security`，旧称安全套接层`SSL:Secure Sockets Layer`

安全套接层

跑在 TCP 之上，在应用层实现

私密性、数据完整性、服务器的认证、报文的完整性

- 不只是 HTTP，任何应用层协议都可以透明地使用 TLS
- 通过加密、认证和完整性保护来保护通信内容

`https`

## Socket API

传输层提供的服务——原语就是`SocketAPI`

socket: 分布式应用进程之间的门，传输层协议提供的端到端服务接口

> A process is analogous to a house and its socket is analogous to its door

- TCP - `Transmission Control Protocol`<br>

  四元组 我 ip+port 对方 ip+port

记忆了一个会话关系，不必要每次都有，建立了一个 socket 的映射

> 经常和朋友寄件，只要知道你经常寄的信息（socket）的代码，顺丰就可以直接寄走

- UDP - `User Datagram Protocol`

  二元组 本地 ip+port

使得穿过层间的信息量最少

UDP 套接字指定了应用所在的端结点（end point）

发送报文必须指定对方的 ip+port

> 不经常寄件，需要提供自己的地址和对方的地址

### TCP socket

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__socket_api.webp)

服务器先运行

--> 建立 socket，返回整数 `welcome socket`

-->和本地端口捆绑

-->等待用户收发

-->返回`connection socket`

-->关闭 socket

> 电脑打开多个 QQ，使用一个 IP 和端口号
>
> 但是每个 QQ 功能可以独立使用、互不影响

#### 具体实现

PF `Protocol Family`协议簇

AF `Address Family`地址簇

inet = internet

如果本地没有指定端口，就调用隐式的

- `socket()`返回的是一个整数

[socket 编程（一）：一个服务器服务一个客户端](https://voidint.github.io/post/socket/one_server_one_client/)

[socket 编程（二）：每个进程服务一个连接](https://voidint.github.io/post/socket/one_process_per_connection/)

[TCP 的 socket 详解_tcpsocket-CSDN 博客](https://blog.csdn.net/weixin_41752434/article/details/116002194)

### UDP socket

建立 socket

bind socket

读取 socket

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__01-ApplicationLayer.assets__image-20240130143354086.webp)
