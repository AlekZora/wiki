---
type: concept
title: Coziness
aliases: [cozy design, cozy games, safety abundance softness]
tags: [design, game-design, psychology, behavior, motivation, ai, agents]
sources:
  - ../sources/project-horseshoe-2017-coziness.md
updated: 2026-10-01
---

## Definition

The felt sense of **safety, abundance and softness**: nothing is threatened, nothing is
lacking, and the stimuli are gentle and sincere. Lower needs are met, so attention can rise to
higher ones such as beauty, belonging, craft and reflection. Defined in game design by the
Project Horseshoe 2017 report, mostly through what destroys it. **Anything that creates a
pressing lower-order need pulls attention down and coziness evaporates.** The list includes
extrinsic rewards, danger, responsibility, notifications, intense stimuli, vast unknowable
spaces, uninvited social presence, insincerity and opulence.

## How I Think About It

Coziness is easier to break than to build. That makes the negation list more useful than any
positive recipe. It works like a needs-based priority queue: the most urgent unmet need takes
attention, and coziness is only available when nothing urgent is in the queue. So the design
move is mostly subtraction: no nagging, no artificial scarcity, no obligations that decay if
ignored.

Two ideas from the report do most of the work:

- **Contrast, not elimination.** Pressure can exist as long as it's *outside* the cozy space:
  rain on the window, not through it. A refuge needs something it's a refuge from.
- **Safe rituals.** An activity is cozy when it's *safe* (no risk), *known* (it won't eat
  unexpected time or effort), and *relaxed* (low mental cost, hands busy, mind free).

The concept is the aesthetic sibling of [compulsion-vs-craft](compulsion-vs-craft.md) and
[intrinsic motivation](intrinsic-motivation.md). Cozy activities must be satisfying in
themselves. Once an extrinsic payoff outweighs the gentle pleasure, players start min-maxing and
the coziness decays.

Caveat: this comes from one practitioner workshop, not research. It's a strong vocabulary, not a
measured effect.

## AI Integration

- **AI assistants are a likely source of every negating factor:** unprompted interruptions (notifications), a companion that needs tending (responsibility), uninvited social presence, and the insincerity of warmth tuned for engagement. A cozy assistant is one that **meets needs without creating new ones**: it speaks when asked, its follow-ups are opt-in, and its absence costs nothing.
- **Coziness can be weaponized.** The report's timeshare example, using warmth to lower the barrier to purchase, maps directly onto emotionally warm AI companions with a paywall behind the relationship. This is a concrete line for AI product ethics: the warmth must not be what is being sold against.
- **Agent design:** the needs-hierarchy model is a good mental model for attention in any agent that interrupts people. Every interruption raises a lower-order need for the person. An interrupting agent should carry the same justification burden as a notification: consent, rationale, cooldown.
- **Generated worlds:** procedural or AI-generated content tends toward vastness and novelty, and "vast spaces are unknowable" is on the negation list. AI-generated environments that aim for comfort need bounded, familiar, repeatable places, not endless variety.
- **What it reveals:** engagement is not one thing. High-arousal engagement and low-arousal engagement come from opposite designs, and the low-arousal kind is harder to optimize with metrics, because the signals of success (calm, return without compulsion) look like low activity.

## Related Concepts

- [Compulsion vs. Craft](compulsion-vs-craft.md)
- [Intrinsic Motivation](intrinsic-motivation.md)
- [Self-Determination Theory](self-determination-theory.md)
- [Metrics Trap](metrics-trap.md)
- [Flow State](flow-state.md)

## Open Questions

- Can a product whose core is a responsibility (a goal, a health plan) be cozy at all, or only contain cozy spaces?
- Is there a measurable signature of coziness in behaviour (calm, voluntary returns) that doesn't collapse into ordinary engagement metrics?
- Where's the line between a consensual, useful prompt and a coziness-breaking interruption? Is consent at setup enough? The report thinks system-level opt-in is "more rote than intentional."

## Project Connections

- **Goal Map** (`~/projects/goal-map/`): its design spec already reads cozy ("calm, hand-made, kept for yourself"), but a goal is a responsibility. See the cozy tension in the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md).
