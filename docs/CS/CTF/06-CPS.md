# 信息物理系统安全

??? note "课程信息"
 === "上课体验"
  因为当时对密码学相关的问题比较感兴趣，所以对这部分内容还仔细听了一下；<br>
  
  小测题目也是可以看一下往年老师讲解题目的 ppt；<br>
  有不定期点名<br>
  课程论文我个人就写的大作业当中负责的部分
  
 === "考核方式"
  平时 20% + 小组 ppt 展示 40% + 期末个人论文 40%<br>

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240422090745001.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__20250109205113.webp)

```text
├─图解密码技术.pdf
├─PPT
│      第 0 次课.pdf
│      第 11+12 次课.pdf
│      第 15 次课.pdf
│      第 1 次课.pdf
│      第 2 次课.pdf
│      第 3+4 次课【小测用】.pdf
│      第 5+6 次课.pdf
│      第 7+8 次课.pdf
│      第 9+10 次课.pdf
│
└─大作业
    │  2.1-替换密码破译.py
    │  2.3.1-RSA 攻击.py
    │  2.3.2-RSA 攻击.py
    │  2.3.3-RSA 攻击.py
    │  crypto_challenge1.png
    │  ppt.pdf
    │  《信息物理系统安全》PPT 展示题目.pdf
    │
    └─附加题
            CPSS
            readme.txt
```

## 课程资料

通过网盘分享的文件：信息物理系统安全
链接：<https://pan.baidu.com/s/1rj3vlQu8t7BNE6DiHCnZ2Q?pwd=PHIL> 提取码：PHIL

### 小测题目

去年考完老师讲了小测，可以去智云看

!!! note "貌似有一道是这个"

 |               Transaction                | Fill In This Column |       Choose From The Following        |
 | :--------------------------------------: | :-----------------: | :------------------------------------: |
 |   Alice wants to sign an email to Bob    |          b          |         a. Alice's public key          |
 |  Alice wants to encrypt an email to Bob  |          c          |         b. Alice's private key         |
 |    Bob wants to verify Alice's email     |          a          |          c. Bob's public key           |
 |    Bob wants to decrypt Alice's email    |          d          |          d. Bob's private key          |
 |  Alice public key certificate signed by  |          f          | e. Certification Authority public key  |
 | Bob public key certificate verifies with |          e          | f. Certification Authority private key |

 答案和解析：

- Alice 想要给 Bob 签名一封电子邮件：因为 Alice 使用她的私钥生成数字签名，而 Bob 需要使用 Alice 的公钥来验证这个签名。
- Alice 想要加密一封发送给 Bob 的电子邮件：应该是使用 Bob 的公钥来加密
- Bob 想要验证 Alice 的电子邮件：因为 Bob 使用 Alice 的公钥验证了数字签名，所以他知道这封电子邮件确实来自 Alice。
- Bob 想要解密 Alice 的电子邮件：d（Bob 的私钥）
- Alice 的公钥证书由以下机构签名：因为公钥证书是由认证机构使用其私钥签名的，所以其他人可以使用认证机构的公钥来验证这个签名。
- Bob 的公钥证书验证如下：使用认证机构的公钥来验证 Bob 的公钥证书

### 大作业题目

每年题目好像变化不大，我将我们小组的 ppt 上传了，可以参考，后果自负 ac01

ppt 展示智云录像

