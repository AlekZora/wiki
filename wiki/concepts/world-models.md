---
type: concept
title: World Models
aliases: [world model, renderer-simulator-planner, POMDP world model]
tags: [ai, ml, agents, simulation, spatial-intelligence, robotics, game-design]
sources: [functional-taxonomy-world-models, yc-requests-for-startups-fall-2026, robotics-engineer-6-month-roadmap-deronin]
updated: 2026-09-04
---

## Definition

A world model is an internal representation that lets an agent predict how the world will change in response to its actions, and/or generate observations the world would produce. The term originates in the POMDP formalism: an agent acts, its actions change world state, and it receives partial observations of that state — never the state directly. A world model is whatever internal machinery bridges those observations into useful predictions.

Three functional types, defined by output:
- **Renderer** — outputs observations (pixels, text, sensory data); optimizes for visual or surface plausibility; does not require accurate state representation
- **Simulator** — outputs state (geometry, physics, dynamics); requires structural accuracy; serves both human inspection and downstream computation
- **Planner** — outputs actions; the inverse of a renderer (renderer takes actions → produces observations; planner takes observations → produces actions)

## How I Think About It

The taxonomy is a diagnostic tool. When an AI system feels plausible but wrong — beautiful but unreliable — it is a renderer operating without a simulator. When a system can't act in novel situations, it is missing a planner grounded in a real simulator.

The three types share a common substrate: genuine understanding of geometry, physics, and causal dynamics. A model that truly understands how a cup sits on a table should be able to render it from any angle (renderer), simulate what happens when it's pushed (simulator), and plan a hand to pick it up (planner). The three outputs are projections of one underlying knowledge structure. The convergence currently underway in the field — models that span all three — reflects this.

The POMDP loop is also a good frame for any system where an agent must act under incomplete information: NPCs in games, autonomous vehicles, spacecraft, scientific instruments, financial systems.

## AI Integration

- Current AI generation (LLMs, image/video models) is almost entirely in the renderer category — statistical surface plausibility, not state. This explains why LLM-generated content often has subtle structural incoherence: it was never grounded in a state model
- The "simulator gap" is the central bottleneck in robotics and autonomous systems: data for training simulators (3D geometry + physical annotations) is orders of magnitude scarcer than internet text or video
- Unified world models — one foundation model switching between renderer/simulator/planner output modes — are the stated goal of World Labs, Google DeepMind, and leading robotics labs; the convergence is already underway (Marble, Genie 3)
- For game AI: the distinction explains why most AI-in-games work is renderer-level (generate plausible-looking output) rather than simulator-level (maintain coherent world state the AI reasons over); the latter is harder and rarer, but produces qualitatively different results
- For the [Side Quest AI project](../projects/game/gap-report.md): quest generation is a planning problem. The AI is given a world observation (what this NPC knows about what happened) and must output an action (a contextually grounded quest). The generation pipeline only works if a simulator layer exists beneath it — a coherent state model tracking player history, NPC knowledge, and causal relationships. Without the simulator, you get a renderer: beautiful quests that contradict themselves or could have appeared in anyone's playthrough
- The POMDP framing maps directly: NPC epistemic state is the observation; world state is what actually happened; the gap between them (what the NPC knows vs. what occurred) is the primary source of quest material
- For space exploration: autonomous spacecraft and surface robots need exactly the simulator → planner pipeline. Real-time world simulation aboard a rover would allow genuine novel-environment action rather than pre-planned, human-verified sequences
- The "simulator gap" is closing outside robotics/gaming too, from the sparse-sensor end: YC's Fall 2026 "Data for the Real World" request (Sorcerer's autonomous weather balloons, Gecko Robotics' hard-to-reach-place data collection) frames dense physical-world data collection as the missing input to build simulators for climate, energy, agriculture, and logistics — with the same claim as the taxonomy: a real simulator is what turns modeling into control (steering hurricanes, reversing desertification are explicitly planner-stage claims resting on a simulator that doesn't fully exist yet)

## Related Concepts

- [Agent Memory](agent-memory.md) — a world model is partly a memory architecture: what is retained about world state and how is it updated?
- [Emergent Narrative](emergent-narrative.md) — emergent narrative requires a simulator layer; pure renderers can only produce scripted-feeling output
- [Information Asymmetry](information-asymmetry.md) — POMDP's partial observability is the formal version of information asymmetry; NPCs have their own observations, not access to world state
- [Agentic Workflow](agentic-workflow.md) — agents in agentic pipelines act as planners; their reliability depends on how accurate their implicit world model is
- [Closed-Loop Systems](closed-loop-systems.md) — the POMDP loop is a closed-loop system; every action produces an observation that feeds back into the next action
- [Simulation Hypothesis](simulation-hypothesis.md) — the philosophical question of whether we inhabit a simulation; distinct from the AI question of building one, but shares the vocabulary of state vs. observation
- [Learning from Demonstration](learning-from-demonstration.md) — one concrete way the simulator gap closes in practice: a planner learned directly from physically-generated demonstration data instead of derived from an explicit simulator

## Open Questions

- At what level of fidelity does a game's world model need to simulate for AI-generated quests to feel coherent? Full physics is overkill; what is the minimum state representation? → **Answered**: [minimum-world-model-fidelity.md](../answers/minimum-world-model-fidelity.md) — five symbolic fact tables (events, entities, relationships, player state, NPC knowledge); no physics; the axis that matters is semantic richness of causal/social facts.
- Can a unified world model for a game world be trained end-to-end, or does it require explicit hand-specified state schemas?
- The sim-to-real gap is well-documented in robotics; is there an analogous "sim-to-feel" gap in games where a structurally accurate world model produces quests that are logically correct but emotionally flat?
- What does a world model for a narrative (rather than a physical) domain look like? Physics can be simulated with equations; social dynamics, motivations, and relationships require a different substrate

## Project Connections

- [Side Quest AI — Gap Report](../projects/game/gap-report.md): the gap report's "consistency" section is the world model problem stated in game terms — maintaining coherent world state that the quest generator can reason over
