---
type: article
title: "Roblox Horror in 2026: Market Structure, Engagement, Retention, Launches and Policy"
url: https://rblxdb.com/best-roblox-games/horror
author: Perplexity Advanced Deep Research synthesis, citing RBLXDB, Rolimons, RoMonitor, BloxBunny, RoVitals, GameAnalytics, Roblox Creator Hub and Community Standards
published: 2026-09-23
ingested: 2026-09-23
tags: [game-design, roblox, horror, market-analysis, retention, moderation, platform]
concepts:
  - ../concepts/compulsion-vs-craft.md
  - ../concepts/elegance-game-design.md
  - ../concepts/metrics-trap.md
---

## Summary

Commissioned for basic-game Phase 1 to supply the quantitative layer missing from
[roblox-horror-and-90s-anthology-structure.md](roblox-horror-and-90s-anthology-structure.md).
It **overturned that note's headline claim** and replaced the project's largest stated risk with a
different, sharper one.

Roblox horror is large, extremely concentrated, and statistically ill-defined — Roblox removed
Horror as a clean genre and treats it as a cross-genre theme, so no authoritative census exists.

## Key Points

### Concentration

16 Sep 2026 snapshot of a curated 30-game tracker universe: all 30 above 1K CCU, 561,482 CCU
total. Leader (*Murder Mystery 2*) **49.1%**; top 3 **69.3%**; top 5 **78.8%**; top 10 **88.2%**.
HHI 2,695 — equivalent to **3.71 equally sized titles**. Rank 30 still held 1,965 CCU, so a long
tail exists. Boundary is contested: a different tracker ranks *99 Nights in the Forest* first at
~172K CCU and RBLXDB omits it.

### Session length — the correction

Public average playtime, not run-completion time:

| Experience | Archetype | Minutes |
|---|---|---:|
| DOORS | long-form procedural | ~12.5 |
| Pressure | long-form procedural | 7.9–13.7 |
| Apeirophobia | long-form exploration | 12.7–16.0 |
| Road-Side Shawarma | short rules/service | 8.1–8.6 (RoMonitor 11.3) |
| Scary Shawarma Kiosk | rules/anomaly | 11.0–11.5 |
| Short Horror Games | short anthology | 10.36 |

Long-form median ~13 min (range 12–16); short/rules 8–11. **A 3–4 minute gap, not 45–90 minutes.**
The mechanical reason is censoring — early deaths, lobby exits and aborted runs. A full successful
*Pressure* ending can exceed 45 minutes while average playtime sits near 13.

### Solo versus co-op

| Classification | Games | CCU share | Median CCU |
|---|---:|---:|---:|
| Solo-capable (usually also co-op) | 19 | 23.0% | 2,940 |
| Multiplayer-dependent / round-based | 11 | 77.0% | 6,359 |
| **Strictly solo** | **0** | **0%** | — |

Excluding *Murder Mystery 2*, the multiplayer median stays ~2.1× solo-capable. Report is careful
that this is **not causal**: *DOORS* is solo-capable at 57,184 CCU. Its interpretation is that the
largest loops are **social, replayable and round-based**, while one-and-done solo narratives rarely
accumulate recurring CCU. A 2025 DevForum thread states the creator-side worry directly — one-shot
horror may be liked but gives no reason to return tomorrow.

### Retention — no public data

Experience-level D1/D7/D30 is not public; Roblox exposes it only through authorized Creator
Analytics / Open Cloud. Roblox publishes **D30, not D28**.

| Dataset | Population | D1 | D7 | D30 |
|---|---|---:|---:|---:|
| GameAnalytics 2026 | its instrumented Roblox sample | 10.3% | 1.6% | 0.5% |
| Roblox illustrative example | similar-experience P50 | 12.4% | — | — |
| BloxG 2026 | claimed all-genre | 28% | 11% | 4.5% |
| BloxG 2026 | claimed horror | 22% | 8% | 2.8% |

The report states these **should not be reconciled** — different populations, weighting, maturity
and instrumentation — and that BloxG exposes no verifiable sampling frame.

### New launches, 18 months

At least **nine** original horror launches since Mar 2025 verifiably exceeded 10K peak CCU;
10–12 at a 5K/multi-million-visit bar. The cohort:

99 Nights in the Forest (co-op survival, 14.15M all-time peak) · Scary Shawarma Kiosk: the ANOMALY
(191,737) · Road-Side Shawarma (76,748, **solo**) · Terminal 13: Not Human (36,389) · Scary
Grocery: The Night Shift (13,243) · Animal Hospital (Anomaly) (~286K) · Home Alone: Anomalies
(29,930) · Verity (38,879) · Scream And Run (58,614).

**Common traits:** repeatable systems over finite stories; social by default; a stream-readable
one-sentence hook ("survive 99 nights", "spot the anomalous customer"); fast content cadence —
Roblox recommends small updates every **2–4 weeks**, larger every **2–3 months** for D30; borrowed
schemas (Backrooms/DOORS traversal, DBD asymmetry, *Exit 8*-style anomaly recognition) that lower
learning cost but create clone and differentiation risk.

