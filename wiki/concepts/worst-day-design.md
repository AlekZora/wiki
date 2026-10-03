---
type: concept
title: Worst-Day Design
aliases: [design for repeatability, thinking in systems, peel the band-aids]
tags: [systems, behavior, psychology, agents, engineering, ai]
sources: [../sources/build-systems-not-goals.md, ../sources/evidence-based-goal-achievement-system.md, ../sources/gollwitzer-sheeran-2006-implementation-intentions.md, ../sources/wang-2021-mcii-meta-analysis.md]
updated: 2026-10-01
---

## Definition

Design a process so it succeeds when conditions are bad, not when everything lines up. Start by assuming the plan will fail, list why, and revise until the process no longer depends on scarce, unreliable inputs (willpower, motivation, ideal conditions). Temporary patches that make it work now are tracked as debt, and the underlying cause is then fixed so the patch can be removed.

## How I Think About It

Three moves, run as a loop: (1) enumerate the barriers, using past failures as data; (2) test each candidate plan for whether it needs willpower on a bad day and lower friction if so; (3) separate patches from root-cause fixes and make removing the patch an explicit goal. No single solution has to be perfect, since what works is usually a combination. The source is a coaching talk with anecdotal evidence, so this is a heuristic, not a finding. Its strength is that it is essentially reliability engineering applied to a person.

**Evidence added 2026-10-01.** The [goal-achievement research report](../sources/evidence-based-goal-achievement-system.md) gives research backing to two of the three moves, though it is itself a secondary, AI-written synthesis:
- *Contingencies* are [implementation intentions](implementation-intentions.md) ("if Y, then X"). **Checked against the primary sources the same day:** d = .65 across 94 tests (Gollwitzer & Sheeran 2006). They help with starting, staying on track, and disengaging from failing goals. Rehearsing the plan beat keeping it as a reminder note, 87% vs 40% follow-through in one study. Adding an obstacle step (MCII) gives g ≈ 0.34, or ≈ 0.24 after a bias correction (Wang et al. 2021). It was stronger when a **human experimenter** delivered it face-to-face than from a document. The report's "interactive" meant that, not software.
- *Enumerating barriers* becomes diagnosis. "Hard to start" splits into unclear, overwhelming, threatening, boring, blocked, conflicted and depleted, each with a matched response (clarify, shrink, define "good enough", add reward, unblock, resolve priority, reschedule). A generic "lower the friction" is replaced by "find which friction."
- The report adds a move the talk lacked: **fade support**. Once starting under a cue becomes easy, remove the prompt and see if the behavior holds. That is the patch-removal step with a test attached.

What still lacks evidence: the band-aid/root-cause split, which remains the talk's heuristic.

## AI Integration

- **Agent design:** an agent pipeline that works only when the prompt, context and model behavior are all good is the "willpower" version. Worst-day design means constrained tools, defaults that are correct, retries and contingencies ("if X fails, do Y"), and evals on the bad case, not the demo case. See [harness-engineering](harness-engineering.md).
- **Prompt patches as band-aids:** special-case instructions accumulate and make success conditional. Treat each as debt to remove by changing capability, tooling or environment.
- **Failure-first planning:** having a model enumerate why a plan will fail before it executes, then revising, is a cheap critic loop and a form of [closed-loop systems](closed-loop-systems.md).
- **AI as coach:** an assistant could run this barrier-elimination dialogue with a person. Open whether it resists settling for the first plausible plan. The MCII finding is often read as "conversational beats a form", but the stronger arm was a person in the room. Whether an AI dialogue gets that effect or the document effect is untested. The part an AI could plausibly supply is plan *quality*, catching vague obstacles and non-executable responses, which the paper names as the weakness of self-written plans.
- **Barrier diagnosis as classification:** mapping "what makes starting hard right now?" onto a fixed set of barrier types, each with a deterministic response, is a narrow LLM classification job plus a code lookup. That makes it testable with labelled examples, unlike open-ended coaching.
- **Rehearse, don't just remind:** an assistant that stores the plan and pings it back is the weaker condition in the one study that compared them. Asking the person to state the cue–response link is a cheap way to aim at the stronger one.
- **Fading as a design target:** an assistant that withdraws prompts once the person starts unaided is optimizing for independence, not usage. Worst-day design applied to the human–AI pair: the person shouldn't need the AI on the worst day either.
- **What it reveals:** reliability comes from removing dependence on a good internal state, in humans and in models.

## Related Concepts

- [Closed-Loop Systems](closed-loop-systems.md)
- [Harness Engineering](harness-engineering.md)
- [Post-Generation Editing](post-generation-editing.md)
- [Self-Determination Theory](self-determination-theory.md)

## Open Questions

- Where does removing motivation dependence end? Intrinsic motivation ([self-determination-theory](self-determination-theory.md)) may be part of what makes a system repeatable, not something to design around.
- How do you tell a band-aid from a legitimate permanent part of a system? The fade-support test (remove it and see whether behavior holds) is one operational answer for prompts and cues. Does it generalize?
- Is "depleted" a barrier to design around, or a signal that the worst-day version should be *rest*? The report says reschedule "without moralizing"; the talk says lower friction until it works anyway. They pull in different directions.

## Project Connections

- **Goal Map** (`~/projects/goal-map/`): the "help when stuck" design. Idea 3 of the [Goal Map synthesis](../answers/goal-map-wiki-synthesis.md) (a worst-day step per milestone, plus barrier diagnosis) is built on this page.
