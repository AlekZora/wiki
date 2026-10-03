---
type: concept
title: Organizational Tacit Knowledge
aliases: [company brain, tacit organizational knowledge, skills files, institutional knowledge formalization]
tags: [ai, agents, knowledge-management, organizations, automation, llm, memory]
sources:
  - ../sources/company-brain-yc.md
updated: 2026-06-10
---

## Definition

Organizational tacit knowledge is the accumulated know-how embedded in a company's people, processes, and informal communication channels that is never fully written down — how refunds actually get handled, when pricing exceptions are granted, how engineers respond to incidents. Organizations function because employees "vaguely remember" where this knowledge lives and how to apply it. It is fragmented across heads, email threads, Slack histories, support tickets, and databases. A new employee can't access it systematically; an AI agent can't access it at all.

A skills file is the formalized output of converting this tacit knowledge into explicit, structured, executable instructions that AI agents can follow. The company brain is the system that performs this conversion: extracting knowledge from fragmented sources, structuring it, keeping it current, and publishing it as skills files.

## How I Think About It

The key distinction the company brain concept draws is between two ways of making organizational knowledge available to an AI:

- **Search/RAG over documents**: finds relevant text fragments but doesn't tell the agent what to *do* with them. Still requires the agent to infer the procedure.
- **Skills file**: a procedural artifact that encodes *how* something gets done — not just what happened but what the decision logic is.

The analogy that helps me: a new employee doesn't learn to handle refunds by searching the email archive. They learn by being told "here's the policy, here are the exceptions, here's who to escalate to." The skills file is the written version of that onboarding. It's the answer to "what would a competent employee need to know to handle X reliably?"

The tacit knowledge problem scales with organizational complexity. A two-person company has almost no tacit knowledge bottleneck — everything fits in a conversation. A 500-person company is mostly running on accumulated informal knowledge that no single person holds. The company brain is more valuable at scale precisely because tacit knowledge accumulates faster than explicit documentation.

**The extraction problem is hard**: tacit knowledge is tacit because no one thought it needed to be written down. Extracting it requires watching how decisions are actually made, not reading what was written about how they should be made. This implies the company brain system must observe behavior, not just index documents.

## AI Integration

- **Bottleneck shift**: as models became capable enough to automate complex tasks, the constraint moved from "can the model do this?" to "does the model know how we do this?" Organizational tacit knowledge is now the primary bottleneck for AI business automation — not model capability.
- **Skills files as agent primitives**: the skills file is an executable representation of organizational procedure. An AI agent consuming a skills file is doing the same thing a human employee does when following a SOP — except the SOP was generated from observation, not written by hand.
- **Living map requirement**: the company brain must stay current as procedures change. This is a continuous extraction and update problem, not a one-time indexing task. The knowledge has a decay rate tied to organizational change velocity.
- **Vertical specialization**: the first company brains to deliver value will likely be domain-specific — legal, medical, engineering, finance — where tacit knowledge has high precision requirements and high cost of error. General-purpose company brains are harder because the extraction heuristics differ across domains. **The demo problem solved by the game**: Enterprise AI grounding is difficult to demonstrate convincingly without access to a real company's messy, proprietary knowledge infrastructure. The Side Quest AI game solves this. A grounded NPC that only references verified world-state facts versus an ungrounded one that hallucinates quest details is immediately visible and legible to any observer — no domain expertise required. The game demo is a proof-of-concept for the enterprise grounding architecture that is actually showable in a pitch room. Same architecture, different domain, publicly demonstrable.
- **Connection to agent grounding**: skills files solve a grounding problem. An agent without a skills file hallucinates procedure from training distribution ("what would typically be done here?"). An agent with a skills file executes from explicit organizational fact ("what does this company actually do here?"). This is the same distinction as general knowledge vs. world-state knowledge in game NPCs.

## Related Concepts

- [Cognitive Externalization](cognitive-externalization.md) — skills files are externalization of organizational cognition; the company brain formalizes what employees carry implicitly
- [Agent Memory](agent-memory.md) — company brain as a form of organizational memory that persists across employee turnover
- [Harness Engineering](harness-engineering.md) — skills files are a harness artifact; the company brain builds and maintains the harness for enterprise AI
- [World Models](world-models.md) — the living map of how a company works is a company-scoped world model: structured, current, agent-readable

## Open Questions

- Can the extraction step be automated — does the company brain observe actual decisions to generate skills files, or does it rely on human annotation?
- How do you validate that a skills file is correct? Refund policies have exceptions and edge cases that may not surface until an agent makes a wrong decision at scale.
- Is there a minimum tacit-knowledge threshold below which the company brain is not worth building — and what determines that threshold?
- How does the skills file handle conflicting signals — when observed behavior differs from documented policy?

## Project Connections

- The Step 6 fact database in the Side Quest AI game project is structurally a company brain for the game world. The NPC schema records what individual NPCs know (tacit, character-local). The fact database extracts and structures world-state facts into an explicit, queryable form the quest generator can use. The hard-constraint validator is the grounding system that ensures the generated quest only references facts that actually exist — the same role the skills file plays in ensuring an AI agent only executes procedures that actually apply. See: [wiki/projects/game/PROJECT-CONTEXT.md](../projects/game/PROJECT-CONTEXT.md)

- This also means the game demo serves a function no enterprise pilot can easily replicate: it makes the grounding architecture _visible_. An NPC that hallucinates a quest detail is immediately wrong in a way anyone can see. An enterprise agent that hallucinates a refund procedure requires domain knowledge to catch. The game is the legible version of the proof.
