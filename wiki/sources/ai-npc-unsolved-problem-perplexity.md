---
type: article
title: "What kind of problem is AI currently facing in games?"
url: https://www.perplexity.ai/search/3b6615dc-2175-43c1-a8a4-00a7886c2903
author:
published: 2026-06-07
ingested: 2026-06-07
tags: [ai, game-design, agents, llm, narrative, npc, grounding]
concepts: [hallucinated-agency, world-models, emergent-narrative, agent-memory]
---
## Summary

A synthesis analysis of the deepest unsolved problem in game AI: the coherent, persistent, game-aware NPC — a character that can talk, reason, remember, and act within the actual constraints of the game world across an entire playthrough. The piece argues the failure isn't primarily technical but organizational and design-structural. Three interlocked sub-problems (grounding, memory, narrative coherence vs. player agency) are mostly solvable in isolation; what's missing is an agreed design framework and a party willing to own the problem end-to-end.

## Key Points

- The recurring failure mode is **hallucinated agency**: an LLM NPC invents lore, quests, and consequences that don't exist in the actual game world — not by intention but because the model has no live access to game state, only a training corpus it can imagine from
- The grounding problem (live, queryable game state) and memory problem (persistent player model across sessions) are technically mostly solved; the gap is the design question of *what the NPC should be allowed to do, promise, or change*
- A classic **accountability vacuum** between AI labs (no game engine expertise) and game studios (no AI safety expertise) prevents either side from shipping a complete solution — the co-development partnership required has never materialized at product scale
- Closest public attempts: Inworld AI and Nvidia ACE demos remain demos precisely because the grounding-and-consequence problem hasn't been solved at game-product quality
- The industry lacks a **design vocabulary** for AI-driven characters — no equivalent of "core loops," "feedback loops," or "juice" for reasoning about what happens when an LLM NPC fails; this makes it unclear whether to fix the prompt, context window, world model, safety filter, or player expectation

## Quotes

> "The model doesn't know the difference between 'what I can imagine' and 'what is real in this simulation.'"

> "It's not a research problem waiting for a breakthrough. It's a design discipline that hasn't been invented yet, sitting at the intersection of narrative design, AI engineering, and game systems — and no single studio or lab has the mandate or courage to define it from scratch."

## My Take

The "hallucinated agency" framing is the most precise diagnosis I've seen of why LLM NPCs fail specifically in games, as opposed to in general AI use. In a chatbot, hallucination is annoying. In a game NPC, it is *a character the player trusted lying to them* — which is qualitatively worse and harder to forgive.

The accountability vacuum maps directly onto the Side Quest AI project: the quest generator only works if there's a coherent world state model beneath it. Without the simulator layer, you get a renderer — beautiful quest text that could have appeared in anyone's playthrough, contradicting what actually happened. This source confirms that the consistency gap in the [gap report](../projects/game/gap-report.md) is the industry's central unsolved problem, not a project-specific edge case.

The "missing design vocabulary" observation is also under-appreciated. Game designers spent decades developing craft language for mechanical systems. AI-driven NPCs introduce failure modes that existing vocabulary doesn't capture — and until there's language for the failure modes, there's no systematic way to fix them. Building that vocabulary is itself a design contribution.

AI intersection: the problem is precisely the absence of a simulator layer beneath the LLM renderer. The industry has powerful renderers (LLMs that produce plausible NPC dialogue) but no game-aware simulator that grounds what the renderer can say. Solving this requires RAG or tool-call architectures that give the LLM live read access to game state — not a new model, but new architecture around existing models.
