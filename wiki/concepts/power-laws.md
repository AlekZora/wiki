---
type: concept
title: Power Laws
aliases: [power law distribution, Pareto distribution, fat tails, scale-free, self-organized criticality]
tags: [mathematics, statistics, systems, emergence, physics, economics, behavior, decision-making]
sources: [working-hard-is-not-enough-veritasium, power-law-mallaby]
updated: 2026-06-27
---

## Definition

A power law is a relationship of the form P(x) ∝ x^−α, where the probability of an event of size x scales as a negative power of x. Unlike normal distributions, power laws have no characteristic scale — there is no "average" event that is representative, and extreme outliers are not just possible but structurally guaranteed. The standard deviation is often infinite. Income, earthquake energy, city populations, internet link counts, and war casualties all follow power laws.

## How I Think About It

The key mental shift is recognizing which distribution governs your domain. Normal distributions arise when many small, independent, additive factors combine. Power laws arise when effects multiply (lognormal) or when two opposing exponentials conspire to cancel out. The second condition is why nature produces so many power laws: exponential growth in one dimension (earthquake energy, payout, spread of disease) often pairs with exponential decay in probability.

Self-organized criticality is the deepest mechanism. Systems like forests, sandpiles, and earthquake faults don't need to be externally tuned to a critical state — they drive themselves there. At criticality, local influences chain into global cascades; the same physical process produces events that span 10 to 10,000,000 in size. Small causes and large outcomes are not qualitatively different — the large outcomes are just the small ones that happened to hit a finger of instability.

The practical implication is the sharpest thing in the video: **in a normal distribution domain, consistency wins; in a power law domain, persistence wins**. Restaurants need to fill tables every night — consistency. Venture capital firms need one outlier to cover all losses — persistence and many bets. Knowing which game you're playing should completely restructure your strategy.

## AI Integration

- **LLM scaling laws are literally power laws.** Model capability (loss) scales as a power function of compute and training data. This means capability is not linearly proportional to investment — it explains why frontier AI labs concentrate resources into the largest possible runs rather than spreading compute across many medium-sized experiments. Small increases at the frontier produce disproportionate gains.
- **Token frequency in training data follows Zipf's law**, a power law. Common tokens appear exponentially more than rare ones. This is why LLMs are deeply fluent in everyday language but shallow in rare technical dialects, obscure languages, or specialized knowledge — the distribution of training signal is power-law distributed, not uniform.
- **AI market structure follows preferential attachment.** Models and platforms with early developer mindshare accumulate integrations and APIs, which attracts more users, which attracts more integrations. The Barabasi-Albert model predicts a power law of usage concentration — a few models capture the majority of all inference. This is structural, not accidental.
- **Emergent capabilities as phase transitions.** The neural criticality hypothesis proposes that trained neural networks operate near a critical point, analogous to a magnet at its Curie temperature. This would explain why capability "emerges" suddenly at scale rather than improving gradually — the model crosses a phase boundary, and influences that were local become long-range. Capability jumps in LLMs may be cascade events, not smooth learning curves.
- **AI research portfolio follows power law logic.** Most papers, experiments, and models produce incremental gains or fail. A handful — Attention Is All You Need, AlphaFold, GPT-3 — restructure the entire field. AI research strategy that tries to optimize every experiment for average return misunderstands the game. The field advances through outliers.
- **VC funding is the selection pressure that built modern AI.** Mallaby's *The Power Law* documents the mechanism: Horsley Bridge data (1985–2014) shows 5% of deployed VC capital generated 60% of returns; Y Combinator found 75% of its gains came from 2 of 280 bets. Because returns are so skewed, VCs who back incremental ideas are rationally guaranteed to underperform. The institution is structurally optimized to fund the most improbable, ambitious bets — which is exactly how OpenAI, Anthropic, and DeepMind got funded. The VC power law selects for grand slams, not doubles, and AI capabilities are the grandest slam currently available.
- **Outsider advantage as power law strategy.** In a power law domain, incremental gains from experts produce normal-distribution returns; radical breakthroughs from outsiders produce the grand slams. Khosla's principle — "I don't want a healthcare CEO for a healthcare company" — is a direct application: domain experts optimize within the distribution, outsiders can shift it. AI-enabled outsiders (people who understand AI but enter a new domain without prior assumptions) are the current instantiation of this strategy.
- **Fire suppression analogy for AI safety.** Suppressing small failures in AI systems (patching every jailbreak, blocking every misuse) may suppress useful small-scale feedback, allowing larger structural failure modes to accumulate — the Yellowstone megafire dynamic. Controlled exposure to failure modes may be safer than total suppression.
- **Self-organized criticality in training dynamics.** It is possible that large-scale training self-organizes toward a critical regime, where the model is maximally sensitive to new information — the state most useful for generalization. This is speculative but testable.

## Related Concepts

- [[self-organized-criticality]] — the mechanism by which systems tune themselves to critical points
- [[emergence]] — power laws are a signature of emergent behavior across scales
- [[scaling-laws]] — LLM scaling laws as a specific AI instance of power law relationships
- [[preferential-attachment]] — the network growth mechanism that produces power law degree distributions
- [[game-theory]] — the "which game are you playing?" framing connects to game-theoretic payoff structures
- [[startup-idea-evaluation]] — startup portfolio strategy is a direct application of power law thinking
- [Leverage](leverage.md) — the mechanism that makes a fat-tail outcome reachable by one person: power laws describe the distribution of payoffs, leverage describes how a single action gets exposure to it

## Open Questions

- Do LLM capability phase transitions match the universality classes seen in physical systems, or is the analogy superficial?
- Is there an equivalent of "fire suppression" in AI safety policy — interventions that reduce small failures but make catastrophic failures more likely?
- Can preferential attachment be deliberately exploited early (accumulating the first links) to ensure a project lands in the power law's fat tail rather than its base?
- What distinguishes the ~6% of bets that produce the outlier returns? Is there signal or is it maximally unpredictable as the video claims?

## Project Connections

The Side Quest AI project operates in a power law domain: most combinations of NPC state + player history + template will generate forgettable quests. The "disorienting recognition" experience goal is the outlier event — it cannot be engineered into every quest, only made probable enough that it occurs. This reframes the design target: not "make every quest good," but "make the conditions right for the occasional quest that changes how the player reads the game."
