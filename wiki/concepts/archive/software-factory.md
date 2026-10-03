---
type: concept
title: Software Factory
aliases: [AI software factory, spec-driven development]
tags: [ai, tool]
sources:
  - ../sources/yc-build-company-with-ai.md
  - ../sources/tokenmaxxing.md
  - ../sources/garry-tan-claude-.md
updated: 2026-05-12
---

## Definition

An AI-driven development model where humans write specs and scenario-based tests that define what success looks like, and agents generate and iterate on the implementation until those tests pass. Humans no longer write application code directly — they write the definition of done. Some companies now have repos with zero handwritten code: only specs and test harnesses. The YC talk describes this as an evolution of test-driven development (TDD), and frames it as enabling a 1000x–10000x engineer multiplier.

## How I Think About It

TDD already said "define success before writing code." The software factory just removes the human from the "write the code" step entirely. The human's job shifts from implementer to spec author and test designer. If your tests are good, you don't care who — or what — wrote the code that passes them. The leverage point becomes the quality of your test coverage and spec clarity, not your typing speed.

The failure mode is obvious: if your specs are vague or your tests don't capture the real success criteria, the agent generates something that passes but doesn't actually work. The discipline required is the same as always — just applied earlier in the process.

**Parallel workstreams** (Tan 2026): GStack supports multiple independent work trees, enabling a single developer to manage dozens of PRs across multiple projects simultaneously. This is the factory model taken literally — multiple assembly lines running in parallel, each producing a different feature. Tan's Posterous rebuild (originally 1.5 years / team → 5 days / solo) is the most concrete benchmark for the productivity claim.

## Related Concepts

- [ai-native-company](ai-native-company.md)
- [closed-loop-systems](closed-loop-systems.md)

## Open Questions

- How do you write scenario-based tests for behavior that is inherently hard to specify (edge cases, UX quality, emergent interactions)?
- Does the software factory model hold for greenfield only, or can it apply to large legacy codebases?
- What does the iteration loop look like when agents fail tests — is human intervention required or can the agent self-debug reliably?
