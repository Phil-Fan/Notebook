# 无人机实验

!!! note "基础信息"
    时间：
    分组：
    实验内容：
    实验要求：4000字以上报告
    tips：每组一位助教，珍惜助教hhh

## 硬件平台

### 硬件搭建

qgroundcontrol

[Download and Install | QGC Guide (master)](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html#windows)

### 树莓派安装

!!! failure "树莓派发烫"
    解决方法：因为实验室没有多余的风扇套装了，所以在淘宝购买了两个树莓派风扇。

### 动捕测试

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920205747.webp)

## 软件搭建

!!! note "网络遇到问题"
    在开始组装时候，遇到了校网连接问题，无法下载软件。

### 基本 linux

换源 ros,pip -> fishros

```shell
wget http://fishros.com/install -O fishros && . fishros
```

```shell
sudo apt-get update
sudo apt-get upgrade
```

terminator

```shell
sudo apt-get install terminator
```

### ssh

```shell
sudo apt install net-tools
```

```shell
ifconfig
```

```shell
sudo apt-get install openssh-server
ssh user@remote
ssh -X ldz@192.168.0.1  # 带图形化界面
ssh -p 1234 ldz@192.168.0.1 # 指定端口
```

```shell
vim /etc/ssh/sshd_config
```

- 第 33 行：将 PermitRootLogin without-password（第 33 行）改为 PermitRootLogin yes 并去掉前面的注释符号（#）
- 第 57 行:#PasswordAuthentication yes(第 57 行) 的注释去掉，如果是 no 就改为 yes
- 保存

```shell
service ssh restart
```

验证安装

```shell
service ssh status
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240711175232.webp)

开机自启动

```shell
update-rc.d ssh enable
```

配置免密登陆

```shell
ssh-keygen -t rsa
```

然后根据提示一步步的按 enter 键即可（其中有一个提示是要求设置私钥口`passphrase`，不设置则为空，这里看心情吧，如果不放心私钥的安全可以设置一下）

执行结束以后会在`/home/当前用户` 目录下生成一个 `.ssh` 文件夹，其中包含私钥文件 `id_rsa` 和公钥文件 `id_rsa.pub`。

ssh-copy-id 会将公钥写到远程主机的 `~/.ssh/authorized_key` 文件中

```shell
ssh-copy-id name@ip
```

注意，windows 的 cmd 中不能直接执行 ssh-copy-id 命令，可以使用 git bash 或者其他 linux 终端工具

当出现
> Number of key(s) added: 1
> Now try logging into the machine, with:   "ssh 'HAHA@127.0.0.1'" and check to make sure that only the key(s) you wanted were added.

说明配置成功！

### vscode

fishros 下载比较方便

```shell
wget http://fishros.com/install -O fishros && . fishros
```

### ros

fishros 下载比较方便

```shell
wget http://fishros.com/install -O fishros && . fishros
```

20.04 装 noetic

### htop | 系统状态监测与进程管理

```shell
sudo apt-get install htop
```

### nomachine

查看芯片架构

```bash
uname -m
```

在官网上下载对应的版本
[NoMachine - NoMachine for Arm](https://downloads.nomachine.com/linux/?distro=Arm&id=30)

```bash
sudo dpkg -i nomachine_7.6.2_4_armhf.deb
```

### PlotJuggler

??? note "简介"
    PlotJuggler，一个基于Qt的应用程序，允许用户加载、搜索和打印数据。许多ROS用户会为此使用MATLAB或rqt_plot，但是当要分析的数据相当大时，使用这些解决方案可能会不尽人意。

    PlotJuggler是rqtplot和rqtbag更好的替代品，它提供了更友好的用户界面。

    - Multiplot(多曲线)：将多条曲线添加到绘图中。在行、列、选项卡和/或单独的窗口中排列绘图。
    - Zoom(缩放)：轻松缩放绘图。可以锁定所有绘图的 X 轴。
    - Save/Load layouts(保存/加载布局)：组织布局后，可以将其保存到文件中以供以后重用。
    - Complete Undo/Redo(完全撤消/重做)：CTRL-Z按您的预期操作。
    - DataLoad plugins(数据加载插件)：轻松加载 CSV 或 rosbags。
    - DataStreaming plugins(数据流插件)：订阅一个或多个 ros 主题并实时绘制它们的数据。
    - RosPublisher plugin(RosPublisher 插件)：使用交互式跟踪器重新发布原始 ROS 消息。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920205340.webp)

```shell
sudo apt-get install ros-noetic-plotjuggler
```

```shell
roscore
rosrun plotjuggler plotjuggler  
```

可以看到如下界面
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920205309.webp)

[教程 | PlotJuggler 绘图工具的安装使用-CSDN 博客](https://blog.csdn.net/qq_39779233/article/details/106478608)

### vrpn

[Pixhawk+PX4+VRPN +NOKOV 无人机飞控平台动捕数据传输\_vrpn 服务器-CSDN 博客](https://blog.csdn.net/MocapLeader/article/details/134463669)

```shell
cd ~/catkin_ws/src
git clone https://github.com/clearpathrobotics/vrpn_client_ros.git

