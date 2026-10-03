---
type: article
title: "Copying Better: How To Acquire The Tacit Knowledge of Experts"
url: https://commoncog.com/how-to-learn-tacit-knowledge/
author: Cedric Chin
published: 2020-06-16
ingested: 2026-06-14
tags: [psychology, expertise, learning, skill-acquisition, tacit-knowledge, ndm, decision-making]
concepts: [recognition-primed-decision-making]
---

## Summary

Part 2 of Cedric Chin's tacit knowledge series. Having established that tacit knowledge exists and can't be taught through explanation, this piece introduces the Naturalistic Decision Making (NDM) toolkit — specifically Gary Klein's Recognition-Primed Decision Making (RPD) model — as a framework for understanding and acquiring expert intuition. The RPD model describes how experts pattern-match situations to prototypes in implicit memory, generating expectancies, goals, cues, and action scripts automatically. The article then derives four practical methods for acquiring tacit knowledge: expanding your prototype set, identifying when an expert has a prototype you lack, developing mental simulation ability, and using cognitive critique to get expert feedback on your recognition and simulation.

## Key Points

- NDM has three tools: Cognitive Task Analysis (CTA), the RPD model, and NDM-designed training programs.
- **RPD model**: when an expert encounters a situation, they pattern-match to a prototype in implicit memory, generating four simultaneous by-products: (1) **expectancies** — how the situation will evolve; (2) **plausible goals** — what to prioritize; (3) **relevant cues** — what to pay attention to; (4) **action script** — what to do. All of this is implicit, which is why experts say "it just felt right."
- When no prototype matches, the expert falls back to recognition: gathers more info, constructs a narrative, tries to match a different prototype.
- Action selection is **satisficing**, not optimizing: the expert mentally simulates each candidate action one at a time, picks the first one that passes, rather than comparing all options and selecting the best.
- Satisficing dominates under time pressure, dynamic conditions, and with experienced practitioners. Comparative evaluation happens when you must justify decisions to others or when the situation is computationally complex.
- **Four acquisition levers**:
  1. Systematically expand the set of prototypes you have (seek unfamiliar situations, use scenario-based training like NDM practitioners, not lecture-style).
  2. Identify when a practitioner has a prototype you don't — the diagnostic: they say "it just felt right" where you would have compared options. Then ask about cues, expectancies, goals, and actions.
  3. Get better at mental simulation (identify your decision requirements, practice them, get feedback so your simulations match reality).
  4. Get expert feedback on recognition and simulation via cognitive critique: narrate past events linearly as you experienced them (never revealing what you learned later), compare your cues/expectancies/actions against the expert's.
- Toyota Production System example: competitors who poached TPS experts still couldn't replicate Toyota's system — the tacit knowledge was organizational, embedded in culture, not just individual expertise.
- NDM is "closer to anthropology than psychology" — field research, not controlled experiments. Klein defends this by results: methods work, training programs show measurable improvements.

## Quotes

> "When an expert says 'it just felt right', what they mean to say is that they recognised the problem as an example of a prototype in their heads, which generated the four by-products; this implicit memory operation happens so quickly that they cannot verbalise how they came up with it."

> "RPD is useful because it gives us a model with which to understand human expertise. When you apprentice under someone, what's actually happening is that you are building up prototypes in your implicit memory — that is, you are identifying cues, learning plausible goals, internalising action scripts, and storing expectancies."

> "Don't get me wrong: this will not be a good extraction of their tacit knowledge, because expert intuition is difficult to explicate, and CTA is itself difficult. But it's surprisingly useful to just ask questions along these lines — at the very least, the hints that you'll get out of it will be marginally better than naive copying."

## My Take

RPD is the most mechanistic model of expert intuition I've encountered — and it maps directly onto how large language models work, which makes it a useful lens for both. LLMs are prototype-matching machines at scale: they absorb millions of expert decisions and build implicit representations (weights) that fire when a situation pattern-matches to something in training distribution. The four by-products (expectancies, goals, cues, action scripts) are what get absorbed across those decisions. The key structural difference: LLMs don't do the sequential satisficing simulation that Klein describes — they generate statistically likely outputs rather than running explicit forward simulations. Systems with chain-of-thought or internal reasoning come closer to simulating the RPD loop.

For NPC design: RPD suggests what expert NPC behavior should look like. A merchant NPC with genuine expertise wouldn't compare every trade offer analytically — it would immediately flag suspicious offers from pattern recognition (cues), form expectancies about what the player is trying to do, and satisfice on the first plausible response. That's harder to produce than a rule list but far more natural-feeling. The quest generator sits at a different level — it's closer to CTA: it surfaces the cues (game state), expectancies (player history), and goals (NPC stakes) that let the LLM generate an appropriate action. The RPD model is the cognitive architecture; the quest system is an implementation of it.

The cognitive critique method is directly transferable to playtesting: walk through a quest session linearly as the player experienced it, compare cue recognition and decision expectations between designer and player. This would surface mismatches between designed intent and actual player prototypes.

Pair with: [tacit-knowledge-is-real-chin.md](tacit-knowledge-is-real-chin.md) (Part 1 — what tacit knowledge is and why it matters).
