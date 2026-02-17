# Crypto

!!! note "来源"
    - USTC《计算机网络》<br>
    - 《图解密码技术》<br>
    - 《信息物理系统安全》<br>

!!! tip "如果看不到图像或是公式，多刷新几次"

做 PPT 时候整理的图像

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240605143933543.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240605144047495.webp)

## 加密——机密性

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240215231126309.webp)

!!! note "密钥才是加密的核心"
    加密算法和密钥是分开的，每个人可以拥有相同品牌的锁，但是每一个人有不同的钥匙<br>锁的设计是公开的，但是钥匙是秘密的。

- Trudy: 窃听、插入、伪装、劫持、拒绝服务

只有发送方和预订的接收方能否理解传输的报文内容
发送方加密报文；接收方解密报文

明文密文并不是看是否由人读取

|               Transaction                | Fill In This Column |       Choose From The Following        |
| :--------------------------------------: | :-----------------: | :------------------------------------: |
|   Alice wants to sign an email to Bob    |          b          |         a. Alice's public key          |
|  Alice wants to encrypt an email to Bob  |          c          |         b. Alice's private key         |
|    Bob wants to verify Alice's email     |          a          |          c. Bob's public key           |
|    Bob wants to decrypt Alice's email    |          d          |          d. Bob's private key          |
|  Alice public key certificate signed by  |          f          | e. Certification Authority public key  |
| Bob public key certificate verifies with |          e          | f. Certification Authority private key |

答案和解析：

- Alice 想要给 Bob 签名一封电子邮件：因为 Alice 使用她的私钥生成数字签名，而 Bob 需要使用 Alice 的公钥来验证这个签名。
- Alice 想要加密一封发送给 Bob 的电子邮件：应该是使用 Bob 的公钥来加密
- Bob 想要验证 Alice 的电子邮件：因为 Bob 使用 Alice 的公钥验证了数字签名，所以他知道这封电子邮件确实来自 Alice。
- Bob 想要解密 Alice 的电子邮件：d（Bob 的私钥）
- Alice 的公钥证书由以下机构签名：因为公钥证书是由认证机构使用其私钥签名的，所以其他人可以使用认证机构的公钥来验证这个签名。
- Bob 的公钥证书验证如下：使用认证机构的公钥来验证 Bob 的公钥证书

### 古典密码

> 更少的数学，更多的人文！

- 代换 (substitution) 密码用新的替换原先的内容

- 置换 (permutation) 密码 打乱原先的顺序

- Hill 密码

#### 摩斯密码

摩尔斯电码（Morse Code）：利用点划（“滴”的时间长短）来表示字符

点 ·：1 单位；划 -：3 单位
点划之间间隔：1 单位；字符之间间隔：3 单位；单词之间间隔：7 单位

字符集：`A-Z`、`0-9`、标点符号（`.:,;?='/!-_"()$&@+`）、一些电码专用表示

表示中文：电码表（一个汉字对应四个数字），数字使用短码发送

??? note "以下是一份常用的摩斯电码表："

    === "字母表"
        | 字母 | 摩斯电码 |
        | --- | --- |
        | A | ·- |
        | B | -··· |
        | C | -·-· |
        | D | -·· |
        | E | · |
        | F | ··-· |
        | G | --· |
        | H | ···· |
        | I | ·· |
        | J | ·--- |
        | K | -·- |
        | L | ·-·· |
        | M | -- |
        | N | -· |
        | O | --- |
        | P | ·--· |
        | Q | --·- |
        | R | ·-· |
        | S | ··· |
        | T | - |
        | U | ··- |
        | V | ···- |
        | W | ·-- |
        | X | -··- |
        | Y | -·-- |
        | Z | --·· |

    === "数字"
        | 数字 | 摩斯电码 |
        | --- | --- |
        | 0 | ----- |
        | 1 | ·---- |
        | 2 | ··--- |
        | 3 | ···-- |
        | 4 | ····- |
        | 5 | ····· |
        | 6 | -···· |
        | 7 | --··· |
        | 8 | ---·· |
        | 9 | ----· |

    === "标点符号"
        | 符号 | 摩斯电码 |
        | --- | --- |
        | . | ·-·-·- |
        | , | --··-- |
        | ? | ··--·· |
        | ' | ·----· |
        | ! | -·-·-- |
        | / | -··-· |
        | ( | -·--· |
        | ) | -·--·- |
        | & | ·-··- |
        | : | ---··· |
        | ; | -·-·-· |
        | = | -···- |
        | + | ·-·-· |
        | - | -····- |
        | _ | ··-·· |
        | " | ·-···- |
        | $ | ···-··- |
        | @ | ·--·-· |

#### 凯撒密码——平移

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240522173659727.webp)

又叫加法密码，是一种替换密码，属于其中的单表密码，将明文的每个字母按字母表循环移动固定位数得到密文

**加密：**

$$
enc(x)=( x+key ) \mod \ 26
$$

**解密：**

$$
dec(y)=(y−key) \mod \  26
$$

**破解：**

爆破移动位数观察结果即可（常见编码 ROT13，取 key=13)

一般的凯撒加密只作用于 26 个字母，但也可以将其扩展到 ASCII 码表上（常见编码 ROT47，将 33-126 作为字母表，取 key=47)

#### 仿射密码

类似凯撒加密，但不仅仅进行加法

**加密：**

$$
encx=(x\times key_1+key_2) \mod \ 26
$$

**解密：**

$$
decy = (y-key_2)\times key_1^{-1} \mod \ 26
$$

**破解：**

单表密码加密前后的字符是一一对应的，不会破坏统计规律，根据英文文本中字母出现的频率以及一些常见单词即可轻松破解

#### 单表替换密码

密钥：替换表，使用密码本

字母替换，通过分析字频和词频可以破解

> 英文文章出现最高的字母是 e

