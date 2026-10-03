---
type: article
title: "Harness Engineering: Leveraging Codex in an Agent-First World"
url: https://openai.com/index/harness-engineering/
author: Ryan Lopopolo (OpenAI)
published: 2026-04-27
ingested: 2026-05-11
tags: [ai, agents, software-engineering, codex, tool]
concepts: [agentic-orchestration, harness-engineering]
---

## Summary

An OpenAI team built and shipped an internal product with zero lines of manually-written code over five months. Every line -- application logic, tests, CI, docs, observability, tooling -- was written by Codex agents. They estimate 10x speed improvement. The post describes what they learned about "harness engineering": designing environments, specifying intent, and building feedback loops so agents can work reliably.

## Key Points

- ~1 million lines of code, ~1,500 PRs merged with initially 3 engineers (now 7)
- Average throughput: 3.5 PRs per engineer per day, increasing as team grew
- Core philosophy: "Humans steer. Agents execute." No manually-written code.
- Engineer's role shifted to: designing environments, specifying intent, building feedback loops
- Early bottleneck was underspecified environments, not agent capability
- Made app bootable per git worktree so Codex could launch isolated instances per change
- Wired Chrome DevTools Protocol into agent runtime for UI validation
- Full local observability stack (logs, metrics, traces) exposed to agents via LogQL/PromQL
- Single Codex runs work on tasks for 6+ hours (often overnight)
- AGENTS.md should be a "table of contents" (~100 lines), not a monolithic manual
- Repository knowledge base lives in structured docs/ directory as system of record
- Agent-to-agent review replaced most human code review over time
- "Ralph Wiggum Loop": agent reviews own changes, requests additional agent reviews, iterates until satisfied

## Quotes

> "Give Codex a map, not a 1,000-page instruction manual."

> "The fix was almost never 'try harder.' Human engineers always stepped into the task and asked: 'what capability is missing, and how do we make it both legible and enforceable for the agent?'"

## My Take

This is the most concrete "agent-first development" case study I've seen. The key insight is that the engineer's job becomes infrastructure/environment design rather than code writing. The AGENTS.md lesson (map not manual) is directly applicable. The overnight 6-hour agent runs producing working PRs is remarkable. This validates the "harness engineering" concept -- human value is in designing the constraints and feedback loops, not the execution.
