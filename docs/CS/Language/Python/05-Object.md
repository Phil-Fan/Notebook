# 对象 `Object`

在创建模块化项目时，一个非常有用的实践是引入可能随时间改变状态的数据。

面向对象编程 (object-oriented programming) 的核心就是向数据添加状态

实际上，Python 中所有的值都是对象。也就是说，所有的值都有行为和属性，它们拥有它们所代表的数据的行为。

## 对象和类

对象三个要素：（id, type, value）

- 类（类型）： `int、 float 、bool 、string list 、tuple 、dict 、set`
- 对象举例： `3，[5.7,’a’]，{1:4,2:5}`
- `type()`函数判断对象的类

- 类 (class): 定义属性 (数据) 和⾏为（⽅法）的模板
- 实例 (instance)：是⽤类产⽣的对象，

- 术语对象 (object) 和实例 (instance) 经常是可以互换的
- 使⽤圆点运算符 (.) 引⽤⽅法和属性
- 类有⾃⼰名字空间
- 每个对象也有⾃⼰的名字空间

### 消息传递

什么是消息传递？
想象你有一部手机（对象）：

你不用知道手机内部怎么工作的

- 你只需要按按钮（发消息），手机就会做出响应

- 按"拍照"按钮 → 手机执行拍照功能

- 按"音量+"按钮 → 手机调大音量

## 创建和使用

```py
class <类名>:    
    initializer    
    methods
    
class Student:    #学⽣类：包含成员变量和成员方法
    def __init__(self,mname,mnumber): #构造方法
        self.name = mname    #成员变量
        self.number = mnumber
        self.Course_Grade = {} 
        self.GPA = 0

    def getInfo(self):    #成员方法
        print(self.name,self.number)

s1 = Student("wang","317000010")    #创建 s1 对象
s1.getInfo() 
Student.getInfo(s1)
s2=Student("zhang","317000011") #创建 s2 对象
s2.getInfo()
```

- `__init__()`

  - `__init__()`⽅法是 Python 类中的⼀种特殊⽅法，⽅法名的开始和结束都是双下划线，该⽅法称为构造⽅法，当创建类的对象时，它被⾃动调⽤

  - `__init__()`⽅法中可以声明类所产⽣的对象属性，并可为其赋初始值。该⽅法有⼀个特点，不能有返回值，因为它是⽤来构造对象的，调⽤后实例化了⼀个该类型的对象

- `self`参数

  - 类的实例⽅法有⼀个名为`self`的参数，并且必须是⽅法的第⼀个形参（如果有多个形参的话），`self`参数代表将来要创建的对象本身

  - 在类的⽅法中访问实例变量（数据成员）时需要以 self 为前缀

  - 在外部通过对象调⽤对象⽅法时并不需要传递这个参数，如果在外部通过类调⽤对象⽅法则需要显式为`self`参数传值

## 属性（attributes）

```py
<expression> . <name>
```

## 方法（methods）

其实也是属性，只不过该属性的值是函数。对象知道如何执行这些方法。

数据共享和身份（Sharing and Identity）

最后两个比较说明了 is 和 == 的区别。前者是检验的是对象的内存地址，而后者只是判断内容是否相同。

- Python 类中成员：
  - 数据成员（变量、属性）
- 类数据成员

  - 公有
  - 内部：以两个下划线`__`开头
  - ⽅法（函数）
    - 实例⽅法：
      - 公有
      - 私有：⽅法名以两个下划线`__`开头
  - 类⽅法： @classmethod
  - 静态⽅法：@staticmethod
- 在 Python 中，以下划线开头的⽅法名和变量名有特殊的含义，尤其是在类的定义中

## 封装

- 将数据和对数据的操作组合起来构成类，类是⼀个不可分割的独⽴单位
- 类中既要提供与外部联系的接⼝，同时⼜要尽可能隐藏类的实现细节。
- Python 类中成员分为数据（变量、属性）成员和⽅法（函数）成员。

## 继承

## 多态

1. 子类型多态（继承多态）
最常见的多态形式，通过继承实现：

    ```python
    class Animal:
        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "汪汪汪！"

    class Cat(Animal):
        def speak(self):
            return "喵喵喵！"

    # 多态体现
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())
    # 输出：
    # 汪汪汪！
    # 喵喵喵！
    ```

2. 鸭子类型多态（Python 特色）
Python 更推崇"鸭子类型"——如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子：

```python
class Dog:
    def speak(self):
        return "汪汪汪！"

class Robot:
    def speak(self):
        return "我是机器人！"

# 不要求继承同一父类，只要有 speak 方法就行
things = [Dog(), Robot()]
for thing in things:
    print(thing.speak())
# 输出：
# 汪汪汪！
# 我是机器人！
```

len 作用在不同对象上，有不同的行为。

```py
print(len("hello"))  # 字符串 → 5
print(len([1,2,3]))  # 列表 → 3
print(len({"a":1, "b":2}))  # 字典 → 2
```
