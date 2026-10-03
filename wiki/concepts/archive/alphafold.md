---
type: concept
title: AlphaFold
aliases: [AlphaFold 2, AlphaFold 3]
tags: [ai, ml, hardware]
sources: [hassabis-yc.md, deepmind-ceo-interview.md]
updated: 2026-04-30
---

## Definition

DeepMind's AI system for predicting the 3D structure of proteins from their amino acid sequences — a problem that had resisted solution for 50 years. AlphaFold 2 effectively solved it in 2020; AlphaFold 3 extends the capability to a broader range of biomolecules. It won Hassabis a Nobel Prize in Chemistry in 2024. Beyond the protein problem itself, Hassabis treats AlphaFold as the proof-of-concept and template for using AI to crack grand challenges in science.

## How I Think About It

AlphaFold matters twice: once as a scientific result (protein structures now predictable at scale, directly enabling drug discovery) and once as a template for how to identify tractable AI-for-science problems. The template Hassabis extracts from it is specific: (1) a massive combinatorial search space no brute force can cover, (2) a clear objective function you can hill-climb against, (3) sufficient in-distribution data or a simulator to train on. Drug discovery, materials science, and mathematics all fit this pattern. It's a useful filter for deciding which scientific domains AI will crack next and which ones it won't — if you can't identify all three components, the problem probably isn't ready.

## Related Concepts

- [artificial-general-intelligence](./artificial-general-intelligence.md)

## Open Questions

- Which scientific domains satisfy all three AlphaFold conditions and haven't been tackled yet?
- How far does AlphaFold 3 (broad biomolecules) get toward the virtual cell Hassabis describes as ~10 years away?
- What is the "virtual nucleus" milestone that DeepMind is treating as the near-term target before a full virtual cell?
- Does the AlphaFold template generalize to mathematics — and if so, what is the "objective function" for mathematical discovery?
