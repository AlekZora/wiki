---
type: concept
title: Block Universe
aliases: ["eternalism", "4D block", "static time", "spacetime block"]
tags: [physics, philosophy, time, causality, ai, determinism]
sources: ["negative-time-quantum-paradox"]
updated: 2026-06-15
---

## Definition
The block universe (also called eternalism) is a philosophical and physical model in which all moments of time — past, present, and future — exist simultaneously within a single four-dimensional object. Time does not flow; all temporal coordinates are equally real. The experience of time passing is a feature of consciousness navigating the block, not a feature of the block itself. In this model, time is a dimension like space: just as "left" and "right" do not flow into each other, "before" and "after" do not either.

The model is scientifically motivated by special relativity, which already treats time as a fourth dimension, and is the cleanest interpretation of quantum retrocausality: if all moments coexist, there is no need for information to travel backward in time between entangled particles — the correlation simply exists as a fact within the block at different coordinates.

## How I Think About It
The block universe is disturbing precisely because it makes the future as fixed and unchangeable as the past. It is not that things will happen — they already do, at different coordinates. Every decision, every outcome, every ending is already there in the block. The finale is already written.

What makes it more than philosophy is that it resolves a real physics problem. Quantum entanglement produces correlations between particles that cannot be explained by any prior common cause. The standard interpretation requires either faster-than-light signaling or accepting that measurement somehow creates reality at a distance. The block universe dissolves this: if the future already exists, particles don't need to signal each other across space. The correlation is a structural feature of the block — it's not produced, it's read.

The hardest implication is for free will. If the future already exists as a fact in the block, agency becomes something that happens within a predetermined script rather than authoring it. Compatibilism argues agency is still real within the block, but the debate is genuinely open.

## AI Integration
- LLMs exist in a de facto block universe with respect to their training data: all temporal moments from the training corpus coexist simultaneously in the model's weights, with no directional flow. A 1995 text and a 2024 text are equally "now" inside the model. The model experiences no arrow of time through its training data — time, for an LLM, really is just another dimension
- This creates LLM temporal blindness: without explicit date anchoring, the model cannot intrinsically distinguish recent from old information. It has no internal mechanism to know that some facts are newer than others. The block universe framing makes this a structural property rather than a bug to patch
- The training-inference gap can be reframed in block universe terms: training processes all time periods simultaneously (block mode); inference requires producing temporally coherent responses about a dynamic, flowing world (arrow mode). These are genuinely different modes, and the friction between them — models confidently citing outdated information, failing to recognize temporal context — is a consequence of this mismatch
- Backward induction in planning and game theory is already retrocausal reasoning: the algorithm starts from a known future state (treated as if it already exists) and works backward to optimal present actions. Block universe framing makes this structurally legible — the future state isn't hypothetical, it's a coordinate in a 4D space the planner is navigating
- If AI systems were explicitly designed around block-universe reasoning — treating all temporal states as equally accessible rather than directionally prior — this could support different planning architectures, more like constraint satisfaction across a 4D state space than sequential causal inference. Whether this would be useful depends on whether the domain itself has block-like properties

## Related Concepts
- [[simulation-hypothesis]] — both propose that experienced reality may not be the fundamental one; the block universe is the most physically motivated version of a "pre-written" reality
- [[paradox]] — the block universe is proposed specifically to resolve the retrocausality paradox (cause before effect) without contradiction; the paradox dissolves if all moments coexist
- [[time-travel-narrative]] — narrative time-travel logic implicitly assumes either block universe (the future already exists, you visit it) or dynamic time (the future is unwritten, you can change it); this choice determines whether paradoxes arise in the story
- [[world-models]] — the block universe is the most complete world model possible: one that contains all states across all time simultaneously; LLM weights are its closest existing approximation

## Open Questions
- Does the block universe imply hard determinism, and if so, what does AI "goal-pursuit" actually mean within it? If future outputs are already fixed, is the appearance of goal-directedness illusory in the same way free will might be?
- Can an AI system be deliberately designed to perform block-universe reasoning — treating all temporal states as equally accessible — and would this improve planning in high-uncertainty domains?
- Is LLM temporal blindness a fixable engineering problem (better date grounding) or a structural consequence of block-universe training that would require a fundamentally different architecture to resolve?
- What would an AI that experiences time as genuinely directional — with a strong built-in arrow — behave like compared to current LLMs? Would it reason better about change, consequence, and sequence?
