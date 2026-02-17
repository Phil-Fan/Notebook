# 数论基础

## Acknowledgement

[数论基础 - OI Wiki](https://oi-wiki.org/math/number-theory/basic/)

## 快速幂

`pow ( a , b );` 太慢了

所以需要快速幂，即更快地求出$a^b$

基本思想是：
把指数分解成 2 的幂的积的形式
比如说，我们要求 3 的 10 次
我们就可以转化为`3^2 * 3^8`;
怎么知道是 2 和 8 呢？？

这里我们需要知道二进制
10 这个数在二进制中 是 1010；
我们发现在第 2 位和第 4 位是有数的，说明 1010 变成 10 进制就要乘以位数的权

这个时候问题就转化成了找二进制上是 1 的位数

```cpp title="二进制的数位分离"
while(p){
    if(p & 1){
    ??????
    p >>= 1;
}
```

~~显然与 10 进制数位分离一模一样~~

```cpp title="快速幂"
#include<bits/stdc++.h>
using namespace std;
int x,y;
int quick(int n,int p){   //快速幂 板子
 int ans = 1;int tmp = n;
 while(p){
  if(p & 1){
   ans *= tmp;
  }
  tmp *= tmp;
  p >>= 1;
 }
 return ans; 
}

int main (){
 scanf("%d %d",&x,&y);
 printf("%d",quick(x,y));
 return 0;
}
```

??? example "例题 [Acwing 90. 64 位整数乘法](https://www.acwing.com/problem/content/92/)"

    ```cpp
    #include<bits/stdc++.h>
    #define ll long long
    using namespace std;
    ll x,y,r;
    ll quick(ll n, ll p, ll r){
        ll ans = 0;   //因为这里是加法，所以一开始是0；
        ll tmp = n;   
        while(p){   //如果没分完就继续循环
            if(p & 1){//位运算--与 
                ans = (ans + tmp) % r;//每次都要%r//注意这里是加法
            }
            tmp = (tmp * 2) % r;
            p >>= 1;  //右移一位
        }
        return ans % r;  //最后也要mod一下
    }

    int main (){
        scanf("%lld %lld %lld",&x,&y,&r);
        printf("%lld",quick(x,y,r));
        return 0;
    }
    ```

### 矩阵快速幂

## 整除

最大公约数

求法

- 欧几里得算法（辗转相除法）

\[ \gcd(a, b) = \gcd(b, a \mod b) \]

> 所有大于 3 的素数都可以表示为$6n-1$

!!! note "proof"

    设 \( a \) 可以表示成 \( a = kb + r \)（其中 \( a, b, k, r \) 均为正整数，且 \( r \neq 0 \)）。假设 \( d \) 是 \( a \) 和 \( b \) 的一个公约数，记作 \( d \mid a \) 且 \( d \mid b \)，即 \( a \) 和 \( b \) 都可以被 \( d \) 整除。

    根据等式 \( r = a - kb \)，我们将等式两边同时除以 \( d \)：

    \[ \frac{r}{d} = \frac{a}{d} - k \cdot \frac{b}{d} \]

    由等式右边可知 \( \frac{a}{d} \) 和 \( \frac{b}{d} \) 均为整数，因此 \( \frac{r}{d} \) 也是整数，这意味着 \( d \mid r \)。

    因此，\( d \) 也是 \( b \) 和 \( a \mod b \) 的公约数。

    由于 \( a \) 和 \( b \) 的公约数与 \( b \) 和 \( a \mod b \) 的公约数相等，所以它们的最大公约数也相等，得证。

## 模

特别的，当

$$
gcd(a, b) = 1
$$

时，我们称$a$和$b$是互质的。互质的两个数的最大公约数是 1。

## 素数

- 质数判断

  O(n) 遍历判断

  O(nlogn) 素数筛/埃氏筛

 1. 朴素算法
 2. 埃氏筛法
 3. 线性筛法（欧拉筛）
 4. P3383【模板】线性筛素数

### 朴素算法

素数最朴素的算法了
它的时间复杂度是`O(n*sqrt(n))`的

```cpp
bool prime (int x){
 for(int i = 2; i <= x; i ++){
  if(x % i ==0){
   return 0;
  }}
 return 1;
}
```

但是，这只适用于小数据的处理，所以我们需要改进算法

### Eratosthenes（埃氏筛法）

- **整数的唯一分解定理：**
任何一个大于 1 的自然数 N，如果 N 不为质数，都可以唯一分解成有限个质数的乘积`N=P1 ^ a1 · P2 ^ a2 · P3 ^ a3 · … · Pn ^ an` ，这里 P1<P2<P3<…<Pn 均为质数，其诸指数 ai 是正整数。
（：当然质数的话直接就是质数本身）

- 埃氏筛法的思想：
枚举每个素数，然后把他们的倍数都打上标记，从而达到筛出的目的
**质数的倍数一定不是质数**

时间复杂度是**O(nloglogn)**

- 注意`j = i`可以做到一部分的优化作用

```cpp
for(int i = 1; i <= sqrt(n); i ++){  //循环一遍可以有倍数的 
 if(b[i] == 1) continue;   //如果不是质数或已经判断过，直接跳过 
 for(int j = i; i * j <= n;j++){  //内层循环倍数 //pay attention to j = i; 
  b[i*j] = 1;      //打上标记     
 }   
} 
```

但是这个算法在 1e7 左右还是不太好用，会 TLE（~~哭晕~
而且埃氏筛法还有一个缺陷：
对于一个合数，有可能被筛多次。例如 30 = 2 *15 = 3* 10 = 5*6……
那么如何确保每个合数只被筛选一次呢？我们只要用它的最小质因子来筛选即可，这便是欧拉筛法

### 线性筛法（欧拉筛法）

线性筛法是什么意思呢？
就是我们在埃氏筛法中有个问题就是一个数可能被筛多次
所以就造成了时间的浪费，所以算法就在这里做了改进

基本思想：在埃氏筛法的基础上，让每个合数只被它的最小质因子筛选一次，以达到不重复的目的

```cpp
int prime[maxn];
int visit[maxn];
void Prime(){
    mem(visit,0);
    mem(prime, 0);
    for (int i = 2;i <= maxn; i++) {
        if (!visit[i]) {
            prime[++prime[0]] = i;      //记录素数，这个 prime[0] 相当于 cnt，用来计数
        }
        for (int j = 1; j <= prime[0] && i*prime[j] <= maxn; j++) {
        //j 循环枚举了当前位置已判定为素数的数，并且限制倍数和质数的和的乘积不大于最大数
//            cout<<"  j = "<<j<<" prime["<<j<<"]"<<" = "<<prime[j]<<" i*prime[j] = "<<i*prime[j]<<endl;
            visit[i*prime[j]] = 1;    //打标记
            if (i % prime[j] == 0) { //这一步比较重要，如果 i%j==0，说明 i 就不是最小的质因子，所以就跳出程序了；
                break;
            }
        }
    }
}

```

- 还有[网友版本](https://blog.csdn.net/enjoy_pascal/article/details/80372454)的~

```cpp
void init() 
{
    memset(bz,1,sizeof(bz));
    tot=0;
    for (int i=2;i<MAXN;i++) 
    {
        if (bz[i])p[tot++]=i;
        for (int j=0;j<tot && i*p[j]<=MAXN;j++) 
        {
            bz[i*p[j]]=0;
            if (i%p[j]==0)break;
        }
    }
}
```

!!! note "P3383【模板】线性筛素数"

    做个水题
    [P3383 【模板】线性筛素数](https://www.luogu.org/problem/P3383)

    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__01-Math.assets__83978c18ca1332d2089af3151f607631.webp)

    裸题

    === "AC code"

        稍微注意一下0和1的特判
        ```cpp
        //Author:PhilFan;
        #include<bits/stdc++.h>
        #define MAXN 10000010
        using namespace std;
        int n,m,a[MAXN],p[MAXN],x;
        void init(int n) 
        {
            memset(p,0,sizeof(p));
            p[1]=1;  tot=0;
            for (int i = 2;i <= n;i++) 
            {
                if(a[i]==0) p[tot++]= i;
                for (int j = 0;j < tot && i * p[j] <= n+5; j++) 
                {
                    a[i * p[j]] = 1;
                    if (i % p[j] == 0) break;
                }
            }
        }
            
        int main()
        {
            scanf("%d %d",&n,&m);
            init(n);
            a[0]=1,a[1]=1;
            for(int i = 1; i <= m; i++){
                scanf("%d",&x);
                if(a[x]==0){printf("Yes\n");}
                else{printf("No\n");}
                x=0;
            } 
            return 0;
        }
        ```

!!! example "P1865 A % B Problem"

    [网址](https://www.luogu.org/problem/P1865)


    这道题是输出区间的质数，需要在线性筛法中加入一个前缀和的数组，因为不加的话会TLE一个点

    ```cpp
    //Author:PhilFan;
    #include<bits/stdc++.h>
    #define MAXN 10000010
    using namespace std;
    int n,m,a[MAXN],p[MAXN],b[MAXN],x,y,cnt;
    void init(int n) 
    {
        memset(p,0,sizeof(p));
        p[1]=1;  
        int tot=0;
        for (int i = 2;i <= n;i++) 
        {
            if(a[i]==0){
                p[tot++]= i;
                b[i]=b[i-1]+1;//前缀和数组   //如果有多的质数，数组++
            }
            else b[i]=b[i-1];//如果质数没有多，b[i]就和上一个一样
            for (int j = 0;j < tot && i * p[j] <= n+5; j++) 
            {
                a[i * p[j]] = 1;
                if (i % p[j] == 0) break;
            }
        }
    }
        
    int main()
    {
        scanf("%d %d",&m,&n);
        a[0]=1,a[1]=1;
        init(n);
        for(int i = 1; i <= m; i++){
            scanf("%d %d",&x,&y);
            if(x<1||x>n||y<1||y>n){  //特判
                printf("Crossing the line\n");
            }
            else{
                cout<<b[y]-b[x-1]<<endl; //x有可能也是质数，所以是x-1
                x = 0 , y = 0;
            }
        } 
        return 0;
    }
    ```

## gcd & lcm

$$
gcd(a,b) \times lcm(a,b) = a \times b
$$

```c
int gcd(int x , int y){
return y ? gcd(y,x%y) : x;
}
```

## 同余 (Congruence)

同余是表示两个整数除以同一个正整数后余数相等的关系。如果整数 $a$ 除以正整数 $n$ 的余数与整数$b$除以$n$的余数相同，我们说$a$和$b$对模$n$同余，表示为：

$$
a \equiv b \mod n
$$

b 是除法的余数

## 逆元/模逆 (Modular Inverse)

如果存在整数$b$使得$ab \equiv 1 \mod n$，则称$b$是$a$模$n$的逆元

$$
a^{-1} \equiv b \mod n
$$

表示找到一个数$b$，使得$a$和$b$相乘对模$n$同余 1。

!!! note "有逆元的充要条件"
    两数互质

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__Algorithm__assets__01-Math.assets__image-20240529115856874.webp)

计算方法

- 拓展欧几里得 `Exgcd(a,mod)` 取 x，略

- **快速幂**

因为 $ax \equiv 1 \pmod b$；

所以 $ax \equiv a^{b-1} \pmod b$（根据费马小定理；

所以 $x \equiv a^{b-2} \pmod b$。

然后我们就可以用快速幂来求了。

这里还可以使用矩阵快速幂进行优化

???+ note "实现"

    === "C++"
        ```cpp
        int qpow(long long a, int b) {
          int ans = 1;
          a = (a % p + p) % p;
          for (; b; b >>= 1) {
            if (b & 1) ans = (a * ans) % p;
            a = (a * a) % p;
          }
          return ans;
        }
        ```
    
    === "Python"
        ```python
        def qpow(a, b):
            ans = 1
            a = (a % p + p) % p
            while b:
                if b & 1:
                    ans = (a * ans) % p
                a = (a * a) % p
                b >>= 1
            return ans
        ```

注意：快速幂法使用了 费马小定理，要求 $b$ 是一个素数；而扩展欧几里得法只要求 $\gcd(a, b) = 1$。

## 裴蜀定理（Bézout's Theorem）

**定义**：
裴蜀定理指出，对于任意的整数 \(a\) 和 \(b\)，存在整数 \(x\) 和 \(y\)，使得 \(ax + by = \gcd(a, b)\)，其中 \(\gcd(a, b)\) 是 \(a\) 和 \(b\) 的最大公约数。

**例子**：
考虑 \(a = 56\) 和 \(b = 15\)，计算它们的最大公约数：
\[ \gcd(56, 15) = 1 \]

我们可以找到 \(x\) 和 \(y\) 使得：
\[ 56x + 15y = 1 \]

一个解是 \(x = -2\) 和 \(y = 15\)：
\[ 56(-2) + 15(15) = -112 + 225 = 113 \]

```python
from sympy import gcd, mod_inverse

a = 56
b = 15
g = gcd(a, b)  # 计算最大公约数

# 使用扩展欧几里得算法找到 x 和 y
def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = extended_gcd(b, a % b)
        return (y, x - (a // b) * y)

x, y = extended_gcd(a, b)
print(f"The coefficients x and y are: {x}, {y}")
```

## 扩展欧几里得定理（Extended Euclidean Algorithm）

根据裴蜀定理我们知道
\[ ax + by = \gcd(a, b) \]

那么对于不定方程
\[ ax + by = m \]
必有 $m$ 是 $\gcd(a,b)$ 的倍数（即第一个用途，判断是否有解）

知道是否有解通常不能达到目的，还需要得到一组可行解

设

$$
ax_1+by_1=\gcd(a,b)\\
bx_2+(a\bmod b)y_2=\gcd(b,a\bmod b)
$$

由欧几里得定理可知

$$
\gcd(a,b)=\gcd(b,a\bmod b)
$$

所以

$$
ax_1+by_1=bx_2+(a\bmod b)y_2
$$

又因为 $a\bmod b=a-(\lfloor\frac{a}{b}\rfloor\times b)$

所以

$$
ax_1+by_1=bx_2+(a-(\lfloor\frac{a}{b}\rfloor\times b))y_2\\
ax_1+by_1=ay_2+bx_2-\lfloor\frac{a}{b}\rfloor\times by_2=ay_2+b(x_2-\lfloor\frac{a}{b}\rfloor y_2)
$$

因为 $a=a,b=b$

所以 $x_1=y_2,y_1=x_2-\lfloor\frac{a}{b}\rfloor y_2$

将 $x_2,y_2$ 不断代入递归求解直至 $\gcd$（最大公约数，下同）为 $0$ 递归 $x=1,y=0$ 回去求解。

通解

对于方程

$$
ax+by=gcd(a,b) \rightarrow ax+by=k
$$

扩大了$\frac{k}{gcd(a,b)}$ 倍，那么 Exgcd 求出来$x_0,y_0$也要响应的扩大$\frac{k}{gcd(a,b)}$倍

$$
\begin{align*}
x_0 = x_0 * \frac{k}{gcd(a,b)}\\
y_0 = y_0 * \frac{k}{gcd(a,b)}\\
\end{align*}
$$

**上述方法可以求得一个特解，而通解形式如下：**

$$
\begin{align*}
\left\{
\begin{array}{lr}
x = x_0 + \frac{b}{\gcd(a,b)} \cdot t\\
y = y_0 - \frac{a}{\gcd(a,b)} \cdot t
\end{array}
\right.
t\in \mathbf{Z}
\end{align*}
$$

最小整数解

$$
x=(x+\frac{b}{\gcd(a,b)}*n)\mod \frac{b}{\gcd(a,b)}\\
=x\mod \frac{b}{\gcd(a,b)}
$$

若 x<=0，则 x+=b/gcd

> 参考网址：[求逆元方法 简单又好记_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11Y4y1U7Gh/?spm_id_from=333.788&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)
> [详解扩展欧几里得算法（扩展 GCD） - Seaway-Fu - 博客园 (cnblogs.com)](https://www.cnblogs.com/fusiwei/p/11775503.html)

=== "C++"
    ```cpp
    int Exgcd(int a, int b, int &x, int &y) {
      if (!b) {
        x = 1;
        y = 0;
        return a;
      }
      int d = Exgcd(b, a % b, x, y);
      int t = x;
      x = y;
      y = t - (a / b) * y;
      return d;
    }
    ```

=== "Python"
    ```python
    def Exgcd(a, b):
        if b == 0:
            return a, 1, 0
        d, x, y = Exgcd(b, a % b)
        return d, y, x - (a // b) * y
    ```

函数最后返回的$d$即为 $\gcd$，在这个过程中计算 $x,y$ 即可。

求解乘法逆元

对于一个数 $a$，求解其模 $m$ 的逆元 $a^{-1} = x$，即满足 $a \times x \equiv 1 \mod m$。

有

$$
a \times x = 1 + m \times k\\
a \times x + m \times (-k) = 1\\
a \times x + m \times y = 1
$$

使用扩展欧几里得算法求解 $x$ 和 $y$ 即可。
此时 $a = a,b = m$ ,求得的$x$即为逆元

## 中国剩余定理（Chinese Remainder Theorem, CRT）

参考视频：[中国剩余定理，考试包会](https://www.bilibili.com/video/BV1Y84y1E7ts)

**定义**：
中国剩余定理解决同余方程组。若\(m_1, m_2, ..., m_k\) 互素，则对于任意整数 \(a_1, a_2, ..., a_k\)，存在唯一的整数 \(x\)，满足：
\[ x \equiv a_i \mod m_i \]

**例子**：
求解以下方程组：
\[ x \equiv 2 \mod 3 \]
\[ x \equiv 3 \mod 5 \]
\[ x \equiv 2 \mod 7 \]

根据 CRT，可以找到唯一解 \(x\)（在模 \(105 = 3 \times 5 \times 7\) 范围内）：
解为 \(x = 23\)，因为：
\[ 23 \mod 3 = 2 \]
\[ 23 \mod 5 = 3 \]
\[ 23 \mod 7 = 2 \]

```python
from sympy.ntheory.modular import crt

# 模数
moduli = [3, 5, 7]
# 余数
remainders = [2, 3, 2]

x = crt(moduli, remainders)[0]
print(f"The solution x is: {x}")
```

## 欧拉函数 (Euler's Totient Function)

欧拉函数$\phi(n)$是小于或等于$n$的正整数中与$n$互质的数的数量。

- 对于质数$p$，$\phi(p) = p - 1$。

- 如果$n$是两个不同质数$p$和$q$的乘积，从定义上考虑，与$p$ 不互质的有 $q$个，与$ q $不互质的有$ p $个，重复计算的有一个，所以

$$
\begin{aligned}
\phi(n) &= n-p-q+1= pq-p-q+1\\
&= (p - 1)(q - 1)
\end{aligned}
$$

- 若$n = p^k$,，从定义上考虑，与 n 不互质的有 $p,2p,3p,\dots p^{k-1}*p $，共$p^{k-1} $个，剩下的就是互质的，所以
$\phi(n) = n -p^{k-1} = n(1-\frac{1}{p})$

- 对于任意的$n = p_1^{a_1}*p_2^{a_2}\dots p_{k}^{a_k}$

$$
\phi(n) = n \prod_{i=1}^k \left(1 - \frac{1}{p_i}\right)
$$

## 费马小定理

若 $p$ 为素数，$\gcd(a, p) = 1$，则

$$
a^{p - 1} \equiv 1 \pmod{p}
$$

另一个形式：对于任意整数 $a$，有

$$
a^p \equiv a \pmod{p}
$$

!!! note "证明"

    设一个质数为 $p$，我们取一个不为 $p$ 倍数的数 $a$。

    构造一个序列：$A=\{1,2,3\dots,p-1\}$，这个序列有着这样一个性质：

    $$
    \prod_{i=1}^{p-1}\space A_i\equiv\prod_{i=1}^{p-1} (A_i\times a) \pmod p
    $$

    **证明：**

    $$
    \because (A_i,p)=1,(A_i\times a,p)=1
    $$

    又因为每一个 $A_i\times a \pmod p$ 都是独一无二的，且 $A_i\times a \pmod p < p$

    得证（每一个 $A_i\times a$ 都对应了一个 $A_i$）

    设 $f=(p-1)!$, 则 $f\equiv a\times A_1\times a\times A_2\times a \times A_3 \dots \times  A_{p-1} \pmod p$

    $$
    \begin{aligned}
    a^{p-1}\times f &\equiv f \pmod p \\
    a^{p-1} &\equiv 1 \pmod p
    \end{aligned}
    $$

    证毕。

    **也可用归纳法证明：**

    显然 $1^p\equiv 1\pmod p$，假设 $a^p\equiv a\pmod p$ 成立，那么通过二项式定理有

    $$
    (a+1)^p=a^p+\binom{p}{1}a^{p-1}+\binom{p}{2}a^{p-2}+\cdots +\binom{p}{p-1}a+1
    $$

    因为 $\binom{p}{k}=\frac{p(p-1)\cdots (p-k+1)}{k!}$ 对于 $1\leq k\leq p-1$ 成立，在模 $p$ 意义下 $\binom{p}{1}\equiv \binom{p}{2}\equiv \cdots \equiv \binom{p}{p-1}\equiv 0\pmod p$，那么 $(a+1)^p \equiv a^p +1\pmod p$，将 $a^p\equiv a\pmod p$ 带入得 $(a+1)^p\equiv a+1\pmod p$ 得证。

## 欧拉定理

欧拉定理指出，对于两个互质的正整数 \(a\) 和 \(n\)（即 \(gcd(a, n) = 1\)），\(a\) 的欧拉函数 \(\phi(n)\) 次幂对 \(n\) 的模等于 1。用数学表达式表示为：

$$
a^{\phi(n)} \equiv 1 \mod n
$$

其中，\(\phi(n)\) 是欧拉函数，表示小于或等于 \(n\) 的正整数中与 \(n\) 互质的数的数量。

若 $\gcd(a, m) = 1$，则 $a^{\varphi(m)} \equiv 1 \pmod{m}$。

欧拉定理是 RSA 加密的数学基础

!!! note "证明"
    实际上这个证明过程跟上文费马小定理的证明过程是非常相似的：**构造一个与 $m$ 互质的数列**，再进行操作。

    设 $r_1, r_2, \cdots, r_{\varphi(m)}$ 为模 $m$ 意义下的一个简化剩余系，则 $ar_1, ar_2, \cdots, ar_{\varphi(m)}$ 也为模 $m$ 意义下的一个简化剩余系。
    
    所以 
    
    $$
    r_1r_2 \cdots r_{\varphi(m)} \equiv ar_1 \cdot ar_2 \cdots ar_{\varphi(m)} \equiv a^{\varphi(m)}r_1r_2 \cdots r_{\varphi(m)} \pmod{m}
    $$
    
    可约去 $r_1r_2 \cdots r_{\varphi(m)}$，即得 
    
    $$
    a^{\varphi(m)} \equiv 1 \pmod{m}
    $$

    当 $m$ 为素数时，由于 $\varphi(m) = m - 1$，代入欧拉定理可立即得到费马小定理。**费马小定理是欧拉定理的特例**