### Moderation

Fear is **not** banned and moderate fear need not be Restricted.

| Label | Horror allowance | Consequence |
|---|---|---|
| Minimal | mild violence, light unrealistic blood | broadest reach |
| Mild | repeated mild violence, heavy unrealistic blood, mild fear | reduced by parental settings |
| Moderate | moderate violence, light realistic blood, **moderate fear** | eligible for Roblox Select 9–15 and 16+ |
| Restricted | strong violence, heavy realistic blood, mature themes | **age-verified 18+ only** |

Prohibited at every level: extreme real-world gore, animal torture, war-crime glorification,
real-world mass shootings/terrorism, and suicide/self-harm depiction including methods. Promotional
material for Restricted experiences must itself be all-ages suitable.

The constraint is **market-access compression, not a ban**: realism and intensity progressively
narrow eligibility.

## My Take

**It dissolves the risk I logged yesterday and I had the metric wrong.** The previous note claimed
successful Roblox horror runs 45–90 minutes and treated that as the largest threat to a short-run
design. That figure was run-*completion* time from a listicle, not average playtime. Actual
telemetry puts long-form at ~13 minutes against short/rules at 8–11. The conflict with the
platform's short-loop signal largely evaporates — and the lesson is the one
[representation-shapes-the-solution](../concepts/representation-shapes-the-solution.md) states:
the number I reached for determined the risk I saw, and it was the wrong number.

**It replaces that risk with a harder one. Zero strictly solo titles in the top 30.** Solo-capable
games are 63% of the sample and 23% of CCU. This is the single most important finding for a
solo-only design, and the report is honest that it is correlational — but the mechanism it
proposes is credible and matches
[compulsion-vs-craft](../concepts/compulsion-vs-craft.md): social play is itself a retention
mechanism. Friends are a reason to return on day 20 that a loop does not have to supply.

**The counter-evidence is precisely our shape.** *Road-Side Shawarma* — solo, rules-based,
score-chasing, instant failure on a rule break — peaked at 76,748. Solo is rare there, not
impossible, and the one that worked did so by being a **legible job with rules** rather than a
narrative.

**The anomaly/rules genre is the dominant breakout pattern and it is crowded.** Six of the nine
verified breakouts are "ordinary job plus anomaly/rules" loops. That is the Attractor Zone's
premise — an ordinary person, a rule, you got exactly what you reached for — already running as
the hottest genre on the platform. Both an enormous validation and a warning: it has its own wiki,
its own clone controversy, and entering it means differentiating inside a pattern rather than
introducing one.

**Our 0.3 D1 floor is probably wrong by a factor of two.** 20% D1 came from mobile-game
benchmarks. GameAnalytics puts Roblox D1 median at 10.3%. If that is the right reference, 20% is a
top-decile outcome being used as a "not broken" line — exactly the error
[metrics-trap](../concepts/metrics-trap.md) warns about, made in the direction of setting a target
we would read as failure.

**Moderation is unexpectedly good news for the register.** Goosebumps/Twilight Zone horror is
implication, dread and reversal rather than gore. That sits at Mild/Moderate, keeps Roblox Select
9–15 eligibility, and avoids the 18+ compression. The chosen tone is the one that costs no reach —
which is fortunate rather than clever, since it was chosen before this was known.

**And the update cadence is a number for 0.9.** Roblox recommends small updates every 2–4 weeks for
D30. That is the anthology's episode cadence, supplied by the platform rather than guessed.

## Cross-Reference Checklist

- [roblox-horror-and-90s-anthology-structure.md](roblox-horror-and-90s-anthology-structure.md) —
  **corrects its session-length claim**; structural material there stands
- [The Metrics Trap](../concepts/metrics-trap.md) — the D1 floor error, and the instruction not to
  reconcile the four retention datasets
- [Representation Shapes the Solution](../concepts/representation-shapes-the-solution.md) — the
  wrong metric produced the wrong risk
- [Compulsion vs Craft](../concepts/compulsion-vs-craft.md) — co-op as a retention mechanism the
  craft list does not contain
- [Comprehension Floor](../concepts/comprehension-floor.md) — "stream-readable one-sentence hook"
  is the floor stated as a growth requirement

## Project Connection

Rewrites 0.3 and adds a solo risk to
[constraint-sheet.md](../projects/basic-game/constraint-sheet.md); supplies the episode cadence for
0.9; clears the register on moderation grounds.

## Uncertainty

- The 30-game universe is a curated tracker, not a census; the horror boundary is contested and
  Roblox has no official horror genre.
- CCU is a point-in-time snapshot, not sustained; "sustain 1K+" is unproven platform-wide.
- Average playtime is not median session length and no source exposes a session distribution.
- The solo finding is correlational. No causal test is available.
- All four retention datasets disagree and the report declines to reconcile them. Nothing here
  establishes a Roblox horror retention baseline.
- Launch cohort is a lower bound; creation dates can be placeholders and universes get replaced or
  relisted.
