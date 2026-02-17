# OpenCV 学习

[OpenCV 计算机视觉（Python）- - 一路狂奔的乌龟 - 博客园](https://www.cnblogs.com/GYH2003/collections/5918)

[OpenCV Python Tutorials](https://opencv-python-tutorials.readthedocs.io/zh/latest/)

## 安装与配置

python 与 opencv 的版本对应关系
[Links for opencv-python](https://pypi.tuna.tsinghua.edu.cn/simple/opencv-python/)
![image](https://img.philfan.cn/AI__CV__assets__OpenCV.assets__20240914103526.webp)

```shell title="安装"
pip install opencv-python==3.4.11.45 # 这里版本要和 python 对应
pip install opencv-contrib-python==3.4.11.45
```

```text
numpy.core.multiarray failed to import
```

解决方案：修改 numpy 版本

[OpenCV-python 安装教程\_opencv python 安装-CSDN 博客](https://blog.csdn.net/qq_41627235/article/details/87692748)

```shell title="验证方法"
ipython
import cv2
```

没有报错即可

## Image Formats

HSV

- meaning

  - `Hue`

  - `Saturation`

  - `Value/Lightness`

- advantage

In image recognition,RGB is easily affected by light

- Manual compensation through programming
- Convert it into `HSV` mode

## Lec1

### Basic

```python
import cv2
## read image
cv2.imread(path, flags)

```

flags:指定以何种方式加载图片，有三个取值：

 `cv2.IMREAD_COLOR`:读取一副彩色图片，图片的透明度会被忽略，默认为该值，实际取值为 1；
 `cv2.IMREAD_GRAYSCALE`:以灰度模式读取一张图片，实际取值为 0
 `cv2.IMREAD_UNCHANGED`:加载一副彩色图像，透明度不会被忽略。

读取成 mat numpy 格式

```py
## show image
cv2.imshow(winname, mat)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.destroyWindow()
cv2.namedWindow()
```

`namewindow`: `cv2.WINDOW_NORMAL`,默认为`cv2.WINDOW_AUTOSIZE`

```py
## save image to local file

```

```py
## convert image
cv2.COLOR_BGR2RGB
cv2.COLOR_BGR2GRAY
cv2.COLOR_GRAY2BGR 
```

### digitalize image

#### step

- 扫描
- 采样
- 量化：空间换质量

#### Grayscale

 0 stand for full black

255 stand for full white

```python
cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
```

- Grayscale conversion algorithms
  - `Gray = (Red + Green + Blue) / 3` averaging
  - `Gray = (Red * 0.3 + Green * 0.59 + Blue * 0.11)` in Photoshop and GIMP
  - `Gray = (Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)`
  - `Gray = (Red * 0.299 + Green * 0.587 + Blue * 0.114)`
  - `Gray = (Max(Red, Green, Blue) + Min(Red, Green, Blue)) / 2` desaturation
- Grayscale conversion algorithms
  - `Gray = Max(Red, Green, Blue)` maximum decomposition
  - `Gray = Min(Red, Green, Blue)` minimum decomposition
  - `Gray = Red` single color channel (red)
  - `Gray = Green` single color channel (green)
  - `Gray = Blue` single color channel (blue)
  - Custom algorithms

#### Binary-scale

The commonly used method is: select a certain threshold `T`, if the gray value is smaller than the threshold, then `0`, otherwise `255`

```text
cv2.threshold (src, dst, thresh, maxval, type)
```

- `src`: input array
- `dst`: output array (same size and type and same number of channels)
- `thresh`: threshold value
- `maxval`: maximum value to use (`cv2.THRESH_BINARY` and `cv2.THRESH_BINARY_INV`)
- type: thresholding type
  - `cv2.THRESH_BINARY`
  - `cv2.THRESH_BINARY_INV`
  - `cv2.THRESH_TRUNC`
  - `cv2.THRESH_TOZERO`
  - `cv2.THRESH_TOZERO_INV`
  - `cv2.THRESH_OTSU`
  - `cv2.THRESH_TRIANGLE`

```py
cv2.adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
```

- `src`：灰度化的图片
- `maxValue`：满足条件的像素点需要设置的灰度值
- `adaptiveMethod`：自适应方法。有 2 种：`ADAPTIVE_THRESH_MEAN_C` 或 `ADAPTIVE_THRESH_GAUSSIAN_C`

adaptiveMethod 的选择非常关键。

一种是使用均值的方法，而另外一种是使用高斯加权和的方法。所谓均值的方法就是以计算区域像素点灰度值的平均值作为该区域所有像素的灰度值。这其实就是一种平滑或滤波作用。
高斯加权和算法是将区域中点（x，y）周围的像素根据高斯函数加权计算他们离中心点的距离。
一般情况下建议使用高斯加权和。

- thresholdType：二值化方法，可以设置为`THRESH_BINARY`或者`THRESH_BINARY_INV`
- `blockSize`：分割计算的区域大小，取奇数
- C：常数，每个区域计算出的阈值的基础上在减去这个常数作为这个区域的最终阈值，可以为负数
- dst：输出图像，可选

Otsu’s Binarization

```text
cv.THRESH_OTSU
```

## Application of OpenCV

- Filtering, binarization, cutting, scale and rotation transformations, image gradients
- Line and circle detection, feature point detection, edge detection, blob detection, feature point detection, pattern recognition
  - QR code identification
  - Face detection
  - Gesture recognition
  - Human gesture recognition
