# Dart & Flutter

## 安装

```shell
brew install cocoapods
```

```shell title="verify"
pod
```

```shell
brew tap dart-lang/dart
brew install dart
brew tap flutter/flutter
brew install flutter
```

```shell title="verify"
flutter doctor
```

```shell title="代理问题"
export NO_PROXY=localhost,127.0.0.1,::1,192.168.0.0/16
```

## 常用 Flutter 命令

### 环境与设备

- 检查环境配置：

  ```bash
  flutter doctor
  ```

- 查找连接的设备：

  ```bash
  flutter devices
  ```

### 项目管理

- 安装项目依赖：
  
  ```bash
  flutter pub get
  ```

- 运行项目（调试模式）：
  
  ```bash
  flutter run
  ```

  ```bash title="指定设备"
  flutter run -d xxx[device_id]
  ```

### 构建 Release 版本

在发布应用前，请确保你已经根据官方文档配置好了应用签名（Android）和开发者证书（iOS）。

#### Android

- **构建 App Bundle (推荐，用于发布到 Google Play)**:

  ```bash
  flutter build appbundle --release
  ```

  *产物路径：`build/app/outputs/bundle/release/app-release.aab`*

- **构建 APK (用于直接分发)**:
  为了减小体积，建议为不同 CPU 架构生成独立的 APK。

  ```bash
  flutter build apk --split-per-abi
  ```

  *产物路径：`build/app/outputs/apk/release/`*

- **构建通用 APK (不推荐，体积较大)**:

  ```bash
  flutter build apk --release
  ```

#### iOS (需在 macOS 上)

- **构建 IPA (用于发布到 App Store)**:

  ```bash
  flutter build ipa
  ```

  *构建前需在 Xcode 中配置好证书与签名。*

#### Web

- **构建 Web 应用**:

  ```bash
  flutter build web
  ```

  *产物路径：`build/web`*

#### 桌面应用 (Desktop)

- **macOS**: `flutter build macos --release`
- **Windows**: `flutter build windows --release`
- **Linux**: `flutter build linux --release`

这些命令可以帮助你为不同平台构建和发布 Flutter/Dart 项目。

## Dart
