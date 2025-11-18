# Shell 与 Shell Script

## Shell

### 通配

- 通配符 - 当你想要利用通配符进行匹配时，你可以分别使用 `?` 和 `*` 来匹配一个或任意个字符。例如，对于文件`foo`, `foo1`, `foo2`, `foo10` 和 `bar`, `rm foo?`这条命令会删除`foo1` 和 `foo2` ，而`rm foo*` 则会删除除了`bar`之外的所有文件。

​  *任意字符

​  ？特定字符

​  `[abcd]`有括号内的任一字符

​  `[0-9]`连续

​  `[^abc]`只要非 abc 就可以

- 花括号`{}` - 当你有一系列的指令，其中包含一段公共子串时，可以用花括号来自动展开这些命令。这在批量移动或转换文件时非常方便。

```bash
convert image.{png,jpg}
# 会展开为
convert image.png image.jpg

cp /project/{a,b,c}.sh /newpath
# 会展开为
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# 也可以结合通配使用
mv *{.py,.sh} folder
# 会移动所有 *.py 和 *.sh 文件

mkdir foo bar

# 下面命令会创建foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h这些文件
touch {foo,bar}/{a..h}
touch foo/x bar/y
# 比较文件夹 foo 和 bar 中包含文件的不同
diff <(ls foo) <(ls bar)
# 输出
# < x
# ---
# > y
```

- source 执行脚本

## Bash Shell 配置

[awesome-cheatsheets/languages/bash.sh at master · skywind3000/awesome-cheatsheets · GitHub](https://github.com/skywind3000/awesome-cheatsheets/blob/master/languages/bash.sh)

- bash = Bourne Again Shell

   bash 是命令解释程序，也是程序设计语言

- 功能：history、命令与文件补全、程序脚本 shell script、通配符 wildcard

- 程序头：脚本文件名、Author、Date、Description、

    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__Linux__assets__02-Shell.assets__image-20221120191459094.webp)![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__Linux__assets__02-Shell.assets__image-20221120191821981.webp)

- 注释

多行注释

```bash
:<<num

num
```

- shebang

​  在 Shebang 之后，可以有一个或数个空白字符，后接解释器的绝对路径，用于指明执行这个脚本文件的解释器。在直接调用脚本时，系统的程序载入器会分析 Shebang 后的内容，将这些内容作为解释器指令，并调用该指令，将载有 Shebang 的文件路径作为该解释器的参数，执行脚本，从而使得脚本文件的调用方式与普通的可执行文件类似。