[2023](https://classroom.zju.edu.cn/livingroom?course_id=51532&sub_id=883382&tenant_code=112)<br>
[2022](https://classroom.zju.edu.cn/livingroom?course_id=39400&sub_id=601927&tenant_code=112)<br>
[2021](https://classroom.zju.edu.cn/livingroom?course_id=21309&sub_id=201082&tenant_code=112)<br>

从以下题目中任选一题准备每组 10 分钟以内 PPT 展示

### 事件综述类

（从真实的信息物理系统安全事件分析，可以分析行业背景、信息物理系统结构与特点、攻击原理、造成影响、防御措施等，也可选择其他信息物理系统安全事件；在展示中融入自己的思考）

1. 从特斯拉 Model X 中继攻击看自动驾驶汽车信息物理系统安全<br>
2. 从 SolarWinds 供应链攻击看信息物理系统安全<br>
3. 从台积电事件看制造业信息物理系统安全<br>
4. 从 colonial pipeline 公司被勒索事件分析信息物理系统安全<br>
5. Vault7 等数据泄露事件与信息物理系统安全<br>
6. 从乌克兰停电事件看电网信息物理系统安全<br>
7.* CVE-2024-3094 Informational: Impact of Malicious Code in XZ Tools and Libraries 研究该事件的供应链攻击原理<br>

### 创新实践类（动手实践，赋分高）

1.Modbus 协议是信息物理系统较为常用的一款网络协议。试分析 Modbus 协议的应用层格式和存在的安全性问题（例如机密性、完整性、实时性等），编写 Python 脚本实现支持 Modbus/TCP 通信的 Client 和 Server（可参考 github 上的开源项目）。

2.了解模糊测试 Fuzzing 以及目前针对 IoT 设备的主流模糊测试方法，了解、介绍、测试开源工具 AFL Fuzz

AFL:<https://github.com/google/AFL>

3.调研私有协议逆向的主流方法，选取现有的工具，如 Netzob 等进行介绍并针对工业控制系统典型协议进行分析。

4.下图展示了某一工业控制信息物理系统网络结构，目前各层内和各层之间没有对信道传输的数据进行保护，尝试调研、设计各层内和各层之间的数据加密/解密算法，并使用 python 进行实现（提示：考虑控制层的实时性问题，其层内和与其他层的通信可采取完整性校验算法；python 的加密算法库可以直接调用）

5.分析 Nmap、p0f、xprobe2、PLCscan（也可以是其他专用工具）等扫描工具对信息物理系统的识别方式，尝试扫描公网上的一些设备，给出设备信息。

（工具可自行选择两种及以上；设备 IP 可利用 Shodan 搜索引擎，请自行检索 Shodan 使用方法；扫描工具建议在 VMware 虚拟机中安装 Kali linux 系统，该系统有上百种已安装好的网络安全分析工具，包括题目中涉及到的扫描工具）

- Shodan：<https://www.shodan.io/>
- Nmap：<https://github.com/nmap/nmap>
- p0f: <https://github.com/p0f/p0f>
- PLCscan: <https://github.com/yanlinlin82/plcscan>

6.选择一款针对信息物理系统进行攻击的开源项目，分析程序的攻击流程、攻击效果（例如 Stuxnet，TRITON 等，可在 github 上寻找其他项目）

STUXNET：参考文献《W32. stuxnet dossier》

TRITON:<https://github.com/MDudek-ICS/TRISIS-TRITON-HATMAN>

7.分析 conpot、snap7 等蜜罐对工业控制器的模拟方式，尝试在云服务器上部署此类常见蜜罐，进行一定时间（一周以上）的捕获，分析捕获结果。（蜜罐可自行选择两种及以上，分析蜜罐主要交互功能的实现方法，并对捕获结果进行分类）

- Conpot：<https://github.com/mushorg/conpot>
- Snap7：<https://github.com/gijzelaerr/python-snap7>

8.分析 ISF、msf 等工具以及 ClearEnergy、Flame、Trisis 等攻击事件的攻击脚本，分析其攻击路径及架构，实施攻击前是否考虑 PLC 运行状态、连接状态、密码保护等情况，有能力的话可以尝试对攻击脚本添加设备状态扫描功能。需要一定的 python 或 C 代码的基础

攻击事件脚本：

- ClearEnergy:<https://github.com/0xICF/ClearEnergy>
Flame:<https://github.com/loneicewolf/flame-sourcecode>
- TRISIS：<https://github.com/MDudek-ICS/TRISIS-TRITON-HATMAN>

攻击工具（分析攻击施耐德、西门子 PLC 的 payload 即可）：

- ISF： <https://github.com/dark-lbp/isf>
- metasploit-framework：<https://github.com/rapid7/metasploit-framework> 附加类（CTF）

### 附加类（CTF）

从给出的附件中得到 flag，需要用到的知识：逆向、反汇编、程序语言，可能用到的工具 (可能包含但不限于)：DIE、IDA。

!!! note "附加题其实用 IDA 打开一下就行了，挺简单的"

## 绪论

CPS 具有四大核心技术要素，即“一硬”（感知和自动控制）、“一软”（工业软件）、“一网”（工业网络）、“一平台”（工业云和智能服务平台）。

工控系统

> 工控系统，即工业控制系统，是对工业生产过程进行监测和控制的系统。它广泛应用于制造业、石油和天然气等各个领域，用于控制和监测各种设备、生产线和机器人等。
>
> 工控系统的核心组件包括数据采集与监控系统（SCADA）、分布式控制系统（DCS）、可编程控制器（PLC）、远程终端（RTU）、人机交互界面设备（HMI）以及确保各组件通信的接口技术。

典型入侵事件

> 震网病毒（Stuxnet）是世界上第一个专门定向攻击真实世界中基础设施的计算机蠕虫病毒。它于 2010 年 6 月首次被检测出来，具有极强的隐身和破坏力。该病毒利用了多个零日漏洞，可以自动感染和传播，主要通过改变离心机的转速来破坏工业设备，如伊朗的核设施中的离心机。震网病毒的发现标志着网络武器由构造简单的低端武器向结构复杂的高端进攻性武器的过渡，也打破了与外界封闭的工业系统可以免受网络袭击破坏的神话。

零日漏洞

> 零日漏洞（Zero-Day Vulnerability）是指被发现后立即被恶意利用的安全漏洞。这种漏洞在被发现的当天，相关的恶意程序或攻击手段就会出现，因此得名为“零日”。零日漏洞之所以危险，是因为它们通常没有已知的解决方案或补丁，使得攻击者可以利用这些漏洞进行未经授权的访问、数据窃取、系统破坏等恶意行为。

信息物理系统（Cyber Physical System，简称 CPS）

> 信息物理系统是一个综合了计算、网络和物理环境的多维复杂系统。它通过人机交互接口实现和物理进程的交互，使用网络化空间以远程的、可靠的、实时的、安全的、协作的方式操控一个物理实体。CPS 的核心特征是将计算、通信和控制三个维度融合在一起，形成一个统一的系统。
>
> CPS 的发展历史可以分为三个阶段：第一阶段是传统的嵌入式系统，主要是将计算机嵌入到物理设备中，实现对设备的控制和管理；第二阶段是物联网（IoT），利用无线通信技术将物理设备连接起来，实现对设备的远程监测和控制；第三阶段是 CPS，利用云计算、大数据、人工智能等技术将物理设备与网络服务集成起来，实现对设备的智能化和优化。
>
> CPS 的应用领域非常广泛，包括智能交通、智能电网、智能制造、智能医疗、智能家居等。例如，在智能交通领域，CPS 可以实现车辆与道路基础设施、交通信号灯等的实时通信和协同控制，提高交通效率和安全性；在智能制造领域，CPS 可以实现生产设备与信息系统的深度融合，实现生产过程的智能化和柔性化。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__v2-446d4c8b5ca56c4e7e2a4deb167ab3c6_r.webp" alt="img" style="zoom:50%;" />

大多数协议没有开放的协议规范或缺乏完整的协议描述尤其是专有协议，如工业控制协议和物联网协议

工业控制系统中处于对安全、隐私等考虑，制造商一般不会透露此类协议的细节，这给入侵检测、模糊测试漏洞分析和指纹识别等安全研究带来了挑战

> 协议的要素
>
> 报文格式语法、语义、次序、采取的动作

### 典型工控协议

#### Modbus TCP 协议

[Modbus](https://so.csdn.net/so/search?q=Modbus&spm=1001.2101.3001.7020)由 MODICON 公司于 1979 年开发，是一种工业现场总线协议标准。1996 年施耐德公司推出基于以太网 TCP/IP 的 Modbus 协议。属于应用层的协议

Modbus 通信的设备分为主站 (mater) 和从站 (slave)，主站为主动方，从站为被动方。

报文结构

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__20210123223219854.webp" alt="在这里插入图片描述" style="zoom:50%;" />

MBAP 报文头为 7 个字节长

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240508144701385.webp" alt="image-20240508144701385" style="zoom:50%;" />

PDU：1 字节功能码+N 字节数据

**通信的过程为**：

1. 主站设备主动向从站设备发送请求：功能码 + 数据
2. 从站设备处理主站的请求后，向主站返回结果。
3. 如果从站设备处理请求出现异常，则向主站设备返回异常功能码。

#### DNP3 协议

基于主从的协议，允许从站上传信息，采用多轮问询——应答的方式。

DNP3 协议在应用层实现了对传输数据的分片、校验、控制等功能，并提供了数据的分片重组、数据校验、链路控制、优先级等一系列服务。协议中大量使用了 CRC 校验来保证数据的准确性。DNP3 协议基于 TCP/IP，使用 20000 端口进行通信。

DNP3 协议的特点包括：

- 可靠性高，适用于工业环境。
- 具有错误检测能力，保证数据的准确性。
- 支持多种数据对象，包括二进制输入、二进制输出、计数器输入、模拟输入、模拟输出等。
- 支持串行点对点、点对多点连接，以及层次到汇聚的点到多点的拓扑结构。

### 逆向方法和原理

协议逆向工程是指在不依赖协议描述的情况下，通过对协议实体的网络输入输出、系统行为和指令执行流程进行监控和分析，提取**协议语法、语义和同步信息**的过程是工程化的协议逆向分析方法。

#### 基于程序执行的方法

基于程序执行的方法，也被称为动态分析方法，通过实际运行目标程序，并监控其行为和状态来分析程序的内部结构和功能。这种方法通常使用调试器、模拟器或虚拟机等工具来执行程序，并记录程序执行过程中的指令、数据流、函数调用等信息。

> **例子：** 假设我们想要分析一个加密程序，以了解其加密算法。我们可以使用调试器附加到该程序上，并逐步执行程序的指令。通过观察程序执行过程中的数据流和函数调用，我们可以推断出程序使用的加密算法，并可能找到解密的方法。

#### 基于报文的方法

> 语法、语义、顺序、动作

基于报文的方法，也被称为静态分析方法，通过分析程序的二进制代码、汇编代码或源代码等静态表示来理解程序的结构和功能。这种方法通常使用反汇编器、反编译器或源代码分析工具等来解析程序的代码，并提取出程序的函数、变量、数据结构等信息。

> **例子：** 假设我们想要分析一个网络通信程序，以了解其通信协议。我们可以使用反汇编器将程序的二进制代码转换为汇编代码，并分析程序的网络通信函数。通过观察函数的参数和返回值，我们可以推断出程序使用的通信协议，并可能找到破解或伪造通信数据的方法。

#### 基于差分的方法

差分是一种比较基本且有效的协议逆向分析方法

方法依赖于**大量的网络数据包**，并比较这些数据包中不同的部分。

通过识别**数据包之间的差异**，可以推断出协议的结构和工作方式。

> 例如，如果工程师站发送两个请求数据包，一个启动设备，一个停止设备并且在网络流量中，这两个请求的数据只有一位 (比如第 N 个字节) 是不同的，那么就可以推断这个位可能是控制设备开关的命令字段

## 威胁建模

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240529154044354.webp)

## 威胁模式分析

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240529142555579.webp)

### 攻击可达性

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240529142633068.webp)

结合漏洞传播的 USB 摆渡攻击模式

第三方供应商攻击是指由于第三方供应商安全意识淡漠、产品安全性参差不齐，致使攻击者可通过对第三方产品进行漏洞挖掘找到突破点，进而对主目标系统实施恶意攻击的方式。这种方式和传统的产业链中，产品通过销售网络送到消费者手中的模式相

基于推送更新的水坑攻击模式是指攻击者首先通过猜测（或观察）来确定目标网络中使用的服务，并入侵其中一个或多个服务，在服务的推送更新中植入恶意代码，达到感染目标中部分成员的目的。与第三方供应链污染相比，此类攻击的目标更加明确且流程更短，由于此种攻击借助正规服务的更新推送，对目标的攻击成功率很高，且隐蔽性很强。

### 横向移动性

横向移动由攻击者用来进入和控制网络中远程系统的技术组成，通常包括利用默认凭证、利用漏洞、利用远程文件共享服务、利用 POU（程序组织单元）、利用合法凭证等，还可能利用 IT 和 OT 网络上的双宿主设备和系统。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240529142833008.webp)

