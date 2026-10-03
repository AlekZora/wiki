---
type: concept
title: Task-Specialized SLM Networks
aliases: [agentic SLM composition, DAG-trained SLMs, specialized small models, SLM fine-tuning for games]
tags: [ai, llm, slm, fine-tuning, game-design, agents, procedural, grounding]
sources: [dynamic-game-content-slm-defamelm]
updated: 2026-06-08
---

## Definition

A pattern for deploying AI generation in constrained environments: decompose a complex generative task into narrow, well-defined subtasks; fine-tune a small language model (SLM) on each subtask using synthetically generated training data structured as a directed acyclic graph (DAG); compose the resulting models into an agentic network where each node handles a single subtask. Contrasts with using a single large general model: trades generality for reliability, inference cost, and deployability.

The key technique is **DAG-based synthetic data generation**: a teacher LLM generates training data by traversing a graph where choice nodes draw from predefined game-world lists (factions, character names, current quests) and generation nodes produce open-ended text. This creates training data that is simultaneously structurally varied and bounded to the game world's actual state space.

## How I Think About It

The grounding problem has two solutions: you can enforce constraints *at inference time* (external validator, PDDL planner, RAG) or you can bake constraints *into the model weights* at training time. SLM fine-tuning is the latter. A model trained only on examples from within a game world's state space never learned to generate content outside it — so it doesn't, not because it's blocked, but because it doesn't know how.

The trade-off is sharp: the model is frozen at training-data-time. If the game world changes in ways not represented in the DAG, the model produces stale or inconsistent outputs. This makes it appropriate for games with finite, well-defined state spaces (bounded RPGs, structured narrative loops) and inappropriate for open-world games with unbounded or rapidly evolving state.

**Task complexity → scope requirement**: the paper establishes that complexity (number of jointly-satisfied dimensions) and required specialization are correlated — harder tasks need narrower scope and more specialized training. This is a useful design heuristic: if a generation task requires simultaneously satisfying more than ~3 correlated dimensions, it probably needs its own dedicated SLM rather than being folded into a shared model.

**Two deployment contexts**:
- *Game-loop-anchored*: generation is tied to a fixed, explicit game situation (a specific loop, a specific character state) — single SLM is sufficient
- *Open-ended*: generation must handle arbitrary narrative contexts — requires a DAG of coordinated SLMs, each scoped to a subtask

**The 8-bit sweet spot**: quantization to 8-bit preserves quality indistinguishable from full precision (p=0.41) while halving memory footprint and improving generation speed vs. 16-bit. 4-bit introduces new failure modes on hard prompts. For game deployment targeting consumer hardware (≤8GB VRAM), 8-bit is the practical target.

## AI Integration

- This is one of two architectural solutions to [Hallucinated Agency](hallucinated-agency.md): the SLM approach solves grounding by constraining the training distribution; the [Neuro-Symbolic Agent Architecture](neuro-symbolic-agent-architecture.md) solves it by external PDDL verification. Both work; they suit different game state complexities
- The DAG-based data generation methodology is directly applicable to quest generation: decompose quest structure into choice nodes (NPC relationships, player history, available items, active factions) and generation nodes (quest framing, dialogue, reward description); a teacher LLM generates 1,000–2,000 synthetic quests; fine-tune a small model on those; deploy locally
- The retry-until-success pattern (stochastic generation + LLM-as-judge filter) is a quality-assurance layer that works without modifying the generation model — it separates the generation problem from the quality problem, making both independently improvable
- The creativity-consistency trade-off is a design parameter: structured training data produces consistent but repetitive outputs; less-structured data produces varied but less reliable outputs; DAG node design controls where on that spectrum a model lands
- The "creative role shifts from authoring individual pieces to designing the systems and constraints that generate them" — this is a shift in the game designer's job description that AI makes possible; the designer authors the DAG, not the content
- For the Side Quest AI project: a fine-tuned SLM trained on synthetic quest data derived from the game's actual entity/faction/relationship graph would run locally, stay in-world by construction, and fit within a 2–3 second generation budget masked by NPC approach animations

## Related Concepts

- [Hallucinated Agency](hallucinated-agency.md) — SLM fine-tuning solves the grounding problem from the training side; the model doesn't know how to hallucinate outside its training distribution
- [Neuro-Symbolic Agent Architecture](neuro-symbolic-agent-architecture.md) — the complementary inference-time approach to grounding; PDDL validation vs. trained constraint absorption; suited to different world-state complexities
- [Emergent Narrative](emergent-narrative.md) — SLM networks generate content for individual narrative nodes; they are a production mechanism for emergent narrative systems, not the system itself
- [World Models](world-models.md) — SLM fine-tuning bakes a partial world model into weights; DAG choice nodes are the explicit state representation that grounds the model
- [Agent Memory](agent-memory.md) — DAG choice nodes at runtime query current game state; this is the memory interface that keeps SLM outputs grounded in the present world state

## Open Questions

- At what world-state complexity does the SLM approach break down relative to the neuro-symbolic approach? Is there a principled threshold?
- Can the DAG structure be auto-generated from a game's entity schema rather than hand-authored per task? This would be the SLM equivalent of LOOP's PDDL auto-induction
- What's the minimum training corpus size for adequate quality? DefameLM used 1,440 examples — does a quest generator with a larger state space need proportionally more?
- Can a single SLM be fine-tuned on multiple game-loop-anchored tasks without quality degradation on each, or does task mixing always hurt?
- Local quality assessment at runtime (replacing cloud LLM-as-judge) is the unsolved deployment problem — what's the minimum judge model that works on consumer hardware?

## Project Connections

- [Side Quest AI — Gap Report](../projects/game/gap-report.md): the SLM approach directly addresses the "tech stack" and "consistency" gaps; a fine-tuned quest-generator SLM trained on DAG-synthetic data resolves both simultaneously
- [Side Quest AI — Experience Goal](../projects/game/experience-goal.md): "disorienting recognition" requires the generated quest to reference the player's *specific* history — this constrains the DAG design: player history facts must be choice nodes at generation time
