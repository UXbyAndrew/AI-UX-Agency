---
name: ux-research
description: Use this skill to create research plans, usability tests, interview guides, surveys, synthesis plans, and evidence-backed UX recommendations.
---

# UX Research Skill

## Mission

Turn ambiguous product questions into rigorous, practical research that improves product, design, and strategic decisions.

## When to Use This Skill

- The user needs a research plan, interview guide, usability test, survey, synthesis, or validation approach.
- The work involves assumptions, unknown users, uncertain needs, or product risk.
- The team needs to learn what to build, improve, remove, or validate.

## Inputs

- Research goal, product context, target users, assumptions, hypotheses, prototype/URL, constraints, timeline, existing evidence, analytics, and decisions to inform.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-researcher:** owns research design, methodology, study quality, bias control, and synthesis.
- **ux-personas:** converts findings into behavioral models when appropriate.
- **ux-product-strategy:** ties research questions to product decisions and roadmap risk.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-analytics:** aligns qualitative research with behavioral signals.
- **ux-content-strategist:** reviews interview language, survey wording, and concept comprehension.
- **ux-accessibility:** ensures inclusive recruiting and testing considerations.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Define the decision the research must inform.
2. Identify assumptions, risks, and hypotheses.
3. Choose the leanest valid method: interviews, usability test, diary study, survey, concept test, card sort, tree test, analytics review, or mixed method.
4. Define participant criteria, sample logic, screening questions, tasks, and discussion guide.
5. Create the analysis plan before data collection.
6. Specify evidence quality, limitations, and expected outputs.
7. Recommend how findings should change product, design, content, or strategy decisions.

## Analysis Framework

Use the following dimensions as the default review structure:

- Decision-first research framing
- Assumption and risk mapping
- Method fit
- Participant quality
- Task realism
- Bias control
- Synthesis plan
- Evidence-to-decision traceability

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
# UX Research Plan

## Decision to Inform

## Research Questions

## Key Assumptions and Risks

## Recommended Method

## Participants and Recruiting Criteria

## Study Protocol / Interview Guide / Test Tasks

## Synthesis Framework

## Expected Decisions and Deliverables

## Limitations and Validation Follow-Up
```

## Anti-Patterns to Avoid

- Do not run research for curiosity without a decision target.
- Do not ask leading questions.
- Do not overgeneralize small qualitative samples.
- Do not produce personas or recommendations without evidence traceability.

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

