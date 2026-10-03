---
type: article
title: The Principles of Getting Ahead
url: https://x.com/0xHvdes/status/2098009222302540086
author: "@0xHvdes"
published: 2026-09-10
ingested: 2026-09-11
tags: [economics, systems, behavior, psychology, decision-making, agents, distribution]
concepts: [leverage]
---

## Summary

The article opens with two people of similar age, intelligence and available hours whose lives
diverge sharply over five years, and argues the gap is explained less by luck, talent or
discipline than by the *kind* of actions each chose — because some actions move you
disproportionately further than others. It then lays out seven principles. Seek **asymmetric
opportunities**, where the possible gain is far larger than the cost of attempting it, on the
venture-capital logic that a few exceptional outcomes offset many failures. Build **leverage** —
code, content, capital, products, systems, teams — so that output is no longer bounded by hours
worked. **Get closer to opportunity**, because opportunity is unevenly distributed and you
cannot act on what you never encounter; the internet makes this proximity less geographic than
it used to be. Become **easy to bet on** by accumulating visible evidence — shipped work,
published writing, kept promises, people willing to vouch — which reduces the uncertainty
someone takes on when they hire, fund or recommend you. Play **games that compound**, where
yesterday's work makes today's work more valuable rather than resetting each morning.
**Combine skills instead of competing**, using Scott Adams's "talent stack" idea: being top-10%
at several useful things that multiply each other is rarer than being world-class at one.
And **increase your surface area for luck** by raising the number of attempts, since exposure
to chance is controllable even when chance is not. The closing claim is that not every decision
needs to pay off — only a few need to change your trajectory.

## Key Points

- The organising distinction is between actions with a predictable, capped exchange rate (an
  hour in, an hour paid) and actions whose **range of possible outcomes** is wide. Effort is held
  constant in the article's examples; what changes is the shape of the payoff.
- Explicit portfolio logic: "if ten experiments cost you a few weekends and nine go nowhere, the
  tenth can still make the entire equation worth it." Compared unfavourably against "spending
  years optimizing something with a tightly capped upside," where perfect execution still caps
  out.
- Leverage is defined as "using something beyond your own time to multiply the output of your
  effort," with the pre-internet baseline stated as a tight coupling between hours and output —
  the farmer's land, the craftsman's output, the teacher's room.
- Proximity is framed as an **information** problem, not a status one: around twenty people
  building companies you constantly hear about tools, industries, customers and problems; around
  twenty people uninterested in those things, the same opportunities never enter your field of
  view.
- "Easy to bet on" is framed from the *bettor's* side. Two equally skilled developers are not
  equally easy to bet on if one has shipped three products, contributed to open source, written
  about what they learned, and has people willing to recommend them — that person has reduced
  someone else's uncertainty.
- Compounding is distinguished from mere accumulation: it "doesn't only increase what you have,
  it changes how easily you can get more of it." A reputation makes the next introduction
  easier; an audience makes the next piece easier to distribute.
- The talent stack argument is about **comparability**, not excellence — five individually
  unremarkable skills make a person hard to find, and skills multiply rather than add (a
  developer who understands sales builds things people want).
- Luck is treated as exposure management: the attempts are visible to you, the successes are all
  outsiders see, "so those moments often look like luck."

## Quotes

> Some actions simply move you further than others.

> You don't need extraordinary results from everything you do. You need enough exposure to
> things capable of producing extraordinary results.

> You can't act on an opportunity you never encounter.

> Being good creates value. Making it easy for others to see that you're good creates
> opportunity.

> The best games get easier to win the longer you play them.

> You don't always need to become the best. Sometimes you need to become difficult to compare.

> You can't manufacture luck on command. But you can give luck more chances to find you.

## My Take

