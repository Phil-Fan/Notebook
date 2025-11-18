# 文件与数据处理

## 正则表达式

## 文件格式化

## 数据处理三剑客

### 过滤文本 grep

`-C` ：获取查找结果的上下文（Context）；

`-v` 将对结果进行反选（Invert），也就是输出不匹配的结果。

`-R` 会递归地进入子目录并搜索所有的文本文件。

[通过 14 个实例彻底掌握 grep 命令 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/561445240)

```bash
## 在文件中搜索单词或字符串
$ sudo grep nobody /etc/passwd

## 多文件中的搜索模式
$ sudo grep linuxtechi /etc/passwd /etc/shadow /etc/gshadow

## 打印与模式匹配的文件名
假设我们想列出包含单词“root”的文件名，可以在 grep 命令中使用“-l”选项，后跟单词（模式）和文件。
$ grep -l 'root' /etc/fstab /etc/passwd /etc/mtab

## 显示带有行号的输出行
$ grep -n 'nobody' /etc/passwd

## 反转模式匹配
$ grep -v 'nobody' /etc/passwd

## 打印以特定字符开头的所有行
Bash Shell 将插入符号 “^” 视为特殊字符，用于标记行或单词的开头。
$ grep ^backup /etc/passwd

## 打印文件中的所有空行
$ grep '^$' /etc/sysctl.conf
$ grep -n '^$' /etc/sysctl.conf #打印空行行号

## 计算与模式匹配的行数
“-c” 选项用于计算与搜索模式匹配的行数。
假设我们要计算 /etc/password 文件中以 “false” 结尾的行数
$ grep -c false$ /etc/passwd
```

- ack，rg

```bash
# 查找所有使用了 requests 库的文件
rg -t py 'import requests'

# 查找所有没有写 shebang 的文件（包含隐藏文件）
rg -u --files-without-match "^#!"

# 查找所有的foo字符串，并打印其之后的5行
rg foo -A 5

# 打印匹配的统计信息（匹配的行和文件的数量）
rg --stats PATTERN
```

### 修改文本 sed

### 处理文本 awk

awk 主要是用来格式化

[linux awk 命令详解 - ggjucheng - 博客园 (cnblogs.com)](https://www.cnblogs.com/ggjucheng/archive/2013/01/13/2858470.html)

awk 工作流程是这样的：先执行 BEGING，然后读取文件，读入有/n 换行符分割的一条记录，然后将记录按指定的域分隔符划分域，填充域，\$0则表示所有域，\$1表示第一个域，$n表示第 n 个域，随后开始执行模式所对应的动作 action。接着开始读入第二条记录······直到所有的记录都读完，最后执行 END 操作。

```bash
awk [参数] [处理内容] [操作对象] 
```
