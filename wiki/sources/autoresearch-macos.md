---
type: article
title: "miolini/autoresearch-macos: AI agents running research on single-GPU nanochat training automatically adopted for MacOS"
url: https://github.com/miolini/autoresearch-macos?tab=readme-ov-file
author: miolini
published:
ingested: 2026-04-08
tags: [ai, ml, llm, autonomous-agents, tool, hardware]
concepts:
  - "[[autonomous-ml-research]]"
  - "[[nanochat]]"
---

## Summary

A GitHub repo (forked from Karpathy's nanochat) that lets an AI coding agent autonomously run ML experiments overnight. The agent edits a single training file (`train.py`), trains for a fixed 5-minute window, checks validation loss, keeps improvements, and repeats — without any human involvement between cycles. The macOS fork adds Apple Silicon / MPS support that the original lacked.

## Key Points

- The human's job is to write `program.md` — a markdown "skill" file that instructs the agent. The agent handles everything else.
- Only one file (`train.py`) is in scope for the agent to edit. `prepare.py` is locked. This keeps diffs reviewable.
- Fixed 5-minute training budget per experiment — makes runs comparable across architectural changes; yields ~12 experiments/hour, ~100 overnight.
- Metric is **val_bpb** (validation bits per byte) — lower is better, vocab-size-independent, so fair across architectural changes.
- This fork removes the hard FlashAttention-3 dependency and falls back to PyTorch SDPA with manual sliding window causal masking for MPS/CPU.
- Karpathy added a tongue-in-cheek quote framing this repo as the origin story of a future where AI swarms have run 10,000+ generations of self-modifying research code.

## Quotes

> "The idea: give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats."

> "The core idea is that you're not touching any of the Python files like you normally would as a researcher. Instead, you are programming the `program.md` Markdown files that provide context to the AI agents."

## My Take

This is a clean, minimal proof of concept for agentic ML research. The design constraint of a single editable file and a fixed time budget is smart — it makes the loop tight and the results interpretable. The interesting meta-layer is that `program.md` is itself something you iterate on, so you're essentially doing prompt engineering on your research org. The macOS fork makes this practically runnable without cloud compute. Worth trying on an M-series Mac with TinyStories as the dataset.
