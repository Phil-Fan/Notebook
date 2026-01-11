---
date:
  created: 2025-10-07
  updated: 2025-10-07
readtime: 8
pin: true
categories:
  - Settings
tags:
  - Router
authors:
  - Phil-Fan
nostatistics: true
---

# Linux L2TP VPN 配置与网络调试

在玉泉教学楼中用 Linux 配置 L2TP VPN，记录一下相关的配置过程。

!!! note "环境"
    一、教学办公区：紫金港校区均可通过自动获取IP上网。其他校区教学办公区，需设置静态IP地址访问网络。可咨询身边同学同事，或致电信息技术中心24小时服务热线0571-87951669获得帮助。

    二、学生宿舍区
    紫金港和玉泉校区学生宿舍可自动获取IP，使用VPN账号登录认证后才可访问校内和校外网络。其他校区学生宿舍需绑定IP，请关注并登陆“浙大学生公寓管理服务中心”，具体操作如下图所示。如有疑问可致电信息技术中心24小时服务热线0571-87951669咨询。

    来源：[有线网络服务说明](https://itc.zju.edu.cn/_t2014/2020/0414/c49796a2059097/page.htm)

## 一、环境说明

以校园或企业内网 VPN 为例，假设网络参数如下：

| 项目                  | 示例值                 | 变量名           |
| ------------------- | ------------------- | ------------- |
| 本机 IP               | 10.15.xxx.xx        | `$LOCAL_IP`   |
| 子网掩码                | 255.255.255.0       | `$LOCAL_MASK` |
| 本地网关                | 10.15.xxx.xx         | `$LOCAL_GW`   |
| DNS 服务器             | 10.10.0.21          | `$DNS_SERVER` |
| VPN 服务器             | 10.5.1.7 或 10.5.1.9 | `$VPN_SERV`   |
| 拨号后 VPN 网关（ppp0 IP） | 210.32.xxx.xx       | `$VPN_GW`     |
| 有线网卡设备              | eth0（视系统可能为 eno1、eno2 等）   | `$ETH_DEV`    |
| VPN 设备接口            | ppp0                | `$PPP_DEV`    |

拨打信息中心电话`0571-87951669`，转 0

- 你所在实验室的 IP 地址`$LOCAL_IP`
- 默认网关`$LOCAL_GW`
- DNS`$DNS_SERVER`

## 二、常用工具安装

1️⃣ 安装网络基础工具包

```bash title="安装网络基础工具包"
sudo apt update
sudo apt install net-tools -y
```

> 提供 `ifconfig`, `route`, `netstat` 等命令。

2️⃣ 安装 DNS 工具

```bash title="安装 DNS 工具"
sudo apt install dnsutils -y
```

> 提供 `nslookup`，用于测试域名解析。

3️⃣ 安装路由追踪工具

```bash title="安装路由追踪工具"
sudo apt install traceroute -y
```

```bash title="安装后验证"
ifconfig
nslookup www.baidu.com
traceroute www.google.com
```

```shell
sudo apt install xl2tpd strongswan ppp -y
```

## 三、L2TP 基础配置

```shell title="配置 IP 地址"
sudo ip addr flush dev eth0
sudo ip addr add 10.15.192.59/24 dev eth0
sudo ip link set eth0 up
sudo ip route add default via 10.15.192.1 dev eth0
```

eth0 是网卡名称，需要根据实际情况修改。

```shell
ping -c 4 10.15.192.1
```

### 1️⃣ 编辑 L2TP 配置文件

```shell
sudo vi /etc/xl2tpd/xl2tpd.conf
```

```ini
[lac ZJU_VPN]
lns = 10.5.1.7
redial = yes
redial timeout = 15
max redials = 5
require pap = no
require chap = yes
require authentication = yes
name = $student_id@$SERVICE_TYPE
ppp debug = no
pppoptfile = /etc/ppp/options.xl2tpd.zju
```

service_type 浙大有 10 元 30 元 50 元三个档网费，分别对应的使用域是 a,c,d

### 2️⃣ 创建 PPP 选项文件

```shell
sudo vi /etc/ppp/options.xl2tpd.zju
```

```ini title="插入内容"
noauth
proxyarp
defaultroute
```

### 3️⃣ 设置认证信息

```shell
sudo vi /etc/ppp/chap-secrets
```

```ini title="插入内容"
$USER_NAME@$SERVICE_TYPE    *   "$USER_PASSWORD"    *
```

## 四、启动与拨号连接

```bash title="启动与拨号连接，没有出现就多输入几遍"
sudo service xl2tpd start
echo "c ZJU_VPN" | sudo tee /var/run/xl2tpd/l2tp-control
echo "c ZJU_VPN" | sudo tee /var/run/xl2tpd/l2tp-control
echo "c ZJU_VPN" | sudo tee /var/run/xl2tpd/l2tp-control
echo "c ZJU_VPN" | sudo tee /var/run/xl2tpd/l2tp-control
```

拨号成功后，用以下命令查看新建的 PPP 接口：

```bash
ifconfig ppp0
```

## 五、路由配置原则

VPN 连接后需要手动调整路由，以保证：

1. 校园/企业内网（10.x.x.x）流量仍走本地网关。
2. 外网流量通过 VPN。

---

### ✅ 推荐配置命令

```shell
sudo ip route flush dev enP2p1s0
```

```bash title="保证 VPN 服务器仍能通过原网关访问"
sudo route add -host $VPN_SERV gw $LOCAL_GW metric 1 dev $ETH_DEV
```

```bash title="删除旧的默认网关"
sudo route del default gw $LOCAL_GW
```

```bash title="设置新的默认网关（VPN）"
sudo route add default gw $VPN_GW dev $PPP_DEV metric 1
```

```bash title="添加内网转发规则（保留校内访问）"
sudo route add -net 10.0.0.0 netmask 255.0.0.0 gw $LOCAL_GW dev $ETH_DEV
```

> ⚠️ **顺序很重要：**
> 必须先添加内网路由，再删除旧网关，否则 SSH 或远程连接可能中断。

## 六、网络测试与排查

**1 查看路由表**

```bash
ip route show
# 或
route -n
```

确认：

- 默认路由 (`default`) 指向 `$PPP_DEV`
- 10.0.0.0/8 指向 `$LOCAL_GW`

**2 Ping 测试连通性**

```bash
ping -c 4 $LOCAL_GW        # 测试本地网关
ping -c 4 $VPN_GW          # 测试 VPN 网关
ping -c 4 8.8.8.8          # 测试外网 IP
```

**3 检查 DNS 配置**

```bash
cat /etc/resolv.conf
```

应包含：

```shell
nameserver $DNS_SERVER
```

如果解析失败，可临时切换为公共 DNS：

```bash
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
```

测试：

```bash
nslookup www.baidu.com
```

**4 路由追踪**

```bash title="路由追踪"
traceroute 8.8.8.8
```

- 若卡在第一跳 → 本地路由问题
- 若卡在第二跳 → VPN 转发异常
- 若能到外网 → DNS 或防火墙问题

## 七、常见错误与解决方案

| 错误类型                   | 现象           | 解决方案                              |
| ---------------------- | ------------ | --------------------------------- |
| `NS_ERROR_NET_TIMEOUT` | 浏览器访问超时      | 检查能否 ping 外网；若能，修改 DNS。           |
| `Network unreachable`  | ping 任意地址失败  | 路由配置错误；确认 default 指向 `$PPP_DEV`。  |
| `File exists`          | route add 报错 | 表示路由已存在，先删除后重新添加。                 |
| 无法访问内网                 | VPN 正常但校内网断开 | 补充 `10.0.0.0/8` → `$LOCAL_GW` 路由。 |

调试流程：

```text
工具安装 → VPN 拨号 → 路由配置 → ping 测试 → DNS 检查 → traceroute 分析
```

核心原则：

- 内网走 `$LOCAL_GW`
- 外网走 `$VPN_GW`
- DNS 正常解析后，网络才真正连通
