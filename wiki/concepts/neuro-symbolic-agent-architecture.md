---
type: concept
title: Neuro-Symbolic Agent Architecture
aliases: [neuro-symbolic hybrid, constrained agent architecture, LLM + planner, grounded agent pipeline]
tags: [ai, agents, llm, game-design, architecture, grounding, planning, pddl]
sources: [npc-grounding-architecture-perplexity, llm-reasoner-automated-planner-npc, loop-neuro-symbolic-planning]
updated: 2026-06-08
---

## Definition

An agent architecture that separates language generation (neural, LLM) from world-state verification (symbolic, formal planner) so that the LLM proposes actions but never executes them directly — every action is validated against a formal model of what is actually true in the environment before it takes effect. The LLM handles intent, language, and reasoning under uncertainty; the symbolic planner handles constraint enforcement over the real state of the world.

In its three-module form as implemented by Puerta-Merino & Sabater-Mir (arxiv:2501.10106, the foundational implementation):

1. **Reasoner** — maintains a memory stream of world perceptions in natural language; holds personality traits; uses the LLM to select among possible goals ("what to do")
2. **Planner** — maintains a live PDDL AP Problem (objects, predicates, goal); calls a classical solver (Fast Downward) to generate valid action sequences given the selected goal ("how to do it")
3. **Interface** — receives world state updates each iteration; generates the possible-goals list; updates both Reasoner and Planner; executes the top validated action

In LOOP's extended form (arxiv:2508.13371), this becomes a four-module system adding:

4. **Learning & Memory** — causal memory that learns from execution traces; cross-task pattern transfer; confidence-based routing between hierarchical and neural-guided planning paths

## How I Think About It

The key insight is the **division of labor by what each component is reliable at**. LLMs are powerful at language, intent modeling, and reasoning over ambiguous situations — but unreliable at respecting hard constraints about world state. Symbolic planners are brittle at language and flexible reasoning — but they enforce constraints absolutely. Combining them gives you both.

The critical design rule: **the LLM never touches the world directly**. It speaks in goals; the planner speaks in facts. Only the planner's verified output reaches the environment. This is the "grounding lock" that prevents hallucinated agency.

The remaining bottleneck (mid-2026) is the formal world model itself. PDDL domain files must either be hand-authored per game — prohibitively expensive at scale — or auto-induced. Two approaches to auto-induction are active:

- **LOOP** (arxiv:2508.13371): generates PDDL specs iteratively, refines via symbolic feedback from execution failures, builds a self-correcting causal knowledge base from `CausalTriple(action, relation, state)` objects extracted from execution traces. Achieves **85.8% success** on IPC benchmarks vs LLM+P at 55.0% and Tree-of-Thoughts at 3.3%. The critical advance over prior work: bidirectional learning — the LLM learns from the planner's failures, not just the planner verifying the LLM's proposals.
- **PSALM-V** (arxiv:2506.20097): induces symbolic action semantics (pre/post-conditions) from visual input in visual environments — NPC explores the world and builds the world model rather than receiving it

The **small-LM alternative** avoids the formal planner entirely: train a small model on synthetic DAG-based game-world data so constraint adherence is baked into the model weights. Trades generality for reliability and inference cost — potentially the first path that ships commercially.

## AI Integration

- This architecture is the direct solution to [Hallucinated Agency](hallucinated-agency.md): by interposing the symbolic planner as a grounding lock between the LLM and the world, the model can't act on invented content that contradicts actual game state
- The architecture generalizes beyond games: any AI agent acting in a constrained domain (robotics, task automation, scientific instruments) needs the same separation between LLM intent and formal constraint verification
- The auto-induction problem (LOOP, PSALM-V) is itself solved using LLMs — the LLM generates candidate PDDL specs, execution feedback corrects them; the architecture is self-bootstrapping given enough interaction traces
- The small-LM alternative (synthetic DAG training) is an instance of the general pattern of encoding world-structure into model weights via training rather than injecting it at inference time; it's cheaper to run but less generalizable across world changes
- The visual grounding extension (arxiv:2604.19192) converts unstructured environmental observations (panoramic images) into structured scene graphs that the LLM can reference precisely — this is the RAG pattern applied to spatial context rather than episodic memory
- Current commercial infrastructure (Inworld AI + Nvidia ACE) handles dialogue safety but not world-state consistency; the research architecture described here addresses the latter gap; no commercial product has shipped the full stack at game-product quality as of mid-2026

## Related Concepts

- [Hallucinated Agency](hallucinated-agency.md) — this architecture is the solution; the grounding lock prevents the failure mode
- [World Models](world-models.md) — the formal world model in layer 2 is a symbolic world model; the PDDL domain is the simulator layer beneath the LLM renderer
- [Agent Memory](agent-memory.md) — layer 3 (episodic memory via RAG) is the memory architecture that makes cross-session NPC consistency possible
- [Agentic Workflow](agentic-workflow.md) — general agent loop; this is a specific instantiation with a formal verification layer between intent and execution
- [Emergent Narrative](emergent-narrative.md) — a fully grounded NPC stack would enable genuine emergent narrative: agent goals + constrained world = narratable consequences the designer didn't write

## Open Questions

- Can LOOP/PSALM-V's auto-induction of PDDL world models be made robust enough to replace hand-authored domain files at commercial scale? This is the unlock that makes the full stack deployable without bespoke engineering per game
- What is the performance cost of the symbolic planner at real-time game speeds? Can PDDL verification run per-dialogue-turn without perceptible latency?
- Does the four-layer separation generalize to open-world games where the world state is effectively unbounded? What's the minimum symbolic representation that catches consequential constraints without modeling everything?
- Is there a hybrid between the full neuro-symbolic pipeline and the small-LM approach — e.g., a small model for constraint checking, large model for intent generation?

## Project Connections

- [Side Quest AI — Gap Report](../projects/game/gap-report.md): the "consistency" gap is the absence of layer 2 (symbolic execution layer). The quest generator needs a grounding lock that validates quest content against actual game state before it reaches the player
- [Side Quest AI — Experience Goal](../projects/game/experience-goal.md): "disorienting recognition" requires that the system never makes promises the world can't keep — the grounding lock is what prevents the inverse
