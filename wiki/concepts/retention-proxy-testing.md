---
type: concept
title: Retention Proxy Testing
aliases: [retention proxies, pre-launch stickiness testing, fast retention signal, D1 proxy]
tags: [game-design, research-methods, metrics, playtesting, production-methodology]
sources:
  - ../sources/web-game-distribution-and-retention-2026.md
updated: 2026-09-21
---

## Definition

Same-day observations that stand in for retention metrics which by definition cannot be measured
yet. D7 retention takes seven days and a population; a four-week solo project has neither.
Proxies substitute *observable in-session behaviour* for *longitudinal cohort behaviour*.

**Status: proposed, thresholds uncalibrated.** The numbers below are invented precision until
something checks them against a game whose real D1 is known — Attractor being the obvious
candidate.

## Scope, and what this concept does not own

This note covers **what to observe**. It does not cover **who you are allowed to observe, and in
what order** — that is [Comprehension Floor](comprehension-floor.md), and it is the harder
problem. Reading this note without that one produces the exact mistake described below.

## The Proxies

- **Unprompted replay rate.** Of players who fail once, what fraction start again without being
  asked? Below ~50% the loop leaks at the failure moment; above ~70% it is a keeper. Proxies D1.
- **The stop test.** Say "stop whenever you like," then say nothing. Measure elapsed time *and
  where in the run they stopped*. Stopping between runs is normal; abandoning mid-run is severe —
  the run itself stopped being worth finishing. Stopping only to an outside interruption is the
  best result available.
- **Time-to-first-meaningful-failure.** Seconds from load to the first failure the player
  understood and cared about. Under 30 seconds for a run-based game. A long ramp to the first
  real stake is the commonest reason a portal player leaves before the loop engages.
- **The articulation question.** After playing: what are the rules, and why did you die? A
  subject who cannot state the rule in one sentence was given a loop too complex for the genre;
  one who blames the game was given a loop that is unfair or illegible. Both fatal, both
  fixable. **Subject to the ordering constraint below.**
- **Cold return.** Send five people a link; say nothing the next day; count unprompted reopens.
  Crude, small-n, and the only true longitudinal signal available inside a week.

## How I Think About It

The standard advice — soft launch, watch D1, iterate — assumes an install budget and a calendar
with slack. Without proxies a short project either ships on taste alone or stalls waiting for
data it structurally cannot collect.

**The correction that matters.** As first written this method said to test three prototypes on
the same testers in one afternoon, order randomised. That is wrong, and
[Comprehension Floor](comprehension-floor.md) records why, from this vault's own worked failure:
ten enthusiastic Attractor testers produced zero usable legibility data because every one of
them had been shown the button label, the hint and the legend before being asked whether the
game read. The sample was not small, it was **spent**. Knowledge of the answer is irreversible
and contaminating, which makes a naive subject a *consumable* resource rather than a renewable
one. Consequences:

1. Three prototypes need three disjoint tester pools, or the second and third are measuring a
   player who already knows what a near-miss looks like in your design language.
2. The articulation question is asked **once per person, before anything explains the game** —
   before the legend, before your verbal setup, before the second prototype.
3. Tester budget is a Phase 1 planning input, not a Phase 2 convenience.

**What the proxies cannot see.** None of them distinguishes craft-side from compulsion-side
stickiness — see [Compulsion vs Craft](compulsion-vs-craft.md). Both families produce identical
replay rates in a one-afternoon window and diverge only across weeks. So the proxies can tell you
a loop is sticky and cannot tell you whether the stickiness will last, which is precisely the
question the business model turns on.

**Guard.** Five testers is an anecdote. The defence is that a carefully observed anecdote beats a
benchmark grid that its own source calls unverified folklore. The moment first-party numbers
arrive from live traffic they supersede every proxy here, and conflicts resolve in favour of the
live data without argument. Treating a proxy as a target rather than an instrument is
[The Metrics Trap](metrics-trap.md) at one remove.

## Related Concepts

- [Comprehension Floor](comprehension-floor.md) — owns the sampling half; read first
- [Compulsion vs Craft](compulsion-vs-craft.md) — the distinction these proxies are blind to
- [Experience Goals](experience-goals.md) — pass/fail signals give the proxies something
  project-specific to test against
- [The Metrics Trap](metrics-trap.md)
- [Vertical Slice](vertical-slice.md) — the gate these proxies support but cannot replace
- [Backward-Chain Game Design](backward-chain-game-design.md)

## Open Questions

- Do the 50% and 70% thresholds hold? They need calibration against at least one game whose real
  D1 is known.
- Does observer presence inflate replay rate? Almost certainly. Unattended remote testing would
  be a better instrument and has not been tried.
- **Which proxy, if any, predicts D7 rather than D1?** Plausibly none — and D7 is where
  ad-supported games die. This is the concept's largest unresolved gap.
- Can a naive subject be partially reused — spent on legibility but still valid for the stop
  test? Comprehension-floor implies no for the first question and is silent on the rest.

## Project Connection

The Gate 2 and Gate 3 protocol in
[Basic Game — Pipeline](../projects/basic-game/pipeline.md); tester budget is line 0.7 of
[constraint-sheet.md](../projects/basic-game/constraint-sheet.md).
