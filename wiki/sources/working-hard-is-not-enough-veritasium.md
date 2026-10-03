---
type: video
title: "Working Hard Is Not Enough"
url: ""
channel: Veritasium
published: unknown
ingested: 2026-06-27
duration: unknown
tags: [mathematics, statistics, physics, systems, emergence, economics, philosophy, behavior, decision-making]
concepts: [power-laws]
---

## Summary

A Veritasium video explaining power laws from the ground up: how they differ from normal distributions, why they emerge, and what they mean for decision-making. The video moves through three casino games (additive coin flip → multiplicative returns → doubling-until-heads / St. Petersburg paradox) to build intuition for normal, lognormal, and power law distributions. It then explores self-organized criticality — the phenomenon by which certain systems (forest fires, sandpiles, earthquakes, magnets at the Curie temperature) naturally tune themselves to a critical state where influences become long-range and events of all sizes become inevitable. The conclusion is practical: knowing whether you're operating in a normal or power law domain should fundamentally change your strategy.

## Key Ideas

- Normal distributions arise from additive random effects; power laws arise when two exponentials — one growing, one decaying — combine to cancel each other out
- Pareto showed that income distributions across all European countries in the late 1800s followed the same power law, regardless of country
- The St. Petersburg paradox: a game with infinite expected value but a median payout near $1 — the distribution has no finite standard deviation
- Power laws are scale-free / fractal: zoom in and the same structure repeats at every scale
- **Self-organized criticality**: some systems don't need external tuning to reach a critical point — they drive themselves there (forest fires, sandpiles, earthquakes). Fire suppression backfires: removing small fires makes the megafire inevitable
- At criticality, local influences chain together to become effectively infinite in range — a single flip can cascade through the entire material
- **Universality**: systems in the same universality class behave identically at criticality regardless of physical details — the simplest toy model captures the real behavior
- **Preferential attachment** (Barabasi-Albert): nodes that link to well-connected pages reinforce existing leaders, producing a power law network. Explains the internet, social graphs, city populations
- In normal distribution domains: consistency is the winning strategy
- In power law domains: persistence is the winning strategy — make many bets, accept most will fail, wait for the outlier

## Timestamps

- ~0:00 — Normal distributions vs power laws, Pareto's income data
- ~mid — Three casino games: additive (normal) → multiplicative (lognormal) → doubling paradox (power law)
- ~mid — Fractals and scale-invariance; magnets at the Curie temperature
- ~mid — Self-organized criticality: forest fires simulation, Yellowstone 1988
- ~mid — Earthquakes, sandpile model, Perback's universality argument
- ~late — Preferential attachment, internet as power law network
- ~late — Practical implications: venture capital, publishing, streaming vs. restaurants and airlines
- ~end — Casper's story: one email to Veritasium changed everything

## My Take

The video's central practical claim is precise: if you are playing a power law game, hard work (consistency) is necessary but not sufficient — what matters is persistent bet-making across many independent attempts. The rare hit overwhelms everything else. This maps directly onto AI research, startup strategy, and content creation.

The AI intersection here is unusually deep. **Scaling laws for LLMs are literally power laws** — model capability (measured as loss) scales as a power function of compute and data. This is why there are no "average" frontier models; each order-of-magnitude increase in compute produces disproportionate gains. Training data token frequency follows Zipf's law, a power law — so LLMs have vastly more exposure to common concepts than rare ones, which shapes where they are fluent vs. shallow.

The Barabasi-Albert preferential attachment model describes AI market structure exactly: OpenAI accumulated early links (developers, APIs, integrations), which attracted more links, which is why the distribution of model usage is highly concentrated. This is not random luck — it is the structural outcome of any network where new entrants preferentially connect to the already-well-connected.

Most provocative: the **neural criticality hypothesis** proposes that biological (and possibly artificial) neural networks operate near a phase transition, much like magnets at the Curie temperature. This would explain why small parameter changes during training can produce sudden qualitative capability jumps — not gradual improvement but cascade events. Whether this is confirmed or not, the framing suggests that "emergent capabilities" in LLMs may be phase transitions in the self-organized criticality sense, not magic.
