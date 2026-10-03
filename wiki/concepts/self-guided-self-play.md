---
type: concept
title: Self-Guided Self-Play
aliases: [SGS, self-play for LLMs, self-guided self-play]
tags: [ai, ml, llm, self-play, training, agents]
sources: [5-papers-ycombinator.md]
updated: 2026-06-13
---

## Definition

Self-Guided Self-Play (SGS) is a training mechanism that allows language models to generate their own curriculum beyond the ceiling of human-annotated data. Naive self-play fails for LLMs because optimizing for task difficulty alone produces arbitrarily complex, useless problems. SGS solves this with a three-role loop: a **conjecturer** generates new problems prompted by existing unsolved ones; a **solver** attempts them; a **guide** scores generated problems for relevance and quality. The conjecturer trains on a dual reward — solver failure (difficulty) and guide score (quality) — keeping self-play grounded in meaningful problem space.

The underlying motivation is the **F-H problem**: AI trained only on human-generated data (H) cannot discover solutions in the full solution space (F) that require non-human strategies. Self-play is how AlphaZero surpassed AlphaGo — escaping the constraint of human chess and Go games.

## How I Think About It

The three-role split is the key insight. Pure self-play degenerates because the model becomes its own adversary without any notion of what makes a problem valuable. The guide is the stabilizer — a critic that keeps the conjecture loop honest by enforcing that difficulty alone isn't enough.

The analogy I find useful: a student who writes their own homework problems. Without guidance they write questions they find interesting (often too easy or too bizarre). Add a teacher-critic scoring for pedagogical value, and the student learns to generate problems that actually build skill. The guide is that teacher, running in the same loop.

This is a curriculum generation mechanism: SGS produces an ever-expanding, self-maintaining problem set grounded in existing high-quality examples.

## AI Integration

- **Curriculum generation**: SGS enables language models to train past the human data ceiling by synthesizing their own training examples. This is one of the most concrete paths to AI systems that exceed human-expert-level performance in narrow domains where formal verification of answers is possible.
- **NPC quest generation**: The conjecturer/solver/guide architecture maps directly onto generative quest systems. Conjecturer generates novel quest scenarios from existing templates; solver "plays" the quest (models what the player would do); guide scores for coherence with player history and world state. Replaces hand-authored templates with a self-maintaining quest curriculum.
- **Agent design pattern**: The three-role split (generate, execute, evaluate) is a general pattern for any agentic loop that needs to produce quality artifacts without human labeling. The guide is the grounding layer that prevents output drift.
- **Formal domains as training ground**: SGS works best where solution correctness can be verified automatically (math proofs in Lean, game win/loss). The more formally specifiable the success criterion, the more effective SGS becomes — pointing toward a class of AI capabilities that grows without human annotation.

## Related Concepts

- [world-models](world-models.md) — the F-H problem is a world-model problem: models trained on human data have a world model shaped by human perception
- [agentic-workflow](agentic-workflow.md) — SGS is a specific agentic loop pattern
- [verified-intelligence](verified-intelligence.md) — formal domains where SGS works best are the same ones where verified intelligence is possible
- [loop-engineering](loop-engineering.md) — SGS is a loop; the guide is the verification layer Osmani's framework identifies as critical

## Open Questions

- Does the guide need to be a separate model, or can it be the same model in a different role?
- What domains outside of math are formally verifiable enough for SGS to work without human annotation?
- How does the quality of the initial "seed" problem set affect SGS? Does it lock in a particular problem style?
- Can SGS generate diverse enough problems or does it converge on a narrow mode around the seed set?
