---
type: concept
title: Incentive-Aligned Infrastructure
aliases: [users-pay-suppliers-profit, aligned-monopoly, mechanism-design-for-public-goods]
tags: [systems, economics, engineering, incentives, agents, ai, design, infrastructure]
sources: [urban-expansion-age-of-liberalism]
updated: 2026-08-02
---

## Definition

A way of producing public goods that works neither by removing constraints nor by
specifying outcomes centrally, but by arranging the environment so that the
locally-optimising private actor produces the globally desirable result as a side effect of
pursuing its own interest. The nineteenth-century urban system is the worked example: cities
that expanded tenfold or more in a century did so under a regime that was heavily regulated
but structured so that building the public network was the profit-maximising move for the
people who had to build it. Its author states the principle as three rules — **users pay,
suppliers profit, spendthrift public bodies go bankrupt**.

The distinguishing move is that the designer changes the *payoff structure* rather than
issuing instructions. A city wanting a coherent street grid could build it (expensive),
mandate it (adversarial, slow, litigated), or publish a map, forbid building on the lines,
and make development permission conditional on grading and ceding them — after which every
landowner builds the city's plan voluntarily, because development is profitable and this is
the price. Only the third scales.

## How I Think About It

Three components recur, and all three have to be present.

**Exclude the competitor where competition destroys value.** Some goods are worse when
contested. Two railway companies serving the same corridor build duplicative track and
bankrupt each other; two bus firms race to reach the waiting passenger first. Hotelling's
Law predicts this — rivals converge toward the middle rather than differentiating, because
each gains by encroaching and loses nothing by abandoning the periphery it already
dominates. Granting one operator the whole network inverts the incentive: adding a service
now complements your existing services rather than cannibalising them, so the monopolist
spaces coverage efficiently on its own.

**Fund from users, not from taxes.** This is the discipline that keeps the first component
from becoming extraction. A monopolist funded by fees must produce something people will pay
for; a monopolist funded by appropriation need not. The nineteenth-century variants —
private franchise, municipal-owned concession, fully municipal *Stadtwerke* — differ in
ownership and agree entirely on this. Even city-owned works were run for profit, and were
often established *because* they were profitable.

**Make failure real.** Municipalities were not bailed out by national governments, so a city
that overbuilt went bankrupt and knew it. Remove this and the other two rot: the excluded
competitor cannot discipline you and the user fee stops being a constraint.

The fourth thing worth carrying is **how it died**, because the failure is more instructive
than the success. Nothing in the design was wrong. The system had silently encoded an
assumption about the world — that prices do not move — into its constants, because in a
zero-inflation economy a fare cap set once stays sustainable forever and may even improve as
productivity rises. When inflation resumed after 1914 the real value of every user fee
collapsed, and within a decade the self-funding transport sector was near ruin, entering the
automobile era financially crippled. The parameter was correct when set and never re-derived.
That is a distinct failure mode from a bad design, and no amount of testing the system
against itself would have found it.

## AI Integration

- **Constraint structures beat instruction sets for agent design.** The extension-plan
  mechanism is what a well-designed agent environment looks like: not a longer prompt
  enumerating desired behaviors, but a situation in which the desired behavior is what an
  agent pursuing its objective would do anyway. Most agent scaffolds reach for the
  instruction set first and then patch the cases it fails to cover. The alternative is to ask
  what the agent is actually optimising and to reshape the payoffs so the good path is also
  the cheap path — making the wrong action unavailable or unprofitable rather than
  forbidden.
- **Hotelling's Law names a real multi-agent failure.** Independent agents given the same
  objective over the same input converge rather than differentiate, duplicating coverage and
  wasting the parallelism they were spun up to provide. This is the market-failure form of
  the diversity problem, and it has the same solution the nineteenth century found: assign
  territory explicitly instead of hoping competition produces spread. Relevant wherever a
  system fans out to multiple agents and expects the union of their outputs to cover a space
  — research, search, generation of alternatives.
- **Hardcoded constants are undated assumptions about a moving world.** The inflation
  collapse generalises directly to AI engineering, where eval thresholds, token budgets,
  timeouts, latency targets, context-window assumptions and cost-per-call arithmetic are
  everywhere and are almost never revisited. Each encodes a snapshot of an unusually
  fast-moving environment. The pattern to watch for is not a parameter that was wrong when
  chosen — that gets caught — but one that was right when chosen and has never been
  re-derived. An explicit inventory of constants whose correctness depends on facts about the
  world, with the fact recorded next to the number, is a cheap defense.
- **User-pays as an alignment mechanism for AI services.** The undertaking-debt pattern —
  price high for ten to twenty years to repay build cost, then lower the cap toward operating
  cost — is close to the observed frontier-model cost curve, but arrived at by design rather
  than by competitive accident. It raises a real question about whether capability access
  should have an explicit schedule of this kind rather than whatever pricing competition
  produces.
- **What it reveals about systems generally.** The dichotomy between "regulate" and "leave
  alone" is usually false, and reaching for it is a sign the mechanism has not been designed.
  The interesting axis is not how much intervention but whether intervention is placed where
  it changes what the self-interested actor wants to do. This applies as much to a reward
  model or a tool-use policy as to a municipal government.

## Related Concepts

- [Game Theory](game-theory.md) — the formal apparatus; Hotelling's Law is a specific result
  within it, and this concept is its applied mechanism-design side
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — where the convergence failure
  bites, and where explicit territory assignment is the countermeasure
- [Metrics Trap](metrics-trap.md) — the adjacent failure: what happens when the aligned
  proxy becomes the target and the alignment silently inverts
- [Diffuse Preference Aggregation](diffuse-preference-aggregation.md) — the other half of the
  same historical story: what happens to a permissive system once distant preference acquires
  veto power
- [Regulatory Integrity](regulatory-integrity.md) — decay of the constraining layer as the
  leading indicator of trouble, which is what "spendthrift public bodies go bankrupt" is
  guarding against

## Open Questions

- Where is the boundary between an aligned monopoly and simple rent extraction? The
  nineteenth-century answer was time-limited franchises, price caps set high enough to fund
  investment but renegotiated at renewal, and genuine bankruptcy risk. Charles Yerkes built
  Chicago's tram system while bribing the Illinois legislature for a generous renewal, which
  suggests the mechanism tolerated a fair amount of capture before it stopped working.
- Constraint structures are harder to specify than instruction sets and fail differently —
  they produce unanticipated behavior that is nonetheless optimal given the payoffs. Is there
  a way to test a proposed constraint structure for its unintended optima short of running it?
- The system undersupplied exactly one thing: stability of neighborhood character, which
  people demonstrably wanted and paid premiums for via private covenants. Is there a general
  pattern where incentive-aligned systems reliably underprovide *predictability*, because
  nobody's fee captures it?
- Does "make failure real" survive at all in contexts where the operator is too important to
  fail? The nineteenth-century municipalities were small enough to go bankrupt without
  systemic consequence, which may be the load-bearing and least portable condition.

## Project Connections

The `fact-database-design.md` validator architecture is closer to an instruction set than a
constraint structure — hard constraints enumerate forbidden outputs and the recovery cascade
retries when one trips. The alternative framing is worth considering when the Godot bridge is
built: rather than generating freely and rejecting violations post hoc, shape the game state
handed to the planner so that the ungrounded quest is not the attractive completion in the
first place. The current design already gestures at this — the LLM reads world state and
never writes it — but the *pre-generation* assembly step (Phase A) is where payoff-shaping
would actually live.
