---
type: concept
title: Diminishing Research Returns (Ideas Getting Harder to Find)
aliases: [research productivity decline, semi-endogenous growth, ideas getting harder to find, Red Queen growth]
tags: [economics, growth-theory, innovation, ai, scaling, research, systems]
sources: [ideas-getting-harder-to-find-bloom]
updated: 2026-07-15
---

## Definition

Research productivity — new ideas produced per researcher — falls over time in essentially every domain it's been measured: semiconductors, crop yields, drug discovery, firm-level R&D, the aggregate economy. Because of this, sustaining a *constant rate* of exponential progress in any field requires an *exponentially growing* amount of research effort. Formally (semi-endogenous growth theory): Ȧ/A = α·A^(−β)·S, where A is the accumulated stock of ideas/quality, S is research effort, and β governs how quickly diminishing returns bite as A grows. The larger β is, the faster a domain's low-hanging fruit gets picked and the more effort each subsequent unit of progress costs. Growth doesn't have to slow down as a result — but only if research effort itself keeps growing to offset the decline. This is a "Red Queen" dynamic: you have to run faster and faster just to hold your position.

## How I Think About It

This is a general law of motion for any cumulative knowledge-generation process, not a special fact about economics. The more a field already knows or has built, the more it costs to find the next increment — not because researchers get worse or lazier, but structurally: the size of the existing stock (A) is itself what raises the cost of the next dA. Obvious extensions get filled in first; what's left requires synthesizing more prior knowledge just to reach the frontier. The useful move this concept gives you is to stop treating "growth slowed down" as evidence of stagnation or lost talent, and instead ask two separate questions: (1) is the domain's β genuinely large (hard to get more diminishing returns out of it), or (2) has research effort simply stopped growing fast enough to offset a β that hasn't changed? Those have very different implications and very different fixes.

## AI Integration

- Neural scaling laws (Kaplan et al. 2020; Chinchilla, 2022) are the same functional form applied to model training: loss falls as a power law in compute/data/parameters, so constant-rate capability gains require exponentially increasing compute — structurally identical to the β in this framework. The "are scaling laws slowing down" debate in frontier AI is a live instance of the exact question this concept asks about semiconductors, crops, and drugs.
- Semiconductors are the empirical case with the *smallest* measured diminishing returns (β≈0.2 in Bloom et al.) of anything studied, yet productivity still falls fastest there because research effort in that sector has grown the fastest of all. Chips are also the substrate AI training rides on — as Moore's Law-driven density gains slow, that's an exogenous drag layered under AI's own scaling curve, part of why the field has pivoted so hard toward algorithmic efficiency and inference-time (test-time) compute: channels that haven't yet hit the same wall.
- The most consequential angle: any research-effort input that goes unmeasured gets silently absorbed into the reported productivity decline. AI-as-researcher — automated hypothesis generation, experiment design, verification loops — is exactly this kind of input, deployed deliberately. If AI can substitute for or augment the "S" term (the researchers doing the work) without the wage and training-time cost of growing the human research population, it's a genuine candidate for the first structural break in a trend that's held since the 1930s: decoupling "more effective research effort" from "more human capital," which is the actual bottleneck the equation describes.
- Any system that accumulates state over time — a knowledge base, a codebase, an agent's memory store — should expect this curve by default. As accumulated state grows, the marginal value of the next unit of undirected search/scanning effort tends to fall, unless the system raises its own effective β by making retrieval and synthesis more targeted rather than broader. This is a useful skepticism check on "just add more compute / more scanning" as a strategy for anything cumulative, including agent memory and long-running knowledge systems.
- Frames agent self-improvement loops usefully: if an agent's own capability is the accumulating "state" being improved, naive self-improvement should predict decelerating returns by default — unless something exogenous enters the loop (better tooling, verified environments, new external data) rather than the system just recursively consuming its own output.

## Related Concepts

- [Power Laws](power-laws.md) — the functional-form cousin: both describe how outcomes concentrate/decay nonlinearly as a system scales, though power laws in VC returns describe outcome *distribution* while this concept describes the *cost curve* of producing outcomes at all.
- [World Models](world-models.md) — tangential: both concern how the cost/value of the next increment of a system changes as its accumulated internal state grows.

## Open Questions

- Does AI-as-researcher (automated hypothesis generation + verification loops, e.g. AI-scientist-style systems) actually raise the *effective* number of researchers enough to offset β, or does it just relabel the same diminishing curve under a new label?
- Is there a measurable β for LLM capability progress itself, and has it visibly shifted since compute/data scaling started running into practical limits (~2024–2025)? If so, in which direction?
- Within a single accumulating knowledge system (this wiki, an agent's memory store), is there a way to detect in practice when you've crossed from "low β, cheap to keep growing" into "high β, next increment is expensive" — before productivity visibly drops?
