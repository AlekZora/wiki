---
type: article
title: "The Rise of 'Wet' Artificial Intelligence"
url: https://proto.life/2023/11/perspective-the-rise-of-wet-artificial-intelligence/
author: Aneil Mallavarapu
published: 2023-11-16
ingested: 2026-04-12
tags: [ai, ml, biology, synthetic-biology, biotech, drug-discovery, philosophy]
concepts: [wet-ai, biotechnology]
---

## Summary

"Wet AI" is a term for small, specialized AI models trained on purposefully generated proprietary experimental (wet lab) data, as opposed to "dry" AI like ChatGPT trained on large public datasets. The author argues wet AI will have enormous impact and durable competitive moats: training data is proprietary, models are tiny (~50MB vs. 570GB for GPT), cheap to train, and purpose-built. The flagship example is Unnatural Products (UNP), which trains generative AI on screening data for peptide macrocycles to explore vast chemical spaces that wet lab alone couldn't reach—breaking Lipinski's Rule of 5 and creating drug candidates that both bind tightly and penetrate cell membranes.

## Key Points

- AI in biology has a data problem: unlike LLMs scraping the internet, biological AI can't draw on pre-existing public data—it must be purposefully generated. AlphaFold, trained on the Protein Data Bank, has known gaps (protein-protein interactions, membrane proteins, conformational changes).
- "Wet AI" = small, private, special-purpose models trained on wet lab data, contrasted with "dry AI" (large, general, public-data-trained). Wet AI models are ~1000x smaller but have enormous commercial value.
- Competitive moat: wet AI companies own their training data, making them harder to replicate than LLM companies whose data is public (c.f. LLaMA replicating GPT-4 functionality using open data).
- Macrocyclic peptides as a case study: natural ring-structured short proteins with drug-like properties (cell permeability, target specificity). Cyclosporine is the canonical example.
- UNP's approach: build large libraries of macrocycles with "unnatural" amino acids (~100,000 variants), screen a small fraction, train AI on screening results, then let AI suggest candidates from an astronomically large chemical space (10^50 molecules). Result: compounds that break Lipinski's rules.
- Analogy: "Wet AI uses experiments to get you to the ballpark and AI to get you to the seat in the stadium."
- Merck spent 10 years (with large team) to design one macrocyclic peptide. UNP-style approaches can find thousands with better properties in ~3 years with a smaller team.
- Wet AI will also drive large public data collection efforts analogous to the Human Genome Project—e.g., the Human Immunome Project, Mark Murcko's "avoidome" concept.
- Future directions: health, synthetic biology, bioeconomy, turning molecular world into programmable medium.

## Quotes

> "In the new AI-driven era, research efforts must be purposefully organized to generate the right data for AI models."

> "Wet AI uses experiments to get you to the ballpark and AI to get you to the seat in the stadium."

## My Take

The Lipinski Rule of 5 story is a perfect example of a paradigm constraint: a heuristic from one era becoming a mental prison in the next. AI-guided synthesis essentially circumvents the practical limit (you can't screen 10^50 molecules) by learning patterns from the manageable fraction. The proprietary moat argument is compelling—wet AI companies don't face the commoditization pressure of LLM companies because their data is irreplaceable. Worth connecting to the Song of the Cell (Mukherjee) for the biology context and to Range (Epstein) for the generalist/specialist dynamics in drug discovery teams.
