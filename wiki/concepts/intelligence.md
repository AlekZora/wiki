---
type: concept
title: Intelligence
aliases: []
tags: [ai, philosophy]
sources: [deepmind-ceo-interview.md]
updated: 2026-04-30
---

## Definition

There is no settled definition — Hassabis's point on 60 Minutes is that something is "obviously not quite right" about current definitions when you look at what AI systems can and can't do. At minimum, intelligence involves reasoning, planning, long-term memory, and the ability to generalize. What current AI systems demonstrate is impressive but still falls short of what most people mean intuitively by the word. Hassabis comes at the question from both neuroscience (his PhD) and game theory (game design, competitive games), which gives him an unusually cross-disciplinary lens.

## How I Think About It

The gap between "passes the test" and "is actually intelligent" is what makes this hard. A system can win at Go, translate between 100 languages, and write coherent essays without necessarily reasoning in the way a person does — it might be doing something else that produces the same output. Intelligence as a concept may need to be decomposed: reasoning, memory, planning, generalization, and metacognition might each be separable capabilities that current systems have in uneven, "jagged" distributions.

## Related Concepts

- [artificial-general-intelligence](./artificial-general-intelligence.md)
- [ai-agents](./ai-agents.md)

## Open Questions

- Is there a definition of intelligence that doesn't implicitly assume human-style cognition?
- Can a system be intelligent without any form of self-model or metacognition?
- Is consciousness a prerequisite for general intelligence, or orthogonal to it?
- How does Hassabis's neuroscience background shape his definition — what does the hippocampus / memory-consolidation literature say about what intelligence requires?

## Game Design Vector

**Mechanic:** The player encounters an AI with a jagged capability distribution — excelling at some tasks, failing surprisingly on others. The player must map the profile: which capabilities are genuine, which are performance without understanding, and where the gaps are. The gap between "passes the test" and "is actually intelligent" is the game's epistemological terrain. Each session is an attempt to design a test that reveals which dimension of intelligence (reasoning, memory, planning, generalization, metacognition) is being measured — and the AI's response is the result.

**2D Expression:** In 2D, the AI's jagged capability profile is readable as a spatial map: the plane is divided into zones where the AI operates reliably and zones where it fails unpredictably. The player discovers the map by moving through it — safe zones and failure zones are not labeled, they emerge from the AI's behavior in response to the player's position and action. The 2D surface is the capability landscape; the player is the cartographer.

**Addictive Loop:** The player is finding the AI's failure edges — the positions and tasks where impressive performance collapses into out-of-distribution brittleness. Each session presses further into uncertain territory. The compulsive loop is: probe → discover failure mode → update capability map → probe the next edge. The AI's jaggedness is the terrain generator; the map is never complete.

**Novel Angle:** Intelligence as a multi-dimensional capability space, not a single score. The player maps separate dimensions (reasoning, memory, planning, generalization) across sessions, discovering that improvement in one dimension can leave others unchanged. The challenge is that the player cannot know in advance which dimension any given test measures — the dimensionality of the capability space is itself something the player must discover.

## AI Integration Vector

**Player-AI Relationship:** The player is an evaluator; the AI is an agent with a jagged capability profile that neither party can fully see. The relationship is defined by the gap between what the AI appears to be able to do and what it actually can do. The player's task is to collapse that gap through test design. The AI's cooperation or non-cooperation with the evaluation is itself data — metacognition, the ability to model one's own capabilities, is one of the dimensions being mapped.

**AI as Evolving System:** The AI's development is visible as a changing capability map — some dimensions growing, others flat or degrading. Development is not uniform improvement but uneven change across the capability distribution. A session that extends planning range may produce new failure modes in generalization. The jagged profile is the development record; its shape at any point in time is the AI's current state.

**AI as Development Environment:** The player's test designs are the development environment. By presenting tasks that probe specific capability dimensions, the player shapes which dimensions the AI encounters challenges in. The development environment is the player's evolving theory of what the AI can and cannot do, expressed as a sequence of tests.

**Persistence:** The AI carries its jagged capability profile across sessions — the distribution of genuine capabilities and performance-without-understanding is stable in a way that event memories are not. What persists is the shape of the profile, not any particular test result. The player's accumulated map persists as their updated model of the AI's capability distribution.
