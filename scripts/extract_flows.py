#!/usr/bin/env python3
"""Create a UX task-flow map from page analysis, URLs, or manual steps.

Best used after analyze_page_ux.py, but can also accept a simple steps file.
Outputs JSON and Markdown/Mermaid for reports.
"""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

CTA_RE=re.compile(r"\b(start|sign up|signup|demo|checkout|buy|continue|next|submit|create|save|book|contact|request|get started|learn more)\b", re.I)
FRICTION_RE=re.compile(r"\b(required|password|captcha|credit card|verify|permission|error|invalid|terms|login|account)\b", re.I)


def load_steps(path: str|None):
    if not path: return []
    lines=Path(path).read_text(encoding="utf-8").splitlines()
    steps=[]
    for line in lines:
        line=line.strip(" -\t")
        if line: steps.append({"label": line, "source": "manual"})
    return steps


def from_page_analysis(path: str):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    steps=[]
    for idx,p in enumerate(data.get("pages",[]), start=1):
        if "error" in p: continue
        label=p.get("title") or p.get("source") or f"Page {idx}"
        ctas=[c.get("text","") for c in p.get("primary_ctas",[]) if c.get("text")]
        risks=[r.get("risk","") for r in p.get("ux_risk_flags",[])]
        steps.append({"label": label, "source": p.get("source"), "ctas": ctas[:8], "risks": risks[:8], "field_count": p.get("counts",{}).get("fields",0), "form_count": p.get("counts",{}).get("forms",0)})
    return steps


def infer_friction(step):
    text=" ".join([step.get("label","")] + step.get("ctas",[]) + step.get("risks",[]))
    flags=[]
    if step.get("field_count",0)>8: flags.append("High field count")
    if step.get("form_count",0)>1: flags.append("Multiple forms on step")
    if FRICTION_RE.search(text): flags.append("Potential barrier language or gated action")
    if not step.get("ctas") and step.get("source") != "manual": flags.append("No obvious next action")
    return flags


def build_flow(task, steps):
    nodes=[]
    edges=[]
    for i,s in enumerate(steps, start=1):
        node={"id": f"S{i}", "label": s.get("label") or f"Step {i}", "source": s.get("source"), "ctas": s.get("ctas",[]), "risks": s.get("risks",[]), "friction_flags": infer_friction(s)}
        nodes.append(node)
        if i>1: edges.append({"from": f"S{i-1}", "to": f"S{i}", "type": "next"})
    return {"task": task, "generated_at": datetime.now(timezone.utc).isoformat(), "nodes": nodes, "edges": edges, "summary": summarize(nodes)}


def summarize(nodes):
    friction=[n for n in nodes if n["friction_flags"]]
    return {"step_count": len(nodes), "friction_step_count": len(friction), "highest_risk_steps": [{"id": n["id"], "label": n["label"], "flags": n["friction_flags"]} for n in friction[:5]]}


def mermaid(flow):
    lines=["```mermaid", "flowchart TD"]
    for n in flow["nodes"]:
        label=n["label"].replace('"','').replace('[','(').replace(']',')')[:60]
        lines.append(f"  {n['id']}[\"{label}\"]")
    for e in flow["edges"]:
        lines.append(f"  {e['from']} --> {e['to']}")
    lines.append("```")
    return "\n".join(lines)


def md(flow):
    lines=[f"# UX Flow Map: {flow['task']}", "", mermaid(flow), "", "## Step Review", ""]
    for n in flow["nodes"]:
        lines += [f"### {n['id']}: {n['label']}", ""]
        if n.get("source"): lines.append(f"Source: `{n['source']}`")
        if n["ctas"]: lines += ["", "Likely actions:"] + [f"- {c}" for c in n["ctas"][:6]]
        if n["friction_flags"]: lines += ["", "Friction flags:"] + [f"- {f}" for f in n["friction_flags"]]
        lines.append("")
    lines += ["## Summary", "", f"- Steps: {flow['summary']['step_count']}", f"- Steps with friction flags: {flow['summary']['friction_step_count']}"]
    return "\n".join(lines)


def main():
    ap=argparse.ArgumentParser(description="Generate UX task-flow map from analysis or manual steps.")
    ap.add_argument("--task", required=True, help="User task, e.g. 'book a demo' or 'checkout'")
    ap.add_argument("--analysis", help="page-analysis.json from analyze_page_ux.py")
    ap.add_argument("--steps", help="Text file with one manual step per line")
    ap.add_argument("--out", default="outputs", help="Output directory")
    args=ap.parse_args()
    steps=[]
    if args.analysis: steps += from_page_analysis(args.analysis)
    steps += load_steps(args.steps)
    if not steps: ap.error("Provide --analysis or --steps")
    out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    flow=build_flow(args.task, steps)
    (out/"flow-structure.json").write_text(json.dumps(flow, indent=2), encoding="utf-8")
    (out/"flow-map.md").write_text(md(flow), encoding="utf-8")
    print(f"Wrote {out/'flow-structure.json'} and {out/'flow-map.md'}")

if __name__ == "__main__": main()
