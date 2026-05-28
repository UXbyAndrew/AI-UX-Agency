#!/usr/bin/env python3
"""Normalize and prioritize UX findings.

Accepts findings from JSON or CSV. Expected fields are flexible, but the best
input includes: title, severity, user_impact, business_impact, frequency,
confidence, effort, recommendation.
"""
from __future__ import annotations
import argparse, csv, json, re
from datetime import datetime, timezone
from pathlib import Path

SCALE={"none":0,"low":1,"minor":1,"medium":2,"moderate":2,"high":3,"major":3,"critical":4,"blocker":4}
EFFORT={"xs":1,"s":1,"small":1,"low":1,"m":2,"medium":2,"l":3,"large":3,"xl":4,"high":4}

def val(x, default=2):
    if x is None or x=="": return default
    if isinstance(x,(int,float)): return float(x)
    s=str(x).strip().lower()
    if s in SCALE: return SCALE[s]
    if s in EFFORT: return EFFORT[s]
    try: return float(s)
    except Exception: return default


def load(path):
    p=Path(path)
    if p.suffix.lower()==".csv":
        with p.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
    data=json.loads(p.read_text(encoding='utf-8'))
    if isinstance(data,list): return data
    for key in ["findings","issues","items","pages"]:
        if isinstance(data.get(key),list):
            if key=="pages":
                out=[]
                for page in data[key]:
                    for i in page.get("issues",[]) or page.get("ux_risk_flags",[]):
                        item=dict(i); item.setdefault("source",page.get("source")); out.append(item)
                return out
            return data[key]
    return []


def score_item(item):
    sev=val(item.get("severity") or item.get("risk") or item.get("impact"),2)
    user=val(item.get("user_impact"),sev)
    biz=val(item.get("business_impact"),2)
    freq=val(item.get("frequency"),2)
    conf=val(item.get("confidence"),2)
    effort=val(item.get("effort"),2)
    # balanced additive score; avoids false precision while supporting sorting
    priority=(sev*1.5 + user*1.25 + biz + freq + conf) - (effort*0.75)
    item=dict(item)
    item["normalized"]={"severity":sev,"user_impact":user,"business_impact":biz,"frequency":freq,"confidence":conf,"effort":effort,"priority_score":round(priority,2)}
    if priority>=10: item["priority_band"]="P0 / P1"
    elif priority>=7: item["priority_band"]="P2"
    elif priority>=4: item["priority_band"]="P3"
    else: item["priority_band"]="Backlog"
    return item


def title(item): return item.get("title") or item.get("rule") or item.get("risk") or item.get("finding") or item.get("issue") or "Untitled finding"

def md(items):
    lines=["# Prioritized UX Findings", "", "| Priority | Score | Finding | Recommendation |", "|---|---:|---|---|"]
    for it in items:
        rec=it.get("recommendation") or it.get("fix") or "Define recommendation during expert review."
        lines.append(f"| {it['priority_band']} | {it['normalized']['priority_score']} | {title(it)} | {str(rec).replace('|','/')} |")
    lines += ["", "## Scoring Model", "", "Priority Score = severity×1.5 + user impact×1.25 + business impact + frequency + confidence − effort×0.75", "", "Scores support prioritization; they do not replace design judgment."]
    return "\n".join(lines)


def write_csv(items, path):
    fields=["priority_band","priority_score","title","severity","user_impact","business_impact","frequency","confidence","effort","recommendation","source"]
    with Path(path).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for it in items:
            n=it["normalized"]
            w.writerow({"priority_band":it["priority_band"],"priority_score":n["priority_score"],"title":title(it),"severity":n["severity"],"user_impact":n["user_impact"],"business_impact":n["business_impact"],"frequency":n["frequency"],"confidence":n["confidence"],"effort":n["effort"],"recommendation":it.get("recommendation") or it.get("fix") or "", "source":it.get("source","")})

def main():
    ap=argparse.ArgumentParser(description="Score and prioritize UX findings from JSON/CSV.")
    ap.add_argument("input", help="Findings JSON/CSV, accessibility-scan.json, or page-analysis.json")
    ap.add_argument("--out", default="outputs")
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    items=[score_item(i) for i in load(args.input)]
    items.sort(key=lambda x:x["normalized"]["priority_score"], reverse=True)
    (out/"prioritized-findings.json").write_text(json.dumps({"generated_at":datetime.now(timezone.utc).isoformat(),"findings":items},indent=2),encoding='utf-8')
    (out/"prioritized-findings.md").write_text(md(items),encoding='utf-8')
    write_csv(items,out/"prioritized-findings.csv")
    print(f"Scored {len(items)} finding(s). Wrote prioritized findings to {out}")
if __name__=="__main__": main()
