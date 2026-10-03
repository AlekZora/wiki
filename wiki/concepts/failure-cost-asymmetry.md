---
type: concept
title: Failure Cost Asymmetry
aliases: [cost of failure, kill-criteria economics, severance asymmetry, exit-cost innovation gap]
tags: [economics, innovation, systems, engineering, agents, decision-making]
sources:
  - ../sources/why-europe-doesnt-have-a-tesla-wip.md
updated: 2026-08-30
---

## Definition

Failure cost asymmetry is the finding that an organization's (or a system's)
willingness to attempt risky, experimental bets is governed primarily by how
expensive it is to *discontinue* a bet that doesn't work out — not by how expensive it
is to *start* one, and not by overall willingness to commit resources. When exit is
cheap, experimentation is abundant even if entry is costly; when exit is expensive,
experimentation is systematically avoided even if entry is cheap and overall resource
commitment is unaffected. The case study is Europe's labor law regime: severance,
works-council approval, and court-reviewable layoffs make discontinuing a job roughly
4–9× more expensive than in the US, and firms respond not by hiring less overall
(employment rates are nearly identical) but by steering hiring away from areas —
frontier, experimental, likely-to-fail — where discontinuation is more probable.

## How I Think About It

The counterintuitive part is that this isn't a story about risk aversion or capital
availability in the usual sense — it's a story about which side of a bet the cost sits
on. A firm facing symmetric costs (cheap to start, cheap to stop) will run many small
experiments and let the losers die quickly. A firm facing this specific asymmetry
(cheap to start, expensive to stop) rationally avoids starting things that might need
to be stopped, which in practice means avoiding anything genuinely experimental,
because experimental work is disproportionately likely to fail and therefore
disproportionately likely to trigger the expensive exit. The employment-rate parity
between the Euro area and the US is the tell: this isn't "Europe hires less," it's
"Europe hires the same amount, redirected away from risk."

This generalizes past labor markets cleanly once you notice that "cost of exit" can be
denominated in almost anything: money, reputation, sunk narrative commitment,
political capital, context/compute already spent. A "kill criteria" framework (defining
in advance what conditions justify abandoning a project) is one deliberate attempt to
make exit cheap *in advance* — to pre-authorize the discontinuation so it doesn't
require a fresh, costly negotiation when the bad outcome actually arrives. That's
structurally identical to what flexicurity does at the labor-market level: it doesn't
remove the cost of a bad outcome, it moves the cost off the entity that would
otherwise avoid taking the bet, and pre-commits to a cheaper resolution path.

## AI Integration

- **This is a general theory of why organizations under-experiment with AI
  deployments, independent of AI capability.** A team where killing a failed model, a
  failed fine-tune, or a failed agent rollout requires re-litigating a public roadmap
  commitment, writing off visible sunk infrastructure, or absorbing reputational cost
  will run fewer, safer AI bets than a team where a bad AI initiative can be killed
  cheaply and quickly — and this holds even if both teams have identical AI talent and
  identical budgets, because the asymmetry sits on the exit side, not the entry side.
- **Agent architecture has a literal version of this same asymmetry.** An agent
  design where abandoning a bad plan or subtask is expensive (large context that must
  be discarded, costly re-planning, a user-visible "I was wrong" event, a lost
  multi-step chain of tool calls) will structurally under-explore relative to a design
  where abandoning a bad path is cheap (checkpointed state, fast rollback, silent
  internal re-planning). This predicts that agent harnesses optimized only for
  headline capability, without attention to how cheap it is for the agent to
  self-correct mid-task, will default to safe, incremental, low-variance actions
  regardless of the underlying model's actual capability — the same prediction the
  labor-market analysis makes for firms.
- **Kill criteria are the deliberate, pre-committed version of cheap exit.** Defining
  in advance what evidence would cause an AI project (or an agent's current plan) to
  be abandoned is functionally equivalent to flexicurity's unemployment insurance: it
  doesn't eliminate the cost of failure, it pre-authorizes and cheapens the
  resolution, removing the need for an expensive, ad hoc negotiation at the moment
  the bad outcome actually shows up.
- **What this reveals about designing any evaluative/selection system:** if you want
  a population of agents, models, or teams to explore aggressively, the leverage
  point is making bad outcomes cheap to discover and cheap to abandon — not making
  good outcomes more rewarding. Reward-side interventions don't fix an exit-cost
  problem; they just raise the bar a bet has to clear before it's worth risking an
  expensive failure.

## Related Concepts

- [Incentive-Aligned Infrastructure](incentive-aligned-infrastructure.md) — a
  companion *Works in Progress* concept about designing constraint structures that
  shape behavior through payoff structure rather than mandate; failure-cost asymmetry
  is one specific instance of a constraint shaping behavior through exit-cost rather
  than entry-cost
- [Engineering Culture](engineering-culture.md) — shares the same source magazine and
  the same underlying question (what structural conditions produce sustained
  innovation), from the complementary angle of belief systems and entrepreneurial
  culture rather than labor-market mechanics
- [Metrics Trap](metrics-trap.md) — a related failure mode: optimizing visible
  entry-side metrics (hiring, R&D spend) while the actual constraint operates
  invisibly on the exit side

## Open Questions

- Is there a measurable "exit cost" for AI projects inside organizations (time,
  political capital, or compute required to formally kill an initiative), and would
  making it explicit and cheap measurably increase the rate of ambitious AI bets, the
  way flexicurity is argued to for firms?
- Does the same asymmetry predict *individual* researcher or agent behavior, not just
  organizational behavior — i.e., does a human or an agent with a costly-to-abandon
  sunk narrative (a public commitment, a long context window already invested) show
  the same risk-averse redirection this essay documents at the firm level?
- The essay's fix (flexicurity) works by moving the cost to a third party (the state)
  rather than eliminating it — is there an equivalent third party for AI
  organizations (e.g., a shared "failure insurance" or portfolio-level risk pooling
  across many small bets) that could play the same role?
- At what point does making exit *too* cheap produce the opposite failure mode —
  abandoning promising bets prematurely because sticking with something through a
  difficult middle phase is no longer required?
