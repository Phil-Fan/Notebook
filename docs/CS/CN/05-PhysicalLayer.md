# 物理层 | Physical Layer

转换成物理信号

传统：IP 协议、路由协议

SDN：数据平面、控制平面（操作系统

流表的形式下发

第零层

media

Manchester 编码

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CN__assets__05-PhysicalLayer.assets__image-20240217170722040.webp" alt="image-20240217170722040" style="zoom:33%;" />

 在 10BaseT 中使用
 每一个 bit 的位时中间有一个**信号跳变**

避免一直是一马平川的信号

 允许在接收方和发送方节点之间进行时钟同步
 节点间不需要集中的和全局的时钟
 10Mbps，使用 20M 带宽，效率 50%

每四个 bit 插入一个跳变用于时钟同步，用五位代替四位

4b5b 编码

多出来的编码相当于打节拍
