---
comments: true
---
# 网络安全

!!! note "来源"
    - USTC《计算机网络》
    - 《人工智能与安全》 | 陈艳姣
    - 《信息安全导论》：[智云链接](https://classroom.zju.edu.cn/livingpage?course_id=53572&sub_id=917457&tenant_code=112)

[8.6 各个层次的安全性_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1JV411t7ow?p=53&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

![image](https://img.philfan.cn/CS__CN__assets__06-security.assets__image-20240611204450499.webp)

## 安全

!!! note "What is Security? "
 Confidentiality, Integrity, Availability (CIA triad)

"CIA 三元组"，它由保密性（Confidentiality）、完整性（Integrity）和可用性（Availability）三个要素组成，用于描述一个安全系统所需的基本属性。

保密性是指保护系统和数据不被未授权的访问或泄露；

完整性是指确保数据的准确性和一致性，防止未经授权的修改或破坏；

可用性是指确保系统和数据在需要时可被授权用户访问和使用。

!!! note "What Security Do We Need? "
 Integrity, Confidentiality, Authenticity, Non-repudiation (I-CAN)

"I-CAN"，它由完整性（Integrity）、保密性（Confidentiality）、认证性（Authenticity）和不可否认性（Non-repudiation）四个要素组成，用于描述一个安全系统所需的具体要求。

Integrity | 完整性 : implementation using **message signature**

Confidentiality | 保密性 : implementation using data encryption

Authenticity | 认证性 : implementation using **challenge - response**,登录

> 两个特工：天王盖地虎 - 宝塔镇河妖

Non-repudiation | 不可否认性 : implementation using **message signature**。用私钥加密，公钥解密

## 攻击手段

### 手段

#### 病毒 virus

计算机病毒是一种计算机程序，它在执行时将自己附于其他程序或文件并编写其自己的代码，从而能够从一个程序传播到另一个程序，并在传播过程中感染计算机。

几乎所有的计算机病毒都附于一个可执行文件，**不点击不感染**！

#### 蠕虫 worm

**自我复制！独立运行！**

蠕虫在设计上类似于计算机病毒，但它是病毒或特洛伊木马程序的一个子类别。

然而与病毒不同的是，它能够在不附于主机程序的情况下传播，并且可以独立运行。

蠕虫利用了系统中的文件或信息传输功能，使其能在无帮助的情况下传播。其结果是蠕虫消耗了太多的系统内存（或网络带宽），从而导致 Web 服务器、网络服务器和个人的计算机停止响应。

> 一个例子是蠕虫向您的电子邮件地址簿列出的每个人发送其副本。然后，蠕虫继续自我复制并将自己发送给每个收件人的地址簿列出的每个人，并继续重复此过程。

#### 木马

特洛伊木马程序是指让用户误解其意图的各类恶意软件，例如看似是正版应用程序或软件程序但实际是破坏性程序。

特洛伊木马程序是根据古希腊神话中特洛伊木马的故事所命名的，特洛伊木马具有欺骗性，它摧毁了特洛伊城。与病毒不同，特洛伊木马程序不会自我复制，但它们同样具有破坏性。特洛伊木马还能打开计算机的后门，向恶意分子发出命令，或能让恶意用户/程序访问您的系统。这会导致机密信息和个人信息被盗。

### 攻击

- 加密算法已知，求密钥
- 加密算法和密钥均不知道
- 唯密文攻击
- 已知明文攻击
- 已经知道部分密文和明文的对应关系
- 选择明文攻击
- 攻击者能够选择一段明文，并得到密文

## 防火墙

将组织内部网络和互联网络隔离开来，按照规则进行分组过滤

防火墙在网络层

1.阻止拒绝服务攻击 (DOS deny of service,DDOS distributive)：

SYN flooding: 攻击者建立很多伪造 TCP 链接，对于真正用户而言已经没有资源留下了

阻止非法的修改/对非授权内容的访问

2.只允许认证的用户能否访问内部网络资源 (经过认证的用户/主机集合)

- 2 种类型的防火墙：
  - 网络级别：分组过滤器
  - 应用级别：应用程序网关

规则

- 源 IP 地址，目标 IP 地址
- TCP/UDP源和目标端口
- ICMP 报文类别
- TCP SYN 和 ACK bits

### 无状态规则

防火墙不维持通讯状态

| 策略 | 设置 |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| 所有的进出 UDP 流以及 telnet 连接的数据报都被阻塞掉 | 只要拥有 IP 协议字段= 17，<br/>而且源/目标端口号= 23. |
| 阻止外部客户端和内部网络的主机建立 TCP 连接<br/>但允许内部网络的客户端和外部服务器建立 TCP 连接 | 阻塞进入内网的 TCP 段：它的 ACK=0. |
| 不允许外部的 web 进行访问 | 阻塞掉所有外出具有目标端口 80 的 IP 分组 |
| 不允许来自外面的 TCP 连接，除非是机构公共 WEB 服务器的连接 | 阻塞掉所有进来的 TCP SYN 分组，除非 130.207.244.203, port 80 |
| 阻止 Web 无线电占用可用带宽。 | 阻塞所有进来的 UDP 分组 除非 DNS 和路由器广播 |
| 阻止你的网络被`smurf DoS`所利用 | 阻塞掉所有具有广播地址的 ICMP 分组 (eg130.207.255.255). |
| 阻止内部网络被`tracerout`，从而得到你的网络拓扑 | 阻塞掉所有外出的 ICMP TTL 过期的流量 |

### 有状态规则

无状态分组过滤根据每个分组独立地检查和行动
有状态的分组过滤联合分组状态表检查和行动

知道连接后，才不被 block 掉；防火墙知道是否已经进行连接

防火墙变成了状态维护的设备

### ACL `access control list`

最后一条规则，默认规则匹配所有

根据应用数据的内容来过滤进出的数据报，就像根据 IP/TCP/UDP 字段来过滤一样

- 检查的级别：应用层数据

对应用进行深度剖析

<img src="https://img.philfan.cn/CS__CN__assets__06-security.assets__image-20240217110805828.webp" alt="image-20240217110805828" style="zoom:50%;" />

`IP spoofing`: 路由器不知道数据报是否真的来自于声称的源地址

更改 IP 的头部字段

对 UDP 要么全过，要么全不过

折中：与外部通信的自由度，安全的级别

## 入侵检测系统 IDS intrusion detection system

multiple IDSs: 在不同的地点进行不同类型的检查

<img src="https://img.philfan.cn/CS__CN__assets__06-security.assets__image-20240217111255212.webp" alt="image-20240217111255212" style="zoom:50%;" />

在所有流量上放置 sensor

- 深入分组检查：检查分组的内容 (e.g., 检查分组中的特征串已知攻击数据库的病毒和攻击串

- 检查分组间的相关性，判断是否是有害的分组

  • 端口扫描
  • 网络映射
  • DoS 攻击

映射：

- 在攻击之前： “踩点” – 发现在网络上实现了哪些服务
- 使用 ping 来判断哪些主机在网络上有地址
- 端口扫描：试图顺序地在每一个端口上建立 TCP 连接 (看看发生了什么)

分组嗅探：对策

- 机构中的所有主机都运行能够监测软件，周期性地检查是否有网卡运行于**混杂模式**
- 每一个主机一个独立的网段 (交换式以太网而不是使用集线器)

IP Spoofing 欺骗：

- 可以有应用进程直接产生“raw”IP 分组，而且可以在 IP 源地址部分直接放置任何地址
- 接收端无法判断源地址是不是具有欺骗性的
- e.g. C 伪装成 B

设置入口过滤，出去的分组源 IP 应该和这个网段一致

Denial of service (DOS): 对策

- 在到达主机之前过滤掉这些泛洪的分组 (e.g., SYN): throw out good with bad
- 回溯到源主机 (most likely an innocent,compromised machine)

## 虚拟专用网络技术

## 访问控制技术

## 网络安全技术

## 安全场景

### HTTP 认证

#### 基本认证

当一个客户端向 HTTP 服务器进行数据请求时，如果客户端未被认证，则 HTTP 服务器将通过基本认证过程对客户端的用户名及密码进行验证，以决定用户是否合法。

客户端在接收到 HTTP 服务器的身份认证要求后，会提示用户输入用户名及密码，然后将用户名及密码以`BASE64`加密，加密后的密文将附加于请求信息中。

> 如当用户名为`anjuta`，密码为：`123456`时，客户端将用户名和密码用“：”合并，并将合并后的字符串用`BASE64`加密为密文，并于每次请求数据时，将密文附加于请求头（Request Header）中

HTTP 服务器在每次收到请求包后，根据协议取得客户端附加的用户信息（`BASE64`加密的用户名和密码），解开请求包，对用户名及密码进行验证

BASIC 认证的步骤：

1. 客户端访问一个受 HTTP 基本认证保护的资源；

2. 服务器返回 `401` 状态，要求客户端提供用户名和密码进行认证。（验证失败的时候，响应头会加上`WWW-Authenticate: Basic realm="请求域"`），如下所示：

   ```text
   401 Unauthorized
   WWW-Authenticate: Basic realm="WallyWorld"
   ```

3. 客户端将输入的用户名密码用`Base64`进行编码后，采用非加密的明文方式传送给服务器；

   ```text
   Authorization: Basic xxxxxxxxxx.
   ```

4. 服务器将 `Authorization` 头中的用户名密码解码并取出，进行验证，如果认证成功，则返回相应的资源；如果认证失败，则仍返回 `401` 状态，要求重新进行认证。

#### 摘要认证 digest authentication

该认证是 HTTP1.1 提出的基本认证的替代方法，不包含密码的明文传递。摘要认证使用`随机数 + MD5 加密哈希函数`来对用户名、密码进行加密，在上述第二步时，服务器返回随机字符串 `nonnce` 之后，客户端发送摘要`MD5（HA1:nonce:HA2）`。其中`HA1=MD5(username:realm:password),HA2=MD5(method:digestURI)`。

#### 开放认证 OAuth Authentication

开放认证允许用户提供一个令牌，而不是用户名和密码来访问它们存放在特定服务器的数据，每一个令牌授权一个特定的第三方系统。

#### 令牌认证 Token Authentication

令牌认证是指当用户第一次登陆时，服务器生成一个 token 并返回给客户端，之后的每次访问客户端都会带上该 token，无需再次带上用户名和密码。

#### 基本认证中的认证相关字段

（1）服务器响应状态码与状态描述：当服务器响应状态码为 401 时，表明服务器资源需要认证。其状态描述为`Unauthorized`，表明未通过认证，当响应`200 OK`时，表明通过认证，正常响应；

（2）当用户提供用户名和密码后，重新提出请求时：  ` Authorization: Basic xxxxxxxxxx. ` `Authorization` 字段表明在请求中，提供了需要的认证方式和认证信息（已经经过加密）。

### 安全电子邮件

私密性：对称式 + 非对称式

可认证性和报文完整性：传报文和数字签名（用对称式密钥加密），密钥用对方公钥加密；

​ 如果接收方 bob 算出的报文摘要和传过来的报文摘要是相同的

PGP 电子邮件加密方案

应用层

![image](https://img.philfan.cn/CS__CN__assets__06-security.assets__image-20240217101521016.webp)

<img src="https://img.philfan.cn/CS__CN__assets__06-security.assets__image-20240217101539896.webp" alt="image-20240217101539896" style="zoom: 67%;" />

### SSL (secure sockets layer)

为使用 SSL 服务的、基于 TCP 的应用提供传输层次的安全性

步骤

- 握手
- 密钥导出
- 数据传输

传输层

### IPsec

网络层

双方要建立通信关系

Authentication Header (AH) 协议

提供源端的可认证性，数据完整性，但是不提供机密性

ESP 协议

提供机密性，主机的可认证性，数据的完整性

### 802.11 security

链路层的安全
