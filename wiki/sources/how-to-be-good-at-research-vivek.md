---
type: article
title: "how to be good at research"
url: https://x.com/itsreallyvivek/article/2064686372737454155
author: vivek (@itsreallyvivek)
published: 2026-06-10
ingested: 2026-08-30
tags: [research, ml, tacit-knowledge, agentic-workflow, learning]
concepts:
  - ../concepts/research-craft.md
---

## Summary

An essay arguing that ML/AI research competence is a trainable stack of discrete
sub-skills rather than a single innate gift, organized into seven practices. (1) Pick
your own problems: absorbed problems (inherited from an advisor or a trending paper)
carry the conclusion without the reasoning, so when the field pivots you're two steps
behind; Hamming's "what are the important problems, and why aren't you working on
them" and Schulman's backward-from-a-desired-outcome mode manufacture originality that
literature-driven forward search can't. Taste is trainable by forecasting experiment
outcomes before running them and checking the hit rate. (2) Upgrade your inputs: shared
reading lists (arXiv trending, group-chat consensus) produce shared, low-value
conclusions; old material is underpriced (MoE dates to 1991, LSTMs to 1997, backprop
went mainstream in 1986) and range across adjacent fields (neuroscience for
interpretability, mechanism design for eval design, GPU memory movement for
architecture intuition) compounds. Read primary papers, not thread summaries — the
limitations section is usually the most honest paragraph. (3) Write everything down:
writing exposes gaps a fully-formed-feeling idea hides; Darwin logged any fact that
contradicted his theory the moment he noticed it, because memory silently deletes
inconvenient evidence faster than convenient evidence. Public writing (per Olah &
Carter's "research debt" framing) is a genuine contribution, not just exposure. (4)
Tighten the loop: research speed is the speed at which you discover you're wrong, so
tooling (one-command runs, fast comparison, reproducibility from config) is a research
activity, not overhead — engineering and research have fused at the frontier. (5) Stare
at the outputs: a descending loss curve is reassurance, not analysis; most information
in an experiment run (transcripts, failure cases, distribution tails) goes unread.
Karpathy's recipe starts with hours of hand-inspecting raw data before any training
code; Andrew Ng's "read 100 failures, bucket them, attack the biggest bucket" applies
equally to models and to evals. (6) Wander on purpose: your first subfield is an
accident of timing, so deliberately spend time in several before committing; run
disposable versions of ideas and let most die young; tune baselines until it hurts,
since most published gains evaporate against a properly-tuned baseline. (7) Find your
people: generosity compounds (replicate and publish, release your internal tools,
explain something hard in plain language); a collaborator who kills a bad idea before
you sink three months into it is worth more than compute.

## Key Points

- Research skill decomposes into trainable sub-skills: problem selection, taste,
  information diet, externalized thinking (writing), tooling velocity, failure
  analysis, and deliberate breadth — not a single unteachable gift.
- Backward-from-desired-outcome problem selection (Schulman) produces more original
  work than forward literature search, because it drags you into territory no survey
  covers.
- Old, "underpriced" material often out-predicts the field's own current surveys (cites
  Sutton's "Bitter Lesson" as an example of an old, short piece that predicts the
  field's shape better than survey papers ten times its length).
- Writing is diagnostic, not just communicative: it's the cheapest available defense
  against fooling yourself (Feynman), and a running experiment log (hypothesis, setup,
  expectation, result, updated belief) outperforms memory, which silently deletes
  inconvenient results.
- "Research speed is mostly the speed at which you discover you're wrong" — this
  reframes tooling investment (fast iteration loops, reproducible configs, one-command
  comparisons) as core research work, not supporting infrastructure.
- Reading failure cases in bulk (Karpathy's raw-data-first step; Ng's "read 100
  failures, bucket, attack the biggest bucket") beats aggregate metrics for
  understanding what's actually wrong.
- Deliberate subfield-wandering before specializing is framed as insurance against
  saturation, since subfields "saturate... usually right after they peak on twitter."

## My Take

This essay is functionally a design spec for a good agentic AI research loop, written
about humans — nearly every practice it recommends maps directly onto what makes an
autonomous or semi-autonomous research agent effective rather than just busy. "Write
everything down" is externalized memory/logging exactly in the sense agent harnesses
need (a persistent, append-only trace an agent — or its supervisor — can audit later,
because in-context memory silently drops inconvenient results the way human memory
does). "Tighten the loop" is literally the case for fast, cheap, auto-verifiable
iteration loops in agent design — the essay's claim that "research speed is the speed
at which you discover you're wrong" is a strong argument for optimizing an agent
harness's time-to-feedback over its per-step sophistication. "Stare at the outputs"
(reading transcripts and failure buckets instead of trusting aggregate metrics) is the
exact discipline that eval-design work for LLMs currently under-does — a benchmark
score without a corresponding read of transcripts is precisely the "descending loss
curve as reassurance, not analysis" trap the essay warns against. The overall argument
— that expertise here is a stack of legible, individually-trainable habits rather than
innate taste — also implies these practices could plausibly be scaffolded directly
into an AI research-agent's operating procedure rather than treated as tacit,
human-only knowledge.
