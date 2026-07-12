# 导论

!!! note "课程信息"
    === "机器学习"

        - 课程时间：2024 年秋冬
        - 课程教师：赵洲
        - 考核内容：2 次书面作业 +2 次编程作业[Kaggle](https://www.kaggle.com/)（45%）+15 次随机签到（15%）+1 次期末摸底考试 +1 次期末考试；（40%）
        - 课本：西瓜书

    === "人工智能与安全"

        - 课程时间：2024 年秋冬
        - 课程教师：陈艳姣
        - workload：一篇论文阅读报告+pre

    === "统计学习"

        - 课程时间：2025 年春夏
        - 课程教师：崔逸凡
        - workload：

    === "CMU 10-414/714: Deep Learning Systems"

        - 课程教师：J. Zico Kolter & Tianqi Chen(CMU)
        - workload：

<div class="card file-block" markdown="1">
<div class="file-icon"><img alt="xmind" src="/style/images/xmind.svg" style="height: 3em;"></div>
<div class="file-body">
<div class="file-title">机器学习思维导图</div>
<div class="file-meta">506KB / 2025-05-21</div>
</div>
<a class="down-button" target="_blank" href="ML.xmind" markdown="1">:fontawesome-solid-download: 下载</a>
</div>

## Acknowledgement

### 笔记

[人工智能基础 - 鹤翔万里的笔记本 (tonycrane.cc)](https://note.tonycrane.cc/cs/ai/basic/)

[02：贝叶斯定理 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/ML/统计机器学习02：贝叶斯定理/)

[命题逻辑 - Jerry's Blog (wxxcl.tech)](https://blog.wxxcl.tech/course/aid/知识表达与推理/命题逻辑/)

[笔记](https://github.com/mura1n/Machine-Learning-in-Practice-Crash-Course-Notes)

<https://github.com/AccumulateMore>

### 网课

B 站<https://space.bilibili.com/1567748478/> 论文带读

[Machine Learning in Practice Crash Course | Jinming Hu (conanhujinming.github.io)](https://conanhujinming.github.io/post/ml_in_practice_crash_course/)

[实用的机器学习 第一课 机器学习导论 2024summer_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Gw4m1i7ys/?spm_id_from=333.788.recommend_more_video.0&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

[机器学习 2023-10-19 第 6-8 节 (zju.edu.cn)](https://classroom.zju.edu.cn/livingpage?course_id=53449&sub_id=915451&tenant_code=112)

[有监督的机器学习：回归与分类 | Coursera](https://www.coursera.org/learn/machine-learning?action=enroll)

[CS229 吴恩达机器学习](https://www.bilibili.com/video/BV16J411t71N)

[CS229: Machine Learning (stanford.edu)](https://cs229.stanford.edu/)

深度学习

[CS231n Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/)：deep learning for CV

[图灵班《机器学习》课程总结 - CC98 论坛](https://www.cc98.org/topic/5599897)

我在心灵学 ML 系列 doge

[再次入门 deep learning 以及一些回忆（更新第二部分） - CC98 论坛](https://www.cc98.org/topic/5207160)

[再次入门 deep learning，这次直接上重点（完结篇） - CC98 论坛](https://www.cc98.org/topic/5208795)

### 会议论文

- ICML (International Conference on Machine
Learning)
- NeurIPS (Neural Information Processing Systems)
- KDD (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- AAAI (AAAI conference on Artificial Intelligence)

### 相关网课

CS188

1. 机器学习：B 站/youtube 李宏毅/吴恩达

2. 深度学习：<https://zh-v2.d2l.ai/> notebook 和课程质量较高，使用的框架的话，pytorch 文献用的比较多，tensorflow 和硬件兼容性好，根据需求选择框架学习，如果觉得难以接受可以多刷几遍

3. 强化学习：<https://hrl.boyuai.com/>   <https://datawhalechina.github.io/easy-rl/#/>

一步步教你每个数据是怎么产生怎么删除的，可视化做的非常好，手脚架给你搭建好了，不需要复杂的工程思考，只需要思考最本质的 梯度，可以快速理解梯度，activation, opt
[LLM Training Puzzles - 寒假摸鱼 (2) - Garl 的文章 - 知乎](https://zhuanlan.zhihu.com/p/20265169815)
[LLM-Training-Puzzles](https://github.com/srush/LLM-Training-Puzzles/tree/main )
[colab 地址](https://colab.research.google.com/github/srush/LLM-Training-Puzzles/blob/main/puzzles.ipynb)

## 定义

!!! note "什么是机器学习"
    以数据作为经验的载体，利用经验数据不断提高性能的计算机系统/程序/算法

    最理想的机器学习技术是学习到 **概念** （⼈类学习，可理解的）

    Artificial Intelligence is a scientific field concerned with the development of algorithms that allow computers to learn without being explicitly programmed

    Machine Learning is a branch of Artificial Intelligence, which focuses on methods that learn from data and make predictions on unseen data

- supervised learning：分类任务（离散），回归任务（连续）；学习一个映射函数$x\rightarrow \mathbf{y}$
- unsupervised learning：找到标签或者模式，聚类、降维
- reinforcement learning：强化学习（相当于是监督学习）
  ![image](https://img.philfan.cn/Math__ML__assets__index.assets__image-20240611173113321.webp)

PAC 模型

$$
P(|f(x)-y \le \epsilon|) \ge 1-\delta
$$

预测误差很小的概率大于 1-δ

iid 保证了统计意义上可以使用机器学习

而$\epsilon$ 表示了泛化能力

概率近似正确：以很高的概率得到一个很接近真实值的结果

??? note "Fundamental Concepts in Machine Learning"

    === "**Sample, Instance, Example**"
        - Sample, instance, and example refer to the same concept, which is a single data point used for training or testing a machine learning model.
        - instance don't contain the label
        - example: instace + label

    === "**Feature, Representation, Predictor**"
        - A feature is an attribute or aspect of the data used to describe a data point.
        - Representation refers to the process of converting data into a form that a computer can process, such as a vector or a matrix.
        - A predictor is a model or function used to predict the target variable.
    
    === "**Label, Target, Class, Pattern Class**"
    
        - A label is the true category or value of the data, used in supervised learning.
        - A target is the variable that the model is intended to predict.
        - A pattern class is a category or grouping of data.
        - A class is a group of data points that belong to the same pattern.
    
    === "**Training Data**"
    
        - Training data is the dataset used to train the model.
        - $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$ represent individual data points in the training data, where $x_i$ is the feature and $y_i$ is the label.
    
    === "**Model, Classifier, Regressor**"
    
        - A model is a mathematical structure used to describe data or predict the target.
        - A classifier is a model used for categorizing data, with a discrete output representing the category.
        - A regressor is a model used for regression analysis, with a continuous output representing the numerical value.
    
    === "**Test Data**"
    
        - Test data is the dataset used to evaluate the performance of the model.
        - $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$ represent individual data points in the test data, where $x_i$ is the feature and $y_i$ is the label.
    
    === "验证集"
        训练集上用来调参数的集合

| 机器学习术语 | 疾病诊断例子 |
| --- | --- |
| 数据集，特征，标记 | 某疾病患者⼈群 |
| 假设空间 | 所有可能的药 |
| 版本空间（跟训练集一致的“假设集合”） | 能治好的药 |
| 归纳偏执 | 偏执：中药西药，副作用大小，费用高低 |
| 没有免费午餐 | 没有特效药，万能药 |

**inductive bias** | 归纳偏好：机器学习算法对于某些假设的倾向性，存在多条曲线符合数据时候，算法的倾向性叫做 inductive bias

### 奥卡姆剃刀原理 | Occam's Razor

在所有可能的解释中，最简单的解释最有可能是正确的（大道至简）

!!! tip "算法的优越性来自于算法的 assumption 和数据的匹配程度"

### NFL | No Free Lunch Theorem

一个算法 A 在某个问题上表现比 B 好，比存在另一个问题，B 比 A 好

脱离具体问题，脱离数据分布和输出，空泛谈论“什么学习算法更好”毫无意义

[NFL 定理推导-CSDN 博客](https://blog.csdn.net/qq_43246110/article/details/104617780)

## 什么时候使用机器学习

there should be some patterns in the data

- we know the patterns,but don't know how to use
- ML can discover the pattern themselves

机器学习是大胆假设和小心求证的折衷

## pipeline

pipeline，中文意为管线，意义等同于流水线。土味一点 你把它 翻译成 **一条龙服务**；专业一点，叫它 **综合解决方案**<br>

![image](https://img.philfan.cn/Math__ML__assets__index.assets__image-20240614191015217.webp)

- **定义问题**:是有监督还是无监督？是分类还是回归？
- 收集数据：
- 数据预处理 transform data & get features：找到 x 和 y
- 创建模型（具体到模型也有相应的 Pipeline，比如模型的具体构成部分：比如 GCN+Attention+MLP 的混合模型）
- 评估模型结果
- 模型调参

是一个**迭代**的过程
