---
type: concept
title: Closed-Loop Systems
aliases: [closed loop, intelligent closed loop, feedback loop, progress monitoring, control loop]
tags: [ai, tool, ml, systems, psychology, behavior]
sources:
  - ../sources/yc-build-company-with-ai.md
  - ../sources/karpathy-no-priors-code-agents.md
  - ../sources/harkin-2016-progress-monitoring.md
  - ../sources/evidence-based-goal-achievement-system.md
updated: 2026-10-01
---

## Definition

A system that continuously monitors its own output and feeds that signal back to adjust the process — as opposed to an open loop, which decides, executes, and stops there with no systematic feedback.

Applied to companies (from the YC talk): AI-native organizations run as closed loops. Every action produces an artifact; artifacts feed back into the intelligence layer; the process improves over time. Old-style companies were open loops — managers decided, teams executed, and the outcome was rarely wired back to improve the next decision.

Applied to AI research (from Karpathy): auto research is a closed loop over ML experimentation. Give an LLM an objective metric, a sandbox, and a loop; let it run overnight. Karpathy's auto research found weight decay and Adam beta tunings he had missed after two decades of manual tuning. The research organization itself can be described as a set of markdown files (Program.md) that the loop can optimize — the meta-optimization layer is the next frontier.

Applied to people (added 2026-10-01): control theory treats a person pursuing a goal as the same loop: set a target, act, compare where you are with where you meant to be, correct. Harkin et al. (2016) measured the "compare" step across 138 randomized studies. Prompting people to monitor their progress improved goal attainment (d = 0.40), and how often they monitored mediated the effect.

## How I Think About It

An open loop is doing work. A closed loop is doing work and learning from it automatically. The difference sounds small, but it compounds. Every iteration where you fail to capture feedback is an iteration where you can't improve. The insight from both sources is the same: the value isn't in the single-pass AI execution, it's in wiring the output back into the input so the system gets better without you.

The human-goal evidence adds three things the engineering framing tends to skip:

- **The sensor decides what can be corrected.** Monitoring behaviour changed behaviour but not outcomes; monitoring outcomes changed outcomes but not behaviour (Harkin). A loop that senses only actions can't steer results, and vice versa.
- **Loops get avoided.** People dodge information about their own progress when they suspect it's bad (the "ostrich problem"). Recording the signal makes it harder to ignore. A loop only closes if someone faces what the sensor shows.
- **A loop must end in a decision.** "A graph without an action is decorative analytics" (goal-achievement report). Monitoring that doesn't change the next action is an open loop with a dashboard.

## AI Integration

- **Auto research and AI-native companies** are closed loops where an LLM is the controller: objective metric, sandbox, iterate. The open frontier is meta-optimization, where the loop edits the documents (Program.md) that define the loop.
- **Agent design:** the human findings carry over directly. Pick the sensor for the thing you want to change: outcome metrics for outcome changes, action traces for behaviour changes. And require every evaluation step to emit a decision (continue, adjust, stop), not just a score.
- **Overfitting the sensor:** a loop that optimizes its own metric drifts from what the metric was for. That's the [metrics trap](metrics-trap.md), and it gets worse the better the optimizer is.
- **AI as the "compare" step for people:** an assistant can do the part people avoid, looking at the record. But it inherits the ostrich problem. A summary that feels like judgement is the information people dodge. The design goal is a record that's easy to face, not a louder alert.
- **Mutual loops:** when a person and an AI share a loop, each one's outputs are the other's inputs. Neither sits outside it. That's useful for co-adaptation, and a risk when both start optimizing for each other instead of the task.
- **What it reveals:** intelligence, human or artificial, is less about the quality of a single decision than about how fast and how honestly a system notices it was wrong. That links to [research-craft](research-craft.md)'s "speed at which you discover you're wrong."

## Related Concepts

- [Metrics Trap](metrics-trap.md)
- [Worst-Day Design](worst-day-design.md)
- [Implementation Intentions](implementation-intentions.md)
- [Research Craft](research-craft.md)
- [Harness Engineering](harness-engineering.md)

## Open Questions

- What is the minimum artifact richness required to make a feedback loop useful vs. noisy?
- In auto research, how do you prevent the loop from overfitting to its objective metric in ways that don't generalize?
- Is there a principled way to design the "Program.md" for a company the way Karpathy envisions for a research org?
- In a human–AI loop, who owns the "compare" step? If the AI always does the comparing, does the person stop being able to?

## Project Connections

- **Goal Map** (`~/projects/goal-map/`): the product is a control loop for one goal. Daily footsteps are behaviour monitoring, reached milestones are outcome monitoring, and the drift rule is the comparator. See the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md).
