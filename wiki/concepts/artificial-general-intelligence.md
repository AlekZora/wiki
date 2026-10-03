---
type: concept
title: Artificial General Intelligence
aliases: [AGI, general AI]
tags: [ai, ml, philosophy]
sources: [hassabis-yc.md, deepmind-ceo-interview.md, Situational Awareness (Leopold Aschenbrenner) (z-library.sk, 1lib.sk, z-lib.sk).md]
updated: 2026-05-20
---

## Definition

A system capable of general problem-solving across a wide range of domains — not optimized for any single task but able to reason, plan, and learn in the way a human expert could, broadly. Hassabis describes it as the most important and potentially most dangerous technology humanity has ever developed. His working timeline is roughly 2030, with current LLMs explicitly not qualifying as AGI.

Aschenbrenner argues for a more aggressive timeline — AGI as plausibly arriving by ~2027 — by extrapolating the qualitative leap from GPT-2 ("preschooler") to GPT-4 ("smart high-schooler"). His mechanism is OOM counting across three drivers: raw compute investment, algorithmic efficiency, and [[unhobbling]] (transforming a chatbot model into an agent via long context, test-time compute, and tool use). The two timelines disagree by ~3 years and on the structural source of the remaining gap — Hassabis points to missing architectural capabilities (continual learning, long-term reasoning, episodic memory); Aschenbrenner points to compounding scale and unhobbling, with capability gaps closing as a function of compute and engineering rather than requiring new ideas.

## How I Think About It

Think of it as the difference between a chess engine and a chess coach who can also help you with your taxes and your startup pitch. Current systems are deep specialists that can fake breadth. AGI is genuine breadth. The three things currently missing — continual learning (integrating new knowledge without forgetting), long-term reasoning (not looping, not self-contradicting mid-thought), and proper memory (episodic, not just a big context window) — are the diagnostic gaps Hassabis keeps coming back to. Until those are solved, what we have is "jagged intelligence," not general intelligence.

The Hassabis-Aschenbrenner disagreement is itself the most useful structure to hold. If Hassabis is right, AGI requires solving discrete architectural problems and the timeline is gated by research breakthroughs. If Aschenbrenner is right, AGI emerges from compounding scale and unhobbling, and the timeline is gated by industrial mobilization. Both could be partially right — the unhobbling agenda may close some Hassabis gaps while leaving others (continual learning) genuinely unsolved.

## Related Concepts

- [ai-agents](./ai-agents.md)
- [intelligence](./intelligence.md)
- [ai-safety](./ai-safety.md)
- [[technological-singularity]]
- [[unhobbling]]
- [[situational-awareness]]
- [[jagged-intelligence]]

## Open Questions

- Is the current pre-training + RLHF + chain-of-thought paradigm sufficient, or does AGI require fundamentally new ideas? Hassabis puts it at ~50/50; Aschenbrenner implicitly leans toward sufficient-with-unhobbling.
- What does "continual learning" look like architecturally — is it a neuroscience-inspired memory module, something else entirely?
- Does reaching AGI require solving consciousness, or can a system be general without being conscious?
- How will we know when we've crossed the threshold — is there a test sharper than "it surprises us"?
- Is the GPT-2 → GPT-4 leap actually a unit of measurement, or a one-off discontinuity that does not repeat? Touches Q3.

## Game Design Vector

**Mechanic:** The player encounters an AI and must determine whether it has crossed the AGI threshold — or design tests that expose which of the three gaps (continual learning, long-term reasoning, proper memory) remain open. The gap between "passes the test" and "is actually intelligent" is the game's epistemological terrain. Failure modes are the mechanics: the AI forgets what it already encountered (continual learning failure), self-contradicts mid-session (reasoning failure), or behaves as if the session is the first despite accumulated evidence (memory failure).

**2D Expression:** In 2D, the three gap types manifest as distinct failure signatures in the plane. Continual learning failure: the AI repeats a mistake it already made, the plane shows the same error pattern twice. Reasoning failure: the AI's path self-intersects — it undoes its own earlier work. Memory failure: the AI ignores accumulated evidence that has been building in the plane across sessions, treating the current moment as origin.

**Addictive Loop:** The player tests the AI against tasks that require the missing capabilities. Each test reveals which gap is the current bottleneck. Progress is closing the gaps. The compulsive loop is the diagnostic: which failure mode will emerge today? The ~2030 Hassabis timeline creates external pressure — the gaps are being closed outside the game; the player races to understand each one before it closes.

**Novel Angle:** The AGI evaluation problem as core mechanic: the player's task is not to build general intelligence but to distinguish it. Designing tests that separate genuine capability from performance-without-understanding has never been a shipped game's primary challenge. The ~50/50 uncertainty about whether the current paradigm (pre-training + RLHF + chain-of-thought) is sufficient is the game's unresolved background tension.

## AI Integration Vector

**Player-AI Relationship:** The player is an evaluator in the Hassabis sense: testing the AI against the three diagnostic gaps and determining where it still falls short. The relationship is diagnostic. The player is not building the AI so much as probing it — constructing tasks that reveal which capabilities are genuine and which are faked by pattern matching.

**AI as Evolving System:** The AI develops toward AGI through the session sequence: each session exposes gaps; the gaps narrow over time. The player observes development as a change in which failure modes occur — some gaps closing before others, in an order that is itself information. The development sequence is part of the game's content.

**AI as Development Environment:** The player's task designs are the development environment. By designing tasks that expose specific gaps, the player shapes what the AI encounters challenges in. The environment the player constructs determines which gaps get worked on — an indirect form of training through diagnostic design.

**Persistence:** Proper memory — episodic, not just a large context window — is the persistence question framed as an AGI gap. Until this gap closes, the AI's cross-session persistence is shallow: context, not genuine memory. The game's progression is toward real persistence: integrating new knowledge without forgetting, reasoning across the full arc of prior sessions, carrying actual experience rather than a context window.
