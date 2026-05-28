#!/usr/bin/env python3
"""Compile UX suite outputs into a Markdown report.

Looks for standard output files created by the core scripts and combines them into
an executive-friendly report skeleton with appendices.
"""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

ORDER=[
    ("prioritized-findings.md","Prioritized Findings"),
    ("page-analysis.md","Page Analysis"),
    ("flow-map.md","Flow Map"),
    ("accessibility-summary.md","Accessibility Pre-Scan"),
    ("content-inventory.md","Content Inventory"),
]

def read_if(path):
    return path.read_text(encoding='utf-8',errors='replace') if path.exists() else ""

def strip_h1(md): return re.sub(r"^# .+\n+", "", md.strip(), count=1)

def load_priority_summary(outdir):
    p=outdir/"prioritized-findings.json"
    if not p.exists(): return []
    try: return json.loads(p.read_text(encoding='utf-8')).get("findings",[])[:10]
    except Exception: return []

def main():
    ap=argparse.ArgumentParser(description="Generate Markdown UX report from script outputs.")
    ap.add_argument("--input-dir", default="outputs")
    ap.add_argument("--out", default="outputs/UX-REPORT.md")
    ap.add_argument("--title", default="UX Review Report")
    ap.add_argument("--client", default="")
    ap.add_argument("--scope", default="")
    args=ap.parse_args(); indir=Path(args.input_dir); out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    top=load_priority_summary(indir)
    lines=[f"# {args.title}", "", f"Generated: {datetime.now(timezone.utc).isoformat()}"]
    if args.client: lines.append(f"Client/Product: {args.client}")
    if args.scope: lines.append(f"Scope: {args.scope}")
    lines += ["", "## Executive Summary", "", "This report consolidates automated UX evidence into a review-ready structure. Findings should be validated by the relevant UX skill and agent review before being treated as final recommendations.", ""]
    if top:
        lines += ["### Highest-Priority Findings", ""]
        for i,it in enumerate(top[:5], start=1):
            title=it.get("title") or it.get("rule") or it.get("risk") or "Untitled finding"
            band=it.get("priority_band","")
            score=it.get("normalized",{}).get("priority_score","")
            lines.append(f"{i}. **{title}** — {band} / score {score}")
        lines.append("")
    else:
        lines += ["### Highest-Priority Findings", "", "Prioritized findings were not found. Run `score_ux_findings.py` or add expert findings before finalizing.", ""]
    lines += ["## Recommended 30/60/90 Roadmap", "", "### 30 Days — Fix obvious friction", "- Address high-confidence usability, accessibility, and content clarity issues.", "", "### 60 Days — Improve core flows", "- Redesign or test the highest-impact task flows and decision points.", "", "### 90 Days — Validate and scale", "- Instrument key events, validate recommendations, and integrate patterns into the design system.", ""]
    lines += ["## Evidence Appendices", ""]
    for fname, heading in ORDER:
        content=read_if(indir/fname)
        if content:
            lines += [f"## {heading}", "", strip_h1(content), ""]
    lines += ["## Review Notes", "", "- Separate evidence from assumptions before sharing externally.", "- Confirm severity with real user/business context where possible.", "- Use relevant UX agents to reconcile conflicts and produce final recommendations.", ""]
    out.write_text("\n".join(lines),encoding='utf-8')
    print(f"Wrote {out}")
if __name__=="__main__": main()
