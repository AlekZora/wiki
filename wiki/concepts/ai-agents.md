---
type: concept
title: AI Agents
aliases: [agents, LLM agents, agentic AI, autonomous agents]
tags: [ai, llm, tool]
sources: [karpathy-no-priors-code-agents.md, hassabis-yc.md, karpathy-sequoia.md, yc-build-company-with-ai.md]
updated: 2026-04-30
---

## Definition

LLM-powered systems that take actions, use tools, and operate autonomously over extended tasks — rather than producing a single response and stopping. An agent reads context, decides what to do, calls tools (file systems, APIs, browsers, terminals), observes results, and loops until the task is done. Hassabis sees agents as the necessary path toward AGI. Karpathy marks December 2024 as the inflection point when code agents became reliable enough that he stopped correcting them and started delegating entirely.

## How I Think About It

Agents are what happens when you give an LLM a loop and tools instead of just a prompt-and-response interface. The capability jump Karpathy describes in December 2024 isn't just a benchmark improvement — it's a qualitative shift in how you interact with the system. Before: you steer it constantly. After: you describe the goal and get out of the way. The "fire and forget" threshold is the key metric. Hassabis's caveat is that continual learning is the blocker for truly fire-and-forget agents — current agents still fail on tasks that require integrating new information mid-run without explicit re-prompting.

The YC framing adds an organizational dimension: agents aren't just developer tools, they're the operational layer of AI-native companies. The "software factory" model (humans write specs and tests, agents generate and iterate on implementation) is the enterprise version of what Karpathy is describing at the individual level.

## Related Concepts

- [artificial-general-intelligence](./artificial-general-intelligence.md)
- [intelligence](./intelligence.md)

## Open Questions

- What does "continual learning" inside an agent loop look like — is it persistent memory, fine-tuning mid-task, or something else?
- How do you reliably verify agent output when the task is long, multi-step, and the success criteria are fuzzy?
- At what point does agent autonomy create liability — who is responsible when a fire-and-forget agent does something wrong?
- Is there a principled architecture for multi-agent coordination, or are current multi-agent systems just prompt engineering stacked on top of each other?

## Game Design Vector

**Mechanic:** The player issues goals to an AI agent that loops autonomously — reading context, deciding, calling tools, observing results, and continuing until done. The player cannot steer mid-loop; they can only set the goal and wait. Success is "fire and forget": the agent completes the task without correction. Failure is re-entry: the player adjusts the goal and restarts the loop. The "fire and forget" threshold is the game's difficulty curve — as tasks grow more complex, the player must develop more precise goal-specification skill.

**2D Expression:** The agent's loop is spatially visible in 2D — each iteration traces a path through the game surface as the agent reads, decides, acts, and observes. The player watches the loop trace its own trajectory, unable to intervene without breaking it. The loop's path is the record of the agent's cognition made legible in the plane.

**Addictive Loop:** The compulsive question is: did I specify the goal correctly enough for the agent to succeed without correction? Each loop is a test of the player's specification skill. The December 2024 inflection — when agents became reliable enough to delegate to entirely — is the game's arc: the player begins micromanaging and earns the right to delegate. Continual learning failure (the agent forgetting mid-run information) is the recurring obstacle that forces re-entry.

**Novel Angle:** The game tracks the closing of the fire-and-forget threshold across sessions. In early sessions, the player steers constantly. As specification skill improves, delegation becomes possible. The continual learning gap — integrating new mid-loop information without re-prompting — is the persistent ceiling: it marks what the agent cannot yet do regardless of how well the player specifies the goal.

## AI Integration Vector

**Player-AI Relationship:** The player is a goal-specifier; the AI is an autonomous executor. The relationship is defined by the quality of the handoff: how precisely the player describes the goal determines how well the agent completes it. The player never directly controls the agent's decisions — only sets the initial condition and observes the outcome.

**AI as Evolving System:** The agent's loop — read context, decide, call tools, observe, repeat — generates its own history as it runs. Each iteration's output is the next iteration's context. The agent develops not through training but through the accumulation of its own observations across loop iterations. The player can read this accumulation as the loop trace.

**AI as Development Environment:** The agent's tool-call sequence is the development record — every decision and observation logged by the loop is a trace of the agent's cognition. The player can read the loop trace as a window into the agent's decision process without access to the agent's internal state.

**Persistence:** Continual learning — integrating new knowledge mid-run without re-prompting — is the agent's unsolved persistence problem. Without it, each new session begins with amnesia about what the previous loop encountered. Persistence is the frontier; its absence is the game's structural constraint.
