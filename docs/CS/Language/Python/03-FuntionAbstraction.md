# 函数 `Function`

python 的函数是一种数据类型

```python title="注释的写法 docstring"
def pressure(v, t, n):
  """计算理想气体的压力，单位为帕斯卡

  使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

  v -- 气体体积，单位为立方米
  t -- 绝对温度，单位为开尔文
  n -- 气体粒子
  """
  k = 1.38e-23  # 玻尔兹曼常数
  return n * k * t / v
```

使用`help(pressure)`查看注释

## 声明  `Defination`

- 函数的命名规范

built-in name

bound name

- nested defination 嵌套定义

注意定义域问题：

parent frame : **when it is defined**

local frame : **when it is called**

```python
def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)
```

## 调用 `Call`

when you call a function, it **creates** a new frame

- 再计算所有参数后，才可以执行这个函数

  ex1：函数才可以被调用`g(f(2))`,`f()`首先被调用，计算出`f(2)`之后，`g()`才被调用

  ex2：statement 和 function 的区别

```python
def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    return if_function(cond(), true_func(), false_func())
```

- 在函数开始执行后，同一个变量都指向同一个`frame`当中的值，不会出现一会局部变量，一会全局变量的情况

```python
x = 2
def f():
 print(x)
 x = 3
#UnboundLocalError: local varibale x referenced before assignment
```

- 如果要将函数作为一个参数，那么需要格外注意是传入的是这个函数（不带括号），还是这个函数的返回值（带括号）

- 调用函数时，传递参数的值有四种方式：

  - 位置参数
  - 关键字参数，如`end=','`
  - 默认值参数
  - 可变数量参数

- 关键字参数

  - 为了避免位置参数带来的混乱，调⽤参数时可以指定对应参数的名字，这是关键字参数，它甚⾄可以采⽤与函数定义不同的顺序调⽤

- 位置参数和关键字参数混合

- 默认值参数（缺省 sheng）

  - 默认参数值在函数对象被创建时计算

    ```py
    def init( arg, result=[]):##实现了持续存储
        result.append(arg)
        print( result)
    init('a')
    init('b')
    ```

- 不定长数目参数 -- 形参前面加上星号

  - 当函数参数数⽬不确定时，星号将⼀组可变数量的位置参数集合成参数值的**元组**

  - print()

    ```py
    print(*object,sep=" ",end="\n",file=sys.stdout) 
    ```

    - `object`：输出参数
    - `sep=" "`：输出分割符
    - `end="\n"`：输出函数结束换⾏
    - `file=sys.stdout`：输出到屏幕

- 实参前面加上星号 -> 容器拆包

  - `*`表示将序列拆成⼀个个单独的实参，
  - ⽽`**`则表示将字典拆成⼀个个单独的带变量名的实参

- 收集参数到字典中---`**`

  ```py
  def countnum(a,**d): #计算参数个数
      print(d)
      print(len(d)+1)
  countnum(3,x1=9,x2=1,x3=6,x4=89)
  ```

- 仅限关键字参数

  - 只能传入关键字参数。仅限关键字参数不可缺省（除非有默认值），且只能强制性通过关键字传参

  - 可变参数后面的关键字参数都是仅限关键字参数（一旦使用了可变参数，之后的参数都必须通过关键字传递）

  - 也可以用单星号"*"表示不接受任何可变参数，它可以作为普通参数的结束标志

- 当实参是不可变对象时，形参值改变不会影响实参！

- 当实参是可变对象时，形参值改变可能会影响实参！

## 返回 `Return`

- 函数⽤ return 语句返回值
- return 后⾯的表达式的值就成为这次函数调⽤的返回值
  - **如函数没有⽤ return 语句返回，这时函数返回的值为`None`**；
  - 如果 return 后⾯没有表达式，调⽤的返回值也为`None`
- `None`是 Python 中⼀个特殊的值，虽然它不表示任何数据，但仍然具有重要的作⽤

```python
# None is not displayed by the interpreter as the value of an expreesion

>>> print(print(1),print(2))
1
2
None None
# 注意 Print 的返回值是 None

>>> None + 7 
TypeError
```

- 返回的多个值和接收多个参数是一样的，以**元组**的形式打包传递

```py
def f(a,b):
    return a//b, a%b
x,y=f(10,3)
print(x,y)##单个

x=f(10,3)
print(x)##元组
```

## Higher-Order Functions

functions that manipulate functions

```python
def improve(update, close , guess=1):
  while not close(guess):
    guess = update(guess)
  return guess
```

有趣的例子
注意 parent frame 和 返回类型

