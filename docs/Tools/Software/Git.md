# Git

## 使用

### 个人使用：init、rm、commit、push、pull

```shell
git init
git remote -v
git remote add origin + ssh
git remote rm origin 

git pull origin [branch]:[master]
git add .
git commit -m ""
git push origin [master]:[branch]

# 本地初始化项目
git config --global user.name "你的名字或昵称"
git config --global user.email "你的邮箱"
```

### 分支操作

```shell
# 创建分支、更改
git checkout -b <branch_name>
git branch -a
git branch -d <branch_name> //删除分支
```

```shell title="删除远端分支"
git push origin --delete <branch_name>
```

### 回退

```shell title="查看详细历史记录"
git log
```

```shell
git log --pretty=oneline
```

格式化 log 形式，每条 log 只有一行，只包含 完整的 hash 值 和 提交的备注；

```shell title="只展示最新的几条日志"
git log -n 3
```

```shell title="展示历史分支路线"
git log --graph
```

```shell title="回退任意版本"
git reset --hard + commit_id
```

```shell
git reset --hard HEAD^ 
```

只能后退，一个 ^ 表示回退一个版本，两个^ 表示回退两个版本，依次类推

```shell title="回退 n 个版本"
git reset --hard HEAD~n
```

### Tag

```bash title="创建轻量标签"
git tag v1.0.0
```

```bash title="创建含信息标签"
git tag -a v1.0.0 -m "Release version 1.0.0"
```

```bash title="推送单个标签"
git push origin v1.0.0
```

```bash title="推送所有本地标签"
git push origin --tags
```

```bash title="删除本地标签"
git tag -d v1.0.0
```

```bash title="删除远端标签"
git push origin --delete v1.0.0
```

```bash title="删除远端标签"
git push origin :refs/tags/v1.0.0
```

### Pull Request

PR，全称 Pull Request（拉取请求），是一种非常重要的协作机制

![Merge Request](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__Git.assets__20240926134813.webp)

1. fork 原仓库 A 到我的仓库 B（B 是 A 的 fork 版本）
2. 将仓库 B clone 到我本地电脑
3. 在本地创建一个分支，如 bugfix/issue-12，该分支用于存放我的代码修改。同时在我的 github 上的仓库 B 也创建一个同名的该分支
4. 切换到该分支 bugfix/issue-12，修改代码
  
```shell
git checkout -b bugfix/issue-12
```

1. 修改好了，add，commit，然后 push 到我远程的仓库 B 的 bugfix/issue-12 分支

```shell
git push -u origin bugfix/issue-12
```

1. 在我的 github 的仓库 B 中创建 pull request。选择仓库 B 的该分支，推送到原仓库 A 的某一个分支。具体是哪个分支，参考仓库 A 的 contributing 说明，一般是 dev 分支；如果没说，就只能选择 master 分支咯

