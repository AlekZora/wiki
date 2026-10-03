---
type: article
title: An Evidence-Based Goal-Achievement System for a Personal Productivity App
url:
author: Unattributed AI deep-research report (31 references; two of them are Perplexity threads asking about a map-inspired goal prototype, so likely Perplexity)
published:
ingested: 2026-10-01
tags: [psychology, behavior, productivity, motivation, habit, procrastination, attention, ai, agents, design, systems]
concepts:
  - ../concepts/worst-day-design.md
  - ../concepts/closed-loop-systems.md
  - ../concepts/cognitive-externalization.md
  - ../concepts/metrics-trap.md
  - ../concepts/compulsion-vs-craft.md
---

## Summary

A product brief, written as a literature synthesis, for a goal app built around a "goal route" rather than a task list. Its argument: goal pursuit fails at distinct points (choosing a goal, translating it into a next action, starting, keeping attention, surviving interruption, repeating, and reviewing). Each failure point needs a different, mechanistically matched intervention: if–then plans, barrier-specific start help, focus protection, ready-to-resume checkpoints, cue-linked repetition, and a sparse review that must end in a decision. Bundling more techniques does not help on its own, and the report cites a meta-analysis where technique count did not predict outcomes. So the system should be "combined at the mechanism level and minimal at the interface level." It closes with an MVP list, a data model, a metrics hierarchy with guardrails, a staged validation program, and a bounded role for AI: the system proposes and remembers, and the person authorizes. No URL, author or date is given. Its effect sizes come from the cited papers. *Checked later the same day:* most hold, but two claims are overstated (MCII "interactive" delivery, and faster resumption from a checkpoint). See section 5 of the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md).

## Key Points

- **Six failure points, one loop:** orient → commit → start → protect → preserve → resume → learn → adapt. The report frames this as a control system: target, act, observe, compare, adjust.
- **Implementation intentions** ("If Y, then I do X") beat plain goal intentions. Reported effects: medium-to-large across 94 tests; d = 0.27–0.66 across 642 tests in a 2025 synthesis. Contingent format, rehearsal and high motivation make them stronger.
- **Mental contrasting with implementation intentions (MCII)** adds an obstacle model: g = 0.336 across 21 studies (N = 15,907), stronger when delivered **interactively** than as a document. The report's inference: planning should be conversational and obstacle-specific.
- **Procrastination needs diagnosis, not a timer.** Seven barrier types (unclear, overwhelming, threatening, boring, blocked, conflicted, depleted), each with a matched response. Treatment effects are small on average, and CBT-style approaches look most promising.
- **Ready-to-resume plan** (four studies): writing down where you stopped and how to return reduces attention residue. This is the report's "most defensible distinctive micro-intervention," and in a map UI it becomes a **footprint at the last known position**.
- **Interruptions are not uniformly harmful** (review of 247 publications). Separate preventable interruptions, necessary ones, deliberate switches, and internal drift.
- **Streaks misrepresent habit.** Habit is a context–response association. Formation time: medians of 59–66 days, individual estimates from 4 to 335 days. Don't promise 21 days or reset to zero after a miss. For complex work, only the **initiation shell** (open, review checkpoint, pick next action, begin) becomes habitual.
- **Tracking alone is weak.** Monitoring improves attainment (d = 0.40, 138 RCTs), more so when recorded and reported, but self-monitoring alone sometimes shows no effect. Collect only what supports the next decision.
- **Review must end in a decision:** continue, increase, simplify, change cue, remove friction, seek support, pause, or stop. "A graph without an action is decorative analytics."
- **Adaptive intervention policy:** borrow just-in-time adaptive intervention (JITAI) structure, but start rule-based and interpretable, with a suppression rule per intervention. **Fade support** as starting becomes easier, so the app doesn't create dependence on itself.
- **Metrics:** north star = verified progress per active goal, not task volume. The guardrails include guilt and compulsive checking, how often recommendations are overridden, and the gap between engagement and real progress. "A healthy product may reduce its own daily active use."
- **Validation:** test single mechanisms first (generic vs. concrete next action, timer pause vs. checkpoint, graph vs. graph + decision), then factorial or micro-randomized designs. Don't use app opens as the main endpoint.
- **AI's role:** turn goals into candidate milestones and actions, catch vague or oversized next actions, generate obstacle-specific if–thens, summarize checkpoints, find recurring blockers, and propose route changes with evidence. It must not choose values, fake confidence about completion dates, silently activate goals, infer diagnoses, or prompt just because a click is likely.
- **Design risks named:** feature accumulation, the notification paradox, metric substitution, shame loops, over-planning as procrastination, false precision, and goal-persistence bias (stopping must be a legitimate outcome).

## Quotes

> "The system should be combined at the **mechanism level** and minimal at the **interface level**."

> "A graph without an action is decorative analytics."

> "A healthy product may reduce its own daily active use as users develop effective routines."

> "The design principle is **co-agency**: the system proposes and remembers; the person authorizes and owns the route."

> "Route design can become sophisticated procrastination. Planning should stop as soon as an executable next action, cue, and obstacle response exist."

## My Take

This is the most directly relevant source the vault has for Goal Map, and it fills three gaps the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md) named: procrastination, habit formation and self-monitoring research. Treat it as a secondary source. It is an AI-written synthesis whose statistics I haven't checked against the papers. Two of its references are prompts about a map-inspired prototype, so it was shaped by the product it advises. The map vocabulary near the end (locked doors, secret passages, footprints) comes from that framing, not from the evidence.

**AI lens:**

- **The loop is an agent architecture.** Orient → commit → act → checkpoint → resume → review is the plan-act-observe-adapt loop of a [closed-loop](../concepts/closed-loop-systems.md) agent. The ready-to-resume checkpoint is the human version of an agent writing state to external memory before a context switch, i.e. [cognitive externalization](../concepts/cognitive-externalization.md) applied to a person. The same four fields (last state, next action, open question, resume cue) would make a good handoff schema for a long-running agent.
- **Where AI earns its place is translation and diagnosis**, not motivation. MCII works better interactively than as a form. *(Checked the same day against [Wang et al. 2021](wang-2021-mcii-meta-analysis.md): "interactive" meant a face-to-face human experimenter, so this is **not** evidence for a conversational AI. Whether AI dialogue gets the effect is untested. The defensible AI role is checking plan quality.)* The same report wants every intervention decision to be an interpretable rule with a suppression condition. That is the [neuro-symbolic](../concepts/neuro-symbolic-agent-architecture.md) split again: the LLM proposes, code decides when to act.
- **Fading support is an alignment property.** A system that stops prompting once the person can start alone is optimizing for the user's independence over its own usage. Most engagement-tuned AI products do the opposite. The guardrail list (override rate, engagement minus progress) is a usable spec for checking whether an assistant is serving the user or itself. It ties to the [metrics trap](../concepts/metrics-trap.md) and [compulsion vs. craft](../concepts/compulsion-vs-craft.md).
- **Situational patterns over traits.** "This task has been postponed three times after ambiguous briefs" rather than "user lacks conscientiousness." That is a good rule for any AI that models a person: describe the situation, don't label the person.
- **For the mission's personal-AI-assistant stage:** the "AI should not" list reads like a draft behavior spec for that assistant.
