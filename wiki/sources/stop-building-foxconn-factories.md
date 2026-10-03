---
type: article
title: Stop Building Foxconn Factories for Your Agents
url: https://x.com/garrytan/status/2061454423034110372
author: Garry Tan
published: 2026-06-01
ingested: 2026-06-24
tags: [ai, llm, agents, architecture, engineering, software-design]
concepts: [just-in-time-software, harness-engineering]
---

## Summary

Garry Tan reflects on building Garry's List — 540,000 lines of Rails code — and names it a Foxconn factory: hyper-vigilant control code wrapping an AI worker that didn't need the cage. The old economics (LLM calls expensive, code cheap) forced that architecture. That equation has inverted: LLM calls are now cheap and improving; code is now the inflexible, expensive part. The new paradigm is just-in-time software — behavior expressed in markdown instructions, versioned and tested, with only a thin deterministic code layer for I/O and hard constraints. The primitive unit is the skill pack: a markdown skill, minimal code, tests, an LLM eval, and a resolver that routes the agent to the skill automatically. Tokenmaxxing — spending on tokens freely — is the price of entry to living two to three years ahead of the market.

## Key Points

- 540,000 lines split into ~262k application code and ~276k tests policing it — the audit committee was bigger than the company
- The Foxconn factory anti-pattern: retry loops, validators, sanitizers, 127 background jobs — all bets that the model will fail; those bets are now wrong
- Economic inversion: LLM calls were expensive → build lots of code to ration them; now LLM calls are cheap → minimal code, instructions as the program
- Just-in-time software: intent expressed in markdown, behavior editable in plain language rather than logic frozen in code the day you wrote it
- Skill pack as the new primitive: markdown skill + minimal TypeScript + unit test + LLM eval + integration test + resolver + eval for the resolver
- "Skillify it" — one-word command that converts a working agent session into a testable, reusable skill pack
- Tokenmaxxing: willingness to spend freely on tokens is the differentiator; $100K in tokens now buys a 2–3 year market lead
- The bottleneck shifts from capability (how much you can build) to clarity, taste, and judgment (what is worth building)

## Quotes

> "We were writing code to babysit a thing that is now smarter than the code."

> "The scarce resource becomes clarity, taste, and judgment."

> "A control system is polished because control needs total control, a Foxconn factory. A free system is rough because it trusts you to finish it."

> "When you can turn intent directly into working, tested, reusable systems, the bottleneck stops being how much you can build and starts being what you actually want and whether it's worth building."

## My Take

This article names the mental model lag as the real failure mode. The tools changed but the 2013 engineer's instincts didn't. Every retry loop, every validator, every sanitizer is a bet that the model will fail — bets that are now systematically wrong.

The AI lens: this is fundamentally about what layer intelligence should live in. Old architecture: intelligence is frozen in code, model is a finite rationed resource called rarely. New architecture: intelligence lives in natural language instructions (alive, editable, composable), code is only for the parts that genuinely must not hallucinate. The model is now the substrate, not the scarce resource.

The skill pack is directly applicable to Side Quest AI: the quest generator, the NPC fact validator, and the consistency checker are each candidates for a skill pack rather than a monolithic code module. The "thin deterministic layer" maps exactly to Step 6 (fact database + hard-constraint validator) — what goes into deterministic code vs. what stays in the instruction layer is precisely the architectural question we're working through. The validator is thin code; the quest generator is fat skill.

Tokenmaxxing reframes the Haiku budget question: the cost we're being cautious about is not the constraint it feels like. Spending more on tokens now and building better skill packs earlier is the dominant strategy.
