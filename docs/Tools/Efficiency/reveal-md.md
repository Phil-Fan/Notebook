# reveal-md

reveal.js 是一个开源的 HTML 框架，用于创建交互式演示文稿。

[官方网站 | reveal.js](https://revealjs.com/)

[TonyCrane 的模板](https://github.com/TonyCrane/slide-template?tab=readme-ov-file)

reveal.js: 用于制作演示文稿。

reveal-md: 用于将 markdown 文件转换为 reveal.js 的演示文稿。

```shell
npm install -g reveal-md
```

## reveal-md 使用

[MartenBE/mkslides: Use mkslides to easily turn markdown files into beautiful slides using the power of Reveal.js!](https://github.com/MartenBE/mkslides)

[使用 reveal-md 来写 Slides - Isshiki 修's Notebook](https://note.isshikih.top/others/reveal-md2Slides/)

```markdown
---
separator: <!--s-->
verticalSeparator: <!--v-->
---
```

背景图片？

我使用的方案是在 illustrator 中制作，然后导出为 svg 格式 or webp 格式，然后当作背景图片插入。

有关 illustrator 的使用记录，可以参考[Adobe Illustrator](../Software/AdobeIllustrator.md)

## Plugin

## reveal-md 模版

```shell
## 最基础的命令，根据 Markdown 文件在本地 1948 端口生成 Slides 服务。
$ reveal-md your-md-file.md

## 为了实现在线部署，需要导出为静态资源。
$ reveal-md your-md-file.md --static your-static-dir
```

[TonyCrane/slide-template: TonyCrane's slide template for reveal-md](https://github.com/TonyCrane/slide-template)

```makefile title="makefile"
.PHONY: live build clean

live:
 @echo "Previewing main slides..."
 @reveal-md main.dark.md -w --scripts https://cdn.tonycrane.cc/heti/heti.js,./utils/heti_worker.js,https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js --template ./utils/template.html || true

build:
 @echo "Building main slides..."
 @reveal-md main.dark.md --scripts https://cdn.tonycrane.cc/heti/heti.js,https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/latest.min.js,./utils/heti_worker.js --template ./utils/template.html --static ../site --assets-dir assets 
 @rm ../site/main.html

clean:
 @echo "Cleaning up..."
 rm -rf ../site/
```

```shell title="开启本地实时预览"
make  # or make live
```

```shell title="构建静态文件"
make build
```

- 生成 pdf 版：在 url 后面加上 `?print-pdf` 使用浏览器打印

如果在服务器上部署，需要开放端口，并注意在安全组中开放端口

```shell title="临时开放端口"
sudo ufw allow 1948/tcp
sudo ufw allow <port>/tcp
```
