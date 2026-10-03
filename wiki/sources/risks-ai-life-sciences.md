---
type: article
title: "Risks and Limitations of AI in the Life Sciences"
url: https://www.answer.ai/posts/2026-03-17-risks-life-sciences/
author: Rachel Thomas
published: 2026-03-17
ingested: 2026-04-13
tags: [ai, ml, biology, life-sciences, ethics, data]
concepts: [machine-learning-in-science]
---

## Summary

Rachel Thomas (via a Q&A with Kamayani Gupta of KAMI Think Tank) discusses where AI confidence in biology is running ahead of scientific understanding. Key themes: data quality limits model quality, scale can entrench bias, the incentive structure rewards exciting AI results and punishes error-checking, and domain experts must be integrated throughout the pipeline — not just at the end.

## Key Points

- The AlphaFold success story required decades of curated data (PDB since the 1970s, CASP since the 1990s) — yet funding for these foundational programs nearly ended.
- A published Nature Communications paper using 22M enzymes was found to have hundreds of errors by a microbiologist (Dr. Valérie de Crécy-Lagard) who had studied one enzyme for a decade. 135 "novel" enzymes were already in UniProt — data leakage. Getting a rebuttal published was extremely difficult.
- "Everyone Wants to Do the Model Work, Nobody Wants to Do the Data Work" — practitioners across three continents found data quality systematically neglected.
- The Zoe COVID app (originally a diet tracker) was repurposed for COVID tracking with no ability to log neurological or long-term symptoms, yet became a dataset for long COVID research. Scale didn't help; the design was wrong.
- Self-reinforcing loops: underdiagnosed diseases → incomplete data → models that predict the disease is rarer → further underdiagnosis (e.g., lupus, average 6-8 year diagnosis delay).
- Arijit Chakravarty's concept of "frankencells": AI encourages assembling pathways from different papers that would never all occur in a single cell.
- Timnit Gebru's "Data Sheets for Datasets" approach — being explicit about what data was collected, its constraints, and where it shouldn't be applied — is the right model.
- Go slow to go far: continue investing in bench science and causal mechanism research; current AI is fuzzy interpolation between existing data points.

## Quotes

> "The type and quality of data really sets limits on the quality of results."

> "People often think data is objective truth, but it's constructed through a series of decisions that really matter."

> "We still need research where new paradigms or different causal mechanisms are required."

## My Take

The enzyme paper case study is a striking example of how hard it is to catch AI errors without deep domain expertise — and how much the incentive system punishes the effort of catching them. The frankencells concept is one I want to hold onto: assemblage of truths that is itself a falsehood. This pairs well with the Wet AI article and the general theme of biological complexity resisting reduction.
