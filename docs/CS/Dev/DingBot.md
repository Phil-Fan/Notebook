# 主流 IM 机器人

## 飞书

## 微信

## DingBot

[官方文档](https://open.dingtalk.com/document/orgapp/custom-robot-access)

### 使用方法

安全验证方式有三种：`IP地址`、`加签`、`自定义关键词`。
这里使用了`加签`的方式，使用已知的密钥进行加密
[自定义机器人安全设置 - 钉钉开放平台](https://open.dingtalk.com/document/robots/customize-robot-security-settings)

```python title='加签代码'
#python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse

timestamp = str(round(time.time() * 1000))
secret = 'this is secret'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)
```

```shell
curl 'https://oapi.dingtalk.com/robot/send?access_token=e4329714f94c' -H 'Content-Type: application/json'  -d '{"msgtype": "text","text": {"content":"我就是我，是不一样的烟火"}}'
```

### 消息类型

[自定义机器人接入 - 钉钉开放平台](https://open.dingtalk.com/document/orgapp/custom-robot-access)

### 高德天气 API

[天气查询 - 基础 API 文档 - 开发指南-Web 服务 API | 高德地图 API](https://lbs.amap.com/api/webservice/guide/api/weatherinfo/#t1)

| 参数名     | 含义             | 规则说明                                                         | 是否必须 | 缺省值 |
|-----------|------------------|------------------------------------------------------------------|---------|--------|
| key       | 请求服务权限标识  | 用户在高德地图官网申请 web 服务 API 类型 KEY                         | 必填     | 无     |
| city      | 城市编码           | 输入城市的 adcode，adcode 信息可参考城市编码表                          | 必填     | 无     |
| extensions| 气象类型           | 可选值：base/all <br> base:返回实况天气 <br> all:返回预报天气             | 可选     | 无     |
| output    | 返回格式           | 可选值：JSON/XML                                                 | 可选     | JSON   |
