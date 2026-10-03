---
type: concept
title: Loop Engineering
aliases: [loop design, autonomous agent loop, agent loop design]
tags: [ai, llm, agents, orchestration, engineering, tool]
sources:
  - ../sources/loop-engineering-osmani.md
updated: 2026-06-09
---

## Definition

Loop engineering is the practice of designing autonomous systems that discover
work, prompt AI agents, verify outputs, record state, and decide what to do
next — replacing the human as the person who prompts. Rather than issuing
one prompt at a time, the engineer authors a *loop*: a self-sustaining
recursive goal structure that runs across sessions without human initiation.
The leverage point moves from *how to prompt* to *how to design the system
that prompts*.

The article that named it (Addy Osmani, 2026) maps the practice onto five
building blocks that both Claude Code and OpenAI Codex now ship:
automations (the heartbeat), worktrees (isolation for parallelism), skills
(persistent intent), plugins/connectors (real-tool access), and sub-agents
(maker/checker split). A sixth element — external memory (any state file
outside context) — is what gives the loop continuity across runs.

## How I Think About It

Loop engineering sits **one floor above harness engineering**. The
[harness](harness-engineering.md) is the runtime environment a single agent
runs inside: it manages tools, memory, approval gates, observability. The
loop is what orchestrates many harness runs over time: it fires the trigger,
selects the task, dispatches the agent, evaluates completion, and persists
what happened. You can have a harness without a loop (a single prompted run);
you cannot have a reliable loop without a harness inside each run.

**The six elements and why each matters:**

1. **Automations (heartbeat)**: Without a trigger that fires without you,
   it's not a loop — it's a recipe you run manually. The automation is what
   makes the loop self-sustaining. In Claude Code: `/loop`, `/cron`, hooks,
   GitHub Actions. The key feature is that findings come *to you*, not you
   going around checking.

2. **Worktrees (isolation)**: Two agents writing the same file is the
   mechanical failure mode of parallelism. A git worktree gives each agent
   its own working directory on its own branch, sharing history but
   preventing collision. Worktrees are what make the loop horizontally
   scalable without coordination overhead.

3. **Skills (intent persistence)**: Skills are authored intent written
   outside context — the conventions, build steps, and "we don't do it like
   this" encoded once and read every run. Without skills, the loop
   re-derives your whole project from scratch every cycle. With skills,
   context compounds. Skills are also the antidote to "intent debt": any
   gap in authored intent gets filled by confident model guessing.

4. **Plugins/connectors (real-tool access)**: A loop that can only touch
   the filesystem is a small loop. MCP-based connectors let the loop open
   PRs, update tickets, query databases, ping Slack. This is the difference
   between an agent that says "here is the fix" and a loop that acts inside
   your actual environment.

5. **Sub-agents (maker/checker split)**: The model that wrote the code is
   too lenient grading its own homework. A second agent with different
   instructions — and sometimes a different model — catches what the first
   talked itself into. This split is applied most interestingly to *the
   stop condition itself*: the `/goal` primitive uses a separate small model
   to evaluate whether the loop is done, not the one that did the work.

6. **External memory (the spine)**: Any state file outside context —
   markdown, Linear board — that persists what's done and what's next. The
   model forgets; the repo doesn't. This is what allows a loop to pick up
   where it stopped rather than restarting from zero.

**The `/goal` primitive** is the sharpest conceptual contribution: a
verifiable stop condition evaluated by a different model from the one that
did the work. It applies the maker/checker split to *termination* — the
most consequential decision the loop makes.

**Three failure modes that sharpen as the loop improves:**
- **Verification burden**: "Done" is a claim, not a proof. A loop running
  unattended makes mistakes unattended. The verifier sub-agent raises the
  bar but doesn't remove the burden — the engineer still confirms it works.
- **Comprehension debt**: The faster the loop ships code you didn't write,
  the bigger the gap between what exists and what you understand. Smooth
  loops accelerate this debt unless you read what the loop produced.
- **Cognitive surrender**: Designing a loop to avoid thinking rather than to
  move faster on understood work produces opposite outcomes from the same
  tooling. The loop doesn't know the difference; the engineer does.

## AI Integration

- **Loop design is itself an AI engineering problem**: specifying skill files
  precisely enough to prevent intent drift, designing sub-agent instructions
  that produce genuinely independent verification, and calibrating
  automation triggers to match the rate work actually arrives are all
  non-trivial AI design questions. Loop engineering is meta-level AI
  application: AI used to design the conditions under which AI operates.

- **The maker/checker split as architectural primitive**: separating the
  generating model from the evaluating model is a structural solution to
  model self-leniency. Applied to stop conditions (`/goal`), it's the most
  principled available answer to "how does an autonomous loop know when it's
  done?" — one of the hardest open questions in agentic AI.

- **Comprehension debt is an AI-specific risk amplifier**: any autonomous
  system that removes humans from the hot path creates a gap between output
  rate and human comprehension rate. AI loops run at a rate no human can
  match; the comprehension debt accrual is proportionally faster than in any
  prior automation paradigm. Skills and verified sub-agents are the only
  structural mitigations.

- **Cognitive surrender as the named failure mode of over-automation**: the
  risk is not that AI replaces the engineer — it's that the engineer
  *delegates judgment* because the loop's fluency makes delegation feel
  safe. This is a behavioral AI risk distinct from model capability; it
  increases with loop quality, not decreases.

- **Loop engineering as the next abstraction layer above prompt engineering**:
  the progression is: single prompt → multi-turn → agentic workflow →
  harness → loop. Each layer handles more of the control flow. Loop
  engineering is where the human fully exits the hot path and becomes
  environment designer. The design question shifts from "what do I say to
  the model?" to "what does the system say to the model, and how does it
  know when to say it?"

## Related Concepts

- [Harness Engineering](harness-engineering.md) — the runtime environment
  each agent run executes inside; loop engineering orchestrates across runs
- [Agentic Workflow](agentic-workflow.md) — the goal→loop→outcome shift;
  loop engineering is the structured engineering discipline built on top
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — sub-agents
  are one of the five building blocks; orchestration is the intra-loop layer
- [Agent Memory](agent-memory.md) — external memory is the sixth element and
  the continuity mechanism across loop executions
- [Cognitive Externalization](cognitive-externalization.md) — loop
  engineering externalizes the prompting act itself, not just agent memory
  or skills

## Open Questions

- What is the right granularity for a loop's memory file? Too fine and it
  becomes a changelog; too coarse and the next run misses load-bearing state.
- How do you design a sub-agent verifier that is genuinely independent rather
  than just agreeing with the maker in different words?
- At what loop maturity level does comprehension debt become a systemic
  risk — when does "reading what the loop made" become practically
  impossible at the loop's output rate?
- How do you measure whether a skill file is reducing intent drift versus
  just constraining the model into local optima?
- What does "loop quality" mean as a metric — output volume, verification
  pass rate, comprehension-debt rate, or something else?

## Project Connection

The Side Quest AI system is a game-domain instance of loop engineering: the
validation pipeline (Phase A–C) replaces the human as the entity deciding
when a quest is ready to offer. The trigger fires without human initiation;
the pre-generation phase assembles game state autonomously; the validator
checks output against the fact database; the recovery cascade decides what
to try next. The "external memory" is the SQLite fact database itself —
the authoritative state that persists across all loop executions.

The maker/checker split appears explicitly: the LLM generates the quest
(maker); the rule-based validator checks it against reality (checker). The
experience goal test — "did the player ask how did they know that?" — is
the domain-specific stop condition the loop is designed to satisfy.
