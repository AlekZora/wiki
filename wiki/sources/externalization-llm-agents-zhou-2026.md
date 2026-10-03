---
type: article
title: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"
url: https://arxiv.org/abs/2604.08224
author: Chenyu Zhou, Huacan Chai, Wenteng Chen, et al. (Shanghai Jiao Tong University, Sun Yat-Sen University, CMU, OPPO)
published: 2026-04-09
ingested: 2026-04-14
tags: [ai, llm, agents, memory, tool, architecture, survey]
concepts:
  - ../concepts/cognitive-externalization.md
  - ../concepts/harness-engineering.md
  - ../concepts/agent-skills.md
  - ../concepts/agent-memory.md
  - ../concepts/multi-agent-orchestration.md
---

## Summary

A 44-page systems-level survey that argues **externalization** — the progressive relocation of cognitive burdens from model weights into persistent external structures — is the unifying transition logic behind all major advances in LLM agent design. The paper organizes this into four components: Memory (externalizes state across time), Skills (externalizes procedural expertise), Protocols (externalizes interaction structure), and the Harness (the runtime environment that unifies the other three). The central claim is that reliability gains in practical agent systems come not from larger models but from restructuring the task so that internal capabilities and external infrastructure jointly cover the full range of competencies required.

## Key Points

- **The cognitive artifact parallel**: the paper opens with Donald Norman's insight that artifacts don't amplify unchanged internal ability — they transform the task itself. A shopping list doesn't expand biological memory; it converts a hard recall problem into an easy recognition problem. The same logic applies to LLM agent infrastructure.
- **Three capability layers** (historical progression, 2022–2026):
  1. **Weights** — capability lives in model parameters (pretraining, fine-tuning, RLHF, scaling laws). Reliable for one-shot tasks; brittle for multi-step work where state accumulates.
  2. **Context** — capability moves into the prompt (few-shot, CoT, RAG, ReAct). More flexible but still session-scoped and context-budget-limited.
  3. **Harness** — capability lives in the surrounding infrastructure (persistent memory, skill libraries, protocol layers, orchestration logic). The current frontier.
- **Three dimensions of externalization**:
  - *Memory externalizes state*: converts recall (regenerate from weights) into recognition (retrieve from persistent store). Addresses the continuity problem across sessions.
  - *Skills externalize procedural expertise*: packages procedures, best practices, and operating guidance into reusable artifacts. Converts improvised generation into composition from pre-validated components.
  - *Protocols externalize interaction structure*: replaces ad-hoc prompt-level coordination with explicit machine-readable contracts for tool discovery, invocation, delegation, and permission management. Converts ambiguous communication into interoperable, governable exchange.
- **The harness** is not a fourth externalization type — it's the runtime layer that hosts the other three. It provides orchestration logic, constraints, observability, feedback loops, and control points that make externalized cognition cohere in practice.
- **Three recurrent LLM mismatches** that each externalization dimension addresses:
  1. Finite context window + weak session memory → *memory* externalization
  2. Multi-step procedures rederived rather than executed consistently → *skill* externalization
  3. Brittle tool/agent interactions with free-form prompting → *protocol* externalization
- **The parametric vs. externalized tradeoff**: parametric knowledge (weights) is fast, compact, generalizable — but hard to update selectively, compose modularly, or govern. Externalized knowledge is inspectable, updatable, and composable — but introduces infrastructure complexity and latency. The frontier question is not "bigger model or better infrastructure?" but "which burdens should live where?"
- **Emerging directions**: self-evolving harnesses (infrastructure that adapts to agent behavior), shared agent infrastructure (from private scaffolding to public utility), embodied externalization (physical world as cognitive environment), and measuring externalization as a systems metric.

## Quotes

> "The power of the cognitive artifact comes from its function as a representation… Cognitive artifacts do not change human capabilities. They change the task." — Donald A. Norman (epigraph)

> "The question is increasingly not only 'how capable is the model?' but also 'what burdens have been externalized so the model no longer has to solve them internally every time?'"

> "Recall becomes recognition, improvised generation becomes composition, and ad hoc coordination becomes structured contract."

## My Take

This is the clearest framing I've seen for why practical agent systems have been improving faster than base model capability alone would predict. The externalization lens unifies a lot of things that previously looked like separate engineering concerns (RAG, tool calling, MCP, skill libraries) into a single coherent design principle. The cognitive artifact parallel with Norman is not just decorative — it's doing real work: it explains *why* externalization helps (representational transformation, not amplification) rather than just describing that it does. The harness-as-environment framing (§6) is particularly useful: the harness is to an LLM agent what a scaffold is to a construction worker — it doesn't make the worker more capable in some abstract sense, it restructures the work so the worker's existing capabilities reliably cover the task.
