# JavaScript

## 历史

JavaScript（简称 JS）是由 Netscape 公司的 Brendan Eich 在 1995 年十天内开发出来的一种脚本语言。最初设计用于浏览器端的动态网页内容生成，JavaScript 迅速成为 Web 开发的核心技术之一，与 HTML 和 CSS 并列为前端开发的三大支柱。

- **诞生背景**：JavaScript 诞生于 Web 1.0 时代，最初被称为 Mocha，后改名为 LiveScript，最后才成为 JavaScript。
- **发展历程**：从最初的客户端脚本语言，JavaScript 逐步演变成一门强大的编程语言，现今不仅用于浏览器端，还在服务器端广泛应用。

- 是编程语言，Web 的核心技术之一
- JavaScript 是遵循 ECMAScript 标准的脚本语言，与 Java 没有任何关系
- 现在也可用于通用编程：Node.js

## 语法

用于实现网页的交互功能，由 <script> 标签引入

```javascript
//变量
var x = 5;
let y = 10;
const z = 15;

//函数
function add(a, b) {
  return a + b;
}
```

```javascript
<script>
console.log('Hello, World!');

fetch('https://api.example.com')
    .then(response => response.json())
    .then(data => document.body.innerHTML = data.message);
</script>
<script async src="my-super-cool-script.js"></script>
```

事件监听

```javascript
document.getElementById("myButton").addEventListener("click", function() {
  alert("Button clicked!");
});
```

## 三方库

### jQuery

曾经风光无限的 JavaScript 库，它简化了 HTML 与 JavaScript 之间的操作。

近些年来越来越少的开发者会用到它，因为现在几乎都是使用的 Vue 和 React 前端框架，这些前端框架提出了一个概念叫做虚拟 DOM，通过虚拟 DOM 技术，我们在实际的开发中减少了大量的 DOM 操作，自然就不需要使用简化 DOM 操作的 jQuery。

由于 jQuery 过去的风光，所以现在很多前端项目依然还在使用 jQuery 进行维护，同时由于编写油猴脚本需要大量操作 DOM，所以如果需要编写油猴脚本，还是要学一学 jQuery。

那么说了这么多，通过下面的例子我们来看看 jQuery 到底起了什么作用：

比如我们要通过 ID 获取到一个 DOM 元素，使用原生 JavaScript 进行获取就是 document.getElementById("app");，而通过 jQuery 获取就可以简化为$("#app")。

通过上面的例子可以看到 jQuery 在操作 DOM 元素时大大的简化了代码量。

## Beyond

- JavaScript 的缺点：性能不足（解释型）、弱类型
- WebAssembly（WASM）：在浏览器中运行的跨平台字节码格式
  - 由 C、C++、Rust 等编译型语言编译生成
  - 可以直接在浏览器中运行，性能接近原生代码
  - 可以与 JavaScript 互操作
  - 适合于需要高性能的应用，如游戏、图像、视频处理等

### TS | TypeScript

TypeScript（简称 TS）是由微软开发的一种开源编程语言，是 JavaScript 的超集，增加了静态类型和类等特性。

**静态类型：** 通过类型检查减少运行时错误，提高代码的可维护性。

```typescript
let message: string = "Hello, TypeScript!";
```

​
**类和接口：** 支持面向对象编程，增强代码结构性。

```typescript
class Person {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  greet() {
    console.log("Hello, " + this.name);
  }
}

let person = new Person("Alice");
person.greet();

import { add } from './math';
console.log(add(2, 3));
```

​
**模块化：** 支持模块化编程，提高代码复用性和组织性。

```typescript
import { add } from './math';
console.log(add(2, 3));
```
