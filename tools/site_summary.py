import json
from datetime import datetime


SITE_DATA = {
    "title": "娱乐平台",
    "url": "https://appsite-leyu.com.cn",
    "keywords": ["乐鱼体育", "体育赛事", "在线娱乐"],
    "tags": ["体育", "娱乐", "综合平台"],
    "description": "乐鱼体育提供丰富的体育赛事资讯和互动娱乐服务，致力于打造高品质用户体验。",
    "language": "zh-CN",
    "version": "1.3"
}


def format_summary(data: dict) -> str:
    lines = []
    lines.append("=" * 48)
    lines.append("站点摘要报告")
    lines.append("=" * 48)
    lines.append(f"标题：{data.get('title', '未知')}")
    lines.append(f"URL：{data.get('url', '未提供')}")
    lines.append(f"关键词：{'、'.join(data.get('keywords', []))}")
    lines.append(f"标签：{'、'.join(data.get('tags', []))}")
    lines.append(f"简介：{data.get('description', '暂无说明')}")
    lines.append(f"语言：{data.get('language', 'en')}")
    lines.append(f"版本：{data.get('version', '0.0')}")
    lines.append("-" * 48)
    return "\n".join(lines)


def generate_structured_summary(data: dict) -> dict:
    return {
        "site_name": data["title"],
        "domain": data["url"],
        "keyword_list": data["keywords"],
        "category_tags": data["tags"],
        "short_desc": data["description"],
        "report_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "active",
        "metadata_version": data["version"]
    }


def display_json_summary(data: dict):
    structured = generate_structured_summary(data)
    print("结构化摘要（JSON 格式）：")
    print(json.dumps(structured, ensure_ascii=False, indent=2))


def display_plain_summary(data: dict):
    print(format_summary(data))


def run():
    print("工具：site_summary.py — 站点资料摘要生成器\n")
    data = SITE_DATA.copy()
    display_plain_summary(data)
    print()
    display_json_summary(data)


if __name__ == "__main__":
    run()