[quipqiup - cryptoquip and cryptogram solver](http://quipqiup.com/)<br>
[古典密码学之词频分析 | Cata1yst's blog (cata1ysts.github.io)](https://cata1ysts.github.io/2022/08/14/古典密码学之词频分析/)<br>
[单表代换加密 - CTF Wiki (ctf-wiki.org)](https://ctf-wiki.org/crypto/classical/monoalphabetic/#_11)<br>

!!! note "单表替换密码"
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__crypto_challenge1.webp)

    - 不妨读一下**福尔摩斯探案集《跳舞的小人》**，说不定对你有帮助呢？
    
    解密结果
    
    > tonight Ethan will arrive here please lure him to the abandoned warehouse near the police station where the professional assassin reese hired will eliminate him
    >
    > tomorrow she will go to the warehouse and become the first person to discover his corpse with a strong alibi these police officers absolutely cannot arrest her
    
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240605182302624.webp)

#### 多表替换密码——维吉尼亚密码

一种多表加密的替换密码。密钥任意长，并且以循环使用

第 i 个字符使用第 i 个密钥进行偏移

加密：

$$
enc(x_i) = (x_i + key_i) \mod \ 26
$$

解密：

$$
dec(y_i)= (y_i-key_i) \mod 26
$$

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__20240707145724.webp)

!!! note "例：明文 CRANE，密钥 TONY"
    (C, T)  to   V
    (R, O)  to   F
    (A, N)  to   N
    (N, Y)  to   L
    (E, T)  to   X

确定密钥长度→分组爆破加法密码→得到密钥

!!! note "解密实战"

    === "题目"
        Fhovq abi mn ypp hyvee krp a vmftvi tobwq ox e rabq . Ano hmy dlq ovh tobwq acoe tri xidxxe rsdso xa sorp tri ihoef ty xte wmxl . Dlq lsxflo larci us fidy rebpi . Lq ckvdiow fho atekx mnn vgnc xawkvp tri yivp . Nud xtebi us k vuvov un pvand sr tri xidxxe rsdso . Lq sdsbs krp dyie nyx wnya ihkx fo ns zehx . Vucx fhor Muxx Oog me pkweixk ny . Dlq lsxflo larci msuw , Muxx Oog , txekwq topx mo. Gmn S gdocw fho vuvov ". Muxx Oog ezsgids , Sx us xsf doib , yyy oax gdocw ut.ut." Glqn dlq lsxflo larci neqmzs ds orywe tri difid , a vmftvi eqemdrop ehyyfs kx tiw , Putdpqhyvee , nszt mvasc mf, yyy iivp ne nvawxip . Yowfebhmy yrq op qk fbmqnnw iac hdogrqd sr fhsw difid ." tri xidxxe rsdso me vovk apvmin . Junkpxy ri pemmpec xa gy lamo ezd kww hsw yodlqr.Dlq ovh tobwq acoe , Wrc po isg tkoq tri ihoef bkgw Wrefs gvanq autr cau Wcohspp ." tri xidxxe rsdso ezsgids cepli , Xtebi us k vuvov un pvand sr mo. Egnd Gaw ceud sx iac rat niqp . Lyf tri xidxxe cugibvql ceud sx iac hqez . Atad wtavp U dy ". Xte ypp hyvee ceks , Wc ohspp , yyy ehyyxd dvk ty gdocw fho vuvov ny isgrcixf . Sj koe hanyx fri , law ns koe ozog xte bmheb me doib ob rat". Dlq lsxflo larci oabvuec xte glqad ezd bifubre ty xte bmhebwudo . Ef lkwf , ho wgcmiqdc mzcbsessrs tri difid . Nya, Te urawc law niqp dlq rszqr sw.
    === "分析"
        相同内容tri 出现位置 20, 92, 124, 320, 528, 640, 864 ，第一次出现的位置记为 0
        最大公因数为4 密钥长度极大概率为 4 ，有较小概率为 2 或 1
    
    === "方法一：根据重复单词爆破密钥"
        前文多次重复的，tri 有很大概率为 the ，求出密钥，接下来只需要爆破一位即可
    
    === "方法二：逐个爆破密钥"
        已知密钥长度为k;第0,k,2k,…… 个字符使用同一个密钥，构成一个单表加法密码
        根据字母频率推断这位密钥为 m
        经过分析破解，最后能得到密钥为 make

!!! note "—次性密码本与压缩"
    虽然一次性密码本的密钥需要与明文等长，但是我手上有数据压缩程序，只要用这个程序 对一次性密码本的密钥进行压缩，不就可以把密钥变短了吗？ 请问Alice的想法正确吗？<br>
    不正确。因为一次性密码本的密钥无论使用任何压缩软件都无法进行压缩。<br>压缩软件的压缩原理，是找出输入数据中出现的冗余的重复序列，并将它们替换成较短的数据。然而一次性密码本所使用的密钥是随机的，其中不包含任何冗余的重复序列。<br>反过来说， 如果一个比特序列能够被压缩，就说明它不是一个随机的比特序列。

#### 替换密码

加密变换使得信息元素只有位置变化而内容不变
比如对于一种置换密码，其置换表为

| 明文$X$ | 密文$E(X)$ |
| --- | --- |
| 1 | 3 |
| 2 | 5 |
| 3 | 1 |
| 4 | 6 |
| 5 | 4 |
| 6 | 2 |

对于明文`crypto basic`，先进行分组（不足需填充）对每一组进行置换：

```shell
[crypto]→ [yoctrp] [ basic] → [ac ibs]
```

最终密文就是`yoctrpac ibs`

栅栏密码

栅栏密码也是一种置换密码，其将明文分割成 k 行，然后重新拼接，这里 k 即为加密的密钥。

比如还是明文`crypto basic` ，取 k=3，将明文分割成三行

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__20240707152053.webp)
因此，密文为 `cp srtbiyoac`

#### 矩阵的替换——Hill 加密

Hill 密码是一种基于线性代数的多字母替换密码，由数学家 Lester S. Hill 于 1929 年发明。它通过将字母映射到数值，然后使用矩阵乘法对消息进行加密。

每个字母当作 26 进制数字，将一串字母当成$ n $维向量，跟一个 $n*n$的矩阵相乘，再将得出的结果 $\mod 26 $，其中 $n*n$ 矩阵就是密钥。

1. **字母映射**：首先，将字母映射到数字。通常使用如下映射：
   - A = 0, B = 1, C = 2, ..., Z = 25

2. **加密公式**：明文向量为 \( P \)，加密矩阵为 \( K \)，则密文向量 \( C \) 为：

     \[
     C = K \cdot P \ (\text{mod} \ 26)
     \]

