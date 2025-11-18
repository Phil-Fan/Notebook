# 魔杖

!!! note "项目简介"
    - 项目名称：
    - 一句话简介：
    - 目的：
    - 项目进程：
      - [ ]
      - [ ]
      - [ ]
    - 相关知识记录
    - 项目技术栈
    - 项目难点
    - 项目成果

[赛博魔杖\_STM32 卷积神经网络 - 立创开源硬件平台](https://oshwhub.com/lyg0927/cyberwand-stm32-convolutional-ne)

[MagicWand-基于魔杖的智能家具控制 - 立创开源硬件平台](https://oshwhub.com/piaoray/magicwand)

[[开源]如何成为赛博法师，STM32 卷积神经网络动作识别\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV187pUeKEMr?spm_id_from=333.788.videopod.sections&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

[魔杖技术文档 – SZU\_TIC](https://chainpray.top/%e9%ad%94%e6%9d%96%e6%8a%80%e6%9c%af%e6%96%87%e6%a1%a3/#Homeassistant%E5%92%8CMQTT%E5%AE%89%E8%A3%85)

[【教程】home assistant 接入大模型，小爱唤醒与控制\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1uT1FYMERo/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

[HomeAssistant 成功接入豆包大模型，迎接 AI\_智能家居\_什么值得买](https://post.smzdm.com/p/awo537ep/)

[【Home Assistant 之 QQ 邮箱推送提醒】\_hacs 极速版使用-CSDN 博客](https://blog.csdn.net/vor234/article/details/127806826)

## 功能

- 手势识别

## 环境配置

### docker 安装

详见 docker 页面

### Home Assistant

```shell title="安装 HA"
docker pull homeassistant/home-assistant:latest
```

```shell title="启动 HA"
docker run -d --restart always --name homeassistant -v /data/homeassistant/config:/config -e TZ=Asia/Shanghai -p 8123:8123 homeassistant/home-assistant:latest
```

### EMQX

[下载 EMQX 开源版](https://www.emqx.com/zh/downloads-and-install/broker?os=Docker)

```shell title="安装 EMQX"
docker pull emqx/emqx:5.8.3
```

```shell title="启动 EMQX"
docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx:5.8.3
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Project__assets__wand.assets__20241219163331.webp)
