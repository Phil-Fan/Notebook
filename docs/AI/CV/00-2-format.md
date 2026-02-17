# 图片格式

!!! note "图像需要存储什么"
    - **图像信息**：宽高、色彩模式、色彩空间等
    - EXIF 信息：拍摄设备、拍摄时间、GPS 信息等

    - **像素数据**：每个像素的颜色信息；二值、灰度、RGB、CMYK、调色盘等 BMP 格式

    压缩算法
    - PNG 无损，JPEG 有损
    - GIF 有损且只支持 256 色
    - 新兴格式如 HEIF、WebP、AVIF 等

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__CV__assets__00-2-format.assets__20240709191542.webp)

- 文件头 `89 50 4E 47 0D 0A 1A 0A | .PNG....`
**采用分块的方式存储数据**,每块的结构都是 4 字节长度 + 4 字节类型 + 数据 + 4 字节 CRC 校验
- 四个标准数据块：IHDR、PLTE、IDAT、IEND
- 其他辅助数据块：eXIf、tEXt、zTXt、tIME、gAMA……
- eXIf 元信息，tIME 修改时间，tEXt 文本，zTXt 压缩文本

=== "文件结构"
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__CV__assets__00-2-format.assets__20240709190857.webp)

    JPEG 使用分段的结构来进行存储，各段以 0xFF 开头，后接一个字节表示类型：
    |开始|作用|
    |---|---|
    |FFD8（SOI）|文件开始|
    |FFE0（APP0）|应用程序数据段，包含文件格式信息（上图没有）|
    |FFE1（APP1）|应用程序数据段，包含 EXIF 信息（上图没有）|
    |FFDB（DQT）|量化表数据|
    |FFC0（SOF）|帧数据，包含图像宽高、色彩模式等信息|
    |FFC4（DHT）|huffman 表数据|
    |FFDA（SOS）|扫描数据，包含数据的扫描方式，huffman 表的使用方式等|
    |FFD9（EOI）|文件结束|

=== "压缩原理"

    **JPEG 的压缩原理是 DCT（离散余弦变换）+ Huffman 编码**
    - 由 RGB 转换到 YCbCr，然后减少 Cb、Cr 的采样率
    - 将图像分块，每个块 8x8，进行 DCT 变换，将图像转换为频域，便于压缩高频部分
    - 量化，将 DCT 变换后的系数除以量化表中的系数：再次减少高频部分的数据，根据不同的量化表，可以调整压缩质量
    - 通过游程编码和 huffman 编码进行压缩

=== "分类"

    `IHDR`：包含图像基本信息，必须位于开头
    - 4 字节宽度 + 4 字节高度
    - 1 字节位深度：1、2、4、8、16
    - 1 字节颜色类型：0 灰度，2 RGB，3 索引，4 灰度透明，6 RGB 透明
    - 1 字节压缩方式，1 字节滤波方式，均固定为 0
    - 1 字节扫描方式：0 非隔行扫描，1 Adam7 隔行扫描

    `PLTE`：调色板，只对索引颜色类型有用,**把像素编码，变成索引编码**
    `IDAT`：图像数据，可以有多个，每个数据块最大 2 31 -1 字节
    `IEND`：文件结束标志，必须位于最后，内容固定
    PNG 标准不允许 IEND 之后有数据块 结尾时`AE 42 60 82`

=== "压缩原理"
    - PNG 使用 Deflate 压缩算法：是 LZ77 结合 huffman 编码的一种压缩算法;LZ77：利用滑动窗口，找到最长的重复字符串，用指针和长度表示
    - 会进行滤波，减少数据的冗余性，提高压缩率;五种滤波器：None、Sub、Up、Average、Paeth

## 图片隐写

