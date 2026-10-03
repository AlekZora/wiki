---
type: article
title: "AI Orchestration Papers 2025 — Curated Research Set"
url: 
author: curated
published: 2025-01-01
ingested: 2026-04-11
tags: [ai, llm, multi-agent, orchestration, gossip, memory, pkb, emergent, protocols]
concepts:
  - ../concepts/multi-agent-orchestration.md
  - ../concepts/gossip-protocols-agents.md
  - ../concepts/agent-memory.md
  - ../concepts/auto-research.md
  - ../concepts/information-networks.md
---

## Summary

A curated set of 18 architecture-heavy papers and preprints (2024–2026) covering the emerging design space of LLM-based multi-agent systems. The collection spans four clusters: (1) hierarchical and protocol-based orchestration frameworks (AgentOrchestra, MCP/A2A standards, IoA, Agora); (2) decentralized and gossip-style coordination (AgentNet, two gossip papers, emergent coordination via theory-of-mind prompting); (3) agent memory, self-improvement, and autonomous research loops (A-Mem, AgentRxiv, iterative optimization, automated paper writing); and (4) propagation dynamics and PKB systems. Together they map the design space from centralized conductor–worker stacks all the way to orchestrator-free evolutionary swarms.

## Key Points

- **Hierarchical orchestration** (AgentOrchestra, arXiv:2506.12508): conductor decomposes tasks → sub-goals → specialized tool-using agents; outperforms flat baselines on real-world benchmarks.
- **MCP + A2A as the emerging standard** (arXiv:2601.13671): Model Context Protocol standardizes tool/context access; Agent-to-Agent protocol handles negotiation and peer delegation — together they form a production-ready backplane.
- **Internet of Agents** (arXiv:2407.07061): treats agents as internet nodes with IM-style routing; protocol-agnostic dynamic teaming across heterogeneous models.
- **Agora communication trilemma** (arXiv:2410.11905): versatility vs. efficiency vs. portability solved by tri-modal policy — fixed routines for common cases, NL for rare cases, LLM-written routines for the middle.
- **AgentNet** (arXiv:2504.00587): fully decentralized, no central orchestrator; evolutionary role refinement over time; NeurIPS 2025 accepted.
- **Gossip as substrate** (arXiv:2512.03285): gossip protocols sit *beneath* MCP/A2A to handle discovery, load signaling, and fault detection without central planners.
- **Theory-of-mind prompting** (arXiv:2510.05174): persistent personas + "consider what others might do" induces measurable emergent coordination purely at the prompt level.
- **A-Mem** (arXiv:2502.12110): agents autonomously generate structured memory notes, trigger link generation, and evolve existing memories — no handcrafted operations needed.
- **AgentRxiv** (arXiv:2503.18102): shared intermediate results across agent "labs" yields 13.7% relative gain on MATH-500 vs isolated labs.
- **Iterative orchestration optimization** (arXiv:2412.17149): specialized agents autonomously search and tune orchestration graph configurations.
- **Flooding vulnerability** (arXiv:2407.07791): manipulated "world knowledge" silently propagates through agent communities via RAG without prompt injection — trust layers are non-optional.
- **ODI** (arXiv:2503.13754): Orchestrated Distributed Intelligence frames multi-loop feedback + cognitive density as the key to turning passive record-keeping into active agent fabrics.

## Quotes

> "Gossip protocols provide diffuse global awareness in large agent swarms that cannot rely solely on central planners." — arXiv:2512.03285

> "Attackers can inject counterfactual knowledge into LLM-based agent communities, which then silently spreads through agent communication and RAG frameworks without explicit prompt injection." — arXiv:2407.07791

> "The Agent Communication Trilemma: versatility, efficiency, and portability — agents use standardized routines for common interactions, natural language for rare communications, and LLM-written routines for intermediate cases." — Agora (arXiv:2410.11905)

## My Take

The field is converging on a two-layer model: a formal orchestration layer (MCP/A2A, hierarchical conductors) sitting on top of an informal propagation layer (gossip, epidemic diffusion). The interesting tension is between centralized planners (AgentOrchestra, MCP) that are auditable and controllable, and decentralized systems (AgentNet, gossip) that are resilient but hard to debug and potentially vulnerable to knowledge poisoning (the flooding paper is a direct warning). The PKB angle (A-Mem, Karpathy-style systems) closes the loop: agents need persistent, self-evolving memory to accumulate skill across sessions, not just within them. The emergent coordination paper is practically useful right now — persona + ToM prompts is something you can test today without any infrastructure.

---

### Paper Index

| Paper                                             | arXiv                     | Date       |
| ------------------------------------------------- | ------------------------- | ---------- |
| AgentOrchestra                                    | 2506.12508                | 2025-06-13 |
| Orchestration Architectures, Protocols, Standards | 2601.13671                | ~2026-01   |
| Internet of Agents (IoA)                          | 2407.07061                | 2024-07-10 |
| Agora (Scalable Communication Protocol)           | 2410.11905                | 2024-10-14 |
| Beyond Black-Box Benchmarking                     | 2503.06745                | 2025-03-09 |
| Multi-Agent Collaboration Survey                  | 2501.06322                | 2025-01-10 |
| AgentNet (Decentralized Evolutionary)             | 2504.00587                | 2025-04-01 |
| Gossip-Enhanced Communication Substrate           | 2512.03285                | 2025-12-01 |
| Revisiting Gossip Protocols (Habiba & Khan)       | 2508.01531                | 2025       |
| Emergent Coordination in MALM                     | 2510.05174                | 2025       |
| A-Mem: Agentic Memory                             | 2502.12110                | 2025-02    |
| AgentRxiv                                         | 2503.18102                | 2025-03-23 |
| Multi-AI Iterative Optimization                   | 2412.17149                | 2024-12-22 |
| Automated AI Research Paper Writing               | 2604.05018                | 2026-04-05 |
| AIOpsLab                                          | 2501.06706                | 2025-01-11 |
| AI Orchestration for Ultrasonic Simulation        | Nature/Scientific Reports | 2025-04-10 |
| News Diffusion Multi-Agent Simulation             | 2410.13909                | 2024-10-16 |
| Rumor Spreading LLM Agents                        | 2502.01450                | 2025-02-03 |
| Flooding Spread of Manipulated Knowledge          | 2407.07791                | 2024-07-22 |
| Karpathy PKB blog                                 | franksworld.com           | 2026-04-05 |
| Orchestrated Distributed Intelligence (ODI)       | 2503.13754                | 2025-03-18 |
