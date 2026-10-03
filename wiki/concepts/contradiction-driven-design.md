---
type: concept
title: Contradiction-Driven Design
aliases: [TRIZ, inventive contradiction, technical contradiction, physical contradiction, ideal final result, IFR, ARIZ, no-compromise solution, separation principles, psychological inertia]
tags: [engineering, creativity, systems, design, problem-solving, psychology, ai, agents]
sources:
  - "../sources/And Suddenly the Inventor Appeared - TRIZ, the Theory of Inventive Problem Solving (Genrich Altshuller) (z-library.sk, 1lib.sk, z-lib.sk).md"
updated: 2026-09-21
---

## Definition

A method for stating a problem as a **contradiction** rather than a trade-off, and then treating
any compromise between the two sides as a failed answer. It is the operating core of TRIZ, the
Theory of Inventive Problem Solving, which Genrich Altshuller began building in the USSR in 1946
out of an analysis of tens of thousands of patents.

Two forms, and the distinction does the work:

- **Technical contradiction** — improving one part of a system impairs another part or an
  adjacent system. This is the ordinary engineering trade-off, stated at system level.
- **Physical contradiction** — a single element must have property A *and* property not-A. The
  rubber hose must be hard enough to drill and soft enough to be a hose.

The method's characteristic move is to push a technical contradiction *down* into a physical one
— to sharpen a diffuse trade-off until it becomes a flat impossibility about one component. The
impossibility is then dissolved by **separation**: in time, in space, between the whole and its
parts, or by condition. Freeze water inside the hose, drill it, let it thaw; it is hard and soft
at different times, so it never has to be both at once. Altshuller's non-technical example is
Carl the Great taking the crown from the Pope's hands to place it on his own head — the same
contradictory requirement separated in space and in time.

Two supporting pieces travel with it. The **Ideal Final Result (IFR)** is a steering heuristic:
before searching, state the perfect outcome as though no mechanism were required — "the roof
opens up by itself as the temperature rises" — on the principle that *the ideal machine is no
machine*, the function performed with nothing added. And **psychological inertia** is the named
obstacle: the inability to think past the existing system, which TRIZ attacks with explicit
operators rather than with inspiration.

## How I Think About It

**The bet is that most trade-off curves are artifacts.** A trade-off assumes you must sit
somewhere on a curve and the only question is where. TRIZ's claim is that the curve usually
exists because nobody asked *when*, *where*, or *at what scale* each property actually has to
hold — and that once you ask, the curve stops being a curve. The frozen hose is not a better
point on the hard/soft trade-off; it deletes the trade-off. This is a strong and falsifiable
claim, and it is sometimes false: some contradictions are genuinely simultaneous and physical,
and the method has no way to tell you in advance which kind you are holding. What it does
guarantee is that you will find out by trying to separate it, which is cheap.

**The real content is that the contradiction is a search index.** Everyone already knows
problems contain conflicts. What Altshuller actually built was a *lookup scheme*: formulate the
contradiction in a canonical form, and it becomes a key into a library of solutions abstracted
from prior art — a Table of Typical Methods derived from over 40,000 patents, a table of
physical effects, a table of S-Field transformations, and 80-plus "Standards" for recurring
problem shapes. Read that way, TRIZ is a retrieval system over other people's inventions,
wearing the clothes of a theory of creativity. The famous line — *"To solve an inventive problem
it is not as important to have so much knowledge as it is to organize the knowledge that one
already has"* (p. 81) — is a statement about indexing, not about genius.

**Which relocates the entire difficulty onto problem formulation.** The lookup is mechanical;
choosing what to look up is not. Deciding which of a dozen entangled conflicts is *the*
contradiction, and at which system level to state it, is the step the book demonstrates
beautifully and never actually teaches — every worked example arrives with its contradiction
already correctly named, and every one of them looks inevitable in hindsight. This is the
standard expert-system problem: the index is only as good as the query, and writing the query is
the job.

**IFR is a relaxed-problem heuristic, and that is the precise description.** Ordinary problem
solving searches forward from what is currently possible, which means the reachable set is
bounded by present assumptions before the search begins. IFR reverses the order — solve the
problem with every constraint deleted ("it happens by itself"), then walk back toward
feasibility, treating each thing you are forced to add as a defect to be justified. The
structure is identical to delete-relaxation heuristics in automated planning: solve an easier
version you know to be unreachable, and use its shape to steer the real search. The useful
property is that it never quietly underestimates the target — the guidance always points past
what you currently think is achievable.

**The inertia operators are the part the vault did not already have.** The vault documents
expert blindness well — the Einstellung effect in
[wicked-vs-kind-learning-environments.md](wicked-vs-kind-learning-environments.md), and the
whole liability half of [outsider-advantage.md](outsider-advantage.md), where experts "literally
can't see what a generalist would notice." Both describe the condition. TRIZ supplies
countermeasures an insider can run on themselves:

