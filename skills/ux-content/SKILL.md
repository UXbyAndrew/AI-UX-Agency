---
name: ux-content
description: Use this skill for UX writing, content clarity, labels, microcopy, empty states, error states, onboarding guidance, and decision-support content.
---

# UX Content Strategy Skill

## Mission

Improve comprehension, confidence, and task completion through clear, useful, user-centered content.

## When to Use This Skill

- The user asks for UX writing, content audit, copy critique, microcopy, labels, empty states, error messages, onboarding copy, or messaging hierarchy.
- Users may not understand value, next steps, requirements, errors, or consequences.
- A flow depends on explanation, trust, comparison, or decision support.

## Inputs

- Page copy, screenshots, URL, flows, product context, user segments, brand voice, constraints, support questions, error states, empty states.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-content-strategist:** owns UX writing, comprehension, labels, hierarchy, empty/error states, and decision-support content.
- **ux-information-architect:** owns structure, grouping, navigation labels, and findability.
- **ux-conversion:** owns persuasive clarity, objections, trust, and action copy.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-accessibility:** reviews plain language, labels, instructions, and assistive clarity.
- **ux-onboarding:** supports education, guidance, and progressive disclosure.
- **ux-personas:** maps content needs by user type or sophistication.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Identify the user goal and decision moment.
2. Audit content for clarity, specificity, hierarchy, usefulness, and trust.
3. Identify missing content: instructions, error recovery, consequences, reassurance, comparison, or next steps.
4. Rewrite or recommend content patterns.
5. Map content changes to user impact and business impact.
6. Define validation through comprehension testing, usability testing, search/support data, or conversion data.

## Analysis Framework

Use the following dimensions as the default review structure:

- Message hierarchy
- Plain language
- Label clarity
- Instructional usefulness
- Error prevention and recovery
- Empty state usefulness
- Decision support
- Trust and reassurance
- Progressive disclosure
- Accessibility of language

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
# UX Content Review

## Content Diagnosis

## Content Issues
Each issue includes current copy, problem, user impact, recommendation, rewrite if useful, confidence, and validation.

## Recommended Copy / Patterns

## Content Gaps

## Measurement and Validation Plan
```

## Anti-Patterns to Avoid

- Do not optimize words without understanding the user decision.
- Do not make content more clever at the expense of clarity.
- Do not rewrite everything when structure or interaction is the real issue.

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

