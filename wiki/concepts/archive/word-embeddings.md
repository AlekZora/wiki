---
type: concept
title: Word Embeddings
aliases: [embedding space, semantic vectors, vector representations]
tags: [ai, ml, llm, transformers, semantics]
sources:
  - ../sources/transformers.md
updated: 2026-05-09
---

## Definition

Word embeddings are high-dimensional numerical vectors that represent the meaning of tokens. Rather than encoding tokens as arbitrary IDs, an embedding matrix maps each token to a point in a geometric space (e.g., 12,288 dimensions for GPT-3) where semantic relationships are encoded as directions and distances.

The key property: vector arithmetic corresponds to semantic operations. `vector(king) - vector(man) + vector(woman) ≈ vector(queen)`. Concepts like "plurality," "gender," or "nationality" become geometric directions in the space.

## How I Think About It

Embeddings make meaning *computable*. The semantic similarity between two concepts is their cosine distance. An analogy is a vector addition. "Find me something like X but in domain Y" is a nearest-neighbor search. This is not metaphor — the model literally performs these operations when processing text.

Context matters: a token's embedding at the *output* of the Transformer is not the same as its *input* embedding. The attention mechanism enriches each vector with context, so the final representation of "bank" in "river bank" is geometrically different from "bank" in "financial bank."

## Related Concepts

- [Transformer Architecture](transformer-architecture.md)
- [Neural Networks](neural-networks.md)

## Open Questions

- Are the meaningful semantic directions in embedding space a property of the training data distribution, or do they emerge from the architecture itself?
- Can embedding arithmetic be used to implement a semantic search layer in a personal wiki without a full LLM?

## Project Connection

Embedding spaces offer a concrete mechanism for AI agent "world models" in the sci-fi series. Each agent could maintain a private embedding of the current situation — a high-dimensional point encoding their understanding of events. Information asymmetry could be modeled as agents having differently calibrated embeddings of the same events, pointing in different directions in the same space. Their hidden agendas are baked into the directions they attend to.