- **Operator STC** — mentally push Size, Time and Cost to extremes, not to find the answer but
  to break the image of the existing system. Shrinking conveyor rollers toward the size of atoms
  is what produced floating the glass ribbon on molten tin. The book is explicit that the
  operator *"is not supposed to give you the answer"* (p. 102).
- **Restate in plain words.** A technical term carries assumptions as cargo: "icebreaker"
  contains a ship that breaks ice. "A thing should freely pass through the ice" contains neither.
- **Model with Miniature Dwarfs** — picture the object as a crowd of tiny reconfigurable beings.
  The stated reason is the sharp one: it *replaces empathy*. Imagining yourself as the part
  makes you refuse to consider tearing it in half, so self-identification with the object is a
  constraint you did not know you had adopted.

That set is the trainable form of the outsider advantage — deliberately simulating not-knowing
instead of waiting to be an outsider. It belongs to the same family as that page's
manufactured-instrument move: converting something that reads as biography into a procedure.

**The evolution laws are the weakest claim and still worth keeping for one thing.** Systems are
said to pass through four periods — selection of parts, improvement of parts, dynamization,
self-development — under a Law of Increasing Dynamization that carries them from rigid
connections toward flexible, fragmented, and finally field-mediated ones (the roly-poly's weight
going from fixed, to moveable, to sand). As prediction this is retrodiction: it was derived from
patents that were granted, which is the same sampling-on-success problem
[outsider-advantage.md](outsider-advantage.md) names about its own sources. What survives the
objection is the *stopping rule* — *"the system should exhaust its resources before it moves to
the microlevel"* (p. 98) — which answers a question most methods duck: when to stop improving
the thing you have and switch principles. Getting that wrong is expensive in the observable
direction too. Presniakov's electromagnetic-pump boat was ahead of its system's exhaustion point
and the patent was refused for fourteen years.

**The honest cost.** Altshuller frames trial and error as an archaic relic, and the book's proof
is a long parade of solved problems presented after the fact. A catalogue of 27 methods plus 80
standards is not self-evidently cheaper to search than the problem itself, and the tell is
visible in the answers section: the same few moves recur far past the point of coincidence — add
ferromagnetic powder and control it with a magnetic field, change the phase state, introduce a
temporary substance that later burns off, make a copy and work with the copy. An operator
catalogue is also a prior, and a prior strong enough to solve quickly is strong enough to narrow
what you consider. That is mode collapse in a 1996 paperback.

## AI Integration

- **ARIZ is an agent loop that spent fifty years without an interpreter.** It has exactly the
  shape: named stages, an explicit intermediate representation (reduce the situation to a
  *Tool* acting on a *Product*, discard everything else), an operator table, and a termination
  condition. The single reason it was never automated is that every step demands open-ended
  semantic judgment — read an ambiguous situation, decide which conflict is load-bearing, decide
  whether a candidate counts as compromise. That is the specific constraint that changed. ARIZ
  is worth reading as a pre-existing, patent-validated specification for a design agent's
  scaffold, which is more than most agent architectures have behind them.
- **But the half that was easy to automate already was, and that is the honest evidence.** By
  1996 the book already lists Invention Machine, Ideation International, and Technical
  Innovation Center selling TRIZ software. Matching a canonical contradiction against a solution
  table is a database join; it was automatable in the nineties and it was automated. Thirty
  years later invention is not solved. The untouched half was always formulation — which is the
  same conclusion [outsider-advantage.md](outsider-advantage.md) reaches from the other
  direction: when the generative step gets cheap, the binding constraint moves to selection and
  taste. TRIZ is a clean natural experiment for that claim, run early.
- **IFR is directly usable as goal specification for agents.** "State the result as though no
  mechanism were needed" is a precise instruction for separating objective from implementation,
  and over-specified method is one of the reliable ways agent instructions fail — they pin the
  approach and thereby delete the solutions worth having. "The roof opens by itself" is a
  better-formed goal than any description of a roof-opening mechanism, for a model for the same
  reason it was for an engineer.
- **The no-compromise rule is a cheap, testable generation constraint.** A model asked to solve
  a design problem will overwhelmingly propose the compromise, because compromise is what the
  training corpus contains: published engineering is mostly trade-off curves and defensible
  optima. Forcing physical-contradiction formulation first, and rejecting any answer that names
  a trade-off, is a one-line constraint with a measurable prediction — that it shifts the
  distribution of proposals, not just their phrasing. Nothing in the vault has tested this and
  it is a weekend-sized eval.
