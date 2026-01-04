.PHONY: help serve format format-md format-py install-dev clean build check-tools

# 获取项目根目录
PROJECT_ROOT := $(shell pwd)

# 默认目标
help:
	@echo "可用命令："
	@echo "  make serve       - 启动 Mkdocs 开发服务器"
	@echo "  make format      - 格式化所有文件（Markdown + Python）"
	@echo "  make format-md   - 格式化 Markdown 文件"
	@echo "  make format-py   - 格式化 Python 文件"
	@echo "  make install-dev - 安装开发依赖"
	@echo "  make build       - 构建 Mkdocs 站点"
	@echo "  make clean       - 清理构建文件"
	@echo "  make check-tools - 检查格式化工具是否已安装"

# 启动 Mkdocs 开发服务器
serve:
	JUPYTER_PLATFORM_DIRS=1 uv run mkdocs serve

# 格式化所有文件
format: format-md format-py
	@echo "✓ 格式化完成"

# 格式化 Markdown 文件
format-md:
	@echo "→ 格式化 Markdown 文件..."
	markdownlint "$(PROJECT_ROOT)" --fix -c "$(PROJECT_ROOT)/.github/.markdownlint.json"
	autocorrect "$(PROJECT_ROOT)/docs" --fix
	@echo "✓ Markdown 格式化完成"

# 格式化 Python 文件
format-py:
	@echo "→ 格式化 Python 文件..."
	uv run ruff check --fix "$(PROJECT_ROOT)"
	@echo "✓ Python 格式化完成"

# 安装开发依赖
install-dev:
	@echo "→ 安装开发依赖..."
	uv sync --extra dev
	@echo "✓ 开发依赖安装完成"

# 构建 Mkdocs 站点
build:
	@echo "→ 构建 Mkdocs 站点..."
	uv run mkdocs build
	@echo "✓ 构建完成"

# 清理构建文件
clean:
	@echo "→ 清理构建文件..."
	rm -rf "$(PROJECT_ROOT)/site"
	@echo "✓ 清理完成"

# 检查格式化工具是否已安装
check-tools:
	@echo "→ 检查格式化工具..."
	@command -v markdownlint >/dev/null 2>&1 && echo "✓ markdownlint 已安装" || echo "✗ markdownlint 未安装"
	@command -v autocorrect >/dev/null 2>&1 && echo "✓ autocorrect 已安装" || echo "✗ autocorrect 未安装"
	@uv run ruff --version >/dev/null 2>&1 && echo "✓ ruff 已安装（通过 uv）" || echo "✗ ruff 未安装"
