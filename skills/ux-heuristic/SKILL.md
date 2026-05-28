---
name: ux-heuristic
description: Use this skill for a structured usability evaluation based on UX heuristics, interaction principles, task clarity, and severity scoring.
---

# UX Heuristic Evaluation Skill

## Mission

Identify usability problems that interfere with comprehension, control, feedback, consistency, error prevention, recovery, and task completion.

## When to Use This Skill

- The user asks for a heuristic review, usability critique, UX inspection, or expert evaluation.
- There is no user research yet but the product needs a structured expert review.
- A flow, page, app, or prototype needs usability risk assessment.

## Inputs

- URL, screenshots, prototype, flow steps, product description, tasks, target users, and business goals.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-heuristics:** owns usability principles, friction diagnosis, and severity scoring.
- **ux-interaction-designer:** owns interaction behavior, feedback, states, affordances, and error recovery.
- **ux-accessibility:** flags accessibility-related usability issues.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-content-strategist:** reviews labels, instructions, errors, and comprehension.
- **ux-information-architect:** reviews navigation and structure.
- **ux-researcher:** identifies what should be validated with users.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define the target user and task context.
2. Inspect the experience against core heuristics and interaction principles.
3. Identify issues by screen, step, or component.
4. Classify severity, evidence, affected users, and likely impact.
5. Group issues by theme and prioritize.
6. Recommend fixes and validation steps.

## Analysis Framework

Use the following dimensions as the default review structure:

- Visibility of system status
- Match between system and user language
- User control and freedom
- Consistency and standards
- Error prevention
- Recognition over recall
- Flexibility and efficiency
- Aesthetic and minimalist design
- Error recovery
- Help and documentation
- Accessibility-related usability

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
# UX Heuristic Evaluation

## Summary

## Heuristic Scorecard
| Heuristic | Score | Notes |
|---|---:|---|

## Findings
Each finding includes heuristic violated, severity, evidence, impact, recommendation, effort, confidence, owner, validation.

## Priority Fixes

## Validation Plan
```

## Anti-Patterns to Avoid

- Do not treat heuristic review as user research.
- Do not cite heuristics without explaining user impact.
- Do not create academic critique disconnected from implementation.

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

