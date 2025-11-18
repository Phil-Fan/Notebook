# Intro

放一些常见语言环境以及版本管理的工具安装过程。

使用频率并不是很高，但是每次都得重新安装一下，不如一遍梳理清楚

## 语言与工具链

| 语言       |笔记  | 运行时 / 编译器          | 包管理工具              | 版本管理工具        | 构建工具               | 测试框架 |
| ---------- | ------------------ | ------------------ | ------------- | ------------------ | ------------------- | ------------------ |
| C / C++    | [Makefile](Makefile.md) | gcc, clang, MSVC   | vcpkg, conan       | 系统依赖          | make, CMake        | Google Test, Catch2 |
| Python     | [Python](Python.md) | CPython, PyPy      | pip, conda, poetry | pyenv, conda  | setuptools, wheel  | pytest, unittest    |
| Ruby       | [Ruby](Ruby.md) | MRI, JRuby         | RubyGems + Bundler | rbenv, RVM    | Rake               | RSpec, Minitest     |
| Java       | [Java](Java.md) | JVM                | Maven, Gradle      | jenv, SDKMAN! | Maven, Gradle, Ant | JUnit, TestNG       |
| JavaScript | [JavaScript](JavaScript.md) | Node.js, Deno, Bun | npm, yarn, pnpm    | nvm, volta    | webpack, vite      | jest, mocha         |
| Dart       | [Dart](Dart.md) | Dart              | pub             | dartenv        | -                  | -             |
| Go         |  | go (编译器 + 运行时)       | go mod             | -             | go build           | go test             |
| Rust       |  | rustc              | cargo              | rustup        | cargo              | cargo test          |
| PHP        |  | Zend Engine        | Composer           | phpenv        | -                  | PHPUnit             |
