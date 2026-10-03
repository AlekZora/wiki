---
type: concept
title: Context Development Life Cycle (CDLC)
aliases: [CDLC, context lifecycle, context as code]
tags: [ai, agents, context, agentic-coding, software-development]
sources: [context-is-the-new-code.md]
updated: 2026-05-04
---

## Definition

The Context Development Life Cycle (CDLC) is a framework for managing context — prompts, instructions, agent.md files, skills, and workflows — as the primary artifact of AI-native software development. Proposed by Patrick (Tessel) at the AI Engineer conference. Analogous to the Software Development Life Cycle (SDLC) and DevOps infinity loop, but centered on context rather than code.

The loop: **Generate → Test → Distribute → Observe → Adapt**

- **Generate**: write prompts, reusable instructions (agent.md, skill files), and bring in external context. Voice coding often produces richer context than typing.
- **Test**: validate context at multiple levels:
  - *Linting* — validate format, length, completeness
  - *Grammarly-checking* — ask AI "do you understand this?" to detect ambiguity and gaps
  - *Evals* — probabilistic test suites with error budgets (not binary pass/fail; assign acceptable failure rates per test group)
- **Distribute**: check context into version control for zero-friction sharing; package reusable context like libraries that teams or projects can install
- **Observe**: monitor agents in production — trace what context is loaded, sandbox agents to detect unexpected behavior and security risks (agents load all context files by default)
- **Adapt**: when production failures occur, generate new test cases from them and update context

## How I Think About It

The key insight is that when AI writes the code, the human's artifact is context. The skill set shifts from "write good code" to "write good context." This is a discipline — context can be linted, tested, versioned, packaged, and distributed just like code. The CDLC makes that explicit.

Error budgets for evals are a useful escape hatch: you can't test context exactly (it influences probabilistic outputs), so you define how much failure is tolerable for each test class and optimize within that.

## Related Concepts

- [agentic-coding](agentic-coding.md)
- [vibe-coding](vibe-coding.md)
- [software-3-0](software-3-0.md)
- [software-factory](software-factory.md)

## Open Questions

- What is the right granularity for context packages — per feature, per agent role, per domain?
- How do you version context when the "language" (model behavior) changes with each model update?
- Is there a universal format emerging (agent.md, CLAUDE.md, etc.) or will this fragment by tool?

## Project Connection

For the paranoid sci-fi series: character bibles, world rules, hidden agendas, and episode constraints are all context packages consumed by agents. The CDLC applies directly — write character context, test it (can the agent maintain the character's hidden agenda?), distribute per-agent packages, observe episode coherence, adapt when characters drift. Error budgets are especially useful: an agent can occasionally break character slightly without invalidating the episode, but core secret reveals must never leak prematurely.
