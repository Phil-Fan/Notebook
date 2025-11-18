# 表达式 `Expression`

- 幂次`**`
- 整数除法 $a//b \equiv \lfloor a/b \rfloor$

- 两种特殊的赋值：

  - 连续赋值：`a = b = 6`

  - 同步赋值：`a, b = 4, 5`

```python title="先计算出等号右边的值，再赋值给等号左边的变量"
a = 6
b = 7
a, b = b, a
```

## 输入输出

### 输入

```python title="常见的题目输入方式"
a,b = map(int, input().split())

list(map(int, input().split()))
#如果数据中有浮点数，直接用 int 会出错

a = tuple(int(item) for item in input().split())
```

```python title="多行 每行不确定"
lst = []
while True:
  m = list(map(int, input().split()))
  lst.extend(m)
  if -1 in m:
    lst.remove(-1)
    break
```

```python title="多行输入"
while True:
    try:
        a = input().split()
        print(int(a[0])+ int(a[1]))
    except:
        break
        
###多行输入 2
for line in sys.stdin:
    a = line.split()
print(int(a[0]) + int(a[1]))
```

### 输出

- `print("面积是：", area)`
- `print(a, end=', ')`
  
  - `print()`里的`end=`用来指定这次输出之后自动输出什么
  - 默认是`\n`，表示要换一行
- 如果要控制输出结果的小数点后的位数，就必须使用格式控制：
  - `print(f"面积是：{area:.2f}")`
  - 字符串前面的`f`表示格式字符串，其中的`{}`中的名字会被同名的变量的值所替换，`:`后面的内容表示输出的格式（可以省略）
  - `.2f`表示小数点后保留两位小数的浮点数
  
### format 格式化输出

```py
print({:[fill][align][width]}.format(data))

print("{:.3f}".format(s))
print(format(s, '.3f'))
```

`fill`：任意一个字符，比如 # 、 * 等，默认空格填充
`width`：字段宽度，如果未指定，那么字段宽度由内容确定，这种情况下的对齐选项没有意义
`data`：填充的数据
`align`：对齐方式

```python
a = [3,4,5]
print(*a,sep="->",end = '\n')  # 解包输出
print(f'{a:<4}')#左对齐
print(f'{1.8*shuzhi+32:.2f}')   # 格式字符串的{}里可以做表达式计算
```

## 中缀、前缀、后缀

- 前缀

  `!a`，`-b`

- 中缀

  `a+b`， `a*b`

- 后缀

## 进制转换

转化为 10 进制的数可用 int(待转数字，进制单位)
bin(m) 将整数 m 转化为二进制字符串
oct(m) 将整数 m 转化为八进制字符串
hex(m) 将整数 m 转化为十六进制字符串

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Language__Python__assets__01-Expression.assets__image-20230405210620174.webp)

- ==变量记得赋初值==

## 取整计算

```py
round( x,n )
## n -- 表示小数位数
当参数n不存在时，round()函数的输出为整数。
当参数n存在时，即使为0，round()函数的输出也会是一个浮点数。
此外，n的值可以是负数，表示在整数位部分四舍五入，但结果仍是浮点数。

print(round(123.45)) # 123
print(round(123.45,0)) # 123.0
print(round(123.45,-1)) # 120.0
```

```py
### 向下取整
int(a)

### 四舍五入
round(a)

###向上取整
math.ceil(a)

###分别取整数部分和小数部分
得到一个元组
math.modf(a)
```

- int()

```py
## int() 函数

a = 5.6
print(int(a)) #可以
print(int('5.6')) #不行
```

不过对于 int() 函数的使用，大家要注意一点：

只有符合整数规范的字符串类数据，才能被 int() 强制转换。

其次，文字形式，比如中文、火星文或者标点符号，不可以被 int() 函数强制转换。

最后，小数形式的字符串，由于 Python 的语法规则，也不能使用 int() 函数强制转换。

浮点形式的字符串，不能使用 int() 函数。但浮点数是可以被 int() 函数强制转换的。

注意：1.文字类和小数类字符串，不能转化为整数

2.浮点数转化为整数：抹零取整

- **float() 函数：**

将其他数据类型转换为浮点数

首先**float()**函数的使用，也是将需要转换的数据放在括号里，像这样：float(数据)。

其次，**float()**函数也可以将**整数**和**字符串**转换为浮点类型。但同时，如果括号里面的数据是**字符串**类型，那这个数据一定得是数字形式。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Language__Python__assets__01-Expression.assets__dd2bdf0fe3cf485bfeae0a055fb51a21.webp)

## conditional expressions

```python
<consequent> if <predicate> else <alternative>
```

```python
#EX
abs(1/x if x!= 0 else 0)
```
