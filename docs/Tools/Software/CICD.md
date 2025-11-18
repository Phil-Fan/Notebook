# CICD

!!! note "Acknowledgements"
    - [来用 GitHub Actions 替代繁琐的工作流吧 | Moear's 主页](https://moeary.github.io/posts/%E6%9D%A5%E7%94%A8GitHub-Actions%E6%9B%BF%E4%BB%A3%E7%B9%81%E7%90%90%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81%E5%90%A7/)

## Github Actions

在你的 GitHub 仓库中，创建一个名为 .github/workflows 的目录。
在该目录中创建一个名为 main.yml 的文件，并添加以下内容：

```yaml
name: CI

on:
push:
    branches:
    - main

jobs:
build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
    uses: actions/checkout@v2

    - name: Set up Node.js
    uses: actions/setup-node@v2
    with:
        node-version: '14'

    - name: Install dependencies
    run: npm install

    - name: Run tests
    run: npm test
```

### 解释工作流文件

- `name`: 工作流的名称。
- `on`: 定义触发工作流的事件。在这个例子中，工作流将在代码推送到主分支时触发。
- `jobs`: 定义工作流中的一个或多个任务。
- `build`: 任务的名称。
- `runs-on`: 指定运行任务的环境。在这个例子中，任务将在最新的 Ubuntu 环境中运行。
- `steps`: 定义任务中的步骤。
- `name`: 步骤的名称。
- `uses`: 使用预定义的 GitHub Actions。
- `run`: 运行特定的命令。

使用 Secrets 管理敏感信息

GitHub Actions 允许你使用 Secrets 来管理敏感信息，如 API 密钥、密码等。你可以在 GitHub 仓库的 Settings -> Secrets and variables -> Actions 中添加 Secrets，然后在工作流中使用它们。

```yaml
name: Use Secrets

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Use secret
      run: echo "My secret is $"
```
