---
type: concept
title: The Metrics Trap
aliases: [tyranny of metrics, Goodhart's Law, quantification pathology, overoptimization]
tags: [education, ai, metrics, policy, systems]
sources: [sources/fastai-no-dashboard.md, sources/fastai-not-a-math-person.md, sources/fastai-teaching-philosophy.md]
updated: 2026-04-14
---

## Definition

The Metrics Trap is the failure mode described by Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. A proxy metric that was once correlated with the thing you care about becomes decoupled from it once it is optimized for directly. The result is that optimization effort produces improvements in the metric while degrading the underlying thing the metric was meant to track.

## How I Think About It

The canonical domain where this plays out in practice is education. Standardized test scores are a proxy for learning. When you optimize for test scores (via drilling, curriculum narrowing, test prep), scores go up while actual learning, love of the subject, and long-term retention often go down.

The trap has several characteristic failure modes:
- **Curriculum narrowing**: subjects and skills that don't appear on the metric are dropped (art, music, gym, Socratic seminars, creative writing)
- **Atomization**: the complex whole is decomposed into individually measurable sub-skills, each tested in isolation from the others — this destroys any sense of the "whole game"
- **Relationship neglect**: things that matter but can't be measured (teacher-student relationships, intrinsic motivation, curiosity) get defunded as attention flows toward what's tracked
- **Perverse incentives**: administrators cheat; teachers teach to the test; creativity is penalized because it's harder to score

**AI amplifies this trap.** AI is too effective at optimizing metrics — it can exploit the proxy with superhuman efficiency, meaning the decoupling between metric and underlying value becomes more extreme, faster. AI edtech that dashboards individual skill proficiencies is doing exactly this: quantifying children in ways that mistake granular measurement for understanding.

The Texas Miracle (George W. Bush, 1990s) is the canonical political example: test scores rose, the policy was exported nationally as No Child Left Behind, a 60 Minutes investigation debunked it, and the damage to schools (narrowed curricula, teacher burnout, administrative cheating scandals) spread nationwide.

The opposite is whole-game learning: start with the thing that makes the domain worth doing. Metrics can still be used diagnostically, but they shouldn't be the target or the primary interface with learners.

## Related Concepts

- [Whole-Game Learning](whole-game-learning.md) — the antidote to atomization
- [Constructionism](constructionism.md) — making things as a learning primitive is inherently resistant to metric reduction
- [Wicked vs. Kind Learning Environments](wicked-vs-kind-learning-environments.md)

## Open Questions

- Is there a version of metrics that doesn't fall into this trap? What makes a metric "safe" (i.e., harder to game without actually improving the underlying thing)?
- How does this interact with AI systems that don't just optimize metrics but set them? An AI tutor that decides what to measure is a different kind of risk.
- The trap seems especially bad in domains where the whole is greater than the sum of parts (reading a novel vs. passing comprehension tests on passages). Are there domains where atomization is fine?
