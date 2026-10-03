---
type: concept
title: Implementation Intentions
aliases: [if-then plans, if–then planning, MCII, mental contrasting with implementation intentions, WOOP]
tags: [psychology, behavior, motivation, habit, agents, ai, systems]
sources:
  - ../sources/gollwitzer-sheeran-2006-implementation-intentions.md
  - ../sources/wang-2021-mcii-meta-analysis.md
  - ../sources/singh-2024-habit-formation-meta-analysis.md
  - ../sources/evidence-based-goal-achievement-system.md
updated: 2026-10-01
---

## Definition

A plan that binds a specific situation to a specific response: "If situation Y occurs, then I
will do X." It is a second step after deciding on a goal. The goal says *what* you want, and the
implementation intention says *when, where and how* you'll act. Across 94 tests it had a
medium-to-large effect on reaching goals (d = .65, Gollwitzer & Sheeran 2006). It works by making
the cue easier to notice and the response more automatic. **MCII** adds a step first: picture the
desired outcome, name the obstacle in present reality, then plan for the obstacle ("if obstacle,
then…"). That gives a small-to-medium effect (g ≈ 0.34, or ≈ 0.24 after correcting for
publication bias; Wang et al. 2021).

## How I Think About It

A goal intention is a wish that still has to be turned into action every time. An implementation
intention does that translation once, ahead of time, and hands the moment of action over to the
environment. When the cue appears, the response fires without a new decision. It moves willpower
from the moment of action to the moment of planning. That's why it fits
[worst-day design](worst-day-design.md): the plan is made on a good day and runs on a bad one.

Four things from the primary sources matter more for design than the effect size:

1. **Encoding beats storage.** People who rehearsed the cue–response link acted 87% of the time.
   People who left the written plan as a reminder: 40%. No plan: 20% (Milne & Sheeran, in
   Gollwitzer & Sheeran p. 108). A plan you *have* is weaker than a plan you've *practised*.
2. **Who makes the plan matters, and so does its quality.** MCII delivered face-to-face by an
   experimenter beat MCII done alone from a document (g 0.465 vs 0.277). The authors suspect
   low-quality self-written plans and weaker commitment.
3. **If–then plans help people quit, too.** They had medium-to-large effects on *disengaging
   from failing goals*, not only on starting and persisting. MCII can lead people with low
   expectations to let go.
4. **It's the bridge to habit.** Repeatedly acting on an if–then plan produced more features of
   habitual control than acting on intention alone (Orbell & Verplanken). Habit strength builds
   with repetition in a stable context, and the timescale varies hugely: median ~2 months,
   individual 4–335 days (Singh et al. 2024). Self-chosen habits form more strongly.

The open edge is **faulty plans**. Nobody knows yet whether people repair a plan that failed,
cling to it, or stop planning (G&S p. 104). Rigidity looks low in general, but perfectionists may
ruminate on their adherence.

## AI Integration

- **It is a trigger–action rule.** Event-driven agents, harness hooks and if-this-then-that automations are implementation intentions for software: a watched condition bound to a pre-decided response, executed without new deliberation. The psychology gives a vocabulary for why it works (cue accessibility, automatic response) and why it fails (cue never noticed; response too vague to execute).
- **AI as plan-quality checker:** the weakest point in self-made MCII is plan quality, meaning vague obstacles and non-actionable responses. That's a narrow job an LLM can plausibly do: flag "if I feel unmotivated, then I'll try harder" as non-executable and propose a concrete cue and response. It's checkable, so it can be evaluated with labelled examples.
- **AI is not the experimenter, as far as anyone knows.** Whether AI-guided MCII performs like the face-to-face arm or the document arm is untested. The interpersonal part of the face-to-face effect is exactly what an AI may imitate without delivering. This is worth testing, not assuming.
- **Reminders vs. rehearsal:** an assistant that writes your plan and pings you with it is the 40% condition. One that gets you to say the link back, or imagine the cue, aims at the 87% one. The difference is small to build and might matter a lot. (It comes from one study.)
- **Disengagement as a supported output:** an AI planning partner should be able to help someone *stop* a goal on evidence. The research counts that as success, while most engagement-tuned systems treat it as churn.
- **What it reveals about intelligence:** deliberation is expensive and fragile under load, so intelligent systems pre-compile responses to anticipated situations. Humans do it with if–then plans and habits; agents do it with cached skills and policies ([cognitive-externalization](cognitive-externalization.md)). Both pay the same price: a pre-compiled response may not notice when the situation has changed.

## Related Concepts

- [Worst-Day Design](worst-day-design.md)
- [Cognitive Externalization](cognitive-externalization.md)
- [Closed-Loop Systems](closed-loop-systems.md)
- [Self-Initiation Gap](self-initiation-gap.md)
- [Intrinsic Motivation](intrinsic-motivation.md)
- [Planning Fallacy](planning-fallacy.md) — same pattern: linking past experience to the present task beats recalling it

## Open Questions

- Does an AI conversation deliver the face-to-face MCII effect, the document effect, or neither?
- What should a system do when a person's if–then plan keeps failing: repair the cue, repair the response, or question the goal?
- For complex creative work, does only the start-up routine (open the project, review the last note, begin) become habitual, as the goal-achievement report argues? Or can more of it? The habit evidence covers simple health behaviours only.
- Rehearsal beat reminders in one study. Does it replicate, and what's the cheapest form of rehearsal a product can ask for?

## Project Connections

- **Goal Map** (`~/projects/goal-map/`): the "help when stuck" design and the worst-day step per milestone are if–then plans. See ideas 3 and 5 in the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md) and its evidence check.