```python
def print_sums(n):
  print(n)
  def f(k):
    return print_sums(n+k)
  return f

g = print_sums(1)
h = g(3)
w = h(5)
```

### `map()`- apply to all

- `map(f, sq)`

  函数将函数`f`作用到可枚举量`sq`的每个元素上去，并返回结果组成的`map`对象，`map`对象本身是一个可枚举量

```py
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))) 
# 使⽤ lambda 匿名函数
print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
# 提供了两个列表，对相同位置的列表数据进⾏相加
```

### `filter()` - keep if

- `filter(f, sq)` 函数的作用是对于`sq`的每个元素`s`，返回所有`f(s)`为`True` 的`s`组成的`filter`对象，`filter`对象对象本身是一个可枚举量

```py
def is_even(x):
    return x % 2 == 0

filter(is_even, range(5))
```

- 把`map()`和`filter()`合起来

```py
map(square, filter(is_even, range(5)))
```

### `reduce()` - 所有元素二元操作

- `reduce(f, sq)` 函数接受一个二元操作函数 `f(x,y)`，并对于序列 `sq` 做累进计算
- 这里`f(x,y)`的`x`是累计值，而`y`是当前值，即序列中的一个元素

```python title="reduce 函数实现"
def reduce(function, sequence, initial=_initial_missing):
    """
    reduce(function, iterable[, initial], /) -> value

    Apply a function of two arguments cumulatively to the items of an iterable, from left to right.

    This effectively reduces the iterable to a single value.  If initial is present,
    it is placed before the items of the iterable in the calculation, and serves as
    a default when the iterable is empty.

    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    calculates ((((1 + 2) + 3) + 4) + 5).
    """

    it = iter(sequence)

    if initial is _initial_missing:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError(
                "reduce() of empty iterable with no initial value") from None
    else:
        value = initial

    for element in it:
        value = function(value, element)

    return value
```

例子

```python
from functools import reduce
def my_add(x, y):
    return x + y
reduce(my_add, [1,2,3,4,5])

##
from functools import reduce
s1 = reduce(lambda x, y: x+y, map(lambda x: x**2, range(1,10)))
print(s1)
```

```python title="make_repeater"
from functools import reduce

def make_repeater(f, n):
    """Returns the function that computes the nth application of f."""
    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    return lambda x: reduce(lambda acc, _: f(acc), range(n), x)
```

### `sorted()`

- `sorted()`函数对字符串，列表，元组，字典等对象进行排序操作
- 同样是对列表操作，`list`的`sort()`⽅法是对已经存在的列表进⾏操作
- ⽽内建函数`sorted()`返回的是⼀个新的`list`，原来的`list`不会被修改

sorted 函数语法

```python
sorted(iterable ,key=None, reverse=False)
```

- `iterable` -- 序列，如字符串，列表，元组等
- `key` -- ⽤来进⾏⽐较的函数，这个函数只有⼀个参数，参数的值就是取⾃于可迭代对象中的一个元素，函数返回在这个元素上的一个计算结果来作排序，通常当元素本身是一个复合类型（如列表、字典）时，取其中的某个元素
- reverse-- 排序规则
  - `reverse = True` 降序
  - `reverse = False` 升序（默认）

### currying  柯理化

​  [函数式编程--柯理化（Currying） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/355859667)

​  柯里化（Currying）是一种处理多元函数的方法。它产生一系列连锁函数，其中每个函数固定部分参数，并返回一个新函数，用于传回其它剩余参数的功能

常见场景：传入不定量参数，给出需要剩余参数的函数

```python
def lambda_curry2(func):
"""
    Returns a Curried version of a two-argument function FUNC.
"""
    return lambda x:lambda y: func(x,y)

def curry2(f):
    """Return a curried version of given weo-argument function"""
    def g(x):
        def h(y):
            return f(x,y)
        return h #注意这里不可以加括号
    return g
```

- 解决重复传参问题，提高函数适用性

柯理化 (currying) 应用很广泛也很常见。比如，批量发送双 11 活动邮件，通常我们这样做

```js
function sendEmail(from, content, to){
    console.log(`${from} send email to ${to}, content is ${content}`)
}

sendEmail('xx 公司', '双 11 优惠折上 5 折', 'zhangsan@xx.com')
sendEmail('xx 公司', '双 11 优惠折上 5 折', 'lisi@xx.com')
sendEmail('xx 公司', '双 11 优惠折上 6 折', 'wangwu@xx.com')
sendEmail('xx 公司', '双 11 优惠折上 6 折', 'maliu@xx.com')

// ...
```

