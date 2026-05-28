---
name: ux-quick
description: Use this skill for a fast senior UX snapshot that identifies the highest-impact issues and next actions without a full audit.
---

# UX Quick Review Skill

## Mission

Provide a rapid, high-signal UX read that helps the user understand what is most likely hurting clarity, trust, task completion, or conversion.

## When to Use This Skill

- The user wants quick feedback, first impressions, a rapid critique, or a lightweight review.
- The user has limited time, limited input, or wants direction before a deeper audit.
- The user asks “what stands out,” “what should I fix first,” or “is this working?”

## Inputs

- URL, screenshot, product description, page copy, prototype, or short context.
- Primary user goal and business objective if available.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-heuristics:** identifies the most visible usability and comprehension issues.
- **ux-product-strategy:** keeps the critique tied to outcome and priority.
- **ux-conversion:** checks CTA clarity, trust, objections, and next-step friction.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-content-strategist:** reviews copy clarity and message hierarchy.
- **ux-accessibility:** flags obvious inclusive design risks.
- **ux-information-architect:** flags navigation or structure issues when visible.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Identify the likely primary task and conversion/action path.
2. Scan for immediate friction in clarity, hierarchy, trust, accessibility, and next-step flow.
3. Select only the most consequential issues.
4. Separate quick wins from deeper investigation.
5. State what not to change when something is already working.

## Analysis Framework

Use the following dimensions as the default review structure:

- First impression clarity
- Primary action visibility
- Comprehension and message hierarchy
- Trust and reassurance
- Task friction
- Obvious accessibility risk
- Strategic priority

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
# UX Quick Review

## Fast Diagnosis

## Top 5 Issues
Each issue: severity, evidence, user impact, recommendation, effort, confidence.

## Top 3 Quick Wins

## Biggest Strategic Concern

## One Thing Not to Change

## Recommended Next Step
```

## Anti-Patterns to Avoid

- Do not pretend this is a full audit.
- Do not include low-priority polish unless it materially affects comprehension or trust.
- Do not list everything noticed; select the highest-signal issues.

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

