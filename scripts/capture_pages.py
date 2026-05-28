#!/usr/bin/env python3
"""Capture UX evidence from web pages.

Fetches page HTML and metadata, and captures screenshots when Playwright is installed.
This script is intentionally dependency-light: without Playwright it still produces
HTML snapshots and page metadata for later UX analysis.

Examples:
  python capture_pages.py https://example.com --out outputs
  python capture_pages.py https://example.com https://example.com/pricing --mobile --desktop
  python capture_pages.py --urls urls.txt --out outputs --crawl-depth 1 --max-pages 5
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List, Optional
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

USER_AGENT = "Mozilla/5.0 (compatible; UXSuite/1.0; +https://example.com/ux-suite)"

@dataclass
class PageCapture:
    url: str
    final_url: str
    slug: str
    status: Optional[int]
    title: str
    description: str
    html_path: str
    desktop_screenshot: Optional[str]
    mobile_screenshot: Optional[str]
    fetched_at: str
    errors: List[str]


def slugify_url(url: str) -> str:
    parsed = urlparse(url)
    raw = f"{parsed.netloc}{parsed.path}".strip("/") or "page"
    raw = re.sub(r"[^a-zA-Z0-9._-]+", "-", raw).strip("-").lower()
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return f"{raw[:70]}-{digest}"


def fetch_html(url: str, timeout: int = 20) -> tuple[Optional[str], str, Optional[int], list[str]]:
    errors: list[str] = []
    try:
        req = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=timeout) as res:
            status = getattr(res, "status", None)
            final_url = res.geturl()
            content_type = res.headers.get("content-type", "")
            raw = res.read()
            charset = "utf-8"
            m = re.search(r"charset=([^;]+)", content_type, re.I)
            if m:
                charset = m.group(1).strip()
            html = raw.decode(charset, errors="replace")
            return html, final_url, status, errors
    except Exception as exc:  # network/page failures should not kill a batch
        errors.append(f"fetch_failed: {type(exc).__name__}: {exc}")
        return None, url, None, errors


def extract_title_desc(html: str) -> tuple[str, str]:
    title = ""
    desc = ""
    tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    if tm:
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", tm.group(1))).strip()
    dm = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', html, re.I)
    if dm:
        desc = re.sub(r"\s+", " ", dm.group(1)).strip()
    return title, desc


def extract_links(html: str, base_url: str) -> list[str]:
    links = []
    for href in re.findall(r'<a\b[^>]*href=["\']([^"\']+)', html, re.I):
        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        abs_url = urljoin(base_url, href)
        if urlparse(abs_url).scheme in {"http", "https"}:
            links.append(abs_url.split("#")[0])
    return list(dict.fromkeys(links))


def same_site(url: str, root: str) -> bool:
    return urlparse(url).netloc == urlparse(root).netloc


def load_urls(args) -> list[str]:
    urls = list(args.urls_pos or [])
    if args.urls:
        for line in Path(args.urls).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)
    return list(dict.fromkeys(urls))


def try_playwright_capture(url: str, out_path: Path, viewport: tuple[int, int], full_page: bool = True) -> Optional[str]:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception:
        return None
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": viewport[0], "height": viewport[1]})
            page.goto(url, wait_until="networkidle", timeout=30000)
            page.screenshot(path=str(out_path), full_page=full_page)
            browser.close()
        return str(out_path)
    except Exception:
        return None


def capture_one(url: str, out_dir: Path, desktop: bool, mobile: bool) -> PageCapture:
    html_dir = out_dir / "html"
    shot_dir = out_dir / "screenshots"
    html_dir.mkdir(parents=True, exist_ok=True)
    shot_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify_url(url)
    html, final_url, status, errors = fetch_html(url)
    title = description = ""
    html_path = html_dir / f"{slug}.html"
    if html is not None:
        title, description = extract_title_desc(html)
        html_path.write_text(html, encoding="utf-8")
    else:
        html_path.write_text("", encoding="utf-8")

    desktop_path = None
    mobile_path = None
    if desktop:
        desktop_path = try_playwright_capture(final_url, shot_dir / f"{slug}-desktop.png", (1440, 1200))
        if desktop_path is None:
            errors.append("desktop_screenshot_skipped: Playwright unavailable or capture failed")
    if mobile:
        mobile_path = try_playwright_capture(final_url, shot_dir / f"{slug}-mobile.png", (390, 844))
        if mobile_path is None:
            errors.append("mobile_screenshot_skipped: Playwright unavailable or capture failed")

    return PageCapture(
        url=url,
        final_url=final_url,
        slug=slug,
        status=status,
        title=title,
        description=description,
        html_path=str(html_path),
        desktop_screenshot=desktop_path,
        mobile_screenshot=mobile_path,
        fetched_at=datetime.now(timezone.utc).isoformat(),
        errors=errors,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture page HTML, metadata, and optional screenshots for UX evidence.")
    parser.add_argument("urls_pos", nargs="*", help="URLs to capture")
    parser.add_argument("--urls", help="Text file of URLs, one per line")
    parser.add_argument("--out", default="outputs", help="Output directory")
    parser.add_argument("--desktop", action="store_true", help="Capture desktop screenshot if Playwright is installed")
    parser.add_argument("--mobile", action="store_true", help="Capture mobile screenshot if Playwright is installed")
    parser.add_argument("--crawl-depth", type=int, default=0, help="Same-domain crawl depth from provided URLs")
    parser.add_argument("--max-pages", type=int, default=10, help="Maximum total pages to capture")
    args = parser.parse_args()
    urls = load_urls(args)
    if not urls:
        parser.error("Provide at least one URL or --urls file")
    if not args.desktop and not args.mobile:
        args.desktop = True
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    queue = urls[:]
    seen: set[str] = set()
    captures: list[PageCapture] = []
    root_urls = urls[:]
    depth_by_url = {u: 0 for u in urls}

    while queue and len(captures) < args.max_pages:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        cap = capture_one(url, out_dir, args.desktop, args.mobile)
        captures.append(cap)
        if args.crawl_depth > depth_by_url.get(url, 0):
            try:
                html = Path(cap.html_path).read_text(encoding="utf-8")
                for link in extract_links(html, cap.final_url):
                    if any(same_site(link, root) for root in root_urls) and link not in seen:
                        depth_by_url[link] = depth_by_url.get(url, 0) + 1
                        queue.append(link)
            except Exception:
                pass
        time.sleep(0.2)

    metadata = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "script": "capture_pages.py",
        "captures": [asdict(c) for c in captures],
    }
    (out_dir / "page-metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print(f"Captured {len(captures)} page(s). Metadata: {out_dir / 'page-metadata.json'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
