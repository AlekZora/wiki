---
type: concept
title: Representation Shapes the Solution
aliases: [notation as instrument, compression as diagnostic, the one-page constraint, representational intervention]
tags: [design, cognition, systems, abstraction, ai, llm, agents, visualization, problem-solving]
sources:
  - ../sources/gdc-one-page-design-v2.md
updated: 2026-09-22
---

## Definition

The form in which a problem is written down is not a neutral window onto it. It determines which
solutions are visible, which are expressible, and which never get considered — so changing the
representation changes the design, not merely its presentation. A second, sharper claim follows:
because the representation acts on the problem, *resistance* from the representation is
evidence. When a system cannot be expressed compactly in a form that has worked for comparable
systems, the most likely explanation is that the system is wrong, not that the form is too small.

## How I Think About It

Most talk about "good documentation" or "clear diagrams" assumes the design exists first and the
depiction comes after — the depiction can be clearer or muddier, but the thing depicted is
fixed. This concept denies that ordering. The clean demonstration is Stone Librande's robot
game: three factions arranged as rock-paper-scissors, one per corner of a triangle. Redrawn with
the factions along the *sides* instead of the corners, the same three factions became a
continuous space — a player could be "mostly scissors with a little rock." Nothing about the
game was reconsidered. A drawing was redrawn, and a discrete three-way choice became a tunable
spectrum. The design improved because the notation did.

The second mechanism is collapse. Spore's consequence system had four stages × four playstyles =
256 routes, maintained as a four-dimensional spreadsheet nobody could hold in their head.
Librande tried a radial diagram (elegant and *wrong* — a circle asserts that the two ends are
adjacent when they are not), then a split-fan version (truer, but a disordered colour spectrum
signalled that something was still off), and finally a vector formulation in which each choice
contributes a direction and choices sum. In that representation the 256 routes collapse to ~36
reachable outcomes, and a hand-typed lookup table becomes an algorithm. The combinatorics never
changed. The coordinate system did. Note the ordering, which is the part people skip: the
collapse was not available until the third representation, and the first two had to be *built*
and rejected to get there. This is not "choose the right abstraction up front"; it is a search,
and the wrong candidates are how you pay for it.

What makes this more than an aesthetic preference is the failure mode, which is where I think
the real value sits. Librande's rule — you know your design is bad when you can't get it onto
one page — converts a formatting constraint into a **diagnostic instrument**. Most constraints
of this kind are arbitrary and people route around them (use bigger paper, add a second page,
get a bigger monitor). The interesting move is to treat the constraint as a *test* and the
failure to satisfy it as a finding about the system. That only works if the constraint is
calibrated — one page is a real threshold precisely because comparable systems do fit — which is
also the thing that makes it falsifiable and the thing that makes it easy to fake.

The honest limit: this can rationalise sunk cost. "I couldn't fit it on a page, so the design is
wrong" is indistinguishable from "I couldn't fit it on a page, so I am not good at this
representation" without some independent check. Librande's implicit check is his own track
record across a decade of comparable systems. Someone without that baseline has a diagnostic
they cannot read.

## AI Integration

**The representation handed to a model is an intervention, not a view.** The structure of the
state you serialize into a prompt determines the reachable output space in the same way the
triangle's corners determined the reachable design space. This is usually discussed as prompt
formatting — a presentation concern — when it is actually the design surface. Practically: if
a fact is not in the representation, no amount of model capability recovers it; if it is in the
representation but unattached to anything the model can ground it in, the model will invent the
attachment. Both failure modes are properties of the drawing, not of the reasoning.

**Collapse versus enumeration is a live architectural choice.** The modern default when facing a
combinatorial space is to enumerate cases and let a model interpolate across them — more
examples, more few-shot cases, more eval rows. Librande's 256 → 36 is the opposite move: find
the geometry in which the cases are generated rather than listed, and replace the table with a
rule. The trade is well understood in the abstract (rules generalize and are auditable; tables
are precise and dumb) but the sequencing lesson is the transferable part — the generating rule
was not visible until the third representation, so "we couldn't find a rule, use a table" is
often a statement about how many representations were tried.

