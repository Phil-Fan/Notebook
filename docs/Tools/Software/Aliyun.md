# Aliyun
## ECS



## CDN

## 域名

### SSL证书
[数字证书管理服务管理控制台](https://yundunnext.console.aliyun.com/?spm=a2c4g.11186623.0.0.30cd27b8XwwRFJ&p=cas#/certExtend/free/cn-hangzhou?currentPage=1&pageSize=10&keyword=&statusCode=)
[在Linux环境的Nginx或Tengine服务器上安装国际标准SSL证书-数字证书管理服务（原SSL证书）-阿里云](https://help.aliyun.com/zh/ssl-certificate/user-guide/install-ssl-certificates-on-nginx-servers-or-tengine-servers?spm=5176.2020520163.console-base_help.dexternal.3ad1cfALcfAL96#6f3a67c335p0g)

## 备案


## OSS


### OSS util

下载之后可以

```
mv ossutil /usr/local/bin/
```

打开设置页面，在隐私与安全性中，拉到最下面，同意使用

```shell title="配置OSS util"
ossutil config
```
[AccessKey ID申请](https://ram.console.aliyun.com/users)
- `AccessKey ID`
- `AccessKey Secret`: 自己保存好
- `Endpoint`: [none] 直接回车
- `Region`: cn-beijing

```shell title="查看OSS桶"
ossutil ls oss://philfan-pic
```

```
ossutil cp source dest [flags]
```
- `source`: 本地文件路径。支持相对路径、绝对路径和-，当为-时，表示从标准输入读入。
- `dest`: 目标Bucket下的文件路径。例如：`oss://bucket[/prefix]`。


```shell title="创建目录"
ossutil mkdir oss://bucket/dir_name [flags]
```

## PAI智能体