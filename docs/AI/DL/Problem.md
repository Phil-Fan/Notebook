# 深度学习问题记录

## D2l 相关

### module `d2l.torch` has no attribute `train_ch3`

```python title="安装旧版本"
pip install d2l==0.17.5 --user
```

```shell
pip show d2l
```

```python title="train_epoch_ch3 函数"
def train_epoch_ch3(net, train_iter, loss, updater):  #@save
    """训练模型一个迭代周期（定义见第 3 章）"""
    # 将模型设置为训练模式
    if isinstance(net, torch.nn.Module): # isinstance() 用来判断一个对象是否是一个已知的类型
        net.train()
    # 训练损失总和、训练准确度总和、样本数
    metric = Accumulator(3)
    for X, y in train_iter:
        # 计算梯度并更新参数
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            # 使用 PyTorch 内置的优化器和损失函数
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            # 使用定制的优化器和损失函数
            l.sum().backward()
            updater(X.shape[0])
        metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
    # 返回训练损失和训练精度
    return metric[0] / metric[2], metric[1] / metric[2]
```

```python title="evaluate_accuracy 函数"
def evaluate_accuracy(net, data_iter):  #@save
    """计算在指定数据集上模型的精度"""
    if isinstance(net, torch.nn.Module):
        net.eval()  # 将模型设置为评估模式
    metric = Accumulator(2)  # 正确预测数、预测总数
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]
```

```python title="train_ch3"
def train_ch3(net, train_iter, test_iter, loss, num_epochs, updater):  #@save
    #该训练函数将会运行多个迭代周期（由 num_epochs 指定）。在每个迭代周期结束时，利用 test_iter 访问到的测试数据集对模型进行评估。 
    #我们将利用 Animator 类来可视化训练进度。
    """训练模型（定义见第 3 章）"""
    animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                        legend=['train loss', 'train acc', 'test acc'])
    for epoch in range(num_epochs):
        train_metrics = train_epoch_ch3(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        animator.add(epoch + 1, train_metrics + (test_acc,))
    train_loss, train_acc = train_metrics
    assert train_loss < 0.5, train_loss
    assert train_acc <= 1 and train_acc > 0.7, train_acc
    assert test_acc <= 1 and test_acc > 0.7, test_acc
```

## Pytorch

### 如何避免“CUDA 内存不足”

把 batch_size 设置小一点

### mat1 and mat2 must have the same dtype, but got Double and Float

因为输入数据和模型参数的数据类型不匹配。输入数据是 `torch.float64`（也就是`Double`），而模型的参数默认是 `torch.float32`（也就是 `Float`）

```python title="将输入数据转换为 Float 类型"
input_data = input_data.float()  # 将输入数据转换为 Float
```

```python title="将模型参数转换为 Double 类型"
model = YourModel().double()  # 将模型参数转换为 Double
```

### can‘t convert np.ndarray of type numpy.object_. The only supported types are: float6

这是因为 pandas 对象中数据类型是混合的或不是 NumPy 可以直接处理的类型（如字符串或 Pandas 特有的数据类型），则可能不会按预期工作

所以需要先转换成 numpy 数组格式

```python title="转换成 numpy 数组格式"
X = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(outputs.to_numpy(dtype=float))
X, y
```

这样就可以成功了

```python title="另一种"
y = torch.tensor(y.astype(np.float32))
```
