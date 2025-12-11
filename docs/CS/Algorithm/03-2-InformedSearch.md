# 启发式搜索

启发函数（Heuristic Function）：$h(n)=$ 从节点 n 代表的状态到目标状态的路径耗散的最小估计值

g(n) 描述了从起点到当前节点的耗散，h(n) 描述了从当前节点到终点的预估耗散

## 贪婪最佳优先搜索

$$
f(n) = h(n)
$$

## A*搜索

[A 搜索算法求解八数码问题（人工智能导论）](https://www.bilibili.com/video/BV1xG4y1N7VR)

[A\*寻路算法详解 #A 星](https://www.bilibili.com/video/BV1bv411y79P/)

A \* 搜索算法（英文：A\*search algorithm，A \* 读作 A-star），简称 A \* 算法，是一种在图形平面上，对于有多个节点的路径求出最低通过成本的算法。它属于图遍历（英文：Graph traversal）和最佳优先搜索算法（英文：Best-first search），亦是 BFS 的改进。

### 过程

定义起点 $s$，终点 $t$，从起点（初始状态）开始的距离函数 $g(x)$，到终点（最终状态）的距离函数 $h(x)$，$h^{\ast}(x)$，以及每个点的估价函数

$$
f(x)=g(x)+h(x)
$$

A \* 算法每次从优先队列中取出一个 $f$ 最小的元素，然后更新相邻的状态。

如果 $h\leq h^*$（不高估计到达目标的最低路径耗散值)，则 A \* 算法能找到最优解。

上述条件下，如果 $h$ 满足三角形不等式，则 A \* 算法不会将重复结点加入队列。

当 $h=0$ 时，A \* 算法变为 Dijkstra；当 $h=0$ 并且边权为 $1$ 时变为 BFS。

### 例题

???+ note "[八数码](https://www.luogu.com.cn/problem/P1379)"
    题目大意：在 $3\times 3$ 的棋盘上，摆有八个棋子，每个棋子上标有 $1$ 至 $8$ 的某一数字。棋盘中留有一个空格，空格用 $0$ 来表示。空格周围的棋子可以移到空格中，这样原来的位置就会变成空格。给出一种初始布局和目标布局（为了使题目简单，设目标状态如下），找到一种从初始布局到目标布局最少步骤的移动方法。

    ```plain
        123
        804
        765
    ```

??? note "解题思路"
    $h$ 函数可以定义为，不在应该在的位置的棋子个数。

    容易发现 $h$ 满足以上两个性质，此题可以使用 A \* 算法求解。

## 爬山法

!!! note "不断与邻居节点的值比较，并选择值更高的节点作为下一个迭代的节点"

- 算法**不会考虑与当前状态不相邻的状态，不维护搜索树**

```text
Step 1: 评估当前的初始状态。如果是目标状态，则返回并退出。

Step 2: 如果当前状态不是目标状态，则循环运行，直到找到解决方案或没有其他操作可比较。

Step 3: 选择一个新状态进行比较。

Step 4: 评估新状态：
    - 如果是目标状态，即最高峰，则退出。
    - 如果它比当前状态好，则使其成为新的当前状态。
    - 如果不是比当前状态更好，请转到步骤 2。
```

### 存在**局部最优的问题**

- 解决方法：每次不一定选择邻域内最优的点，而是依据一定概率从邻域内选择一个点：**指标函数优的点被选中的概率大，指标函数差的点被选中的概率小**

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106193129.webp)

!!! tip "爬山算法的优势在于当正解的写法你并不了解（常见于毒瘤计算几何和毒瘤数学题），或者本身状态维度很多，无法容易地写分治时，可以通过非常暴力的计算得到最优解"

### 存在**步长选取的问题**

- 解决方法：变步长

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106193153.webp)

爬山算法一般会引入温度参数（类似模拟退火）。类比地说，爬山算法就像是一只兔子喝醉了在山上跳，它每次都会朝着它所认为的更高的地方（这往往只是个不准确的趋势）跳，显然它有可能一次跳到山顶，也可能跳过头翻到对面去。不过没关系，兔子翻过去之后还会跳回来。显然这个过程很没有用，兔子永远都找不到出路，所以在这个过程中兔子冷静下来并在每次跳的时候更加谨慎，少跳一点，以到达合适的最优点。

兔子逐渐变得清醒的过程就是降温过程，即温度参数在爬山的时候会不断减小。

关于降温：降温参数是略小于 1 的常数，一般在 [0.985, 0.999] 中选取。

### 存在**起始点的问题**

