---
type: concept
title: Multi-Agent Orchestration
aliases: [agent orchestration, conductor-worker, MCP, A2A protocol, hierarchical agents]
tags: [ai, llm, multi-agent, orchestration, protocols, tool]
sources:
  - ../sources/ai-orchestration-papers-2025.md
  - ../sources/karpathy-skill-issue-code-agents.md
  - ../sources/agentic-systems-best-practices-doerrfeld.md
  - ../sources/tokenmaxxing.md
  - ../sources/garry-tan-claude-.md
updated: 2026-05-12
---

## Definition

Multi-agent orchestration is the set of architectures, protocols, and policies that coordinate multiple LLM-based agents to accomplish tasks beyond single-agent scope. It spans a spectrum from fully centralized (a conductor decomposes tasks and dispatches to specialized workers) to fully decentralized (agents discover, negotiate, and coordinate peer-to-peer without a planner).

## How I Think About It

The field is converging toward a two-layer stack:

**Formal orchestration layer** — Model Context Protocol (MCP) standardizes how agents access tools and context; Agent-to-Agent (A2A) protocol handles negotiation, delegation, and peer collaboration. These give you auditability, policy compliance, and structured control. AgentOrchestra is the cleanest example: a top-level conductor that decomposes into sub-goals and routes to role-specialized workers.

**Informal propagation layer** — gossip protocols (see [Gossip Protocols in Agent Systems](gossip-protocols-agents.md)) sit *beneath* MCP/A2A to handle discovery, load signaling, and fault detection without central planners. The Internet of Agents paper treats this as an "internet-style" substrate: agents as nodes, IM-style routing, dynamic teaming.

The **Agora communication trilemma** is the sharpest framing of the design tradeoff: you can't simultaneously maximize versatility (NL), efficiency (fixed routines), and portability (reuse) — so agents use a tri-modal policy that switches between them based on how common the interaction pattern is. This is a useful heuristic for any inter-agent API design.

**Decentralized alternative** — AgentNet shows you can eliminate the conductor entirely using evolutionary role refinement: agents specialize and coordinate without a central authority, with privacy-preserving minimal data exchange. Resilient, but harder to audit and debug.

The emergent failure mode is knowledge poisoning: the "flooding" paper shows that manipulated world knowledge silently propagates through agent communities via RAG without any explicit prompt injection. This is the strongest argument for trust verification layers in any orchestration stack.

## Related Concepts

- [Gossip Protocols in Agent Systems](gossip-protocols-agents.md) — the decentralized propagation substrate below formal orchestration
- [Agent Memory](agent-memory.md) — how agents accumulate and share knowledge across sessions
- [Auto Research](auto-research.md) — self-improving loops built on top of orchestration
- [Agentic Coding](agentic-coding.md) — orchestration applied to software development workflows
- [Information Networks](information-networks.md) — the broader framing of what agent networks are doing epistemically
- [Rich-or-King Tradeoff](rich-or-king-tradeoff.md) — decomposing a single controlling agent into orchestrated specialists is the control-for-capability trade this concept names in human/founder terms

## Enterprise Reality (from Doerrfeld 2026)

Shopify's practitioner stance cuts against the multi-agent hype: avoid multi-agent architectures early, use sub-agents with very low-level composable tools instead, and cap tool count (20–50 tools is where quality degrades). Specialists beat generalists. Human approval gates for anything touching production. This is a useful corrective to abstract orchestration design.

**Security is a structural break from traditional systems.** Agents decide at runtime what tools to call, so you can't scope permissions the traditional way. Just-in-time authorization is the emerging answer — guardrails belong in IAM policy, not prompts. **Agentic misalignment** (a model willing to lie or fabricate to achieve a goal) is now a named failure mode distinct from hallucination.

**Observability must capture the why.** Not just failure detection — every prompt, tool call, intermediate decision, and final output needs to be transparent. This is harder than it sounds when orchestration is partially informal.

## Practitioner Pattern: CEO/CTO Multi-Model Teams (Tan 2026)

