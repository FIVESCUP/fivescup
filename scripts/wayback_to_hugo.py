#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
waybackmachine/old および new の index.html から記事を抽出し、
content/posts/<slug>/index.md を生成する。
既に content に存在するスラッグはスキップ。old を優先。
"""
import re
import os
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
WAYBACK_OLD = ROOT / "waybackmachine" / "old"
WAYBACK_NEW = ROOT / "waybackmachine" / "new"
CONTENT_POSTS = ROOT / "content" / "posts"

# 除外: カテゴリ・タグ・著者・ページネーション・tournaments・wp-json・css・ルートindex
SKIP_PREFIXES = ("category/", "tag/", "author/", "page/", "tournaments/", "wp-json/", "css/", "embed/")
SKIP_NAMES = ("index",)  # ルートの index.html

# wayback のスラッグのうち、既に別スラッグで移行済みのもの（重複作成しない）
ALREADY_MIGRATED_AS = {"fives-cup-open-1": "fivescup-open-1"}

# 既存の content スラッグ（posts のみ）
def existing_slugs():
    if not CONTENT_POSTS.exists():
        return set()
    return {d.name for d in CONTENT_POSTS.iterdir() if d.is_dir()}

def extract_title(html: str) -> str:
    m = re.search(r"<title>([^<]+)</title>", html, re.IGNORECASE | re.DOTALL)
    if m:
        t = m.group(1).strip()
        for suffix in [" │ S5Projects | FIVESCUP", " | S5Projects | FIVESCUP", " │ S5Works | FIVESCUP"]:
            if t.endswith(suffix):
                t = t[: -len(suffix)].strip()
                break
        return t
    m = re.search(r'<h1[^>]*class="[^"]*heading-singleTitle[^"]*"[^>]*>([^<]+)</h1>', html)
    if m:
        return m.group(1).strip()
    return ""

def extract_date(html: str) -> str:
    m = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    m = re.search(r'icon-calendar">(\d{4})\.(\d{2})\.(\d{2})</li>', html)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return "2019-01-01"

def extract_content_section(html: str) -> str:
    for marker in ('<section class="content">', '<section class="content content-page">'):
        start = html.find(marker)
        if start != -1:
            start += len(marker)
            break
    else:
        return ""
    depth = 1
    i = start
    while i < len(html) and depth > 0:
        if html[i:i+8] == "</section":
            depth -= 1
            if depth == 0:
                return html[start:i]
            i += 8
            continue
        if html[i:i+8] == "<section":
            depth += 1
            i += 8
            continue
        i += 1
    return html[start:start+8000]

def html_to_markdown(raw: str) -> str:
    s = raw
    # 目次ブロックを削除
    s = re.sub(r'<div class="outline">.*?</div>', '', s, flags=re.DOTALL)
    # 内部リンクをサイト内パスに (../slug/index.html -> /posts/slug/ または /slug/)
    def fix_link(href):
        href = href.strip()
        if href.startswith("http"):
            return href
        if href.startswith("../"):
            path = href[3:].replace("/index.html", "").replace("index.html", "").rstrip("/")
            if path and not path.startswith("category") and not path.startswith("tag") and not path.startswith("author"):
                if path in ("rules", "about-fivescup", ""):
                    return f"/{path}/" if path else "/"
                return f"/posts/{path}/"
        return href
    # a タグ
    def replace_a(m):
        href = m.group(1).replace("&amp;", "&")
        body = m.group(2)
        href = fix_link(href)
        return f"[{body}]({href})"
    s = re.sub(r'<a\s+href=["\']([^"\']+)["\'][^>]*>([^<]*)</a>', replace_a, s, flags=re.DOTALL)
    # img は alt があれば残す、なければ削除
    s = re.sub(r'<img[^>]+alt=["\']([^"\']*)["\'][^>]*>', r'![ \1 ]', s)
    s = re.sub(r'<img[^>]*>', '', s)
    # iframe は削除
    s = re.sub(r'<iframe[^>]*>.*?</iframe>', '(埋め込み)', s, flags=re.DOTALL | re.IGNORECASE)
    # 見出し
    s = re.sub(r'<h2\s+id="[^"]*">([^<]*)</h2>', r'\n## \1\n', s)
    s = re.sub(r'<h3\s+id="[^"]*">([^<]*)</h3>', r'\n### \1\n', s)
    s = re.sub(r'<h4\s+id="[^"]*">([^<]*)</h4>', r'\n#### \1\n', s)
    s = re.sub(r'<h2>([^<]*)</h2>', r'\n## \1\n', s)
    s = re.sub(r'<h3>([^<]*)</h3>', r'\n### \1\n', s)
    s = re.sub(r'<h4>([^<]*)</h4>', r'\n#### \1\n', s)
    # strong
    s = re.sub(r'<strong>([^<]*)</strong>', r'**\1**', s)
    s = re.sub(r'<b>([^<]*)</b>', r'**\1**', s)
    # br
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.IGNORECASE)
    # table
    lines = []
    in_table = False
    for line in s.split('\n'):
        if '<table' in line or '<tbody' in line:
            in_table = True
            continue
        if '</table>' in line or '</tbody>' in line:
            in_table = False
            continue
        if in_table:
            row = re.findall(r'<t[hd][^>]*>([^<]*)</t[hd]>', line)
            if row:
                lines.append('| ' + ' | '.join(row) + ' |')
                continue
        lines.append(line)
    s = '\n'.join(lines)
    # ul/li
    s = re.sub(r'<li>([^<]*)</li>', r'- \1\n', s)
    s = re.sub(r'</?ul>', '\n', s, flags=re.IGNORECASE)
    # p
    s = re.sub(r'<p>([^<]*)</p>', r'\1\n\n', s)
    s = re.sub(r'<p>', '\n', s)
    s = re.sub(r'</p>', '\n\n', s)
    # 残りのタグを削除
    s = re.sub(r'<[^>]+>', '', s)
    # 実体参照
    s = s.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
    # 空行整理
    s = re.sub(r'\n{3,}', '\n\n', s).strip()
    return s

def collect_wayback_slugs():
    seen = set()
    order = []
    for base in (WAYBACK_OLD, WAYBACK_NEW):
        if not base.exists():
            continue
        for d in sorted(base.iterdir()):
            if not d.is_dir():
                continue
            slug = d.name
            skip = slug in SKIP_NAMES or any(slug.startswith(p) for p in ("category", "tag", "author", "page", "tournaments", "wp-json", "css"))
            if skip:
                continue
            index_html = d / "index.html"
            if not index_html.exists():
                continue
            if slug not in seen:
                seen.add(slug)
                order.append((base.name, slug, index_html))
    return order

def main():
    existing = existing_slugs()
    candidates = collect_wayback_slugs()
    CONTENT_POSTS.mkdir(parents=True, exist_ok=True)
    created = []
    for source, slug, index_path in candidates:
        if slug in existing:
            continue
        if slug in ALREADY_MIGRATED_AS:
            continue
        html = index_path.read_text(encoding="utf-8", errors="replace")
        title = extract_title(html)
        if not title:
            title = slug
        date = extract_date(html)
        body_html = extract_content_section(html)
        if not body_html.strip():
            continue
        body_md = html_to_markdown(body_html)
        if not body_md.strip():
            body_md = "(本文はWayback Machineのアーカイブから復元した記事です。)"
        post_dir = CONTENT_POSTS / slug
        post_dir.mkdir(parents=True, exist_ok=True)
        front = f'''---
title: "{title.replace('"', '\\"')}"
slug: "{slug}"
date: {date}
categories:
  - "news"
tags:
  - "event"
---

'''
        (post_dir / "index.md").write_text(front + body_md, encoding="utf-8")
        created.append((slug, source))
    for slug, src in created:
        try:
            print(f"Created content/posts/{slug}/ (from wayback {src})")
        except UnicodeEncodeError:
            print(f"Created content/posts/... (from wayback {src})")
    print(f"Total created: {len(created)}")

if __name__ == "__main__":
    main()