**利用 POU 在控制器之间扩散**：

程序组织单元（Programming Organization Unit, POU）是 PLC 编程中用于创建程序和项目的块结构。PLC 可以执行用户编写的 POU，这些 POU 包含控制可编程逻辑控制器的指令，从而控制工业过程。除此之外，不同型号的 PLC 还具有扩展的 POU 功能，例如可以使用扩展指令和其他设备之间建立连接。但是，这种扩展功能也存在一定的弊端，如果该 PLC 被攻击者攻陷、植入病毒的话，利用此连接就可以把病毒传播给其他设备，从而在控制器之间扩散。

利用工控协议从上位机向控制器扩散

协议认证是指根据协议规范来检查协议实体间的交互是否满足一定特性或条件的过程，例如，检查是否有死锁存在。通过协议认证，可以获知协议设计是否满足正确性、完整性和一致性等要求。在工控系统中，Modbus 协议无疑是主流的工控协议之一，但是该协议具有致命的缺陷——**缺乏认证和完整性机制**。攻击者可以利用此缺陷，构造蠕虫病毒在不同设备之间传播。

暴力突破 PLC 密码认证机制

防御方法

①确保对控制逻辑的保护，防止未经授权的访问和对控制逻辑的修改，同时增强工业控制系统与其他网络的隔离，加强纵深防御安全