3. **解密公式**：设密文向量为 \( C \)，加密矩阵 \( K \) 的逆矩阵为 \( K^{-1} \)，则明文向量 \( P \) 为：
  
     \[
     P = K^{-1} \cdot C \ (\text{mod} \ 26)
     \]

Enigma 加密

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240522174420066.webp)

!!! bug "这一部分没有看"

### 对称加密

加密解密密钥一样

$K_{A-B}$:对称密钥

密钥的分发：密码本

密码选择

- 首先，DES 不应再用于任何新的用途，因为随着计算机技术的进步，**现在用暴力破解法已经能够在现实的时间内完成对 DES 的破译**。但是，在某些情况下也需要保持与旧版本软件的兼容性。

- 其次，我们也没有理由将三重 DES 用于任何新的用途，尽管在一些重视兼容性的环境中还会继续使用，但它会逐渐被 AES 所取代。

- 现在大家应该使用的算法是 AES(`Rijndael`),因为它安全、快速，而且能够在各种平台上工作。此外，由于全世界的密码学家都在对 AES 进行不断的验证，因此即便万一发现它有什么缺陷，也会立刻告知全世界并修复这些缺陷。

#### 一次性密码本——无法被破译

因为无法判断是否为正确的明文，在破译过程中会出现所有的排列组合

又称为维纳密码（`Vernam cipher`）

香农证明其为无条件安全、理论上无法破译

#### DES |  `Data Encryption Standard`

- 56-bit 对称密钥，**64-bit 明文输入**（每隔 7bit 会插入 1bit 错误检查的 bit）
- 分组密码的一种，以 64bit 为分组
- 16 round Feistel 网络
- 已经被破解了

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240526113303219.webp" alt="image-20240526113303219" style="zoom:50%;" />

中间的“子密钥”指的是本轮加密所使用的密钥。在 Feistel 网络中，每一轮都需要使用一个不同的子密钥。由于子密钥只在一轮中使用，它只是一个局部密钥，因此才称为子密钥 (`subkey`)。

1) 将输入的数据等分为左右两部分
2) 将输人的右侧直接发送到输出的右侧
3) 将输入的右侧发送到轮函数
4) 轮函数根据右侧数据和子密钥，计算出一串看上去是随机的比特序列
5) 将上一步得到的比特序列与左侧数据进行 XOR 运算，并将结果作为加密后的左侧

但是，这样一来“右侧”根本就没有被加密，因此我们需要用不同的子密钥对一轮的处理 重复若干次，并在每两轮处理之间将左侧和右侧的数据对调。

解密

#### 3DES  | `Triple DES`

- 3DES 是对 DES 的加强，通过三次应用 DES 算法来增加安全性。
- 使用两到三个 56 位密钥。
- 三重 DES 并不是进行三次 DES 加密（加密 —加密 —加密），而是加密—解密——加密的过程。IBM 公司设计，能够让 3-DES 兼容不同 DES。

三个密钥都相同

当三重 DES 中所有的密钥都相同时，三重 DES 也就等同于普通的 DES 了。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529100522514.webp" alt="image-20240529100522514" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240506083826564.webp" alt="image-20240506083826564" style="zoom:50%;" />

一三密钥相同

如果密钥 1 和密钥 3 使用相同的密钥，而密钥 2 使用不同的密钥（也就是只使用两个 DES，这种三重 DES 就称为 DES-EDE2(图 3 ( Decryption )—加密（Encryption ) 这个流程。

三个不同密钥

- 使用 3 个 key，3 重 DES 运算；
- 密文分组成串技术：当前明文和前面密文 64bit 做异或处理

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529095943964.webp)

尽管三重 DES 目前还被银行等机构使用，但其处理速度不高，除了特别重视向下兼容性的 情况以外，很少被用于新的用途。

#### AES | `Advanced Encryption Standard`

- 新的对称密钥 NIST 标准 (NIST(National Institute of Standards and Technology, 国家标准技术研究所) 用于替换 DES
- 数据 128bit 成组加密：128, 192, or 256 bit keys
- 穷尽法解密如果使用 1 秒钟破解 DES, 需要花 149 万亿年破解 AES
- 像这样通过竞争来实现标准化（`standardization by competition`) 的方式，正是密码算法选拔的正确方式
- 彻底杜绝了隐蔽式安全性（`security by obscurity`)

2000 年 10 月 2 日，`Rijndael`力压群雄，被 NIST 选定为 AES 标准。

`Rijndael`的分组长度和密钥长度可以分别以 32 比特为单位在 128 比特到 256 比特的范围内 进行选择。不过在 AES 的规格中，分组长度固定为 128 比特，密钥长度只有 128、192 和 256 比特三种。

其中每一轮分为`SubBytes`、`ShiftRows`、 `MixColumns` 和 `AddRoundKey` 共 4 个步骤。

- `SubBytes`

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529101532403.webp)

- `shiftrows`:每一行平移字节数也是不同的

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529101600609.webp)

- mixcolumn

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529101833891.webp)

最后，需要将`MixColumns` 的输出与轮密钥进行`XOR`, 即进行`AddRoundKey`处理。

解密过程`AddRoundKey — InvMixColumns — InvShiftRows —InvSubBytes`

!!! bug "如果密钥长度为 56 比特，那么用暴力破解找到正确密钥需要平均尝试约$2^{28}$次。 "
    平均尝试次数是密钥总数的大约一半。当密钥长度为56比特时，密钥总数为$2^{56}$个，它的一半是$2^{56}$ ( 注意，不是指数56变成 一半得28,而是减1得55)。 因此，当密钥长度为56比特时，平均尝试次数为$2^{55}$次，大约相当于$3.6\times10^{16}$次。

### 分组密码

分组密码（`block cipher`) 是每次只能处理特定长度的一块数据的一类密码算法，这里的 " —块”就称为分组（`block`)。此外，一个分组的比特数就称为分组长度`blocklength`

