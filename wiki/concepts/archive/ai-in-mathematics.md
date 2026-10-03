---
type: concept
title: AI in Mathematics
aliases: [AI math, autoformalization, AlphaEvolve]
tags: [ai, mathematics, ml]
sources: [sources/ai-revolution-math-kakaes.md, sources/ml-in-physics-education.md]
updated: 2026-04-19
---

## Definition

The use of AI systems — especially large language models and evolutionary algorithms — to assist, accelerate, or autonomously generate mathematical research: finding conjectures, suggesting proof strategies, verifying formal proofs, and discovering new mathematical structures.

## How I Think About It

There are at least three distinct modes AI operates in for math:

1. **Reference/literature mode** — LLMs as a better semantic search engine than Google Scholar, surfacing forgotten proofs and connections.
2. **Conversation partner mode** — LLMs as a sparring partner for proof ideas. They hallucinate a lot, but the partial results and wrong turns can be useful. Tolerance for error required.
3. **Autonomous discovery mode** — Systems like AlphaEvolve (Gemini + genetic algorithms) that evolve programs searching for mathematical objects with desired properties. This is where serendipitous discovery happens — finding structures no one was looking for.

The most surprising 2025–26 development: **serendipitous discovery**. AlphaEvolve found hypercube structure in Bruhat intervals that had been sitting in front of mathematicians for 50 years. It wasn't prompted to find it. This is qualitatively different from "LLM helps with proof steps."

Terence Tao's mountain/jumping robot metaphor is good: AI can parkour up 6-foot walls that humans would have to laboriously plan routes around. But it can't plan the expedition to Everest. The walls may grow, but the strategic gap seems real for now.

**Autoformalization** — converting natural-language proofs to machine-verifiable formal logic — is the key enabling technology for using AI safely in mathematics. Without verification, LLM math is unreliable. With it, the error-prone parts can be checked.

## Related Concepts

- [machine-learning-in-science](machine-learning-in-science.md)
- [multi-agent-orchestration](multi-agent-orchestration.md) — AgentRxiv applies collaborative agent research to mathematics

## Open Questions

- Is there a point at which AI discovers mathematics that humans *can't* verify, even in principle? (Could be practically unreachable but theoretically interesting)
- Does the "serendipitous discovery" mode transfer to other fields — biology, chemistry, physics?
- What happens to mathematical culture when the tools accelerate result production but slow down the formation of new mathematicians?
