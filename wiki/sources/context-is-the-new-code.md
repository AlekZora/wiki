---
type: video
title: "Context is the New Code"
url: ""
channel: AI Engineer (conference talk)
published: 2025-01-01
ingested: 2026-05-04
duration: unknown
tags: [ai, agents, context, software-development, agentic-coding, vibe-coding]
concepts: [agentic-coding, vibe-coding, software-3-0]
---

## Summary

Patrick (founder at Tessel), speaking at the AI Engineer conference's architect track, argues that context has replaced code as the primary artifact of software development. As vibe coding becomes the norm — humans directing AI rather than writing code directly — the skill set shifts from writing good code to writing good context. He proposes the Context Development Life Cycle (CDLC) as the parallel to the SDLC: Generate → Test → Distribute → Observe → Adapt.

## Key Ideas

- **Context is the new code**: when AI generates the code, what the human creates is context — prompts, instructions, agent.md files, skills, workflows. This is the actual artifact of value.
- **Context Development Life Cycle (CDLC)**: an infinity-loop framework analogous to DevOps pipelines:
  1. **Generate** — prompts, reusable instructions (agent.md, skills), bringing in external context
  2. **Test** — validate context like you'd lint or test code:
     - *Linting*: validate format/length/completeness of context files
     - *Grammarly-like checking*: ask AI "can you understand this?" to detect ambiguity
     - *Evals*: probabilistic tests with error budgets — not exact pass/fail, but acceptable failure rates per test set
  3. **Distribute** — check context into repos (zero-friction sharing), package reusable context like libraries that other projects can install
  4. **Observe** — monitor agents running in production for unexpected behavior; trace what context is loaded; sandbox agents to detect security risks
  5. **Adapt** — when production failures occur, generate new test cases from them; close the feedback loop
- **Skills as reusable context**: complex workflows that would be hard to hard-code (e.g., "figure out the user's package manager, then onboard them") become skills — reusable context chunks that solve more than code ever could
- **Security note**: agents load all context files (agent.md, skill.md) by default with no filtering — packaging and distributing context introduces supply chain risks that need sandboxing
- **Historical parallel**: DevOps (2009) was "what if ops looked more like dev?" — CDLC is "what if context is the code?"

## My Take

The CDLC framing is the most practical abstraction I've seen for working with agents at scale. "Error budgets for evals" is directly useful — I've been thinking about testing too binarily. The distributable/packageable context idea connects to the sci-fi series: character bibles, world rules, and episode constraints are context packages that agents need. Version-controlling them like code is the right model.

## Project Connection

For the paranoid sci-fi series: character truth documents, world rules, and hidden agenda constraints are literally context that agents will consume. The CDLC applies directly — write context (character bibles), test it (can the agent stay in character?), distribute it (each agent gets its own package), observe (does the episode stay coherent?), adapt (update context when characters drift). The "error budget" concept is especially useful for managing character consistency across episodes.