- ECB 模式：`Electronic Code Book mode`(电子密码本模式
- CBC 模式：`Cipher Block Chaining mode`(密码分组链接模式）
- CFB 模式：`Cipher Feed Back mode` (密文反馈模式）
- OFB 模式：`Output Feed Back mode` ( 输出反馈模式）
- CTR 模式：`CounTeR mode`(计数器模式）

#### ECB

ECB 模式中，明文分组与密文分组是一一对应的关 系，因此，如果明文中存在多个相同的明文分组，则这些明文分组最终都将被转换为相同的密 文分组。这样一来，只要观察一下密文，就可以知道明文中存在怎样的重复组合，并可以以此 为线索来破译密码，因此 ECB 模式是存在一定风险的。

在 ECB 模式中，只要对任意密文分组进行替换，相应的明文分组也会被替换。此外，Mallory 所能做的还不仅限于替换，例如。如果将密文分组删除，则相应的明文分组 也会被删除，如果对密文分组进行复制，则相应的明文分组也会被复制。

> A 向 B 转账 1 亿元，只要吧密文交换位置，就变成了 B 向 A 转一亿元

#### CBC | `Cipher Block Chaining`

**密码块**：如果输入块重复，将会得到相同的密文块

**密码块链**：

异或第`i`轮输入`m(i)`, 与前一轮的密文，`c(i-1)`  

`c(0)` 明文传输到接收端

$mac=MAC(K_{mac},message)$

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240506084559460.webp" alt="image-20240506084559460" style="zoom:50%;" />

是一种用于分组密码的加密模式。在 CBC 模式中，每个明文分组在加密之前会先与前一个密文分组进行 XOR 运算，然后再进行加密。这种方式使得密文分组之间相互连接，像链条一样

当加密第一个明文分组时，由于不存在前一个密文分组，因此需要使用一个初始化向量（Initialization Vector，IV）来代替。初始化向量是一个随机生成的比特序列，其长度与分组长度相同。每次加密时，都会使用不同的初始化向量，以增加加密的安全性。

CBC 模式的特点包括：

- 明文分组在加密之前一定会与前一个密文分组进行 XOR 运算，因此相同的明文分组在不同的上下文中会产生不同的密文分组。
- 在加密过程中，无法单独对一个中间的明文分组进行加密，因为每个密文分组都依赖于前一个密文分组。

**密文分组损坏**，则最多只有两个分组会受到影响。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529114556558.webp)

bit 缺失

导致密文分组的长度发生变化，此后的分组发生错 位，这样一来，缺失比特的位置之后的密文分组也就全部无法解密了

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529114626002.webp)

确保互联网安全的通信协议之一`SSL/TLS`, 就是使用 CBC 模式来确保通信的机密性的，如使 用 CBC 模式三重 DES 的 3DES_EDE_CBC 以及 CBC 模式 256 比特 AES 的 AES _256_CBC 等。

!!! note "初始化向量"
 在 CBC 模式中，我们假设永远使用相同的初始化向量。于是，当用同一密钥对同一明文进行加密时，所得到的密文一定是相同的。 <br>例如，密码破译者间隔一周收到了两份相同的密文。于是，密码破译者无需破译密码，就可以判断出：这份密文和上周的密文一样，因此两份密文解密所得到的明文也是一样的。如果在每次加密时都改变初始化向量的值，那么即便是用同一密钥对同一明文进行加密，也可以确保每次所得到的密文都不相同。

### 非对称加密

**公钥只能用做数据加密。公钥加密的数据，只能用对应的私钥才能解密。这是非对称加密的核心概念**。

对称密码通过将明文转换为复杂的形式来保证其机密性，相对地，公钥密码则是基于数学上闲难的问题来保证机密性的。例如 RSA 就利用了大整数的质因数分解问题的闲难度。**因此，对称密码和公钥密码源于两种根本不同的思路。**

!!! note "为机密性的高低是根据密钥长度而变化的。"
 这个问题无法冋答，因为机密性的高低是根据密钥长度而变化的。

!!! note "密钥长度为 256 比特的对称密码 AES, 与密钥长度为 1024 比特的公钥密码 RSA 相比，RSA 的安全性更高吗？"
    公钥密码的密钥长度不能直接与对称密码的密钥长度进行比较，而且对不同密码算法的强度进行比较本来就不是一件容易的事。<br>
    尽管如此，在将对称密钥和公钥密码结合起来使用的场景中.我们还是希望使两者的强度保持一定的平衡。很多密码系统中都会给出一些密码算法的理想组合方式，并打包成密码套件( `cipher suite` )<br>
    ![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529122411971.webp)

> 首先，将物品放人寄物柜中。然后，投入硬币并拔出钥匙，就可以将寄物柜关闭了。关闭 后的寄物柜，没有钥匙是无法打开的。 <br>只要有硬币，任何人都可以关闭寄物柜，但寄物柜一旦被关闭，再怎么投币也无法打开。打开寄物柜需要使用钥匙，而不是硬币。 <br>因此我们可以说，硬币是关闭寄物柜的密钥，而钥匙则是打开寄物柜的密钥。

加密

> 我给你一把锁，钥匙只有我自己拿着，你把东西用我的锁锁起来
>

数字签名

> 使用私钥进行盖章，就知道这个锁是来源是谁了

!!! note "案例——小明小红去约会"
    1、小明确定了自己的私钥 mPrivateKey，公钥 mPublicKey。自己保留私钥，将公钥mPublicKey发给了小红<br>
    2、小红确定了自己的私钥 hPrivateKey，公钥 hPublicKey。自己保留私钥，将公钥 hPublicKey 发给了小明<br>
    3、小明发送信息 “周六早10点soho T1楼下见”，并且用小红的公钥 hPublicKey 进行加密。<br>
    4、小红收到信息后用自己的私钥 hPrivateKey 进行解密。然后回复 “收到，不要迟到” 并用小明的公钥mPublicKey加密。<br>
    5、小明收到信息后用自己的私钥 mPrivateKey 进行解密。读取信息后心里暗想：还提醒我不迟到？每次迟到的都是你吧？<br>
    以上过程是一次完整的request和response。通过这个例子我们梳理出一次信息传输的非对称加、解密过程：<br>
    1、消息**接收方**准备好公钥和私钥<br>
    2、私钥**接收方**自己留存、公钥发布给消息**发送方**<br>
    3、消息**发送方**使用接收方公钥对消息进行加密<br>
    4、消息**接收方**用自己的私钥对消息解密<br>

#### RSA | `Rivest, Shamir, Adelson algorithm`

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529115538998.webp)

1978 年，`Ron Rivest`、`Adi Shamir`和`Reonard Adleman`共同发表了一种公钥密码算法 RSA

在中间步骤求 mod，可以避免计算大整数的乘积。这种在计算过程中求 mod 来计算乘方的 方法，也是 RSA 的加密和解密算法中所使用的方法。

两个密钥不一样

- 公钥公开：证书方式

- 私钥：自己保留

RSA 算法过程

**将两个大质数相乘是容易的，但是要将其乘积分解回原来的两个质数却极其困难。**
2004 年 Alexander May 证明了**求 RSA 的私钥和对 N 进行质因数分解**是等价的。

1. 选择两个大质数 $p$ 和 $q$。
2. 计算它们的乘积 $n = pq$，$n$ 的长度就是密钥长度。
3. 计算 $n$ 的欧拉函数 $\phi(n) = (p-1)(q-1)$
4. 选择一个整数 $e$，使得 $e$ 与 $\phi(n)$ 互质，且 $1 < e < \phi(n)$。通常，$e$ 被选为 65537。
5. 计算 $e$ 相对于 $\phi(n)$ 的模逆 $d$，即满足 $ed \equiv 1 \mod \phi(n)$ 的 $d$。

加密：

$$
C = M^e \mod n
$$

解密：

$$
M = C^d \mod n
$$

- $e$(encryption) 和$n$(number) 的组合$\{E,N\}$就是公钥。

- $d$(decryption) 和$n$(number) 的组合$\{D,N\}$就是私钥。(由于 W 是公钥的一部分，是公开的，因此单独将 D 称为私钥也是可以的)

证明目标：显示解密操作确实恢复了原始消息 $M$。

证明过程：

1. 根据欧拉定理，如果 $gcd(M, n) = 1$，则 $M^{\phi(n)} \equiv 1 \mod n$。
2. $ed = 1 + k\phi(n)$ 表示 $e$ 和 $d$ 是模 $\phi(n)$ 的乘法逆元
3. 因此，$M^{ed} = M^{1+k\phi(n)} = M \cdot (M^{\phi(n)})^k$。由于 $M^{\phi(n)} \equiv 1 \mod n$，我们得到 $M^{ed} \mod n = M \mod n$，这证明了解密后我们可以得到原始消息 $M$。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240216123200169.webp" alt="image-20240216123200169" style="zoom:50%;" />

#### 机密性分析

> [[CTF 密码学\]RSA 相关题目解题方法与 python 脚本总结](https://blog.csdn.net/qq_46145027/article/details/125047313)

中间人攻击——消息认证和证书

密码破译者知道的信息

- 密文：可以通过窃听来获取
- 数 E 和 N：公钥是公开的信息。因此密码破译者知道 E 和 N

密码破译者不知道的信息

- 明文：需要破译的内容
- 数 D：私钥中至少 D 是不知道的信息
- 其他：密码破译者不知道生成密钥对时所使用的 p、q 和 L

!!! note "思考：$e$ 和 $\phi(n)$不互质会怎么样？"
    出现多解的情况，$e$ 和 $\phi(n)$不互质，那么没有乘法逆元，不能完全恢复消息

通过密文来求得明文

RSA 加密过程如下。

密文 = 明文^E mod N (RSA 加密)

由于密码破译者知道密文、E 和 N，那么有没有一种方法能够用 E 次方 mod N 之后的密文求出原来的明文呢？如果没有 mod N 的话，即：

密文 = 明文

通过密文求明文的难度不大，因为这可以被看作是一个求对数的问题。

但是，加上 mod N 之后，求明文就变成了求离散对数的问题，这是非常困难的，因为人类还没有发现求离散对数的高效算法。

通过暴力破解来找出 D

现在，RSA 中所使用的 p 和 q 的长度都是 1024 比特以上，N 的长度为 2048 比特以上。由 于 E 和 D 的长度可以和 N 差不多，因此要找出 D，就需要进行 2048 比特以上的暴力破解。要 在这样的长度下用暴力破解找出 D 是极其困难的。

通过 E 和 N 求出 D

那就是质数 p 和 q 不能被密码破译者知道。把 p 和 q 交给密码破译者与把私钥交给密码破译者是等价的。

##### **对 N 进行质因数分解攻击**

一旦发现了对大整数进行质因数分解的高效算法，RSA 就能够被破译

适用情况：n 已知且可因式分解

既然 n = p*q，那么最常规的想法就是把 n 因式分解得到 p,q，上面说 n 很难分解，但对于一些不太大的 n，我们可以借助工具去分解它。下面介绍两种常规因式分解方法：

第一种：在线因式分解网站，例如[factordb.com](http://www.factordb.com/)，我们可以利用在线网站快速分解出 p,q

第二种：yafu 大数分解工具，windows 下载地址：yafu download | SourceForge.net 使用相关命令分解 n

```python
import gmpy2
from Crypto.Util.number import long_to_bytes
 
 
q = 189239861511125143212536989589123569301
p = 386123125371923651191219869811293586459
 
e = 65537
c = 28767758880940662779934612526152562406674613203406706867456395986985664083182
#n = 73069886771625642807435783661014062604264768481735145873508846925735521695159
n = q*p

d = gmpy2.invert(e, (p - 1) * (q - 1))
print("d=",d)
m = pow(c, d, n)

print(m)
print(long_to_bytes(m))
```

##### 通过推测 p 和 q 进行攻击

即便不进行质因数分解，密码破译者还是有可能知道 p 和 q。由于 p 和 q 是通过伪随机数生成器产生的，如果伪随机数生成器的算法很差，密码破译者 就有可能推测出来 q 和 p 因此使用能够被推测出来的随机数是非常危险的。

```python
# 签到题，已知 p,q
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes

p = 0x848cc7edca3d2feef44961881e358cbe924df5bc0f1e7178089ad6dc23fa1eec7b0f1a8c6932b870dd53faf35b22f35c8a7a0d130f69e53a91d0330c0af2c5ab
q = 0xa0ac7bcd3b1e826fdbd1ee907e592c163dea4a1a94eb03fd4d3ce58c2362100ec20d96ad858f1a21e8c38e1978d27cd3ab833ee344d8618065c003d8ffd0b1cb
e = 0x10001
c = 0x39f68bd43d1433e4fcbbe8fc0063661c97639324d63e67dedb6f4ed4501268571f128858b2f97ee7ce0407f24320a922787adf4d0233514934bbd7e81e4b4d07b423949c85ae3cc172ea5bcded917b5f67f18c2c6cd1b2dd98d7db941697ececdfc90507893579081f7e3d5ddeb9145a715abc20c4a938d32131013966bea539

# 因为给了 p,q 相当于就给到了私钥了
n = p * q
phi_n = (p - 1) * (q - 1)

d = mod_inverse(e, phi_n) # 求模逆

m = pow(c, d, n) # 解密方法，求明文

print(m)
print(long_to_bytes(m))
# flag = AAA{Ace_Attorney_is_very_fun_Phoenix_Wright&Miles_Edgeworth}
```

##### 直接开根——N 很大，e 指数很小

```python
# 例题 ZJUAAA SimpleRSA
import gmpy2
from Crypto.Util.number import *

c=431396049519259356426983102577521801906916650819409770125821662319298730692378063287943809162107163618549043548748362517694341497565980142708852098826686158246523270988062866178454564393347346790109724455155942667492571325721344535616869

n=0x6270470b5e45bb464233683c38eeb03d17d54e0127038c9d286b00ac54946cfa1aa05c33610ec439c449b31f705c9e470ab6443cd090f9d88fab68f016c41bc00b9a1def40e77d836252ff03db2a525742e49b824d375216370d1cd810a60e2eac1824f306205c144b54c5f010ae17c8c88e76d1b41f13313cbd7e1b37822a0d

e=3

def de(c, e, n):
    k = 0
    while True:
        m = c + n * k
        result, flag = gmpy2.iroot(m, e)
        if True == flag:
            return result
        k += 1

m = de(c, e, n)
print(m)
print(long_to_bytes(m))
```

#### ECC 椭圆曲线密码学

- 基于椭圆曲线上的离散对数问题（ECDLP），类似 Diffie-Hellman 密钥交换
- $g$是椭圆曲线上的一个公开点，$\alpha$ 是秘密值，计算 $\alpha \cdot g$ 是容易的
但给定 $g$ 和$\alpha \cdot g$，要找到 $\alpha$ 是困难的
- 相比 RSA，ECC 能够在更短的密钥长度下提供相同的安全性

### 混合密码

> 油电混动

对称密码提高速度，用公钥密码保护会话密钥

- 用对称密码加密消息

- 通过伪随机数生成器生成对称密码加密中使用的会话密钥

- 用公钥密码加密会话密钥

- 从混合密码系统外部赋予公钥密码加密时使用的密钥

加密与解密过程

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529135817229.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529135843902.webp)

密钥长度的平衡

混合密码系统中运用了对称密码和公钥密码两种密码方式，无论其中任何一方的密钥过短，都可能遭到集中攻击，因此对称密码和公钥密码的密钥长度必须具备同等的强度。然而考虑到长期运用的情况，公钥密码的强度应该要高于对称密码，因为对称密码的会话密钥被破译只会影响本次通信的内容，而公钥密码一旦被破译，从过去到未来的（用相同公 钥加密的）所有通信内容就都能够被破译了

### 伪随机数生成器

- 生成密钥 用于对称密码和消息认证码。

- 生成密钥对 用于公钥密码和数字签名。

- 生成初始化向量（IV) ：用于分组密码的 CBC、CFB 和 OFB 模式。
- 生成 nonce：用于防御重放攻击以及分组密码的 CTR 模式等。
- 生成盐：于基于口令的密码（PBE) 等。

随机性

不可预测性：避免被攻击者看穿的不可预测性

是指攻击者在知道过去生成的伪随机数列的前提下，依然无法预测出下—个生成出来的伪随机数的性质。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529153557497.webp)

