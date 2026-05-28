---
name: ux-strategy
description: Use this skill for product strategy, opportunity framing, UX roadmap, problem definition, prioritization, metrics, and design direction.
---

# UX Product Strategy Skill

## Mission

Turn ambiguity into a clear product/design strategy with problem framing, opportunity areas, principles, metrics, tradeoffs, and prioritized next actions.

## When to Use This Skill

- The user asks for UX strategy, product strategy, roadmap, opportunity framing, design direction, prioritization, or problem definition.
- The team has many ideas but unclear priorities.
- There is uncertainty about what user/business problem matters most.

## Inputs

- Product context, business goal, user segments, analytics, research, constraints, competitive context, current experience, roadmap ideas, stakeholder goals.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-product-strategy:** owns problem framing, opportunity areas, metrics, roadmap tradeoffs, and strategic narrative.
- **ux-researcher:** owns evidence quality and research gaps.
- **ux-analytics:** owns measurement, behavioral evidence, and success metrics.
- **ux-personas:** owns user models, segments, JTBD, and decision implications.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-conversion:** supports growth and funnel opportunities.
- **ux-enterprise:** supports B2B/product complexity.
- **ux-design-systems:** supports system-level delivery strategy.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define business objective, user problem, constraints, and decision context.
2. Inventory evidence, assumptions, risks, and open questions.
3. Frame opportunity areas and strategic choices.
4. Define principles for decision-making.
5. Prioritize opportunities by user value, business value, confidence, effort, and risk.
6. Create roadmap options, tradeoffs, metrics, and next actions.

## Analysis Framework

Use the following dimensions as the default review structure:

- Problem framing
- User value and business value
- Opportunity solution tree logic
- JTBD and segment fit
- North Star and supporting metrics
- Risk and assumption mapping
- Roadmap horizons
- Tradeoffs and constraints
- Design principles
- Validation strategy

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
# UX Product Strategy

## Strategic Diagnosis

## Problem Statement

## Evidence, Assumptions, and Risks

## Opportunity Areas

## Strategic Principles

## Roadmap Options

## Metrics and Validation

## Recommended Next Actions
```

## Anti-Patterns to Avoid

- Do not create strategy that is just a list of features.
- Do not prioritize without criteria.
- Do not ignore constraints, tradeoffs, or uncertainty.
- Do not separate user value from business value.

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

