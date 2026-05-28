# UX Suite Core Scripts

These scripts support the UX skills by producing repeatable evidence, inventories, scoring, and report outputs. They are intentionally dependency-light and designed to fail gracefully.

## Core 8

1. `capture_pages.py` — fetch HTML, metadata, and optional screenshots.
2. `analyze_page_ux.py` — extract page structure, CTAs, forms, hierarchy, and risk flags.
3. `extract_flows.py` — turn page analysis or manual steps into flow maps.
4. `accessibility_scan.py` — run a practical accessibility pre-scan.
5. `content_inventory.py` — extract UX writing, CTA, form, trust, pricing, and error copy.
6. `score_ux_findings.py` — normalize and prioritize findings.
7. `generate_ux_report.py` — compile outputs into `UX-REPORT.md`.
8. `generate_pdf_report.py` — convert `UX-REPORT.md` into PDF with ReportLab.

## Suggested first run

```bash
python scripts/capture_pages.py https://example.com --out outputs --desktop --mobile
python scripts/analyze_page_ux.py outputs/page-metadata.json --out outputs
python scripts/accessibility_scan.py outputs/html/*.html --out outputs
python scripts/content_inventory.py outputs/html/*.html --out outputs
python scripts/extract_flows.py --task "complete primary conversion task" --analysis outputs/page-analysis.json --out outputs
python scripts/score_ux_findings.py outputs/accessibility-scan.json --out outputs
python scripts/generate_ux_report.py --input-dir outputs --out outputs/UX-REPORT.md
python scripts/generate_pdf_report.py outputs/UX-REPORT.md --out outputs/UX-REPORT.pdf
```

## Optional dependencies

```bash
pip install beautifulsoup4 reportlab playwright
python -m playwright install chromium
```

Without optional dependencies, most scripts still run with lighter parsing and graceful fallbacks.
