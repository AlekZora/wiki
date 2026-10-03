---
type: concept
title: Metaprompting
aliases: [prompt generation, prompt refinement, recursive prompting]
tags: [ai, llm, prompt-engineering, agents]
sources:
  - ../sources/tokenmaxxing.md
  - ../sources/garry-tan-claude-.md
updated: 2026-05-12
---

## Definition

Metaprompting is the technique of using an LLM to generate, refine, or transform a prompt for another task. Rather than writing the final instruction directly, you write a higher-order instruction that produces the instruction. This creates a two-stage pipeline: the meta-level shapes the problem framing, and the object-level executes within that frame.

## How I Think About It

Garry Tan's "CEO skill" is the clearest example: you feed a basic feature plan into a prompt that asks the model to reimagine it as a "10-star experience" (Brian Chesky's concept). The output isn't code — it's a more ambitious, more detailed plan that then gets handed to the implementation agent. The meta-step amplifies ambition and completeness before any code is written.

This is essentially prompt-level chain of thought. Instead of asking the model to think step-by-step *within* a task, you ask it to think step-by-step *about the task itself* before starting. The GStack "Office Hours" skill is another form: a Socratic dialogue that refines a vague idea into a structured spec before any implementation begins.

The power is in separation of concerns: one model (or prompt) optimizes for creativity and ambition, another for disciplined execution.

## Related Concepts

- [Agent Skills](agent-skills.md) — metaprompting often lives inside skill definitions
- [Harness Engineering](harness-engineering.md) — the harness orchestrates the meta→object pipeline
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — metaprompting is a lightweight form of multi-agent collaboration

## Open Questions

- How many meta-levels deep is useful before you get diminishing returns?
- Can metaprompting be automated — an agent that learns when to invoke a meta-step?
- Does metaprompting reduce or increase the risk of hallucination?

## Project Connection

Metaprompting could be used in the sci-fi series to generate episode premises. A meta-level prompt takes the current state of all character agendas and generates "what would be the most dramatically interesting thing to happen next" — then a second prompt executes that premise into actual scene content.
