---
name: ux-onboarding
description: Use this skill for activation, first-run experience, setup flows, product education, empty states, lifecycle nudges, and time-to-value analysis.
---

# UX Onboarding Skill

## Mission

Help new or returning users reach meaningful value faster with less confusion, lower setup burden, stronger confidence, and better product momentum.

## When to Use This Skill

- The user asks about onboarding, activation, first-run experience, setup, tutorials, walkthroughs, empty states, product education, or habit formation.
- A signup, trial, account setup, or initial workflow has drop-off or low activation.
- The product needs a clearer path to first value.

## Inputs

- Product description, screenshots, onboarding flow, signup flow, activation metric, user segments, analytics, lifecycle emails, empty states, setup requirements.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-onboarding:** owns activation, first-run flow, setup logic, aha moment, product education, and lifecycle momentum.
- **ux-product-strategy:** owns activation metric, value definition, and roadmap tradeoffs.
- **ux-content-strategist:** owns guidance, labels, education, empty states, and progressive disclosure.
- **ux-analytics:** owns activation events, drop-off measurement, and cohort analysis.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-personas:** maps onboarding differences by role, sophistication, or lifecycle stage.
- **ux-accessibility:** reviews onboarding accessibility and inclusive guidance.
- **ux-interaction-designer:** reviews state, feedback, and setup interactions.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define first value, activation, and user readiness.
2. Map the current onboarding journey from entry through first meaningful outcome.
3. Identify friction: setup burden, unclear next step, excessive education, missing defaults, weak empty states, permissions, data import, or anxiety.
4. Separate required setup from optional personalization.
5. Recommend improved sequencing, guidance, defaults, empty states, and success feedback.
6. Define activation metrics and validation plan.

## Analysis Framework

Use the following dimensions as the default review structure:

- First value definition
- Time to value
- Setup burden
- Progressive disclosure
- Aha moment
- Empty states
- Guidance and education
- Personalization and defaults
- Lifecycle nudges
- Activation measurement

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
# UX Onboarding Review

## Activation Diagnosis

## Current Onboarding Map

## Friction Points

## Recommended Onboarding Model

## Content and Empty State Recommendations

## Activation Metrics

## Experiment / Validation Plan
```

## Anti-Patterns to Avoid

- Do not add tutorials to compensate for unclear product design.
- Do not force users through unnecessary setup before value.
- Do not confuse account creation with activation.
- Do not design one onboarding path for all user types when needs differ.

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