- 解决方法：随机生成一些初始点，从每个初始点出发进行搜索，找到各自的最优解。再从这些最优解中选择一个最好的结果作为最终结果

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106193221.webp)

## 模拟退火法 | Simulated Annealing

>[模拟退火 - OI Wiki](https://oi-wiki.org/misc/simulated-annealing/)

!!! note "如果新状态的解更优则修改答案，否则以一定概率接受新状态"

1. **初始解：** 随机选择一个初始解，并设置初始温度。
2. **迭代过程：**

   - 在当前解的邻域中随机选择一个新的解。
   - 计算新解的能量（或成本）与当前解的能量之差$\Delta E$。
   如果新解的能量更低（$\Delta E<0$），则接受该新解；如果新解的能量更高，则以一定概率接受该解

3. **退火：** 逐步降低温度，通常使用冷却调度（如指数冷却）来控制温度的下降。
4. **终止条件：** 算法在达到预设的迭代次数或温度低于某一阈值时终止。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106154900.webp)

### Metropolis 准则

$$
P(\text{accept}) = \begin{cases}
1 & \text{if } E(N+1) < E(N) \leq 0 \\
e^{-\frac{\Delta f}{T}} & \text{if } E(N+1) \ge E(N) 0
\end{cases}
$$

- $P(\text{accept})$ 是接受新解的概率。
- 新解如果更优就直接接受，新解如果没有更优就以一定概率接受。
- $T$ 是当前的温度。

### 退火参数

一开始初始温度较高，使的所有转移状态都被接受。初始温度越高，获得高质量的解的概率越大，耗费的时间越长。

随着迭代次数增加，温度逐渐降低（使用类似指数衰减函数）。转移概率逐渐减小。

如果温度下降到终止温度或者达到用户设定的阈值，则退火完成。

- $T(n) = \lambda T(n-1)$, $\lambda$ 是降温系数，一般取值在 0.8-0.99 之间。
- $T(n ) =\frac{T_0}{log(1+t)}$
- $T(n) = \frac{T_0}{1+t}$

### 分析

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__simulated-annealing.gif)

随着温度的降低，跳跃越来越不随机，最优解也越来越稳定

### 例子

$$
f_7(X) = 4x_1^2 - 2.1x_1^4 + \frac{x_1^6}{3} + x_1x_2 - 4x_2^2 + 4x_2^4, \quad |x_i| \leq 5
$$

其最优状态和最优值为

$$
\min(f_7(X^*)) = f_7(0.08983, -0.7126) = f_7(-0.08983, 0.7126) = -1.0316285
$$

```python title="模拟退火算法例子"
import math
from random import random
import matplotlib.pyplot as plt

def func(x, y): #x 为公式里的 x1,y 为公式里面的 x2
    res= 4*x**2-2.1*x**4+x**6/3+x*y-4*y**2+4*y**4
    return res

class SA:
    def __init__(self, func, iter=100, T0=100, Tf=0.01, alpha=0.99):
        self.func = func
        self.iter = iter         # 内循环迭代次数，即为 L=100
        self.alpha = alpha       # 降温系数，alpha=0.99
        self.T0 = T0             # 初始温度 T0 为 100
        self.Tf = Tf             # 温度终值 Tf 为 0.01
        self.T = T0              # 当前温度
        self.x = [random() * 11 -5  for i in range(iter)] #x in [-5,5],随机生成 100 个 x 的值
        self.y = [random() * 11 -5  for i in range(iter)] #y in [-5,5],随机生成 100 个 y 的值
        self.most_best =[] # 最优解
        self.history = {'f': [], 'T': []} # 记录最优解和温度

    def generate_new(self, x, y):   #扰动产生新解的过程
        while True:
            x_new = x + self.T * (random() - random())
            y_new = y + self.T * (random() - random())
            if (-5 <= x_new <= 5) & (-5 <= y_new <= 5):  
                break # 重复得到新解，直到产生的新解满足约束条件
        return x_new, y_new 

    def Metrospolis(self, f, f_new):   #Metropolis 准则
        if f_new <= f:
            return 1
        else:
            p = math.exp((f - f_new) / self.T)
            if random() < p:
                return 1
            else:
                return 0

    def best(self):    #获取最优目标函数值
        f_list = []    #f_list 数组保存每次迭代之后的值
        for i in range(self.iter):
            f = self.func(self.x[i], self.y[i])
            f_list.append(f)
        f_best = min(f_list)
        
        idx = f_list.index(f_best)
        return f_best, idx    #f_best,idx 分别为在该温度下，迭代 L 次之后目标函数的最优解和最优解的下标

    def run(self):
        count = 0
        
        while self.T > self.Tf: # 外循环迭代，当前温度小于终止温度的阈值     
            for i in range(self.iter): # 内循环迭代 指定次数
                f = self.func(self.x[i], self.y[i])                    #f 为迭代一次后的值
                x_new, y_new = self.generate_new(self.x[i], self.y[i]) #产生新解
                f_new = self.func(x_new, y_new)                        #产生新值
                if self.Metrospolis(f, f_new):                         #判断是否接受新值
                    self.x[i] = x_new             #如果接受新值，则把新值的 x,y 存入 x 数组和 y 数组
                    self.y[i] = y_new
            # 迭代 L 次记录在该温度下最优解
            ft, _ = self.best()
            self.history['f'].append(ft)
            self.history['T'].append(self.T)
            self.T = self.T * self.alpha   # 温度按照一定的比例下降（冷却）     
            count += 1
            
            # 得到最优解
        f_best, idx = self.best()
        print(f"F={f_best}, x={self.x[idx]}, y={self.y[idx]}")

sa = SA(func)
sa.run()

plt.plot(sa.history['T'], sa.history['f'])
plt.title('SA')
plt.xlabel('T')
plt.ylabel('f')
plt.gca().invert_xaxis()
plt.show()
```