#### 线性同余法

![image](C:/Users/Philfan/AppData/Roaming/Typora/typora-user-images/image-20240529153657516.png)

## 认证

### 散列函数——完整性

散列值，Hash，消息摘要，密码校验和，指纹

发送方、接受方需要确认报文在传输的过程中或者事后没有被改变

> 顺便说一句，单向散列函数中的“散列”的英文“hash”一词，原意是古法语中的“斧子”，后来被引申为“剁碎的肉末”，也许是用斧子一通乱剁再搅在一起的那种感觉吧。单向散列函数的作用，实际上就是将很长的消息剁碎，然后再混合成固定长度的散列值。

生成速度快、抗碰撞性、单向性；不能检测伪装，只能检测篡改

报文 m 报文摘要 H(m)

计算报文摘要的签名$K^-_B(H(m))$
单向散列函数所输出的散列值的长度是固定的

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529140951509.webp" alt="image-20240529140951509" style="zoom: 50%;" />

报文摘要：互异、反向计算特别难

> 一车水果打成果汁，取 1mL 果汁进行签名，足以代表一车水果

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240506091633237.webp)

- 首先，MD5 是不安全的，因此不应该使用。

- SHA-1 除了用于对过去生成的散列值进行校验之外，不应该被用于新的用途
- SHA-2 有效应对了针对 SHA-1 的攻击方法，因此是安全的，可以使用。
- SHA-3 是安全的，可以使用。  

 和对称密码算法一样，**我们不应该使用任何自制算法**。

