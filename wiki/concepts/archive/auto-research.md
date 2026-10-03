---
type: concept
title: Auto Research
aliases: [autoResearch, auto-research, closed-loop ML research]
tags: [ai, ml, agents, tool]
sources: [karpathy-no-priors-code-agents.md]
updated: 2026-04-30
---

## Definition

Auto research is the practice of delegating the ML experimentation loop entirely to an autonomous agent. You give the agent an objective metric, a sandbox environment, and no human in the loop — then let it run overnight finding improvements through repeated trial and measurement. The researcher's role shifts from doing experiments to setting up the conditions under which experiments run themselves.

## How I Think About It

The core shift is from "I run experiments" to "I design systems that run experiments." Token throughput becomes the bottleneck, not researcher time. If verification is cheap (train a small model, measure a metric), then compute is the scarce resource — not human attention. A distributed version extends this further: untrusted machines on the open internet can contribute experiments as long as results can be independently verified, similar to SETI@home or folding@home. Each verified experiment commit is like a block in a blockchain — cheap to check, valuable in aggregate.

Karpathy reports this actually worked: a closed-loop agent found weight decay and Adam beta tunings he had missed after two decades of manual tuning.

## Related Concepts

- [agentic-workflow](agentic-workflow.md)
- [speciation-of-models](speciation-of-models.md)

## Open Questions

- How do you prevent the agent from overfitting to the objective metric (Goodhart's Law at the experiment level)?
- What's the minimum viable sandbox setup to make auto research safe to run overnight without supervision?
- How much of the blockchain-like distributed compute model is theoretical vs. something anyone has actually shipped?
- Does auto research work as well for non-numerical objectives (e.g., improving response quality on open-ended tasks)?
