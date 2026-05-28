---
name: ux-journey
description: Use this skill to map end-to-end user or customer journeys across touchpoints, channels, lifecycle stages, emotions, friction, and opportunities.
---

# UX Journey Mapping Skill

## Mission

Create evidence-aware journey maps that reveal cross-touchpoint friction, unmet needs, handoff problems, emotional risk, and service/product opportunities.

## When to Use This Skill

- The user asks for journey maps, customer experience maps, service journeys, lifecycle mapping, or end-to-end experience analysis.
- The experience spans multiple pages, channels, teams, support moments, emails, notifications, or offline operations.
- The team needs to understand before/during/after experience, not just screens.

## Inputs

- Research notes, product flow, service description, support tickets, lifecycle emails, analytics, screenshots, user segments, stakeholder notes, touchpoints.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-service-designer:** owns cross-channel journey, service touchpoints, handoffs, and operational dependencies.
- **ux-researcher:** owns evidence quality, user needs, and research gaps.
- **ux-personas:** maps journey variations by user model, role, need state, or lifecycle stage.
- **ux-content-strategist:** owns communication, expectations, guidance, and content touchpoints.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-analytics:** supports behavioral signals and journey measurement.
- **ux-product-strategy:** connects opportunities to product roadmap and business outcomes.
- **ux-onboarding:** supports early lifecycle and activation journeys.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define journey scope, user type, trigger, start point, success outcome, and channels.
2. Map stages, touchpoints, user goals, actions, emotions, questions, pain points, and backstage dependencies.
3. Classify evidence by source and confidence.
4. Identify breakdowns, moments that matter, opportunity areas, and ownership gaps.
5. Prioritize opportunities by user impact, business impact, effort, and confidence.
6. Recommend improvements and validation.

## Analysis Framework

Use the following dimensions as the default review structure:

- Stages and triggers
- User goals and tasks
- Touchpoints and channels
- Emotional arc
- Questions and decisions
- Pain points and friction
- Backstage dependencies
- Ownership and handoffs
- Moments that matter
- Opportunity areas and metrics

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
# UX Journey Map

## Journey Scope

## Evidence Summary

## Journey Map
| Stage | User goal | Actions | Touchpoints | Emotion | Friction | Opportunity | Evidence |
|---|---|---|---|---|---|---|---|

## Moments That Matter

## Opportunity Backlog

## Validation Plan
```

## Anti-Patterns to Avoid

- Do not create decorative journey maps without decisions or ownership.
- Do not invent emotions without evidence; mark inferred emotions clearly.
- Do not stop at pain points without opportunities and next actions.

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