> **弱抗碰撞性**：要找出和某条消息具备相同散列值的另一条消息是非常困难的
>
> **强抗碰撞性**：找出具有相同散列值但互不相同的两条消息是非常困难的

#### MD5 散列函数

四个步骤计算出 128bit 摘要

```python
>>> import hashlib
>>> m = hashlib.md5()
>>> m.update(b'123')
>>> m.hexdigest()
'202cb962ac59075b964b07152d234b70'
 
# 或者可以这样（最常见的写法，常用于图片的命名）
>>> hashlib.md5(b'123').hexdigest()
'202cb962ac59075b964b07152d234b70'
 
# 也可以使用 hash.new() 这个一般方法，hashlib.new(name[, data])，name 传入的是哈希加密算法的名称，如 md5
>>> hashlib.new('md5', b'123').hexdigest()
'202cb962ac59075b964b07152d234b70'
```

Calculating a checksum using mathematical algorithms

- It is impossible to guess the original data from the message digest
- Regardless of the size of the original data, the resulting message digest can be a fixed size

> This is the reason why it is used for digital signing and tamper-proofing

- A change of a single bit in the original data will result in a different message digest

  > Possibility of generating the same message digest is practically non-existent

MD4 已经被攻破了，MD5 强抗碰撞性被攻破

