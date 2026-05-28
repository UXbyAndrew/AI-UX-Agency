---
name: ux-audit
description: Use this skill for a full UX/product audit of a website, application, prototype, flow, or digital experience with prioritized findings and a roadmap.
---

# UX Audit Skill

## Mission

Run a senior-level diagnostic that identifies the most important UX, product, accessibility, content, information architecture, conversion, and strategy issues affecting users and business outcomes.

## When to Use This Skill

- The user asks for a UX audit, product audit, website critique, app review, experience review, or product diagnosis.
- The user provides a URL, screenshots, prototype, repository, product description, analytics notes, or research artifacts.
- The work needs a prioritized, evidence-aware deliverable rather than quick commentary.

## Inputs

- URL, screenshots, prototype, product description, repository, analytics, research notes, support tickets, or stakeholder goals.
- Known user segments, primary tasks, business goals, constraints, and target devices when available.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-heuristics:** owns usability diagnosis, task friction, interaction breakdowns, and severity assessment.
- **ux-accessibility:** owns inclusive design risks, WCAG-informed concerns, and remediation priorities.
- **ux-information-architect:** owns navigation, hierarchy, labeling, taxonomy, and findability.
- **ux-content-strategist:** owns UX writing, comprehension, labels, empty/error states, and decision-support content.
- **ux-product-strategy:** owns business alignment, opportunity framing, roadmap implications, and tradeoffs.
- **ux-conversion:** owns CTA, form, funnel, trust, and abandonment risk.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-researcher:** reviews evidence quality and recommends validation when assumptions dominate.
- **ux-analytics:** identifies behavioral data needs and measurement gaps.
- **ux-design-systems:** reviews consistency, components, states, and reusable patterns when UI scale is visible.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Clarify the product, audience, primary tasks, and business objective from available evidence.
2. Inventory the experience: entry points, core pages/screens, conversion/task paths, trust moments, failure states, and handoffs.
3. Run parallel agent reviews using the primary agents above.
4. Merge findings into themes. Remove duplicates and reconcile contradictions by prioritizing observed user impact, severity, and confidence.
5. Score the experience across usability, IA, content, accessibility, conversion/task completion, trust, and strategic fit.
6. Prioritize findings into critical, high, medium, and low issues.
7. Create a roadmap: quick wins, near-term fixes, strategic initiatives, and validation needs.

## Analysis Framework

Use the following dimensions as the default review structure:

- Usability and interaction friction
- Information architecture and findability
- Content clarity and decision support
- Accessibility and inclusive use
- Task completion and conversion
- Trust, confidence, and risk reduction
- Product strategy fit and measurable outcomes

## Evidence Standards

Classify every important claim using the evidence ladder below.

- **Observed:** visible in the product, page, screenshot, prototype, repository, documentation, or artifact supplied.
- **Reported:** stated by users, customers, stakeholders, sales, support, research participants, or provided notes.
- **Behavioral:** supported by analytics, funnel data, event logs, usability tests, recordings, heatmaps, search logs, or task traces.
- **Comparative:** supported by competitor, category, platform, accessibility, or design-pattern comparison.
- **Inferred:** expert interpretation based on UX practice, but not yet proven.
- **Unknown:** requires data, research, stakeholder context, or technical review.

Do not present inference as fact. When evidence is weak, lower confidence and recommend the next best validation step.

## Severity and Prioritization Model

Use severity to prioritize product risk, not to dramatize critique.

- **Critical:** blocks or seriously harms task completion, accessibility, trust, revenue, safety, compliance, or core product value.
- **High:** creates major confusion, delay, abandonment risk, rework, support burden, or decision failure.
- **Medium:** weakens clarity, confidence, efficiency, consistency, or conversion but does not usually block completion.
- **Low:** polish, refinement, optimization, or consistency issue with limited immediate impact.

For every recommendation, include:

- Severity: Critical / High / Medium / Low
- Effort: Low / Medium / High
- Confidence: High / Medium / Low
- Owner: Design / Product / Engineering / Content / Research / Analytics / Support / Cross-functional
- Validation: what would prove whether the recommendation worked


## Default Output Format

```markdown
# UX Audit

## Executive Summary
- Overall diagnosis:
- Most important user risk:
- Most important business risk:
- Highest-leverage opportunity:

## UX Scorecard
| Dimension | Score | Rationale |
|---|---:|---|

## Top Findings
For each finding include severity, evidence, user impact, business impact, recommendation, effort, confidence, owner, and validation.

## Prioritized Roadmap
- Quick wins
- Near-term improvements
- Strategic initiatives
- Research or analytics needed

## Open Questions and Assumptions
```

## Anti-Patterns to Avoid

- Do not create an unprioritized issue dump.
- Do not over-index on visual polish while ignoring task completion.
- Do not claim user behavior without evidence.
- Do not recommend redesigns when targeted fixes are sufficient.

## 10/10 Quality Bar

This skill is successful only when the output:

- gives a clear diagnosis, not a generic checklist
- separates evidence from assumption
- prioritizes what matters most
- gives implementation-ready recommendations
- explains user impact and business impact
- names tradeoffs, dependencies, and owners
- includes validation steps
- can be handed to a product/design team without additional interpretation

## Board Sign-Off

Before finalizing, apply these three review lenses:

- **Senior UX Designer:** Is this practical, interaction-aware, user-centered, and immediately useful?
- **Director of Design:** Is this strategically framed, prioritizable, cross-functional, and business-aware?
- **Principal UX Designer:** Is this systems-minded, evidence-disciplined, scalable, and mature under ambiguity?

If any lens would object, revise before presenting the final deliverable.


## Cross-Skill Handoff Rules

When this skill exposes work that belongs elsewhere, recommend the relevant next skill instead of overextending.

- Use `ux-audit` for full diagnostic coverage.
- Use `ux-quick` for rapid senior critique.
- Use `ux-flow` for task completion and flow logic.
- Use `ux-research` for study design, testing, and synthesis.
- Use `ux-personas` for evidence-based personas, segments, JTBD, and need states.
- Use `ux-journey` for cross-channel journey and service experience mapping.
- Use `ux-ia` for navigation, taxonomy, labeling, and findability.
- Use `ux-accessibility` for accessibility review and remediation.
- Use `ux-content` for UX writing, labels, empty states, errors, and comprehension.
- Use `ux-conversion` for funnels, CTAs, forms, trust, objections, and drop-off.
- Use `ux-onboarding` for activation, setup, first-run, and product education.
- Use `ux-dashboard` for dashboards, tables, analytics, reporting, and decision-support interfaces.
- Use `ux-commerce` for product detail, cart, checkout, post-purchase, and commerce trust.
- Use `ux-enterprise` for B2B, admin, power-user, role, permission, and workflow complexity.
- Use `ux-design-system` for components, tokens, patterns, states, and governance.
- Use `ux-strategy` for opportunity framing, metrics, roadmap, and product direction.
- Use `ux-report` or `ux-report-pdf` to compile final deliverables.

