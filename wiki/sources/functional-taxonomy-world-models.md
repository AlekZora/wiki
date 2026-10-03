---
type: article
title: "A Functional Taxonomy of World Models"
url: https://x.com/drfeifei/status/2062247238143996275
author: Fei-Fei Li (@drfeifei), World Labs team
published: 2026-06-03
ingested: 2026-06-04
tags: [ai, ml, world-models, spatial-intelligence, simulation, robotics, agents]
concepts: [world-models]
---

## Summary

Fei-Fei Li and the World Labs team argue that "world model" is one of the most overloaded terms in AI — computer vision, robotics, RL, and generative AI all claim to be building them while meaning different things. The essay provides a clarifying taxonomy grounded in the POMDP loop: an agent takes actions, those actions change world state, and the agent receives partial observations of that state. The three functions of a world model are defined by what each one outputs: a **renderer** outputs observations (pixels for human eyes, optimizing for visual fidelity); a **simulator** outputs state (geometry, physics, dynamics — structural accuracy over visual beauty); and a **planner** outputs actions (given observation and goal, what to do next). Of the three, simulation is the linchpin — it is the structural backbone from which both rendering and planning derive. The essay closes by arguing the boundaries are already collapsing: the same underlying knowledge of geometry, physics, and dynamics is required for all three, and the field is converging toward a unified world model that can switch output modalities on demand.

## Key Points

- The POMDP loop (agent → action → state → observation) is the technical origin of "world model"; the different things currently called world models are different projections of this same loop
- Kenneth Craik (1943) proposed minds reason by running "small-scale models" of reality — this is where the phrase comes from
- **Renderer**: outputs pixels; optimizes visual plausibility; commercially most mature; cannot be trusted for structural accuracy (buildings look right from above, fall apart on closer inspection)
- **Simulator**: outputs state (geometry + physics + dynamics); serves both human professionals (architects, filmmakers, game devs) and computer programs (RL agents, robot controllers); gets least public attention but is most consequential
- **Planner**: outputs actions; the inverse of a renderer (renderer: actions → observations; planner: observations → actions); most nascent — compelling demos exist but none validated at real-world complexity or duration
- Simulation is the bridge between renderer and planner; mastering only one of the other two leaves you unable to do the third
- World Labs' Marble: takes multimodal prompts, generates Gaussian splats (for visual exploration) + collision meshes (for physics engine) — one model straddling renderer and simulator
- Key convergence trend: renderers becoming action-conditioned, simulators becoming more controllable, planners gaining deliberation rather than just reaction
- Data bottleneck: internet video is abundant for renderers; 3D assets with geometric/physical annotations are orders of magnitude scarcer for simulators

## Quotes

> "Where language models learn the statistical structure of text, world models learn the statistical structure of space and time."

> "If language is an abstraction of the world and pixels are a projection of it, then geometry, physics, and dynamics are the world itself."

> "The logical endpoint is a unified world model: one foundation model that can render photorealistic views, produce physically accurate structure, and plan action sequences, switching between output modalities depending on what the downstream consumer needs."

## My Take

The renderer/simulator/planner taxonomy is immediately useful as a diagnostic tool. Most "AI in games" falls entirely in the renderer category — AI generates text, images, dialogue that *looks* right without modeling underlying state. The Side Quest AI project is attempting something closer to a simulator: it must maintain a model of world state (NPC knowledge graphs, player action history, causal relationships between events) before it can generate quests that feel real. That distinction explains why LLM-generated quests so often feel generic — they are renderers operating without a simulator beneath them. The generation pipeline works on surface statistics, not on state.

The POMDP framing maps cleanly onto game AI architecture. NPCs are agents with partial observations of world state. The quest system is a planner: given the current world observation (what this NPC knows) and a goal (what should emerge from this interaction), it outputs an action (the quest). The player-facing dialogue is the rendering layer. If you build only the renderer, you get pretty quests that contradict themselves. If you build the simulator first — a coherent world state model — the planner and renderer follow from it.

For the space exploration mission: autonomous spacecraft and Mars robots need exactly the simulator → planner pipeline Li describes. The reason rovers are so constrained (pre-planned, slow, human-verified) is the absence of a reliable real-time world simulator aboard. The unified world model she describes would allow a robot to act in genuinely novel environments — which is what space exploration actually requires.

The convergence of all three functions into one foundation model is the long bet. If it materializes, it will change what game AI can do more than any single technique: a unified world model for a game world would let the AI reason about physics, generate visuals, and plan NPC behavior from a single shared understanding rather than three disconnected systems.
