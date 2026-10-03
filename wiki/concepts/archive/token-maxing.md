---
type: concept
title: Token Maxing
aliases: [tokenmaxxing, token maximalism, compute abundance mindset]
tags: [ai, llm, agents, productivity, strategy]
sources:
  - ../sources/tokenmaxxing.md
  - ../sources/garry-tan-claude-.md
updated: 2026-05-12
---

## Definition

Token maxing is the deliberate, aggressive use of LLM compute to achieve a level of thoroughness and quality that a human, constrained by time and effort, would never attempt. Instead of minimizing API calls, the practitioner treats token spend as a crucial investment — analogous to paying high rent in a tech hub for network effects and serendipity.

## How I Think About It

The key insight is a mindset flip: tokens are not a cost to minimize but a resource to deploy. A human researcher might read 3 sources before writing a summary; a token-maxing agent "boils the ocean" by ingesting and cross-referencing dozens. A human developer writes minimal tests; a token-maxing agent generates 80-90% coverage automatically.

This only works when compute cost is low relative to human time cost. Right now that ratio is extremely favorable — a few dollars of API calls can replace hours of manual work. The strategy bets that this ratio will keep improving.

The risk is waste without judgment. Token maxing without taste produces voluminous mediocrity. The human still provides direction, quality criteria, and the decision about *what* is worth boiling the ocean for.

## Related Concepts

- [Agentic Coding](agentic-coding.md) — the development context where token maxing is most directly applied
- [Software Factory](software-factory.md) — the factory model benefits from token maxing on test generation
- [Agent Skills](agent-skills.md) — skills direct where tokens are spent most effectively

## Open Questions

- At what point does token maxing hit diminishing returns — is there a quality ceiling per task type?
- How do you measure the ROI of additional token spend on a given task?
- Does token maxing change which tasks are worth automating in the first place?

## Project Connection

Token maxing could power the sci-fi series' daily episode generation. Instead of generating a single draft, the system could generate multiple narrative branches, cross-reference them against character memory and hidden agendas, and select the most dramatically coherent one — using compute abundance to achieve narrative quality a single pass couldn't.
