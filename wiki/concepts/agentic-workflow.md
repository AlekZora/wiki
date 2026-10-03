---
type: concept
title: Agentic Workflow
aliases: [agentic workflows, agentic loop]
tags: [ai, llm, tool, agents]
sources: [karpathy-no-priors-code-agents.md, karpathy-sequoia.md, yc-build-company-with-ai.md, 5-papers-ycombinator.md]
updated: 2026-06-13
---

## Definition

An agentic workflow is a structure where autonomous AI agents handle extended tasks with minimal human-in-the-loop involvement. Rather than a human issuing one prompt and reviewing one response, the agent runs a loop — planning, executing, observing results, and iterating — until a goal is reached or a checkpoint triggers human review. Multiple agents can run in parallel on independent subtasks.

Key aspects from the sources:
- Token throughput (not GPU flops) becomes the primary resource bottleneck (Karpathy, No Priors).
- The shift Karpathy describes post-December 2024: he went from 80/20 human/agent to nearly 0/100 in code writing.
- YC frames it as intelligent closed loops: actions produce artifacts, artifacts feed back into the intelligence layer.
- The software factory model (YC) is a concrete instance: specs and tests define success, agents generate and iterate on implementation.

## How I Think About It

The key mental shift is from "prompt → response" to "goal → loop → outcome." The human's job becomes defining the goal, setting up the environment (tools, memory, success criteria), and reviewing the output — not steering every step.

Parallelism is the force multiplier: multiple agents running simultaneously compress calendar time, not just effort. Token throughput is the new compute budget.

The YC framing adds an organizational layer: if every process in a company is a closed loop with legible artifacts, the whole company becomes an agentic workflow, not just the engineering team.

**RTS metaphor (Luke Orthwine, YC 2026):** The best articulation of what the human role becomes is a Real-Time Strategy game commander. You "macro" — spawn agents onto tasks, manage token economy, monitor a minimap-style dashboard for outliers — rather than "micro" (steering individual moves). APM (Actions Per Minute) as a productivity metric is reframed: not keystrokes, but agent tool calls per minute. The key operational principle is satisficing: ship good-enough solutions at high throughput rather than perfect solutions at low throughput. A continuously updated, machine-readable knowledge base (agents update it as they work) is the shared context layer that prevents each spawned agent from starting blind.

## Related Concepts
- [agentic-engineering](agentic-engineering.md)
- [vibe-coding](vibe-coding.md)
- [llm-as-computer](llm-as-computer.md)

## Open Questions
- At what complexity level do agentic loops become unreliable without human checkpoints?
- How do you design good success criteria for open-ended tasks so agents know when to stop?
- What does debugging look like when the "program" is a multi-agent loop running overnight?
- How does token cost scale with parallelism — is there a practical ceiling for individuals vs. companies?

## Game Design Vector

**Mechanic:** The player specifies success criteria — what the AI's output must satisfy — and the AI runs its own loop to reach them: planning, executing, observing its own results, iterating. The player does not steer individual actions; they define the target and observe the iterations. The game's challenge is in the gap between what the player intended and what their specification actually produces.

**2D Expression:** The AI's loop is spatially legible in 2D — the player watches the agent plan a path, execute it, observe the result, and adjust on the next iteration. Each iteration is a traversal of the 2D world that the player can read and evaluate. The loop's progress is a visible movement pattern rather than a hidden background process.

**Addictive Loop:** The player's skill is in specification rather than execution. Better specs produce better agent behavior; ambiguous specs produce surprising failures. The compulsive loop is: specify → observe iterations → identify the failure mode in the spec → refine → observe again. Mastery is understanding how to encode intent precisely enough that the agent's loop converges on the right outcome.

**Novel Angle:** No shipped game has made the player a spec-writer rather than a controller — setting success criteria and watching an AI find solutions within them across multiple observed iterations. The player's control is indirect and upstream; the immediate game surface is watching the loop run.

## AI Integration Vector

**Player-AI Relationship:** Delegation with accountability — the player defines the goal and the environment (tools, memory, success criteria), and the AI executes autonomously. The player bears responsibility for the AI's behavior because they configured the conditions. The relationship is closer to management than to control.

**AI as Evolving System:** The agentic loop is the AI's development mechanism within a session: each iteration the AI observes its own results and adjusts. The AI evolves through repeated self-observation across a single run. Across sessions, changed success criteria produce changed development trajectories.

**AI as Development Environment:** The player watches the AI's iterations in real time — planning, executing, observing, adjusting. Each loop cycle is a visible development step. The gap between early iterations and later ones within a session is a miniature development arc that the player can read and evaluate.

**Persistence:** The YC framing: artifacts produced in each iteration feed back into the intelligence layer. What carries across sessions is the accumulated artifact trail — every prior loop execution contributing as input to subsequent runs. Persistence is the substrate that makes each new session start from where the last loop ended, not from scratch.