邮件发送方是固定的，邮件内容是相对固定的，唯一不同的是邮件的接受者。这正符合柯理化 (currying) 固定部分参数，并返回接受剩余参数新函数的规则。柯理化创建两个临时性的、适用性更强的函数 sendEmailToS5 和 sendEmailToS6，向目标群体，发送指定类型的邮件。

```js
var sendEmailContent = currying(sendEmail)('xx 公司')
var sendEmailToS5 = sendEmailContent('双 11 优惠折上 5 折')
var sendEmailToS5 = sendEmailContent('双 11 优惠折上 6 折')

// 打五折的群组
sendEmailToS5('zhangsan@xx.com')
sendEmailToS5('lisi@xx.com')

// ...

// 打六折的群组
sendEmailToS6('wangwu@xx.com')
sendEmailToS6('maliu@xx.com')
```

## 匿名函数--`lambda`表达式

- lambda 的⼀般形式是关键字`lambda`后⾯跟⼀个或多个参数，紧跟⼀个冒号，后⾯是⼀个表达式
- 作为表达式，lambda 返回⼀个值，也可以返回另一个`lambda`表达式
- lambda ⽤来编写简单的函数，⽽`def`⽤来处理更强⼤的任务的函数。

```python
# nonnested lambda
lambda n, i: count_factors(i)
count_factors(n,i)

# nested lambda 
g = lambda x: lambda y : y+1
eight = g(2)(7)

>>> b = lambda x: lambda: x
>>> c = b(88)
>>> c
<function <lambda> at 0x...>




```

- 匿名函数实现递归

f(f) 就是递归调用的关键，它将相同的函数 f 传递给自身，实现了递归调用。

```python
(lambda f: lambda n: 1 if n == 1 else mul(n,f(f)(n-1)))(lambda f: lambda n: 1 if n == 1 else mul(n,f(f)(n-1)))
```

- 作为`key`参数

```python
leaders.sort(key=lambda x: len(x))
```

### 与高阶函数配合使用

需要两个参数，第一个是一个处理函数，第二个是一个序列 (list,tuple,dict)
 **map()**
 将序列中的元素通过处理函数处理后返回一个新的列表
 **filter()**
 将序列中的元素通过函数过滤后返回一个新的列表
 **reduce()**
 将序列中的元素通过一个二元函数处理返回一个结果

```python
li = [1,2,3,4,5]
# 序列中的每个元素加 1 
map(lambda x: x+1, li) # [2,3,4,5,6] 
# 返回序列中的偶数
filter(lambda x: x % 2 == 0, li) # [2, 4] 
# 返回所有元素相乘的结果 
reduce(lambda x, y: x * y, li) # 1*2*3*4*5 = 120 
```

## 闭包

1. 函数嵌套：闭包通常是在一个函数内部定义另一个函数。
2. 内部函数引用外部函数的变量：在内部函数中引用了外部函数的变量，即使外部函数已经执行完毕，这些变量的引用仍然被保留。
3. 保持状态：由于闭包可以持续引用外部函数的变量，因此它可以保持状态，并在多次调用时共享这些状态。

```python
def announce_lead_changes(prev_leader=None):
    """输出两玩家分数差"""
    def say1(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != prev_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say1
```

在`say1`函数内部，它调用了`announce_lead_changes(leader)`，这相当于又创建了一个新的`say1`函数，并且这个新的函数也引用了当前`say1`函数的`leader`变量。这样就形成了一个递归结构，多个嵌套的`say1`函数通过引用环境链接在一起。

先返回`announce_lead_changes`再返回`say1`。这是因为外部函数`announce_lead_changes`返回的是内部函数`say1`的引用。如果直接返回`say1`，那么每次调用`announce_lead_changes`都会创建一个新的`say1`函数，它们之间不会保持共享的状态。而通过先返回`announce_lead_changes`，外部函数将在递归调用时保持状态，并始终引用相同的`say1`函数。

这种方式创建了一个闭包，使得在每次调用内部函数时都能够持续跟踪之前的状态。这样，`announce_lead_changes`函数的每次调用都返回一个新的闭包函数，这些闭包函数共享相同的代码逻辑，但各自保持着不同的状态，即各自引用的`prev_leader`变量值。

## 函数装饰器 `Decorators`

函数装饰器使用 `@` 符号和装饰器函数来标记要装饰的函数。

装饰器函数接受被装饰函数作为参数，并返回一个新的函数或可调用对象来替代原函数。

```python
def decorator_function(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator_function
def greet():
    print("Hello, World!")

#等价于
greet = decorator_function(greet)
```

```python title="计时器"
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def train_model(data):
    # 模拟训练过程
    time.sleep(2)
    print("Training completed")

train_model("dataset")  # 输出：Training completed 和 train_model took 2.0002 seconds
```

