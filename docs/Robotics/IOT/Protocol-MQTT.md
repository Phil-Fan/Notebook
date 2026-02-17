# MQTT

## 简介

MQTT（Message Queuing Telemetry Transport）是一种轻量级的消息传输协议，广泛用于物联网（IoT）设备之间的通信。它基于发布/订阅模型，支持低带宽、高延迟或不稳定网络环境下的通信。

- **发布者（Publisher）**：将消息发送到特定主题（Topic）。
- **订阅者（Subscriber）**：订阅某个主题，并接收与该主题相关的消息。
- **代理（Broker）**：负责管理所有的消息发布和订阅。它是 MQTT 网络的核心。

!!! example "参考文档"
    - [EMQX GitHub](https://github.com/emqx/emqx)
    - [EMQX 文档](https://www.emqx.io/docs/en/v5.0/)
    - [paho-mqtt，Python 工具包文档](https://pypi.org/project/paho-mqtt/)
    - [PySerial，Python 工具包文档](https://wiki.python.org/moin/PySerial)

## 环境安装

### Docker 环境

1.docker 安装：过程略
2.[下载 EMQX 开源版](https://www.emqx.com/zh/downloads-and-install/broker?os=Docker)

```shell title="安装 EMQX"
docker pull emqx/emqx:5.8.3
```

```shell title="启动 EMQX"
docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx:5.8.3
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__IOT__assets__Protocol-MQTT.assets__20241219163331.webp)

## EMQX 使用

[魔杖技术文档 – SZU\_TIC](https://chainpray.top/%e9%ad%94%e6%9d%96%e6%8a%80%e6%9c%af%e6%96%87%e6%a1%a3/#Homeassistant%E5%92%8CMQTT%E5%AE%89%E8%A3%85)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__IOT__assets__Protocol-MQTT.assets__20250221153305997.webp)

### 账号相关

```shell title="添加 Dashboard 用户"
emqx ctl admins add <Username> <Password> <Description> 
```

```shell title="重置指定用户的密码"
emqx ctl admins passwd <Username> <Password> 
```

```shell title="删除指定用户"
emqx ctl admins del <Username> 
```

### 使用

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__IOT__assets__Protocol-MQTT.assets__20250221154249938.webp)

## Python 编程

Python 中常用的 MQTT 客户端库是 `paho-mqtt`，它是 Eclipse Paho 项目的一部分。

```bash
pip install paho-mqtt
```

### 常见指令

| 方法 | 描述 |
| ---------------------------------- | -------------------------------------------------------- |
| `mqtt.Client("client_id")` | 创建一个 MQTT 客户端实例 |
| `client.connect(broker, port, keepalive)` | 连接到 MQTT 代理服务器 |
| `client.subscribe(topic)` | 订阅一个主题 |
| `client.publish(topic, payload)` | 发布消息到指定的主题 |
| `client.on_connect` | 设置连接回调函数（连接成功后执行的函数） |
| `client.on_message` | 设置消息接收回调函数（当接收到订阅主题的消息时执行的函数） |
| `client.loop_start()` | 启动客户端并在后台运行（非阻塞） |
| `client.loop_forever()` | 启动客户端并在当前线程运行（阻塞） |
| `client.disconnect()` | 断开与代理的连接 |

### 实例

CS 模式

需要有一个 mosquitto 服务器，用于订阅和发布消息。

```shell title="安装 mosquitto"
brew install mosquitto
```

```shell title="启动 mosquitto"
mosquitto -v
```

```text title="mosquitto 日志"
1765886137: mosquitto version 2.0.22 starting
1765886137: Using default config.
1765886137: Starting in local only mode. Connections will only be possible from clients running on this machine.
1765886137: Create a configuration file which defines a listener to allow remote access.
1765886137: For more details see https://mosquitto.org/documentation/authentication-methods/
1765886137: Opening ipv4 listen socket on port 1883.
1765886137: Opening ipv6 listen socket on port 1883.
```

```python title="publisher 程序"
import paho.mqtt.client as mqtt
import time

# MQTT 配置
BROKER = "localhost"  # 替换为你的 MQTT Broker 地址
PORT = 1883
TOPIC = "topic"  # 主题

# 设置 MQTT 客户端
client = mqtt.Client()
client.username_pw_set("user id", "passwd")  # 设置用户名和密码
client.connect(BROKER, PORT, 60)

client.publish(TOPIC, message)
print(f"已发送消息：{message}")
time.sleep(1)  # 可选的延时，防止过快发送

client.disconnect()
```

```python title="subscriber 程序"
import paho.mqtt.client as mqtt
import os

BROKER = "localhost"  # 替换为你的 MQTT Broker 地址
PORT = 1883
TOPIC = "topic"  # 主题，用于接收开关控制消息

import time

# 回调函数，当接收到 MQTT 消息时触发
def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(payload)
    # 执行操作

# 设置 MQTT 客户端
client = mqtt.Client()
client.on_message = on_message
client.username_pw_set("user id", "passwd")  # 设置用户名和密码
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("已经连接，等待接受信息")
client.loop_forever()
```
