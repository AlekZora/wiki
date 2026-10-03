---
type: concept
title: Post-Generation Editing
aliases: [the filter moved, editor role, ready vs good]
tags: [ai, design, creativity, systems, agents, engineering]
sources: [../sources/katie-dill-stripe.md]
updated: 2026-09-29
---

## Definition

When the cost of producing candidates collapses, the quality filter that used to sit inside the production process (scarcity forced early pruning) has to be applied after production, to a pile of finished-looking things. The work of deciding what is actually good, whole and worth keeping becomes its own role: the editor. The trap is treating "built" as "finished" and "finished" as "good."

## How I Think About It

Scarcity was doing quiet work. If you can only complete one of twenty ideas, you argue about the twenty early and prune as you go, and the survivor is shaped by many small decisions. If you can generate twenty a week, no one is forced to decide, and the decisions pile up at the end where saying no is more expensive because something polished already exists. Katie Dill's microwave-burrito image captures the perceptual failure: speed of arrival makes a mediocre result feel acceptable.

The editing question is not yes/no but "is it fully formed, and how do we finish it?" That includes the level of detail (going one level deeper than the user can see) and whole-experience coherence, since parts that look fine alone can feel disjointed together.

## AI Integration

- **AI changes it:** generation is cheap, so selection is the bottleneck. This is the generate-then-verify asymmetry applied to taste, not just correctness.
- **Agent design:** any pipeline of generate → ship needs an explicit post-hoc filter stage with an owner. Autonomous agents fixing issues "while we sleep" have no scarcity-imposed pruning either, so the filter must be encoded (standards, evals, critic agents) or performed by a human editor.
- **What exists:** iterate-and-judge loops (Stripe's 56 animation re-rolls, each judged by a person), adversarial critic agents, design systems that encode intent as patterns and flows.
- **Open AI question:** the human editor here supplies taste as a search-guidance signal over cheap samples. Whether a model can play that role reliably, or only reproduces the most-likely-good, is unresolved. It ties to [metrics-trap](metrics-trap.md): an automated filter is only as good as what it measures.
- **What it reveals:** quality has been partly a byproduct of scarcity, not only of skill.

## Related Concepts

- [Harness Engineering](harness-engineering.md)
- [Vibe Coding](vibe-coding.md)
- [Metrics Trap](metrics-trap.md)
- [Compulsion vs Craft](compulsion-vs-craft.md)
- [Representation Shapes the Solution](representation-shapes-the-solution.md)

## Open Questions

- Can a critic model substitute for the human editor, or does editing need the unexpected-detail judgment the talk says AI lacks?
- Who is the editor in a team of three shipping what used to need thirty?
- Is there a way to reintroduce cheap scarcity (a fixed budget of candidates) so pruning stays in the process?

## Project Connections

- [Attractor Zone](../projects/attractor/attractor-zone.md): volume posting across five platforms makes a review pass before publishing the equivalent of the editor stage.
