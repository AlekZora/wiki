---
type: concept
title: Software 3.0
aliases: [software 3.0, software 1.0 2.0 3.0]
tags: [ai, llm, philosophy, software-development]
sources: [karpathy-sequoia.md]
updated: 2026-04-30
---

## Definition

Karpathy's framing of three eras of software:

- **Software 1.0** — explicit, hand-coded rules; humans write instructions the CPU executes.
- **Software 2.0** — neural networks trained on data; humans define the objective and data, gradient descent writes the weights.
- **Software 3.0** — LLMs where programs are written in natural language; the context window is the source code, the LLM is the interpreter. English is the new programming language.

The canonical example Karpathy gives: Claude Code's install instructions are a prompt you paste to your agent. The documentation is written for an agent to execute, not a human to read.

## How I Think About It

Each era didn't replace the previous one — they stacked. 1.0 code still runs everything at the hardware level. 2.0 models (neural nets) are embedded inside 3.0 systems. What changed is where human intention enters the stack: at 1.0 you specify steps, at 2.0 you specify objectives and data, at 3.0 you describe what you want in plain language.

The practical implication is that "programming skill" is being redefined. Knowing Python matters less; knowing how to express intent precisely and evaluate outputs matters more.

## Related Concepts
- [vibe-coding](vibe-coding.md)
- [agentic-engineering](agentic-engineering.md)
- [llm-as-computer](llm-as-computer.md)

## Open Questions
- Is 3.0 a new paradigm or a layer on top of 2.0? (The LLM is itself a 2.0 artifact.)
- Does the natural-language interface actually lower the barrier for non-programmers, or does it just shift what skills are required?
- What does "debugging" look like in Software 3.0 — you can't step through a prompt the way you can step through code.
