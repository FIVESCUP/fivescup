#!/usr/bin/env python3
"""
Verify built Hugo site:
- Collect all index.html paths (logical URLs)
- From each HTML extract internal hrefs, resolve relative to base, check target exists
- Check required tags: title, canonical, charset, viewport
- Report design/link/tag issues
"""
import re
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

PUBLIC = Path(__file__).resolve().parent.parent / "public"
# baseURL path (no scheme/host): /fivescup/
BASE_PATH = "/fivescup/"


def list_pages():
    """Yield (path_from_public, logical_url) for each page. logical_url = path under public as URL."""
    for path in PUBLIC.rglob("index.html"):
        rel = path.relative_to(PUBLIC)
        # logical URL: e.g. posts/foo/ from public/posts/foo/index.html
        parts = rel.parts[:-1]  # drop 'index.html'
        logical = "/".join(parts) + "/" if parts else ""
        yield path, logical


def normalize_url(href: str, base_logical: str) -> str | None:
    """Return logical path (no leading slash, with trailing /) for internal same-site links, else None."""
    if not href or href.startswith("#"):
        return None
    href = href.strip()
    if ":" in href[:10]:  # http: or https:
        return None
    if href.startswith("//"):
        return None
    # Strip base path if absolute: /fivescup/xxx -> xxx
    if href.startswith("/"):
        path = href.lstrip("/")
        if path.startswith("fivescup/"):
            path = path[len("fivescup/"):]
    else:
        # Relative: resolve from base_logical (e.g. "posts/foo/" -> parent is "posts/")
        base_dir = base_logical
        if not base_dir.endswith("/"):
            base_dir += "/"
        path = urljoin(base_dir, href)
        path = path.lstrip("/")
    path = path.rstrip("/") + "/" if path else ""
    return path


def path_to_file(logical: str) -> Path:
    """Logical URL (e.g. posts/foo/ or empty for index) to public file path."""
    logical = unquote(logical).rstrip("/")
    if not logical:
        return PUBLIC / "index.html"
    return (PUBLIC / logical.replace("/", "/")) / "index.html"


def extract_hrefs(html: str) -> list[str]:
    """Extract href values from HTML."""
    return re.findall(r'href\s*=\s*["\']([^"\']+)["\']', html, re.I)


def check_page(path: Path, logical: str, all_logicals: set[str]) -> list[str]:
    errors = []
    html = path.read_text(encoding="utf-8", errors="replace")

    # Required tags
    if "<title>" not in html and "title=" not in html:
        errors.append("missing <title>")
    if "rel=\"canonical\"" not in html and "rel=canonical" not in html:
        errors.append("missing canonical")
    if "charset=" not in html and "charset =" not in html:
        errors.append("missing charset")
    if "viewport" not in html:
        errors.append("missing viewport")

    # Internal links
    for href in extract_hrefs(html):
        norm = normalize_url(href, logical)
        if norm is None:
            continue
        # Normalize: ensure we compare same form
        if norm in ("", "posts/", "about-fivescup/", "rules/"):
            target = path_to_file(norm)
            if not target.exists():
                errors.append(f"broken link -> {href} (resolved {norm})")
        elif norm.startswith(("posts/", "about-fivescup", "rules/", "tags/", "categories/", "pages/")):
            target = path_to_file(norm)
            if not target.exists():
                errors.append(f"broken link -> {href} (resolved {norm})")

    return errors


def main():
    pages = list(list_pages())
    all_logicals = {logical for _, logical in pages}
    # Add root
    all_logicals.add("")

    broken = []
    tag_issues = []

    for path, logical in pages:
        errs = check_page(path, logical, all_logicals)
        for e in errs:
            if "broken link" in e:
                broken.append((logical or "index", e))
            else:
                tag_issues.append((logical or "index", e))

    if broken:
        print("Broken internal links:")
        for page, msg in broken:
            print("  [%s] %s" % (page, msg))
    if tag_issues:
        print("Tag / meta issues:")
        for page, msg in tag_issues:
            print("  [%s] %s" % (page, msg))
    if not broken and not tag_issues:
        print("OK: no broken links or missing tags found.")
    print(f"Checked {len(pages)} pages.")


if __name__ == "__main__":
    main()
