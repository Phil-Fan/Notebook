# Kubernetes

## 安装

### 安装 kubectl

```shell
sudo apt-get update
# apt-transport-https 可以是一个虚拟包；如果是这样，你可以跳过这个包
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
```

```shell title="添加 Kubernetes GPG 密钥"
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.34/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring   
```

```shell title="添加 Kubernetes 稳定仓库"
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.34/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # 有助于让诸如 command-not-found 等工具正常工作
```

```shell title="更新 APT 包索引"
sudo apt-get update
sudo apt-get install -y kubectl
```

### 安装 minikube

[minikube start | minikube](https://minikube.sigs.k8s.io/docs/start/)

```shell title="下载 minikube"
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_arm64.deb
sudo dpkg -i minikube_latest_arm64.deb
```

```shell title="添加用户到 docker 组"
sudo usermod -aG docker $USER && newgrp docker
```

```shell title="启动 minikube"
minikube start
```

```shell title="验证安装"
kubectl cluster-info
```

```shell title="验证节点"
kubectl get nodes
```

应该看到类似下面的输出：

```shell
NAME       STATUS   ROLES    AGE   VERSION
minikube   Ready    control-plane   1m    v1.30.0
```

## 部署验证 —— 部署第一个应用

### Deployment

先创建一个 Deployment 文件：

`nginx-deploy.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

```shell title="部署 Deployment"
kubectl apply -f nginx-deploy.yaml
```

```shell title="查看 Pod"
kubectl get pods -l app=nginx
```

你应该看到类似：

```shell
nginx-5c68965b8f-bvzfm   1/1   Running   0   10s
nginx-5c68965b8f-k92lg   1/1   Running   0   10s
```

### Service

创建文件：

`nginx-svc.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```

部署：

```shell title="部署 Service"
kubectl apply -f nginx-svc.yaml
```

查看：

```shell title="查看 Service"
kubectl get svc
```

你会看到：

```shell
nginx-svc   NodePort   ...   80:30080/TCP
```

### 访问

```shell title="直接访问"
curl http://localhost:30080
```

```shell title="使用 minikube 提供的内置代理"
minikube service nginx-svc
```

它会自动打开浏览器访问。

### 滚动更新（Rolling Update）

修改 Deployment，将镜像改为：

```yaml
image: nginx:1.21.0
```

重新 apply：

```shell title="重新 apply"
kubectl apply -f nginx-deploy.yaml
```

```shell title="查看 rollout 进度"
kubectl rollout status deployment/nginx
```

```shell title="回滚"
kubectl rollout undo deployment/nginx
```

## 调试

查看 Pod 日志：

```shell title="查看 Pod 日志"
kubectl logs nginx-xxxxxx
```

```shell title="进入 Pod"
kubectl exec -it nginx-xxxxxx -- bash
```

```shell title="查看 Pod 的详细信息"
kubectl describe pod nginx-xxxxxx
```

最常用来排查镜像拉取失败、CrashLoopBackOff 等。

```shell title="删除 Deployment"
kubectl delete deployment nginx
```

## 初始化

## 层级与命名空间

### Kubernetes 对象层级

| 层级 | 说明 | 示例 |
| --- | --- | --- |
| Cluster | 整个 Kubernetes 控制平面与节点集合 | `minikube`、生产集群 |
| Namespace | Cluster 内的逻辑隔离边界 | `default`、`kube-system`、`rbgs-test` |
| Workload/Resource | 以 YAML 定义的 Kubernetes 对象 | Deployment、Service、RoleBasedGroup |
| Pod | 最小运行单元，真正承载容器 | 运行 `nginx` 的 Pod |

### RoleBasedGroup 的 namespace

- `RoleBasedGroup`（缩写 `rbg`）属于 `workloads.x-k8s.io/v1alpha1` 的 CRD，作用类似一个“多角色工作负载控制器”。
- 若 YAML `metadata` 中未声明 `namespace`，对象创建时会默认落在 `default` 命名空间；可用以下命令核对：

```bash
kubectl get rbg -n default
kubectl get rolebasedgroup -n default
```

### RBG 与底层 Workload 的关系

```text
Cluster
└─ Namespace (e.g., default)
     └─ RoleBasedGroup
          ├─ Role "sts" → StatefulSet → Pods
          ├─ Role "deployment" → Deployment → Pods
          └─ Role "lws" → LeaderWorkerSet → Pods
```

- RBG 自身不会直接运行容器，而是交给对应 controller 创建各 Role 的 Deployment / StatefulSet / LeaderWorkerSet，再由这些对象拉起 Pod。
- 每个 Role 共享所在 Namespace，因此同一个 RBG 下的所有衍生资源也归属于 RBG 的命名空间。

### 关键理解

1. RBG 是顶层 CRD 资源，属于 Workload 层级，并受 Namespace 约束。
2. Namespace 是逻辑分组，除非 CRD 声明为 `ClusterScope`，否则所有实例都需要 namespace。
3. 想查看 RBG 创建的角色状态，直接查询对应的 Deployment/StatefulSet，或使用 `kubectl describe rbg/<name>` 追踪 controller 事件。

删除 Service：

```shell title="删除 Service"
kubectl delete svc nginx-svc
```

```shell title="删除整个 Minikube 集群"
minikube delete
```

## 进阶原理

### 调度器（Scheduler）

当你创建一个 Pod 或 Deployment 时：

```shell title="部署 Deployment"
kubectl apply -f xxx.yaml
```

K8s 的 scheduler 会将 Pod 分配到一个合适的 Node。

```text title="调度过程"
Pending → (scheduler) → Node assigned → kubelet 启动容器
```

如果调度失败，Pod 会卡住：

```text
Pending
```

调度器的三步流程（非常重要）

=== "① 过滤（Filtering）"

    排除掉不满足条件的节点，比如：

    * 节点资源不足（CPU / 内存 / GPU）
    * 有污点（taint）
    * 不匹配 nodeSelector
    * 不匹配 affinity
    * 端口冲突
    * 节点 not ready

    例如 GPU Pod：

    ```yaml
    resources:
    limits:
        nvidia.com/gpu: 1
    ```

    → scheduler 只会考虑有 GPU 的节点。

=== "② 打分（Scoring）"

    在筛选后的节点上打分：

    * CPU、内存利用率
    * 负载均衡
    * 网络拓扑
    * anti-affinity
    * 自定义调度插件

    得分最高的节点被选中。

=== "③ 绑定（Binding）"

    最后 scheduler 调用：

    ```shell title="POST /binding"
    POST /binding
    ```

    把 Pod 绑定到节点。

K8s 允许你表达复杂的调度需求：

#### Gang Scheduling

大模型并行（Tensor Parallel）必须多个 Pod 同时启动。
普通 scheduler 不支持这种逻辑，会造成死锁：

- 4 卡模型：需要 4 个 worker
- 但调度器调到 2 个卡后剩余卡不足 → 永远 Pending

解决方案：

- PodGroup（CRD）
- Volcano Scheduler
- RBG 内部集成

### StatefulSet —— 有状态应用的核心机制

StatefulSet 出现就是为了解决 Deployment 不能解决的 3 个问题：

| 能力           | Deployment | StatefulSet         |
| ------------ | ---------- | ------------------- |
| Pod 固定名称     | ❌          | ✔（nginx-0, nginx-1） |
| 稳定持久化存储      | ❌          | ✔（PVC 自动绑定）         |
| Headless DNS | ❌          | ✔                   |
| 有序创建/删除      | ❌          | ✔                   |

**StatefulSet** 的 Pod 命名

```shell title="StatefulSet 的 Pod 命名"
app=redis
```

Pod 不会叫`redis-xxxxxx`
而是`redis-0`、`redis-1`、`redis-2`。

顺序固定不变。

StatefulSet 必须配合 Headless Service：

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis
spec:
  clusterIP: None
  selector:
    app: redis
```

这样每个 Pod 会有独立的 DNS：

```text
redis-0.redis.default.svc.cluster.local
redis-1.redis.default.svc.cluster.local
```

分布式系统（如 Etcd、Zookeeper、Redis Sentinel）都要用它。

**有序滚动更新**

StatefulSet 必须按顺序更新：

```text
redis-2 → redis-1 → redis-0
```

最适合：

- 数据库
- leader/follower 系统
- 分布式本地存储

---

### HPA (Horizontal Pod Autoscaler)

HPA = 自动横向扩容

目标——根据负载自动增加/减少 Pod 数

```shell title="基于 CPU 扩缩容"
kubectl autoscale deployment nginx --cpu-percent=50 --min=1 --max=10
```

K8s 会读取`metrics-server`：

```text title="公式"
当前副本数 * (当前 CPU 使用率 / 目标 CPU 使用率)
```

对 LLM 服务更有意义：

- qps
- request in queue
- pending tokens
- KV cache 使用量

需要`Prometheus Adapter`，并在 HPA 中定义：

```yaml
type: Pods
metric:
  name: queue_length
target:
  type: AverageValue
  averageValue: 10
```

### CRD（Custom Resource Definition）—— 自定义资源

K8s 是一个高度可扩展系统。
你可以自定义一个新的**资源类型**：

```shell title="查看自定义资源"
kubectl get <myresource>
```

一个**CRD**定义类似：

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: podgroups.scheduling.sigs.k8s.io
spec:
  group: scheduling.sigs.k8s.io
  names:
    kind: PodGroup
    plural: podgroups
  scope: Namespaced
  versions:
  - name: v1alpha1
    served: true
    storage: true
```

安装后，K8s 会有新的资源：

```shell title="查看自定义资源"
kubectl get podgroups
```

### Operator

Operator = Controller + CRD

目的：把复杂系统的运维逻辑自动化

Operator 会持续检测资源：

```text title="流程"
Desired State（CRD YAML）
→
Controller reconcile loop
→
Actual State 实现
```

```text
watch(crd) → reconcile() → 更新 pod / config / svc / pvc
```

这就是 K8s 的自愈机制扩展到 Custom Resource。

| 能力          | 用途           |
| ----------- | ------------ |
| 调度器         | 控制 Pod 运行在哪  |
| StatefulSet | 分布式有状态系统     |
| HPA         | 自动扩缩容        |
| CRD         | 拓展 K8s API   |
| Operator    | 自动化复杂 LLM 服务 |

## 进阶实践
