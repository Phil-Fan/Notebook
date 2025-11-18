---
comments: true
---
# Jekyll

[Jekyll • 简单静态博客网站生成器 - 将纯文本转换为静态博客网站](https://jekyllcn.com/)

## 安装

### 安装`Jekyll`

```shell
gem install jekyll
```

!!! bug "ERROR: Could not find a valid gem 'sass-embedded' (~> 1.54) (required by 'jekyll' (>= 0)) in any repository ERROR: Possible alternatives: sass-embedded"
    这一步报错了，所以再把镜像源切换回官方的

    ```shell
    gem sources -a https://rubygems.org/
    ```

### 安装`jekyll-paginate`

```shell
gem install jekyll-paginate
```

验证 jekyll :  

```shell
jekyll -v
```

### 本地启动服务

在命令行中切换到你的网站仓库内

```shell
bundle install（这一步不要）

jekyll serve 
```

### 查看网站

`127.0.0.1:4000` 或 `localhost:4000`

注意：如端口被占用修改端口

```shell
jekyll serve -P 5555
```

## [academicpages](https://github.com/academicpages/academicpages.github.io)

> 参考
> [Wanjia Zhao](https://wanjiazhao1203.github.io/#academicservices)
> [Leo / Zeqing Yuan](https://leoyuan.site/)

```shell
bundle config set --local path 'vendor/bundle'
```

```shell
bundle install
```

```shell
bundle exec jekyll serve -l -H localhost
```