[【Git】PR 是啥？一篇文章学会 Pull Request 到底是干嘛的\_github pull request-CSDN 博客](https://blog.csdn.net/Supreme7/article/details/136813376)

### `git commit`规范

为了方便使用，我们避免了过于复杂的规定，格式较为简单且不限制中英文：

```txt title="commit 规范"
<type>(<scope>): <subject>
// 注意冒号 : 后有空格
// 如 feat(miniprogram): 增加了小程序模板消息相关功能
```

**scope 选填**表示 commit 的作用范围，如数据层、视图层，也可以是目录名称

**subject 必填**用于对 commit 进行简短的描述

 **type 必填**表示提交类型，值有以下几种：

- feat - 新功能 feature
- fix - 修复 bug
- docs - 文档注释
- style - 代码格式 (不影响代码运行的变动)
- refactor - 重构、优化 (既不增加新功能，也不是修复 bug)
- perf - 性能优化
- test - 增加测试
- chore - 构建过程或辅助工具的变动
- revert - 回退
- build - 打包

## 合并

### 合并 commit

#### git rebase 合并最近 N 个 commit

```shell
git rebase -i HEAD~N
```

### squash 写法（关键）

```text
pick   <commit1>
squash <commit2>
squash <commit3>
```

**规则：第一个必须是 pick，后面才能 squash**

### 操作流程

1. `git rebase -i HEAD~N`
2. 保留第一个 pick，其余改成 squash
3. 保存退出
4. 编辑最终 commit message
5. `git rebase --continue`

### merge vs rebase vs squash

| 方式       | 本质     | 历史形态       | 是否改历史 | 什么时候用         |
| -------- | ------ | ---------- | ----- | ------------- |
| `merge`  | 两条线合并  | 有 merge 节点 | 否     | 公共分支、安全第一     |
| `rebase` | 把提交挪位置 | 一条直线       | 是     | 整理个人提交        |
| `squash` | 多个变一个  | 一条直线       | 是     | 提 PR / 上 main |

### 放弃本地修改，强制覆盖

```shell title="快速使用云端"
# 1. 放弃本地所有修改（包括未提交的、冲突的）
git reset --hard HEAD

# 2. 拉取远程最新版本，强制覆盖本地
git fetch origin
git reset --hard origin/main

# 3. 清理未跟踪文件
git clean -fd

# 现在本地与云端完全一致
```

## 进阶

### Pre-Commit

[Git 技巧：Pre-commit-CSDN 博客](https://blog.csdn.net/Topsort/article/details/140965269)

[pre-commit 钩子 中文](https://pre-commit.git-scm.cn/)

### submodule

```shell title="添加子模块"
git submodule add <repo-url> <path>
```

这会在你的 repo 中生成：

- `.gitmodules` 文件
- <path> 目录（但内部是一个独立 Git 仓库）

```shell title="初始化并克隆子模块"
git submodule update --init --recursive
```

```shell title="更新子模块指向的版本"
git pull origin main
```

```shell title="回到主仓库提交新的指针"
cd ..
git add .
git commit -m "update yyy submodule"
```

```shell title="删除子模块（必须完整删除）"
git submodule deinit -f third_party/yyy
git rm -f <path>
rm -rf .git/modules/<path>
```

## 配置

### git 的安装

### 创建个人令牌

[github 创建个人令牌](https://blog.csdn.net/qq_46941656/article/details/119737804)  

```txt
Setting 
-> Developer settings
-> Personal access tokens 
-> Generate new token 保存密码到自己可以看到的位置 
```

### 免密登陆

[git 保存密码](https://cloud.tencent.com/developer/article/2207770)

``` shell
# 记住密码 
git config --global credential.helper store  
# 删除密码 
git config --global --unset credential.helper 
```

### github 配置 ssh

```shell
cd ~
ssh-keygen -t rsa -C "xxx@xxx.com" # 这里输入你的邮箱
cd .ssh
cat id_rsa.pub # 复制到 github 的 ssh 设置中
```

![ssh key](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__Git.assets__20240816111626.webp)
点击右上角的 settings
![ssh key](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__Git.assets__20240816111700.webp)

将刚才复制的内容粘贴到这里

验证是否成功

```shell
ssh -T git@github.com
```

显示如下信息表明设置成功
![ssh key](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Software__assets__Git.assets__20240816111807.webp)

### SSH

- 连接虚拟机

[win 系统使用 vscode 连接虚拟机](https://blog.csdn.net/qq_40300094/article/details/114639608)

```shell
ifconfig #记录 ip 地址 
ssh user.name@ip 
```

#### 设置 ssh 免密登录  

在 win 主机上`ssh-keygen`生成一对公私钥，将公钥发送到服务器的`~/.ssh/authorized_keys`文件下  

在 win 主机上的 ssh 配置中加入`IdentityFile`文件，即可实现免密登录  

[理解公钥和私钥](https://zhuanlan.zhihu.com/p/113522792)

### git 代理

```shell title="代理的配置"
#http 代理
git config --global http.proxy 'http://127.0.0.1:7890'
#https 代理
git config --global https.proxy 'http://127.0.0.1:7890'
#http 代理
git config --global http.proxy 'socks5://127.0.0.1:7890'
#https 代理
git config --global https.proxy 'socks5://127.0.0.1:7890'
 
#取消 http 代理
git config --global --unset http.proxy
#取消 https 代理
git config --global --unset https.proxy
```

### .gitignore 的配置

有时候不想要`.git`,`.DS_Store` 等文件，那么就需要在`.gitignore`中写清楚

```shell
git rm -r --cached .DS_Store
git rm -r --cached **/.DS_Store
```

## 原理

missing semester

[版本控制 (Git) · the missing semester of your cs education](https://missing-semester-cn.github.io/2020/version-control/)

[6. Lecture 6 - 版本控制 git\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1Tp4y1H7jr/?p=6&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

## 问题与解决

### 连接不上 `port 443 Couldn‘t connect to server`

- 方案一：关闭 VPN
- 方案二：取消代理

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### 拒绝连接 `connect to host github.com port 22: Connection refused`

- 使用`github 443` 端口

给`~/.ssh/config`文件里添加如下内容，这样 ssh 连接 GitHub 的时候就会使用 443 端口。

```txt title="~/.ssh/config"
Host github.com
  Hostname ssh.github.com
  Port 443
```

- `https`和`git`链接换着试试

```txt title="git config"
url = https://github.com/username/repo.git
url = git@github.com:username/repo.git
```

- 换梯子节点，检查 DNS 污染

### 推送失败 `src refspec master does not match any`

按照下面的顺序执行

```shell
git commit -m "init"
git remote add origin xxxxxxxx.git
git push -u origin master
```

### 远端链接失败 `fatal: Couldn‘t find remote ref master`

````shell
# 检查本地配置
git config user.name/git config --global user.name
git config user.email/git config --gloabl user.email

# 检查仓库配置
git remote -v
git remote rm origin
git remote add origin XXXX
````

### 文件过大 `RPC failed；curl 56 Recv failure: Connection was reset`

```shell
git config --global http.postBuffer 524288000
```

如果设置之后提交还是报错的话，可能是因为某几个文件过大造成的；

这时就需要用到 git-lfs 具体用法见[官网](https://git-lfs.github.com/)

```shell
git lfs install
git lfs track "*.so"
git add .gitattributes
```

### Host key verification failed

重新配置一下 ssh，删除`~/.ssh`文件夹，重新生成 ssh key，然后再次连接。

具体操作看`配置/github 配置ssh`一节
