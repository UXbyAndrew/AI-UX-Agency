#!/usr/bin/env python3
"""Extract UX-relevant structure and signals from HTML pages.

Inputs may be URLs, HTML files, or a capture_pages.py page-metadata.json file.
Outputs JSON plus a readable Markdown summary.
"""
from __future__ import annotations

import argparse, json, re, sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Optional
from urllib.request import Request, urlopen

USER_AGENT = "Mozilla/5.0 (compatible; UXSuite/1.0)"

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:
    BeautifulSoup = None

CTA_WORDS = re.compile(r"\b(get started|start|try|buy|purchase|checkout|sign up|signup|subscribe|book|demo|contact|learn more|download|request|join|continue|next|create|save)\b", re.I)
TRUST_WORDS = re.compile(r"\b(review|rating|testimonial|case study|customer|trusted|secure|privacy|guarantee|refund|certified|award|logo|clients?)\b", re.I)
FRICTION_WORDS = re.compile(r"\b(required|password|captcha|create account|credit card|error|invalid|terms|permission|verify|loading)\b", re.I)


def read_source(source: str) -> tuple[str, str]:
    if source.startswith(("http://", "https://")):
        req = Request(source, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=20) as res:
            return res.read().decode("utf-8", errors="replace"), res.geturl()
    p = Path(source)
    return p.read_text(encoding="utf-8", errors="replace"), str(p)


