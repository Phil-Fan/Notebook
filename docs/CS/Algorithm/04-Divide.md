# divide and conquer

- 分治法
- 分治法的核心思想是将一个问题分解为若干个子问题，然后递归地解决这些子问题，最后将这些子问题的解合并起来得到原问题的解。
- 分治法的核心思想是将一个问题分解为若干个子问题，然后递归地解决这些子问题，最后将这些子问题的解合并起来得到原问题的解。

- 二分算法

注意二分板子的打法，注意 +1 问题

```c
int l = 0 , r = Count -1 , mid = (l+r) / 2;
while(l < r){ 
    mid = (l+r) / 2;
    if(value <= a[mid])     r = mid;
    else                    l = mid + 1;
}
```

## 二分答案

- **二分答案有==三个步骤（难点）==**

1. 判断这个题是否用到二分这种思想
2. 写判断函数
3. 写二分部分
    - 板子 1——最小值最大
    - 板子 2——最大值最小
4. 分析问题，确定左右半段哪个是符合题意的区间，以及 mid 归属于哪一段
5. 分析结果，选择两种板子

```cpp
mid = (l + r) / 2;
r = mid, l = mid + 1;   //板子 1
```

```cpp
mid = ( l + r + 1) / 2;
l = mid; r = mid - 1;  //板子 2
```

- 判断 mid 的算法==要不要加 1==!!  判断错误就会出现死循环；
（~~建议此步骤在草图画两个小圈圈代表最后两个数，把表达式带进去验证，就可以知道是要不要加 1 了~~ ）
- 二分终止条件是`l == r；`  也是答案所在的位置

