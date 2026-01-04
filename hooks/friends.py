import csv
from pathlib import Path


def on_page_markdown(markdown, **kwargs):
    """
    在页面 Markdown 渲染前处理友链页面，从 CSV 文件生成友链卡片
    """
    page = kwargs["page"]
    config = kwargs["config"]

    # 只处理 friends.md 页面
    if page.file.src_path != "friends.md":
        return markdown

    # CSV 文件路径
    csv_path = Path(config["docs_dir"]) / "friend.csv"

    if not csv_path.exists():
        return markdown

    # 读取 CSV 文件
    friends_type0 = []
    friends_type1 = []

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 跳过空行
                if not row.get("Name") or not row.get("Name").strip():
                    continue

                friend_data = {
                    "name": row.get("Name", "").strip(),
                    "link": row.get("Link", "").strip(),
                    "avatar": row.get("Avatar", "").strip(),
                    "desc": row.get("Desc", "").strip(),
                    "type": row.get("Type", "0").strip(),
                    "email": row.get("Email", "").strip(),
                }

                # 根据 type 分类
                if friend_data["type"] == "0":
                    friends_type0.append(friend_data)
                elif friend_data["type"] == "1":
                    friends_type1.append(friend_data)

    except Exception as e:
        print(f"Error reading friend.csv: {e}")
        return markdown

    # 生成友链卡片 HTML
    def generate_friend_card(friend):
        return f'''<div class="flink-list-item">
    <a href="{friend["link"]}" title="{friend["name"]}" target="_blank">
        <div class="flink-item-icon">
            <img src="{friend["avatar"]}" alt="{friend["name"]}">
        </div>
        <div class="flink-item-name">{friend["name"]}</div>
        <div class="flink-item-desc">{friend["desc"]}</div>
    </a>
</div>'''

    # 生成 Type0 友链列表
    type0_html = '<div class="flink-list">\n\n'
    for friend in friends_type0:
        type0_html += generate_friend_card(friend) + "\n\n"
    type0_html += "</div>"

    # 生成 Type1 友链列表
    type1_html = '<div class="flink-list">\n\n'
    for friend in friends_type1:
        type1_html += generate_friend_card(friend) + "\n\n"
    type1_html += "</div>"

    # 替换 markdown 中的占位符
    # 查找并替换 Type1 部分（第一个 flink-list）
    type1_start = markdown.find("## 朋友们")
    if type1_start != -1:
        # 找到 Type1 后面的 <div class="flink-list"> 开始位置
        list_start = markdown.find('<div class="flink-list">', type1_start)
        if list_start != -1:
            # 找到对应的 </div> 结束位置
            list_end = markdown.find("</div>", list_start)
            if list_end != -1:
                list_end += len("</div>")
                # 替换这部分内容
                markdown = markdown[:list_start] + type0_html + markdown[list_end:]

    # 查找并替换学习过的博客部分（第二个 flink-list）
    blog_start = markdown.find("## 记录一些学习过的博客")
    if blog_start != -1:
        # 找到这个标题后面的 <div class="flink-list"> 开始位置
        list_start = markdown.find('<div class="flink-list">', blog_start)
        if list_start != -1:
            # 找到对应的 </div> 结束位置
            list_end = markdown.find("</div>", list_start)
            if list_end != -1:
                list_end += len("</div>")
                # 替换这部分内容
                markdown = markdown[:list_start] + type1_html + markdown[list_end:]

    return markdown
