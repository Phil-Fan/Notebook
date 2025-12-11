"""
TOC Manager for MkDocs
改编自 https://github.com/TonyCrane/note/tree/master/hooks
todo: template 修改的好看一些
"""

import os
import re
import time
import logging
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional, Union
from pathlib import Path

import yaml
from git import Repo, Git
from jinja2 import Template
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files

logger = logging.getLogger("mkdocs.hooks.toc")

@dataclass
class Statistics:
    """
    文档统计信息数据类
    用于存储文档的字数、代码行数、阅读时间等统计数据
    """
    words: int = 0        # 文档总字数（中英文）
    codes: int = 0   # 代码总行数
    read_time: int = 0    # 预计阅读时间（分钟）
    update_time: int = 0  # 最后更新时间（Unix 时间戳）

class GitManager:
    """
    Git 仓库管理器
    提供高效的 Git 仓库操作和缓存机制
    """
    _repo_cache: Dict[str, Git] = {}
    
    @classmethod
    def get_repo(cls, path: Union[str, Path]) -> Git:
        """
        获取 Git 仓库实例，使用缓存机制避免重复初始化
        
        参数：
            path: 文件或目录路径
            
        返回：
            Git 仓库实例
            
        说明：
            - 对于文件路径，自动获取其所在目录
            - 使用路径作为缓存键，避免重复创建仓库实例
            - 支持向上查找父目录中的 Git 仓库
        """
        path = Path(path).resolve()
        if not path.is_dir():
            path = path.parent
            
        cache_key = str(path)
        if cache_key not in cls._repo_cache:
            cls._repo_cache[cache_key] = Repo(path, search_parent_directories=True).git
        return cls._repo_cache[cache_key]
    
    @staticmethod
    def get_latest_commit_time(path: Union[str, Path], ignore_commits: List[str] = None) -> int:
        """
        获取文件最后一次有效提交的时间戳
        
        参数：
            path: 文件路径
            ignore_commits: 需要忽略的提交 SHA 列表
            
        返回：
            最后一次有效提交的 Unix 时间戳
            
        说明：
            - 可以通过 ignore_commits 列表忽略特定的提交
            - 如果所有提交都被忽略，返回当前时间戳
            - 出现错误时会记录警告并返回当前时间戳
        """
        path = Path(path).resolve()
        repo = GitManager.get_repo(path)
        
        if not ignore_commits:
            try:
                timestamp = repo.log(str(path), format="%at", n=1)
                return int(timestamp) if timestamp else int(time.time())
            except Exception as e:
                logger.warning(f"获取{path}的提交时间失败：{e}")
                return int(time.time())
                
        try:
            commits = repo.log(str(path), format="%H %at", follow=True).splitlines()
            for commit in commits:
                sha, timestamp = commit.split()
                if not any(sha.startswith(ic) for ic in ignore_commits):
                    return int(timestamp)
        except Exception as e:
            logger.warning(f"获取{path}的提交历史失败：{e}")
            
        return int(time.time())

class MarkdownProcessor:
    """
    Markdown 文档处理器
    提供高效的 Markdown 文本处理和统计功能
    """
    
    @staticmethod
    def process_markdown(content: str) -> Tuple[int, int, int]:
        """
        处理 Markdown 内容并返回统计信息
        修复了代码行数统计的问题，现在正确处理代码块
        """
        # 提取代码块，保留完整内容
        code_blocks = []
        lines = content.split('\n')
        in_code_block = False
        current_block = []
        
        for line in lines:
            if line.strip().startswith('```'):
                if in_code_block:
                    current_block.append(line)
                    code_blocks.append('\n'.join(current_block))
                    current_block = []
                else:
                    current_block = [line]
                in_code_block = not in_code_block
            elif in_code_block:
                current_block.append(line)
                
        # 移除代码块
        for block in code_blocks:
            content = content.replace(block, '')
        
        # 清理 Markdown 语法
        content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
        content = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", content)
        content = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", content)
        content = re.sub(r"</?[^>]*>", "", content)
        content = re.sub(r"[#*`~\-–^=<>+|/:]", "", content)
        
        # 统计字数
        chinese_chars = len(re.findall(r"[\u4e00-\u9fa5]", content))
        english_words = len(re.findall(r"\b[a-zA-Z0-9]+\b", content))
        
        # 正确计算代码行数（不包括首尾的 ```）
        codes = 0
        for block in code_blocks:
            lines = block.split('\n')
            if len(lines) > 2:  # 确保至少有开始、内容和结束
                codes += len(lines) - 2  # 减去首尾的 ``` 行
        
        words = chinese_chars + english_words
        read_time = round(words / 300 + codes / 80)  # 标准阅读速度
        
        return words, codes, read_time

