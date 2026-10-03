---
type: article
title: "Why Europe doesn't have a Tesla"
url: https://worksinprogress.co/issue/why-europe-doesnt-have-a-tesla/
author: Works in Progress (wip-admin byline; attribution unconfirmed)
published: 2026-02-17
ingested: 2026-08-30
tags: [economics, innovation, labor, regulation, engineering-culture]
concepts:
  - ../concepts/failure-cost-asymmetry.md
---

## Summary

An essay arguing that Europe's innovation gap with the US (specifically the absence of
a European Tesla/Waymo-scale bet) is best explained not by research spending, energy
costs, or taxes (all of which are comparable to or higher in California, which still
produced Tesla and Waymo) but by the cost of failure: European labor law makes laying
off workers far more expensive than in the US, which makes companies systematically
avoid creating jobs in innovative-but-risky areas rather than avoiding hiring
altogether. Since experimentation inherently produces more discontinued jobs than
stable business lines, high severance costs act as a structural tax specifically on
innovation, not on employment overall (Euro-area and US employment rates are nearly
identical: ~71 vs ~72 per 100 working-age people). The piece walks through concrete
mechanisms — Germany's Sozialauswahl (mandatory seniority/need-based ranking for who
gets laid off), works councils with approval power over layoffs, France's regulator-
reviewed collective-dismissal process, court power to reclassify "unjustified" layoffs
as fines — and a comparative cost estimate: a layoff costs roughly 7 months' salary
per employee in the US versus 31 (Germany), 38 (France), 52 (Italy), 62 (Spain) months.
Case studies: Audi's Q8 E-Tron plant closure cost more in severance (€610M) than the
value of the assets being written off; Volkswagen's decades-long lifetime-employment
norm contributed to its late, expensive, and initially failed EV/software pivot; Nokia
had touchscreen/smartphone prototypes years before the iPhone but avoided the risk
given its own restructuring costs. The essay's proposed fix is not deregulation but
"flexicurity" — Denmark's model of near-at-will firing paired with generous
state-funded unemployment insurance and retraining (2% of GDP), which shifts the cost
of failure from the firm to a social insurance pool, preserving worker income security
without taxing the firm's willingness to experiment.

## Key Points

- The core mechanism is a failure-cost asymmetry, not an overall employment-cost or
  hiring asymmetry: European firms hire about as much as American firms, but hiring is
  displaced away from experimental/innovative roles because those roles are more likely
  to be later discontinued, and discontinuation is what's expensive.
- Concrete cost multiple: restructuring costs ~7 months' salary/employee in the US vs.
  31–62 months across major European economies (Coste & Coatanlem estimate).
- Small/flexible European economies (Denmark, Switzerland, Austria) are simultaneously
  Europe's most innovative (Novo Nordisk, Roche, Nestlé, Novartis) and its most
  labor-flexible — the paper reads this as evidence the causal story runs through labor
  flexibility, not some other confound.
- Regulatory exemptions for small firms create a "growth ceiling" effect: rules
  designed to protect workers at scale become a disincentive for a successful startup
  to keep growing past the threshold that triggers them (e.g., works councils at 5–50
  employees).
- Historical framing: Europe was innovation-leading for over a century before WWII
  (De Dion-Bouton pivoting from steam to petrol engines in the 1890s is the essay's own
  "Tesla" precedent), so the labor-market explanation is presented as institutional and
  reversible, not cultural or permanent.
- Proposed fix (flexicurity) explicitly reallocates failure cost from firm to state
  insurance pool rather than removing it — workers keep income protection, firms regain
  the ability to experiment cheaply.

**Source quality note:** author byline is `wip-admin`, a placeholder — attribution to
Works in Progress' editorial staff specifically is unconfirmed, consistent with a
pattern already flagged in this wiki's other *Works in Progress* ingests (see
[Beauty In My Backyard](beauty-in-my-backyard-hughes.md), [Urban expansion in the age of
liberalism](urban-expansion-age-of-liberalism.md)).

## My Take

The mechanism here — that the *cost of discontinuing* a bet, not the cost of making
one, is what actually governs an organization's willingness to experiment — is a
sharper and more general version of "kill criteria" thinking than the term usually
gets credit for, and it applies directly to AI project and product management, not
just labor markets. A team that can cheaply kill a failed model, a failed fine-tune, or
a failed agent deployment (in compute cost, reputational cost, or sunk organizational
commitment) will run more, riskier bets than a team where killing a bad initiative
requires re-litigating a public roadmap commitment or absorbing large sunk
infrastructure cost — this is functionally the same asymmetry as European severance
law, just denominated in compute-hours and credibility instead of months of salary.
It's also a useful frame for AI agent architecture itself: an agent design where
abandoning a bad plan/subtask is expensive (large context to discard, expensive re-
planning, a user-visible "failure" event) will structurally under-explore compared to
one where abandoning a bad path is cheap — the same logic that predicts European firms
avoid innovative hiring predicts an agent harness with high "exploration exit costs"
will default to safe, incremental actions over ambitious ones, independent of the
model's actual capability.
