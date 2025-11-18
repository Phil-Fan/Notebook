---
date:
  created: 2025-10-17
  updated: 2025-10-17
readtime: 3
pin: false
categories:
  - Settings
tags:
  - Mkdocs
authors:
  - Phil-Fan
nostatistics: true
---

# Mkdocs 瘦身

## 图片 to 图床

由于图片特别多，而且之前的图床文件又很大了，将近 800MB，所以决定重新换一下

可能之后图床这块的费用要大一些

## 一些查看命令

### 命令（先预览，再删除）

- 先预览将被删除的所有 `assets` 目录：

```bash
find "/Users/philfan/CodeSource/Phil-Fan.github.io/docs" -type d -name assets -print
```

- 确认无误后，执行删除：

```bash
find "/Users/philfan/CodeSource/Phil-Fan.github.io/docs" -type d -name assets -exec rm -rf {} +
```

### 文件大小统计并排序（macOS，按字节）

- 仅看最大的 20 个文件

```bash
find "/Users/philfan/CodeSource/Phil-Fan.github.io" -type f -exec stat -f "%z %N" {} + | sort -n | tail -20
```

- 统计指定路径下一层目录/文件大小并按大小排序（人类可读）

```bash
du -h -d 1 
```