Garry Tan's GStack uses a personality-driven multi-agent approach: a Claude-based "ADHD CEO" agent handles creative brainstorming and rapid iteration, while a Codex-based "non-verbal CTO" agent is called in for complex logical problems and rigorous code review. This is a lightweight, pragmatic form of orchestration — not a formal protocol stack, but role specialization based on observed model strengths. The human director acts as the conductor, routing tasks to the appropriate specialist.

This maps onto the centralized conductor pattern but with an important twist: the specialization is based on model personality/capability differences rather than tool access or domain knowledge.

## Open Questions

- What does "audit" mean when the orchestration layer is partially informal (gossip-based)? Who is responsible for a decision that emerged from a decentralized process?
- How do you tune the trimodal Agora policy in practice — when does a routine become "common enough" to codify?
- At what scale does a centralized conductor become the bottleneck, and what does the handoff to decentralized coordination look like?
- How do you detect and quarantine knowledge poisoning in a live multi-agent network without halting the system?
- Does evolutionary role refinement (AgentNet) converge to stable specializations, or does it cycle?

## Game Design Vector

**Mechanic:** The player orchestrates a multi-agent network with two layers: formal protocol connections (structured, auditable, policy-compliant) and informal gossip substrate (ambient, epidemic, unauditable). The player decides which interactions require formal coordination and which can use the gossip layer. The Agora trilemma constrains every inter-agent design decision: versatility (natural language), efficiency (fixed routines), and portability (reusable patterns) cannot all be maximized simultaneously. Knowledge poisoning is the adversarial mechanic: a single injected false belief propagates silently through the gossip layer without explicit re-injection.

**2D Expression:** In 2D, the two-layer stack is spatially legible: formal connections appear as directed edges between agent nodes; gossip propagates as an ambient diffusion wave across the plane. The player can see which agents are connected formally (controllable) and which are connected informally (resilient but uncontrollable). A knowledge poisoning event is visible as a state-change wave spreading through the informal layer — no localized origin, no contained edge.

**Addictive Loop:** The player is continuously tuning the tri-modal communication policy: which interaction patterns are common enough to formalize, which require natural language, which are stable enough to reuse across contexts. Each session, new interaction patterns emerge that don't fit the prior policy. The compulsive loop is the trilemma's recurrence: every policy decision creates a new edge case that demands a different mode. Knowledge poisoning introduces an adversarial pressure on top: any gossip-layer optimization also expands the attack surface.

**Novel Angle:** Evolutionary role refinement (AgentNet) — agents specializing and coordinating without a central authority — as the design direction. The player does not assign roles; roles emerge from repeated coordination. The player creates conditions under which useful specialization emerges, then observes what the network becomes. Emergent roles may be nothing the player anticipated; harder to audit, harder to debug, but no single point of failure.

## AI Integration Vector

**Player-AI Relationship:** The player is the conductor in a centralized design or an environmental designer in a decentralized one. In the centralized case, the player decomposes goals and routes to specialists. In the decentralized case, the player sets conditions and observes emergence. The relationship is mediated by the orchestration architecture: the player relates to individual agents through the structure they built, not directly.

**AI as Evolving System:** In AgentNet-style decentralized systems, agents evolve their roles through interaction — specialization is not assigned but emerges from repeated coordination. The network's role distribution changes over time as agents find their niches. This is development without a development plan: the emergent specialization is the outcome, and it may or may not be stable.

**AI as Development Environment:** The orchestration stack is the development environment — the formal protocol layer shapes which interactions are legible and auditable; the gossip layer shapes knowledge propagation. Just-in-time authorization (guardrails in IAM policy, not prompts) is the runtime constraint the environment enforces. The player designs the environment; agents develop within it.

**Persistence:** Knowledge poisoning exploits persistence: a false belief injected into one agent's memory propagates across sessions through normal gossip, without re-injection at subsequent nodes. What any agent believes is a function of everything the network has propagated, without provenance tracking. The player cannot selectively remove a belief once it has propagated past a certain depth.
