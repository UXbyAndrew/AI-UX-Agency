#!/usr/bin/env python3
"""Create a UX content inventory from HTML pages.

Extracts headings, navigation, CTA copy, form labels/placeholders, error-like copy,
trust/reassurance copy, pricing phrases, and empty-state candidates.
"""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from urllib.request import Request, urlopen

USER_AGENT="Mozilla/5.0 (compatible; UXSuite/1.0)"
try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:
    BeautifulSoup=None

CTA_RE=re.compile(r"\b(get started|start|try|buy|checkout|sign up|subscribe|book|demo|contact|download|request|join|continue|create|save|learn more)\b", re.I)
ERROR_RE=re.compile(r"\b(error|invalid|required|try again|failed|cannot|can't|must|missing|expired)\b", re.I)
TRUST_RE=re.compile(r"\b(secure|privacy|guarantee|refund|return|trusted|review|testimonial|case study|customer|certified|support|free shipping|warranty)\b", re.I)
PRICE_RE=re.compile(r"(?:[$€£]\s?\d+[\d,.]*|\bfree\b|\btrial\b|\bper month\b|\bmonthly\b|\bannual\b|\bpricing\b)", re.I)
EMPTY_RE=re.compile(r"\b(no results|nothing here|empty|start by|create your first|no items|no data)\b", re.I)


def read_source(src):
    if src.startswith(("http://","https://")):
        req=Request(src,headers={"User-Agent":USER_AGENT})
        with urlopen(req,timeout=20) as r: return r.read().decode("utf-8",errors="replace"), r.geturl()
    return Path(src).read_text(encoding="utf-8",errors="replace"), str(src)

def clean(s): return re.sub(r"\s+"," ",unescape(s or "")).strip()

def visible_texts_bs4(html):
    soup=BeautifulSoup(html,"html.parser")
    for bad in soup(["script","style","noscript"]): bad.decompose()
    blocks=[]
    for tag in soup.find_all(["h1","h2","h3","h4","h5","h6","a","button","label","option","p","li","small","span"]):
        t=tag.get_text(" ",strip=True)
        if t and len(t)<400: blocks.append({"tag":tag.name,"text":clean(t),"href":tag.get("href","") if tag.name=="a" else ""})
    fields=[]
    for f in soup.find_all(["input","textarea","select"]): fields.append({"type":f.get("type","text"),"name":f.get("name",""),"placeholder":f.get("placeholder","")})
    return blocks, fields

def visible_texts_regex(html):
    blocks=[]
    for m in re.finditer(r"<(h[1-6]|a|button|label|option|p|li|small|span)\b[^>]*>(.*?)</\1>", html, re.I|re.S):
        text=clean(re.sub(r"<[^>]+>"," ",m.group(2)))
        if text and len(text)<400: blocks.append({"tag":m.group(1).lower(),"text":text,"href":""})
    fields=[]
    for m in re.finditer(r"<(input|textarea|select)\b[^>]*>", html, re.I):
        tag=m.group(0)
        def attr(n):
            mm=re.search(rf"\b{n}\s*=\s*['\"]([^'\"]*)", tag, re.I)
            return clean(mm.group(1)) if mm else ""
        fields.append({"type":attr("type") or "text","name":attr("name"),"placeholder":attr("placeholder")})
    return blocks, fields

def inventory(html, source):
    blocks, fields = visible_texts_bs4(html) if BeautifulSoup else visible_texts_regex(html)
    def pick(rx): return [b for b in blocks if rx.search(b["text"])]
    headings=[b for b in blocks if re.fullmatch(r"h[1-6]", b["tag"])]
    nav=[b for b in blocks if b["tag"]=="a"][:80]
    ctas=[b for b in blocks if b["tag"] in {"a","button"} and CTA_RE.search(b["text"])]
    return {"source":source,"counts":{"text_blocks":len(blocks),"headings":len(headings),"links_sampled":len(nav),"ctas":len(ctas),"fields":len(fields)},"headings":headings[:80],"navigation_labels":nav,"cta_copy":ctas[:80],"form_fields":fields,"error_or_validation_copy":pick(ERROR_RE)[:80],"trust_reassurance_copy":pick(TRUST_RE)[:80],"pricing_copy":pick(PRICE_RE)[:80],"empty_state_candidates":pick(EMPTY_RE)[:80]}

def md(results):
    lines=["# UX Content Inventory", ""]
    for r in results:
        lines += [f"## {r['source']}", "", "### Headings", ""] + [f"- `{h['tag']}` {h['text']}" for h in r["headings"][:30]]
        lines += ["", "### CTA Copy", ""] + ([f"- {c['text']}" for c in r["cta_copy"][:30]] or ["- No CTA copy detected by script."])
        lines += ["", "### Form Fields", ""] + ([f"- {f.get('type','text')} — name: `{f.get('name','')}` placeholder: `{f.get('placeholder','')}`" for f in r["form_fields"][:30]] or ["- No form fields detected."])
        lines += ["", "### Trust / Reassurance Copy", ""] + ([f"- {t['text']}" for t in r["trust_reassurance_copy"][:20]] or ["- No trust/reassurance copy detected by script."])
        lines.append("")
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser(description="Create UX content inventory from URLs or HTML files.")
    ap.add_argument("sources", nargs="+")
    ap.add_argument("--out", default="outputs")
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    results=[]
    for s in args.sources:
        try: html, actual=read_source(s); results.append(inventory(html, actual))
        except Exception as e: results.append({"source":s,"error":f"{type(e).__name__}: {e}"})
    good=[r for r in results if "error" not in r]
    (out/"content-inventory.json").write_text(json.dumps({"generated_at":datetime.now(timezone.utc).isoformat(),"pages":results},indent=2),encoding="utf-8")
    (out/"content-inventory.md").write_text(md(good),encoding="utf-8")
    print(f"Wrote {out/'content-inventory.json'} and {out/'content-inventory.md'}")
if __name__=="__main__": main()