sudo apt-get install ros-noetic-vrpn

cd ~/catkin_ws

catkin_make
```

查看电脑 ip 地址

```shell title="启动"
roslaunch vrpn_client_ros sample.launch server:=192.168.43.195:3883
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920210352.webp)

```shell title="查看"
rostopic echo /vrpn_client_node/<刚体名称>
```

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920210343.webp)

### mavros

```shell
sudo apt-get install ros-noetic-mavros ros-noetic-mavros-extras ros-noetic-control-toolbox

cd /opt/ros/noetic/lib/mavros
sudo ./install_geographiclib_datasets.sh
sudo chmod 777 /dev/ttyACM0
```

```shell
cd real_ws
sudo cp src/mavros_launch_files/px4_pluginlists.yaml /opt/ros/noetic/share/mavros/launch
sudo cp src/mavros_launch_files/px4.launch /opt/ros/noetic/share/mavros/launch
```

启动 mavros，检查是否正常通信：

```shell
roslaunch mavros px4.launch
```

另一个终端

```shell
rostopic hz /mavros/imu/data
```

应该能得到如图所⽰的 50hz imu 数据

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920203808.webp)

## 数学建模

## 仿真

## 代码实现

要编写的控制器部分代码位于`real_ws/src/px4ctrl/src/linear_control.cpp`

其中`computeDesiredCollectiveThrustSignal`函数⽤来根据加速度计算油门百分⽐，在实际过程中通过在线估计参数，这部分不需要同学们实现，只需要给定加速度即可。

另外需要计算的是⽆⼈机的姿态`u.q`。
程序提供了 debug 的接⼝，通过`rostopic`向外发送，可通过`run.sh`中最后一行注释记录`rosbag`，通过`plotjuggler`进行后续分析（详⻅ ros 仿真中的说明）

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920204728.webp)

参数⽂件位于`real_ws/src/px4ctrl/config/ctrl_param_fpv.yaml`，可调节增益参数。

## attention

1. 注意实验安全！！！
2. 四元数、旋转矩阵、欧拉⻆之间的转换
3. 世界系、机体系的坐标变换
4. 建议在实物控制器测试前确保其它模块功能正常

## 调试

移动飞机，查看获得的位姿是否连续光滑

检查动捕球、动捕相机、刚体识别是否都正常

注意小组间区分

### 启动

已经将所有要启动的程序写在⼀个脚本`run.sh`中，只需要⼀键即可启动，但需要先检查各个 ros 节点的 topic 是否正确：

⾸先根据在动捕中创建的刚体名称，修改`src/ekf_pose/launch/PX4_vicon.launch`中接收的位姿 topic

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920203843.webp)

改节点利⽤ EKF 扩展卡尔曼滤波，对 imu 和动捕的数据进⾏融合估计，我们以此结果作为⽆⼈机的里程计信息给到控制器。

随后修改 run.sh 中启动 vrpn 的 ip 为动捕主机的 ip

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20240920204616.webp)

```shell title="编译"
catkin_make
source devel/setup.bash
./run.sh
```

可通过 rqt_graph 来检查各模块间的通讯是否正常。

### 调试方法

- 录 rosbag，记录里程计数据

```shell
rosbag record /sim/odom
```

- plotjuggler 数据分析软件

<https://github.com/facontidavide/PlotJuggler>

## 结果

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Robotics__Robo__assets__Drone_experiment.assets__20241031223517.webp)
