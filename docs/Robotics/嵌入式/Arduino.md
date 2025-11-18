# Arduino

## 资源

[Built-in Examples | Arduino Documentation](https://docs.arduino.cc/built-in-examples/)

[Arduino Tutorials](https://docs.arduino.cc/tutorials/)

[Arduino 板载设备例程](https://docs.arduino.cc/built-in-examples/)

[Arduino 库函数文档](https://www.arduino.cc/reference/en/)

[Arduino 中文教程](https://www.w3cschool.cn/arduino/)

## 配置

### IDE 下载

[Software | Arduino](https://www.arduino.cc/en/software)

下载对应版本的 IDE 即可

### IDE 汉化

打开 arduino，然后点击`File`——>`Preference`，按图 3 顺序点击设置，然后重启，就可以设置成中文了

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Arduino.assets__20250220102213498.webp)

### IDE 库的下载和导入

1. 直接下载
2. 导入 zip 库：点击左上角“项目” -> “加载库” -> “添加.ZIP 库”然后选择下载的 zip 文件即可
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Arduino.assets__20250220101913345.webp)

### vscode 中 Arduino IDE 插件

- 保证 Arduino IDE 下载完成
- 下载插件
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Arduino.assets__20250221115430443.webp)
-

### Python 固件烧录

## 简单例程

### LED 闪烁

[Blink | Arduino Documentation](https://docs.arduino.cc/built-in-examples/basics/Blink/)
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics_______assets__Arduino.assets__20250220090330961.webp)

This example uses the built-in LED that most Arduino boards have. This LED is connected to a digital pin and its number may vary from board type to board type.

```c title="闪烁的代码"
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```

```c title="点亮 LED，实现 LED 闪烁，周期为 1000ms"
int ledPin = 13;  // LED 连接到数字引脚 13

void setup() {
  pinMode(ledPin, OUTPUT);  // 设置 LED 引脚为输出
}

void loop() {
  digitalWrite(ledPin, HIGH);  // 点亮 LED
  delay(500);  // 延时 500ms
  digitalWrite(ledPin, LOW);  // 熄灭 LED
  delay(500);  // 延时 500ms
}
```

## 串口通信

串口通信最重要的参数是波特率、数据位、停止位和奇偶校验。

### 串口操作函数总结

#### `begin()`

**功能**：初始化串口，通常放在 `setup()` 函数中，可配置串口参数。  
**语法**：

```cpp
Serial.begin(speed);
Serial.begin(speed, config);
```

**参数**：

- `speed`：波特率，如 `9600`、`115200` 等。
- `config`：数据位、校验位和停止位配置，如 `Serial.begin(9600, SERIAL_8E2)`（8 位数据，偶校验，2 位停止位）。  
**返回值**：无。

#### `end()`

**功能**：结束串口通信，释放 `Rx` 和 `Tx` 引脚，使其可作为普通 `IO` 使用。  
**语法**：

```cpp
Serial.end();
```

**参数**：无。  
**返回值**：无。

#### `available()`

**功能**：返回串口缓冲区中可读取的字节数（最大 `64B`）。  
**语法**：

```cpp
Serial.available();
```

**参数**：无。  
**返回值**：可读取的字节数。

#### `print()`

**功能**：输出数据到串口，以 `ASCII` 码格式发送。  
**语法**：

```cpp
Serial.print(val);
Serial.print(val, format);
```

**参数**：

- `val`：要输出的数据，任意类型。
- `format`：输出格式，如 `BIN`(二进制)、`OCT`(八进制)、`DEC`(十进制)、`HEX`(十六进制) 或浮点数小数位数。

**示例**：

```cpp
Serial.print(55, BIN);   // 输出 "110111"
Serial.print(55, OCT);   // 输出 "67"
Serial.print(55, DEC);   // 输出 "55"
Serial.print(55, HEX);   // 输出 "37"
Serial.print(3.1415926, 2); // 输出 "3.14"
Serial.print("Hello!");  // 输出 "Hello!"
```

**返回值**：输出的字节数。

#### `println()`

**功能**：与 `print()` 类似，但输出后自动换行。  
**语法**：

```cpp
Serial.println(val);
Serial.println(val, format);
```

**参数**：同 `print()`。  
**返回值**：输出的字节数。

#### `read()`

**功能**：读取串口数据（一个字节），读取后从缓冲区删除。  
**语法**：

```cpp
Serial.read();
```

**参数**：无。  
**返回值**：读取的字节，若无数据则返回 `-1`。

#### `readBytes()`

**功能**：从串口读取指定长度的数据存入数组，超时退出。  
**语法**：

```cpp
Serial.readBytes(buffer, length);
```

**参数**：

- `buffer`：存储数据的数组（`char[]` 或 `byte[]`）。
- `length`：读取的字节数。  
**返回值**：成功读取的字节数，若无数据则返回 `0`。

#### `peek()`

**功能**：读取串口缓冲区的第一个字节，但不删除。  
**语法**：

```cpp
Serial.peek();
```

**参数**：无。  
**返回值**：缓冲区第一个字节数据，若无数据返回 `-1`。

#### `write()`

**功能**：以字节形式发送数据到串口。  
**语法**：

```cpp
Serial.write(val);
Serial.write(str);
Serial.write(buf, len);
```

**参数**：

- `val`：单个字节数据。
- `str`：`String` 类型数据。
- `buf`：数据数组。
- `len`：数据长度。  
**返回值**：输出的字节数。

### 通信例程

```c title="串口读取字符串"
// 读取字符串
void setup(){
  Serial.begin(9600);
}

void loop(){
  String inString="";
  while(Serial.available()>0){
    inString += char(Serial.read());
    delay(10);      // 延时函数用于等待字符完全进入缓冲区，可以尝试没有延时，输出结果会是什么
  }
  // 检查是否接收到数据，如果接收到数据，则输出该数据
  if(inString!=""){
    Serial.print("Input String:");
    Serial.println(inString);
  }
}
```

```c title="使用串口控制 LED 的亮灭"
int ledPin = 13;  // LED 连接到数字引脚 13
String inputString = "";  // 用于存储串口输入的字符串

void setup() {
  pinMode(ledPin, OUTPUT);  // 设置 LED 引脚为输出
  Serial.begin(9600);  // 初始化串口通信
}

void loop() {
  // 检查串口是否有数据输入
  if (Serial.available() > 0) {
    char incomingChar = Serial.read();  // 读取串口输入的字符
    inputString += incomingChar;  // 将字符添加到输入字符串中

    // 如果接收到"On"或者"1"，点亮 LED
    if (inputString == "On" || inputString == "1") {
      digitalWrite(ledPin, HIGH);  // 点亮 LED
      Serial.println("LED is ON");  // 输出状态
    }
    // 如果接收到"Off"或者"0"，熄灭 LED
    else if (inputString == "Off" || inputString == "0") {
      digitalWrite(ledPin, LOW);  // 熄灭 LED
      Serial.println("LED is OFF");  // 输出状态
    }

    inputString = "";  // 清空输入字符串
  }
}
```

### 两个 Arduino 通信

## 中断

>Interrupts are useful for making things happen automatically in microcontroller programs and can help solve timing problems. Good tasks for using an interrupt may include reading a rotary encoder, or monitoring user input.
>
>If you wanted to ensure that a program always caught the pulses from a rotary encoder, so that it never misses a pulse, it would make it very tricky to write a program to do anything else, because the program would need to constantly poll the sensor lines for the encoder, in order to catch pulses when they occurred. Other sensors have a similar interface dynamic too, such as trying to read a sound sensor that is trying to catch a click, or an infrared slot sensor (photo-interrupter) trying to catch a coin drop. **In all of these situations, using an interrupt can free the microcontroller to get some other work done while not missing the input.**

```c title="当手指触摸 2 号引脚时，打印一次 finger touch，手指离开 2 号引脚的时候，打印一次 finger leave"
int pinInterrupt = 2; // 接中断信号的引脚
 
void onTouch()
{
  Serial.println("[info] finger touch");   
}

void onLeave()
{
  Serial.println("[info] finger leave");
}
 
void setup()
{
  Serial.begin(9600);
  Serial.println("[info] begin to work");
 
  pinMode( pinInterrupt, INPUT);// 设置管脚为输入
   
  // Enable 中断管脚，中断服务程序为 onTouch(), 监视引脚变化
  attachInterrupt(digitalPinToInterrupt(pinInterrupt), onLeave, FALLING);
  attachInterrupt(digitalPinToInterrupt(pinInterrupt), onTouch, RISING);
}
 
void loop()
{
  while(1);
}
```

按照触发方式分为下面四类：

- `LOW` to trigger the interrupt whenever the pin is low,
- `CHANGE` to trigger the interrupt whenever the pin changes value
- `RISING` to trigger when the pin goes from low to high,
- `FALLING` for when the pin goes from high to low.

## 定时器
>
> 参考文献：[Arduino 定时器&中断的使用和快速上手\_arduino 定时器-CSDN 博客](https://blog.csdn.net/linZinan_/article/details/127832771)

!!! tip "TimerOne 不仅可以完成定时器的功能，也封装了 PWM 的功能，功能上更加丰富。不过在代码可读性上来说，MsTimer2 更具优势"

Arduino UNO 有三个定时器，

- `timer0`：一个被 Arduino 的`delay()`, `millis()`和`micros()`使用的 8 位定时器
- `timer1`：一个被 Arduino 的`Servo()`库使用的 16 位定时器
- `timer2`：一个被 Arduino 的`Tone()`库使用的 8 位定时器

Actually，定时器的使用也有多种方式，常见的定时器使用方式有**自定义触发、MsTimer2 库、TimeOne 库**三种方式，但事实上，我们不推荐自定义编写定时器触发方式，如果你想使用操作寄存器这种复杂的方式，你就没必要使用 arduino

### MsTimer2

MsTimer2 封装了 Timer2 的定时器，因为为第三方库，所以需要先安装 MsTimer2 库。

[MsTimer2 | Arduino Documentation](https://docs.arduino.cc/libraries/mstimer2/)

```c title="每 500ms 让 13 引脚的 LED 灯亮一下" linenums="1"
#include <MsTimer2.h>

void flash() {
  static boolean output = HIGH;
  digitalWrite(13, output);
  output = !output;
}

void setup() {
  pinMode(13, OUTPUT);
  MsTimer2::set(500, flash); // 500ms period
  MsTimer2::start();  // enables the interrupt.
  // MsTimer2::stop();  // disables the interrupt.
}

void loop() {
}
```

```c title="定时器控制 LED 闪烁，点亮 400ms，熄灭 600ms，窗口输出状态"
#include <MsTimer2.h>

int ledPin = 13;  // LED 连接到数字引脚 13
bool ledState = LOW;  // LED 状态（初始熄灭）
int interval = 400;  // 400ms 亮，600ms 灭

void toggleLED() {
  ledState = !ledState;  // 切换 LED 状态
  digitalWrite(ledPin, ledState);  // 设置 LED 状态
  Serial.println(ledState ? "LED is ON" : "LED is OFF");  // 通过串口输出状态
  MsTimer2::set(ledState ? 400 : 600, toggleLED);  // 设置下次定时
  MsTimer2::start();  // 重新启动定时器
}

void setup() {
  pinMode(ledPin, OUTPUT);  // 设置 LED 引脚为输出
  Serial.begin(9600);  // 初始化串口通信
  MsTimer2::set(interval, toggleLED);  // 设置定时器
  MsTimer2::start();  // 启动定时器
}

void loop() {
  // 主循环无须处理，LED 由中断定时控制
}
```

### TimerOne

[Arduino Playground - Timer1](https://playground.arduino.cc/Code/Timer1/)

```c title=" 在引脚 9 上设置占空比为 50% 的 PWM 输出，并附加一个中断，使 LED 灯频闪"
#include <TimerOne.h>

void callback()
{
    static boolean output = HIGH;
    digitalWrite(13, output); // 状态翻转
    output = !output;
}

void setup()
{
    pinMode(13, OUTPUT);
    Timer1.initialize(500000); // initialize timer1, and set a 1/2 second period
    Timer1.pwm(9, 512); // setup pwm on pin 9, 50% duty cycle
    Timer1.attachInterrupt(callback); // attaches callback() as a timer overflow interrupt
}

void loop()
{
    
}
```

```c title="定时器控制 LED 闪烁，点亮 400ms，熄灭 600ms，窗口输出状态"
#include <TimerOne.h>

int ledPin = 13;  // LED 连接到数字引脚 13
bool ledState = LOW;  // LED 状态（初始熄灭）

void toggleLED() {
  ledState = !ledState;  // 切换 LED 状态
  digitalWrite(ledPin, ledState);  // 设置 LED 状态
  Serial.println(ledState ? "LED is ON" : "LED is OFF");  // 通过串口输出状态
  Timer1.initialize(ledState ? 400000 : 600000);  // 重新设置定时时间（us）
  Timer1.attachInterrupt(toggleLED);  // 绑定中断函数
}

void setup() {
  pinMode(ledPin, OUTPUT);  // 设置 LED 引脚为输出
  Serial.begin(9600);  // 初始化串口通信
  Timer1.initialize(400000);  // 设置定时 400ms（us）
  Timer1.attachInterrupt(toggleLED);  // 绑定中断函数
}

void loop() {
  // 主循环无须处理，LED 由中断定时控制
}
```

### 注意事项

1. 如果你使用了 `MsTimer2` 库，则 `pin11` 和 `pin3` 就不能再用做 PWM 输出了！因为该 `pin3` 和 `pin11` 的 PWM 是靠 `timer2` 帮忙的！(`tone()`也是)
2. 注意 `Servo.h` 库与 `TimerOne` 都是使用内部定时器 `timer1` 会影响 `pin 9`, `pin 10` 的 PWM
3. `tone()` 使用 `timer2` 定时器; 若使用 `Tone` 库的 `Tone` 对象 (`Tone` 变量) 也是优先使用 `timer2` 定时器，若用两个 `Tone` 变量则 `timer1` 也会被用掉，用三个 `Tone` 则连控制 `millis( )`的 `timer0` 也会被用掉。
4. 别忘了， `timer0` 负责帮忙控制 `pin 5` 和 `pin 6` 的 PWM 输出。只要不去改变 `timer` 的 `Prescaler` 就不会影响其控制的 PWM pin，但`MsTimer2` 库与 `tone( )`都会改变 `Prescaler`
