# Nginx

## 隐藏端口

## SSL 服务

```shell
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d file.eestudy.com.cn
```

> Only UTF-8 encoding is supported. An unexpected error occurred: KeyError: '/etc/nginx/nginx.conf'

```shell
file -i /etc/nginx/nginx.conf
```

如果不是 utf-8 需要转码

```shell
sudo iconv -f GBK -t UTF-8 /etc/nginx/nginx.conf -o /etc/nginx/nginx.conf.utf8
sudo mv /etc/nginx/nginx.conf.utf8 /etc/nginx/nginx.conf
```

```shell
sudo nginx -t
sudo systemctl reload nginx
```

## 代理密码

```shell
sudo apt install apache2-utils
htpasswd -c /etc/nginx/.htpasswd alice   # 创建用户 alice
```

```shell title="查看密码"
cat /etc/nginx/.htpasswd
# 应该看到类似：
# user:$apr1$XXXXXXXXXXXXXXXXXXXXXX
```

## 错误码和问题解决

499

201

404

解决方法

curl 指令

chown
