---
type: concept
title: Experiential Memory
aliases: [procedural memory, trajectory-based learning, skill accumulation, self-reflective learning]
tags: [ai, memory, agents, evolution, self-improvement, persistence, behavior, player-ai, building]
sources:
  - ../sources/2512.13564v2.md
updated: 2026-05-24
---

## Definition

Experiential memory is the functional layer of an agent's memory that accumulates **procedural knowledge** from past trajectories — not facts about the world, but learned patterns of action, strategy, and skill distilled from what has happened before. Where factual memory answers "what is true?", experiential memory answers "what works?".

Two primary sub-types:
- **Skill-based**: libraries of reusable executable procedures. *Voyager* (Minecraft) builds a growing code-skill library through exploration — each skill is a retrievable program that solved a past task. New tasks are tackled by composing existing skills before generating novel ones.
- **Reflection-based**: textual self-assessments generated after failure. *Reflexion* stores action trajectories alongside LLM-generated critiques of what went wrong. These reflections enter a long-term buffer that the agent reads before attempting similar tasks — preventing repeated errors without parameter updates.

The defining feature: the agent's behavior at time T+1 is meaningfully altered by specific *events* that happened at time T, not just by aggregate training.

## How I Think About It

Experiential memory is the mechanism that makes an AI feel like it *has a history*. Factual memory lets it recall what you said; experiential memory lets it adjust what it does because of what happened between you. The difference is the gap between a database and a mind that has been through something.

The Voyager implementation is striking: the skill library is the game artifact. Playing Minecraft produces a growing library of programs. The more you play, the richer the library, the more capable the agent. The player is not just progressing through content — they are *developing an AI in real time*. The skill library is the record of the agent's education, and it is created through play.

Reflexion is the failure-learning case: the agent *writes a note to its future self* after each mistake. That note changes behavior on the next attempt. This is the minimal viable form of an AI that learns from experience — no weight updates, just a growing file of self-addressed warnings.

Both mechanisms are already architecturally feasible in small games. Neither requires training infrastructure — they run on top of existing LLMs.

## Related Concepts

- [[agent-memory]] — parent concept; experiential memory is one of the three functional layers
- [[memory-forgetting]] — what happens when skill libraries or reflection buffers are pruned
- [[agentic-workflow]] — the trajectory structures that generate the raw material for experiential memory
- [[emergent-narrative]] — player + AI with experiential memory generates narrative the designer did not author

## Open Questions

- When skill libraries grow large, retrieval becomes expensive. What is the right pruning strategy — recency, success rate, novelty? And who decides: the agent, the player, the game? Touches Q2.
- Reflexion's failure-learning requires the agent to *notice* it has failed. What happens in a game where failure is ambiguous or gradual — can an agent learn from slow decline? Touches Q3, Q5.
- If a player can read the skill library or the reflection buffer, they have direct insight into the AI's experiential history. What is the design of that interface — and does making it visible change how the player relates to the AI? Touches Q4, Q5.
- What does it mean for an AI companion's skill library to degrade — skills becoming stale, strategies forgetting context? Could designed decay make loss emotionally meaningful? Touches Q8.
- Touches Q3 (AI evolving through play via real trajectory-learning, not scripted), Q5 (interiority — the AI responds differently because of its specific history), Q4 (player-AI relationship: player educates the AI through play), Q8 (loss: if skills degrade, what the player built is at risk).

## Game Design Vector

**Mechanic:** The AI companion accumulates a skill library through events in the game. Skills are explicit, nameable, and visible to the player (e.g., "learned to distract guards after session 3"). The player can see the library grow. Some skills expire or decay without reinforcement — the player decides, implicitly, what the AI retains by choosing what to practice.

**2D Expression:** The skill library renders as a 2D inventory space — each learned skill occupies a tile, with visual markers for recency and access frequency. The 2D plane makes the library's structure legible at a glance: dense clusters indicate areas the player has explored; sparse edges indicate capabilities the AI almost developed but didn't. The player navigates both the game world and the AI's competence map simultaneously.

**Addictive Loop:** Session → events generate raw trajectories → AI distills new skills or self-reflections → skill library reshapes AI behavior in the next session → player encounters an AI that is visibly different because of what they did together. Return is motivated by wanting to see what the AI has *become* since last time.

**Novel Angle:** No shipped game makes the skill library the game artifact — something the player can see, tend, and partially lose. The closest is Voyager's library, but it is invisible infrastructure. A 2D game where the player navigates the AI's accumulated experience — and can watch it reorganize in response to new events — has not been made.

## AI Integration Vector

**Player-AI Relationship:** Education. The player's actions are the AI's curriculum. Over time, the AI's behavior reflects the player's specific choices, not just aggregate training. This is a building relationship — not building an AI from scratch, but shaping what it becomes through shared experience.

**AI as Evolving System:** Experiential memory is the concrete mechanism. Each play session produces trajectory data; the AI distills it into skills or reflections; behavior changes without parameter updates. This is genuine evolution through play, not just difficulty scaling or scripted progression.

**AI as Development Environment:** If the skill library is visible, the player watches the AI develop in real time. They can observe which events triggered which skills. When the AI applies a skill learned two sessions ago to a new context, that generalization is observable. The game becomes a site where AI learning is witnessed as it happens.

**Persistence:** The skill library and reflection buffer *are* persistence. Between sessions, the AI carries forward a structured record of what it learned. If sessions are deleted, those skills are lost. If the player returns after a long absence, the AI's library is exactly as they left it — a snapshot of a shared history. Forgetting can be designed: skills that are not accessed decay; reflection buffers have a maximum depth.
