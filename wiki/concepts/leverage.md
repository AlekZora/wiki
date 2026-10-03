---
type: concept
title: Leverage
aliases:
  - permissionless leverage
  - output decoupled from time
  - multiplier artifacts
  - non-time inputs
tags:
  - economics
  - systems
  - agents
  - distribution
  - decision-making
  - engineering
  - behavior
sources:
  - ../sources/principles-of-getting-ahead-hvdes.md
updated: 2026-09-11
---

## Definition

Leverage is the use of some input other than your own time — code, written or recorded content,
capital, a product, a system, other people — to break the proportionality between hours worked
and output produced. Without leverage, output stops when you stop: a craftsman makes as many
objects as he has hours, a teacher reaches as many students as fit in the room. With leverage, a
single unit of work keeps producing after the work is finished, so the same hour can yield
radically different amounts of value depending on what it was spent building. The distinguishing
property is not size of effect but **persistence without the author present.**

A useful sub-distinction, originally Naval Ravikant's: some leverage is **permissionless** and
some is not. Capital and labour must be granted by someone — an investor, an employer, a person
who agrees to work for you. Code and content require no one's approval, which makes them the
only forms an individual can acquire unilaterally.

## How I Think About It

The word gets used loosely to mean "anything that helps," which drains it. The test I apply is
narrower: *does this keep working while I am asleep, and does it do so without me having to be
re-consulted?* A consulting relationship that pays well is not leverage — it is a good hourly
rate. A template that lets me do the same work in a third of the time is only weak leverage,
because it still needs me in the loop for every instance. A published artifact that someone
finds and uses in three years, with no involvement from me, is the real thing.

The second thing I keep separate is **leverage versus compounding**, which most treatments of
this idea run together. Leverage makes output exceed input in the present. Compounding makes
*future* leverage cheaper to acquire — a reputation makes the next introduction easier, an
audience makes the next piece easier to distribute, existing knowledge makes the next skill
faster to learn. They are different mechanisms and they fail differently. You can have leverage
without compounding (a one-off viral piece that leaves nothing behind) and compounding without
much leverage (a slowly accumulating professional reputation that still bills hourly). The
combination is what produces the divergence between two people working equally hard.

The constraint that the optimistic framings skip: **leverage amplifies whatever judgment
produced it, including bad judgment.** An artifact that encodes a decision once and re-executes
it without the decider is a wonderful thing when the decision was right and a distribution
mechanism for error when it wasn't. The cost of being wrong scales with exactly the same
multiplier as the benefit of being right, which means leverage raises the return on judgment far
more than it raises the return on effort. That is the actual reason it separates people: not
that some work harder, but that leverage prices thinking rather than labour.

## AI Integration

- **An agent is the first leverage class that acts rather than stores, and that is a categorical
  addition, not an incremental one.** Code, content and capital are static: they multiply past
  work by re-executing a response their author anticipated in advance. A conditional was written
  down, and the artifact honours it. An agent responds to situations nobody enumerated. This
  breaks the standard arithmetic of leverage — "one hour can produce ten hours of value" assumes
  a fixed multiplier on stored work, whereas an artifact that keeps *making decisions* has no
  such ceiling and also no such guarantee.
- **AI commoditises the production of leverage artifacts, which moves the advantage to
  distribution and judgment.** If code and content are the two permissionless forms, and both
  become cheap to generate at reasonable quality, then possessing them stops being
  differentiating. What remains scarce is knowing which artifact is worth making and being able
  to get it in front of anyone — so the binding constraint migrates from production to taste and
  distribution. Any strategy built on "acquire code or content leverage" needs re-deriving under
  this condition, because the scarcity it assumed has moved.
- **For agent design, the leverage frame explains why harness and tooling dominate raw
  capability.** An agent's output ceiling is set by what it can act *through*, not by how well it
  reasons — the same structural claim as "without leverage your output is bounded by your time."
  A highly capable model with no tools is a craftsman with no land. This is the economic
  restatement of [harness-engineering](harness-engineering.md), and it predicts that marginal
  investment in what an agent can reach will usually beat marginal investment in how well it
  thinks.
