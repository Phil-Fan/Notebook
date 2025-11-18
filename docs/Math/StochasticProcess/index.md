# 随机过程

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Math__StochasticProcess__assets__index.assets__964741a61d8044f9a864e5dfb860cbb2aa865e69.webp)
> 莫奈《昂蒂布的城堡》高中时候最喜欢的一个错题本的封面

- [x] Chap1 随机过程基本概念
- [x] Chap2 马尔可夫链
- [x] Chap3 泊松过程
- [x] Chap4 布朗运动
- [x] Chap5 平稳过程

!!! note "段子"
    人的一生应当学四次随机过程

    第一次是在概率论的阶梯教室，马尔可夫链在转移矩阵里安睡，而你的青春正与无记忆性较劲。抛硬币的轨迹画出鞅的边界，像极了二十岁未知的心跳，总以为找到稳态分布，就握住了命运的均值，却不知窗外纷飞的柳絮，正把泊松过程写成飘散的随机游走诗篇。

    第二次是在数字丛林的代码战场，条件期望在循环语句里重构日常。你在算法构筑的"遍历性"迷宫中突围，用蒙特卡洛采样丈量需求的热度。当截止日期逼近，BUG像布朗运动般涌现，那些闪烁的屏幕，都是随机微分的证明，将三十岁的热望，熔炼成凌晨三点的概率流。 

    第三次是在孩童的乐高城堡边，陪他拼接蒙特卡洛的积木。马尔科夫毯下藏着成长的平稳分布——就像房贷是本该收敛的鞅，旋转木马的欢笑是瞬态响应，而生活样本空间的更新，总在亲子协方差的涨落中，把中年的方差，换算成睡前故事的正交分解。

    第四次是在夕阳浸润的落地窗前，看见鞅的收敛穿过时间序列。窗格间的卡方检验折射生涯的置信区间。那些离散的故人啊，原来是协方差平稳的相位噪声，虽隔着重样本的间距，仍有自相关的温度，在记忆的宽平稳里，完成最后一次弱收敛的证明。

## 简介

选这个课是想再学一点概率相关的话题，补一点数学知识

课程成绩由平时成绩（40%）和期末成绩（60%）组成。平时成绩注重过程考核，包括平时到课率 (数字点名)，课后作业，以及随堂小测（周六小测，类似概统）；

期末考试采用闭卷考试，考试时间通常为两个小时。

填空：布朗运动、数字特征、平稳过程、泊松运动
大题：数字特征 + 泊松过程 + 马尔科夫链×2+ 平稳过程

### 学习方法

公式记牢、基本概念记牢、多做计算题

对于数学基础不好的同学，强调应用结论而不是理解或者推导结论；不要过于重视公式或者概念背后的深层含义，不求甚解

随机过程各个章节的内容其实关联不是特别紧密，中间可以不按照顺序来学。

### 复习进度记录 & todo

- [x] 半个下午 + 晚上 chap4possion+brown+chap5 stationary
- [x] 听了复习课 + 复习 Chap3 Markov Chap2 定义；梳理特殊概念；做了 4 章复习题 PPT
- [x] 做了老师上课讲的 3 套卷子 + 历年题的几套卷子
- [x] 复习题目整理
- [x] Brown 两个定理理解 + 各态历经定理
- [x] 布朗桥证明题写法
- [x] 作业整理
- [ ] 通俗含义解释
- [x] 公式 cheet sheet 整理

## 资源汇总

通过网盘分享的文件：随机过程

链接：<https://pan.baidu.com/s/1Z47JujDl_nhpDbRhhAdOGw?pwd=PHIL> 提取码：PHIL

