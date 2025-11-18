# Tableau

## Tableau 的基本操作

- 3.1. 连接数据
  - 如何连接到不同类型的数据源（文件、数据库、在线数据集等）。
- 3.2. 创建视图
  - 解释维度和度量的概念。
  - 基本图表类型的创建（条形图、折线图、饼图等）。

### 视图

#### 地图

shift 移动地图

#### 折线图

#### 多维图像

- 双轴

[Tableau 双轴图和组合图_tableau 双轴合并-CSDN 博客](https://blog.csdn.net/weixin_58587245/article/details/122780987)

-

### 构建仪表板

- 如何将多个视图组合到一个仪表板中。
- 仪表板交互性设置（过滤器、操作等）。

## Tableau 进阶使用技巧

### Tableau Prep 数据清洗

- 4.1. 数据预处理和转换
  - 使用数据转换功能，如分组、分段、计算字段等。
- 4.2. 高级图表类型
  - 创建更复杂的图表类型，如热图、树图、散点图矩阵等。
- 4.3. 动态参数和计算
  - 利用参数和计算字段实现动态交互。
- 4.4. 性能优化
  - 提升仪表板性能的技巧和最佳实践。

## 常见问题与解决方案

### 获取 Tableau

- 官方网站提供的下载链接（需要提供官网链接，如<https://www.tableau.com/products/trial）>

### 获取学生免费使用资格

### tabpy 环境配置

[tableau 调用 python 脚本 (纯干货) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/54766875)

[在 Tableau 中使用 Python（TabPy 的使用） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/65402912)

```shell
pip install tabpy-server
```

---

!!! bug "出现问题"
    ```
line 501, in add_reader
        raise NotImplementedError
    NotImplementedError
    ```

通过查询资料，解决方案有：

=== "方法 1: 使用 ProactorEventLoop"

    在Python 3.8及更高版本中，可以通过设置默认的事件循环策略为`ProactorEventLoop`来解决这个问题。这可以通过在运行TabPy之前，在Python代码中添加以下代码实现：
    ```python
    pythonCopy codeimport asyncio
    if sys.platform == 'win32':
     asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    ```

=== "方法 2: 降级 Tornado 版本"
    另一个解决方案是使用一个与Python 3.8及以上版本兼容的Tornado版本。Tornado 6.0及以上版本通常与Python 3.8和3.9有更好的兼容性。确保你的Tornado版本是最新的，或至少是6.0以上。可以通过以下命令更新Tornado：

    ```shell
    shCopy code
    pip install --upgrade tornado
    ```

=== "方法 3: 检查端口是否被占用"

    这个错误还可能是因为TabPy尝试监听的端口已经被另一个进程占用。确保TabPy配置的端口（默认是9004）没有被其他应用程序使用。可以通过更改TabPy配置文件中的端口号或使用命令行参数来指定一个不同的端口。
    
    [参考网址](https://github.com/tableau/TabPy/issues/200)

=== "其他问题"

    另外，发现`startup.py`文件最后有一行语法错误，print没有加括号，导致报错，修正后解决问题

tabpy 安装成功后，在 python 安装目录的 tabpy 文件夹下回有 startup.bat 文件，双击打开，即可启动 tabpy 服务。

启动后，若输出以下结果，则说明 TabPy 服务启动成功！

```text
Initializing TabPy...
Done initializing TabPy.
Web service listening on port 9004
```

打开 Tableau 软件，依次点击菜单栏 ***帮助***-***设置和性能**-**管理外部服务连接***，即可打开服务器连接设置。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__Tableau.assets__image-20240203152819659.webp" alt="image-20240203152819659" style="zoom:50%;" />

## 资源和社区

- 6.1. 官方文档和教程
  - 提供官方文档和学习资源的链接。
- 6.2. 社区论坛和博客
  - 推荐一些活跃的 Tableau 社区和博客，以便深入学习和解决问题。
