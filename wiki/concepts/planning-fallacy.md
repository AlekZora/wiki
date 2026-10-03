---
type: concept
title: Planning Fallacy
aliases: [inside view, outside view, reference-class forecasting, optimistic time estimates]
tags: [psychology, behavior, productivity, systems, ai, agents, llm]
sources:
  - ../sources/buehler-griffin-ross-1994-planning-fallacy.md
  - ../sources/planning-fallacy-evidence-and-product-implications.md
updated: 2026-10-01
---

## Definition

The tendency to predict that your own tasks will finish sooner than they actually do, even when
similar past tasks ran late (Kahneman & Tversky, 1979). The cause is the **inside view**:
simulating how this particular plan should unfold, while ignoring the **outside view**, the
distribution of how comparable cases actually went. In Buehler et al. (1994), fewer than a third
of thesis writers finished by their best estimate, and fewer than half by their *worst-case*
estimate. The standard correction is **reference-class forecasting**: start from comparable
past outcomes, then adjust only for documented differences.

## How I Think About It

The fallacy isn't ignorance. People *know* they usually run late and forecast optimistically
anyway, because they decide the past doesn't apply this time (external, one-off causes). The
estimates are informative (r = .77 with actual times in Buehler's thesis study), but shifted.
So the fix isn't more information. It's a different *position* and an explicit *link*:

- **Position:** observers predicting someone else's task weren't optimistic and used past
  experience more (Buehler Study 5). The bias belongs to the actor's seat, not to the data.
- **Link:** recalling past experience didn't help. Recalling it *and connecting it to this
  task* removed the bias (Buehler Study 4: 60% on time vs 29–38%).

That second finding rhymes with the if–then evidence, where rehearsing a cue–response link
beat having a reminder ([implementation intentions](implementation-intentions.md)). **Inference:**
self-knowledge doesn't change behaviour until it's tied to the current situation.

Two practical additions from the brief: separate **active effort** from **elapsed time** (three
hours of work can span five days), and give **ranges, not points**. A single date hides the
variance that the outside view is about. The limits matter too. Reference classes need truly
comparable cases, narrow classes run out of data, and a new user has no personal history at
all.

## AI Integration

- **LLMs default to the inside view.** Asked to plan, a model narrates the ideal sequence, which is the mechanism of the fallacy. AI planners that produce timelines without distributional data will be coherent and optimistic. Architectural fix: the model proposes *structure*, and code supplies *durations* from recorded outcomes.
- **AI in the observer seat:** the actor/observer asymmetry is a principled reason to have a system other than the planner estimate time. Open question: does an LLM fed the user's own hopeful framing act as an observer, or absorb the actor's optimism?
- **Agents have it too.** Agent plans underestimate steps, retries, integration and recovery. The brief's "hidden work" list (setup, coordination, revision, waiting, recovery) is a usable checklist for agent task decomposition and for eval design.
- **Calibration as a closed loop:** predict, record, compare, adjust is a [closed loop](closed-loop-systems.md) on the forecaster, the same habit as [research-craft](research-craft.md)'s forecast-and-check. Personal AI assistants can keep the record that people don't.
- **Honesty about confidence:** with sparse data, the right AI output is a wide range and a stated basis ("based on 3 similar milestones"), not a precise date. This matches the goal-achievement report's "false precision" warning.

## Related Concepts

- [Implementation Intentions](implementation-intentions.md)
- [Closed-Loop Systems](closed-loop-systems.md)
- [Research Craft](research-craft.md)
- [Worst-Day Design](worst-day-design.md)
- [Metrics Trap](metrics-trap.md)

## Open Questions

- What's the reference class for a *personal goal milestone* when the user has no history? Population data from other users, the user's own similar tasks elsewhere, or nothing (with honesty about it)?
- Does an LLM estimating someone else's task take the observer's realism or the actor's optimism?
- What's the cheapest "link" prompt that reproduces Buehler's recall-relevant effect in a product, and does it hold for weeks-long goals rather than day-scale assignments?

## Project Connections

- **Goal Map** (`~/projects/goal-map/`): the AI generates milestones, so planning-fallacy correction decides whether the first milestone feels reachable. See ideas 8 and 9 in the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md).