两篇博客
[CTF MISC 图片隐写简单题学习思路总结（持续更新）\_ctf jpg 末尾隐写-CSDN 博客](https://blog.csdn.net/weixin_42193791/article/details/126825592)

[常见的隐写工具的使用\_stegoveritas-CSDN 博客](https://blog.csdn.net/qq_44101248/article/details/108850686)

!!! note "WorkFlow"
    - 使用`file`查看信息，使用 `exiftool` 检查图片元信息，看看有没有看起来会有用的信息
    - 使用十六进制编辑器打开，观察文件中有无附带信息、图片基本格式是否正确
    - 使用 `binwalk` 检查文件末尾是否叠加了多余的文件
    - 使用 `stegsolve` 打开图片 / 或者使用 `CyberChef`
    - 使用`steghide extract -sf <file> -p <passwd>`解密数据
    - `zsteg`：自动检测隐写，`zsteg <file>`
    - `stegoveritas -steghide <file>`
    - 观察各个通道的 `bit plane`
    - 使用 `Extract LSB` 尝试提取数据格式的 LSB（或者使用 `zsteg` 猜测）
    - 考虑能否查找原图，如果找到了尝试进行比较
    - 考虑是否是使用工具进行的图片隐写，多尝试一些常见的工具

### 图像大小修改

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__CV__assets__00-2-format.assets__20240709193713.webp)

- PNG 图像按行进行像素数据的压缩，以及存储 / 读取
- 当解码时已经达到了 IHDR 中规定的大小就会结束
- 因此题目可能会故意修改 IHDR 中的高度数据，使之显示不全
-恢复的话更改高度即可，同时注意 crc 校验码，否则可能报错

`binascii.crc32(data)`，data 为从 IHDR 开始的数据 (包含 IHDR)

### 需要原图的图片隐写

使用识图工具进行搜索
一般需要搜原图的题题目描述会带有来源暗示之类的
多注意搜到的图像大小、质量，确保是真正的原图
接下来利用原图和隐写图像的差异进行分析

图像像素异或观察差异

- PIL 手动处理 / `ImageChops.difference`
- stegsolve image combiner

盲水印系列

- 给了打水印的代码的话直接尝试根据代码逆推即可
- 没有给代码的可能就是常见的现有盲水印工具

[guofei9987/blind\_watermark](https://github.com/guofei9987/blind_watermark)

### LSB 图片隐写

LSB 全称为 least significant bit，是最低有效位的意思

LSB 隐写将颜色通道的最低位用来编码信息

- 图像：stegsolve / CyberChef View Bit Plane
- 数据：stegsolve / CyberChef Extract LSB / zsteg / PIL

```python
# PIL 库的使用
from PIL import Image #导入和图像读写处理有关的 Image 类
img = Image.open(file_name) #打开图像
img.show() 显示图像；img.save(file_name) #保存图像
img.size #图像大小
img.mode #图像模式
img.convert(mode) #转换图像模式
img.getpixel((x, y)) #获取像素点颜色
img.putpixel((x, y), color) #设置像素点颜色
np.array(img) #将图像转换为 numpy 数组
```

具体图像模式

- '1'：黑白二值（0/255）；'L'：灰度（8 bit），'l'：32 bit 灰度
- L = 0.299 R + 0.587 G + 0.114 B
- 'P'：8bit 调色盘，获取的像素值是调色盘索引
- 'RGB'、'RGBA'
- 'CMYK'：转换时有色差，CMY = 255 - RGB，K = 0
- 'YCbCr'、'LAB'、'HSV' 等，转换时有复杂公式（可能出现新的隐写）

PIL 其他模块用途

- ImageDraw 用于绘制图像、绘制图形
- ImageChops 用于图像通道的逻辑运算
- ImageOps 用于图像整体的运算一类
- ImageFilter 用于图像的滤波处理

### 人为隐写

- JPEG 中 DCT 系数可以进行 LSB 隐写
- JPEG 中 DHT 定义的 huffman 表可能有冗余项，可以隐写
- PNG 中附加多余 IDAT 数据块的隐写（显示时被忽略）
- PNG 中使用调色盘时可以进行调色盘隐写（EZStego 隐写）