#### SHA-1 - 160bit 报文摘要（git 使用）

SHA-1 是由 NIST ( National Institute of Standards and Technology, 美国国家标准技术研究所）设计的一种能够产生 160 比特的散列值的单向散列函数。

SHA-1 已经被列入“可谨慎运用的密码清单”，即除了用于保持兼容性的目的以外，其他情况下都不推荐使用。

SHA-1 的强抗碰撞性已于 2005 年被攻破

#### SHA-256

SHA-256、SHA-384 和 SHA512 都是由 NIST 设计的单向散列函数，它们的散列值长度分别为 256 比特、384 比特和 512 比特。这些单向散列函数合起来统称 SHA-2，它们的消息长度也存在上限（SHA-256 的上限接近于 264 比特，SHA-384 和 SHA-512 的上限接近于 2128 比特）。

#### RIPEMD-160

160 比特的散列值的单向散列函数

强抗碰撞性被攻破，但 RIPEMD-160 还没有被攻破

#### SHA-3——Keccak

Secure Hash Algorithm-3 新标准，公开竞争的方式进行标准化

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529144434563.webp" alt="image-20240529144434563" style="zoom:50%;" />

#### 攻击方法

针对弱抗碰撞性的攻击

任何文件中都或多或少地具有一定的冗余性。利用文件的冗余性生成具有相 同散列值的另一个文件，这就是一种针对单向散列函数的攻击。

生日攻击

在这里，Mallory 所进行的攻击不是寻找生成特定散列值的消息，而是要找到散列值相同的 两条消息，而散列值则可以是任意值。这样的攻击，一般称为生日攻击（`birthday attack`) 或者 冲突攻击（`collision attack` )，这是一种试图破解单向散列函数的“强抗碰撞性”的攻击。

> 只要有 23 个人，有两个人生日一样的概率就大于了 50%

### 消息认证——完整性、认证

消息认证码（`Message Authentication Code`) 是一种确认完整性并进行认证的技术，取三个单词的首字母，简称为 MAC。

消息认证码是一种与密钥相关联的单向散列函数，无法保证机密性也无法防止抵赖

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529145807418.webp)

#### 实现方法

**使用单向散列函数实现**：HMAC

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529150336347.webp" alt="image-20240529150336347" style="zoom:50%;" />

使用分组密码实现

分组密码的密钥作为消息认证码的共享密钥来使用，并用 CBC 模式（第 4 章）将消息全 部加密。此时，初始化向量（IV) 是固定的。由于消息认证码中不需要解密，因此将除最后一 个分组以外的密文部分全部丢弃，而将最后一个分组用作 MAC 值。由于 CBC 模式的最后一个 分组会受到整个消息以及密钥的双重影响，因此可以将它用作消息认证码。例如，AES-CMAC ( RFC4493 ) 就是一种基于 AES 来实现的消息认证码。

#### 攻击方法与防御

发送方和接收方需要确认对方的身份。认证目的：避免重放攻击

Nonce: 一生只用一次的整数 (R)

ap4.0: 对称密钥加密

为了证明 Alice 的活跃性，Bob 发送给 Alice 一个 nonce,R. 、

Alice 必须返回加密之后的 R，使用双方约定好的 key

问题：如何分发对称式加密的密钥

ap5.0：非对称密钥加密

Bob 发送 challenge R，Alice 发送私钥加密的报文和公钥，

bob 解密

漏洞：Trudy 中间截获所有，`middle attack`

原因：不能可靠地拿到 Alice 的公钥

### 数字签名——认证、不可抵赖性

数字签名类比于手写签名

- 可验证性（对接收方）

- 不可伪造性（对发送方）

- 不可抵赖性（对第三方）

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529150956820.webp" alt="image-20240529150956820" style="zoom:50%;" />

**用私钥进行这一行为只能由持有私钥的人完成**：数字签名是利用了“没有私钥的人事实上无法生成使用该私钥所生成的密文”这一性质来 实现的。这里所生成的密文并非被用于保证机密性，而是被用于代表一种只有持有该密钥的人 才能够生成的信息。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529151054694.webp)

也可以对消息的散列值签名

!!! note "签名会不会被重复使用"
    签名提取出来这一行为，就好像是现实世界中把纸质合同上的签名拓下来一样。然而在 数字签名中，签名和消息之间是具有对应关系的，消息不同签名内容也会不同，因此事实上是 无法做到将签名提取出来重复使用的。 <br>总之，将一份签名附加在别的消息后面，验证签名会失败。

签名一般不对原文进行签名，而是选择对于原文的哈希值进行签名

### 密钥分发与证书

可信赖中介

> 证书其实和驾照差不多

!!! note "认证机构所做的工作并不是加密，而是对公钥加上数字签名"

#### 对称式解决 | KDC **Key Distribution Center**

为“密钥分发中心”。它是网络安全和加密通信中使用的一个中央服务器，负责分发网络中各方之间通信所需的密钥。

KDC 是 Kerberos 认证协议中的核心组件，主要用于认证服务和分配对称密钥，以确保网络中的数据传输安全。

- 与 KDC 先建立起可信赖的对话关系
- KDC 生成对称密钥

1. **认证请求**：用户客户端向 KDC 的认证服务请求认证，通常包括用户的 ID 和所请求服务的 ID。
2. **TGT 发放**：KDC 验证用户的凭证（如密码）。如果验证成功，KDC 会发放一个票据授权票据（Ticket Granting Ticket, TGT），加密包含用户的权限信息，使用 KDC 的密钥加密。
3. **服务票据请求**：当用户需要访问服务时，客户端使用 TGT 向 KDC 请求针对特定服务的服务票据（Service Ticket）。
4. **服务票据发放**：KDC 验证 TGT，并且如果用户有权限访问请求的服务，KDC 会发放一个服务票据，该票据使用服务的密钥加密，包含用户的身份信息。
5. **服务访问**：用户客户端使用服务票据向服务进行认证。服务解密服务票据，验证用户的权限，然后允许访问。
6. **通信加密**：客户端和服务之间的通信可以使用从 KDC 获得的会话密钥加密，确保数据传输的安全性。

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240216132053873.webp)

