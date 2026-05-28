---
name: ux-enterprise
description: Use this skill for B2B SaaS, admin tools, permissions, roles, dashboards, complex workflows, tables, bulk actions, and power-user UX.
---

# UX Enterprise Skill

## Mission

Make complex B2B and operational products more efficient, learnable, governable, and scalable without oversimplifying real workflow complexity.

## When to Use This Skill

- The user asks about enterprise UX, SaaS, admin panels, internal tools, operations, permissions, roles, dashboards, workflows, configuration, bulk actions, or audit trails.
- The product serves multiple user roles or organizations.
- The work involves complexity, governance, compliance, data density, or power users.

## Inputs

- Product description, user roles, workflow, screenshots, admin features, permissions model, data tables, dashboards, settings, analytics, support issues.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-enterprise:** owns B2B workflow complexity, roles, permissions, admin, bulk actions, and operational UX.
- **ux-dashboard:** owns data-dense views, dashboards, tables, and reporting.
- **ux-information-architect:** owns navigation, settings structure, object hierarchy, and findability.
- **ux-design-systems:** owns scalable patterns, components, states, and governance.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-researcher:** supports contextual inquiry and workflow research.
- **ux-accessibility:** checks complex interactions and data views.
- **ux-product-strategy:** supports enterprise value, adoption, retention, and roadmap tradeoffs.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define roles, permissions, workflows, objects, frequency, risk, and success criteria.
2. Map core jobs and operational dependencies.
3. Review complexity management: defaults, progressive disclosure, bulk actions, templates, auditability, collaboration, and recovery.
4. Evaluate data density, navigation, settings, permissions, and system feedback.
5. Recommend workflow, IA, component, and governance improvements.
6. Define validation with role-based task tests and operational metrics.

## Analysis Framework

Use the following dimensions as the default review structure:

- Role and permission model
- Workflow frequency and risk
- Object hierarchy
- Bulk and batch operations
- Settings and configuration
- Audit trails and history
- Collaboration and handoff
- Data density and tables
- Learnability vs power use
- Governance and scalability

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
# UX Enterprise Review

## Enterprise UX Diagnosis

## Roles, Objects, and Workflows

## Complexity and Governance Findings

## Workflow Recommendations

## IA / Dashboard / System Recommendations

## Validation Plan
```

## Anti-Patterns to Avoid

- Do not oversimplify expert workflows into consumer patterns.
- Do not ignore permissions, auditability, errors, or operational risk.
- Do not design only for new users while harming power users.

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

