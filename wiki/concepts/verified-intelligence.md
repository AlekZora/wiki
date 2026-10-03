---
type: concept
title: Verified Intelligence
aliases: [formal verification + AI, verified AI, lean for AI]
tags: [ai, ml, formal-verification, mathematics, agents, ai-safety]
sources: [5-papers-ycombinator.md]
updated: 2026-06-13
---

## Definition

Verified intelligence is the combination of language model generation with formal verification systems — tools like the Lean theorem prover — to produce outputs whose correctness is guaranteed, not just plausible. The LLM generates candidate proofs, code, or scientific claims; a trusted formal kernel checks each step for logical validity. The result is a system that cannot hallucinate in its output domain: every claim it presents has been mechanically verified.

The key insight: LLMs excel at search (generating candidate solutions across a large space) while formal provers excel at checking (guaranteeing correctness of each candidate). Neither is sufficient alone. Together, they produce intelligence that is both creative and provably correct.

Current applications: formal mathematics (Lean + LLMs proving theorems in Mathlib), software verification (proving correctness of code like Flash Attention), and scientific model validation.

## How I Think About It

Verified intelligence draws a hard line between "probably correct" and "certainly correct." Most LLM output lives in the first category — statistically likely based on training, but unverifiable. Formal verification systems create a second category where the output has been checked against an axiomatic foundation.

The cost is scope: formal verification only works where you can specify correctness formally. You can formally prove a sorting algorithm is correct; you cannot formally prove a poem is beautiful. Verified intelligence therefore has a natural domain: mathematics, formal logic, type-checked code, scientific models with explicit mathematical structure.

I think of it as building a knowledge base with provably correct entries vs. a knowledge base with statistically plausible entries. The former is narrower but load-bearing in a way the latter never can be.

## AI Integration

- **Hallucination elimination in formal domains**: Verified intelligence is the only known approach that eliminates hallucination (rather than reducing it). In any domain with formal structure — code, math, logic, constrained simulations — combining LLM generation with a formal verifier produces outputs that cannot be wrong in the dimensions the verifier checks.
- **Grounding layer for AI agents**: The fact database and hard-constraint validator (Step 6 of the game build) is a weak version of verified intelligence — assertions the system cannot violate. The more formal these constraints are expressed, the closer to verified intelligence the system becomes.
- **Self-play in formal domains**: Formal verification is what makes self-guided self-play tractable in math — the solver's output can be checked without human annotation. Verified intelligence is the infrastructure that enables SGS to scale.
- **Scientific AI**: Formal verification of neural network components (Flash Attention correctness proof) opens a path to AI systems whose internal computations are auditable and verifiable, not just empirically tested. Long-term, this could be the foundation for AI used in safety-critical scientific inference.

## Related Concepts

- [self-guided-self-play](self-guided-self-play.md) — formal verification provides the automated feedback signal SGS needs
- [ai-safety](ai-safety.md) — verified intelligence is a structural approach to AI safety in formal domains
- [loop-engineering](loop-engineering.md) — verification is the "checker" in the maker/checker loop
- [regulatory-integrity](regulatory-integrity.md) — formal verification is the hard-constraint version of regulatory integrity

## Open Questions

- What is the minimum structure required in a domain for formal verification to be applicable?
- Can formal verification extend to probabilistic or fuzzy domains, or is it inherently binary (correct/incorrect)?
- Is there a path to formally verifying AI behavior in open-ended environments, or only in fully specified ones?
- How does the expressiveness ceiling of formal systems (Gödel incompleteness) affect the long-term scope of verified intelligence?
