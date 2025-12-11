# IOS 开发

!!! note "记录一下学习 IOS 开发的尝试"

## 安装

## 注册开发者账号

## 第一个环境构建

1.

bundle indentifier 随便写一个

如果是用的别人的项目，关掉自动

Unable to read contents of XCFileList '/Target Support Files/Pods-**/Pods-**-frameworks-Debug-output-files.xcfilelist

```shell
sudo gem update cocoapods --pre
pod update
```

```shell title="在 xcode 当中重新建立"
clean
build
```

## 如何连接手机

使用 usb 线连接电脑和手机

在手机“通用 - vpn 与设备管理”处，信任开发者 APP

## 如何发布内测

### 使用模拟器

```shell title="打开模拟器"
xcrun simctl create "iPhone 15" "iPhone 15" "iOS18.5"
xcrun simctl list devices
xcrun simctl boot 36291DE5-5BCF-4C05-A4E2-B1AE812D35C2
```

- 第一个 "iPhone 15"：你自定义的模拟器名称。
- 第二个 "iPhone 15"：设备类型（必须是 Xcode 支持的设备型号，如 iPhone 15, iPad (10th generation)）。
- 第三个 "iOS18.5"：指定模拟器使用的系统 runtime（对应 Xcode 已安装的 Simulator runtime）。

也可以在 xcode 中，product - destination - simulator - 选择新加一个设备

```shell title="打开模拟器"
open -a Simulator
```

## Safari Extension

- [Safari web extensions | Apple Developer Documentation](https://developer.apple.com/documentation/safariservices/safari-web-extensions)
- [如何开发一个 Safari 插件 | 今是昨非的博客](https://morganwang.cn/2023/06/07/%E5%A6%82%E4%BD%95%E5%BC%80%E5%8F%91%E4%B8%80%E4%B8%AASafari%E6%8F%92%E4%BB%B6/)
