---
type: article
title: "Exploring persistence in gaming: The role of self-determination and social identity"
url: https://www.sciencedirect.com/science/article/abs/pii/S0747563214002684
author: Jeroen Jansz et al., Computers in Human Behavior (2014), DOI 10.1016/j.chb.2014.04.047
published: 2014
ingested: 2026-05-19
tags: [psychology, motivation, game-design, loop, compulsion, identity]
concepts:
  - ../concepts/self-determination-theory.md
  - ../concepts/social-identity-theory.md
  - ../concepts/intrinsic-motivation.md
---

## Summary

A large survey study (N = 7252, recruited via IGN.com and Gamer.nl) attacking "the paradox of gaming": why do players keep going when intermediate rewards repeatedly fail to arrive — when, to an outsider, persistent play looks more like labor than fun? The authors explain persistence with two stacked frameworks. Self-Determination Theory (Deci & Ryan) supplies the motivational deep structure: games that satisfy autonomy, competence, and relatedness produce intrinsic motivation, which sustains effort through frustration. Social Identity Theory (Tajfel & Turner) supplies the contextual modifier: the authors introduce **Gamer Identity Strength (GIS)** and show that how strongly a person identifies *as a gamer* changes their motivational structure and how persistently they play. Only the abstract, method, and section snippets are accessible in this clipping; full results are paywalled.

## Key Points

- **The persistence paradox:** unlike film/TV, a game only delivers content if the player keeps supplying active input. When intermediate rewards stop, frustration is inevitable — yet some players quit and some try again. The difference is the research target.
- Persistence is explained by **need satisfaction**, not reward schedules: autonomy, competence, relatedness (measured via Rigby's Player Experience of Need Satisfaction / PENS instrument).
- **Gamer Identity Strength (GIS):** identifying as a gamer is a salient social identity that modulates the motivational structure. Stronger gamer identity → different (and more persistent) motivational profile.
- Persistence is therefore *both* an internal-need phenomenon and a social-identity phenomenon. Neither alone explains it.
- Sample skew worth recording: ~95% male, 56% US, mean age ~20.5, mean ~18 hrs/week. Findings are about a self-selected core-gamer population.

## Quotes

> "Gamers tend to persist with playing even when they are not immediately sufficiently rewarded." (the paradox the paper exists to explain)

> Persistent play "looks more like labor than gaming" to the outside observer.

## My Take

This is the academic backbone under several softer wiki sources. The Gamestar nostalgia piece, the Fandom self-expression stat, and the "why players recommend games" synthesis all gesture at identity; this paper names the mechanism (SDT need satisfaction × social-identity strength) and measures it. The key transferable insight for the project is that **persistence is not bought with rewards — it is produced by need satisfaction and amplified by identity**. That directly contradicts a metrics/retention-hook design philosophy and confirms the overjustification logic already in [[intrinsic-motivation]]: bolting extrinsic incentives onto a need-satisfying loop does not increase persistence and can corrode it. The GIS finding is the more novel hook: persistence is partly a function of *who the player thinks they are*, not just what the game does — which means an AI that participates in or reflects the player's identity could be a persistence lever no reward schedule can match. Paywall limits this to abstract-level claims; flagged as a candidate for a fuller open-access replication to ingest.

## Cross-Reference Checklist

**On AI in games** — Misses all four; no AI content. Pure player-motivation psychology.
**On player-AI relationship** — Misses directly. Indirect: relatedness as a core need implies an AI that satisfies relatedness could anchor persistence (building/coexisting).
**On design and feel** — Strong hit on the compulsive-loop question (Q6): names the actual pull mechanism behind non-reward persistence (need satisfaction + identity). Partial hit on emotional-investment-without-stakes (Q7) via relatedness/identity. Misses 2D-specific affordance (Q9).

## Project Connection

Directly relevant to the meta-loop design of the AI artifact testbed: if users must run failure-pattern sessions repeatedly without paid incentive, the loop has to satisfy competence (visible mastery of the failure space) and autonomy (genuine control), and ideally attach to an identity ("I'm someone who can read these systems"). The paper says this is what makes labor-like activity persist. See [[self-determination-theory]], [[social-identity-theory]], [[intrinsic-motivation]].