②对控制逻辑进行验证，在将每次编写好的程序下载进 PLC 执行之前先验证控制逻辑，防止程序的控制流劫持

③对未经授权的工业控制系统网络中控制逻辑包传输进行检测和阻止

### 持续隐蔽性

持续隐蔽性相关技术包括劫持重要的 DLL 文件、伪装成正常的应用程序或关键设备、篡改控制器控制逻辑程序、篡改控制器固件、开发针对控制器的 Rootkit、控制主设备与从设备进行通信、抑制响应功能避免安全报警和清除攻击痕迹以防止技术人员攻击溯源等技术。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__06-CPS.assets__image-20240529143058534.webp)

DLL 劫持工程师站中的组态软件

伪装成虚拟 PLC 隐藏恶意攻击

利用 PLC 逻辑炸弹持续窃取敏感信息

梯形逻辑炸弹是指用梯形图编写的恶意软件。攻击者可以将恶意软件注入 PLC 的现有控制逻辑中，改变控制动作或者等待特定的触发信号来激活恶意行为。

利用引脚控制攻击开发高隐蔽的 Rootkit

### 破坏杀伤性

通过干扰工厂过程控制造成生产损失

利用 PLC 安全机制漏洞进行勒索

通过欺骗 SCADA 控制现场设备

利用虚假数据注入影响控制决策

攻击安全仪表系统突破安全约束

## 设备安全分析

## 控制安全分析

## 安全防御技术
