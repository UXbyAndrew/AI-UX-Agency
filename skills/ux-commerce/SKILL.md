---
name: ux-commerce
description: Use this skill for ecommerce product discovery, product detail pages, carts, checkout, payments, shipping, returns, trust, and post-purchase UX.
---

# UX Commerce Skill

## Mission

Improve commerce experiences by reducing purchase friction, increasing decision confidence, making costs and policies clear, and protecting trust throughout the buying journey.

## When to Use This Skill

- The user asks about ecommerce, product pages, checkout, cart, payment, shipping, returns, recommendations, reviews, pricing, or post-purchase experience.
- The product involves buying, comparing, subscribing, booking, or transacting online.
- The team needs conversion improvements without manipulative patterns.

## Inputs

- URL, product page, category page, cart/checkout flow, analytics, traffic source, products, pricing, shipping/return policy, reviews, screenshots.

If inputs are incomplete, proceed with best-effort analysis. Explicitly mark unknowns instead of blocking the work.

## Primary Agents

Use these agents as the main expert lenses when running this skill:

- **ux-commerce:** owns product discovery, PDP, cart, checkout, payments, shipping, returns, trust, and post-purchase.
- **ux-conversion:** owns funnel, CTA, form, objection, and abandonment analysis.
- **ux-content-strategist:** owns product information, policy clarity, error messages, and reassurance.
- **ux-accessibility:** owns accessible forms, checkout, payment, and commerce interactions.
- **ux-analytics:** owns funnel metrics, cart abandonment, and measurement plan.

## Supporting Agents

Consult these agents when their domain appears in the work:

- **ux-information-architect:** supports categories, search, filters, and product discovery.
- **ux-interaction-designer:** supports cart, quantity, variant, validation, and payment interactions.

## Agent Reconciliation Rules

When agents disagree, reconcile findings using this order:

1. Direct evidence from the supplied product, research, analytics, or artifacts.
2. Impact on task completion, accessibility, trust, safety, revenue, retention, or core product value.
3. Confidence level and severity.
4. Implementation feasibility and cross-functional dependencies.
5. Strategic alignment with the user and business objective.

Do not include duplicate findings from multiple agents. Merge them into one stronger recommendation with clear ownership.

## Workflow

1. Map commerce journey: discovery, product evaluation, cart, checkout, payment, confirmation, post-purchase.
2. Identify decision and trust moments.
3. Evaluate product information, pricing, availability, reviews, policies, cart behavior, form burden, payment options, and error recovery.
4. Prioritize friction by likelihood to block purchase or damage trust.
5. Recommend UX, content, accessibility, and measurement improvements.
6. Define experiments and success metrics.

## Analysis Framework

Use the following dimensions as the default review structure:

- Product discovery
- Product detail clarity
- Comparison and selection
- Price and cost transparency
- Shipping and return confidence
- Reviews and proof
- Cart behavior
- Checkout form burden
- Payment trust
- Error recovery
- Post-purchase reassurance

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
# UX Commerce Review

## Commerce Diagnosis

## Journey Map

## Purchase Friction and Trust Risks

## PDP / Cart / Checkout Recommendations

## Accessibility and Content Recommendations

## Experiment and Measurement Plan
```

## Anti-Patterns to Avoid

- Do not recommend deceptive urgency, hidden costs, or dark patterns.
- Do not optimize checkout while ignoring product confidence upstream.
- Do not ignore returns, shipping, fulfillment, or support impact.

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

