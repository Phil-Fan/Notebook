# Next.js

## 安装

- **依赖**：在已有 React 项目内手动安装 `next`、`react`、`react-dom`，再补充脚本即可。

```bash
npm install next@latest react react-dom
```

```jsonc
// package.json (scripts 摘要)
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
```

- **开发体验**：`npm run dev` 默认在 `http://localhost:3000` 启动开发服务器（Turbopack），保存 `app/page.tsx` 或 `pages/index.tsx` 后会热更新；`next build` 产出生产包，`next start` 读取 `.next` 目录托管产物。
- **可选配置**：根据需要添加 `next.config.(js|ts|mjs)`、`tsconfig.json`、`.eslintrc` 等文件；若在 monorepo 中，记得让 `next.config` 所在的 Next.js 项目根与仓库根区分开。

## 脚手架

`create-next-app` 是官方脚手架，可快速生成一套包含 TypeScript、ESLint、Tailwind CSS、App Router、Turbopack 与 `@/*` Alias 的推荐默认模版。

```bash
npx create-next-app@latest my-app
cd my-app
npm run dev
```

执行命令后可选择：

1. 是否启用 TypeScript、React Compiler、Tailwind CSS；
2. 使用 ESLint、Biome 或不启用 Lint；
3. 代码是否放在 `src/` 目录；
4. 选择 App Router 或 Pages Router；
5. 自定义 import alias。

脚手架也支持 `--example` 拉取官方示例，为测试、PWA 等场景准备好的模版会自动连同 Playwright 等依赖一起生成。

## 文件结构

- **App Router**：在项目根（或 `src/`）中创建 `app/` 目录。任意文件夹都会映射为一个路由段，但必须包含 `page.tsx`/`page.jsx` 或 `route.ts` 才能对外暴露。根目录必须包含 `app/layout.tsx`（Root Layout），显式返回 `<html>` 与 `<body>`，相当于原 `pages/_app.tsx + _document.tsx`。
- **Colocation**：可以把组件、数据请求逻辑、测试等文件与路由段放在同一层，因为只有 `page`/`route` 的返回内容才会发送到客户端；若不想混合，也可把非路由代码放在 `src/` 外部。
- **公共资源**：所有静态资源放在 `public/`，`next/image` 组件可以直接引用 `/logo.png` 等路径；Manifest、Icons 等 PWA 资源也建议放在该目录。
- **配置与辅助文件**：`next.config.*`、`.env*`、`tsconfig.json` 等需要位于项目根目录。App Router 额外支持 `app/manifest.ts`、`app/icon.png`、`app/robots.ts` 这类文件约定；API Route 则位于 `app/api/**/route.ts`。
- **脚本与产物**：开发阶段输出写入 `.next/dev`，正式构建写入 `.next`。记得把 `.next`、`.next/dev`、`next-env.d.ts` 写入 `.gitignore`，避免将构建结果提交到仓库。