**The diagnostic is cheap to build and nobody builds it.** An automated critic that reports *this
state does not compress* — that a system's representation has outgrown a calibrated budget — is
a far better use of a model than generating the diagram. It targets the informative signal (the
resistance) rather than the artifact. This also inverts the instinctive response to context
pressure: the reflex is a larger context window, and the diagnostic reading is that an
irreducible context is evidence of a mis-factored system.

**Automating the artifact destroys the mechanism.** The value in Librande's practice accrues
during the making — he is explicit that writing the document is the act of designing, and the
vector insight arrived through drawing, not before it. Any AI application that produces the
finished representation without the search skips the step that generated the understanding. This
is a general caution about agent-produced deliverables: when the artifact is a by-product of
thinking, delivering the artifact is not delivering the value, and the gap is invisible in the
output.

**On intelligence and systems.** This is a concrete case of the extended-mind claim with a
measurable consequence: the same cognitive agent, handed a different external structure, solves
a different problem. It says something uncomfortable about capability benchmarks — performance
is partly a property of the representation the task arrives in, so a fixed benchmark measures a
model-plus-encoding pair rather than the model. It also suggests a form of assistance we do not
build much: not answering the question, but re-encoding it.

## Related Concepts

- [Cognitive Externalization](cognitive-externalization.md) — the adjacent idea, and worth
  distinguishing: externalization is about *where* cognitive burden lives (weights, context,
  harness); this concept is about what the *shape* of the external structure does to the problem
  once it is out there. Externalizing into the wrong representation buys nothing.
- [Contradiction-Driven Design](contradiction-driven-design.md) — TRIZ's push from technical to
  physical contradiction is a representational move of exactly this kind: the sharpened
  restatement is what dissolves, and the difficulty relocates onto formulation
- [Elegance in Game Design](elegance-game-design.md) — compactness as a quality signal
- [Comprehension Floor](comprehension-floor.md) — the reader-side limit any compression is
  aiming at
- [World Models](world-models.md) — a world model is a representation choice with exactly these
  stakes
- [Illusory Insight](illusory-insight.md) — the counterweight: the dreamcatcher diagram was
  beautiful, felt like understanding, and was wrong

## Open Questions

- How do you distinguish "this won't compress because the design is broken" from "this won't
  compress because I lack the right representation"? Librande's answer is a decade of baseline;
  what works for someone without one?
- Is the search over representations automatable, or is it the irreducibly human part? The Spore
  case needed three candidates and the rejections carried the information.
- Does the one-page constraint have a principled analogue for machine-consumed representations,
  where the reader has no scroll-bar fatigue and no visual system? Or is the budget purely about
  the human in the loop?
- Are there domains where the compression diagnostic actively misleads — genuinely irreducible
  systems whose complexity is real rather than self-inflicted? (Suspect yes, and that biology is
  the obvious candidate.)
- If capability is partly a property of the encoding a task arrives in, what does that do to
  benchmark claims?

## Project Connections

**[Side Quest AI](../projects/game/build-log.md)** — the pipeline's central job is deciding what
enters the `game_state` object an NPC's prompt is assembled from, which is precisely a
what-goes-on-the-page decision. The knowledge-boundary work is this concept in practice: the
`player_action` leak was closed by scoping what the representation carries, and the open
`MAIN_QUEST` half is hard for a representational reason — it sits in the prompt as a global
constant attached to no `event_id`, so no NPC can legitimately know it. That is a badly drawn
diagram, and the reason the fix that closed `player_action` cannot close it.

**[Attractor](../projects/attractor/build-log.md)** — one input, and the same force pulls what
saves you and what kills you. That is a design that fits on one page, and the distribution
fiction reuses the compression rather than explaining it away.
