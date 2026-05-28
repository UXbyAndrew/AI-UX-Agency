---
name: ux-conversion
description: Use this skill for funnel, CTA, form, trust, objection, lead generation, trial, signup, and conversion path analysis.
---

# UX Conversion Skill

## Mission

Improve the likelihood that qualified users complete meaningful actions by reducing friction, increasing clarity, and strengthening trust without manipulative patterns.

## When to Use This Skill

- The user asks about conversion, funnels, landing pages, CTAs, signups, forms, demo requests, trials, lead gen, or drop-off.
- The product has a measurable action path that needs improvement.
- The team needs conversion recommendations grounded in UX quality and user trust.

## Inputs

- URL, funnel steps, landing page, form, analytics, conversion goals, audience, offer, pricing, objections, traffic source, screenshots.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-conversion:** owns funnel friction, CTA clarity, objections, trust, and abandonment risk.
- **ux-analytics:** owns funnel instrumentation, behavioral evidence, and measurement plan.
- **ux-content-strategist:** owns value clarity, CTA copy, objection handling, and reassurance.
- **ux-product-strategy:** owns fit between conversion goal, user intent, and business model.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-accessibility:** checks form and interaction accessibility.
- **ux-commerce:** supports ecommerce conversion paths.
- **ux-onboarding:** supports activation after signup or trial.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define the conversion goal and user intent.
2. Map funnel steps and decision moments.
3. Identify friction: unclear value, weak CTA, form burden, missing trust, hidden cost, anxiety, poor sequencing, or accessibility barriers.
4. Evaluate traffic-message-offer fit.
5. Prioritize fixes by likely impact, effort, and confidence.
6. Define experiments, analytics, and validation plan.

## Analysis Framework

Use the following dimensions as the default review structure:

- Intent match
- Value proposition clarity
- CTA specificity and placement
- Form friction
- Trust and risk reversal
- Objection handling
- Social proof and credibility
- Pricing/cost transparency
- Accessibility of conversion path
- Measurement and experimentation

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
# UX Conversion Review

## Conversion Diagnosis

## Funnel Map

## Friction and Trust Issues

## Prioritized Recommendations

## Experiment Ideas

## Measurement Plan

## Ethical Guardrails
```

## Anti-Patterns to Avoid

- Do not recommend dark patterns.
- Do not optimize conversion at the expense of user trust or accessibility.
- Do not assume traffic quality is fixed.
- Do not claim uplift without testing.

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

