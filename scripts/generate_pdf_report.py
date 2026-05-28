#!/usr/bin/env python3
"""Convert a UX Markdown report to PDF.

Uses ReportLab when available. Falls back to a plain text .pdf-like note if the
dependency is missing, so the workflow fails gracefully.
"""
from __future__ import annotations
import argparse, re, textwrap
from pathlib import Path


def md_to_blocks(md):
    blocks=[]
    for line in md.splitlines():
        if line.startswith("# "): blocks.append(("h1", line[2:].strip()))
        elif line.startswith("## "): blocks.append(("h2", line[3:].strip()))
        elif line.startswith("### "): blocks.append(("h3", line[4:].strip()))
        elif line.startswith("- "): blocks.append(("bullet", line[2:].strip()))
        elif re.match(r"\d+\. ", line): blocks.append(("bullet", re.sub(r"^\d+\.\s*", "", line).strip()))
        elif line.strip(): blocks.append(("p", line.strip()))
        else: blocks.append(("space", ""))
    return blocks


def clean_inline(s):
    s=re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s=re.sub(r"`([^`]*)`", r"\1", s)
    s=re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", s)
    return s


def write_with_reportlab(md, out):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
    from reportlab.lib.enums import TA_LEFT
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name="UXH1", parent=styles["Title"], spaceAfter=18, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="UXH2", parent=styles["Heading2"], spaceBefore=14, spaceAfter=8))
    styles.add(ParagraphStyle(name="UXH3", parent=styles["Heading3"], spaceBefore=10, spaceAfter=6))
    doc=SimpleDocTemplate(str(out), pagesize=letter, rightMargin=.7*inch, leftMargin=.7*inch, topMargin=.7*inch, bottomMargin=.7*inch)
    story=[]; bullets=[]
    def flush_bullets():
        nonlocal bullets
        if bullets:
            story.append(ListFlowable([ListItem(Paragraph(clean_inline(b), styles["BodyText"])) for b in bullets], bulletType='bullet'))
            story.append(Spacer(1,6)); bullets=[]
    for kind,text in md_to_blocks(md):
        if kind != "bullet": flush_bullets()
        if kind=="h1": story += [Paragraph(clean_inline(text), styles["UXH1"]), Spacer(1,8)]
        elif kind=="h2": story.append(Paragraph(clean_inline(text), styles["UXH2"]))
        elif kind=="h3": story.append(Paragraph(clean_inline(text), styles["UXH3"]))
        elif kind=="bullet": bullets.append(text)
        elif kind=="p": story.append(Paragraph(clean_inline(text), styles["BodyText"]))
        elif kind=="space": story.append(Spacer(1,6))
    flush_bullets(); doc.build(story)


def main():
    ap=argparse.ArgumentParser(description="Generate PDF from UX-REPORT.md")
    ap.add_argument("input", nargs="?", default="outputs/UX-REPORT.md")
    ap.add_argument("--out", default="outputs/UX-REPORT.pdf")
    args=ap.parse_args(); inp=Path(args.input); out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True)
    md=inp.read_text(encoding='utf-8',errors='replace')
    try:
        write_with_reportlab(md, out)
        print(f"Wrote {out}")
    except Exception as e:
        fallback=out.with_suffix('.txt')
        fallback.write_text("PDF generation requires reportlab. Install with `pip install reportlab`.\n\n"+md, encoding='utf-8')
        print(f"PDF generation failed ({type(e).__name__}: {e}). Wrote fallback text report: {fallback}")
if __name__=="__main__": main()
