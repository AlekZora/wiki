---
type: video
title: "Learning While You Sleep"
url:
channel: AI DevCon
published:
ingested: 2026-07-04
duration:
tags: [ai, agents, memory, context-engineering, multi-agent, dreaming, production, llm]
concepts:
  - ../concepts/agent-memory.md
  - ../concepts/dreaming.md
---

## Summary

Lamish, a member of technical staff on Anthropic's Applied AI team, traces the past year of context engineering from the first CLAUDE.md files through memory tools and skills, arriving at a production architecture built on file systems. The centerpiece of the talk is "dreaming" — an out-of-band, batch-mode process that reviews accumulated agent transcripts to consolidate memory and identify cross-session failure patterns that in-session agents can never see.

## Key Ideas

- **Context engineering as a force multiplier**: raw model intelligence compounds when paired with well-engineered context; the two effects stack even as models improve
- **Evolution of memory systems** (past year, in order):
  1. CLAUDE.md — injected markdown, "unreasonably effective," but bloats over time
  2. Memory tools — agents autonomously read/write; in-band, within a session
  3. Skills — progressive disclosure; agent scans front matter, loads body only when relevant (bookshelf analogy)
  4. File system memory — markdown + bash/grep; agents search rather than retrieve; most flexible, current state of the art
- **File system as canonical memory substrate**: markdown is human-readable, agents can grep and bash across it, no opinionated tooling required
- **Progressive disclosure**: the key innovation in skills — the agent sees a short summary before deciding to load the full detail, so depth doesn't cost context
- **Production challenges at scale**: multi-agent concurrent writes, stale memories, malicious injection, human/agent collaboration on shared memory
- **Four production guardrails**:
  - *Versioning* — every memory update stores the source session/transcript, author, rollback capability
  - *Concurrency* — optimistic locking via hashing: agent takes hash before drafting, checks hash before committing; if mismatch, re-pulls and retries
  - *Permissioning* — org-wide memory (read-only for agents) vs. team-level vs. individual scratchpad (write access); granularity matters
  - *Portability* — curated memory should be accessible across product surfaces via a clean API
- **In-band vs. out-of-band memory**: in-band = agent manages memory within a session (competing focus, limited visibility); out-of-band = dedicated process with cross-session access
- **Dreaming** — the out-of-band memory consolidation process:
  - Runs in batch, asynchronously, with its own token budget
  - Takes memory store + N transcripts from recent sessions (including tool call metadata, not just message passes)
  - Orchestrator deploys sub-agent fleet to analyze transcripts for patterns
  - Sub-agents report pattern candidates; orchestrator synthesizes, decides what's prevalent enough to warrant a memory update
  - Outputs proposed diffs to the memory store, with supporting transcript examples and prevalence statistics
  - Human reviews and accepts or rejects proposed changes
- **Dreaming examples**: missing topic in curriculum (entire agent fleet wrong on same question); misconfigured tool (all agents output radians instead of degrees); org-wide style drift (too many em dashes)
- **Why dreaming pays off**: agents that learn from accumulated failures one-shot tasks more often → fewer tokens spent per task → cost reductions that offset the dreaming token budget
- **Anthropic product**: the Managed Agents API includes a memory and dreaming infrastructure implementing these patterns

## Timestamps

- ~00:00 — Introduction and context engineering framing
- ~mid — Evolution of memory: CLAUDE.md → tools → skills → file systems
- ~mid — Production challenges: concurrency, versioning, permissioning, portability
- ~mid — In-band limitations (split focus, visibility)
- ~mid — Dreaming: architecture, teacher/student analogy, examples
- ~end — Memory + dreaming as complementary parallel processes; summary
- ~Q&A — Managed Agents as the out-of-box implementation; permissioning and dreaming compose; "are we reinventing databases?" (yes, deliberately)

## My Take

The most interesting AI angle here is the convergence with neuroscience: dreaming in agents recapitulates sleep-based hippocampal replay almost exactly. During sleep, the brain replays experiences to consolidate important patterns into long-term memory and prune noise — without the distraction of waking tasks. Lamish's dreaming process does the same thing: dedicated capacity, cross-session visibility, batch mode, human review in the loop. This isn't an analogy for presentation purposes; it appears to be a genuine structural parallel — any sufficiently capable learning system may require a dedicated offline consolidation phase because in-session learning is fundamentally constrained by competing task demands.

For the Side Quest AI project, dreaming becomes relevant once enough playtesting transcripts exist to surface patterns. A quest template that silently fails on a specific world state combination will never be caught in a single session, but dreaming over 50 playtesting runs would expose it immediately. This is a step-8+ concern, not a prototype concern.

The file system approach (markdown + bash/grep) is worth noting as a design validation of the current wiki architecture: Anthropic's production recommendation is essentially what this knowledge base already does.
