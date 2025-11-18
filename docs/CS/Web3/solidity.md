# Solidity

## 编译器

[remix](https://remix.ethereum.org/)

### 方法 ID

每个 Solidity 函数都有一个唯一的标识符，称为函数选择器或方法 ID。它是函数签名的前 4 个字节的 Keccak-256 哈希值。

#### 计算方法 ID

假设有一个函数签名为`setVars(uint256)`，计算方法 ID 的步骤如下：

1. 获取签名字符串的 Keccak-256 哈希值。
2. 取哈希值的前 4 个字节。

```solidity
pragma solidity ^0.8.0;

contract MethodIDExample {
    function getSelector() public pure returns (bytes4) {
        return bytes4(keccak256("setVars(uint256)"));
    }
}
```

在上面的示例中，`setVars(uint256)`的函数选择器是`bytes4(keccak256("setVars(uint256)"))`。

## 语法

Solidity 是一种面向智能合约的编程语言，主要用于在以太坊区块链上开发智能合约。它是一种静态类型语言，语法类似于 JavaScript，但也有一些自己的特性。

### 1. 基本结构

一个简单的智能合约示例如下：

```solidity
// 声明编译器版本
pragma solidity ^0.8.0;

// 声明合约
contract SimpleStorage {
    // 状态变量
    uint256 storedData;

    // 设置值的函数
    function set(uint256 x) public {
        storedData = x;
    }

    // 获取值的函数
    function get() public view returns (uint256) {
        return storedData;
    }
}
```

### 2. 数据类型

Solidity 支持多种数据类型，包括：

- `uint`/`int`：无符号/有符号整数，可以指定位数（如`uint8`、`uint256`）。
- `bool`：布尔类型，值为`true`或`false`。
- `address`：20 字节的以太坊地址。
- `bytes`/`string`：动态大小的字节数组和字符串。
- `struct`：自定义数据结构。
- `enum`：枚举类型。

### 3. 状态变量和局部变量

- 状态变量：存储在区块链上的数据，定义在合约内。
- 局部变量：只存在于函数调用期间，定义在函数内。

### 4. 函数

函数是合约中的关键部分，定义合约的行为：

- `public`：任何人都可以调用。
- `internal`：只能从内部调用。
- `private`：只能从本合约内部调用。
- `external`：只能从外部调用。

当然，以下是关于 Solidity 文档中`delegatecall`低级函数、如何使用它来委托操作到链上库，以及它对执行范围的影响的介绍。

#### delegatecall

`delegatecall`是 Solidity 中的一种低级函数，允许一个合约在另一个合约的上下文中执行代码。使用`delegatecall`时，被调用合约的代码以调用合约的存储、消息和余额来执行。这意味着在`delegatecall`执行过程中，当前合约的存储、msg.sender 和 msg.value 不会改变，而是继续引用原来的上下文。

**用法**

假设有两个合约，合约 A 和合约 B。合约 A 希望使用合约 B 的某些功能。可以使用`delegatecall`将操作委托给合约 B：

```solidity
contract B {
    uint public num;
    address public sender;
    uint public value;

    function setVars(uint _num) public payable {
        num = _num;
        sender = msg.sender;
        value = msg.value;
    }
}

contract A {
    uint public num;
    address public sender;
    uint public value;

    function setVars(address _contract, uint _num) public payable {
        // A的存储将被改变，B的存储不会改变
        (bool success, bytes memory data) = _contract.delegatecall(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
    }
}
```

在上面的示例中，当调用 A 合约的`setVars`方法时，`delegatecall`将 B 合约中的`setVars`函数在 A 合约的上下文中执行。因此，A 合约中的`num`、`sender`和`value`会被更新，而 B 合约中的相应变量不会改变。

**影响**

`delegatecall`的执行范围影响如下：

1. **存储**：调用者合约的存储被使用和修改，被调用合约的存储不受影响。
2. **msg.sender**：保持为最初调用者，而不是被调用合约。
3. **msg.value**：保持为最初发送的值，而不是被调用合约。

#### Fallback 方法

在 Solidity 中，`fallback`方法是一种特殊的函数，当调用一个合约时，如果该合约中没有匹配的函数签名，或者直接发送以太币而不调用任何函数时，`fallback`函数会被调用。Solidity 还引入了一个新的`receive`函数用于接收纯以太币转账。

- `fallback`：用来处理所有不匹配函数调用和无数据的直接转账。
- `receive`：专门用于处理无数据的纯以太币转账。

```solidity
contract FallbackExample {
    event LogFallback(address sender, uint value, bytes data);
    event LogReceive(address sender, uint value);

    fallback() external payable {
        emit LogFallback(msg.sender, msg.value, msg.data);
    }

    receive() external payable {
        emit LogReceive(msg.sender, msg.value);
    }
}
```

### 5. 修饰符

修饰符用于改变函数的行为，例如：

- `view`：声明函数不会修改状态。
- `pure`：声明函数不读取也不修改状态。
- `payable`：声明函数可以接收以太币。

### 6. 事件

事件用于记录交易日志，前端可以监听这些事件：

```solidity
event StoredDataChanged(uint256 newValue);

function set(uint256 x) public {
    storedData = x;
    emit StoredDataChanged(x);
}
```

### 7. 继承

Solidity 支持合约继承：

```solidity
contract Parent {
    function foo() public pure returns (string memory) {
        return "Parent";
    }
}

contract Child is Parent {
    function bar() public pure returns (string memory) {
        return "Child";
    }
}
```

### 8. 库

库是一种特殊的合约，不能有状态变量，不能继承或被继承：

```solidity
library Math {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        return a + b;
    }
}

contract Test {
    using Math for uint256;

    function testAdd(uint256 a, uint256 b) public pure returns (uint256) {
        return a.add(b);
    }
}
```

### 9. 接口

接口定义函数而不实现：

```solidity
interface IExample {
    function exampleFunction() external;
}

contract Example is IExample {
    function exampleFunction() external override {
        // 实现函数
    }
}
```

### 10. 错误处理

使用`require`、`assert`和`revert`进行错误处理：

```solidity
function testRequire(uint256 a) public pure {
    require(a > 10, "Value must be greater than 10");
}

function testAssert(uint256 a) public pure {
    assert(a != 0);
}

function testRevert(uint256 a) public pure {
    if (a == 0) {
        revert("Value cannot be zero");
    }
}
```
