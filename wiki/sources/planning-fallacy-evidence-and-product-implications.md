---
type: article
title: "Planning Fallacy: Evidence and Product Implications"
url:
author: Unattributed AI deep-research report (10 references; same format as the goal-achievement report, likely Perplexity)
published:
ingested: 2026-10-01
tags: [psychology, behavior, productivity, systems, ai, agents, design]
concepts:
  - ../concepts/planning-fallacy.md
---

Supplied by the user to fill the planning-fallacy gap in the
[Goal Map synthesis](../answers/goal-map-wiki-synthesis.md). No URL, author or date. Its central
empirical claim was checked against the primary paper,
[Buehler, Griffin & Ross 1994](buehler-griffin-ross-1994-planning-fallacy.md), and holds.

## Summary

A short brief on the planning fallacy, the tendency to predict your own tasks will finish
sooner than they do, even when similar past tasks ran late. It traces the idea to Kahneman and
Tversky's "inside view": people simulate how *this* plan should go and ignore how comparable
cases actually went. The causes are cognitive, motivational and social. The fixes it presents
are **reference-class forecasting** (start from the distribution of comparable past outcomes),
**task segmentation** (estimating subtasks and summing gives longer, less biased estimates), and
explicitly linking past experience to the current forecast. The product section turns this into
a background calibration system. Store planned vs. actual results, show the user's own
historical range next to their gut estimate, give ranges rather than single dates, separate
active effort from elapsed time, and recalculate without blame when reality diverges.

## Key Points

- **Mechanisms:** inside view, neglect of past experience (overruns treated as special cases), motivated reasoning, incomplete decomposition (setup, coordination, revision and recovery left out), single-point estimates that hide variance.
- **Not every overrun is the fallacy:** scope change, dependencies, strategic misrepresentation, bad data and genuinely unusual events produce the same symptoms.
- **Reference-class forecasting** works if the reference class is truly comparable. Narrowing the class improves similarity but leaves too few cases. The brief cites a 2026 critical review (Cantarelli et al.), not checked here.
- **Segmentation** lengthens estimates and reduces underestimation, but heavy decomposition costs planning effort and still misses unknown work. Cited to a *Memory & Cognition* paper (Forsyth & Burt 2008), not checked here.
- **Seven-step procedure:** define the unit; retrieve comparable cases (the user's own first, population data second); start from the outside view (median and range); decompose; adjust only for documented differences; express uncertainty; record prediction and outcome.
- **Example output:** "Similar tasks took you 4–7 hours; your inside-view estimate is 2.5 hours. Plan around 5 hours, with 7 hours as the safer boundary."
- **Product features:** outside-view estimate before accepting a deadline; inside/outside contrast; scope checklist; forecast ranges; calibration history; decompose only large, novel or repeatedly underestimated work; buffer at uncertain dependencies, not everywhere; non-punitive recalculation.
- **Active effort ≠ elapsed duration:** three hours of work can take five calendar days. Mixing them up blocks learning.
- **Caution:** show which past cases informed a forecast, let users exclude ones that don't compare, and lower confidence when data is sparse.

## Quotes

> "Plan from history, adjust from current evidence, and learn from every forecast error."

> "The app should separate **active effort** from **elapsed duration**."

## My Take

Useful and mostly well-grounded. The one claim I checked against its primary source holds,
with a detail the brief compresses. In Buehler et al.'s Study 4, simply **recalling** past
experience did nothing. Only *linking* the past to the current task removed the bias. The
brief's step 2, "retrieve comparable cases", reads as if retrieval were enough. The evidence
says the linking step does the work.

Two cautions:
- **The research is about tasks with hours-to-weeks timescales** (theses, assignments, household projects). Personal goals measured in months, with a sparse personal history, are where reference classes are thinnest. A new user has no history at all.
- **Reference 6 links to a Sci-Hub copy.** I didn't use it, and the vault shouldn't cite it.

**AI lens:**
- **LLMs are inside-view machines by default.** Ask one to plan a goal and it simulates the
  plan's ideal unfolding, which is the fallacy's mechanism. Unless the system supplies
  distributional data, an AI milestone generator will tend to produce plans that are
  internally coherent and too optimistic. The fix is architectural: the model proposes
  structure, and code supplies durations from recorded outcomes.
- **AI as the outside observer:** Buehler's Study 5 found that observers estimating *someone
  else's* task were not optimistic and used past experience more. An assistant can stand in that
  observer seat. Whether an LLM behaves like a human observer or inherits the user's optimism from
  the user's own framing is untested.
- **Agents have the same bias.** Agent plans routinely underestimate steps, retries and
  integration work. The "incomplete decomposition" row (setup, coordination, revision, recovery)
  is a usable checklist for agent task planning too.
- **The calibration loop** (predict, record, compare, adjust) is a
  [closed loop](../concepts/closed-loop-systems.md) on the forecaster itself, and the same
  forecast-and-check habit as [research-craft](../concepts/research-craft.md).
