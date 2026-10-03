---
type: answer
question: Why can a competent system execute extremely well once given an objective, yet struggle to originate objectives and commit to them?
related_concept:
  - ../concepts/self-initiation-gap.md
  - ../concepts/imaginative-empathy.md
answered: 2026-09-07
tags: [psychology, behavior, agents, ai, identity, decision-making, systems]
---

## Short Answer

Because execution and origination are not the same operation applied to
different-sized problems — they are different operations, and only one of them
has a stopping rule. Execution is optimization *within* a space against a
supplied error signal that terminates when the task does. Origination is
selection *of* the space, has no error signal internal to the system, and no
natural halting condition. Five structural asymmetries follow from that, and
one non-obvious consequence: what closes the gap is not better evidence but
**option-collapse** — removing alternatives rather than improving the
comparison between them.

---

## The Five Asymmetries

### 1. Execution has an error signal; origination has to invent one

Given an objective, every candidate action can be scored against it — there is
a gradient to descend. Origination has no objective yet; the objective *is* the
output. The system is not solving a problem, it is choosing which loss function
to minimize, and there is no meta-loss function inside the system that says
which choice is correct. Competence at descending a gradient tells you nothing
about how to pick one.

### 2. Execution terminates by itself; deliberation does not

A task completes or fails — either way it ends. Comparing imagined options has
no built-in termination condition. This is the mechanism
[Self-Initiation Gap](../concepts/self-initiation-gap.md) already names: an
imagined option can always be out-argued by a better imagined alternative,
because nothing is real yet, so nothing is falsifiable, so nothing forces a
stop. Search without a halting condition does not halt — it just looks like
thinking.

### 3. Capability actively widens the gap

This is the counterintuitive part, and it is why "competent system" is doing
real work in the question. More simulation capacity means a *better generator
of plausible competitors* to any candidate commitment. A weak system commits
early because it can only see one option; a strong one sees six, each vividly
renderable, each defeating the others.

Rowling's Harvard address
([source](../sources/rowling-harvard-commencement.md)) is a case study: she was
excellent at passing exams, and "that for years had been the measure of success
in my life" — which is precisely high competence at objectives supplied by
someone else, developed to a high level while the origination faculty stayed
untrained.

### 4. Committing to an objective is an identity claim; executing one is not

Executing a supplied task badly is a bounded, local failure — the objective can
always be disowned ("I was doing the job"). Originating one is a statement
about what the system judges worth doing, so failing at it falsifies *the
originator*, not just the plan.

That makes perceived exit cost enormous, and per
[Failure Cost Asymmetry](../concepts/failure-cost-asymmetry.md), willingness to
*start* is governed by cost of *exit*, not cost of entry. A system that cannot
cheaply abandon a chosen objective rationally avoids choosing one. This is
exactly why the concept's prescribed fix is making commitments **temporary**:
it converts an apparently irreversible identity claim into a bounded
experiment, which is the same move flexicurity makes at the labour-market
level — not removing the cost of a bad outcome, but pre-authorising a cheap
resolution path.

### 5. Supplied objectives smuggle in the entire hard part

When a task arrives from outside, someone else has already (a) noticed the
need, (b) judged it worth doing, (c) ruled out the alternatives, and (d)
absorbed responsibility for that judgment. The executor inherits all four for
free.

The consequence is that execution competence can scale indefinitely without the
origination machinery ever being exercised. It is not that such a system fails
at origination — it never trained on it. This is the situation of current agent
frameworks by construction: their training and evaluation distributions are
objective-supplied almost without exception.

---

## What Actually Closes the Gap — and It Isn't More Evidence

The sharpest version of the fix comes from the Rowling speech, and it is not
the one you would expect. Failure did not help her *choose* better. It
**destroyed the alternatives**:

> failure meant a stripping away of the inessential. I stopped pretending to
> myself that I was anything other than what I was and began to direct all my
> energy into finishing the only work that mattered to me.

"Rock bottom became the solid foundation" works as a mechanism, not just a
metaphor: when one option remains, the possibility → commitment transition
becomes trivial. The forcing function is not information. It is option-collapse.

This reframes every fix listed in
[Self-Initiation Gap](../concepts/self-initiation-gap.md) as the same move
performed deliberately rather than catastrophically:

| Fix | What it actually does |
|---|---|
| Deadline | Collapses options by expiry |
| Commitment window | Suppresses re-entry of alternatives for a fixed period |
| Kill criteria | Pre-authorises exactly one exit condition, closing the rest |
| Ship a tiny artifact | Converts one option from hypothetical into evidence, breaking symmetry |

Adding evidence to a set of mutually-defeating hypotheticals does not converge,
because each new consideration is available to every option equally. Shrinking
the set does.

---

## The Asymmetry Worth Noting: Why Imagination Sometimes Mobilizes Instead

Set this against [Imaginative Empathy](../concepts/imaginative-empathy.md),
derived from the same speech, and a puzzle appears: the *same* imaginative
simulation capacity paralyzes when aimed at one's own futures and mobilizes
when aimed at other minds. Amnesty International's entire model is people
acting decisively on suffering they have only ever imagined.

The difference is the **truth status of the simulation's target**:

- **Empathy simulates something actual.** A real experience that already
  happened. It arrives as evidence and cannot be argued with by constructing a
  competing scenario — the competing scenario would simply be false.
- **Deliberation simulates things that are all equally unreal.** Symmetric,
  mutually defeating, none falsifiable, so none eliminable.

So imagination produces action when its target is true and paralysis when its
target is merely possible. The faculty is identical; the convergence properties
are opposite, and they are determined by whether the thing being imagined has a
truth value yet.

**Testable prediction for agent design:** grounding an agent's deliberation in
artifacts that already exist should produce commitment, while grounding it in
projected outcomes should produce thrashing — and this should hold *regardless
of how good the projections get*, since the problem is the symmetry of
unrealised options, not the quality of the forecasting.

---

## Conclusion

The gap is architectural, not characterological, and not a capability deficit.
A system can be arbitrarily strong at execution and remain structurally unable
to originate, because origination requires three things execution never
supplies: an error signal that must be chosen rather than received, a
termination condition that must be imported rather than inherited, and an
acceptance of identity-level exit cost that increases with the system's own
sophistication.

The lever is not more reasoning. It is manufactured option-collapse — and the
choice is only whether it is designed in advance (deadlines, commitment
windows, kill criteria, published artifacts) or arrives on its own terms, which
is the expensive version Rowling describes.
