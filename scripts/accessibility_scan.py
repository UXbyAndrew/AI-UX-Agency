#!/usr/bin/env python3
"""Practical accessibility pre-scan for UX reviews.

This is not a full WCAG audit. It detects common structural issues in HTML and
creates evidence for manual expert review.
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


def read_source(src):
    if src.startswith(("http://","https://")):
        req=Request(src,headers={"User-Agent":USER_AGENT})
        with urlopen(req,timeout=20) as r: return r.read().decode("utf-8",errors="replace"), r.geturl()
    return Path(src).read_text(encoding="utf-8",errors="replace"), str(src)


def text_clean(s): return re.sub(r"\s+"," ",unescape(re.sub(r"<[^>]+>"," ",s))).strip()

def attr(tag, name):
    m=re.search(rf"\b{name}\s*=\s*['\"]([^'\"]*)", tag, re.I)
    return unescape(m.group(1)).strip() if m else ""


def scan_bs4(html, source):
    soup=BeautifulSoup(html,"html.parser")
    headings=[int(h.name[1]) for h in soup.find_all(re.compile("^h[1-6]$"))]
    issues=[]
    def issue(rule, severity, evidence, recommendation): issues.append({"rule":rule,"severity":severity,"evidence":evidence,"recommendation":recommendation})
    if not soup.find("h1"): issue("Missing H1","medium",source,"Add a clear page-level H1.")
    if len(soup.find_all("h1"))>1: issue("Multiple H1s","low",f"{len(soup.find_all('h1'))} H1 elements","Use one primary H1 unless the page structure intentionally supports multiple landmarks.")
    for a,b in zip(headings, headings[1:]):
        if b-a>1: issue("Skipped heading level","medium",f"h{a} followed by h{b}","Use hierarchical heading order to support screen reader navigation.")
    imgs=soup.find_all("img")
    missing=[img.get("src","") for img in imgs if img.get("alt") is None]
    if missing: issue("Image missing alt attribute","high",f"{len(missing)} image(s)","Add meaningful alt text or empty alt for decorative images.")
    fields=soup.find_all(["input","textarea","select"])
    labels={l.get("for") for l in soup.find_all("label") if l.get("for")}
    unlabeled=[]
    for f in fields:
        typ=(f.get("type") or "").lower()
        if typ in {"hidden","submit","button"}: continue
        if not (f.get("aria-label") or f.get("aria-labelledby") or (f.get("id") and f.get("id") in labels)):
            unlabeled.append(f.get("name") or f.get("id") or typ or "field")
    if unlabeled: issue("Form control may be unlabeled","high",f"{len(unlabeled)} field(s): {', '.join(unlabeled[:8])}","Connect visible labels to controls or add appropriate accessible names.")
    buttons=soup.find_all("button")
    empty_buttons=[str(b)[:80] for b in buttons if not (b.get_text(strip=True) or b.get("aria-label") or b.get("aria-labelledby"))]
    if empty_buttons: issue("Button missing accessible name","high",f"{len(empty_buttons)} button(s)","Ensure every button has clear visible text or an accessible name.")
    links=soup.find_all("a")
    vague=[]
    for a in links:
        t=a.get_text(" ",strip=True).lower()
        if not t and not (a.get("aria-label") or a.get("aria-labelledby")): vague.append("empty link")
        elif t in {"click here","read more","learn more","more"}: vague.append(t)
    if vague: issue("Link text may be vague","medium",f"{len(vague)} link(s)","Use link text that describes the destination or action.")
    if not soup.find(["main", {"role":"main"}]): issue("No main landmark detected","medium",source,"Add a main landmark to support assistive technology navigation.")
    return {"source":source,"counts":{"headings":len(headings),"images":len(imgs),"fields":len(fields),"buttons":len(buttons),"links":len(links)},"issues":issues}


def scan_regex(html, source):
    issues=[]
    headings=[int(m.group(1)) for m in re.finditer(r"<h([1-6])\b", html, re.I)]
    if not re.search(r"<h1\b", html, re.I): issues.append({"rule":"Missing H1","severity":"medium","evidence":source,"recommendation":"Add a clear page-level H1."})
    for a,b in zip(headings, headings[1:]):
        if b-a>1: issues.append({"rule":"Skipped heading level","severity":"medium","evidence":f"h{a} followed by h{b}","recommendation":"Use hierarchical heading order."})
    imgs=re.findall(r"<img\b[^>]*>", html, re.I)
    miss=[i for i in imgs if not re.search(r"\balt\s*=", i, re.I)]
    if miss: issues.append({"rule":"Image missing alt attribute","severity":"high","evidence":f"{len(miss)} image(s)","recommendation":"Add meaningful or decorative alt text."})
    fields=re.findall(r"<(input|textarea|select)\b[^>]*>", html, re.I)
    return {"source":source,"counts":{"headings":len(headings),"images":len(imgs),"fields":len(fields)},"issues":issues}


def scan(html, source): return scan_bs4(html, source) if BeautifulSoup else scan_regex(html, source)

def md(results):
    lines=["# Accessibility Pre-Scan", "", "> This automated pre-scan supports, but does not replace, manual accessibility review.", ""]
    for r in results:
        lines += [f"## {r['source']}", "", "### Issues", ""]
        if r["issues"]:
            for i in r["issues"]: lines.append(f"- **{i['severity'].upper()} — {i['rule']}**: {i['evidence']} → {i['recommendation']}")
        else: lines.append("- No common structural issues detected by script. Manual review still required.")
        lines.append("")
    return "\n".join(lines)


def main():
    ap=argparse.ArgumentParser(description="Run a practical HTML accessibility pre-scan.")
    ap.add_argument("sources", nargs="+", help="URLs or HTML files")
    ap.add_argument("--out", default="outputs")
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    results=[]
    for s in args.sources:
        try: html, actual=read_source(s); results.append(scan(html, actual))
        except Exception as e: results.append({"source":s,"error":f"{type(e).__name__}: {e}","issues":[]})
    data={"generated_at":datetime.now(timezone.utc).isoformat(),"note":"Automated pre-scan, not a full WCAG audit.","pages":results}
    (out/"accessibility-scan.json").write_text(json.dumps(data,indent=2),encoding="utf-8")
    (out/"accessibility-summary.md").write_text(md([r for r in results if "error" not in r]),encoding="utf-8")
    print(f"Wrote {out/'accessibility-scan.json'} and {out/'accessibility-summary.md'}")
if __name__=="__main__": main()
