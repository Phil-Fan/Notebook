# 常识

!!! tip "这篇文章列举一些在产品开发中遇到的知识点和有用的技能"

## 开发过程

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114572195274554&bvid=BV1ZZjjzvEFD&cid=30156590888&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

## 版本号

版本号的格式为 X.Y.Z[主版本号。次版本号。修订号]，版本号递增规则如下：

- 主版本号：一般当软件整体重写，或出现不向后兼容的改变时，主版本号递增 1，次版本清零，修订号清零，如 `1.9.1 -> 2.0.0`
- 次版本号：一般功能更新或者增加功能时，主版本号不变，次版本号递增 1，修订号清零，如 `1.5.1 -> 1.6.0` 。
- 修订号：当 Bug 修复发布时，主版号不变，次版本号不变，修订号递增 1，如 `1.5.0 -> 1.5.1`。
- 其他：开发一个新项目时一般以`0.1.0`作为你的初始化开发版本，并在后续的每次发行时递增。当软件开发好后准备正式发布，第一个公开的版本一般是`1.0.0`

## 开源

[Choose an open source license | Choose a License](https://choosealicense.com/)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Dev__assets__rules.assets__20240714184808.webp)

[x-lab 课程 第一讲](https://xlab2017.yuque.com/staff-kbz9wp/ut3q7i/uipcr0gbxd7d3kvx?singleDoc)

## 现代 C++ 开发框架与工具

### 1. 核心框架

| 框架名称 | 用途 | 特点 |
|---------|------|------|
| **Qt** | GUI/跨平台应用 | 信号槽机制、丰富的 UI 组件 |
| **Boost** | 通用库集合 | 智能指针、多线程、算法等 |
| **STL** | 标准模板库 | 容器、算法、迭代器 |
| **Abseil** | Google 基础库 | 补充 STL 功能 |
| **Catch2** | 单元测试 | 简单易用的测试框架 |

### 2. 构建工具链

- **CMake**：跨平台构建系统
- **Conan**：C++ 包管理器
- **vcpkg**：微软 C++ 库管理工具
- **Bazel**：Google 开源的构建工具

### 3. 开发工具

- **CLion**：专业 C++ IDE
- **VSCode + C++ 插件**：轻量级开发环境
- **GDB/LLDB**：调试工具

## Python 开发框架与工具

### 核心框架

| 框架名称 | 用途 | 特点 |
|---------|------|------|
| **Django** | 全栈 Web 开发 | "包含电池"哲学、ORM |
| **Flask** | 轻量级 Web 框架 | 灵活、可扩展 |
| **FastAPI** | 现代 API 开发 | 异步支持、自动文档 |
| **PyQt/PySide** | GUI 开发 | Qt 的 Python 绑定 |
| **Scrapy** | 网络爬虫 | 高性能爬取框架 |

### 数据科学栈

- **NumPy/Pandas**：数据处理
- **Matplotlib/Seaborn**：数据可视化
- **PyTorch/TensorFlow**：深度学习
- **Jupyter**：交互式笔记本

### 开发工具

- **PyCharm**：专业 Python IDE
- **Poetry**：依赖管理和打包工具
- **Pytest**：单元测试框架
- **Black**：代码格式化工具

## 学习路线建议

### C++ 学习路线

1. **基础阶段**（1-2 个月）
   - C++11/14/17 核心语法
   - STL 标准库使用
   - CMake 基础构建

2. **中级阶段**（2-3 个月）
   - Boost 常用组件
   - 多线程编程
   - 内存管理优化

3. **高级阶段**（3-6 个月）
   - 模板元编程
   - 现代 C++ 设计模式
   - 性能分析与优化

4. **专业方向选择**
   - GUI 开发：Qt 框架
   - 游戏开发：Unreal Engine
   - 高频交易：低延迟编程

### Python 学习路线

1. **基础阶段**（1 个月）
   - Python 核心语法
   - 常用标准库
   - 虚拟环境管理

2. **中级阶段**（2-3 个月）
   - Web 开发（Django/Flask）
   - 数据处理（Pandas/NumPy）
   - 自动化脚本编写

3. **高级阶段**（3-6 个月）
   - 异步编程（asyncio）
   - 性能优化（Cython）
   - 架构设计

4. **专业方向选择**
   - 数据科学：PyData 生态
   - 机器学习：PyTorch/TensorFlow
   - DevOps：自动化运维

## 现代项目开发实践

### 典型 C++ 项目结构

```shell
my_project/
├── CMakeLists.txt
├── include/
│   └── my_lib.h
├── src/
│   └── my_lib.cpp
├── tests/
│   └── test_my_lib.cpp
└── third_party/  # 外部依赖
```

### 典型 Python 项目结构

```shell
my_project/
├── pyproject.toml  # Poetry 配置
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── module.py
├── tests/
│   └── test_module.py
└── .github/  # CI/CD配置
```

掌握这些框架和工具后，您将能够高效地开发现代化 C++ 和 Python 应用程序。建议从一个小型项目开始实践，逐步积累经验。
