---
type: concept
title: Transformer Architecture
aliases: [GPT, attention mechanism, autoregressive generation, large language model]
tags: [ai, llm, transformers, attention-mechanism, neural-networks]
sources:
  - ../sources/transformers.md
updated: 2026-05-09
---

## Definition

The Transformer is the neural network architecture underlying all modern large language models (GPT, Claude, etc.). Its distinguishing innovation over prior architectures is the **attention mechanism**: instead of processing tokens sequentially (like an RNN), all tokens interact with each other in parallel, each "attending" to the others to build up context.

The pipeline: text → tokens → embedding vectors → repeated blocks of (attention + MLP) → unembedding → probability distribution over next token. Generation is autoregressive: sample a token, append it, repeat.

## How I Think About It

The core frame: a Transformer is a machine that takes token vectors and progressively enriches each one with context from the rest of the sequence. By the final layer, each vector has "soaked in" the information it needs to predict what comes next, given the whole preceding context.

The **temperature** parameter at sampling time controls the creativity-coherence tradeoff: low temperature → the model picks the highest-probability token reliably → coherent but predictable; high temperature → the distribution is flattened → surprising but potentially incoherent. This is a direct mechanical lever.

The context window is the architecture's hard constraint. Everything the model "knows" about the current situation must fit inside it. Longer context = more state, but not infinite.

## Related Concepts

- [Word Embeddings](word-embeddings.md)
- [Neural Networks](neural-networks.md)
- [Cognitive Externalization](cognitive-externalization.md)
- [Agent Memory](agent-memory.md)

## Open Questions

- What is actually happening inside the attention heads? What "decisions" are being made, and can they be interpreted?
- Is the context window limit a fundamental architectural constraint or an engineering tradeoff?

## Project Connection

The autoregressive generation loop is the core mechanism by which AI agents in the sci-fi series would "think" and "speak." The temperature parameter maps directly to character design: a paranoid, cautious character runs at low temperature (precise, measured speech), while an unhinged or creative character runs hot (unpredictable, associative). The context window limit is a built-in mechanic for agent amnesia — information that falls out of context is genuinely "forgotten," a property that could be exploited for narrative information asymmetry.