random() 这个函数取 0 到 1 之间的小数
如果你要取 0-10 之间的整数（包括 0 和 10）就写成 (int)random()*11 就可以了，11 乘以零点多的数最大是 10 点多，最小是 0 点多
该实例中 x1 和 x2 的绝对值不超过 5（包含整数 5 和 -5），（random()* 11 -5）的结果是 -6 到 6 之间的任意值（不包括 -6 和 6）
（random() * 10 -5）的结果是 -5 到 5 之间的任意值（不包括 -5 和 5），所有先乘以 11，取 -6 到 6 之间的值，产生新解过程中，用一个 if 条件语句把 -5 到 5 之间（包括整数 5 和 -5）的筛选出来。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106192331.webp)

## 遗传算法

蚂蚁在路径上释放信息素。后到的蚂蚁沿信息素浓度高的路径行走。
在所有可能的路径中，由于往返最短路径花的时间少，通过频率高，所以信息素浓度高。这又会吸引更多蚂蚁走这条路径，形成正反馈。

每只蚂蚁只关心局部的信息

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106200900.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__03-2-InformedSearch.assets__20241106200625.webp)

- 编码和初始群体生成
- 群体评价
- 个体选择
- 交换和变异

与传统优化算法的不同：

- 并非直接作用在参变量集上而是利用参变量集的某种编码
- 不是从单个点，而是从一个点的群体开始搜索
- 利用适应值信息，无须导数或其他辅助信息
- 利用概率转移规则，而非确定性规则

优越性：

- 不易陷入局部最优
- 算法具有并行性，适合大规模并行计算机

## 常见问题

### 八皇后问题

### TSP | 旅行商问题