```text
.
├── 01-book
│   ├── 应用随机过程 张帼奋.pdf
│   └── 应用随机过程（第二版）.pdf
├── 02-slides
│   ├── 第1章  预备知识.ppt
│   ├── 第2章  随机过程的基本概念.ppt
│   ├── 第3章 马尔可夫链.ppt
│   ├── 第4章 泊松过程和维纳过程.ppt
│   └── 第5章 平稳过程.ppt
├── 03-hw
│   ├── README.txt
│   ├── 第1次作业.pdf
│   ├── 第2次作业.pdf
│   ├── 第3次作业.pdf
│   ├── 第4次作业.pdf
│   ├── 第5次作业.pdf
│   ├── 第6次作业.pdf
│   ├── 第7次作业.pdf
│   └── 思考题、习题答案.pdf
├── 04-quiz
│   ├── 随过小测题库1.pdf
│   ├── 随过小测题库2.pdf
│   └── 小测题库 by czqlds.pdf
└── 05-review
    ├── 复习题
    │   ├── 第2章复习题.ppt
    │   ├── 第3章复习题 .ppt
    │   ├── 第4章复习题 .ppt
    │   ├── 第5章复习题 .ppt
    │   ├── 复习题 .ppt
    │   ├── 复习题.docx
    │   └── 复习题.pdf
    ├── 历年卷
    │   ├── 16-17补考.doc
    │   ├── 16-17补考.pdf
    │   ├── 17.md
    │   ├── 19-20.md
    │   ├── 22-23_答案.pdf
    │   ├── 22-23.pdf
    │   ├── 23-24.pdf
    │   ├── 25.pdf
    │   └── 随过历年卷 蓝田书店.pdf
    ├── 随过笔记 by 启动.pdf
    ├── 随过笔记 by 竝
    └── 随过笔记 by Peter_H.pdf
```

## Acknowledgement

### 课程笔记

在学习随机过程的过程中，我参考了以下资料：

其中，markdown 笔记记录过程中参考了[竝](https://www.cc98.org/topic/4929320)学长，[小胖一族](https://skillful-vest-b8d.notion.site/1-5-68ec83a57e504b79901e66a2b7e4e5ce)学长和[TyrannosaurusLjx](https://github.com/TyrannosaurusLjx/TyrannosaurusLjx.github.io/tree/main/docs/Notebook/Random-Process)学长的，感谢几位学长。

- [启动 前辈的笔记](https://file.cc98.org/v4-upload/d/2025/0602/55uqtm1w.pdf)
- [竝 - 笔记](https://www.cc98.org/topic/4929320)

### 回忆卷

- [2025 夏 - principle](https://www.cc98.org/topic/6215739)
- [Akino - 随过（工科 1.5 学分）版搜历年卷合集](https://www.cc98.org/topic/6198962)
- [2023-2024](https://www.cc98.org/topic/5930307)
- [2022-2023](https://www.cc98.org/topic/5643156)
- [2019-2020](https://www.cc98.org/topic/4958697)
- [2018-2019](https://www.cc98.org/topic/4855261) (随机过程与排队论)
- [16-17 秋随过补考题目](https://file.cc98.org/v4-upload/d/2025/0528/2zeatkye.pdf)
- [2017](https://www.cc98.org/topic/4728993) (随机过程与排队论)
- [2016](https://www.cc98.org/topic/4641632) (随机过程与排队论)
- 蓝田扫描版
- 另外，老师发了一些复习题目 ppt

### 习题与小测

- [orz_xiaoa - 应用随机过程（1.5 学分）部分作业习题答案 - CC98 论坛](https://www.cc98.org/topic/5358767):链接：<https://pan.baidu.com/s/11s85aX0ZooESH3shA02fHA>  提取码：7ttc
- 我也把我自己的部分习题答案写在了对应章节，欢迎纠错
- [czqlds - 小测题目和答案分享](https://www.cc98.org/topic/6191222)
- [climb - 书后附课后题答案分享](https://www.cc98.org/topic/5891251)

### 课程资料

1. [宫水三翊 - 随机过程 / 随过（1.5 学分 wxy 老师班）资料分享](https://www.cc98.org/topic/6121175)

2. [暴龙战士 - 随机过程资源分享](https://www.cc98.org/topic/5927145) 数院 3 学分

3. [Uiiiii - 复习资料](https://www.cc98.org/topic/5926769)

4. [N 丿 aivest - 复习笔记＆平时作业答案](https://www.cc98.org/topic/5642973)

5. [聊以 - 学习资料](https://www.cc98.org/topic/5643340)

6. [WinW - 学习笔记](https://www.cc98.org/topic/5720807)

7. [keke25 - 复习整理](https://www.cc98.org/topic/5355801)

8. [8h5d233 - 随机过程传送门（资源整合）](https://www.cc98.org/topic/5639264)

### 其他

[人的一生应该学四次随机过程 - CC98 论坛](https://www.cc98.org/topic/6158605)
