---
type: concept
title: Research Craft
aliases: [research taste, how to do research, research skill stack]
tags: [research, ml, tacit-knowledge, agentic-workflow, learning, agents]
sources:
  - ../sources/how-to-be-good-at-research-vivek.md
updated: 2026-08-30
---

## Definition

Research craft is the claim that "being good at research" is not a single innate
gift but a stack of separable, trainable sub-skills: choosing your own problems
(rather than absorbing them from an advisor or a trending paper), developing taste
through repeated forecast-and-check cycles, curating an information diet that
includes old/underpriced material and cross-domain range, externalizing thought
through writing as a diagnostic (not just communicative) act, building fast
iteration loops so tooling becomes a research activity rather than overhead, reading
raw failures instead of trusting aggregate metrics, deliberately wandering across
subfields before specializing, and cultivating collaborators who catch bad ideas
early. Each sub-skill is independently identifiable and independently improvable.

## How I Think About It

The load-bearing move in this framing is refusing the "some people just have it"
explanation. If research ability decomposes into a list of concrete habits — forecast
an experiment's result before running it and check your hit rate; keep a log of
hypothesis/setup/expectation/result/updated-belief; read 100 failure cases and bucket
them before trusting a benchmark number — then each one is a discrete practice you can
adopt starting today, independent of talent. That reframing matters because it
converts "research taste" from a mystical trait into an auditable checklist.

The sharpest individual insight is "research speed is mostly the speed at which you
discover you're wrong." This inverts the usual framing of research productivity
(more experiments, more compute, more hours) into a statement about latency to
falsification. A researcher who can be wrong and *know it* in an hour is
structurally faster than one who is wrong for a month before finding out, even if
the second person runs more total experiments. This is why the essay treats tooling
(one-command runs, reproducible configs, fast comparisons) as core research work
rather than supporting infrastructure — the tooling *is* the speed at which you find
out you're wrong.

The other insight that generalizes past ML specifically: writing is diagnostic before
it's communicative. An idea that feels complete in your head reliably turns out to
have gaps once you're forced to state it in full sentences — the page exposes
untested assumptions and quietly contradictory claims that a head-only idea can hide
from you. Darwin's practice of logging any fact that contradicted his own theory the
moment he noticed it is the extreme version: an explicit defense against memory's
tendency to delete inconvenient evidence faster than convenient evidence.

## AI Integration

- **Nearly every practice here is a design spec for an agentic research loop, not
  just human advice.** "Write everything down" is externalized, append-only memory —
  precisely what an agent harness needs so that inconvenient intermediate results
  aren't silently dropped from context the way human memory silently drops them.
  "Tighten the loop" is a direct argument for optimizing an agent's time-to-feedback
  over its per-step sophistication, since the essay's claim ("research speed is the
  speed at which you discover you're wrong") applies just as literally to an
  autonomous agent iterating on a hypothesis as to a human.
- **"Stare at the outputs" names a specific eval-design failure mode.** A benchmark
  score without a corresponding read of transcripts is exactly "a descending loss
  curve as reassurance, not analysis" — this is a concrete, actionable critique of how
  LLM capability claims often get made (aggregate score reported, failure transcripts
  never read) and a direct argument for transcript-level eval review as a required
  step, not an optional one.
- **Backward-from-outcome problem selection (Schulman's second mode) is a template
  for goal specification in agentic systems.** An agent given a forward-search
  objective ("find things to improve in this codebase") will default to the same
  well-trodden territory a forward-literature-search researcher does; an agent given
  an outcome to reason backward from is more likely to surface non-obvious paths —
  suggesting agent task framing itself should be audited for which mode it's
  implicitly using.
- **The claim that expertise here is legible and trainable, not tacit and
  gatekept, implies these practices could be scaffolded directly into an AI research
  agent's operating procedure** rather than treated as tacit human-only knowledge —
  which would make this a candidate source of concrete design patterns for
  [neuro-symbolic-agent-architecture](neuro-symbolic-agent-architecture.md)-style
  systems or any AI-agent-personality-design work aimed at autonomous research.

## Related Concepts

- [Organizational Tacit Knowledge](organizational-tacit-knowledge.md) — the company-
  level version of the same problem (encoding expert practice so it transfers); this
  concept is the individual-skill-stack version
- [Recognition-Primed Decision-Making](recognition-primed-decision-making.md) — a
  different model of expertise (fast intuitive pattern-matching under time pressure)
  that research craft's "taste" practices are partly trying to deliberately train
  toward
- [Loop Engineering](loop-engineering.md) — "tighten the loop" is the same underlying
  principle (fast, cheap, verifiable iteration) applied to autonomous coding/agent
  systems rather than to human research practice

## Open Questions

- Can the seven practices here be turned into an explicit checklist or scaffold for an
  autonomous research agent, and would doing so actually improve agent research
  output, or does some of this only work because a human is doing the forecasting/
  taste-calibration step?
- Is "research speed = speed of discovering you're wrong" the right optimization
  target for an agent harness generally, or specific to open-ended research tasks
  with no ground truth?
- Does an LLM's fluency undermine the "write everything down" practice specifically —
  if an agent can generate a plausible-sounding log entry without having done the
  diagnostic work of actually confronting a contradiction, does the practice lose its
  value when automated?
- The essay explicitly recommends deliberate cross-subfield wandering before
  specializing — is there an equivalent argument for deliberately exposing a research
  agent (or a fine-tuning curriculum) to adjacent domains before narrowing its scope?
