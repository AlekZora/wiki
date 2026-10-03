---
type: project
title: Goal Map
status: active
updated: 2026-10-01
tags: [ai, llm, productivity, design, psychology, behavior]
---

# Goal Map

Turn one goal into a map, and see each day whether you're still on it.

**Status (2026-10-01):** active build and the current priority. It started as a two-day
prototype that doubles as an AI-engineering portfolio piece. **The user has decided it will
become a product**, so research and design notes in the vault are written for the product, not
only for the prototype scope.

Repo `github.com/AlekZora/goal-map` · local `~/projects/goal-map/` · Next.js + TypeScript,
Zod, Vitest, localStorage, Vercel, Anthropic via `lib/llm.ts`.
The code and its standing rules live in the repo; the vault keeps the prose.
Build log: [build-log.md](build-log.md).

## Core loop (from `docs/PROJECT.md`)

1. The user writes a goal in their own words.
2. AI structures the goal and proposes 3–7 milestones.
3. Code draws the map: start, milestones, summit.
4. Once a day, the user writes one line about what they did.
5. AI classifies that line against the milestones; code places a footstep.
6. Three unmarked off-route steps in a row trigger a gentle drift warning (plain code rule).

## Rules that shape every design idea

- AI does exactly three jobs (structure goal, generate milestones, classify check-in).
  Everything else is deterministic code. Every AI response is Zod-validated, retried once,
  then errors. Never shown unvalidated.
- The app never claims to know the best path, only whether you're on the one you declared.
- Declared detours are never drift. Drift needs a pattern, never one day.
- Warm, plain tone. No guilt, no hype. **No borrowed IP**; Harry Potter is named explicitly.
- Prototype out of scope: accounts, sync, databases, payments, multiple goals, notifications,
  AI-written drift messages, replanning, weekly reflection, mobile app, analytics SDKs. Several
  of these are things the product version will have to revisit. Change `PROJECT.md` first,
  never build around it.

## Repo docs

- `docs/PROJECT.md`: standing context and rules (stop and ask on conflicts)
- `docs/TASKS.md`: Tasks 1–9, J1–J4, optional 10
- `docs/DESIGN.md`: the survey-sheet visual spec (paper, ink trail, summit triangle, footsteps)

## Research in the vault

- [Goal Map — What the Wiki Says](../../answers/goal-map-wiki-synthesis.md): ranked ideas,
  tensions, bolder directions. **The main design-research document.**
- [Goal Map Feature Inspiration](../../answers/goal-map-feature-inspiration.md): earlier,
  unprioritised exploration pass
- [Evidence-based goal-achievement report](../../sources/evidence-based-goal-achievement-system.md):
  the main external source on goal-pursuit research
- [Worst-Day Design](../../concepts/worst-day-design.md): basis for "help when stuck"

## Open research gaps (2026-10-01)

Filled today: primary studies behind the research report (checked; see section 5 of the
synthesis), cozy-game design, subscription pricing.
Planning fallacy filled the same day (the user's brief, verified against Buehler et al. 1994;
concept `planning-fallacy`).
Lower priority: story structure beyond the hero's journey (only if a narrator is built), deep
work, consent and privacy for shared journeys (only for the bolder directions).
