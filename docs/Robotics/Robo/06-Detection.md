# 传感与检测

!!! note "课程信息"
    === "主要内容"
        各种检测技术和仪表;

        目标：可以设计一个测量系统，完成传感器的选型

    === "成绩组成"
        - 期末60% 
        - 半开卷1张A4
        - 实验课（25%）
        - 平时互动15%
  
        平时作业一共 7 次，再加一个期中大作业（其实就是一张卷子）算是有 8 次作业，难度不大，基本是课后习题，大部分网上也能搜得到。平时作业和期中作业建议一定要认真完成，尤其是期中作业，期末真的会考原题。以及最后期末涉及到的计算题基本在平时作业里也都是出现过的。

    === "实验课"
        - 冬学期开始上实验课，在[控制学院自动化实验中心](http://10.202.69.21/aec/redir.php?catalog_id=441)网站上进行预约；记得提早预约提早做完。报告就是在模板上增加一些记录的内容就可以了。
        - 三个实验：
            - 智能产线传感与检测实验：比较水，时间最短
            - 温度检测和显示仪表实验：稍微久，要使用热电偶。
            - 压力与液位检测实验：大概1h多

    === "考试"
        原理——元件——仪表——测量系统

        而是按3-1-2-4顺序抄的（按照章节的重要度排序，保证把最重要考的最多的部分抄完，老师在复习课上也会提）；
        题型很固定，一般就是三道计算（虽然今年只有两道）：准确度量程计算、热电偶计算、量程迁移计算。
        
        宏观来讲二三章是考试重点，第一章篇幅少但是考的多；第二章辐射式检测元件基本补考，红外要求偏弱；第三章比较重要，3.7仅作为案例（反馈的作用）；第四章“跟着听了就会了”

        言多必失

    === "资料整理"
        [awslasasd的笔记](https://awslasasd.github.io/Class/%E4%BC%A0%E6%84%9F%E4%B8%8E%E6%A3%80%E6%B5%8B/)

        [2022-2023秋冬《传感与检测》线上A卷回忆卷 - CC98论坛](https://www.cc98.org/topic/5506035)

        [控院课程《传感与检测》半开卷A4纸分享 - CC98论坛](https://www.cc98.org/topic/5506130)

        [控院 自动化专业 传感与检测课程 期末半开卷a4 分享 - CC98论坛](https://www.cc98.org/topic/5508695)

        [传感与检测 2023-2024秋冬 回忆卷 - CC98论坛](https://www.cc98.org/topic/5799432)


        [【现代控制理论】【电气控制技术】【信号分析与处理】【计算机网络原理】【电路与模拟电子技术实验】【大学物理实验】【测控系统综合实践】【传感与检测】参考实验报告（自动化、电子信息工程、电气工程及其自动化） - CC98论坛](https://www.cc98.org/topic/6035333/1#1)

!!! tip "本笔记只记录知识框架的思维导图和具体难理解的点，不做细节完全整理"

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets___E4_BC_A0_E6_84_9F_E4_B8_8E_E6_A3_80_E6_B5_8B.svg)

## 计算题整理

[期中考试讲解](https://interactivemeta.cmc.zju.edu.cn/#/replay?course_id=67888&sub_id=1465044&tenant_code=112)

### 热电偶

### 压力表等级选择

允许最大绝对误差应该使用压力范围的下界进行计算

### 量程迁移

## 第一章——检测技术基础

准确度计算

灵敏度

减少误差的方法：P19-21

非线性补偿的方法

检测仪表结构与设计
开环和闭环（直接串联和平衡/反馈）仪表的特点

测量标准差：两个公式都写

- 使用真值：

- 使用均值：

## 第二章——检测技术与检测元件

复杂公式和图表放过

建议做表格（原理、特点、使用中的考虑的问题）

### 热电

两种原理：接触电势 & 温差电势

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=294913421&bvid=BV16F411q7uS&cid=463225721&p=1&autoplay=0" width="600" height="450" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=537416266&bvid=BV1Ni4y1a7sN&cid=1372016762&p=1&autoplay=0" width="600" height="450" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

- 对应关系加减法
- 非线性，不能直接对应

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241031181717.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241031181647.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241031181700.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241031181749.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241116163557.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241116163142.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241116163159.webp)

电阻：要采用三线或四线接法，减少引线电阻的影响
电偶：对冷端进行温度补偿

### 光电

!!! bug "光敏三极管和二极管的理解"

倍增管

### 磁电

!!! note "为什么霍尔元件一般用半导体"

    霍尔系数:$K=\frac{1}{n\cdot q}$式中,$n$为载流子密度,

    一般金属中载流子密度很大，所以金属材料的霍尔系数系数很小,霍尔效应不明显；而半导体中的载流子的密度比金属要小得多，所以半导体的霍尔系数系数比金属大得多,能产生较大的霍尔效应

!!! bug "霍尔元件测转速"

### 磁弹性

基于铁磁材料的磁弹性效应：受外力作用产生内应力，引起磁阻或磁导率的变化

**磁致伸缩效应**

用来描述这种长度变化的程度，定义为材料长度变化量与原始长度的比值，即 $\lambda = \frac{\Delta l}{l}$。

**压磁效应**

当铁磁材料受到外力作用（如压力或拉力）时，其磁导率（即材料对磁场的响应能力）会发生变化$\frac{\Delta \mu}{\mu} = \frac{2\lambda}{B^2} \sigma \mu$。其中，$B$ 是磁感应强度，$\sigma$ 是应力，$\mu$ 是原始磁导率。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241031112847.webp)
ex:负磁滞材料，受到正压力，磁畴向磁矢量垂直于正压力方向偏转，磁导率降低

压磁元件

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__06-Detection.assets__20241031113428.webp)

一开始测量线圈平行，压一下之后，不平行

磁致伸缩原理的应用？

从应用角度讨论并分析压阻式（半导体应变片）、压电式和压磁式检测元件各有什么特点

- **压阻：** 灵敏度高，受温度影响大；对快速系统和慢速系统都适用

- **压电：** 频率响应好，只能测快速变化，不能测恒力；只能适用快系统

- **压磁：** 功率大，灵敏度不足，反应速度慢；只能适用于慢系统

[第二章 - 第三讲](https://vod.cmc.zju.edu.cn/newdefault/2024/10/26/a9fa36d608f2022fea8807884c4365cc_1920_1080.mp4?auth_key=1730360364-0-0-a57a0dbad20e8380846b5f7c6ad9f420&t=636426-1730345965-20c6c58016e732bd954a500acca545e9)

### 核辐射式

利用被测物质对射线的吸收、散射、反射或射线对被测物质的电离作用

不关心还剩多少，只关心单位时间衰变多少

- 放射性强度
- 半衰期
- 平均

盖革计数器

如何用核辐射式检测元件实现材料厚度、液体浓度、成份等的测量？

大气窗口：吸收比较弱的区域

### 超声波

人耳 20-20KHz

声场参量：

- 声压（声压级：对数级 dB）
- 声强（声强级）
- 声阻抗

横波不能在液体或气体介质中传播
表面波不能在液体或者气体介质中传播

## 仪器

敏感元件和显示装置必不可少

### 温度检测

### 压力检测

### 物位检测

### 流量检测

### 气体成分检测

## 现代检测技术

### 软测量
