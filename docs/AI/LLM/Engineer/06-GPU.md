# GPU 工作原理

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1056401051&bvid=BV1rH4y1c7Zs&cid=1621184404&p=1&autoplay=0&high_quality=1&danmaku=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

## 显卡简介

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121100854.webp)

显卡由 **显卡核心（GPU） 、电路板（PCB）、显存、金手指、供电 & 显示接口以及散热**等构成。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121100941.webp)

显卡核心里主要由运算单元 cuda core，控制单元，缓存单元等构成。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121101011.webp)
显存，类似于系统的内存，但它是显卡专用的内存。显存主要用来缓存 GPU 处理过的或者即将提取的渲染数据。显存主要包括容量、频率和位宽这三个参数。容量就是显存的大小，一般来说，显存越大能存储的数据越多，对于部分场景很有用

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121101048.webp)

输出部分就是显卡挡板处的接口，有：VGA、DVI、HDMI、DP、USB-C（包括雷电 3）

显卡和显示器之间的接口，共有 VGA、HDMI、DVI、DP 以及 USB-C（包括雷电 3）等。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121101127.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121101207.webp)

开放式风扇是直接吹显卡（鳍片）来提供散热，使用场景比较广泛，有无风道都能用，而且相较而言更静音。涡轮风扇散热则是靠吸入风量横吹核心（鳍片），与开放式相比，对整机内部其它硬件影响不大，比较适合有平行风道，而且工作温度不高的显卡。但估计以后公版也会多采用开放式而放弃涡轮。

### 显卡分类

显卡根据不同的位置，有**集显、核显和独显**的区别
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/AI__LLM__Engineer__assets__06-GPU.assets__20241121101331.webp)

- **集显** 集成在主板北桥芯片的显示芯片，有些共享系统内存，有些自带内存。现在少见了，常有人把核心显卡当作集成显卡，再过些年这么叫也可能是对的了。
- **核显**  集成在核心（CPU 内）中的显卡，共享系统内存资源。
- **独显** 将显示芯片及相关器件制作成一个独立于电脑主板的板卡，成为专业的图像处理硬件设备。

英伟达 Geforce 共有 GT、GTX、RTX 和 TITAN 四个系列，

（这时可能会有没看前面的脑子瓦特的就会跳出来说明明还有 quadro 系列）

GT 代表 GeForce Technology，比较适合家用入门级，影音和小游戏都能满足。

GTX 代表更高级的游戏独显，后来随着技术进步，出现了光线追踪（Ray Tracing），于是命名也增加了一个 RTX，因为是最先进的技术，再低端也是很昂贵，所以 RTX 都是从 -60 结尾往上走，价格也比以往 GTX 的更贵。而 TITAN 就是英伟达 GeForce 的看家显卡，霸主的存在。

> [【显卡科普】小白必看的入门显卡科普，关于显卡的原理、结构、作用 - 知乎](https://zhuanlan.zhihu.com/p/156083352)

## 精度

## 存储

## 计算