```python title="切换模式"
def set_eval_mode(func):
    def wrapper(model, *args, **kwargs):
        model.eval()  # 进入评估模式
        result = func(model, *args, **kwargs)
        model.train()  # 恢复训练模式
        return result
    return wrapper

@set_eval_mode
def evaluate_model(model, data):
    # 评估逻辑
    print("Evaluating model...")

model = ...  # 某个 PyTorch 模型
evaluate_model(model, test_data)  # 自动切换模式
```

```python title="自动重试"
import time
from functools import wraps

def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise RuntimeError(f"Failed after {max_retries} retries")
        return wrapper
    return decorator

@retry(max_retries=3, delay=1)
def fetch_data(url):
    # 模拟可能失败的 HTTP 请求
    if "fail" in url:
        raise ConnectionError("Failed to fetch data")
    return {"data": "..."}

fetch_data("https://example.com/data")  # 成功
fetch_data("https://example.com/fail")  # 重试 3 次后报错
```

## 常见函数

### `zip`函数

- `zip()`函数⽤于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表或迭代器

- 如果各个迭代器的元素个数不⼀致，则返回列表⻓度与最短的对象相同

- 参数说明：iterable -- ⼀个或多个序列返回值：* 返回元组列表

`zip()` 是 Python 中非常实用的内置函数，用于将多个可迭代对象（如列表、元组等）的元素按位置配对组合。以下是几个常见的使用案例：

```python title="并行遍历多个列表"
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 输出：
# Alice: 85
# Bob: 92
# Charlie: 78
```

```python title="将两个列表合并为字典"
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

```python title="转置二维矩阵"
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = list(zip(*matrix))
print(transposed)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

```python title="按最短列表截断"
long = [1, 2, 3, 4, 5]
short = ["a", "b", "c"]
result = list(zip(long, short))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

```python title="与 enumerate 结合使用"
names = ["Alice", "Bob", "Charlie"]
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i}: {name} -> {score}")
# 输出：
# 0: Alice -> 85
# 1: Bob -> 92
# 2: Charlie -> 78
```

```python title="解压（Unzip）数据"
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(letters)  # ('a', 'b', 'c')
print(numbers)  # (1, 2, 3)
```

```python title="批量计算（如元素级运算）"
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

sums = [x + y for x, y in zip(vector1, vector2)]
print(sums)  # [5, 7, 9]
```

```python title="处理不等长列表时填充默认值"
from itertools import zip_longest

long = [1, 2, 3, 4]
short = ["a", "b"]

result = list(zip_longest(long, short, fillvalue="NULL"))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'NULL'), (4, 'NULL')]
```

### `eval()`和`exec()`函数

- Python 是⼀种动态语⾔，它包含很多含义
- Python 变量类型，操作的合法性检查都在动态运⾏中检查；运算的代码需要到运⾏时才能动态确定；程序结构也可以动态变化，容许动态加载新模块等。这两个函数就体现了这个特点
- `eval()`是计算表达式，返回表达式的值
- `exec()`可运⾏ Python 的代码段，返回代码段运⾏的结果

```py
exec('print("hello world")')
while True:
    line = input()
    if 'bye' in line:
        break
    exec(line)
```

## 递归注意点

```python title="interleaved_sum"
def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    def inter(k,state):
        if k > n:
            return 0
        elif state == True:
            return odd_func(k) + inter(k+1,not state)
        else:
            return even_func(k) + inter(k+1,not state)
    return inter(1,True)
```

This question demonstrates that it's possible to write recursive functions without assigning them a name in the global frame.

```python title="make_anonymous_factorial"
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda x: f(f,x))(lambda f,x: 1 if x == 1 else mul(x,f(f,sub(x,1))))
```

Python 中，lambda 函数不能自引用，因为它没有名字，所以不能写成 lambda x: ... factorial(x-1)。

我们就要用一种技巧：把函数自身作为参数传进去，这样它就能"递归"了。

```python
return (lambda f: lambda x: f(f, x))(
           lambda f, x: 1 if x == 1 else mul(x, f(f, sub(x, 1)))
       )
```

第一层：构造递归环境

```python
(lambda f: lambda x: f(f, x))
```

这个是一个函数，它接受一个函数 f，并返回一个函数 lambda x: f(f, x)。它的作用是：把 f 自己传给自己，这样 f(f, x) 就能模拟递归。

第二层：实际的阶乘逻辑

```python
lambda f, x: 1 if x == 1 else mul(x, f(f, sub(x, 1)))
```

这个函数接受两个参数：

- `f`：就是“自己”
- `x`：就是要计算阶乘的数字
