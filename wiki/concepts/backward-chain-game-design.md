---
type: concept
title: Backward-Chain Game Design
aliases: [backward chaining, constraint-first design, distribution-first design, derive backward execute forward]
tags: [game-design, production-methodology, business, distribution, systems]
sources:
  - ../sources/web-game-distribution-and-retention-2026.md
  - "../sources/A Playful Production Process For Game Designers - Richard Lemarchand.md"
updated: 2026-09-21
---

## Definition

A design method in which decisions are derived from the commercial and distribution constraints
at the *end* of the project, in strict reverse order — payout, channel, metric, session, loop,
verb, theme — and then executed in the forward direction. Theme and setting are chosen last, as
clothing for a structure already fixed.

**Status: proposed, untested.** Written 2026-09-21 for the basic-game project. It has not yet
survived a single project, and the honest test of it is whether Phase 0 changes any decision
that taste would not have reached anyway.

## The Chain

| # | Link | Question | Fixed by |
|---|---|---|---|
| 7 | Payout | What is one play worth, and to whom? | Market |
| 6 | Channel | What does the distributor require and reward? | Portal terms |
| 5 | Metric | What number must the game hit to earn distribution? | 7 and 6 |
| 4 | Session | What shape of session produces that number? | 5 |
| 3 | Loop | What cycle produces that session? | 4 |
| 2 | Verb | What single interaction drives that loop? | 3 |
| 1 | Theme | What does the verb look and sound like? | 2 |

Derivation runs 7 → 1. Execution runs 1 → 7: you build the verb first and integrate the ad SDK
last.

## How I Think About It

The default indie sequence is theme first — a setting, a mood, a story — and distribution last,
discovered as a disappointment after the build. Backward chaining inverts the discovery order so
the hardest constraints are known on day one, while they are still free to satisfy.

Web games make this unusually concrete because the constraints are published and early-binding.
A 50MB initial-download ceiling is a stack decision. A prohibition on opening menus is a
first-thirty-seconds design decision wearing a technical costume. A mandatory SDK event and an
ad-block-tolerant ad path are architecture. Each is trivial at the start and expensive to
retrofit — see
[web-game-distribution-and-retention-2026.md](../sources/web-game-distribution-and-retention-2026.md).

**What the chain cannot do, and the guard against pretending otherwise.** A constraint chain
narrows the space of acceptable games; it cannot generate a good one inside that space. Nothing
in it tells you to make a game about stacking blocks rather than dodging lasers. Treating the
derived numbers as the design brief is [The Metrics Trap](metrics-trap.md) in its game-design
form — the targets are diagnostic instruments, and the moment one becomes the goal it stops
measuring the thing it was chosen to track. The ordering rule that follows is: **taste filters
first, metrics filter second, and they are never merged.** A prototype a person enjoys that
misses a number gets an iteration; a prototype that hits every number and that nobody
voluntarily replays is dead. If a metric is consulted before anyone has played the thing and
reacted, the method has already failed.

**Where the chain is incomplete, and the fix.** As first written it ran straight from
constraints to loop generation, which skips the step [Experience Goals](experience-goals.md)
owns: how should the player *feel*? Lemarchand puts that at the top of ideation, before
mechanics, precisely because it is the filter every later decision passes through. The corrected
sequence inserts it between links 5 and 4 — the experience goal is derived under the metric
constraint but decided before any session or loop work. For a game whose target is "hard to put
down," the experience goal must name the feeling that *produces* the retry, not the retry
itself.

**Relation to the four-phase process.** This is not an alternative to Lemarchand's Ideation →
Preproduction → Full Production → Postproduction. It is a compression of it for one person, one
mechanic and a few weeks, and the mapping should stay visible so that what is skipped is skipped
knowingly. His central claim — that preproduction is the most critical phase and rushing it
causes most project failures — is the standing objection to any compressed schedule. The only
defensible answer is that in a single-mechanic game the
[vertical slice](vertical-slice.md) *is* the game, so preproduction and production collapse
rather than preproduction being cut. Which means the risk is not calendar but the **skipped
slice gate**: proving at final quality that the target experience is achievable.

## What It Is Not

Not metrics-driven design — see above. Not a licence to skip divergence: the chain produces a
box, and generation inside the box must still be wide, fast and wasteful. Not a claim that
constraints improve art in general; the claim is narrower, that *published, early-binding,
non-negotiable* constraints are cheaper to satisfy early than late.

## Design Uses

- Fixing a technical envelope before any code, so compliance is a property of the build rather
  than a late scramble.
- Killing candidate concepts on paper against written constraints rather than against opinion.
- Giving a solo developer a defensible reason to say no — the scarcest resource on a short
  schedule.
- Making theme a late, cheap, reversible decision rather than the emotional anchor that resists
  every later change.

## Related Concepts

- [Experience Goals](experience-goals.md) — the step the chain omitted; sits between metric and
  session
- [The Metrics Trap](metrics-trap.md) — the failure mode this method is most exposed to
- [Elegance (Game Design)](elegance-game-design.md) — what to generate once the box is drawn
- [Vertical Slice](vertical-slice.md) — the gate that compression is most likely to skip
- [Compulsion vs Craft](compulsion-vs-craft.md) — which mechanisms are allowed to satisfy link 5
- [Retention Proxy Testing](retention-proxy-testing.md) — how link 5 is checked before real data
  exists
- [Failure Cost Asymmetry](failure-cost-asymmetry.md) — the kill gates only work if killing is
  cheap

## Open Questions

- At what project scale does backward chaining stop paying? It plausibly suits a four-week web
  game and actively harms a four-year narrative project. Untested at either end.
- Does deriving theme last produce measurably weaker theming, or merely more replaceable
  theming? Attractor is a counter-example worth examining: its
  [Zone fiction](../projects/attractor/attractor-zone.md) was derived from the mechanic
  afterwards and is not obviously thin.
- How many links can be fixed on stale market data before the derivation is worthless?
- The method's own falsification test has not been designed: what would it look like for Phase 0
  to have been a waste of half a day?
- **Known failure mode, found 2026-09-23.** The method verifies *external* constraints rigorously
  — portal terms, rev-shares, technical envelopes — and is entirely silent about verifying the
  assets you believe you already have. On the basic-game project the chain's top links were
  derived from an assumed audience that turned out to be 3 followers, and the error propagated
  through channel, stack and platform before anyone asked the cheap question. A chain is only as
  sound as its least-examined premise, and the least-examined premise is reliably the one about
  yourself. Phase 0 needs an explicit "what am I assuming I already have, and what is its actual
  size" step.

## Project Connection

The operating framework for [Basic Game — Pipeline](../projects/basic-game/pipeline.md); Phase 0
is the backward pass and [constraint-sheet.md](../projects/basic-game/constraint-sheet.md) is
its output.
