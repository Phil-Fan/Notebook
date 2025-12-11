---
date:
  created: 2025-10-18
  updated: 2025-10-18
readtime: 8
pin: true
categories:
  - Settings
tags:
  - Website
authors:
  - Phil-Fan
nostatistics: true
---


# Aliyun ECS + Mkdocs 网站部署与配置

## 一、前提条件

1. 拥有一个域名，例如 `philfan.cn`。
2. 拥有一台服务器，且服务器具有可访问公网 IP，例如 `47.xxx.xxx.xxx`。
3. 已经有 Mkdocs 文档，比如 (`gh-pages`分支)

---

## 二、准备网站目录

假设你的 MkDocs 构建输出目录为 `/www/philfan.cn`：

```bash
sudo mkdir -p /www/philfan.cn
sudo chown -R USERNAME:USERNAME /www/philfan.cn
sudo chmod -R 755 /www/philfan.cn
```

> ⚠️ `USERNAME` 用户是你用于部署网站的普通用户，拥有该目录的写权限即可，无需 sudo。

---

## 三、配置 Nginx

```shell
sudo apt-get install nginx -y
```

```shell
sudo systemctl start nginx
sudo systemctl enable nginx
```

```shell
sudo systemctl status nginx
```

### 1. 创建站点配置文件

```bash
sudo vi /etc/nginx/sites-available/philfan.cn.conf
```

内容示例：

```txt title="配置 nginx serve 在 80 端口，根目录是/www/philfan.cn"
server {
    listen 80;
    server_name philfan.cn www.philfan.cn;

    root /www/philfan.cn;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location ~ /\. {
        deny all;
    }

    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml+rss image/svg+xml;
    gzip_min_length 256;
}
```

### 2. 测试配置并重载 Nginx

```bash
sudo ln -s /etc/nginx/sites-available/philfan.cn.conf /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## 四、配置 GitHub Actions 自动上传

!!! note "原理其实就是 scp 上传文件到服务器"

在仓库中创建 `.github/workflows/ssh-upload.yml`：

```yaml
name: upload-to-server

on:
  workflow_run:
    workflows: ["deploy"]
    types:
      - completed

jobs:
  upload:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout gh-pages
        uses: actions/checkout@v3
        with:
          ref: gh-pages

      - name: Deploy to Server via SSH
        uses: appleboy/scp-action@v0.1.7
        with:
          host: ${{ secrets.SSH_HOST }}
          username: ${{ secrets.SSH_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          source: "./"
          target: "/www/philfan.cn"
```

### 1. 配置 GitHub Secrets

在 GitHub 仓库 `Settings → Secrets and Variables → Actions` 添加：

| Secret 名称       | 内容                 |
| --------------- | ------------------ |
| SSH_HOST        | 服务器公网 IP 或域名       |
| SSH_USER        | USERNAME            |
| SSH_PRIVATE_KEY | 对应 SSH 私钥（用于登录服务器） |

### 2. 生成 SSH 密钥对（本地）

```bash title="生成SSH密钥对"
ssh-keygen -t ed25519 -C "github-action-deploy"
```

```shell title="复制公钥到服务器"
ssh-copy-id -i ~/.ssh/id_ed25519.pub USERNAME@47.xxx.xxx.xxx 
# 也可以
cp ~/.ssh/id_ed25519.pub ~/.ssh/authorized_keys
```

```shell title="测试"
ssh -i ~/.ssh/id_ed25519 USERNAME@47.xxx.xxx.xxx
```

---

## 五、阿里云 DNS 配置

1. 登录阿里云控制台：[https://dns.console.aliyun.com](https://dns.console.aliyun.com)
2. 选择你的域名，进入“解析设置”
3. 添加解析记录：

    | 记录类型 | 主机记录 | 记录值（服务器 IP）    | 说明                                      |
    | ---- | ---- | -------------- | --------------------------------------- |
    | A    | @    | 47.xxx.xxx.xxx | 根域名 philfan.cn                          |
    | A    | www  | 47.xxx.xxx.xxx | [www.philfan.cn](http://www.philfan.cn) |

4. 保存，等待 5~10 分钟生效
5. 测试解析：

```bash
dig philfan.cn +short
dig www.philfan.cn +short
```

浏览器访问：

```html
http://philfan.cn
https://philfan.cn（如已配置 HTTPS）
```
