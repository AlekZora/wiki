---
type: project
title: Goal Map
status: active
updated: 2026-10-04
tags: [ai, llm, agents, productivity, design, psychology, behavior]
---

# Goal Map

Goal Map is a web app that helps one person reach one personal goal along the path they chose.
AI designs a path of 3–7 milestones that has to follow eight rules. Code draws the path as a map.
After each working session the user writes one line, AI places it as a footstep, and repeated
off-path steps trigger a gentle drift warning. It started as a two-day prototype and is now built
as a product, in stages, while staying an AI-engineering portfolio piece. The product's bet: "we
don't sell better answers than a chatbot; we sell finishing."

**Status (2026-10-04):** active build and the current priority. Tasks 1–6 and P1 (the path
design pipeline) are done. Everything is pushed, up to `897c55a`.
**Current task:** P1b, ask before planning. After that P3 → P4 → W → G → GE → P2 → visual direction → J1–J3 → 7 → H → S → J4 → 8 → 9
(order in [TASKS.md](docs/TASKS.md)).
**Next gate:** a demand test with strangers, then the test week with 10–20 builders (go / change / stop).

Repo `github.com/AlekZora/goal-map` · local `~/Projects/goal-map/` · Next.js + TypeScript, Zod,
Vitest, localStorage, Vercel, Anthropic via `lib/llm.ts`.

## Where things live

One copy of every document.

- **Specs, in the repo** (the source of truth, shown here through the `docs/` symlink, Mac only):
  - [PROJECT.md](docs/PROJECT.md): product, principles, path rules, business model, data model
  - [TASKS.md](docs/TASKS.md): task prompts, run in order
  - [DESIGN.md](docs/DESIGN.md): the current visual spec (version 1, plus the proposed journey layer)
  - [design/BRIEF.md](docs/design/BRIEF.md): the brief for the separate design track
  - [prototypes/journey.html](docs/prototypes/journey.html): the throwaway journey prototype
- **Everything around the code, in this vault:** the sections below.
- **The Claude project** only holds a handoff note.

## Decisions

All in the vault's [decision log](../../decisions/decision-log.md), newest first:

- 10-03 [Design direction shifting toward an epic voyage with tension](<../../decisions/decision-log.md#2026-10-03 — Goal Map: design direction shifting toward an epic voyage with tension>) (in progress)
- 10-03 [Design track in a separate worktree](<../../decisions/decision-log.md#2026-10-03 — Goal Map: design track in a separate worktree>)
- 10-03 [Positioning: general headline, builders first](<../../decisions/decision-log.md#2026-10-03 — Goal Map: positioning, a general headline with builders first>)
- 10-03 [Demand test with strangers before the test week](<../../decisions/decision-log.md#2026-10-03 — Goal Map: demand test with strangers before the test week>)
- 10-03 [Waypoints and "Show me how" as AI job 4](<../../decisions/decision-log.md#2026-10-03 — Goal Map: waypoints and "Show me how" as AI job 4, measured against blind baselines>)
- 10-02 [Starting segment: builders shipping side projects](<../../decisions/decision-log.md#2026-10-02 — Goal Map: starting segment, builders shipping side projects>)
- 10-02 [First milestone free, Plus can be bought from day one](<../../decisions/decision-log.md#2026-10-02 — Goal Map: first milestone free, and Plus can be bought from day one>)
- 10-02 [Ask before planning (P1b)](<../../decisions/decision-log.md#2026-10-02 — Goal Map: ask before planning (Task P1b)>)
- 10-01 [Sonnet as the plan model](<../../decisions/decision-log.md#2026-10-01 — Goal Map: Sonnet as the plan model>)
- 10-01 [Eight path rules and the planning pipeline](<../../decisions/decision-log.md#2026-10-01 — Goal Map: eight path rules and the planning pipeline>)
- 10-01 [Business model and decision point](<../../decisions/decision-log.md#2026-10-01 — Goal Map: business model and decision point>)
- 10-01 [Four layers: purpose → engine → engagement → revenue](<../../decisions/decision-log.md#2026-10-01 — Goal Map: four layers, purpose → engine → engagement → revenue>)
- 10-01 [Built as a product, in stages](<../../decisions/decision-log.md#2026-10-01 — Goal Map: built as a product, in stages, instead of a two-day prototype>)

## Build log

[build-log.md](build-log.md): newest first, under the CLAUDE.md Build Log Rule.

## Research

[research.md](research.md): the wiki synthesis, the Perplexity reports, the primary-source
checks, and the competitor scan.

## Design references

[design-references/](design-references/README.md): images and notes for the design session.

## Testing

- [testing/real-goals.md](testing/real-goals.md): real goals for the plan and guide evals, plus my own path as benchmark cases
- [testing/test-week.md](testing/test-week.md): testers, check-ins, milestones, payments, quotes

## Launch

- [launch/demand-test.md](launch/demand-test.md): the clip, the page, views → clicks → sign-ups → purchases
- [launch/build-in-public.md](launch/build-in-public.md): posts, drafted and published
- [launch/founding-offer.md](launch/founding-offer.md): terms, checkout link, buyers

## Ideas

[ideas/later.md](ideas/later.md): ideas parked for later stages.
