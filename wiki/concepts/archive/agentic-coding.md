---
type: concept
title: Agentic Coding
aliases: [vibe coding, agent-driven development, coding agents]
tags: [ai, llm, autonomous-agents, tool]
sources:
  - ../sources/karpathy-skill-issue-code-agents.md
  - ../sources/autoresearch-macos.md
  - ../sources/tokenmaxxing.md
  - ../sources/garry-tan-claude-.md
updated: 2026-05-12
---

## Definition

Agentic coding is the practice of directing AI coding agents to write, modify, and reason about code rather than writing it yourself. The human's role shifts from implementer to manager: specifying intent, reviewing agent output, parallelizing tasks across multiple agents, and iterating on the instructions (agents.md, CLAUDE.md, etc.) rather than the code directly.

## How I Think About It

The shift Karpathy describes isn't just "autocomplete got better." It's a flip in the ratio: from writing 80% of code yourself to writing 0% yourself. The new bottleneck is token throughput — how many agent-hours you can direct per day. This makes the human the binding constraint, not compute, which is both empowering (skill issue, not hardware issue) and stressful (idle tokens = wasted capacity, like idle GPUs).

The "macro actions" framing is useful: instead of "write this function," the unit of work is "implement this feature in repo A while agent B handles this other non-interfering feature." Managing multiple parallel agents who each run for 20 minutes is a different cognitive skill from pair-programming with an autocomplete.

"Claws" (persistent background agents like Open Claw) extend this further: agents that loop independently without you in the session, with their own memory, operating on your behalf even when you're not watching. The Dobby home automation example is the clearest demo of what this feels like in practice — you interact via WhatsApp, and the agent manages multiple underlying systems.

**Garry Tan's 400x claim** (May 2026): Tan reports a 100x–400x productivity increase measured in logical lines of code, after returning to hands-on development after a 13-year hiatus. His workflow: human acts as director/CEO, queuing high-level tasks for AI agents. Uses ASCII art diagrams as pre-computation (forcing the model to plan before coding), multi-model teams (Claude for creative iteration, Codex for deep logical work), and automated QA via Playwright browser control. Key benchmark: rebuilt his startup Posterous (originally 1.5 years, $4M, team) in 5 days for ~$200 in API costs.

The GStack framework formalizes this into a repeatable process: Office Hours (Socratic product refinement) → planning → Design Shotgun (generative UI brainstorming) → implementation → Adversarial Review (red-teaming the plan) → automated QA. The critical insight is that 80-90% of the time should go into the Office Hours / planning phase, not coding.

## Related Concepts

- [Auto Research](auto-research.md) — applying the same agentic loop to ML experimentation
- [LLM Jaggedness](llm-jaggedness.md) — the capability gaps that still make agentic coding frustrating
- [Token Maxing](token-maxing.md) — the compute abundance mindset that enables aggressive agent use
- [Metaprompting](metaprompting.md) — using LLMs to refine prompts before execution
- [Harness Engineering](harness-engineering.md) — the "thin harness, fat skills" architecture
- [Agent Skills](agent-skills.md) — the "fat" in thin harness, fat skills

## Open Questions

- What does "mastery" of managing coding agents look like at 2-3 years? What skills does it require?
- How do you review agent output efficiently when it's thousands of lines per session?
- At what granularity do agents break down — what kinds of tasks still require direct human implementation?
- How do "claws" (persistent agents) handle security and trust for access to email, calendar, files?