class TOCManager:
    """
    目录管理器主类
    负责生成和管理文档的目录结构
    """

    _FULLWIDTH_PUNCT_MAP = str.maketrans({
        "：": ":",
        "﹕": ":",  # 兼容少数输入法的全宽冒号
    })
    
    def __init__(self, template_path: Union[str, Path]):
        """
        初始化目录管理器
        
        参数：
            template_path: 目录模板文件的路径
            
        说明：
            - 读取并编译目录模板
            - 模板用于生成最终的 HTML 目录结构
        """
        self.template_path = Path(template_path)
        with open(self.template_path, 'r', encoding='utf-8') as f:
            self.template = Template(f.read())
            
    def _normalize_path(self, path: str, use_directory_urls: bool) -> str:
        """
        规范化 URL 路径
        
        参数：
            path: 原始路径
            use_directory_urls: 是否使用目录形式的 URL
            
        返回：
            规范化后的 URL 路径
            
        说明：
            - 保持外部链接和锚点不变
            - 根据配置转换内部链接格式
            - 支持 index.md 特殊处理
        """
        # 保持绝对 URL 不变
        # print(path)
        if path.startswith(("http://", "https://", "#")):
            return path
            
        # 处理页内锚点
        if path.startswith("#"):
            return path
            
        # 规范化 markdown 路径
        if path.endswith(".md"):
            if use_directory_urls:
                # index.md -> 目录 URL
                if path.endswith("index.md"):
                    return path[:-8]
                return path[:-3] + "/"
            else:
                return path[:-3] + ".html"
        elif path.endswith("index"):
            return path + ".html"
        elif path.endswith("/"):
            return path + "index.html"
        else:
            return path + ".html"
        
    def get_file_statistics(self, path: Path, ignore_commits: List[str] = None) -> Statistics:
        """
        获取文件或目录的统计信息
        
        参数：
            path: 文件或目录路径
            ignore_commits: 需要忽略的提交列表
            
        返回：
            Statistics 对象，包含统计信息
            
        说明：
            - 支持单个文件和整个目录的统计
            - 递归处理目录中的所有.md 文件
            - 合并统计信息，包括更新时间
        """
        stats = Statistics()
        
        if not path.exists():
            return stats
            
        if path.is_dir():
            for md_file in path.rglob("*.md"):
                file_stats = self.get_file_statistics(md_file, ignore_commits)
                stats.words += file_stats.words
                stats.codes += file_stats.codes
                stats.read_time += file_stats.read_time
                stats.update_time = max(stats.update_time, file_stats.update_time)
        else:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    words, codes, read_time = MarkdownProcessor.process_markdown(f.read())
                    stats.words = words
                    stats.codes = codes
                    stats.read_time = read_time
                    stats.update_time = GitManager.get_latest_commit_time(path, ignore_commits)
            except Exception as e:
                logger.error(f"处理文件{path}失败：{e}")
                
        return stats
        
    def process_toc_item(self, item: dict, base_path: Path, use_directory_urls: bool) -> dict:
        """
        处理单个目录项
        
        参数：
            item: 目录项配置字典
            base_path: 基础路径
            use_directory_urls: 是否使用目录形式的 URL
            
        返回：
            处理后的目录项字典
            
        说明：
            - 支持简单键值对和嵌套结构
            - 处理 index 文件和普通文件
            - 计算每个文件的统计信息
            - 按更新时间排序子项
        """
        result = {"n": 0}
        
        title = next(iter(item.keys()))
        result["title"] = title
        
        if isinstance(item[title], str):
            # 获取相对于 base_path 的路径
            rel_path = item[title]
            abs_path = Path(base_path) / rel_path
            
            # 生成相对 URL
            result["link"] = self._normalize_path(rel_path, use_directory_urls)
            
            # 获取统计信息
            stats = self.get_file_statistics(abs_path)
            result.update(vars(stats))
            result["contents"] = [{
                "title": title,
                "link": result["link"],
                **vars(stats)
            }]
            
        elif isinstance(item[title], list):
            contents = []
            for entry in item[title]:
                if not isinstance(entry, dict):
                    continue
                    
                key = next(iter(entry.keys()))
                value = entry[key]
                
                if key == "index":
                    # 处理索引文件
                    rel_path = value
                    abs_path = Path(base_path) / rel_path
                    result["link"] = self._normalize_path(rel_path, use_directory_urls)
                    stats = self.get_file_statistics(abs_path)
                    
                    result.update(vars(stats))
                else:
                    # 处理常规文件
                    rel_path = value
                    abs_path = Path(base_path) / rel_path
                    stats = self.get_file_statistics(abs_path)
                    # print("stats=",stats)
                    # print({**vars(stats)})
                    contents.append({
                        "title": key,
                        "link": self._normalize_path(rel_path, use_directory_urls),
                        **vars(stats)
                    })
            
            if contents:
                contents.sort(key=lambda x: x["update_time"], reverse=True)
            result["contents"] = contents
                
        return result

    def process_markdown(self, content: str, page: Page, config: MkDocsConfig) -> str:
        """
        处理 Markdown 内容并生成目录
        
        参数：
            content: Markdown 内容
            page: MkDocs 页面对象
            config: MkDocs 配置对象
            
        返回：
            处理后的 Markdown 内容
            
        说明：
            - 查找并解析目录标记
            - 处理 YAML 格式的目录配置
            - 生成 HTML 格式的目录
            - 替换原始标记为生成的 HTML
        """
        if "{{ BEGIN_TOC }}" not in content or "{{ END_TOC }}" not in content:
            return content
            
        try:
            toc_yml = content.split("{{ BEGIN_TOC }}")[1].split("{{ END_TOC }}")[0]
            toc_yml = self._normalize_toc_yaml(toc_yml)
            toc_config = yaml.safe_load(toc_yml)
            
            base_path = Path(page.file.abs_src_path).parent
            toc_items = []
            
            for i, item in enumerate(toc_config):
                processed_item = self.process_toc_item(item, base_path, config.use_directory_urls)
                processed_item["n"] = i
                toc_items.append(processed_item)
                
            toc_html = self.template.render(items=toc_items)
            return re.sub(
                r"\{\{ BEGIN_TOC \}\}.*\{\{ END_TOC \}\}",
                toc_html,
                content,
                flags=re.DOTALL
            )
            
        except Exception as e:
            logger.error(f"处理目录失败：{e}")
            return content

    def _normalize_toc_yaml(self, toc_yml: str) -> str:
        """兼容 full-width 冒号导致的 YAML 解析失败"""
        if not toc_yml:
            return toc_yml

        normalized = toc_yml.translate(self._FULLWIDTH_PUNCT_MAP)

        fixed_lines = []
        for line in normalized.splitlines():
            if "://" not in line:
                line = re.sub(r":(?=\S)", ": ", line)
            fixed_lines.append(line)

        return "\n".join(fixed_lines)

# 全局 TOC 管理器实例
_toc_manager = None

def get_toc_manager() -> TOCManager:
    """
    获取或创建全局 TOC 管理器实例
    
    返回：
        TOC 管理器实例
        
    说明：
        - 使用单例模式
        - 延迟初始化，首次使用时才创建实例
        - 自动查找模板文件
    """
    global _toc_manager
    if _toc_manager is None:
        template_path = Path(__file__).parent / "templates" / "toc.html"
        _toc_manager = TOCManager(template_path)
    return _toc_manager

def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, **kwargs) -> str:
    """
    MkDocs 的页面处理钩子函数
    
    参数：
        markdown: 原始 Markdown 内容
        page: MkDocs 页面对象
        config: MkDocs 配置对象
        **kwargs: 额外参数
        
    返回：
        处理后的 Markdown 内容
        
    说明：
        - MkDocs 插件系统的入口点
        - 调用 TOC 管理器处理页面内容
        - 处理失败时保持原内容不变
    """
    return get_toc_manager().process_markdown(markdown, page, config)
