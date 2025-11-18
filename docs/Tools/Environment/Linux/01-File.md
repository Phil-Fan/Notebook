# 文件、目录、磁盘格式

## 文件权限与目录

~ home directory

- ls  -list\

  [技术|Linux 中的 15 个基本‘ls’命令示例](https://linux.cn/article-5109-1.html)

  ```bash
  ls - d #列出目录本身  
  
  ls -a(all)
  -l (long)   
  -i(inode 号)  
  -d(属性) 
  
  ls -h
  -d 列出目录本身
  -R 目录树
  -F
  
  所有文件（包括隐藏文件） ：-a
  文件打印以人类可以理解的格式输出 : -h
  文件以最近访问顺序排序：-t
  以彩色文本显示输出结果：--color=auto
  ```

- mkdir = make directories

  mkdir -p 递归创建 没有这个目录就创建一个目录

- rmdir = remove directory

- cd = change directory

  cd - cd to the directory you previously in

- fasd: 快速跳转

```bash
alias a='fasd -a'        # any
alias s='fasd -si'       # show / search / select
alias d='fasd -d'        # directory
alias f='fasd -f'        # file
alias sd='fasd -sid'     # interactive directory selection
alias sf='fasd -sif'     # interactive file selection
alias z='fasd_cd -d'     # cd, same functionality as j in autojump
alias zz='fasd_cd -d -i' # cd with interactive selection

a foo 列出最近操作的路径匹配'foo'的文件与目录
f foo 列出最近操作的路径匹配'foo'的文件
d foo 列出最近操作的路径匹配'foo'的目录
s foo 列出最近操作的路径匹配'foo'的文件与目录，并可以通过序号选择
sf foo 列出最近操作的路径匹配'foo'的文件，并可以通过序号选择
sd foo 列出最近操作的路径匹配'foo'的目录，并可以通过序号选择
z foo cd到最近操作的匹配'foo'并且得分最高的目录
zz foo 列出最近操作的路径匹配'foo'的目录，通过序号选择，然后cd进目录
```

- pwd = print working directory

- cp = copy       cp -rp -r -p 保留属性

- mv = move

- rm = remove

  rm -i 先询问再删除//询问是否删除

  rm - rf 文件或目录

  -r 目录（**非常危险**）

- echo 打印

### 文件夹导航

- fasd

 基于 [*frecency*](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/Places/Frecency_algorithm)对文件和文件排序，也就是说它会同时针对频率（*frequency*）和时效（*recency*）进行排序。默认情况下，`fasd`使用命令 `z` 帮助我们快速切换到最常访问的目录。

例如，如果您经常访问`/home/user/files/cool_project` 目录，那么可以直接使用 `z cool` 跳转到该目录

- autojump

- tree

- nnn

## 文件与目录管理

### ln 链接

[硬链接和符号链接的区别 - LubinLew - 博客园 (cnblogs.com)](https://www.cnblogs.com/LubinLew/p/LinuxFileLink.html)

- 硬链接

不可跨越文件系统

只有超级用户才可以建立目录硬链接

占用空间极少

- 符号链接

文件内容作为路径名去访问真正的共享文件

可跨越文件系统

占有少量空间

```linux
[root@localhost ~]# touch cangls
[root@localhost ~]# ln /root/cangls /tmp
\#建立硬链接文件，目标文件没有写文件名，会和原名一致
\#也就是/tmp/cangls 是硬链接文件
```

- -s：建立软链接文件。如果不加 "-s" 选项，则建立硬链接文件；

  符号链接：inode 号不同

- -f：强制。如果目标文件已经存在，则删除目标文件后再建立链接文件

### 查找文件

- which 查询脚本文件 -a 全列出来

- find

  - atime = access time
  - ctime = status time  
  - mtime = modification time

  【-mtime n 几天之前的“一天之内】【-mtime +n n 天之前】【-mtime -n n 天之内】

  ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__Linux__assets__01-File.assets__0ca63c3736084f4f9d35a949f33413d0.webp)

  [使用 find 命令在 Linux 上查找文件和目录](https://linux.cn/article-14071-1.html)

  ```bash
  # 查找所有名称为 src 的文件夹
  find . -name src -type d
  
  # 查找所有文件夹路径中包含 test 的 python 文件
  find . -path '**/test/*.py' -type f
  #  ** 表示所有
  
  # 查找前一天修改的所有文件
  find . -mtime -1
  
  # 查找所有大小在 500k 至 10M 的 tar.gz 文件
  find . -size +500k -size -10M -name '*.tar.gz'
  
  # 删除全部扩展名为.tmp 的文件
  find . -name '*.tmp' -exec rm {} \;
  
  # 查找全部的 PNG 文件并将其转换为 JPG
  find . -name '*.png' -exec convert {} {}.jpg \;
  
  # 文件名中有空格
  -print 打印 find 命令 结果集，默认用换行符分割。而且 -print 是默认省略的。
  -print0 打印 find 命令 结果集，用 NULL 字符 ('\0') 分割，而不是换行符。 
  
  # 编写一个命令或脚本递归的查找文件夹中最近使用的文件。更通用的做法，你可以按照最近的使用时间列出文件吗？
  find . -type f -print0 | xargs -0 ls -lt | head -1
  
  当文件数量较多时，上面的解答会得出错误结果，解决办法是增加 -mmin 条件，先将最近修改的文件进行初步筛选再交给 ls 进行排序显示
  find . -type f -mmin -60 -print0 | xargs -0 ls -lt | head -10
  ```

  find+exec

  ```bash
  # ls -l 命令放在 find 命令的-exec 选项中 
  find . -type f -exec ls -l {} \;
  
  # 在目录中查找更改时间在 n 日以前的文件并删除它们
  find . -type f -mtime +14 -exec rm {} \;
  在 shell 中用任何方式删除文件之前，应当先查看相应的文件，一定要小心！当使用诸如 mv 或 rm 命令时，可以使用-exec 选项的安全模式。它将在对每个匹配到的文件进行操作之前提示你。 
  
  #3 在目录中查找更改时间在 n 日以前的文件并删除它们，删除之前先给出提示
  find . -name "*.log" -mtime +5 -ok rm {} \;
  在上面的例子中，find 命令在当前目录中查找所有文件名以.log 结尾、更改时间在 5 日以上的文件，并删除它们，只不过在删除之前先给出提示。按 y 键删除文件，按 n 键不删除。 
  
  #4 -exec 中使用 grep 命令
  find /etc -name "passwd*" -exec grep "root" {} \;
  任何形式的命令都可以在-exec 选项中使用。在上面的例子中我们使用 grep 命令。find 命令首先匹配所有文件名为“passwd*”的文件，例如 passwd、passwd.old、passwd.bak，然后执行 grep 命令看看在这些文件中是否存在一个 root 用户。
  
  #5 查找文件移动到指定目录
  find . -name "*.log" -exec mv {} .. \;
  
  #6 用 exec 选项执行 cp 命令  
  find . -name "*.log" -exec cp {} test3 \;
  ```

- locate

  -i 大小写

### 查找 shell 命令

- history

```BASH
history N #数字 ： 最近___条命令
history -c #删除历史
history -a #保存
history -r #读取
history !n #执行历史中的第n条命令
history !+ #命令 执行历史中这条命令开头的命令

!! #重新执行上一条命令
!N  #重新执行第N条命令。比如 !3
!-N #重新执行倒数第N条命令。!-3
!string  #重新执行以字符串打头的命令。 比如 !vim
!?string?  #重新执行包含字符串的命令。 比如 !?test.cpp?
!?string?%  #替换为： 最近包含这个字符串的命令的参数。比如：   vim !?test.cpp?%
!$   #替换为：上一条命令的最后一个参数。比如 vim !$
!!string  #在上一条命令的后面追加 string ，并执行。
!Nstring  #在第N条指令后面追加string，并执行。
^old^new^  #对上一条指令进行替换
```

```bash
history N | grep find

```

## 磁盘与文件系统

## 压缩与打包
