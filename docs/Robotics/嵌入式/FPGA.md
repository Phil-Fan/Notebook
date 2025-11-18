# FPGA

## USRP

## TempestSDR

[martinmarinov/TempestSDR: Remote video eavesdropping using a software-defined radio platform](https://github.com/martinmarinov/TempestSDR)

打开`JavaGUI`，双击`JTempestSDR.jar`

打开`gnuradio-companion`（类似于 matlab 里面的 simulink）

```shell
gnuradio-companion
```

在大约 110 的整数倍会有较清楚的图像

先调频率，再调宽和高

点中间的 auto 获得稳定的图像

先写一个自动播放的脚本

- 系统优化
- 跑实验
- 裁剪图片
- 平衡和滤波;'
- 直方图增强，参数

## x310 配置

UHD
[files.ettus.com:/binaries/images/](https://files.ettus.com/binaries/images/)

```shell
apt list | grep uhd
```

```shell title="查找设备"
uhd_find_devices
```

```shell title=""
uhd_usrp_probe
```

!!! bug "RuntimeError: RuntimeError: Expected FPGA compatibility number 38, but got 39:The FPGA image on your device is not compatible with this host code build.Download the appropriate FPGA images for this version of UHD."
[USRP 2954(X310) 在 ubuntu 系统下版本不兼容的问题\_expected fpga compatibility number 33, but got 39:-CSDN 博客](https://blog.csdn.net/gcc12345678/article/details/132840468)
=== "方法一"

    如果你已经安装好了UHD，那么就只需要从第三步开始，下载镜像并烧录。下载镜像文件有两种方法，第一种就是参考里面的方法，在 [网址](files.ettus.com:/binaries/uhd_stable/latest_release/) 当中选择所需要的版本，如果你是uhd4.1.0,那就选择4.1.0即可。解压下载好的压缩文件，打开文件夹下的目录/host/utils，然后右键选择在终端中打开，输入ls即可看到所有文件，再输入
    
    ```shell
    sudo uhd_images_downloader
    ```
    
    即可下载USRP的镜像bit,然后进行镜像的烧录.

    默认目录会在终端当中有提示，我的在`/usr/local/share/uhd`，如果是安装在默认位置，就运行以下命令进行烧录：

    ```shell
    uhd_image_loader --args="type=x300,addr=192.168.10.3,fpga=HG"
    ```

    注意在运行之前，先输入`uhd_find_devices`查看ip地址；

    如果没有在默认位置，就运行：

    ```shell
    uhd_image_loader --args="type=x300,addr=192.168.10.2" --fpga-path="<path_to_images>/usrp_x310_fpga_HG.bit"
    ```

    其中<path_to_images>就是路径。

=== "方法 2"

    https://files.ettus.com/binaries/cache/x3xx/，在这个网站里面选择对应版本的FPGA镜像，直接下载，解压后采用非默认位置的烧录命令进行烧录，不过这种方法我还不知道怎么判断所需版本，我是试了两个就可以了。

    注意：烧录完之后需要重启2954再运行gnuradio。