def text_clean(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def attr(tag: str, name: str) -> str:
    m = re.search(rf"\b{name}\s*=\s*['\"]([^'\"]*)", tag, re.I)
    return unescape(m.group(1)).strip() if m else ""


def parse_with_bs4(html: str):
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    headings = [{"level": int(h.name[1]), "text": h.get_text(" ", strip=True)} for h in soup.find_all(re.compile("^h[1-6]$"))]
    links = [{"text": a.get_text(" ", strip=True), "href": a.get("href", "")} for a in soup.find_all("a")]
    buttons = [{"text": b.get_text(" ", strip=True), "type": b.get("type", "")} for b in soup.find_all("button")]
    inputs = [{"type": i.get("type", "text"), "name": i.get("name", ""), "placeholder": i.get("placeholder", ""), "id": i.get("id", "")} for i in soup.find_all(["input", "textarea", "select"])]
    forms = [{"action": f.get("action", ""), "method": f.get("method", "get"), "field_count": len(f.find_all(["input", "textarea", "select"]))} for f in soup.find_all("form")]
    images = [{"src": img.get("src", ""), "alt": img.get("alt", "")} for img in soup.find_all("img")]
    navs = [n.get_text(" ", strip=True)[:500] for n in soup.find_all(["nav", "header", "footer"])]
    main_text = soup.get_text(" ", strip=True)
    return title, headings, links, buttons, inputs, forms, images, navs, main_text


def parse_with_regex(html: str):
    title = text_clean(re.search(r"<title[^>]*>(.*?)</title>", html, re.I|re.S).group(1)) if re.search(r"<title[^>]*>(.*?)</title>", html, re.I|re.S) else ""
    headings=[]
    for m in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", html, re.I|re.S):
        headings.append({"level": int(m.group(1)), "text": text_clean(m.group(2))})
    links=[{"text": text_clean(m.group(2)), "href": attr(m.group(1), "href")} for m in re.finditer(r"(<a\b[^>]*>)(.*?)</a>", html, re.I|re.S)]
    buttons=[{"text": text_clean(m.group(2)), "type": attr(m.group(1), "type")} for m in re.finditer(r"(<button\b[^>]*>)(.*?)</button>", html, re.I|re.S)]
    inputs=[{"type": attr(m.group(0), "type") or "text", "name": attr(m.group(0), "name"), "placeholder": attr(m.group(0), "placeholder"), "id": attr(m.group(0), "id")} for m in re.finditer(r"<(input|textarea|select)\b[^>]*>", html, re.I)]
    forms=[{"action": attr(m.group(1), "action"), "method": attr(m.group(1), "method") or "get", "field_count": len(re.findall(r"<(input|textarea|select)\b", m.group(2), re.I))} for m in re.finditer(r"(<form\b[^>]*>)(.*?)</form>", html, re.I|re.S)]
    images=[{"src": attr(m.group(0), "src"), "alt": attr(m.group(0), "alt")} for m in re.finditer(r"<img\b[^>]*>", html, re.I)]
    navs=[text_clean(m.group(0))[:500] for m in re.finditer(r"<(nav|header|footer)\b[^>]*>.*?</\1>", html, re.I|re.S)]
    main_text=text_clean(html)
    return title, headings, links, buttons, inputs, forms, images, navs, main_text


def analyze(html: str, source: str) -> dict:
    if BeautifulSoup:
        title, headings, links, buttons, inputs, forms, images, navs, main_text = parse_with_bs4(html)
    else:
        title, headings, links, buttons, inputs, forms, images, navs, main_text = parse_with_regex(html)
    cta_candidates=[]
    for item in links + buttons:
        t=item.get("text","")
        if t and CTA_WORDS.search(t):
            cta_candidates.append(item)
    label_gaps = [i for i in inputs if not (i.get("name") or i.get("placeholder") or i.get("id"))]
    missing_alt = [img for img in images if not img.get("alt")]
    heading_levels=[h["level"] for h in headings]
    skipped=[]
    for a,b in zip(heading_levels, heading_levels[1:]):
        if b-a>1: skipped.append({"from": a, "to": b})
    trust_hits = sorted(set(m.group(0).lower() for m in TRUST_WORDS.finditer(main_text)))
    friction_hits = sorted(set(m.group(0).lower() for m in FRICTION_WORDS.finditer(main_text)))
    return {
        "source": source,
        "title": title,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "counts": {"headings": len(headings), "links": len(links), "buttons": len(buttons), "forms": len(forms), "fields": len(inputs), "images": len(images), "ctas": len(cta_candidates)},
        "headings": headings[:80],
        "primary_ctas": cta_candidates[:40],
        "forms": forms,
        "fields": inputs[:80],
        "navigation_samples": navs[:5],
        "image_alt_gaps_count": len(missing_alt),
        "form_label_gap_count": len(label_gaps),
        "heading_order_issues": skipped,
        "trust_signal_terms": trust_hits[:25],
        "friction_terms": friction_hits[:25],
        "ux_risk_flags": risk_flags(headings, cta_candidates, forms, inputs, missing_alt, skipped, trust_hits, friction_hits),
    }


def risk_flags(headings, ctas, forms, inputs, missing_alt, skipped, trust_hits, friction_hits):
    flags=[]
    h1=[h for h in headings if h.get("level")==1]
    if not h1: flags.append({"risk":"No H1 detected", "why":"The page may lack a clear primary message or accessible structure."})
    if len(h1)>1: flags.append({"risk":"Multiple H1s detected", "why":"Competing primary headings may weaken page hierarchy."})
    if not ctas: flags.append({"risk":"No obvious CTA detected", "why":"Users may not know the intended next action."})
    if forms and len(inputs)>8: flags.append({"risk":"High form burden", "why":"Long forms can increase abandonment and cognitive load."})
    if missing_alt: flags.append({"risk":"Images missing alt text", "why":"Non-text content may be unavailable to assistive technology."})
    if skipped: flags.append({"risk":"Skipped heading levels", "why":"Heading order may create navigation confusion for screen reader users."})
    if friction_hits: flags.append({"risk":"Friction language detected", "why":"Terms may indicate barriers such as verification, required fields, or errors."})
    if not trust_hits: flags.append({"risk":"Few explicit trust signals detected", "why":"Users may lack reassurance before committing."})
    return flags


def sources_from_arg(inputs):
    result=[]
    for x in inputs:
        if x.endswith(".json") and Path(x).exists():
            data=json.loads(Path(x).read_text(encoding="utf-8"))
            for c in data.get("captures",[]):
                hp=c.get("html_path")
                if hp: result.append(hp)
        else:
            result.append(x)
    return result


def md_summary(results):
    lines=["# UX Page Analysis", ""]
    for r in results:
        lines += [f"## {r.get('title') or r['source']}", "", f"Source: `{r['source']}`", "", "### Counts", ""]
        for k,v in r["counts"].items(): lines.append(f"- {k}: {v}")
        lines += ["", "### UX Risk Flags", ""]
        if r["ux_risk_flags"]:
            for f in r["ux_risk_flags"]: lines.append(f"- **{f['risk']}** — {f['why']}")
        else: lines.append("- No major structural flags detected by script. Requires expert review.")
        lines += ["", "### Primary CTA Candidates", ""]
        for c in r["primary_ctas"][:10]: lines.append(f"- {c.get('text') or '[no text]'}")
        lines.append("")
    return "\n".join(lines)


def main():
    ap=argparse.ArgumentParser(description="Analyze page HTML for UX structure and risk signals.")
    ap.add_argument("sources", nargs="+", help="URLs, HTML files, or page-metadata.json")
    ap.add_argument("--out", default="outputs", help="Output directory")
    args=ap.parse_args()
    out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    results=[]
    for src in sources_from_arg(args.sources):
        try:
            html, actual=read_source(src)
            results.append(analyze(html, actual))
        except Exception as e:
            results.append({"source": src, "error": f"{type(e).__name__}: {e}"})
    (out/"page-analysis.json").write_text(json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "pages": results}, indent=2), encoding="utf-8")
    good=[r for r in results if "error" not in r]
    (out/"page-analysis.md").write_text(md_summary(good), encoding="utf-8")
    print(f"Analyzed {len(results)} source(s). Wrote {out/'page-analysis.json'} and {out/'page-analysis.md'}")

if __name__ == "__main__": main()
