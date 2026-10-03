---
type: concept
title: Wet AI
aliases: [wet artificial intelligence, wet lab AI, biology AI]
tags: [ai, ml, biology, synthetic-biology, drug-discovery, biotech]
sources: [sources/wet-ai-mallavarapu.md, sources/biotechnology-wikipedia.md]
updated: 2026-04-12
---

## Definition

Wet AI refers to small, special-purpose AI models trained on data generated intentionally by wet lab (physical/biological) experiments, as opposed to "dry AI" (large general-purpose models like LLMs trained on pre-existing public data). The defining feature is the feedback loop: AI predictions guide which experiments to run, experiments generate new proprietary data, new data trains better models.

## How I Think About It

The key insight is about the nature of the competitive moat. LLM companies are racing on public data—anyone can scrape the internet and train a model. Wet AI companies generate their own training data through experiments, so their moat is intrinsically proprietary and hard to replicate. The models themselves are tiny (~50MB vs. hundreds of GB for an LLM), but they encode enormous value because the data behind them is irreplaceable.

The chemical space intuition is striking: a macrocycle library of 10 amino acids from 100,000 variants contains 10^50 candidates—more than atoms in Earth. You can physically screen maybe billions. AI trained on those billions learns patterns that let it navigate the rest of the space without synthesizing. This is the core bet: AI gets you from "the ballpark" (experiments) to "the right seat" (the optimal candidate).

It also reflects a broader shift: from opportunistic data collection (databases accumulating as a side effect of research) to purposefully designed experiments optimized to teach an AI what it needs to know.

## Related Concepts

- [Biotechnology](biotechnology.md)
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — analogous proprietary-data moat dynamics in AI software
- [Creativity](creativity.md) — AI-guided exploration of vast design spaces

## Open Questions

- How does the wet AI approach handle distribution shift when moving from in vitro to in vivo?
- Will large foundation models (trained on public biology data) eventually outcompete proprietary small models, or is the data gap insurmountable?
- What happens when wet AI becomes commoditized—does the moat shift to the biological experiment infrastructure itself?

## Game Design Vector

**Mechanic:** The player runs a wet AI loop: design experiments (tasks for the AI to predict), observe the AI's predictions, run the experiments, generate data, feed data back to train a better model. The competitive moat is the proprietary data the player generates — not scraped from the world but designed to teach the AI what it needs to know. The chemical space intuition applies: the game world has a candidate space of 10^50 items; the player can directly explore only billions; the AI trained on those billions must navigate the rest through learned patterns.

**2D Expression:** In 2D, the candidate space is the plane — visually vast, mostly unexplored. The player's experiments are the locations they can actually visit; the AI's predictions are the routes it recommends for exploration. Proprietary data the player has generated appears as explored territory; the AI's small, high-value model is the inference engine that navigates the unexplored territory from the patterns in the explored one. The moat is visible as the growing ratio of explored to unexplored territory.

**Addictive Loop:** The player returns because the last session's experimental data has improved the AI's predictions, and the improved predictions reveal new promising territories. The compulsive loop is the wet AI feedback circuit: design experiment → generate data → train better model → better predictions → design next experiment. The moat deepens with each iteration — the player's experimental data is irreplaceable and grows more valuable over time.

**Novel Angle:** The shift from opportunistic data collection to purposefully designed experiments optimized to teach the AI — exploration and curriculum design as the same act. The player is doing science in the service of AI development, not in the service of discovery. What to run next is determined not by the player's curiosity but by what the AI most needs to learn to navigate the unexplored space.

## AI Integration Vector

**Player-AI Relationship:** The player designs experiments; the AI predicts which experiments will be most informative. The relationship is bidirectional: the player shapes the AI's training data; the AI shapes the player's experimental agenda. Neither is in control — both are constrained by the proprietary data loop they are jointly running. The player's domain judgment and the AI's pattern recognition are complementary; neither is sufficient alone.

**AI as Evolving System:** The AI is a small, special-purpose model that grows more capable with each round of experimental data. Development is not architectural — the model stays compact — but representational: training data progressively fills in the AI's model of the candidate space. The AI develops by learning patterns that let it navigate territory it has never directly observed. The development record is the experimental history.

**AI as Development Environment:** The feedback loop (predict → experiment → data → train) is the development environment. The player designs which experiments to run — the same act as designing the training curriculum. The development environment is a laboratory: the player is a scientist whose experimental choices determine what the AI can learn.

**Persistence:** The proprietary data generated by each session persists as the AI's irreplaceable training set. Unlike knowledge derived from public sources, this data cannot be replicated by a competitor starting from scratch. Persistence is the accumulated experimental record — every data point is a permanent addition to the AI's development history. The moat deepens with each session because the persistence is genuinely proprietary and non-reproducible.
