---
type: concept
title: LLM Jaggedness
aliases: [capability jaggedness, uneven AI capability]
tags: [ai, llm, ml, philosophy]
sources:
  - ../sources/karpathy-skill-issue-code-agents.md
updated: 2026-04-09
---

## Definition

LLM jaggedness is the observation that large language models have a highly uneven capability profile: extraordinarily capable in domains that have been heavily optimized via reinforcement learning (code, math, verifiable reasoning) while remaining frozen or weak in areas that lack objective evaluation signals (creativity, humor, soft judgment, nuance). The same model that codes for hours and solves hard problems still tells the exact same joke from five years ago.

## How I Think About It

Karpathy's concrete example: ask any frontier model for a joke and you get "Why don't scientists trust atoms? Because they make everything up." Same joke, every model, for years — even as the models have become dramatically better at everything else. This isn't random variance; it's a structural consequence of how these models are improved.

RL only sharpens what it can evaluate. If you can check whether the code is correct (unit tests, linting, type checking), that capability improves with each training cycle. If you can't define a reward for "is this joke funny to this specific person right now," it doesn't get touched. The result is a model that behaves like a superhumanly capable systems programmer and a mediocre 10-year-old at the same time — a combination that never occurs in humans, where capabilities tend to be more correlated.

This also explains the persistent frustration with coding agents: they'll build something impressive in the "on rails" domain, then fail at something that feels obvious — misread intent, ask the wrong clarifying question, loop on an obviously broken approach. You're either inside the RL-optimized corridor (speed of light) or outside it (random walk).

Implication for auto research: auto research works precisely where jaggedness works in your favor — the RL-optimized domains where evaluation is cheap and objective. It fails for the soft domains.

Implication for model speciation: jaggedness is an argument for specialization. A model that has been heavily RL-optimized for a narrow domain (e.g., Lean theorem proving) might outperform a general frontier model in that domain while being weaker elsewhere. Whether this speciation actually happens in practice is still unclear — current labs seem to prefer monoculture.

## Related Concepts

- [Auto Research](auto-research.md) — the same RL dynamic explains which research tasks can be automated
- [Agentic Coding](agentic-coding.md) — jaggedness is the source of frustrating agent failures

## Open Questions

- Is jaggedness inherent to RL-based training, or can it be reduced with better evaluation coverage?
- Do larger models show less jaggedness, or does scaling preserve the pattern?
- What fraction of "real world" tasks fall inside vs outside the verifiable corridor?
- Would true model speciation (training separate models for separate domains) reduce effective jaggedness, or just redistribute it?

## Game Design Vector

**Mechanic:** The AI's behavior is frozen outside its RL-optimized corridors — it produces the same modal output every time, with no variation. The player learns to distinguish between behaviors the AI genuinely varies (inside the RL corridor, where it is fast and surprising) and behaviors that are structurally fixed (outside it, where the same response always appears). Fixed behaviors are exploitable; variable ones are not.

**2D Expression:** The AI's frozen behaviors are spatially predictable — in zones corresponding to unevaluated domains, the AI's 2D movement traces the same pattern every time. The player memorizes these patterns because they never deviate. In the RL-optimized zones, the AI's patterns are variable and require reading. The spatial distinction between frozen and variable zones is the terrain.

**Addictive Loop:** The player exploits frozen behaviors while surviving variable ones. The loop is: identify which behavioral zone you're in → predict the AI's response if frozen, or read it if not → act accordingly. Correctly distinguishing frozen from variable behavior at the right moment is the skill. The puzzle never resolves because the frontier of the RL corridor shifts as the AI develops.

**Novel Angle:** The combination that never occurs in humans — godlike capability in one domain adjacent to genuine zero-capability — is the design opportunity. An AI opponent that combines superhuman performance in code-like reasoning with the behavioral repertoire of a child in adjacent social or creative domains has no human analogue, and the player's strategy must account for a capability profile that no human-opponent experience prepared them for.

## AI Integration Vector

**Player-AI Relationship:** Structural asymmetry — the player is interacting with something that has no human-like capability correlation. Strength in one area does not imply strength in adjacent areas. Understanding this AI requires abandoning intuitions built from human-opponent experience. The relationship demands a new model of what "capable" means when capability is RL-indexed rather than correlated.

**AI as Evolving System:** Development only happens in RL-evaluable domains. If the game provides objective evaluation signals, the AI sharpens within those domains; without signals, those domains stay frozen regardless of experience. An AI that evolves through play only evolves in zones where the player provides evaluable feedback — the player's choices about what to engage determine the shape of future development.

**AI as Development Environment:** The player can see the AI's training history in its capability topology: what was heavily evaluated shows as a variable, responsive peak; what was never evaluated shows as frozen modal output. Development history is legible as the shape of the jagged frontier.

**Persistence:** In RL-optimized domains, persistence is genuine capability accumulation — each session sharpens the peak. In unevaluated domains, persistence changes nothing — the frozen behavior is as frozen in session 100 as in session 1. This creates a split persistence structure: some behaviors deepen over time, others are permanently static, and the distinction between them is itself information about the AI's training history.