??? example "例子——可拆分的 TSP"

    ```python title="需求可拆分"
    class Ant:
        def __init__(self, num_customers, num_vehicles, capacity, demands):
            self.num_customers = num_customers
            self.num_vehicles = num_vehicles
            self.capacity = capacity
            self.routes = [[] for _ in range(num_vehicles)]
            self.route_num = 1
            self.route = [[] for _ in range(num_vehicles)]
            self.loads = [0] * num_vehicles
            self.demands = demands
            self.visited = set()

        def add_route(self):
            self.route.append([])

        def add_customer_to_route(self, route_num, customer):
            while len(self.route) <= route_num:
                self.add_route()
            self.route[route_num].append(customer)

        def visit_customer(self, vehicle, customer):
            self.routes[vehicle].append(customer)
            self.add_customer_to_route(self.route_num, customer)
            demand = self.demands[customer]  # 调整索引以适应需求数组
            if (self.capacity - self.loads[vehicle] >= demand):  # 如果车够空，全都装掉
                self.loads[vehicle] += demand
                self.demands[customer] = 0
            else:  # 如果不空，装满为止
                self.demands[customer] -= (self.capacity - self.loads[vehicle])
                self.loads[vehicle] = self.capacity
            self.visited.add(customer)

        def can_visit(self, vehicle, customer):
            return (self.loads[vehicle] < self.capacity)

        def return_to_depot(self, vehicle):
            self.routes[vehicle].append(0)
            self.add_customer_to_route(self.route_num, 0)
            self.route_num += 1
            self.loads[vehicle] = 0


    class ACO:
        def __init__(self, num_customers, num_vehicles, capacity, demands, distance_matrix, num_ants, num_iterations,
                    alpha=1, beta=5, evaporation_rate=0.3):
            self.num_customers = num_customers
            self.num_vehicles = num_vehicles
            self.capacity = capacity
            self.demands = demands
            self.distance_matrix = distance_matrix
            self.num_ants = num_ants
            self.num_iterations = num_iterations
            self.alpha = alpha
            self.beta = beta
            self.evaporation_rate = evaporation_rate
            self.pheromone_matrix = np.ones((num_customers + 1, num_customers + 1))
            self.best_routes = None
            self.best_distance = 10000000
            self.dis = []

        def plot_best_distances(self): # 绘制收敛曲线
            plt.plot(range(1, self.num_iterations + 1), self.dis)
            plt.xlabel('Iteration')
            plt.ylabel('Best Distance')
            plt.title('Best Distance vs Iteration')
            plt.grid(True)
            plt.savefig('../result/three_eva_rate_aco_convergence.png')
            plt.show()


        def run(self):
            for iteration in range(self.num_iterations):
                # print(iteration)
                ants = [Ant(self.num_customers, self.num_vehicles, self.capacity, copy.deepcopy(demands)) for _ in
                        range(self.num_ants)]
                for ant in ants:
                    self.construct_solution(ant)
                    distance = self.calculate_total_distance(ant.routes)
                    if distance < self.best_distance:
                        self.best_distance = distance
                        self.best_routes = ant.routes
                self.dis.append(self.best_distance)
                self.update_pheromones(ants)
                # print(f'Iteration {iteration + 1}/{self.num_iterations}, Best distance: {self.best_distance}')

            return self.best_routes, self.best_distance

        def construct_solution(self, ant):
            for vehicle in range(self.num_vehicles):
                current_customer = 0  # 从仓库开始
                # print(ant.demands.values())
                while any(idemand > 0 for idemand in ant.demands.values()):
                    # print(ant.demands.values())
                    next_customer = self.select_next_customer(ant, current_customer)
                    # print(current_customer,next_customer)
                    if next_customer is not None:
                        if ant.can_visit(vehicle, next_customer):
                            ant.visit_customer(vehicle, next_customer)
                            current_customer = next_customer
                        else:  # 返回仓库卸货
                            ant.return_to_depot(vehicle)
                            current_customer = 0  # 返回仓库
                    else:
                        ant.return_to_depot(vehicle)  # 确保车辆最终返回仓库
                        current_customer = 0
                # print(ant.routes)
                # break  # 没有更多客户可以访问

        def select_next_customer(self, ant, current_customer):
            probabilities = []
            for customer in range(0, self.num_customers + 1):
                if ant.demands.get(customer, 0) == 0 or customer == current_customer:
                    continue
                pheromone = self.pheromone_matrix[current_customer][customer] ** self.alpha
                visibility = (1.0 / self.distance_matrix[current_customer][customer]) ** self.beta
                probabilities.append((pheromone * visibility, customer))

            if not probabilities:
                return None

            total_prob = sum(prob for prob, customer in probabilities)
            if total_prob == 0:
                return None

            probabilities = [(prob / total_prob, customer) for prob, customer in probabilities]
            rand = np.random.random()
            cumulative_prob = 0.0

            for prob, customer in probabilities:
                cumulative_prob += prob
                if rand <= cumulative_prob:
                    return customer

            return None

        def calculate_total_distance(self, routes): # 根据路径列表计算最短路径的长度
            total_distance = 0
            for route in routes:
                if route:
                    distance = 0
                    # print("route", route)
                    for i in range(len(route) - 1):
                        distance += self.distance_matrix[route[i]][route[i + 1]]
                    distance += self.distance_matrix[route[-1]][0]  # 返回仓库
                    distance += self.distance_matrix[0][route[0]]
                    total_distance += distance
            return total_distance

        def update_pheromones(self, ants):
            self.pheromone_matrix *= (1 - self.evaporation_rate)
            for ant in ants:
                distance = self.calculate_total_distance(ant.routes)
                for route in ant.routes:
                    for i in range(len(route) - 1):
                        self.pheromone_matrix[route[i]][route[i + 1]] += 1.0 / distance
                    if route:
                        self.pheromone_matrix[route[-1]][route[0]] += 1.0 / distance  # 返回仓库
    ```
