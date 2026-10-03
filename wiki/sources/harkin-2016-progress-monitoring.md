---
type: article
title: "Does Monitoring Goal Progress Promote Goal Attainment? A Meta-Analysis of the Experimental Evidence"
url: https://eprints.whiterose.ac.uk/id/eprint/87431/
author: Benjamin Harkin, Thomas L. Webb, Betty P. I. Chang, et al.
published: 2016
ingested: 2026-10-01
tags: [psychology, behavior, motivation, systems, ai, agents, medicine]
concepts:
  - ../concepts/closed-loop-systems.md
  - ../concepts/metrics-trap.md
---

*Psychological Bulletin* (2016). Ingested from the authors' accepted version on White Rose
Research Online (`raw/articles/Harkin et al 2016 - …(accepted version).pdf`). Page numbers
refer to that manuscript.

## Summary

Control theory says monitoring progress is what sits between setting a goal and reaching it. This
meta-analysis of 138 randomized studies (N = 19,951) tested that claim. Interventions that
prompted progress monitoring massively increased how often people monitored (d = 1.98). They also
improved goal attainment (d = 0.40), about the same as the effect of goal intentions themselves.
Changes in monitoring frequency **mediated** the effect. Monitoring worked better when the
results were **reported or made public** and when they were **physically recorded**. It also
mattered *what* was monitored. Monitoring behaviour changed behaviour; monitoring outcomes
changed outcomes. Almost all studies were about health. Only one tracked a non-health goal.

## Key Points

- **Effects:** monitoring frequency d = 1.98; goal attainment d = 0.40 (95% CI 0.32–0.48). Monitoring frequency mediated the effect, though only at study level (p. 41).
- **Match the monitor to the target** (p. 33): monitoring *behaviour* changed behaviour but not outcomes, and monitoring *outcomes* changed outcomes but not behaviour. The authors' reading is that outcome monitoring lets people switch means, while behaviour monitoring commits them to one means.
- **Public > private, recorded > not** (pp. 34–35). They suggest public commitment, accountability, self-presentation, or experimenter demand. On recording: "it is not enough merely to monitor progress — the person must also face up to what the information shows." Recording makes it harder to ignore.
- **The ostrich problem** (p. 31): people avoid information about their own progress, especially when they suspect it's bad. Self-protective motives inhibit monitoring (pp. 42–43).
- **Combinations help** (p. 37): effects were larger when monitoring came with goal setting, action planning, and immediate feedback on behaviour.
- **Reference point** (p. 35): comparing against a past state vs. a desired future state worked equally well. They raise an untested hypothesis (Bonezzi et al.): early on people ask "how far have I come?", and near the end "how far do I have to go?"
- **Active vs. passive monitoring** were equally effective for attainment (p. 36).
- **Limits** (pp. 38, 40): almost entirely health goals, and effects shrank when participants and experimenters were blind to condition. Social comparison as a reference point was untested.

## Quotes

> "It is not enough merely to monitor progress – the person must also face up to what the information shows." (pp. 34–35)

> "Prompting participants to monitor their behavior had a significant impact on rates of behavioral performance but not on outcomes, whereas prompting participants to monitor outcomes had a significant impact on outcomes, but not on behavior." (p. 33)

## My Take

This confirms the [research report](evidence-based-goal-achievement-system.md)'s monitoring figures (138 studies, d = 0.40, public and recorded larger). The finding the report left out matters most for a map-based goal app: **behaviour monitoring and outcome monitoring do different jobs.** A daily footstep is behaviour monitoring. A reached milestone is outcome monitoring. An app that shows only one of them is pulling only one lever.

The ostrich problem explains why drift warnings are hard to get right. A warning that feels like judgement is exactly the information people avoid. A warning they never see does nothing.

**AI lens:** this is the control-loop argument from [closed-loop-systems](../concepts/closed-loop-systems.md), measured on people. The sensor matters as much as the controller, and what you sense decides what you can correct. For agents, that's "monitor the outcome metric if you want outcome changes, the action trace if you want behaviour changes". The [metrics-trap](../concepts/metrics-trap.md) note is the warning about what happens when the outcome sensor becomes the target. An AI that summarizes progress for a person must also beat the ostrich problem without becoming the nag people avoid. One reading is to make the record easy to face, not loud.
