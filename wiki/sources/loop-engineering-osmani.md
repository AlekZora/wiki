---
type: article
title: "Loop Engineering"
url: https://x.com/addyosmani/status/2064127981161959567
author: Addy Osmani
published: 2026-06-09
ingested: 2026-06-09
tags: [ai, llm, agents, orchestration, agentic-workflow, engineering, tool]
concepts:
  - ../concepts/loop-engineering.md
  - ../concepts/harness-engineering.md
  - ../concepts/multi-agent-orchestration.md
  - ../concepts/agentic-workflow.md
---

## Summary

Loop engineering is the practice of designing autonomous systems that discover
work, prompt AI agents, verify outputs, and advance state — replacing the
engineer as the person doing the prompting. Rather than issuing prompts
one-at-a-time, the engineer authors the loop: a recursive goal structure that
runs independently across sessions. Both Claude Code and OpenAI Codex now ship
all five required building blocks. The post identifies those blocks, maps them
across both tools, names the failure modes that emerge as loops improve, and
argues the engineer's judgment remains irreplaceable even when no human is
in-the-loop during execution.

## Key Points

- **The shift**: "You shouldn't be prompting coding agents anymore. You should
  be designing loops that prompt your agents." (steipete / Brian Cherny)
- **Five building blocks** every loop needs:
  1. **Automations** — scheduled runs that discover and triage work without
     a human initiating them. In Claude Code: `/loop`, `/cron`, hooks, or
     GitHub Actions. In Codex: the Automations tab with its Triage inbox.
  2. **Worktrees** — isolated git working directories so parallel agents
     don't collide. Mechanical isolation, not social coordination.
  3. **Skills** — reusable intent files (SKILL.md / `.claude/agents/`)
     that encode project conventions once so the agent doesn't re-derive
     them from scratch every session. The antidote to "intent debt."
  4. **Plugins and connectors** — MCP-based integrations that let the loop
     act inside real tooling (issue trackers, databases, Slack, PRs) rather
     than just the filesystem.
  5. **Sub-agents** — the maker/checker split: one agent writes, a separate
     one verifies. The model that wrote the code is too lenient grading its
     own homework; a second agent with different instructions catches the
     gaps.
- **The sixth element — memory**: an external state file (markdown, Linear
  board, anything outside context) that persists what's done and what's next
  across sessions. The model forgets; the repo doesn't.
- **`/loop` vs `/goal`**: `/loop` re-runs on a cadence. `/goal` runs until
  a verifiable stop condition holds — checked by a *separate* small model,
  not the one that did the work. The maker/checker split applied to
  termination itself.
- **Three failure modes that sharpen as loops improve**:
  1. **Verification burden** — the loop makes mistakes unattended. "Done" is
     a claim, not a proof. The engineer still has to confirm it works.
  2. **Comprehension debt** — the faster the loop ships code you didn't
     write, the bigger the gap between what exists and what you understand.
     Smooth loops accelerate this debt unless you read what the loop made.
  3. **Cognitive surrender** — the comfortable posture is the risky one.
     Designing a loop to avoid thinking rather than to move faster produces
     the opposite result from the same tooling.
- **Token cost caveat**: usage patterns vary wildly; loop design must account
  for whether you are token-rich or token-poor.

## Quotes

> "Loop engineering is replacing yourself as the person who prompts the agent.
> You design the system that does it instead."

> "Two people can build the exact same loop and get completely opposite results.
> One uses it to move faster on work they understand deeply. The other uses it
> to avoid understanding the work at all. The loop doesn't know the difference.
> You do."

> "Build the loop. But build it like someone who intends to stay the engineer,
> not just the person who presses go."

## My Take

The most important observation in the piece is architectural, not tooling:
**loop engineering sits one floor above harness engineering**. The harness is
the runtime environment a single agent runs inside; loop engineering is what
orchestrates many harness runs across time, discovers work autonomously, and
decides what happens next. The distinction clarifies a confusion common in
discussions of agentic workflows — the harness and the loop are different
design surfaces with different engineering concerns.

The `/goal` primitive is the sharpest AI-specific idea here: a verifiable
stop condition evaluated by a *different model* from the one that did the
work. This is the maker/checker split applied not to code review but to
*termination itself* — a subtle but important extension of the principle.
A loop that self-evaluates its own completion condition has the same bias
problem as a model grading its own homework.

The three failure modes (verification burden, comprehension debt, cognitive
surrender) are named risks for autonomous AI systems, not just loop
engineering specifically. Any system that removes humans from the hot path
amplifies all three. Loop engineering accelerates the rate at which an
engineer can accrue comprehension debt — the loop's fluency is the greatest
threat to the engineer's judgment. The practical upshot: skills (written
project intent) and sub-agent verifiers are what keep the loop honest; the
loop without those two is cognitive surrender with extra steps.
