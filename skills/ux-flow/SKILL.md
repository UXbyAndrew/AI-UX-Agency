---
name: ux-flow
description: Use this skill to analyze a specific user task, funnel, workflow, or step-by-step path through a product or service.
---

# UX Flow Analysis Skill

## Mission

Diagnose how well a specific task flow supports user intent, comprehension, momentum, error recovery, accessibility, and completion.

## When to Use This Skill

- The user asks about a signup, checkout, booking, onboarding, demo request, account creation, admin, reporting, or product workflow.
- The work involves steps, states, decisions, branching paths, or completion risk.
- The user wants a flow map, friction analysis, or task-completion recommendations.

## Inputs

- Task to analyze, user type, starting point, endpoint, screens/pages, URL, prototype, screenshots, analytics, or event data.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-interaction-designer:** owns step logic, affordances, feedback, state changes, and error prevention.
- **ux-heuristics:** owns usability violations and friction patterns.
- **ux-conversion:** owns CTA, form, trust, and abandonment risk when the flow is conversion-oriented.
- **ux-analytics:** owns measurement plan, funnel events, and drop-off signals.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-accessibility:** reviews keyboard, focus, form, state, and assistive technology risks.
- **ux-content-strategist:** reviews instructional copy, labels, errors, confirmations, and microcopy.
- **ux-service-designer:** reviews cross-channel or operational handoffs.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define the user, goal, trigger, starting state, success state, and failure states.
2. Map each step, decision point, required input, system response, and dependency.
3. Identify friction: uncertainty, repetition, missing feedback, unnecessary fields, weak recovery, trust gaps, or accessibility barriers.
4. Assess every friction point by severity, evidence, effort, and confidence.
5. Recommend improved flow logic, content, interaction, validation, and measurement.
6. Define success metrics and instrumentation needs.

## Analysis Framework

Use the following dimensions as the default review structure:

- Entry trigger
- User goal and mental model
- Step count and cognitive load
- Decision points
- Form/input burden
- Feedback and system status
- Error prevention and recovery
- Accessibility of interactions
- Completion confidence
- Measurement and drop-off visibility

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
# UX Flow Analysis

## Flow Summary
- User:
- Goal:
- Start state:
- Success state:

## Current Flow Map
| Step | User action | System response | Risk |
|---|---|---|---|

## Friction Points

## Recommended Flow Improvements

## Instrumentation and Validation Plan

## Open Questions
```

## Anti-Patterns to Avoid

- Do not critique screens in isolation when the problem is flow logic.
- Do not ignore edge cases, errors, empty states, or recovery paths.
- Do not optimize for fewer steps if clarity or trust would suffer.

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

