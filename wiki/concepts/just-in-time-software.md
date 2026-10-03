---
type: concept
title: Just-in-Time Software
aliases: [instruction-first architecture, fat skills thin harness, skill pack architecture]
tags: [ai, llm, agents, architecture, engineering, software-design]
sources:
  - ../sources/stop-building-foxconn-factories.md
updated: 2026-06-24
---

## Definition

Just-in-time software is an architectural paradigm where behavior lives in natural language instructions (typically markdown) rather than in code. Code is reserved for the thin deterministic layer — I/O and operations that genuinely must not hallucinate. The LLM is the execution engine; instructions are the program. The primitive unit is the skill pack: a versioned, tested, reusable bundle consisting of a markdown skill, minimal code, automated tests, and LLM evals.

## How I Think About It

The old architecture was built on one assumption: LLM calls are expensive, so you write lots of code to ration them. You build validators, sanitizers, retry loops, background jobs — a Foxconn factory of control code for an AI worker that doesn't need the cage. The more you didn't trust the model, the more code you added. The more code you added, the more tests you needed to police it.

That assumption has inverted. LLM calls are now cheap and falling fast. Code is now the inflexible, expensive part — logic frozen in syntax the day you wrote it, requiring tests to police it, requiring engineers to change it.

When behavior lives in instructions, you can edit it in plain English. When it lives in code, editing requires understanding every dependent path. The instruction layer is more readable, more flexible, and — tested properly through LLM evals — more reliable for tasks requiring contextual judgment.

The skill pack is the unit that makes this composable. Build something with the agent until it works, then "skillify it": the agent writes the markdown skill, its minimal code, its tests, its evals, and a resolver that routes future tasks to it automatically. You accumulate reusable capability rather than accumulating code.

The bottleneck shifts too. When code is the program, the bottleneck is how much you can build. When instructions are the program, the bottleneck becomes clarity, taste, and judgment — what is worth building and whether you can specify it precisely enough that the model converges on the right outcome. The engineer who writes the least code is often the one building the most.

## AI Integration

- The economic inversion is an AI-native architectural insight: as model intelligence and cheapness increase together, the optimal point on the code/instruction axis shifts toward instruction. This is not a one-time shift — it continues as models improve. Every new generation makes more of the code layer redundant.
- Skill packs are the first proposed primitive for agentic software engineering — analogous to functions, classes, or modules in traditional software, but instruction-first and eval-tested. The field is discovering its systems primitives in real time the way early CPU architecture invented the stack, heap, and registers.
- LLM evals as the testing primitive is the key shift in quality assurance: instead of unit tests checking code logic, you evaluate whether the model's output satisfies the skill's intent — a fundamentally different and more honest kind of correctness check for judgment-dependent tasks.
- The "thin deterministic layer" is the core design question for any JIT system: what genuinely needs to be code (I/O, hard constraints, guaranteed non-hallucination) vs. what can be an instruction? Getting this boundary wrong in either direction produces failure — too much code and you're back in the factory; too little and you lose the hard guarantees.
- Just-in-time software directly addresses [[hallucinated-agency]]: by keeping the LLM in the execution path rather than replacing its judgment with code proxies, you get the model's actual contextual reasoning rather than a frozen approximation of it.
- Tokenmaxxing is the financial corollary: spending freely on tokens now buys a market lead measured in years, because model costs are collapsing quarterly. Organizations still rationing tokens are optimizing for economics that no longer exist.

## Related Concepts

- [harness-engineering](harness-engineering.md) — the thin harness is the runtime environment that runs the skill packs; JIT software defines what lives in the instruction layer vs. code layer
- [agentic-workflow](agentic-workflow.md) — JIT software is the architectural substrate that makes scalable agentic workflows practical; skill packs are the reusable units agentic loops draw on
- [hallucinated-agency](hallucinated-agency.md) — JIT software keeps the model in the loop rather than replacing it with code proxies that can't reason about context
- [cognitive-externalization](cognitive-externalization.md) — instructions-as-program is a form of cognitive externalization: intent lives outside the model in persistent, editable, versioned form

## Open Questions

- How do you meaningfully diff and version-control a skill pack when the "code" is natural language? What does a regression look like in a markdown skill?
- At what complexity level does a natural language instruction layer become unmaintainable — when does it need to be refactored back into structured code?
- How do LLM evals compose across skill packs? Can you detect when one skill's change breaks another's downstream outputs?
- Is the skill pack genuinely a new software primitive, or is it a prompt management system by another name — and does that distinction matter?
- As models improve, what is today's "must be deterministic code" that could safely migrate to the instruction layer in two years?

## Project Connections

Side Quest AI Step 6 (fact database + hard-constraint validator) is exactly the thin/fat boundary question: what goes into the thin deterministic layer (hard constraints: locations must exist, NPCs must be alive, items must be real) vs. what stays in the instruction layer (quest narrative, contextual judgment, tone matching). The quest generator is already instruction-first; Step 6 is about making the deterministic boundary explicit and testable. Each template in quest-templates.md is a candidate skill pack — markdown skill plus minimal validation code plus an LLM eval that checks whether the recognition line lands. See [wiki/projects/game/PROJECT-CONTEXT.md](../projects/game/PROJECT-CONTEXT.md).
