---
type: concept
title: Hallucinated Agency
aliases: [NPC grounding problem, game-world grounding, grounded game agent]
tags: [ai, llm, game-design, agents, grounding, npc, narrative]
sources: [ai-npc-unsolved-problem-perplexity]
updated: 2026-06-07
---

## Definition

The failure mode where an LLM-driven agent acts on invented content that contradicts the actual world it inhabits. Distinguished from ordinary hallucination (being factually wrong) by the *agentic* dimension: the agent doesn't just generate false text, it makes promises, issues quests, references items, or describes consequences that the environment cannot fulfill — causing the gap between imagination and reality to manifest as broken trust rather than mere inaccuracy.

In games, this means an NPC sends a player to a location that doesn't exist, promises a reward the engine can't give, or invents lore that contradicts the canonical world. The NPC becomes a liar not by design, but by architecture.

## How I Think About It

The root cause is always the same: the model is operating as a **renderer** (generating plausible-sounding output from a training corpus) without a **simulator** underneath it (live, queryable access to what is actually real in this world right now). The model's imagination fills the gap where world-state knowledge should be.

This is why "make the LLM smarter" doesn't fix it. A more capable renderer still doesn't know game state unless the architecture gives it that information via tool calls, RAG, or structured context injection. The failure is architectural, not capability-based.

Three interlocked sub-problems sit beneath it:
1. **Grounding** — the agent needs live read access to world state (what quests exist, what items are acquirable, what the player has done)
2. **Memory** — the agent needs a persistent model of this specific player across sessions, not just a context window
3. **Consequence scope** — even with grounding and memory, there's no agreed design answer for what the agent should be *allowed* to promise or change; this is a design question, not an AI one

The third sub-problem is why the issue remains unsolved: grounding is technically feasible (RAG + tool calls), memory is mostly solvable (vector stores), but the design vocabulary for *what the agent should be authorized to do* hasn't been invented yet.

## AI Integration

- Hallucinated agency is the game-specific instance of the renderer/simulator gap described in [World Models](world-models.md): LLMs are powerful renderers but have no simulator layer by default; adding one requires architecture, not a better model
- The fix is not a model capability improvement but a pipeline architecture: tool-call access to game state APIs + structured world context injected into every NPC prompt; this is already the pattern in agent frameworks (RAG, MCP, tool use)
- An accountability vacuum in the industry mirrors a structural pattern in AI deployment: AI labs own the model but not the deployment context; application builders own the context but not the model; grounded, game-aware NPCs require both parties to co-own a shared architecture that neither is incentivized to build alone
- The missing design vocabulary problem has a direct AI parallel: AI systems currently lack diagnostic craft language for agent failure modes the way mechanical game design has language for mechanical failures; building that vocabulary is itself a form of AI research (evaluation frameworks, failure taxonomies)
- For the [Side Quest AI project](../projects/game/gap-report.md): the gap report identifies "consistency" as the weakest area; hallucinated agency is the precise name for what consistency failure looks like from the player's perspective — a character that made promises the world couldn't keep

## Emerging Solution

The 2025–2026 research consensus is a four-layer **neuro-symbolic hybrid**: LLM intent generator → symbolic planner (PDDL/STRIPS) that validates every proposed action against the formal world model → episodic memory via RAG → behavior executor that calls game engine APIs. The critical principle: the LLM proposes, the planner verifies, only verified actions execute. This "grounding lock" structurally prevents hallucinated agency. Full details in [Neuro-Symbolic Agent Architecture](neuro-symbolic-agent-architecture.md).

## Related Concepts

- [Neuro-Symbolic Agent Architecture](neuro-symbolic-agent-architecture.md) — the four-layer solution; the grounding lock is the structural fix for this failure mode
- [World Models](world-models.md) — the renderer/simulator taxonomy explains hallucinated agency architecturally; grounding is the simulator layer that prevents it
- [Agent Memory](agent-memory.md) — persistent player model is the second sub-problem; memory is the substrate that makes cross-session consistency possible
- [Emergent Narrative](emergent-narrative.md) — emergent narrative requires the AI to reason coherently about consequences; hallucinated agency is what happens when it can't
- [AI Agent Personality Design](ai-agent-personality-design.md) — consistency is a core retention pillar; hallucinated agency destroys consistency at the world-grounding level
- [Agentic Workflow](agentic-workflow.md) — the tool-call and RAG patterns that exist in agentic pipelines are the architectural fix for hallucinated agency in games

## Open Questions

- What is the minimum world state representation needed to prevent hallucinated agency? Full game state is noisy; what's the minimal schema that grounds NPC dialogue without overwhelming context?
- Can a grounded NPC be given genuine consequence authority — the ability to actually change world state — without breaking game balance or narrative coherence?
- Is there a "hallucinated agency spectrum"? Minor lore inconsistency vs. impossible quest vs. promised-but-undeliverable consequence — do players treat these the same or differently?
- What does the design vocabulary for AI-driven NPC failures actually need to include? The article names the absence; what would fill it?

## Project Connections

- [Side Quest AI — Gap Report](../projects/game/gap-report.md): the "consistency" gap is hallucinated agency stated in engineering terms; solving it requires a world state layer the quest generator can query
- [Side Quest AI — Experience Goal](../projects/game/experience-goal.md): "disorienting recognition" (the world noticed *your* specific story) is the exact opposite of hallucinated agency — the failure mode to engineer against