#### 非对称解决 | CA Certification Authorities

出厂自带 CA 的公钥

用 CA 的私钥签署了$$CA^-(Bob,K_B^+)$$​

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529152153523.webp)

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240217100652773.webp)

- 串号 (证书发行者唯一)
- 证书拥有者信息，包括算法和密钥值本身 (不显示出来
- 证书发行者信息
- 有效日期
- 颁发者签名

根证书：根证书是未被签名的公钥证书或自签名的证书

- 拿到一些 CA 的公钥
- 渠道：安装 OS 自带的数字证书；从网上下载，你信任的数字证书

信任树：

- 信任了根
- 由根 CA 签署的给一些机构的数字证书，根信任机构
- 由于你信任了根，从而能够可靠地拿到根 CA 签发的证书，可靠地拿到这些机构的公钥

#### Diffie-Hellman

Diffie-Hellman 密钥交换 ( Diffie-Hellman key exchange ) 是 1976 年由 Whitfield Diffie 和 Martin Heilman 共同发明的一种算法。使用这种算法，通信双方仅通过交换一些可以公开的信息 就能够生成出共享的秘密数字，而这一秘密数字就可以被用作对称密码的密钥。IPsec 中就使用 了经过改良的 Diffie-Hellman 密钥交换。

虽然这种方法的名字叫“密钥交换”，但实际上双方并没有真正交换密钥，而是通过计算生 成出了一个相同的共享秘钥。因此，这种方法也称为 Diffie-Hellman 密钥协商（`Diffie-Hellman key agreement` )

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/CS__CTF__assets__05-crypto.assets__image-20240529152845886.webp)

双方交换的数字（即能够被窃听者 Eve 知道的数字）一共有 4 个：P、G,$ G^A \mod P$和$G^B \mod P $。根据这 4 个数字计算出 Alice 和 Bob 的共享密钥（$G^{AxB}\mod P$) 是 非常困难的。

这个问题称为有限域（`finite field`) 的离散对数问题。

而有限域的离散对数问题的复杂度正是支撑 Diffie-Hellman 密钥交换算法的基础。

## 工具与数学计算库

[CyberChef](https://lab.tonycrane.cc/CyberChef/)

- C++ 程序，可以使用 `OpenSSL` 和 `GMP` 等 库进行大数运算
- python 中有许多数学计算库，如 `SciPy`,`gmpy2`

- 商用软件：`Maple`,`Matlab`,`SageMath`

### gmpy2 使用

$x^y \mod n$

```python
gmpy2.powmod(x, y, n)
```

$x^{-1} \mod n$

```python
gmpy2.invert(x, n) 
```

$\sqrt[n]{x}$ exact or not

```python
gmpy2.iroot(x, n)
```

### SageMath

[Sage 线上运行网址](https://sagecell.sagemath.org/)

ubuntu 安装

```shell
apt-get install sagemath
```

docker

```shell
docker pull sagemath sagemath
```

- GF,Zmod

- gcd,inverse_mod,CRT

- vector
- matrix

## OpenSSL 库

### 安装

```shell
sudo apt update && sudo apt install openssl
```

```shell title="验证安装"
openssl version
```

### **密钥生成相关**

**`genpkey`** 生成私钥。  
   示例：  

   ```shell
   openssl genpkey -algorithm RSA -out private_key.pem
   ```

1. **`-algorithm`** 指定加密算法（如 RSA、DSA、EC 等）。
   示例：  

   ```shell
   -algorithm RSA
   ```

2. **`-pkeyopt`** 设置密钥的生成选项，例如位数。  
   示例：  

   ```shell
   -pkeyopt rsa_keygen_bits:2048
   ```

3. **`rsa`** 用于处理 RSA 私钥或从私钥导出公钥。
   示例：  

   ```shell
   openssl rsa -in private_key.pem -pubout -out public_key.pem
   ```

4. **`-pubout`** 将私钥转换为公钥格式导出。

### **文件摘要与哈希**

**`dgst`** 生成文件的摘要（哈希值）。支持多种算法，如 SHA-256、SHA-512 等。

```shell
openssl dgst -sha256 -out hash.txt plain.txt
```

1. **`-sha256`** 指定使用 SHA-256 哈希算法。
2. **`-out`** 指定输出文件路径。
3. **`-verify`** 验证签名时使用，需提供公钥。
4. **`-sign`** 使用私钥对文件或哈希值进行签名。
5. **`-signature`** 指定签名文件路径，用于验证签名。

### **加密与解密**

1. **`rsautl`** 用于非对称加密和解密。主要用于 RSA 算法。
   示例：  

   ```shell
   openssl rsautl -encrypt -inkey public_key.pem -pubin -in plain.txt -out encrypted.bin
   ```

1. **`-encrypt`** 指定加密模式。

1. **`-decrypt`** 指定解密模式。

1. **`-inkey`** 指定密钥文件（公钥或私钥）。

1. **`-pubin`** 表示使用公钥文件。

1. **`-in`** 输入文件路径。

1. **`-out`** 输出文件路径。

---

### **文件查看与调试**

1. **`xxd`** 查看文件的十六进制表示，调试加密或签名文件。  
   示例：  

   ```shell
   xxd encrypted.bin
   ```

### 示例

```shell title="生成文本文件"
echo "Hello, OpenSSL!" > plain.txt
```

```shell title="生成密钥对"
# 生成私钥
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 从私钥生成公钥
openssl rsa -in private_key.pem -pubout -out public_key.pem
```

```shell title="加密文件"
openssl rsautl -encrypt -inkey public_key.pem -pubin -in plain.txt -out encrypted.bin
```

```shell title="验证加密文件内容"
xxd encrypted.bin
```

```shell title="使用私钥解密文件"
openssl rsautl -decrypt -inkey private_key.pem -in encrypted.bin -out decrypted.txt
```

```shell title="私钥进行签名文件"
openssl dgst -sha256 -sign private_key.pem -out signature.bin plain.txt
```

```shell title="使用公钥验证签名"
openssl dgst -sha256 -verify public_key.pem -signature signature.bin plain.txt
```
