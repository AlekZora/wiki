---
type: concept
title: Self-Initiation Gap
aliases: [competence vs agency gap, possibility-to-commitment bottleneck, commitment window]
tags: [psychology, behavior, agents, ai, identity]
sources: [human-agency-analysis-chatgpt]
updated: 2026-09-07
---

## Definition

The gap between being able to competently execute a well-defined task and being able to originate one from scratch — notice a need, choose a direction, commit to it under uncertainty, and begin, without something external first removing the ambiguity. The bottleneck sits at one specific transition: **possibility → commitment**. An agent can be capable of extensive reasoning and still never act, because that reasoning is spent comparing purely imaginary options, and an imaginary option can always be out-argued by a better imaginary alternative — nothing is real yet, so nothing is falsifiable, so nothing forces a stop.

This is distinct from low ability or low motivation. The person (or system) can be highly capable at execution once a task exists; the failure is entirely upstream of execution, in the step that would have produced the task.

## How I Think About It

The useful reframe is architectural, not characterological: this isn't "I'm undisciplined," it's "my decision process has no forcing function." Three structural fixes recur across the source material:

- **Separate evaluation-time from execution-time.** If both run concurrently, the system is simultaneously building the thing and asking whether the thing deserves to exist — which never converges.
- **Make commitments temporary, not permanent.** "X is the hypothesis until day N" is psychologically much cheaper than "X is my future," because it doesn't require ruling out every alternative forever.
- **Force contact with reality before allowing rejection.** An idea evaluated purely in imagination is infinitely killable; an idea that has produced even a tiny external artifact generates actual evidence, which is a fundamentally different kind of input to the decision.

The deeper point: more raw reasoning/simulation capacity does not by itself produce action, and can make the problem worse, because it's better at generating plausible alternatives to compare against a plan that hasn't been tested yet. Convergence requires an added constraint — a deadline, a commitment window, an external stake — not more thinking.

## AI Integration

- Names the same failure mode in current AI agents that the source names in humans: agents are highly competent at "solve this well-defined problem" but measurably weaker at the earlier pipeline — noticing what needs doing, generating and prioritizing their own goals, and initiating without an external prompt already having done that work. This lines up with long-horizon agent benchmarks (e.g. AgencyBench-style evaluations) finding a gap between well-defined subtasks and ambiguous, self-directed, extended trajectories.
- Proposes a concrete, transferable architecture mechanism: a **commitment window** — once a plan is selected, suppress replanning/reconsideration until new evidence crosses an explicit threshold. This is a direct answer to agent thrashing (an agent that endlessly re-plans instead of executing), and mirrors human analysis paralysis closely enough to suggest the same fix works in both directions.
- Suggests a shared diagnostic pipeline usable for humans or agent architectures: goal generation → priority selection → commitment → task decomposition → initiative → persistence → feedback → reconsideration → closure. A stalled agent (or person) can be localized to a specific stage in this pipeline rather than diagnosed as generically "low agency," the same way a bug is localized to a function rather than blamed on "the code."
- Raises an open implementation question for agent design: most current agentic frameworks (see [Agentic Workflow](agentic-workflow.md)) treat the loop as continuous plan→act→observe→replan, with no first-class, time-boxed "decision" object. A commitment window plausibly requires reifying "we decided X, and this decision expires/reopens under condition Y" as explicit state, not just a policy layered on top of an otherwise undifferentiated loop.
- Reveals something general about intelligence: the capacity to generate and evaluate options is not the same capacity as the one that converts an option into action. Systems (biological or artificial) that are strong at the first can be systematically weak at the second, and stronger option-generation without a corresponding forcing function can widen rather than close that gap.

## Related Concepts

- [Agentic Workflow](agentic-workflow.md) — covers the execute/observe/iterate loop *after* a goal exists; this concept is about the upstream step of originating and committing to the goal in the first place, which that loop assumes is already solved
- [Hallucinated Agency](hallucinated-agency.md) — a different agency failure mode (acting confidently on invented, ungrounded content); this concept is the opposite direction — failing to act at all absent externally supplied structure
- [Intrinsic Motivation](intrinsic-motivation.md) — related but distinct: motivation is "wanting to act," this concept is specifically the mechanical transition from wanting/considering to committing, which can fail even when motivation is present
- [Rich-or-King Tradeoff](rich-or-king-tradeoff.md) — the next bottleneck in sequence: this concept covers originating a venture, that one covers retaining control once it's scaling past the founder's own skill

## Open Questions

- **Partly answered** ([Why Origination Is Harder Than Execution](../answers/why-origination-is-harder-than-execution.md), 2026-09-07): the possibility → commitment transition converges through **option-collapse**, not through better evaluation — deadlines, commitment windows, kill criteria and shipped artifacts all work by removing alternatives rather than by improving the comparison between them. Adding evidence to a set of mutually-defeating hypotheticals doesn't converge, because each new consideration is available to every option equally. Open remainder: whether option-collapse can be *induced* in an agent that has no identity-level exit cost to begin with, or whether it only bites on systems that experience commitment as self-implicating.
- Does the truth status of what's being simulated determine whether imagination paralyzes or mobilizes? [Imaginative Empathy](imaginative-empathy.md) describes the same faculty producing decisive action when aimed at *actual* experiences (Amnesty International) while it stalls here when aimed at *possible* futures — suggesting unrealised options are mutually defeating precisely because none of them has a truth value yet.
- Is a "commitment window" actually implementable as agent-architecture policy (suppress replanning until an evidence threshold), or does it require the loop to reify decisions as explicit, time-boxed state objects first?
- Can an AI agent's own goal-generation stage be benchmarked stage-by-stage the way this source proposes diagnosing a human's bottleneck (goal generation vs. commitment vs. persistence, etc.), rather than scored as one aggregate "agentic capability" number?
- Does supplying an agent with manufactured "stakes" (the Harry Potter analogy — an externally supplied concrete problem) measurably improve self-directed initiative, or does it just change what gets executed without touching whether initiation happens unprompted at all?

## Project Connections

The [Side Quest AI decision log](../decisions/decision-log.md) is a live instance of exactly this gap: the locale/player-identity decision was made 2026-07-24, then reopened 2026-08-01/02, with multiple candidates generated and rejected in-head (Theseus's road, Ithaca) and a front-runner (the Argo) still "not yet stress-tested" — the possibility → commitment transition stalling out with no external artifact forcing resolution. Separately, `generate_quest()`'s retry policy (retry only on sampling-dependent failures, never on deterministic ones — see [Side Quest AI project](../projects/game/gap-report.md)) is already a working primitive of a commitment window: it doesn't discard a structurally valid plan just because one sample came out wrong.
