---
type: concept
title: Agentic Engineering
aliases: [agentic engineering]
tags: [ai, llm, tool, software-development]
sources: [karpathy-sequoia.md]
updated: 2026-04-30
---

## Definition

Agentic engineering is the disciplined, production-grade approach to AI-assisted software development. As described by Karpathy at Sequoia, it involves writing specs and tests, setting up agent harnesses, and having AI do the implementation — while humans maintain quality standards through review and verification. It preserves the quality bar of professional software while dramatically accelerating delivery. Karpathy frames the 10x engineer multiplier as having exploded under this model.

## How I Think About It

Where [vibe coding](vibe-coding.md) raises the floor, agentic engineering preserves the ceiling. The human's job shifts from writing code to writing the constraints the code must satisfy — specs, tests, and review criteria. The agent handles implementation and iteration. It's closer to how a senior engineer directs junior developers, except the feedback loop is much faster.

The YC software factory model maps onto this: humans write specs and scenario-based tests; agents generate implementation and iterate until tests pass. Some companies reportedly already have repos with no handwritten code.

## Related Concepts
- [vibe-coding](vibe-coding.md)
- [agentic-workflow](agentic-workflow.md)
- [software-3-0](software-3-0.md)

## Open Questions
- At what scale does agentic engineering break down without human review?
- What does "spec writing" look like as a formal discipline — is there a best practice emerging?
- How much domain knowledge does a human need to write useful specs if they can't evaluate the implementation directly?
