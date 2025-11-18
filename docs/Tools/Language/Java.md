# Java

## 简介

## 安装

在下面的网址进行下载

<https://www.oracle.com/java/technologies/downloads/>

```shell title="解压"
sudo tar -xvzf yourfile.tar.gz -C /usr/lib/jvm/
```

```shell title="更改环境变量"
export JAVA_HOME=/usr/lib/jvm/jdk-21.0.8
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

```shell title="验证安装"
$ java --version


java 21.0.8 2025-07-15 LTS
Java(TM) SE Runtime Environment (build 21.0.8+12-LTS-250)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.8+12-LTS-250, mixed mode, sharing)
```

### MacOS

```bash title="用 Homebrew 安装"
# 安装 OpenJDK 17
brew install openjdk@17

# 安装 OpenJDK 21（可选）
brew install openjdk@21

# 其他版本（例如 Corretto 11，已经装过的话可跳过）
brew install --cask corretto11
```

安装完成后，JDK 会放在：

* Homebrew 默认目录：
  `/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home`
* Amazon Corretto:
  `/Library/Java/JavaVirtualMachines/amazon-corretto-11.jdk/Contents/Home`

```bash title="系统自带查询（确认 JDK 安装情况）"
/usr/libexec/java_home -V
```

会列出所有已安装的 JDK。

```bash title="安装 jenv"
brew install jenv
```

```bash title="把 jenv 添加到 shell 配置文件"
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(jenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

```bash title="把 JDK 添加到 jenv"
jenv add /Library/Java/JavaVirtualMachines/amazon-corretto-11.jdk/Contents/Home
jenv add /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home
```

```bash title="查看 jenv 管理的版本"
jenv versions
```

示例输出：

```shell
* system (set by /Users/you/.jenv/version)
  11
  11.0
  11.0.26
  corretto64-11.0.26
  17
  17.0
  17.0.12
  openjdk64-17.0.12
```

5️⃣ 切换 JDK 版本

* **全局切换（对所有项目生效）**

  ```bash
  jenv global 17
  ```

* **本地切换（只对当前项目生效）**
  进入项目目录后执行：

  ```bash
  jenv local 11
  ```

  会生成 `.java-version` 文件。

* **临时切换（只在当前终端会话生效）**

  ```bash
  jenv shell 17
  ```

```bash title="验证"
java -version
javac -version
```

输出应该和 jenv 设置一致。

这样就不用每次手动找路径了。

## 使用

### `.jar`文件打开方式

1. 双击打开
2. 命令行打开 x

```shell
java -jar xxx.jar
```

```shell title="后台执行"
java -jar xxx.jar &
```

```shell title="不挂断执行"
nohup java -jar test_jar-1.0-SNAPSHOT.jar &   
```  

nohup 意思是不挂断运行命令，当账户退出或终端关闭时，程序仍然运行。

当用 nohup 命令运行 jar 包时，缺省情况下该应用的所有输出被重定向到 nohup.out 的文件中，除非另外指定了输出文件。
