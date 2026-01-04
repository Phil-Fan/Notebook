# ROS 操作

## 系统烧录

[balenaEtcher 已经烧录的 u 盘恢复](https://blog.csdn.net/A___LEi/article/details/117700660)

```shell
wget http://fishros.com/install -O fishros && . fishros
```

[小鱼的一键安装系列 | 鱼香 ROS](https://fishros.org.cn)

!!! note "no directory"
    切换到`bash`使用 可以把 `. fishros` 替换成 `bash fishros`

注意安装 desktop 版本而不是 sever 版本

```shell title="测试代码"
roscore
rosrun turtlesim turtlesim_node
rosrun turtlesmi turtle_teleop_key
```

## 软件安装

### PlotJuggler 画图工具

```shell
sudo apt-get install ros-noetic-plotjuggler 
```

```shell
roscore
rosrun plotjuggler plotjuggler  
```

然后通过 `File–>Load Data` 导入`CSV`或`rosbags`数据，然后把对应的 topic 数据拖到右侧就可以了。
![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__ROS.assets__1e5581845afc87ff9dad1d79a4b33643.gif)
如果加载 `.bag` 文件的时候不支持加载 `.bag` 文件，那么需要安装包`ros-noetic-plotjuggler-ros`

```shell
sudo apt-get install ros-kinetic-plotjuggler-ros
```

### htop 系统监控工具

```shell
sudo apt-get install htop
```

## `ROS`操作

### 创建

```shell title="启动"
roscore
```

```shell title="创建工作空间"
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```

``` shell title="编译"
cd ~/catkin_ws
catkin_make
```

如果出现时间问题

- 删除`devel`与`build`文件夹
- 先进入系统设置调整时区
-

### 执行

| 命令       | 重要度 | 详细说明 |
|------------|--------|----------|
| `rosrun`   | ★★★    | 运行节点 |
| `roslaunch`| ★★★    | 运行多个节点及设置运行选项 |
| `rosclean` | ★★☆    | 检查或删除 ROS 日志文件 |

### topic

| 命令              | 详细说明                         |
|-------------------|----------------------------------|
| `rostopic bw`     | 测量消息发布所占用的带宽         |
| `rostopic delay`  | 显示话题中消息的延迟             |
| `rostopic echo`   | 查看某个话题上发布的消息         |
| `rostopic find`   | 按类型查找话题                   |
| `rostopic hz`     | 测量消息发布的频率               |
| `rostopic info`   | 获取更多关于话题的信息           |
| `rostopic list`   | 获取当前活跃的话题               |
| `rostopic pub`    | 发布数据到话题                   |
| `rostopic type`   | 打印话题类型                     |

```shell title="查看活动话题"
rostopic list
```

```shell title="查看话题信息"
rostopic info /topic_name
```

```shell title="查看话题消息"
rostopic echo /topic_name
```

```shell title="查看特定话题的消息字段和数据类型"
rostopic type <topic_name> | rosmsg show
```

将<topic_name>替换为你要查看的话题名称，该命令将显示该话题消息的字段和数据类型。

### 查看信息

#### rosmsg

```shell
rosmsg  show
```

#### service

```shell title="查看 service 列表"
rosservice list
```

```shell title="调用 service"
rosservice call [service] [args]
```

```shell title="查看 service 格式并显示数据"
rosservice type [service] | rossrv show
```

```shell title="设置 service parameter"
rosparam set [parame_name] [args] + rosservice call clear
```

```shell title="获得 parameter"
rosparam get [parame_name]
```

```shell title="加载 parameter"
rosparam load [file_name] [namespace]
```

```shell title="删除 parameter"
rosparam delete
```

#### bag

会在当前目录下生成一个`bag.active`文件，说明正在记录数据；按`Ctrl+C`停止记录，生成`bag`文件。

```shell title="记录所有 topic"
rosbag record -a
```

```shell title="记录某些 topic"
rosbag record -O subset <topic1> <topic2>
```

```shell title="查看信息"
rosbag info <bagfile_name>
```

```shell title="回放"
rosbag play (-r 2) <bagfile_name>
```

### 功能包

`rosinstall`安装 ROS 附加功能

## 可视化

### rviz

- rviz 操作：平移，2d，视角转换，家

### rqt

输入

```shell
rosrun rqt_graph rqt_graph

rosrun rqt_plot rqt_plot
```

可以打开一个界面观察节点与话题的关系 绿色和蓝色的是节点 红色的是话题

## 外设

### 风扇

风扇安装与控制

```shell
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
sudo vi /etc/rc.local
sudo chmod 755 /etc/rc.local
```

```shell
#!/bin/bash
sleep 10
sudo /usr/bin/jetson_clocks
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
```

### 摄像头

```shell
#查看摄像头
rqt_image_view
```

### 蓝牙

[jetson nano 之 (6):配置蓝牙音响 – 走着的博客 (openpilot.cc)](https://blog.openpilot.cc/archives/2307)
[英伟达 Jetson Nano 新手必备：连接蓝牙音频_jetson nano 链接音响_许野平的博客-CSDN 博客](https://blog.csdn.net/quicmous/article/details/115174779)

### 激光雷达

```shell
#gmapping slam
roslaunch clbrobot bringup.launch
roslaunch clbrobot lidar_slam.launch

#hector slam
roslaunch clbrobot bringup.launch
roslaunch clbrobot hector_slam.launch
rviz
open "slam.rviz"
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
roscd clbrobot/maps/
./map.sh

#Karto SLAM
roslaunch clbrobot bringup.launch
roslaunch clbrobot karto_slam.launch
rviz
open "slam.rviz"
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

#Cartographer SLAM 算法构建地图
roslaunch clbrobot bringup.launch
roslaunch clbrobot rplidar.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
roslaunch clbrobot cartographer_slam.launch
rviz
open config "cartographer.rviz"
```

??? note "jetson Nano 小车"
    ```shell
    #查看ip地址
    ifconfig

    #底盘
    roslaunch clbrobot bringup.launch

    #键盘操控
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py
    小写 & 大写字母

    #imu校正
    roslaunch clbrobot bringup.launch
    rosrun imu_calib do_calib
    按照提示调整小车，并按照指示按下enter

    #线速度修正
    roslaunch clbrobot bringup.launch
    rosrun clbrobot_nav calibrate_linear.py
    rosrun rqt_reconfigure rqt_reconfigure
    设定1m，最后一栏记录实际值，多次实验平均
    roscd clbrobot/launch
    gedit bringup.launch

    #角速度修正
    roslaunch clbrobot bringup.launch
    rosrun clbrobot_nav calibrate_angular.py
    rosrun rqt_reconfigure rqt_reconfigure


    #雷达启动


    #相机启动
    roslaunch clbrobot camera.launch
    roslaunch clbrobot clbrobot_web.launch
    IP:8080

    #相机建图
    roslaunch clbrobot bringup.launch

    roslaunch clbrobot astra_xtion_gmapping.launch
    rviz
    打开 home/catkin_ws/src/clbrobot_project/clbrobot/rviz/slam.rviz
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py
    roscd clbrobot/maps
    ./map.sh

    #相机导航
    roslaunch clbrobot bringup.launch
    roslaunch clbrobot astra_navigate.launch
    rviz
    nav goal

    #避障
    roslaunch clbrobot bringup.launch
    roslaunch clbrobot_follower follower.launch

    #手机
    roslaunch clbrobot bringup.launch
    roslaunch clbrobot camera.launch
    roslaunch clbrobot lidar_slam.launch
    roscd clbrobot/maps
    ./map.sh

    #巡线
    roslaunch clbrobot bringup.launch
    roslaunch clbrobot camera.launch
    roslaunch clbrobot_line_follower clbrobot_line.launch


    #二维码识别
    roslaunch clbrobot bringup.launch
    roslaunch clbrobot camera.launch

    roslaunch clbrobot_ar_track clbrobot_ar_camera.launch
    roslaunch clbrobot_ar_track clbrobot_ar_large_markers.launch
    roslaunch clbrobot_ar_track clbrobot_ar_tags_cog.launch
    roslaunch clbrobot_ar_track clbrobot_ar_follower.launch

    #多点导航
    roslaunch clbrobot bringup.launch
    roslaunch clbrobot navigate.launch
    rviz
    open "navigate.rviz"

    use "2D Pose Estimate"
    use "Publish Point" to choose dots to be passed


    roslaunch clbrobot_hand_pose clbrobot_hand_pose.launch
    roslaunch clbrobot_object_detect clbrobot_face_object.launch  
    ```

## 三方库

### darknet

```shell
catkin_make -DCATKIN_WHITELIST_PACKAGES="darknet_ros"

roslaunch clbrobot bringup.launch
roslaunch clbrobot camera.launch
roslaunch darknet_ros darknet_ros.launch
roscd darknet_ros/script
python ObjectLocation.py

roslaunch clbrobot astra_navigate.launch
```

[darknet-yolov3 训练自己的数据集，并测试训练结果_dota 数据集在 yolov3 训练结果_pd 很不专业的博客-CSDN 博客](https://blog.csdn.net/qq_42145185/article/details/105816128)

[Jetson Nano 之 ROS 入门 -- YOLO 目标检测与定位_ros 目标检测_szu_ljm 的博客-CSDN 博客](https://blog.csdn.net/m0_55202222/article/details/132016297)

### 语音合成

[ROS 实战 ( 三 ) 利用科大讯飞 tts 实现 ROS 下语音合成播报_无驰复逸的博客-CSDN 博客](https://blog.csdn.net/weixin_40522162/article/details/80525758)