- **[Cognitive externalization](cognitive-externalization.md) is the inward-facing twin of
  leverage.** Both relocate work into persistent external structures; the difference is who the
  beneficiary is. Leverage points the artifact at the world and collects returns from strangers.
  Externalized memory, skills and protocols point the artifact at the agent's own future work and
  collect returns from its later self. The same mechanism, aimed differently — which suggests
  that an agent's memory store should be evaluated on leverage terms: does it keep paying without
  being re-consulted, or does it require the agent to re-derive its contents each time?
- **What this reveals about intelligence:** leverage is externalized cognition that persists. The
  property that makes an artifact leverage — it encodes a decision once and re-executes it
  without the decider — is also a definition of a **policy**. That equivalence carries the risk
  profile with it: a wrong policy operating at scale is the canonical failure mode of both
  leveraged human work and deployed AI systems, and in both cases the fix is not to reduce the
  multiplier but to raise the quality of the encoded decision and keep it cheap to revoke.

## Related Concepts

- [Power Laws](power-laws.md) — leverage is what makes a power-law payoff *reachable*; power
  laws describe the distribution of outcomes, leverage describes the mechanism that lets one
  person's single action land in the fat tail
- [Failure Cost Asymmetry](failure-cost-asymmetry.md) — the necessary counterweight: leverage
  argues for bigger upside, exit cost determines whether the bet gets attempted at all. A
  leveraged bet that is expensive to abandon will be avoided regardless of its multiplier
- [Cognitive Externalization](cognitive-externalization.md) — the same relocation of work into
  persistent artifacts, aimed at the agent's own future rather than at the world
- [Harness Engineering](harness-engineering.md) — the agent-side instance: an agent's leverage
  is its tools, and its output ceiling sits there rather than in its reasoning
- [Network Effects vs. Word-of-Mouth Diffusion](network-effects-vs-wom-diffusion.md) — how
  content leverage actually propagates once it exists, and why possessing a distributable
  artifact is not the same as distributing it

## Open Questions

- Is "acts rather than stores" a genuinely new leverage class or just a faster feedback loop on
  the existing code class? The test would be whether agent leverage produces returns in
  situations its author could not have enumerated — if every profitable agent action turns out
  to be one a sufficiently thorough author would have scripted, the distinction collapses.
- If AI commoditises both permissionless forms (code and content), does *permissionless* leverage
  stop being the individual's advantage and revert the advantage to the granted forms — capital
  and labour — which AI does not obviously cheapen? That would reverse fifteen years of
  "anyone can build and publish" strategy advice.
- Does leverage have a measurable exit cost, in the failure-cost-asymmetry sense? A published
  artifact is hard to un-publish and a deployed agent is hard to recall, which suggests
  high-leverage work is systematically *harder* to abandon — and therefore systematically
  under-attempted by anyone reasoning about exit cost rather than upside.
- For an agent memory store: what is the equivalent of "keeps working while you sleep"? Is a
  memory that must be retrieved, re-read and re-interpreted on every use leverage at all, or
  merely a faster form of re-derivation?

## Project Connections

**Attractor, 2026-09-11 — a live and still-open distribution question.** Both app stores were
ruled out (Google Play rejected, Apple deferred) and **no replacement channel has been chosen**;
itch.io is the only one in use. The concept is the right lens for the pending decision — a store
is *granted* leverage, with a gatekeeper, a fee, and in Play's case a required audience on a
platform the project does not have, whereas a plain URL is permissionless and zero-marginal-cost.
That framing argues for the web, but the choice is the user's and is not made. Record:
`wiki/decisions/decision-log.md` (2026-09-11).

The concept also names the project's known weakness precisely: roastmycvai.com was built
leverage that was never distributed — leverage in the artifact and none in the channel.