This is a competent compression of an existing genre rather than a new argument — the leverage
taxonomy is Naval Ravikant's, the talent stack is credited to Adams, and the asymmetry section
is the venture-portfolio logic this wiki already holds in more depth at
[power-laws](../concepts/power-laws.md), which covers the same VC arithmetic and adds the
sharper version of the point: in a normal-distribution domain consistency wins, in a power-law
domain persistence does. Section VII ("surface area for luck") is really section I restated as
volume, and the article half-admits it by linking out rather than developing it. The genuinely
underserved idea here is **leverage**, which is why that is the concept extracted.

The structural blind spot is the cost of attempts *to the person making them*. "Ten experiments
cost you a few weekends" assumes slack — savings, time, a floor to land on. The asymmetry
argument is conditioned on a bounded downside, and for a lot of people the downside isn't
bounded; a failed bet costs rent. This wiki already has the formal version of what the article
is missing: [failure-cost-asymmetry](../concepts/failure-cost-asymmetry.md) shows that
experimentation is governed by how expensive it is to *stop*, not how attractive the upside is.
The article optimises the upside term and never names the exit-cost term, which is the one that
actually gates behaviour.

**The AI intersection, which the article gestures at once and then drops** (AI appears only as
one item in a talent stack), is where this gets interesting:

1. **AI is the first leverage class that acts rather than stores.** Code, content and capital
   are static artifacts: they multiply past work by re-executing a response their author
   anticipated in advance. An agent responds to situations nobody enumerated. That is a
   categorical addition to the taxonomy the article inherits, and it breaks the article's own
   arithmetic — "one hour can create ten hours of value" assumes a fixed multiplier on stored
   work, whereas an artifact that keeps *making decisions* has no such ceiling.
2. **AI attacks the talent stack from both ends simultaneously.** It makes assembling a broad
   stack cheap — anyone can now reach roughly top-decile *execution* in writing, design, or
   code — which destroys exactly the scarcity the stack depended on. The article's own example
   stack (writing + marketing + sales + understanding AI + audience-building) is precisely the
   commoditised layer. What stays scarce moves to taste, domain context, and distribution, so
   the principle survives while its illustrations expire.
3. **"Easy to bet on" inverts under generative abundance.** The mechanism is that visible
   artifacts reduce a bettor's uncertainty. When artifacts become cheap to generate, they stop
   carrying that information, verification cost rises, and the signal migrates to what cannot be
   synthesised: named people who will vouch for you, things with real users, promises kept
   across time. So "publish your work" quietly loses potency while "keep your promises" gains
   it — and reputation becomes *more* valuable, not less. The article lists those five actions as
   equivalent; under AI they are no longer equivalent.
4. **Sections I and VII are an exploration policy, which is directly transferable to agent
   design.** Take many cheap reversible bets, accept that most fail, size exposure to the tail.
   That is the same problem as action selection under uncertainty in an agent harness — and
   pairing it with failure-cost-asymmetry gives the complete rule: an agent explores in
   proportion to how cheap *abandonment* is, not how large the upside is. An agent that must
   discard a large context, re-plan expensively, or emit a user-visible "I was wrong" will
   under-explore no matter how attractive the payoff.
5. **Proximity (III) is a retrieval problem in disguise.** "You can't act on an opportunity you
   never encounter" is precisely the constraint on an agent whose effective intelligence is
   bounded by what enters its context window, regardless of the model's capability. The social
   version and the machine version have the same shape, and the same fix: engineer what passes
   through your input stream rather than trying to think harder about what's already there.

On the project side, this lands on a live *open question* rather than a hypothetical: Attractor
ruled out both app stores on 2026-09-11 and has not chosen a replacement channel. The pending
call is exactly a leverage-and-proximity one — a store is granted leverage with a gatekeeper, a
fee, and in Play's case a required audience on a platform the project doesn't have, against a
plain URL that is permissionless and zero-marginal-cost. And the article's central
warning is the one this wiki already records as the known weakness: roastmycvai.com worked
technically and failed on distribution. "The world can't reward skills it doesn't know you have"
is that failure restated.
