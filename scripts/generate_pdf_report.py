#!/usr/bin/env python3
"""Generate a polished, client-ready UX PDF report from Markdown.

This script is designed for the AI UX Agency / Claude Code UX suite.
It reads a Markdown UX report and produces a branded PDF with:
- designed cover page
- score gauge
- score breakdown bars
- styled tables
- section hierarchy
- professional typography and spacing
- consistent header/footer treatment

Usage:
  python scripts/generate_pdf_report.py UX-REPORT.md
  python scripts/generate_pdf_report.py UX-REPORT.md --output UX-REPORT.pdf
  python scripts/generate_pdf_report.py UX-REPORT.md --brand-name "AI UX Agency"

Dependencies:
  pip install reportlab

If ReportLab is unavailable, the script writes a clear fallback text file beside
where the PDF would have been created, rather than failing silently.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

try:
    from reportlab.lib import colors
    from reportlab.lib.colors import HexColor
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.pdfbase.pdfmetrics import stringWidth
    from reportlab.platypus import (
        BaseDocTemplate,
        Flowable,
        Frame,
        KeepTogether,
        ListFlowable,
        ListItem,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )
    REPORTLAB_AVAILABLE = True
except Exception:  # pragma: no cover - used only in missing dependency environments
    REPORTLAB_AVAILABLE = False


# -----------------------------------------------------------------------------
# Brand system
# -----------------------------------------------------------------------------

NAVY = HexColor("#14213D") if REPORTLAB_AVAILABLE else None
BLUE = HexColor("#2563EB") if REPORTLAB_AVAILABLE else None
TEAL = HexColor("#0E7490") if REPORTLAB_AVAILABLE else None
GREEN = HexColor("#16A34A") if REPORTLAB_AVAILABLE else None
AMBER = HexColor("#D97706") if REPORTLAB_AVAILABLE else None
RED = HexColor("#DC2626") if REPORTLAB_AVAILABLE else None
INK = HexColor("#111827") if REPORTLAB_AVAILABLE else None
MUTED = HexColor("#4B5563") if REPORTLAB_AVAILABLE else None
LIGHT = HexColor("#F3F4F6") if REPORTLAB_AVAILABLE else None
LINE = HexColor("#D1D5DB") if REPORTLAB_AVAILABLE else None
WHITE = colors.white if REPORTLAB_AVAILABLE else None


@dataclass
class ReportMeta:
    title: str = "UX Report"
    subtitle: str = "User Experience Review"
    client: str = "Client"
    url: str = ""
    report_type: str = "UX Review"
    date: str = ""
    prepared_by: str = "AI UX Agency for Claude Code"
    audience: str = "Business Owner / Decision-Maker"
    score: Optional[int] = None
    grade: str = ""


@dataclass
class Section:
    heading: str
    level: int
    lines: List[str]


# -----------------------------------------------------------------------------
# Parsing helpers
# -----------------------------------------------------------------------------


def clean_text(value: str) -> str:
    """Normalize markdown-ish text for paragraph rendering."""
    value = value.replace("\u2013", "-").replace("\u2014", "-")
    value = value.replace("\u201c", '"').replace("\u201d", '"').replace("\u2019", "'")
    value = value.replace("&", "&amp;")
    value = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"\*(.*?)\*", r"<i>\1</i>", value)
    value = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", value)
    return value.strip()


def strip_markdown(value: str) -> str:
    value = re.sub(r'[#*_`>"]', "", value)
    value = value.replace("\u2013", "-").replace("\u2014", "-")
    return value.strip()


def parse_metadata(markdown: str) -> ReportMeta:
    lines = [line.rstrip() for line in markdown.splitlines()]
    meta = ReportMeta()

    first_heading = next((re.sub(r"^#\s+", "", line).strip() for line in lines if line.startswith("# ")), "")
    if first_heading:
        meta.title = strip_markdown(first_heading)
        if ":" in meta.title:
            maybe_title, maybe_client = meta.title.split(":", 1)
            meta.title = maybe_title.strip() or meta.title
            meta.client = maybe_client.strip() or meta.client

    # Subtitle is often the first non-empty line after title.
    for idx, line in enumerate(lines):
        if line.startswith("# "):
            for nxt in lines[idx + 1 : idx + 5]:
                if nxt.strip() and not nxt.startswith("#"):
                    meta.subtitle = strip_markdown(nxt)
                    break
            break

    joined = "\n".join(lines[:40])
    patterns = {
        "client": r"Client:\s*([^\n]+?)(?:\s+URL:|\s+Report Type:|$)",
        "url": r"URL:\s*(https?://\S+|\S+\.\S+)",
        "report_type": r"Report Type:\s*([^\n]+?)(?:\s+Date:|\s+Prepared by:|$)",
        "date": r"Date:\s*([^\n]+?)(?:\s+Prepared by:|\s+Audience:|$)",
        "prepared_by": r"Prepared by:\s*([^\n]+?)(?:\s+Audience:|$)",
        "audience": r"Audience:\s*([^\n]+)",
    }
    for field, pattern in patterns.items():
        match = re.search(pattern, joined, re.IGNORECASE)
        if match:
            setattr(meta, field, strip_markdown(match.group(1)))

    score_match = re.search(r"(?:Overall(?:\s+Readiness)?\s+Score|Overall)\s*:?\s*(\d{1,3})\s*/\s*100", markdown, re.IGNORECASE)
    if score_match:
        meta.score = max(0, min(100, int(score_match.group(1))))
    else:
        score_match = re.search(r"\b(\d{1,3})\s*/\s*100\b", markdown)
        if score_match:
            meta.score = max(0, min(100, int(score_match.group(1))))

    if meta.score is not None:
        if meta.score >= 85:
            meta.grade = "A"
        elif meta.score >= 70:
            meta.grade = "B"
        elif meta.score >= 55:
            meta.grade = "C"
        elif meta.score >= 40:
            meta.grade = "D"
        else:
            meta.grade = "F"

    if meta.url and meta.subtitle == "User Experience Review":
        domain = meta.url.replace("https://", "").replace("http://", "").strip("/")
        meta.subtitle = f"{domain} - UX Review"

    return meta


def split_sections(markdown: str) -> List[Section]:
    sections: List[Section] = []
    current = Section("Document", 1, [])
    for raw in markdown.splitlines():
        match = re.match(r"^(#{1,3})\s+(.+)$", raw)
        if match:
            if current.lines or current.heading != "Document":
                sections.append(current)
            current = Section(strip_markdown(match.group(2)), len(match.group(1)), [])
        else:
            current.lines.append(raw.rstrip())
    if current.lines or current.heading != "Document":
        sections.append(current)
    return sections


def extract_summary(markdown: str) -> str:
    match = re.search(r"##\s+Executive Summary\s*(.*?)(?=\n##\s+|\Z)", markdown, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    text = match.group(1).strip()
    text = re.sub(r"\n{2,}", "\n\n", text)
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "\n\n".join(paragraphs[:3])


def extract_scorecard(markdown: str) -> List[Tuple[str, int, str]]:
    """Return rows of (dimension, score, status)."""
    rows: List[Tuple[str, int, str]] = []
    in_scorecard = False
    for line in markdown.splitlines():
        if re.match(r"^##\s+Scorecard", line, re.IGNORECASE):
            in_scorecard = True
            continue
        if in_scorecard and line.startswith("## "):
            break
        if in_scorecard and "|" in line and not re.search(r"Dimension|---", line, re.IGNORECASE):
            cells = [strip_markdown(c) for c in line.strip("|").split("|")]
            if len(cells) >= 2:
                score_match = re.search(r"(\d{1,3})", cells[1])
                if score_match:
                    dimension = cells[0]
                    score = max(0, min(100, int(score_match.group(1))))
                    status = cells[2] if len(cells) >= 3 else ""
                    if dimension.lower() != "overall":
                        rows.append((dimension, score, status))
    if rows:
        return rows

    # Fallback: scan any markdown table for score-like rows.
    for line in markdown.splitlines():
        if "|" not in line or re.search(r"Dimension|Category|---", line, re.IGNORECASE):
            continue
        cells = [strip_markdown(c) for c in line.strip("|").split("|")]
        if len(cells) >= 2:
            score_match = re.search(r"(\d{1,3})\s*/?\s*100?", cells[1])
            if score_match and cells[0].lower() != "overall":
                rows.append((cells[0], max(0, min(100, int(score_match.group(1)))), cells[2] if len(cells) > 2 else ""))
    return rows[:8]


def parse_markdown_table(lines: Sequence[str], start: int) -> Tuple[Optional[List[List[str]]], int]:
    if start >= len(lines) or "|" not in lines[start]:
        return None, start
    table_lines: List[str] = []
    idx = start
    while idx < len(lines) and "|" in lines[idx] and lines[idx].strip():
        table_lines.append(lines[idx])
        idx += 1
    rows: List[List[str]] = []
    for line in table_lines:
        if re.match(r"^\s*\|?\s*:?-{3,}:?", line):
            continue
        cells = [strip_markdown(c) for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return None, idx
    max_cols = max(len(r) for r in rows)
    rows = [r + [""] * (max_cols - len(r)) for r in rows]
    return rows, idx


# -----------------------------------------------------------------------------
# Custom flowables
# -----------------------------------------------------------------------------


class ScoreGauge(Flowable):
    def __init__(self, score: Optional[int], grade: str = "", width: float = 1.9 * inch, height: float = 1.55 * inch):
        super().__init__()
        self.score = score
        self.grade = grade
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        x = self.width / 2
        y = self.height / 2 + 4
        radius = 42
        score = self.score if self.score is not None else 0
        accent = score_color(score)

        c.setFillColor(LIGHT)
        c.circle(x, y, radius, stroke=0, fill=1)
        c.setStrokeColor(NAVY)
        c.setLineWidth(4)
        c.circle(x, y, radius, stroke=1, fill=0)

        # Progress arc approximation using wedge segments.
        c.setStrokeColor(accent)
        c.setLineWidth(6)
        start_angle = 90
        extent = -360 * (score / 100.0)
        c.arc(x - radius, y - radius, x + radius, y + radius, start_angle, extent)

        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 26)
        text = "--" if self.score is None else str(score)
        c.drawCentredString(x, y + 5, text)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(x + 32, y + 8, "/100")

        c.setFillColor(accent)
        c.setFont("Helvetica-Bold", 12)
        grade = f"Grade: {self.grade}" if self.grade else "UX Score"
        c.drawCentredString(x, 8, grade)


class ScoreBar(Flowable):
    def __init__(self, label: str, score: int, status: str = "", width: float = 6.2 * inch, height: float = 0.34 * inch):
        super().__init__()
        self.label = label
        self.score = score
        self.status = status
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        label_w = 2.35 * inch
        bar_x = label_w + 0.15 * inch
        bar_w = self.width - label_w - 0.78 * inch
        y = 4
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(0, y + 2, truncate(self.label, 34))
        c.setFillColor(HexColor("#E5E7EB"))
        c.roundRect(bar_x, y, bar_w, 9, 4, stroke=0, fill=1)
        c.setFillColor(score_color(self.score))
        c.roundRect(bar_x, y, max(2, bar_w * self.score / 100.0), 9, 4, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawRightString(self.width, y + 1, f"{self.score}")


def truncate(value: str, max_len: int) -> str:
    return value if len(value) <= max_len else value[: max_len - 1] + "..."


def score_color(score: int):
    if score >= 80:
        return GREEN
    if score >= 60:
        return TEAL
    if score >= 40:
        return AMBER
    return RED


# -----------------------------------------------------------------------------
# PDF rendering
# -----------------------------------------------------------------------------


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=26,
            leading=31,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=10,
        ),
        "meta": ParagraphStyle(
            "meta",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=12,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceBefore=14,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13.5,
            leading=17,
            textColor=INK,
            spaceBefore=11,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14.2,
            textColor=INK,
            spaceAfter=7,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=10.5,
            textColor=MUTED,
            spaceAfter=5,
        ),
        "callout": ParagraphStyle(
            "callout",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14.5,
            textColor=INK,
            leftIndent=10,
            rightIndent=10,
            spaceBefore=5,
            spaceAfter=8,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=13.5,
            textColor=INK,
            leftIndent=12,
            firstLineIndent=-8,
            spaceAfter=4,
        ),
    }


def header_footer(canvas, doc, brand_name: str):
    canvas.saveState()
    width, height = LETTER
    canvas.setStrokeColor(NAVY)
    canvas.setLineWidth(2)
    canvas.line(0.72 * inch, height - 0.45 * inch, width - 0.72 * inch, height - 0.45 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.72 * inch, 0.35 * inch, f"Generated by {brand_name} for Claude Code")
    canvas.drawRightString(width - 0.72 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()


def make_table(rows: List[List[str]], styles) -> Table:
    if not rows:
        return Table([[]])
    data = [[Paragraph(clean_text(cell), styles["small"]) for cell in row] for row in rows]
    col_count = len(rows[0])
    total_width = 6.75 * inch
    col_widths = [total_width / col_count] * col_count
    if col_count >= 3:
        col_widths[0] = total_width * 0.36
        remaining = total_width - col_widths[0]
        for i in range(1, col_count):
            col_widths[i] = remaining / (col_count - 1)
    table = Table(data, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("LEADING", (0, 0), (-1, -1), 10),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("BACKGROUND", (0, 1), (-1, -1), HexColor("#F9FAFB")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, HexColor("#F9FAFB")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def build_cover(meta: ReportMeta, summary: str, score_rows: List[Tuple[str, int, str]], styles) -> List:
    story: List = []
    story.append(Spacer(1, 0.28 * inch))
    story.append(Paragraph(clean_text(meta.title), styles["title"]))
    story.append(Paragraph(clean_text(meta.client), styles["subtitle"]))
    if meta.url:
        story.append(Paragraph(clean_text(meta.url), styles["meta"]))
    meta_line = f"{meta.report_type}"
    if meta.date:
        meta_line += f" | {meta.date}"
    if meta.audience:
        meta_line += f" | Audience: {meta.audience}"
    story.append(Paragraph(clean_text(meta_line), styles["meta"]))
    story.append(Spacer(1, 0.20 * inch))

    gauge = ScoreGauge(meta.score, meta.grade)
    if summary:
        summary_text = "<br/><br/>".join(clean_text(p) for p in summary.split("\n\n")[:3])
    else:
        summary_text = "This report summarizes the most important UX risks, opportunities, and recommended next steps."
    summary_table = Table(
        [[gauge, Paragraph(summary_text, styles["callout"])]],
        colWidths=[1.95 * inch, 4.7 * inch],
        hAlign="CENTER",
    )
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), HexColor("#F8FAFC")),
                ("BOX", (0, 0), (-1, -1), 0.75, LINE),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 13),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 13),
                ("LEFTPADDING", (0, 0), (-1, -1), 13),
                ("RIGHTPADDING", (0, 0), (-1, -1), 13),
            ]
        )
    )
    story.append(summary_table)

    if score_rows:
        story.append(Spacer(1, 0.22 * inch))
        story.append(Paragraph("Score Breakdown", styles["h1"]))
        for label, score, status in score_rows[:7]:
            story.append(ScoreBar(label, score, status))
            story.append(Spacer(1, 2))

    story.append(PageBreak())
    return story


def render_lines(lines: Sequence[str], styles) -> List:
    story: List = []
    idx = 0
    while idx < len(lines):
        line = lines[idx].rstrip()
        if not line.strip():
            idx += 1
            continue
        table_rows, next_idx = parse_markdown_table(lines, idx)
        if table_rows:
            story.append(make_table(table_rows, styles))
            story.append(Spacer(1, 0.12 * inch))
            idx = next_idx
            continue
        if re.match(r"^#{1,4}\s+", line):
            heading = strip_markdown(re.sub(r"^#{1,4}\s+", "", line))
            story.append(Paragraph(clean_text(heading), styles["h2"]))
        elif re.match(r"^\s*[-*]\s+", line):
            bullet = re.sub(r"^\s*[-*]\s+", "", line)
            story.append(Paragraph("• " + clean_text(bullet), styles["bullet"]))
        elif re.match(r"^\s*\d+\.\s+", line):
            item = re.sub(r"^\s*(\d+\.\s+)", r"\1", line)
            story.append(Paragraph(clean_text(item), styles["bullet"]))
        elif re.match(r"^(Finding|Severity|Effort|Confidence|Validation|What to do|Why it matters|Goal|Metric)\b", line, re.IGNORECASE):
            story.append(Paragraph(clean_text(line), styles["body"]))
        else:
            story.append(Paragraph(clean_text(line), styles["body"]))
        idx += 1
    return story


def build_pdf(markdown_path: Path, output_path: Path, brand_name: str) -> None:
    markdown = markdown_path.read_text(encoding="utf-8")
    meta = parse_metadata(markdown)
    score_rows = extract_scorecard(markdown)
    summary = extract_summary(markdown)
    styles = build_styles()

    doc = BaseDocTemplate(
        str(output_path),
        pagesize=LETTER,
        leftMargin=0.72 * inch,
        rightMargin=0.72 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.58 * inch,
        title=meta.title,
        author=brand_name,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates(
        [PageTemplate(id="main", frames=[frame], onPage=lambda canv, d: header_footer(canv, d, brand_name))]
    )

    story: List = []
    story.extend(build_cover(meta, summary, score_rows, styles))

    # Dedicated scorecard page when rows exist.
    if score_rows:
        story.append(Paragraph("Scorecard", styles["h1"]))
        rows = [["Dimension", "Score", "Status"]] + [[label, f"{score}/100", status] for label, score, status in score_rows]
        if meta.score is not None:
            rows.append(["Overall", f"{meta.score}/100", grade_label(meta.score)])
        story.append(make_table(rows, styles))
        story.append(Spacer(1, 0.15 * inch))
        for label, score, status in score_rows:
            story.append(ScoreBar(label, score, status))
            story.append(Spacer(1, 3))
        story.append(PageBreak())

    # Render all sections except title-only cover duplication; include executive summary again only if needed.
    sections = split_sections(markdown)
    for section in sections:
        if section.heading.lower().startswith("ux report") or section.heading == "Document":
            # Render only non-metadata content from the intro if any.
            body_lines = [line for line in section.lines if not re.search(r"Client:|URL:|Report Type:|Prepared by:|Audience:", line)]
            body_content = render_lines(body_lines, styles)
            if body_content:
                story.extend(body_content)
            continue
        if section.heading.lower() == "scorecard" and score_rows:
            continue
        story.append(Paragraph(clean_text(section.heading), styles["h1" if section.level <= 2 else "h2"]))
        story.extend(render_lines(section.lines, styles))

    doc.build(story)


def grade_label(score: int) -> str:
    if score >= 80:
        return "Strong"
    if score >= 60:
        return "Functional"
    if score >= 40:
        return "Needs Action"
    return "Critical Gap"


def write_fallback(markdown_path: Path, output_path: Path) -> None:
    fallback = output_path.with_suffix(".pdf-generation-needed.txt")
    fallback.write_text(
        "ReportLab is not installed, so the polished PDF could not be generated.\n\n"
        "Install it with:\n  pip install reportlab\n\n"
        f"Then rerun:\n  python scripts/generate_pdf_report.py {markdown_path}\n",
        encoding="utf-8",
    )
    print(f"ReportLab unavailable. Wrote fallback note: {fallback}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a polished UX PDF report from Markdown.")
    parser.add_argument("input", help="Path to UX Markdown report")
    parser.add_argument("--output", "-o", help="Output PDF path")
    parser.add_argument("--brand-name", default="AI UX Agency", help="Brand name shown in footer")
    args = parser.parse_args(argv)

    markdown_path = Path(args.input).expanduser().resolve()
    if not markdown_path.exists():
        print(f"Input file not found: {markdown_path}", file=sys.stderr)
        return 2
    output_path = Path(args.output).expanduser().resolve() if args.output else markdown_path.with_suffix(".pdf")

    if not REPORTLAB_AVAILABLE:
        write_fallback(markdown_path, output_path)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    build_pdf(markdown_path, output_path, args.brand_name)
    print(f"Generated polished UX PDF: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
