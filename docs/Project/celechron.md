# Celechron

## 什么是 Celechron

![GitHub Stars](https://img.shields.io/github/stars/Celechron/Celechron) ![GitHub License](https://img.shields.io/github/license/Celechron/Celechron) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Celechron/Celechron) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Celechron/Celechron) ![GitHub contributors](https://img.shields.io/github/contributors/Celechron/Celechron)

Celechron 是 [iotang](https://github.com/iotang) 和 [n0sig](https://github.com/n0sig) 发起的一个服务于浙大学生的时间管理工具，前身是一个 SQTP 项目。提供任务规划、本研课表查看、成绩查询、付款码展示等功能。

![feature](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125100646716.webp)

![task](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125100709320.webp)

Celechron iOS 支持两种桌面小组件：日程小组件和付款码小组件：

![widget](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125100738688.webp)

Android 支持付款码小组件：

![Android](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125100754638.webp)

### OSS Project Checklist

- **Stars**: ![GitHub Stars](https://img.shields.io/github/stars/Celechron/Celechron)
- **Lisence**: 项目采用 GPL-3.0 开源协议，源代码已开源在 [GitHub](https://github.com/Celechron/Celechron) 上。
- **Version**: 在 17 个版本，269 次提交后，项目完成在 App Store 的上线。

    ![app store](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125100325182.webp)

  - 2024-01-23 [Celechron：服务于浙大学生的时间管理器 - CC98 论坛](https://www.cc98.org/topic/5807824)
  - 2025-06-11 [Celechron iOS 版现已上架 App Store！ - CC98 论坛](https://www.cc98.org/topic/6211431)

- **Contributors**: 项目目前共有 11 位 contributors，其中 iotang 和 n0sig 是项目的核心开发者。
    ![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125095836379.webp)
- **Activity**
    ![issues](https://img.shields.io/github/issues/Celechron/Celechron) ![closed issues](https://img.shields.io/github/issues-closed/Celechron/Celechron) ![pull requests](https://img.shields.io/github/issues-pr/Celechron/Celechron) ![closed pull requests](https://img.shields.io/github/issues-pr-closed/Celechron/Celechron)

## 技术栈

### Flutter

**Flutter 是 Celechron 的核心框架**，用于构建跨平台的 iOS 和 Android 应用。

Flutter 的主要特点：

- **真正跨平台一致的 UI**：Celechron 的界面在 iOS / Android 表现一致且流畅。
- **高性能渲染引擎（Skia）**：60fps+ 的交互体验，适合课表、日程等复杂界面。
- **由 Widget 构建 UI**：组件化结构清晰，方便扩展和维护。
- **丰富的生态插件**：在 Celechron 中大量使用
- **热重载（Hot Reload）**：提升开发效率，使 UI 调整和交互调试更快。

### 小组件

小组件部分则采用平台原生代码，在 iOS 上使用 Swift UI，Android 上使用 Jetpack Glance。

### 我使用到的一些软件和工具

- [Xcode](https://developer.apple.com/xcode/)
- [Android Studio](https://developer.android.com/studio)
- [Cursor](https://www.cursor.so/)
- [录屏](https://support.apple.com/zh-cn/guide/mac-help/mh26782/mac)
- [Apple Developer Forums](https://developer.apple.com/forums/)
- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Flutter 文档](https://docs.flutter.cn/get-started)

## Features

| 名称 | PR | 相关 Issue |
|---|---|---|
| 日程同步至系统日历 | [![PR 69](https://img.shields.io/badge/PR-69-brightgreen)](https://github.com/Celechron/Celechron/pull/69) | [![issue 10](https://img.shields.io/badge/issue-10-red)](https://github.com/Celechron/Celechron/issues/10) [![issue 48](https://img.shields.io/badge/issue-48-red)](https://github.com/Celechron/Celechron/issues/48) |
| 日程支持 iCal 格式导出 | [![PR 69](https://img.shields.io/badge/PR-69-brightgreen)](https://github.com/Celechron/Celechron/pull/69) | [![issue 66](https://img.shields.io/badge/issue-66-red)](https://github.com/Celechron/Celechron/issues/66) |
| 课程主修绩点计算 | [![PR 73](https://img.shields.io/badge/PR-73-brightgreen)](https://github.com/Celechron/Celechron/pull/73) | — |
| 获取二三课堂分数 | [![PR 91](https://img.shields.io/badge/PR-91-brightgreen)](https://github.com/Celechron/Celechron/pull/91) | — |
| 支持百分制绩点显示 | [![PR 101](https://img.shields.io/badge/PR-101-brightgreen)](https://github.com/Celechron/Celechron/pull/101) | [![issue 39](https://img.shields.io/badge/issue-39-red)](https://github.com/Celechron/Celechron/issues/39) |
| 课程加权绩点计算 | [![PR 120](https://img.shields.io/badge/PR-120-brightgreen)](https://github.com/Celechron/Celechron/pull/120) | — |

## UI/UX

| 名称 | PR | 相关 Issue |
|---|---|---|
| 期中考试增加强调字样 | [![PR 114](https://img.shields.io/badge/PR-114-purple)](https://github.com/Celechron/Celechron/pull/114) | — |
| 任务界面添加滑动手势：完成/重启/删除 | [![PR 104](https://img.shields.io/badge/PR-104-purple)](https://github.com/Celechron/Celechron/pull/104) | [![issue 11](https://img.shields.io/badge/issue-11-red)](https://github.com/Celechron/Celechron/issues/11) |
| 日程界面增加课表入口 | [![PR 117](https://img.shields.io/badge/PR-117-purple)](https://github.com/Celechron/Celechron/pull/117) | — |
| 绩点隐藏 | [![PR 73](https://img.shields.io/badge/PR-73-purple)](https://github.com/Celechron/Celechron/pull/73) | — |
| 退出登录二次确认弹窗 | [![PR 95](https://img.shields.io/badge/PR-95-purple)](https://github.com/Celechron/Celechron/pull/95) | [![issue 11](https://img.shields.io/badge/issue-11-red)](https://github.com/Celechron/Celechron/issues/11) |
| Contributors 页面动态更新 | [![PR 89](https://img.shields.io/badge/PR-89-purple)](https://github.com/Celechron/Celechron/pull/89) | — |
| 付款码刷新按钮 | [![PR 103](https://img.shields.io/badge/PR-103-purple)](https://github.com/Celechron/Celechron/pull/103) | [![issue 102](https://img.shields.io/badge/issue-102-red)](https://github.com/Celechron/Celechron/issues/102) [![issue 67](https://img.shields.io/badge/issue-67-red)](https://github.com/Celechron/Celechron/issues/67) |

## Bug Fix

| 名称 | PR | 相关 Issue |
|---|---|---|
| 修复本研课程互通导致的课程信息抓取问题 | [![PR 97](https://img.shields.io/badge/PR-97-red)](https://github.com/Celechron/Celechron/pull/97) | — |
| iCal 导出适配 iPad | [![PR 100](https://img.shields.io/badge/PR-100-red)](https://github.com/Celechron/Celechron/pull/100) | [![issue 81](https://img.shields.io/badge/issue-81-red)](https://github.com/Celechron/Celechron/issues/81) |
| 修复 `setState() called during build` 错误 | [![PR 112](https://img.shields.io/badge/PR-112-red)](https://github.com/Celechron/Celechron/pull/112) | — |
| 修复课程名称过长导致课表显示不全的问题 | [![PR 117](https://img.shields.io/badge/PR-117-red)](https://github.com/Celechron/Celechron/pull/117) | — |
| 雪灾浙大：修复助教布置作业依然显示为待办的错误 | [![PR 125](https://img.shields.io/badge/PR-125-red)](https://github.com/Celechron/Celechron/pull/125) | [![issue 82](https://img.shields.io/badge/issue-82-red)](https://github.com/Celechron/Celechron/issues/82) |
| 修复所有现存 lint error | — | — |

## 效果

- 版本号更新到 v1.1.0，两个相关帖子登上 CC98 十大：
  - [Celechron 更新至 1.1.0：增加系统日历同步/ iCal 导出/绩点隐藏/学年主修/大一付款码 - CC98 论坛](https://www.cc98.org/topic/6331383)
  - [调研一下大家想增加的 Celechron 功能，以及偷跑几个我最近写的 Celechron 的新 feature - CC98 论坛](https://www.cc98.org/topic/6345259)
- 已提交 PR 16，已合并 PR 3

## 未来开发计划

- Bug
  - [![bug-issue 124](https://img.shields.io/badge/bug-issue%20124-red)](https://github.com/Celechron/Celechron/issues/124) 系统日历同步功能在安卓系统有同步问题
  - [![bug-issue 106](https://img.shields.io/badge/bug-issue%20106-red)](https://github.com/Celechron/Celechron/issues/106) 系统日历中的上课位置需要映射成更详细的地址
  - [![bug-issue 96](https://img.shields.io/badge/bug-issue%2096-red)](https://github.com/Celechron/Celechron/issues/96) v1.1.0 在 macOS 不可用
- Feature
  - [![feat-issue 122](https://img.shields.io/badge/feat-issue%20122-green)](https://github.com/Celechron/Celechron/issues/122) 增加对于 PTA 平台的支持
  - [![feat-issue 121](https://img.shields.io/badge/feat-issue%20121-green)](https://github.com/Celechron/Celechron/issues/121) 增加对于浙大体艺的支持
  - [![feat-issue93](https://img.shields.io/badge/feat-issue%2093-green)](https://github.com/Celechron/Celechron/issues/93) 付款码支持 iWatch 小组件
  - [![feat-issue 83](https://img.shields.io/badge/feat-issue%2083-green)](https://github.com/Celechron/Celechron/issues/83) 增加作业详情界面
- Refactor
  - [![refactor-issue 127](https://img.shields.io/badge/refactor-issue%20127-blue)](https://github.com/Celechron/Celechron/issues/127) 重构 calendar2sys 以支持所有 Period 类型的同步
- UI/UX
  - [![UI-issue 99](https://img.shields.io/badge/UI-issue%2099-purple)](https://github.com/Celechron/Celechron/issues/99) 本科生研究生互相选课，在课程详情界面做不同标记
- Ops
  - [![ops-issue 118](https://img.shields.io/badge/ops-issue%20118-lightgrey)](https://github.com/Celechron/Celechron/issues/118) 增加 Log 一键上传错误，更方便错误定位与修复
- Question
  - [![question-issue 123](https://img.shields.io/badge/question-issue%20123-green)](https://github.com/Celechron/Celechron/issues/123) 是否会重新上架 TestFlight 内测，以放出一些比较新但是并不稳定的功能

## 开发故事

我算是 Celechron 的第一批用户吧，第一次看到 Celechron 的时候就下载使用了。当时还用的是 Testflight 内测版本。

- 提了 [![issue-10](https://img.shields.io/badge/issue-10-red)](https://github.com/Celechron/Celechron/issues/10)，但是当时由于对相关的工具掌握的太少，之前尝试了一个小 flutter demo 也不是特别成功，所以就一直没有实现
    ![issue 10](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/20251125105541159.webp)
- 9 月的时候发现原先的项目 `ical.top` 由于钉钉去掉了课表页面，故无法正常使用，所以花了一些时间学习，在 AI 的帮助下学习了工具链的使用，开发了初版，在和 maintainer 讨论的过程中修改了部分 bug

总结下来就是

- **从我的需求痛点出发，先解决了我自己的使用问题**
- 解决社区当中提到的 Issue 问题
- 进行一些用户调研，根据调研结果进行功能迭代
