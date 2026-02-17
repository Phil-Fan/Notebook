# Statement

## assignment 赋值语句

1.evaluate all expressions to the right of `=` from left to right

2.bind all names to the left of `=` to the resulting values in the current frame

```python
#attention the unique syntax of Python
a,b = b+a,a
```

## if

```python
if x<=2760:
   y = 0.538 * x
elif x<=4800:
   y = 0.588 * x
else:
   y = 0.838 * x
```

- 在`if`之后的行，如果保持相同的缩进，就是这个`if`的一部分，是当表达式的结果是`True`，即关系成立的时候，要执行的内容

## boolean operators

优先级规则 not>and>or

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Language__Python__assets__02-Statement.assets__a26c8031eeb36116320ad0f23883c8c.webp)

## while

冒号，True 大写

```python
while True:
    x = int(input())
    if x == -1:
        break
    cnt += 1
    s += x
```

## for

python 中有`for - else` 结构，不要使用

所谓 else 指的是循环正常结束后要执行的代码，

即如果是 bresk 终止循环的情况。else 下方缩进的代码将不执行。

```py
x = int(input())
for k in range(2,x):
  if x%k==0:
    print(f'{x} is compsite')
    break
else:
  print(f'{x} is prime')
```

## 异常

```py
try:
     语句块1
except 异常类型1:
     语句块2
except 异常类型2:
     语句块3 
…
except 异常类型N:
     语句块N+1
except:
     语句块N+2
else:
     语句块N+3
finally:
    语句块N+4  
    
except Exception as n: ##万能捕捉器
```

- 在`except 异常类型`子句中找对应的异常类型，如果找到的话，执行后面的语句块
- 如果找不到，则执行`except`后面的语句块 N+2
- 如果程序正常执行没有发生异常，则继续执行`else`后的语句块 N+3
- 无论异常是否发生，最后都执行`finally`后面语句块 N+4

- raise 抛出异常

```py
raise Exception
raise Exception('load overload')
```

### 标准异常

| 异常名称 | 描述 |
| ---------------------- | --------------------------- |
| SystemExit | 解释器请求退出 |
| **FloatingPointError** | 浮点计算错误 |
| OverflowError | 数值运算超出最大限制 |
| **ZeroDivisionError** | 除 (或取模) 零 (所有数据类型) |
| KeyboardInterrupt | 用户中断执行 (通常是输入^C) |
| ImportError | 导入模块/对象失败 |
| **IndexError** | 序列中没有此索引 (index) |
| RuntimeError | 一般的运行时错误 |
| AttributeError | 对象没有这个属性 |
| IOError | 输入/输出操作失败 |
| OSError | 操作系统错误 |
| **KeyError** | 映射中没有这个键 |
| **TypeError** | 对类型无效的操作 |
| ValueError | 传入无效的参数 |

```py
##一次捕捉多个异常
try:
    x,y = map(int, input('输入两个整数：').split())
    print(x/y)
except (ZeroDivisionError, TypeError, NameError):
    print('输入错误')
```

### 异常变量

- 有时需要除了异常类型以外其他的异常细节：

```py
except Exception as name
```

### 再抛异常

- 如果需要在`except`子句中再次抛出刚捕捉到的异常：

```py
def calc(expr):
    try:
        return eval(expr)
    except ZeroDivisionError:
        print('divided by zero is illegal!')
        raise
```

### 自定义异常

- 根据自己的目的可以自己定义异常类型
- 异常类需要从`Exception`类继承

```py
class AgeOutofRange(Exception):
    pass
```

## Testing

### 断言

- 通常写在本文件或者同文件夹下的`_test.py`
- 函数是写出来给别的程序员用的
- 检查函数接口的数据错误
- 函数入口应该对传入的参数值做检查
- `assert <条件>, <失败提示文字>`

```py
def divide(a, b):
    assert b!=0, 'Divided by zero'
    return a/b
```

### Doctest

placing simple tests directly in docstring of a function

```py
def add(a, b):
    """
    返回两个数的和。

    示例：
    >>> add(2, 3)
    5
    >>> add(-1, 5)
    4
    """
    return a + b
```

```py
import doctest

if __name__ == '__main__':
    doctest.testmod()
```

```python
from doctest import run_docstring_examples
run_docstring_examples(sum_naturals, globals(), True)
```

```shell
python3 -m doctest -v <source_file>
```

Doctest 的优点是它与文档紧密结合，测试用例直接嵌入在文档字符串中，使得测试更加直观和易于维护。它还可以作为文档的一部分，提供实例和用法示例。

然而，Doctest 适用于简单的测试场景，对于复杂的测试需求，如测试边界条件、异常处理等，通常需要使用其他测试框架，如 `unittest` 或 `pytest`。