!!! example "P1182 数列分段 Section II"

    [网址](https://www.luogu.org/problem/P1182)

    - 初始值是为 1 的，想想为什么？？
    - 因为这种写法是类似于进位的，就是满了给定值，段数就++；所以初始值是 1；

    ```cpp
    #include<iostream>
    #include<cstdio>
    #include<algorithm>//最大值最小 
    using namespace std;
    int a[100005];
    int n,c,mx,tot;
    int jud(int x){
        int cnt = 1,sum=0;//cnt 初始值为 1，思考为什么 
        for(int i = 1; i<= n; i++){
            if(sum+a[i]>x){
                cnt++,sum=a[i];
            }
            else  sum+=a[i];
        }
        return cnt;
    }

    int main(){
        scanf("%d %d",&n,&c);
        for(int i = 1; i <= n; i++){
            scanf("%d",&a[i]);
            mx=max(a[i],mx);
            tot+=a[i];
        }

        int l = mx,r = tot;
        while(l < r){
            int mid = (l+r)/2;
            if(jud(mid)>c) l=mid+1;
            else if(jud(mid)<=c) r=mid; 
        }
        printf("%d",l);
        return 0;
    }
    ```

!!! example "P1873 砍树"

    [网址](https://www.luogu.org/problem/P1873)

    
    ~~一个long long 引发的惨案~~ 
    因为数据范围过大，所以要用long long ！！！
    本蒟蒻多次70分后一气之下全部换成了long long
    - 还有一点就是要学会用`#define` 来代替一些重复且无意义的代码，可以提高代码质量

    ```cpp
    #include<iostream>
    #include<cstdio>
    #include<algorithm>
    #define ll long long
    using namespace std;
    ll a[1000005];
    ll n,c,mx;
    ll jud(ll x){     //砍了多少木头 
        ll sum=0;
        for(ll i = 1; i<= n; i++){
            if(a[i]>x) sum+=a[i]-x; 
        }
        return sum;
    }

    int main(){
        scanf("%lld %lld",&n,&c);
        for(int i = 1; i <= n; i++){
            scanf("%lld",&a[i]);
            mx=max(mx,a[i]); 
        }
    // printf("%d\n",jud(mx));
        ll l = 0,r = mx;
        while(l < r){     //最小值最大模板
            ll mid = (l+r+1)/2;
            if(jud(mid)>=c)  l=mid;
            else if(jud(mid)<c) r=mid-1;
        }
        printf("%lld",l);
        return 0;
    }
    ```

!!! example "P2440 木材加工"

    [网址](https://www.luogu.org/problem/P2440)

    这个题需要注意一下二分部分的写法
    各位大佬有更标准的解法告诉偶一下哦
    ```cpp
    #include<bits/stdc++.h>
    #define ll long long
    using namespace std;
    int a[100005],n,c;
    int jud(ll x){
        int cnt = 0;
        for(int i = 1; i <= n; i++)
            cnt += a[i] / x;
        return cnt;
    }

    int main(){
        scanf("%d %d",&n,&c);
        for(int i = 1; i <= n; i++){
            scanf("%d",&a[i]);
        }
        int l = 0 , r = 210000000;
        while(l < r-1){
            int mid = (l+r)/2;
            if(jud(mid)>=c)   l=mid;
            else if(jud(mid)< c) r= mid;
        }
        printf("%d",l);
        return 0;
    }
    ```

## 经典问题 - 汉诺塔问题

问题描述

## 经典问题 - 树递归

!!! note "问题"

求正整数 n 的分割数，最大部分为 m，即 n 可以分割为不大于 m 的正整数的和，并且按递增顺序排列。例如，使用 4 作为最大数对 6 进行分割的方式有 9 种：

1. 6 = 2 + 4  
2. 6 = 1 + 1 + 4  
3. 6 = 3 + 3  
4. 6 = 1 + 2 + 3  
5. 6 = 1 + 1 + 1 + 3  
6. 6 = 2 + 2 + 2  
7. 6 = 1 + 1 + 2 + 2  
8. 6 = 1 + 1 + 1 + 1 + 2  
9. 6 = 1 + 1 + 1 + 1 + 1 + 1  

我们将定义一个名为 `count_partitions(n, m)` 的函数

**转化方式**

我们可以递归地将使用最大数为 m 的整数分割 n 的问题转化为两个较简单的问题：  
① 使用最大数为 m 的整数分割更小的数字 n-m，  
② 使用最大数为 m-1 的整数分割 n。

**边界条件**

- 整数 0 只有一种分割方式
- 负整数 n 无法分割，即 0 种方式
- 任何大于 0 的正整数 n 使用 0 或更小的部分进行分割的方式数量为 0

```python
def count_partitions(n, m):
    """
    计算使用最大数 m 的整数分割 n 的方式的数量

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
```

!!! note "练习题目"

    Given a positive integer `total`, a set of dollar bills makes change for `total` if the sum of the values of the dollar bills is `total`. Here we will use standard US dollar bill values: 1, 5, 10, 20, 50, and 100. For example, the following sets make change for 15:

    - 15 1-dollar bills
    - 10 1-dollar, 1 5-dollar bills
    - 5 1-dollar, 2 5-dollar bills
    - 5 1-dollar, 1 10-dollar bills
    - 3 5-dollar bills
    - 1 5-dollar, 1 10-dollar bills

    Thus, there are 6 ways to make change for 15. Write a recursive function `count_dollars` that takes a positive integer `total` and returns the number of ways to make change for `total` using 1, 5, 10, 20, 50, and 100 dollar bills.

    Use `next_smaller_dollar` in your solution: `next_smaller_dollar` will return the next smaller dollar bill value from the input (e.g. `next_smaller_dollar(5)` is 1). The function will return `None` if the next dollar bill value does not exist.

    ```python title="count_dollars"
    def next_smaller_dollar(bill) -> int:
        """Returns the next smaller bill in order."""
        if bill == 100:
            return 50
        if bill == 50:
            return 20
        if bill == 20:
            return 10
        elif bill == 10:
            return 5
        elif bill == 5:
            return 1
        
    def count_with_top(total,top) -> int:
        """ Return the number of partition of charge with a maximum of top
        """
        if total == 0:
            return 1
        elif total < 0:
            return 0
        else:
            return count_with_top(total-top,top) + (count_with_top(total,next_smaller_dollar(top)) if top != 1 else 0)
        

    def count_dollars(total) -> int:
        """Return the number of ways to make change.

        >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
        6
        >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
        4
        >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
        10
        >>> count_dollars(45)  # How many ways to make change for 45 dollars?
        44
        >>> count_dollars(100) # How many ways to make change for 100 dollars?
        344
        >>> count_dollars(200) # How many ways to make change for 200 dollars?
        3274
        >>> from construct_check import check
        >>> # ban iteration
        >>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
        True
        """
        return count_with_top(total,100)
    ```

!!! example "P2386 放苹果"
    本题是递归以及递推很经典的一道题
    我们设f(int m,int n)为m个苹果放到n个盘子里面
    这个我们分两种情况
    ！

    当前位置不放苹果那么方案数为f(m,n-1)
    相当于把m个苹果压榨到了n-1个盘子里（空一个盘子给蔡徐坤）
    第2种是该位置放苹果
    那么方案数为f(m-n,n)
    相当于每个盘子拿走一个方案数不变；