在 `shebang` 行中使用 [`env`](https://man7.org/linux/man-pages/man1/env.1.html) 命令是一种好的实践，它会利用环境变量中的程序来解析该脚本，这样就提高来您的脚本的可移植性。`env` 会利用我们第一节讲座中介绍过的`PATH` 环境变量来进行定位。

例如，使用了`env`的 shebang 看上去时这样的`#!/usr/bin/env python`。

- PS1 的自定义

[linux 修改 PS1，自定义命令提示符样式 - 自我更新 - 博客园 (cnblogs.com)](https://www.cnblogs.com/liu-shijun/p/11075314.html)

## Shell Script

- 单引号：所见即所得；双引号或者没有引号：会先解析变量；

  [Shell 双引号和单引号的区别_shell 中单引号和双引号的区别_恋喵大鲤鱼的博客-CSDN 博客](https://blog.csdn.net/K346K346/article/details/86752313)

- 命令串太长 \反斜杠 + enter

- echo 显示变量

  `echo $+变量名`

  等号左右不能有空格、开头不能是数字、**用\转义特殊字符**

  unset 删除变量

- env = environment 列出环境变量

  - HOME

  - SHELL

  - MAIL

  - PATH

  - LANG 语系数据

  - RANDOM 随机数

    - declare Set variable values and attributes.

      生成 0-9 的随机数

      `declare -i number=$RANMDOM*10/32768 ; echo $number`

  - $ 本 SHELL 的线程代号 即 PID

    ex  echo $$ 即输出 proceesID

  - ？上一个执行命令回传值

  - PWD 当前工作目录

- export 自定义变量变成环境变量

  ​ 子进程继承父进程的环境变量

### 括号问题

- 双引号

不想让空格把变量分割开，有空格的变量视为一个变量

`"$arg"`

- 大括号

大括号 `{}` 的作用是限定大括号里面的字符串是一个整体，不会跟相邻的字符组合成其他含义。

```bash
$ var="Say"
$ echo $var Hello
Say Hello
$ echo $varHello

$ echo ${var}Hello
SayHello
$ echo "$var"Hello
SayHello
```

#### 环境变量

![image](C:/Users/Philfan/AppData/Roaming/Typora/typora-user-images/image-20221120191523907.png)

0 表示正常执行，非零值表示有错误发生

- `$0` - 脚本名

- `$1` 到 `$9` - 脚本的参数。 `$1` 是第一个参数，依此类推。

- `$@` - 所有参数

- `$#` - 参数个数

- `$?` - 前一个命令的返回值

- `$$` - 当前脚本的进程识别码

- `!!` - 完整的上一条命令，包括参数。常见应用：当你因为权限不足执行命令失败时，可以使用 `sudo !!`再尝试一次。

- `$_` - 上一条命令的最后一个参数。如果你正在使用的是交互式 shell，你可以通过按下 `Esc` 之后键入 . 来获取这个值。
  (下划线) 表示的是打印上一个输入参数行，当这个命令在开头时，打印输出文档的绝对路径名。

- $- 是 set 命令的 –h 和 –B 的参数，表示使用内置的 set 命令扩展解释之后的参数行，
     具体分别表示为，记住工作路径，和允许使用 ! 历史扩展，详细请参阅 set 命令。

#### 变量读取、数组、声明

- read + 变量 -p 接提示符 -t 接时间

- declare / typeset       声明变量类型

  -a 定义为数组   -i 定义为 integer -x 与 export 一样

  **bash**中数值运算仅支持整数

  ```bash
  read -p "输入网站名：" website
  echo "你输入的网站名是 $website" 
  exit 0
  ```

- 数组定义   ==没有逗号==

  ```bash
  a1=(0 1 1)
  echo=${a1[1]}
  //*和@获取所有元素
  echo "数组的元素为：${my_array[*]}"
  echo "数组的元素为：${my_array[@]}"
  echo ${#array[1]} // 显示长度
  ```

  ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__Linux__assets__02-Shell.assets__image-20221123204440835.webp)

  关联数组

  ```bash
  declare -A array_name
  ```

- 变量删除、替代、替换

  - 删除

    从前到后删除符合选项的最短字符

    从前到后删除符合选项的最长字符

    `echo ${path#/*/kerberos/bin:}`

    %从后向前删除

    %%从后向前删除最长项数 z

  - 替换

    **/旧/新  第一个**

    **//旧/新   全部**

- 变量别名 alias

  `alias lm='ls -l | more`

  `alias rm='rm -i'`

  ## Shell 运算符

- bc 数学运算

### 短路运算

|| or：第一个没成功，执行第二个

&&

；：不管是否成功都会执行

```bash
false || echo "Oops, fail"
# Oops, fail

true || echo "Will not be printed"
#

true && echo "Things went well"
# Things went well

false && echo "Will not be printed"
#

false ; echo "This will always run"
# This will always run
```

- eval

    二次扫描

    可以实现指针效果

    ``` bash
    x=50
    a=x
    eval echo $$a
    ```

- set 命令

    ```bash
    set $(date)
    echo $1 $3
    
    set -- $(ls -l $demo)
    #--用来让后面的 - 不被识别成为 set 的参数
    ```

    把 set 后的命令转换为$变量

    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__Linux__assets__02-Shell.assets__image-20221207201248626.webp)

  expr

  用反引号
