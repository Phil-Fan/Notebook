# MCP

## 简介与洞见

![image](https://philfan-pic.oss-cn-beijing.aliyuncs.com/web_pic/Tools__Environment__assets__MCP.assets__20250408080715.webp)

MCP 类似一个拓展坞，让大模型理解如何使用工具。

就类似于一个互联网上的服务器，MCP 告诉 LLM 如何使用工具，如何调用工具，让 LLM 调用工具，MCP 返回结果。

MCP 并不是最早出现的类似事物，之前就有很多类似的尝试，比如：

- OpenAI plugins：限制于 OpenAI 的生态
- longchain：抽象层数太多，想要囊括的太多
- pydantic：使用 python 抽象器进行抽象

!!! note "把时间花在解决问题上面，而不是 build server"
    mcp作为distribute一个好的方式

当我们使用一个工具的时候，我们不仅仅是在使用这个工具，更是接受这个工具对于未来的设想与设计

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114213045405352&bvid=BV1cho6YPEeR&cid=29035724975&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

## 有用资源

[awesome-mcp-servers/README-zh.md at main · punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-zh.md)

## 环境配置

一个简单 demo

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114073660301264&bvid=BV1eYPpeWEnT&cid=28597289610&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

[Cursor – Model Context Protocol](https://docs.cursor.com/context/model-context-protocol)

[Introduction - Model Context Protocol](https://modelcontextprotocol.io/introduction)

## 使用的 server

### Playwright

[microsoft/playwright-mcp: Playwright MCP server](https://github.com/microsoft/playwright-mcp?tab=readme-ov-file)

### sequentialthinking

[reference-servers/src/sequentialthinking at main · smithery-ai/reference-servers](https://github.com/smithery-ai/reference-servers/tree/main/src/sequentialthinking)

```bash
npm install playwright && npx playwright install chrome
```

### iTerm-MCP

[ferrislucas/iterm-mcp: A Model Context Protocol server that executes commands in the current iTerm session - useful for REPL and CLI assistance](https://github.com/ferrislucas/iterm-mcp)

[reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration)
