# 使用者管理

## 用户权限

- UID

  - 500~65535  普通用户
  - 0 超级用户

- PID process identification

- useradd

- 文件分类
    p 表示命名管道文件

      d 表示目录文件

      l 表示符号连接文件

      - 表示普通文件

      s 表示 socket 文件

      c 表示字符设备文件

      b 表示块设备文件

- 特殊访问位置

  [linux 一文带你彻底搞懂特殊权限位 suid，sgid，sticky_大雷编程的博客-CSDN 博客_suid 位](https://blog.csdn.net/csdn_leidada/article/details/122223958)

  通过有效用户标识实现

  SUID :  set-user-ID

  ​   拥有用户的权限

  ​   chmod u+s XXX

  SGID : set-group-ID

  ​   拥有组权限

  ​   chmod g+s XXX

  ​   chmod 2777 XXX

  uname 可显示电脑以及操作系统的相关信息。

  ```bash
  -a 或--all  显示全部的信息。
  -m 或--machine  显示电脑类型。
  -n 或--nodename  显示在网络上的主机名称。
  -r 或--release  显示操作系统的发行编号。
  -s 或--sysname  显示操作系统名称。
  -v  显示操作系统的版本。
  --help  显示帮助。
  --version  显示版本信息
  ```

  sticky BIt: 只有所有者可以删除或者重命名、在共享文档中使用

  ​   可以修改、不能删除

  ​   chmod 1755 XXX

  ​   chmod +t XXX

  文件和目录操作权限不同：

  对于目录来说，read 权限是读取 list，write 是更改文件名字、移动、删除等等

  execute 权限是 search 权限，也就是是否可以 access

- 用户 用户组

  user = u = 用户

  group = g = 用户组

  others = o = 其他人

  r = read   w = write    x = execute 可执行

  没有则用‘-’替代

  顺序 u -> g -> o

- chgrp = change group

- chown = change owner

- chmod =

  r = 4 , w  = 2 , x = 1

  rwx = 7, rw = 6

- chattr

  `chattr +i XXX`防止删除

## 磁盘配额

## 例行工作

## 程序管理与进程

**信号（Signal）**：信号是在软件层次上对中断机制的一种模拟，通过给一个进程发送信号，执行相应的处理函数。

|      |         |      |                                  |
| ---- | ------- | ---- | -------------------------------- |
| 2    | SIGINT  | 终止 | 键盘输入中断命令，一般是 CTRL+C   |
| 9    | SIGKILL | 终止 | 立即停止进程，不能捕获，不能忽略 |
| 20   | SIGSTP  | 停止 | 停止进程，一般是 CTRL+Z           |

- type 类似于 which 找到执行文件

   显示类型

   **内部命令、外部命令**：内部命令不创建进程、外部命令创建进程

   [Linux shell 内部命令和外部命令](https://blog.csdn.net/coding_dong/article/details/103576071)

- ps 查看进程属性

   ps -a

- 前台后台

   加**&**变成后台：大量计算、查找

   fg  = foreground 后台转到前台

   ​ bg = background  + "%作业号"

- 作业、作业号

   查看作业 jobs

   定时执行 at

   分号：顺序进行
   与号：并发执行

- 终止进程

   <ctrl+C>

   kill -9（强制）

   -15 +进程号

- 睡眠 sleep n

- &&成功则运行

   || 失败才运行

### 管道

管道是进程之间的通讯机制

经过几道手续之后再输出

#### tee

中间结果保存

#### cut

-d 后面接分割字符 -f 取出第几段的意思

-c 以字符的单位去除

[【Linux 篇】cut 命令详解_linux cut_傻啦猫@_@的博客-CSDN 博客](https://blog.csdn.net/weixin_45842494/article/details/124679008)

#### xargs

命令行可以从参数或标准输入接受输入。在用管道连接命令时，我们将标准输出和标准输入连接起来，但是有些命令，例如`tar` 则需要从参数接受输入。

xargs 默认的命令是 echo，这意味着通过管道传递给 xargs 的输入将会包含换行和空白，不过通过 xargs 的处理，换行和空白将被空格取代。

```bash
# 实例1
find /sbin -perm +700 |ls -l       #这个命令是错误的
find /sbin -perm +700 |xargs ls -l   #这样才是正确的

# -d 选项可以自定义一个定界符：
$ echo "nameXnameXnameXname" | xargs -dX
name name name name

# 结合 -n 选项使用：
$ echo "nameXnameXnameXname" | xargs -dX -n2
name name
name name

# xargs 结合 find 使用
用 rm 删除太多的文件时候，可能得到一个错误信息：/bin/rm Argument list too long. 用 xargs 去避免这个问题：
$ find . -type f -name "*.log" -print0 | xargs -0 rm -f

# 查找所有的 jpg 文件，并且压缩它们
find . -type f -name "*.jpg" -print | xargs tar -czvf images.tar.gz

# 很多你希望下载的 URL
$ cat url-list.txt | xargs wget -c

# find -print0 | xargs -0
分析：第一个 -print0 指定结果集分隔为 null，第二个 -0 指定 xargs 分隔为 null。 
   find -print0表示在find的每一个结果之后加一个NULL字符，而不是默认加一个换行符。find的默认在每一个结果后加一个'\n'，所以输出结果是一行一行的。当使用了-print0之后，就变成一行了。
   然后xargs -0表示xargs用NULL来作为分隔符。这样前后搭配就不会出现空格和换行符的错误了。选择NULL做分隔符，是因为一般编程语言把NULL作为字符串结束的标志，所以文件名不可能以NULL结尾，这样确保万无一失。
```

### 重定向

- 输出

  stdout  >>累加 >覆盖

  stderr  2>> 累加 2>覆盖

  输出到同一个文件 2>&1

- 输入

  stdin <

  stdin <<结束输入  ex: <<"eof"

## 系统服务

## 日志文件
