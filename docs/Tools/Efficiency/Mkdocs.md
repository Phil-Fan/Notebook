---
status:new
---
# Mkdocs

## 我为什么选择 Mkdocs

在我看来 mkdocs 的构建形式其实是适合结构化的知识和文档的，很多时候是需要博主自己去把自己的知识梳理出一个树形的逻辑 (nav)
所以它和 98 这种以帖、标签、版面为主导的网页以及一些以帖为组织单元的博客网页（比如很多 wordpress 的模版）是有设计哲学的差别的

严格来讲或许叫它技术文档站可能更合适一点，当然从易用性来看，用 pages 托管的 mkdocs 部署服务比一众需要自己搭前后端的网站要简单不少，但是也有麻烦之处，比如写博文或者写随笔可能 mkdocs 并不是一个合适的选择（每次更新需要重新更新目录）。

自己建站的话很大比起内容来讲精力有些时间可能更多会花在配置环境、增添属性上 doge，虽然 mkdocs 我也经常干这种事、、、

## 有什么其他的工具？

- [Notion](https://www.notion.so/)
- [WordPress](https://wordpress.org/)
- [Jekyll](https://jekyllrb.com/)
- [Hexo](https://hexo.io/)
- [Hugo](https://gohugo.io/)
- [VuePress](https://vuepress.vuejs.org/)

## Acknowledgement

这里放一些好的资源和博客

[Mkdocs Material 文档](https://squidfunk.github.io/mkdocs-material/)

[Mkdocs Material 使用记录 - shafish.cn](https://shafish.cn/blog/mkdocs/#%E5%9B%9B%E9%83%A8%E7%BD%B2)

[Mkdocs 中文教程 - Wcowin](https://wcowin.work/Mkdocs-Wcowin/blog/MIT.html)

## Build From Scratch

### 本地部署

### Github-Pages

发布也遇到了好几个坑

[GitHub Pages 文档自动化部署 - MkDocs - Arisa | Blog](https://blog.arisa.moe/blog/2022/220407-github-pages/#vcs)

[github pages 绑定域名 - 腾讯云开发者社区 - 腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1454059)

- 编写`workflow`文件

在仓库上方有 actions 选项，点击 new workflow，我这里选择了自己编写的 workflow 文件，貌似也有针对 Mkdocs 的模板

```yml
name: deploy

on:
  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0    # for mkdocs-git-revision-date-localized-plugin
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - name: Create CNAME file
        run: echo "www.philfan.cn" > docs/CNAME   # Adjust the path if your configuration is different
      - run: mkdocs gh-deploy --force
```

- 设置 deploy from branch

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Efficiency__assets__Mkdocs.assets__20240707225202.webp)

### 自定义域名

- 设置自定义域名
  将域名填入`CNAME`文件中，然后打开仓库的设置界面，在 cumtom domain 中设置好自己的域名

### Vercel 部署

[MkDocs + Vercel](https://mkdocs.celsiusnarhwal.dev/)

## Markdown 相关功能

### 提示块

!!! failure "这是 failure 类型的提示框"
 注意`extension`不要拼成`extention`！！

!!! bug "这是 bug 类型的提示框"
    发现一个 bug，请尽快修复！

!!! tip "tip"

!!! note "note"

!!! question "这是 question 类型的提示框"
    这是一个问题，请回答！

!!! warning "这是 warning 类型的提示框"
    注意！注意！注意！

!!! success "这是 success 类型的提示框"
    恭喜你，完成了一个任务！

!!! example "这是 example 类型的提示框"

!!! info "这是 info 类型的提示框"

!!! abstract "这是 abstract 类型的提示框"

!!! quote "这是 quote 类型的提示框"

### 列表

```text
- [x] finished
- [ ] not finished
```

### 图标 Badge

其实是一个图片

[![image](https://img.shields.io/github/stars/Phil-Fan/Phil-Fan.github.io)](https://github.com/Phil-Fan/Phil-Fan.github.io)

- [Badge 制作指北——手把手教你制作 Badge - 少数派](https://sspai.com/post/81310)
- [Static Badge | Shields.io](https://shields.io/badges)
- [Simple Icons](https://simpleicons.org/)
- [Semantic Scholar - Academic Graph API](https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data)
- [Google Scholar API | Scrape Google Scholar - SerpApi](https://serpapi.com/google-scholar-api)

### 代码块

[Code blocks(代码块) - Material for MkDocs](https://wdk-docs.github.io/mkdocs-material-docs/reference/code-blocks/#annotations-with-numbers)

`hl_lines="2 3"` 高亮行

`linenums="1"` 显示行号

`title="bubble_sort.py"` 显示文件名字

### 嵌入 b 站/youtube 视频

1.打开 B 站的视频
2.点击“分享”按钮，获取“嵌入代码”：B 站视频的下一行，点击“分享”按钮，下方弹出分享页面。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Efficiency__assets__Mkdocs.assets__20241031230641.webp)

禁用方法很简单，就是在视频 url 链接最后加上 autoplay=0。例如：

```html title="禁止自动播放"
<iframe src="//player.bilibili.com/player.html?aid=951910057&bvid=BV1zs4y177sv&cid=1078968085&page=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="500" height="300"> </iframe>
```

??? info "参数用途"

    | 参数用途                         | 参数名      | 使用方法          |
    |----------------------------------|-------------|-------------------|
    | 是否自动播放(默认否)            | `autoplay`    | 1: 开启, 0: 关闭  |
    | 默认弹幕开关(默认开启)          | `danmaku`    | 1: 开启, 0: 关闭  |
    | 是否默认静音(默认否)            | `muted`       | 1: 开启, 0: 关闭  |
    | 一键静音按钮是否显示(默认不显示) | `hasMuteButton` | 1: 开启, 0: 关闭  |
    | 视频封面下方是否显示播放量弹幕量等信息(默认显示) | `hideCoverInfo` | 1: 开启, 0: 关闭  |
    | 是否隐藏弹幕按钮(默认不隐藏)    | `hideDanmakuButton` | 1: 开启, 0: 关闭 |
    | 是否隐藏全屏按钮(默认显示)      | `noFullScreenButton` | 1: 开启, 0: 关闭 |
    | 是否开始记忆播放(默认开启)      | `fw`          | 1: 开启, 0: 关闭  |
    | 默认开始时间(默认0)             | `t`           | 直接填写数值, 单位秒 |
    | 是否显示高清(默认否)            | `highQuality` | 1: 开启, 0: 关闭 (貌似是无用的, 各位可以试试) |

### 嵌套列表

> 来自 [解决 mkdocs 不支持无序列表嵌套 - SegmentFault 思否](https://segmentfault.com/a/1190000042842937)

安装 `mdx_truly_sane_lists`

```shell
pip install mdx_truly_sane_lists
```

然后在 `mkdoc.yml` 的 `markdown_extensions` 添加 `mdx_truly_sane_lists` 就好了

### 嵌入下载界面

```html
<iframe src="xxx.pdf" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>
```

```html
<div class="card file-block" markdown="1">
<div class="file-icon"><img src="/style/images/xmind.svg" style="height: 3em;"></div>
<div class="file-body">
<div class="file-title">思维导图</div>
<div class="file-meta">xxxxKB / 2024-01-10</div>
</div>
<a class="down-button" target="_blank" href="xxx.xmind" markdown="1">:fontawesome-solid-download: 下载</a>
</div>
```

### mermaid 支持

## 个性配置 —— Mkdocs DIY

### Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

??? note "安装代码"

 ```Shell
    pip install mkdocs
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    pip install mkdocs-git-revision-date-localized-plugin
    pip install mkdocs-statistics-plugin
    pip install mkdocs-heti-plugin
 ```

### 页面组织

- index.md 会放到小标题下的第一个页面

### Overrides

#### 主页

#### banner 位置

### social links

### nav 配置

### hooks

### Mathjax

[mkdocs-material/docs/plugins/privacy.md 在 master ·squidfunk/mkdocs-材料](https://github.com/squidfunk/mkdocs-material/blob/master/docs/plugins/privacy.md)

jupyter 遇到了单行公式无法显示的问题
[Local MathJax with mkdocs-jupyter · squidfunk/mkdocs-material · Discussion #7134](https://github.com/squidfunk/mkdocs-material/discussions/7134)

Steps to reproduce

Download MathJax:

```shell
wget https://github.com/mathjax/MathJax/archive/refs/tags/3.2.2.zip
unzip 3.2.2.zip "MathJax-3.2.2/es5/*" -d docs/assets/javascripts/
```

Create mathjax.js:

```js title="mathjax.js"
window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
    //   displayMath: [ ['$$', '$$'], ['\[', '\]'] ],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
    //   ignoreHtmlClass: ".*|",
    //   processHtmlClass: "arithmatex"
    }
  };
  document$.subscribe(() => { 
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
  })
```

Adapt nbconvert:, removing implicit load of Mathjax (see here)

```shell title="remove mathjax"
sed -i 's#https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe##g' venv/lib/python3.12/site-packages/nbconvert/exporters/html.py
```

这一步如果在虚拟环境下面，自己找到对应的路径进行修改

```yml title="static.yml"
- name: Modify nbconvert HTML exporter
        run: sed -i 's#https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe##g' $(python -c "import nbconvert; print(nbconvert.__file__.replace('__init__.py', 'exporters/html.py'))")
```

Adjust mkdocs.yml:

```yml title="mkdocs.yml"
plugins:
    - privacy
    - mkdocs-jupyter

extra_javascript:
  - assets/javascripts/mathjax.js
  - assets/javascripts/MathJax-3.2.2/es5/tex-mml-chtml.js
```

### 查看与编辑代码

### 颜色主题

## 锦上添花 —— Plugins

### Blog

blog 功能 下面这个仓库有[template](https://github.com/mkdocs-material/create-blog/tree/main)

1. 首先在 docs 文件夹下放一个 blog 目录，下面是一个目录的样例

    ```shell
    docs/blog
    ├── author
    │   └── team.md
    ├── posts ---------------------------------- 放所有的博文
    │   ├── drafts ----------------------------- drafts 目录下是所有的草稿
    │   │   └── draft.md
    │   └── helloworld.md
    ├── index.md
    └── tags.md
    ```

2. 配置一下`mkdocs.yml`，具体的配置可以看这个[Basic blogs - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/tutorials/blogs/basic/)

```yml
- blog:
    blog_toc: true
    archive_date_format: MMMM yyyy
    # authors_profiles: true
    pagination_per_page: 5
```

### RSS

**RSS (Really Simple Syndication / RDF Site Summary / Rich Site Summary)**
 是一种基于 XML 的内容分发格式，常用于网站内容的聚合与订阅。

简单来说：

- 网站提供 **RSS Feed**（订阅源），里面包含文章标题、摘要、链接、发布时间等信息。
- 用户用 **RSS 阅读器**（如 Feedly、Inoreader、Tiny Tiny RSS 等）订阅这些源，就能在一个地方集中看到多个网站的更新，而不用逐个打开网站。

工作原理

1. 网站生成一个 RSS 文件（通常是 `.xml` 格式），例如：`https://example.com/feed.xml`
2. RSS 阅读器定期抓取这个文件。
3. 阅读器解析 XML，把文章列表显示给用户。
4. 用户可以在阅读器中点击链接，跳转到原网站查看全文。

配置方法

第一步，安装插件

```shell
pip install mkdocs-rss-plugin
```

第二步，在`mkdocs.yml`中加入以下信息

```yml
site_description: required. Used as feed mandatory channel description.
site_name: required. Used as feed mandatory channel title and items source URL label.
site_url: required. Used to build feed items URLs.

plugins:
  - rss
```

### git-committers

[byrnereese/mkdocs-git-committers-plugin: A mkdocs plugin for displaying the last commit and a list of a file's contributors.](https://github.com/byrnereese/mkdocs-git-committers-plugin)

这个插件的作用是在页面底部显示该文档的贡献者，比较适合有多个作者的情况，我这个库目前暂时还只有我一个人 qwq，觉得好玩还是放了一下。

为了可以解决 git-committers 插件的 token 问题，需要设置环境变量，但是这种 token 不适宜明文传递，所以需要使用 github 的 secret 来存储

所以第一步是在 github 的仓库中设置 secret

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Efficiency__assets__Mkdocs.assets__image-20250817151216756.webp)

第二步是在 github actions 中设置环境变量

```yml title="github actions"
- name: Deploy with MkDocs
    run: export MKDOCS_GIT_COMMITTERS_APIKEY=${{ secrets.MKDOCS_GIT_COMMITTERS_APIKEY }} && mkdocs gh-deploy --force
```

第三步是在 mkdocs.yml 中设置插件和 token

```yml
plugins:
  - git-committers:
      repository: johndoe/my-docs
      branch: master
      token: !!python/object/apply:os.getenv ["MKDOCS_GIT_COMMITTERS_APIKEY"]
```

### Jupyter Notebook

使用 mkdocs-jupyter 插件可以支持 jupyter notebook 文件
[mkdocs-jupyter](https://pypi.org/project/mkdocs-jupyter/)
[Jupytext demo (.py) - mkdocs-jupyter demo](https://mkdocs-jupyter.danielfrg.com/demo-script/)

[mkdocs-jupyter/demo/mkdocs.yml at main · danielfrg/mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter/blob/main/demo/mkdocs.yml)

```shell
pip install mkdocs-jupyter
```

```yml title="mkdocs.yml" hl_lines="11" linenums="1"
nav:
    - Home: index.md
    - Notebook page: notebook.ipynb
    - Python file: python_script.py
plugins:
    - mkdocs-jupyter
        execute: true
        kernel_name: python3
        theme: dark
        include_source: True
        custom_mathjax_url: "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"
```

!!! bug "遇到的问题"
    1. 无法显示数学公式（解决方法：加上了 js 文件）
    2. toc 配置与之前的逻辑不同，导致自动配置 123 的时候出现错误
    3. 奇怪的路径问题

    ```
      DeprecationWarning: Jupyter is migrating its paths to use standard platformdirs
      given by the platformdirs library.  To remove this warning and
      see the appropriate new directories, set the environment variable
      `JUPYTER_PLATFORM_DIRS=1` and then run `jupyter --paths`.
      The use of platformdirs will be the default in `jupyter_core` v6
    ```
    
    [DeprecationWarning: Jupyter is migrating its paths to use standard platformdirs · Issue #148 · danielfrg/mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter/issues/148)

如果想要实现 material 中的某些功能，需要自己写 html 代码

```html
<details class="tip">
    <summary>Extra: What are latent variables?</summary>
    <p><br>
    If you go about exploring any paper talking about Variational Inference, then most certainly, the papers mention about latent variables instead of parameters. The parameters are fixed quantities for the model whereas latent variables are  <strong>unobserved</strong> quantities of the model conditioned on parameters. Also, we model parameters by probability distributions. For simplicity, let's consider the running terminology of  <strong>parameters </strong> only.
    </p>
</details>
```

```html
<div class="admonition success">
    <p class="admonition-title">Success</p>
    <p>
        The above ELBO equation is the final one which needs to be optimized.
    </p>
</div>
```

### Github 评论

- 安装[giscus](https://giscus.app/zh-CN)

1. 安装 giscus GitHub App。这一步只需要在 GitHub 官网上点击安装即可。
2. 访问 giscus 官网，配置与 giscus 评论系统关联的 GitHub 仓库。

请确保：

- 该仓库是**公开**的，否则访客将无法查看 Discussions。
- **giscus app** 已安装，否则访客将无法评论和回应。
- Discussions 功能已在你的仓库中启用。

在`mkdocs.yml`中添加如下配置

```yml linenums="1" hl_lines="3"
theme:
  name: material
  custom_dir: overrides  #主要是这一行
```

访问[giscus](https://giscus.app/)网站，并通过网站上的配置工具生成代码段。复制此代码段，下面的步骤要用
复制如下面格式的代码到`overrides/comments.html`文件中

```html
<script src="https://giscus.app/client.js"
        data-repo="Phil-Fan/Phil-Fan.github.io"
        data-repo-id=""
        data-category="General"
        data-category-id=""
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="dark"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
```

```html hl_line="5"

{% if page.meta.comments %}
  <h2 id="__comments">{{ lang.t("meta.comments") }}</h2>

  <!-- Insert generated snippet here -->
  <!-- 在这里粘贴刚才获得代码段 -->
  <!-- ... -->

  <!-- Synchronize Giscus theme with palette -->
  <script>
    var giscus = document.querySelector("script[src*=giscus]")

    /* Set palette on initial load */
    var palette = __md_get("__palette")
    if (palette && typeof palette.color === "object") {
      var theme = palette.color.scheme === "slate" ? "dark" : "light"
      giscus.setAttribute("data-theme", theme) 
    }

    /* Register event handlers after documented loaded */
    document.addEventListener("DOMContentLoaded", function() {
      var ref = document.querySelector("[data-md-component=palette]")
      ref.addEventListener("change", function() {
        var palette = __md_get("__palette")
        if (palette && typeof palette.color === "object") {
          var theme = palette.color.scheme === "slate" ? "dark" : "light"

          /* Instruct Giscus to change theme */
          var frame = document.querySelector(".giscus-frame")
          frame.contentWindow.postMessage(
            { giscus: { setConfig: { theme } } },
            "https://giscus.app"
          )
        }
      })
    })
  </script>
{% endif %}

```

**一个页面单独添加**

在每个文档头前添加 comments: true

```markdown
---
comments: true
---
```

**所有页面**

在`mkdocs.yml`的插件中添加

```yml
plugins:
  - comments
```

[mkdocs-material 集成评论系统 - 知识库 (geodoer.github.io)](https://geodoer.github.io/Z-工具/博客相关工具/mkdocs/mkdocs-material/评论系统/#commentshtml)
[为 Mkdocs 网站添加评论系统（以 giscus 为例）\_giscus mkdocs-CSDN 博客](https://blog.csdn.net/m0_63203517/article/details/133819706)

### changelog

[TonyCrane/mkdocs-changelog-plugin: A MkDocs plugin that create changelog in a page](https://github.com/TonyCrane/mkdocs-changelog-plugin?tab=readme-ov-file)

在 mkdocs.yml 中启用插件：

```yml
plugins:
    - changelog
```

changelog 从外部的 yaml 文件读取，默认在 docs/changelog.yml 中，可以通过 file 选项来选择其他位置：

```yml
plugins:
  - changelog:
      file: changelog.yml
```

按照格式编写 changelog yaml 文件（见下）
在需要插入 changelog 的页面 meta 部分中添加：

```yml
changelog: True
```

在页面需要插入对应部分的位置添加：

```text
{{ placeholder }}
```

```yml title="changelog.yml格式"
- "placeholder1":
  - "time1":
    - "type": text
    - "type": text
- "placeholder":
  - "time2":
    - "type":
        text: text
        href: /link/to/page/
    - "type":
        text: text
        href: /link/to/page/
  - "time3":
    - "type": text
```

示范
[note/docs/changelog.yml at master · TonyCrane/note](https://github.com/TonyCrane/note/blob/master/docs/changelog.yml)

### git-revision

### statistics

使用统计插件

### heti

### mkdocs-video

### minify

有 bug

### 解析 xmind

!!! todo "可以实现吗"

[OpenFiles.online](https://openfiles.online/)
[在浏览器中解析和渲染 XMind 文件 | 文森的主站](https://liangwensen.com/blog/parse-and-render-xmind-file-in-browser)

## Deprecated

### 图床的配置与更换

原先配置的时候使用的是 gitee 的仓库配置

但在发布网站后发现所有的图片都无法显示

#### 原因

[查询资料](https://blog.csdn.net/qq_45173404/article/details/123759688)后发现是 Gitee 防盗链的原因

>发现图片请求的过程与上面不同，请求头中多了一个`Referer`字段，也就是我自己的 gitee 地址。
>应该是 Gitee 添加了防盗链机制，当我们通过直接访问存储在 Gitee 上的图片时，Http 请求头没有 Referer 字段，所以被 Gitee 服务器当作黑名单而拒绝响应。而前面我们通过 Gitee Page 部署的 Hexo 博客请求时，由于代码都托管在 Gitee 上，在加载所有图片的时候都附加了 Referer 字段指向 Gitee，相当于被 Gitee 服务器看作白名单因而可以访问。

#### 解决办法

将图像存储更改为阿里云 OSS，根据[教程](https://zhuanlan.zhihu.com/p/104152479)做出以下操作

- 购买阿里云 oss 服务
- 创建用户，记录 id 和密码
- 将图床中的所有图片迁移到阿里云当中
- 更换 picgo 中服务
- 更换`.md`中所有图片的链接

picgo 中的设置如下

1. 设定`keyid`，就是创建用户的`AccessKey ID`，
2. `KeySecret` 就是`AccessKeySecret`
3. 存储空间名就是创建 Bucket 的名字，存储区域也是创建时设定的，忘记的可以通过 Bucket 概览查看，如下图所示：
4. 存储路径默认设置 img/即可
5. 如果自己有已经备案的域名，可以填写设定自定义域名，如果没有不填即可。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Efficiency__assets__Mkdocs.assets__20240813014140.webp)

#### 图床的迁移

[利用 PicGo 快速迁移 Gitee 图床外链图片到服务器 - 腾讯云开发者社区 - 腾讯云](https://cloud.tencent.com/developer/article/1975652)

[替换的工具 - 时光](https://blog.shiguang666.eu.org/2024/10/15/6b65681b29d7/#%E4%B8%80%E3%80%81%E9%9C%80%E6%B1%82%E6%8F%8F%E8%BF%B0)

[jarvanstack/markpic: 一键下载 markdown 中图片，并通过 picgo 上传图片到图床并替换链接](https://github.com/jarvanstack/markpic)

### 显示音乐符号

关于安装 lilypond

LilyPond (荷花池) 是一个音乐雕版软件，致力产生最高质量的乐谱。它把传统音乐雕版印刷的美学，呈现在计算机打印的乐谱上。LilyPond 是自由软件，也是 GNU Project 的一部分。

[Download (LilyPond – 人人的乐谱软件)](https://lilypond.org/download.zh.html)

下载之后，是没有安装的，但是需要将其添加到环境变量中.win 菜单搜索`查看高级环境设置`,在 path 中添加`lilypond\bin\`的路径

编译

```shell
lilypond -o output music.ly
```

[LilyPond 学习手册：LilyPond — 学习手册](https://lilypond.org/doc/v2.23/Documentation/learning/index)

[关于在 Markdown 中描述音乐符号](https://blog.twofei.com/1425/)
[Lilypond in Markdown](https://lilypond-in-markdown.netlify.app/)

[Render LilyPond in Markdown](https://pianomanfrazier.com/post/lilypond-in-markdown/)

[uliska/markdown-lilypond：支持 LilyPond（符号软件）输入的 MkDocs 插件](https://github.com/uliska/markdown-lilypond)

### termynal

作用：动态显示终端窗口

```shell
pip install termynal
```
