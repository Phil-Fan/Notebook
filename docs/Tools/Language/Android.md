# Android

## 安装

### 安装 Android SDK

1. **下载 CLI 工具**

   * 链接：[https://developer.android.com/studio#command-tools](https://developer.android.com/studio#command-tools)
   * 选择对应系统（Windows / macOS / Linux）。

2. **解压并设置环境变量**

    ```shell
    export ANDROID_SDK_ROOT=~/Android/Sdk
    export PATH=$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$PATH
    export PATH=$ANDROID_SDK_ROOT/platform-tools:$PATH
    ```

    解压之后把文件移动到`~/Android/Sdk/cmdline-tools/latest`目录下

    ```shell title="期望的目录结构"
    <SDK_ROOT>/
    └─ cmdline-tools/
        └─ latest/
            ├─ bin/
            ├─ lib/
            └─ ...
    ```

3. **使用 sdkmanager 管理 SDK**

   * 查看可用包：

       ```bash
       sdkmanager --list
       ```

   * 安装指定版本：

       ```bash
       sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"
       ```

   * 更新所有已安装包：

       ```bash
       sdkmanager --update
       ```

    | 命令                                  | 作用                |
    | ----------------------------------- | ----------------- |
    | `sdkmanager --list`                 | 查看可用 SDK 和已安装 SDK |
    | `sdkmanager "platform-tools"`       | 安装 platform-tools |
    | `sdkmanager "platforms;android-33"` | 安装 Android 33 平台  |
    | `sdkmanager --update`               | 更新所有已安装的 SDK 包    |
    | `avdmanager list avd`               | 查看已创建模拟器          |
    | `avdmanager create avd`             | 创建新的模拟器           |

### 安装 Android Studio

1. **下载 Android Studio**

   * 官方网站：[https://developer.android.com/studio](https://developer.android.com/studio)
   * 安装时勾选 **Android SDK** 和 **Android SDK Platform-Tools**。

2. **SDK 管理**

   * 打开 Android Studio → `Preferences` / `Settings` → `Appearance & Behavior` → `System Settings` → `Android SDK`
   * 在这里你可以：

     * 下载不同版本的 **SDK Platform**
     * 下载 **SDK Tools**（如 adb、emulator、NDK、CMake）
     * 设置 SDK 路径（默认在：

       * macOS/Linux: `~/Library/Android/sdk`
       * Windows: `C:\Users\<用户名>\AppData\Local\Android\Sdk`）

3. **更新 SDK**

   * 在 SDK 管理界面直接勾选更新项 → 点击 `Apply` 更新即可。

## 使用

### 创建模拟器

**1. 确认环境变量**

假设 Android SDK 路径在 `~/Library/Android/sdk`（macOS/Linux）或 `C:\Users\<username>\AppData\Local\Android\Sdk`（Windows）：

```bash
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools
```

> Windows 使用 `setx` 或在系统环境变量里添加相同路径。

**2. 查看可用系统镜像**

Android 系统镜像是创建 AVD 的基础：

```bash
sdkmanager --list | grep "system-images;"
```

你会看到类似：

```text
system-images;android-33;google_apis;x86_64
system-images;android-33;google_apis_playstore;x86_64
```

> 选择一个适合的镜像，比如 `android-33;google_apis;x86_64`

**3. 安装系统镜像**

```bash
sdkmanager "system-images;android-33;google_apis;x86_64"
```

**4. 创建 AVD**

```bash
avdmanager create avd -n Pixel6_API33 -k "system-images;android-33;google_apis;x86_64" --device "pixel_6"
```

参数说明：

* `-n Pixel6_API33` → 模拟器名字
* `-k "..."` → 系统镜像
* `--device "pixel_6"` → 设备型号（`avdmanager list device` 可以查看可用设备）

创建完成后，会生成一个模拟器配置。

**5. 启动模拟器**

```bash
emulator -avd Pixel6_ARM33
```

* 启动成功后，Flutter 就能检测到：

```bash
flutter devices
flutter run
```
