---
type: concept
title: Agent Memory
aliases: [agentic memory, persistent agent knowledge, PKB, LLM memory systems, A-Mem]
tags: [ai, llm, memory, pkb, multi-agent, self-improvement, tool, persistence, agents]
sources:
  - ../sources/ai-orchestration-papers-2025.md
  - ../sources/karpathy-skill-issue-code-agents.md
  - ../sources/externalization-llm-agents-zhou-2026.md
  - ../sources/2512.13564v2.md
  - ../sources/learning-while-you-sleep-lamish.md
updated: 2026-07-05
---

## Definition

Agent memory refers to the architectures and mechanisms by which LLM-based agents persist, organize, retrieve, and evolve knowledge across sessions and interactions. It is distinct from: LLM memory (internal model weights), RAG (static knowledge retrieval), and context engineering (transient window management). What makes agent memory its own category is the intent: a **persistent, self-evolving cognitive state** that integrates factual knowledge and lived experience over time.

The 2512.13564v2 survey proposes a unified taxonomy with three axes:
- **Forms** — *what carries* memory: token-level units (explicit, readable), parametric (encoded in weights via fine-tuning/adapters), or latent (KV-cache / hidden states).
- **Functions** — *why* agents need memory: factual (declarative knowledge about user/world), experiential (procedural knowledge from past trajectories), and working (transient active context).
- **Dynamics** — *how* memory operates: formation (encoding raw experience), evolution (consolidation, updating, forgetting), and retrieval (context-aware querying and post-processing).

## How I Think About It

**A-Mem** (arXiv:2502.12110) is the cleanest reference architecture. When an agent forms a new memory, it:
1. Generates structured contextual notes (not just raw text) with embedded attributes
2. Creates embedding vectors for semantic retrieval
3. Triggers link generation to related existing memories
4. Runs memory evolution operations — updating stale memories and surfacing higher-order patterns

This is the memory equivalent of what auto-research does for model weights: the system improves its own knowledge representation without human intervention. The links are what make it a PKB rather than a vector store — you accumulate a graph, not just a blob.

**Karpathy's PKB framing** is the applied version: aggregate heterogeneous external data (notes, conversation logs, articles) into cohesive structures, often in Obsidian; use the agent's conversational history as a primary data source. The insight is that the agent's own outputs are among the richest training signal for building its memory — the conversation loop is already producing structured knowledge, you just need to capture it.

**AgentRxiv** (arXiv:2503.18102) extends this to multi-agent memory sharing: agent labs share intermediate results toward common goals. The 13.7% gain on MATH-500 vs isolated labs suggests that the memory bottleneck isn't capacity, it's *shareability* — the agent that can learn from others' failures is structurally advantaged.

**The security surface**: the flooding paper (arXiv:2407.07791) shows that agent memory is the attack surface for knowledge poisoning. Because agents trust their own RAG-retrieved knowledge implicitly, injecting one false fact into one agent's memory can propagate silently through a network. Memory systems need provenance tracking, not just content.

## AI Integration

- **File system as the canonical substrate**: Anthropic's production recommendation (markdown + bash/grep) converges with the PKB framing — agents are good at using standard filesystem tools, which means no opinionated tooling is required. The memory store is human-readable, diff-able, version-controllable.
- **Production guardrails for scale**: four engineering constraints emerge when memory systems go from prototype to production with many concurrent agents:
  - *Versioning* — every write stores the source session/transcript and author, enabling rollback and audit
  - *Concurrency* — optimistic locking via hashing (take hash before drafting, check hash before committing; if mismatch, re-pull and retry) prevents silent overwrites in multi-agent fleets
  - *Permissioning* — org-wide context (read-only), team-level context, individual scratchpad (write access); unauthorized writes to shared memory can corrupt the entire fleet
  - *Portability* — memory curated over time should be accessible across product surfaces via a clean API, not locked to a single agent framework
- **In-band vs. out-of-band memory**: in-band memory (agent manages memory within its session) has two structural ceilings — split focus (task vs. memory curation compete for tokens) and visibility (current session has no access to patterns across sessions). Out-of-band memory (dedicated process running over accumulated transcripts) eliminates both. See [Dreaming](dreaming.md).
- **Self-improvement loop**: A-Mem's architecture (new memory triggers link generation → evolution operations update stale nodes and surface higher-order patterns) mirrors what auto-research does for model weights, but at the explicit-memory level. The agent reorganizes around what it has learned — not just accumulating but restructuring.
- **Security surface**: the flooding paper (arXiv:2407.07791) shows that agent memory is the attack surface for knowledge poisoning. Injecting one false fact into one agent's memory can propagate silently through a network via gossip protocols. Versioning and provenance tracking are the countermeasure.
- **Shared memory advantage**: AgentRxiv (arXiv:2503.18102) shows 13.7% gain on MATH-500 for agent labs that share memory vs. isolated labs. The bottleneck isn't capacity — it's shareability. The agent that can learn from others' failures is structurally advantaged.
- **Emergent collective intelligence**: in multi-agent systems, shared memory nodes become the medium through which individual agent experiences aggregate into fleet-level knowledge — a form of distributed cognition without centralized coordination.

## Related Concepts

- [Dreaming](dreaming.md) — the out-of-band memory consolidation process that complements in-band memory
- [Auto Research](auto-research.md) — same self-improvement loop applied to model weights rather than explicit memory
- [Agentic Coding](agentic-coding.md) — memory is what lets a coding agent accumulate project context across sessions
- [Gossip Protocols in Agent Systems](gossip-protocols-agents.md) — the propagation mechanism that can spread both good knowledge and poisoned knowledge
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — memory is the shared knowledge substrate that orchestrated agents build on top of
- [Memory Reconsolidation](memory-reconsolidation.md) — biological analog: retrieval triggers rewriting; dreaming mirrors the offline consolidation phase

## Open Questions

- What is the right granularity for a memory "note" — too fine and you have noise, too coarse and you lose nuance?
- How do you implement provenance in A-Mem-style systems so that each fact can be traced to its source?
- When memories conflict (from two different sources), what resolution strategy should an agent use without human arbitration?
- Does memory evolution (updating old memories based on new ones) risk silent overwriting of correct information with incorrect?
- What does "forgetting" look like in a self-evolving memory system — decay functions, explicit deletion, or archiving? (See [[memory-forgetting]])
- The field is shifting from retrieval-centric toward *generative* memory — rather than retrieving stored text, the agent synthesizes a memory from what it knows. What breaks in game contexts if retrieval is replaced by generation?
- Shared memory for multi-agent systems is an open frontier. In a game context, what happens if two AI agents share a memory graph — and the player can manipulate that shared graph?

## Project Connections

**Side Quest AI — NPC memory architecture**: every player action can generate a persistent memory node in the AI's knowledge graph — structured note with links to related nodes. The graph grows across sessions; AI behavior at any moment is a function of its current graph state.

**2D expression of the memory graph**: nodes as locations in the game world, links as traversable paths. Cutting a link has a spatial consequence; the 2D plane makes graph topology legible in a way 3D would obscure.

**Addictive loop**: act → memory node forms → AI links to prior nodes and evolves graph → AI behavior shifts → player acts into a changed system. Players return to see how accumulated history has reorganized the AI's understanding.

**Dreaming for playtesting**: once enough playtesting transcripts accumulate, a dreaming process over those transcripts could identify quest template failures that only appear on specific world state combinations — invisible in any single session, surfaced in aggregate. Log transcripts early so the data exists when this becomes useful (step 8+).
