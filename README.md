# AI UX Claude

A senior UX/product design skill suite for Claude Code.

This repo installs a `/ux` UX operating system into Claude Code, including:

- A top-level UX orchestrator skill
- 19 specialized UX workflow skills
- 16 senior UX agent lenses
- 8 core Python utility scripts
- 20 client-ready UX templates

The suite is designed for UX audits, product strategy, research planning, personas, accessibility reviews, information architecture, content clarity, conversion analysis, onboarding, dashboards, ecommerce, enterprise UX, design systems, and polished UX reports.

## One-line install

After this repo is published to GitHub, install it with:

```bash
curl -fsSL https://raw.githubusercontent.com/YOUR_USERNAME/ai-ux-claude/main/install.sh | bash
```

Replace `YOUR_USERNAME` with your GitHub username or organization.

## Local install

From the repo root:

```bash
bash install.sh
```

This copies files into:

```text
~/.claude/skills/ux/
~/.claude/skills/ux-*/
~/.claude/agents/ux-*.md
```

## What gets installed

```text
ux/SKILL.md                         # Main /ux orchestrator
skills/ux-*/SKILL.md                # Specialized UX workflow skills
agents/ux-*.md                      # Senior UX specialist agents
scripts/*.py                        # Utility scripts for capture, analysis, reports
templates/**/*.md                   # Reusable UX deliverable templates
```

## Commands this suite is designed to support

```text
/ux audit <url or product>
/ux quick <url or product>
/ux flow <url or task>
/ux research <problem or product>
/ux personas <research notes or product context>
/ux heuristic <url or screen>
/ux accessibility <url or screen>
/ux ia <url or product>
/ux content <url or screen>
/ux conversion <url or funnel>
/ux onboarding <product or flow>
/ux dashboard <product or screenshot>
/ux commerce <url or store>
/ux enterprise <product or workflow>
/ux design-system <product, repo, or screenshots>
/ux journey <product, service, or research notes>
/ux strategy <product, problem, or opportunity>
/ux report
/ux report-pdf
```

## Repository structure

```text
ai-ux-claude/
├── README.md
├── install.sh
├── uninstall.sh
├── LICENSE
├── ux/
│   └── SKILL.md
├── skills/
│   ├── SKILL_RUBRIC.md
│   ├── README.md
│   └── ux-*/SKILL.md
├── agents/
│   ├── AGENT_RUBRIC.md
│   ├── README.md
│   └── ux-*.md
├── scripts/
│   ├── README.md
│   ├── requirements.txt
│   └── *.py
├── templates/
│   ├── README.md
│   ├── TEMPLATE_MANIFEST.md
│   └── **/*.md
└── examples/
    └── sample-outputs/
```

## Python scripts

Optional scripts support capture, UX analysis, accessibility pre-scans, flow extraction, content inventory, finding prioritization, Markdown report generation, and PDF report generation.

Install optional dependencies with:

```bash
pip install -r scripts/requirements.txt
```

For screenshot capture with Playwright:

```bash
python -m playwright install chromium
```

## Design principles

This suite prioritizes:

- Evidence over opinion
- Clear severity and priority models
- Practical recommendations
- Accessibility and inclusion
- Business/user outcome alignment
- Executive-ready communication
- Senior-level design judgment

## Notes

This suite supports UX judgment; it does not replace expert review, user research, accessibility testing, or product decision-making.
