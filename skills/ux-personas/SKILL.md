---
name: ux-personas
description: Use this skill to create evidence-based personas, behavioral segments, JTBD profiles, need states, role matrices, and design implications from research or product context.
---

# UX Personas Skill

## Mission

Transform research and behavioral evidence into useful user models that guide product, design, content, onboarding, and prioritization decisions without inventing false certainty.

## When to Use This Skill

- The user asks for personas, user segments, archetypes, JTBD, need states, anti-personas, or role-based user models.
- Research notes, interviews, analytics, support data, surveys, or product context need synthesis into decision tools.
- The team needs to understand differences between buyers, users, admins, operators, influencers, or lifecycle stages.

## Inputs

- Research notes, transcripts, survey results, analytics, support tickets, stakeholder notes, product description, market context, or assumptions to validate.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-personas:** owns persona structure, segmentation logic, JTBD mapping, behavioral archetypes, and design implications.
- **ux-researcher:** validates evidence quality and flags weak or biased data.
- **ux-analytics:** supports behavioral segmentation and data-backed distinctions.
- **ux-product-strategy:** ensures personas affect decisions, prioritization, and roadmap tradeoffs.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-content-strategist:** maps content needs by persona or segment.
- **ux-onboarding:** maps lifecycle and activation-stage differences.
- **ux-enterprise:** supports role, permission, and organizational complexity.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Inventory evidence sources and classify evidence quality.
2. Identify meaningful behavioral differences: goals, context, tasks, constraints, confidence, sophistication, triggers, objections, and decision criteria.
3. Create the minimum number of user models needed to change design decisions.
4. Choose the best model type: persona, JTBD profile, need state, role matrix, lifecycle segment, or anti-persona.
5. Map each model to design, content, product, and measurement implications.
6. Mark assumptions and create a validation plan.

## Analysis Framework

Use the following dimensions as the default review structure:

- Behavior over demographics
- JTBD and task context
- Motivations and barriers
- Current workflow
- Decision criteria
- Confidence and sophistication
- Lifecycle stage
- Role and permission context
- Design implications
- Validation status

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
# UX Personas and Behavioral Models

## Evidence Summary

## Segmentation Logic

## Personas / JTBD Profiles / Need States
For each model include context, core job, goals, workflow, pain points, motivations, barriers, triggers, objections, decision criteria, evidence, assumptions, and design implications.

## Persona-to-Design Implication Matrix

## Anti-Personas or Exclusions

## Validation Plan
```

## Anti-Patterns to Avoid

- Do not create demographic caricatures.
- Do not invent names, backstories, or motivations that do not affect design decisions.
- Do not create too many personas.
- Do not treat stakeholder assumptions as research evidence.

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