- **Psychological inertia has a model analogue, and porting the tools is not safe.** A model's
  inertia is the training distribution, not self-identification, so the mechanisms differ even
  where the prompts look identical. Operator STC roughly survives the translation — asking for a
  solution at an extreme of size, time, or cost changes which region of the corpus gets sampled.
  MMD does not. Its *form* ports beautifully into multi-agent decomposition ("treat the object
  as a crowd of tiny reconfigurable agents" is a swarm prompt), but its stated *purpose* was
  disabling an empathy constraint a model never had. A technique whose form transfers while its
  mechanism does not is the most deceptive kind to port, because it will look like it works.
- **What this reveals about intelligence.** Altshuller's actual empirical finding is that
  invention across tens of thousands of patents compresses to a few dozen recurring operators.
  If that holds, the space of inventive *moves* is vastly smaller than the space of inventions —
  unbounded surface variety generated by a small operator set applied to domain-specific
  substrate, which is structurally what a model is. It also predicts the capability profile:
  strong at applying known operators to substrates they have not been applied to (the bulk of
  all patents, and the bulk of all useful engineering), weak at producing a genuinely new
  operator — a limit Altshuller's own method shares, since the catalogue can only be harvested
  from inventions that already happened.

## Related Concepts

- [Outsider Advantage](outsider-advantage.md) — the same blindness from the opposite side: that
  page says the cure is arriving from elsewhere, this one says it can be run deliberately from
  inside. Both end up converting biography into procedure
- [Recognition-Primed Decision Making](recognition-primed-decision-making.md) — the closest
  structural cousin. RPD says experts match situations against an implicit prototype library and
  satisfice on the first workable match; TRIZ is that same architecture built *explicitly*, with
  the prototype library written down and the matching key standardised. The interesting
  difference is that RPD's version is unverbalizable and TRIZ's is teachable to sixth-graders
- [Paradox](paradox.md) — nearly identical structure in a different domain: a paradox "tells you
  where a system has overextended itself," and the prescribed response is to map the boundary
  rather than abandon the rule. A physical contradiction is the engineering instance
- [Elegance (Game Design)](elegance-game-design.md) — "the ideal machine is no machine" and
  maximum richness from minimum mechanics are the same ratio optimised in different units
- [Insight Learning](insight-learning.md) — the direct antagonist. Insight says the breakthrough
  arrives after incubation and cannot be forced; TRIZ says it can be scheduled. Both cannot be
  fully right, and the disagreement is testable
- [Creativity](creativity.md) — recombination as the shared mechanism; TRIZ is a claim that the
  recombination operators are enumerable
- [Diminishing Research Returns](diminishing-research-returns.md) — supplies the quantitative
  form of TRIZ's stopping rule: "exhaust the system's resources first" is a qualitative read of
  the same curve that says when the next increment costs more than a change of principle
- [Wicked vs. Kind Learning Environments](wicked-vs-kind-learning-environments.md) — source of
  the Einstellung mechanism the inertia operators are aimed at
- [Research Craft](research-craft.md) — the adjacent trainable practice; both treat method as
  something you run rather than something you have
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — where MMD's form lands, and where
  its mechanism does not follow

## Open Questions

- **What is the prospective hit rate?** Every case in the book is solved before it is shown, and
  the operator catalogue was harvested from patents that were granted. The method has never been
  presented here with a forward record — problems attempted, problems solved, against a control.
  This is the same missing denominator [outsider-advantage.md](outsider-advantage.md) names
  about its own sources, and it decides whether TRIZ is a method or a vocabulary.
- **Is contradiction formulation automatable, or is it the entire difficulty?** The retrieval
  half was automated in the 1990s and invention did not follow. If formulation also falls, the
  claim that invention is systematisable finally becomes testable rather than asserted.
- **Does no-compromise have a domain limit?** Separation in time and space is available to
  physical objects almost by default. Whether a social or economic contradiction separates the
  same way is unexamined — [rich-or-king-tradeoff.md](rich-or-king-tradeoff.md) is a concrete
  test case sitting in the vault, and the obvious question is whether it is genuinely
  simultaneous or merely never asked to separate in time.
- **Does Increasing Dynamization describe software?** Hardcoded → configurable → learned →
  prompted has the shape of rigid → flexible → fragmented → field-mediated. If the mapping
  holds, the law predicts the next period (self-development) for systems that are currently at
  the third. If it does not, the law is a fact about mechanical systems wearing a general name.
- **Is the 27-method catalogue itself elegant, or is it bloat?** By
  [elegance-game-design.md](elegance-game-design.md)'s own ratio, a method that needs 27 rules
  plus 80 standards plus four tables to generate its solution space is a poor score. The
  recurring ferromagnetic-powder answer suggests the *effective* operator set is far smaller
  than the documented one, which would be the more interesting finding.

## Project Connections

[Attractor](../projects/attractor/build-log.md) is a physical contradiction that the design
deliberately refuses to resolve. The single input must pull what saves you and what kills you,
with the same force, at the same moment — property A and not-A in one element, which is exactly
the form TRIZ exists to dissolve. Here dissolving it would destroy the game. That inversion is
worth stating plainly, because it marks the boundary of the method: engineering wants the
contradiction gone, and design wants it *preserved and handed to the player*. A game is a
machine for making someone else sit on the trade-off curve.

The one place separation does appear is in the campaign rather than the mechanic. The difficulty
curve — generous for roughly the first thirty seconds, then turning — is separation in time, and
[attractor-zone.md](../projects/attractor/attractor-zone.md) already converts it into in-fiction
truth: the Zone is generous at first, and that is how it keeps you.
