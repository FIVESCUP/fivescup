#!/usr/bin/env python3
"""
Fix internal links in Hugo content for GitHub Pages (baseURL .../fivescup/).
- /rules/ -> ../../rules/ (from posts)
- /posts/SLUG/ -> ../SLUG/
- / or ../index.html -> ../../ (home)
- Remove WordPress category sidebar blocks, replace with single link to ../../posts/
"""
import re
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
POSTS = CONTENT / "posts"


def fix_links_in_posts(text: str) -> str:
    # /rules/ -> ../../rules/
    text = re.sub(r'\]\(/rules/\)', '](../../rules/)', text)
    # /posts/anything/ -> ../anything/
    text = re.sub(r'\]\(/posts/([^)]+)/\)', r'](../\1/)', text)
    # ](/) -> ](../../)  (link to home)
    text = re.sub(r'\]\(/\)', '](../../)', text)
    # ](../index.html) -> ](../../)
    text = re.sub(r'\]\(\.\./index\.html\)', '](../../)', text)
    return text


def remove_category_block(text: str) -> str:
    """Replace WordPress category sidebar with single 投稿一覧 link; collapse duplicates."""
    # Match a line that is optional whitespace + [anything](../category/...)
    category_line = re.compile(
        r'^\s*\[[^\]]*\]\(\.\./category/[^)]+\)\s*$',
        re.MULTILINE
    )
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if category_line.match(line):
            # Skip entire run of category lines, emit one link only once
            if not out or out[-1].strip() != '[投稿一覧](../../posts/)':
                out.append('')
                out.append('[投稿一覧](../../posts/)')
                out.append('')
            while i < len(lines) and category_line.match(lines[i]):
                i += 1
            continue
        out.append(line)
        i += 1
    text = '\n'.join(out)
    # Collapse duplicate [投稿一覧] lines (with optional blank lines between)
    text = re.sub(r'(\n\s*\[投稿一覧\]\(../../posts/\)\s*\n)(\s*\n\s*\[投稿一覧\]\(../../posts/\)\s*\n)+', r'\1\n', text)
    return text


def process_file(path: Path) -> bool:
    try:
        raw = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Read error {path}: {e}")
        return False
    new_text = fix_links_in_posts(raw)
    new_text = remove_category_block(new_text)
    if new_text != raw:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def main():
    changed = 0
    for md in sorted(POSTS.rglob("index.md")):
        if process_file(md):
            changed += 1
    print(f"Updated {changed} files.")


if __name__ == "__main__":
    main()
