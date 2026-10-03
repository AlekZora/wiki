---
type: concept
title: Vibe Coding
aliases: [vibe coding]
tags: [ai, llm, tool, software-development]
sources: [karpathy-no-priors-code-agents.md, karpathy-sequoia.md]
updated: 2026-04-30
---

## Definition

Vibe coding is writing software by expressing intent to an AI agent rather than typing code directly. Coined by Andrej Karpathy, it describes the mode of development he shifted into around December 2024, when agentic coding tools reached a threshold where he stopped correcting them and started trusting them fully. Since then he writes almost zero code himself. His phrase: "code is not even the right verb anymore."

## How I Think About It

Think of it as raising the floor for everyone. Instead of writing a function, you describe what you want and review what comes back. The human role becomes directing and reviewing rather than implementing. It democratizes creation — people who couldn't write code before can now ship things — but that democratization comes with risks if the vibe coder doesn't understand what's being built.

It's distinct from [agentic engineering](agentic-engineering.md): vibe coding is informal and fast, agentic engineering is disciplined and production-grade. Conflating the two is how vulnerabilities get shipped.

## Related Concepts
- [agentic-engineering](agentic-engineering.md)
- [agentic-workflow](agentic-workflow.md)
- [software-3-0](software-3-0.md)
- [llm-as-computer](llm-as-computer.md)

## Open Questions
- Where exactly is the boundary between vibe coding and agentic engineering in practice?
- Does vibe coding require a human who understands code to review output, or can it work end-to-end for non-programmers?
- How does the quality gap between vibe-coded and hand-coded software evolve as models improve?
