# Vim

## 安装与配置

[教程](https://www.cnblogs.com/cxl-/p/15319734.html)

### 改键

编辑`.vimrc`文件

```text
inoremap jk <ESC> 
```

### 插件

[vim on vscode](https://www.cnblogs.com/YunyaSir/p/15522565.html)

F1 打开 首选项：用户设置，按需增添以下代码

```json
//j+j 替换 esc 键位，更加高效快捷
"vim.insertModeKeyBindings": [
    {
        "before": [
        "j",
        "j"
        ],
        "after": [
        "<Esc>"
        ]
    }
], 
//以下键位将由 vscode 进行处理
"vim.handleKeys": {
    "<C-a>": false,
    "<C-f>": false,
    "<C-x>": false,
    "<C-w>": false,
    "<C-b>": false,
},
// 突出显示与当前搜索匹配的所有文本
"vim.hlsearch": true,
```

[vimium-C on Chorme](https://vimium.github.io)
自定义搜索引擎

```text
b|ba|baidu|Baidu|百度：https://www.baidu.com/s?ie=utf-8&wd=%s \
  blank=https://www.baidu.com/ 百度
bi: https://www.bing.com/search?q=$s
bi|bing|Bing|必应：https://cn.bing.com/search?q=%s \
  blank=https://cn.bing.com/ 必应
g|go|gg|google|Google|谷歌：https://www.google.com/search?q=%s\
  www.google.com re=/^(?:\.[a-z]{2,4})?\/search\b.*?[#&?]q=([^#&]*)/i\
  blank=https://www.google.com/ Google

b.m|bm|map|b.map|bmap|地图 | 百度地图：\
  https://api.map.baidu.com/geocoder?output=html&address=%s&src=vimium-c\
  blank=https://map.baidu.com/
gd|gaode|高德地图：https://www.gaode.com/search?query=%s \
  blank=https://www.gaode.com
g.m|gm|g.map|gmap: https://www.google.com/maps?q=%s \
  blank=https://www.google.com/maps 谷歌地图

bili|bilibili|bz|Bili: https://search.bilibili.com/all?keyword=%s \
  blank=https://www.bilibili.com/ 哔哩哔哩
y|yt: https://www.youtube.com/results?search_query=%s \
  blank=https://www.youtube.com/ YouTube

w|wiki: https://www.wikipedia.org/w/index.php?search=%s Wikipedia
b.x|b.xs|bx|bxs|bxueshu: https://xueshu.baidu.com/s?ie=utf-8&wd=%s \
  blank=https://xueshu.baidu.com/ 百度学术
gs|g.s|gscholar|g.x|gx|gxs: https://scholar.google.com/scholar?q=$s \
  scholar.google.com re=/^(?:\.[a-z]{2,4})?\/scholar\b.*?[#&?]q=([^#&]*)/i\
  blank=https://scholar.google.com/ 谷歌学术

t|tb|taobao|ali|淘宝：https://s.taobao.com/search?ie=utf8&q=%s \
  blank=https://www.taobao.com/ 淘宝
j|jd|jingdong|京东：https://search.jd.com/Search?enc=utf-8&keyword=%s\
  blank=https://jd.com/ 京东
az|amazon: https://www.amazon.com/s?k=%s \
  blank=https://www.amazon.com/ 亚马逊

zhihu|zh|知乎:https://www.zhihu.com/search?type=content&q=%s

douban|db|豆瓣:https://www.douban.com/search?q=%s

wm|wayback:https://web.archive.org/web/20240000000000*/%s

98|cc98:https://www.cc98.org/search?boardId=0&keyword=%s

icon:https://www.iconfont.cn/search/index?searchType=icon&q=%s
iresearch|艾瑞 | 研报|yb:https://www.iresearch.com.cn/search?type=1&keyword=%s
png|img:https://pngimg.com/search_image/?search_image=%s

\:i: vimium://sed/s/^//,lower\ $S re= Lower case
v.m|math: vimium://math\ $S re= 计算器
v.p: vimium://parse\ $S re= Redo Search
github: https://github.com/search?q=$s \
  blank=https://github.com/ GitHub 仓库
gitee: https://search.gitee.com/?type=repository&q=$s \
  blank=https://gitee.com/ Gitee 仓库
js\:|Js: javascript:\ $S; JavaScript
```

## 简介

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Efficiency__assets__vim.assets__20240706181314.webp)

## 用法

### 正常模式

- 基本移动：`hjkl` （左，下，上，右）
词： `w` （下一个词）， `b` （上一个词/词初）， `e` （下一个词/词尾）
- 行： `0` （行初）， `^` （第一个非空格字符）， `$` （行尾）
屏幕： `H` （屏幕首行）， `M` （屏幕中间）， `L`（屏幕底部）
- 翻页： `Ctrl-u` （上翻）， `Ctrl-d` （下翻）
- 文件： `gg` （文件头）， `G` （文件尾）
行数：{行数}G ({行数}为行数)
- 杂项： `%` （找到配对，比如括号或者 `/* */` 之类的注释对）
- 查找：`f{字符}`，`t{字符}`，`F{字符}`，`T{字符}`
- 查找/到 向前/向后 在本行的
, / ; 用于导航匹配
- 搜索：/{正则表达式}, n / N 用于导航匹配

### 底线命令模式

在命令模式下按下 :（英文冒号）就进入了底线命令模式。

底线命令模式可以输入单个或多个字符的命令，可用的命令非常多。

在底线命令模式中，基本的命令有（已经省略了冒号）：

`:w`：保存文件。
`:q`：退出 Vim 编辑器。
`:wq`：保存文件并退出 Vim 编辑器。
`:q!`：强制退出 Vim 编辑器，不保存修改。

## 技巧

### [重复](https://blog.csdn.net/ii1245712564/article/details/46496347)

`.`操作就是用来重复上一次更改的

=== "example"
    用x操作来删除一个字符，接着用.重复删除字符
    ![image](https://img-blog.csdn.net/20150614230108127)
