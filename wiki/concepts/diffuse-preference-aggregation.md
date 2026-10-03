---
type: concept
title: Diffuse Preference Aggregation
aliases: [nitby-effect, low-stakes-veto, distant-stakeholder-preference]
tags: [systems, psychology, economics, preferences, ai, design]
sources: [beauty-in-my-backyard-hughes, urban-expansion-age-of-liberalism]
updated: 2026-08-02
---

## Definition

A large population holding faint, low-intensity preferences about outcomes that do not
affect them can aggregate into a decisive constraint on the much smaller population that
actually lives with those outcomes. Each individual signal is weak, cheap to produce, and
formed on cursory inspection; the sum is strong enough to veto. Samuel Hughes coins
**NITBY** — "not in *that* backyard" — for the distant, casually-interested objector, as
against the NIMBY who has a direct material stake. The distinguishing features are that
the preference is genuinely held rather than pretextual, that its holder is basically
well-meaning, that it costs almost nothing to express, and that it is formed from a
surface impression rather than from lived exposure to the thing being judged.

The pattern is not the same as a well-organized minority capturing policy, and not the
same as mass preference in the ordinary democratic sense. What makes it distinctive is
the mismatch between the *intensity* of the preference and the *weight* it carries — and
the fact that the people whose preferences are most intense (those who will live there)
are outnumbered by people for whom the question is nearly costless.

## How I Think About It

The important asymmetry is not power, it is *evaluation cost*. The distant objector judges
from a photograph, a headline, a rendering — whatever can be assessed in a few seconds.
The resident judges from consequences they will absorb for decades. Both preferences are
sincere. But because the distant judgment is cheap, there are vastly more of them, and the
aggregate therefore optimizes for **what looks good on cursory inspection** rather than
what is good to live inside. Any system that sums cheap evaluations will drift toward
surface legibility, and will do so without anyone intending it or behaving badly.

Hughes's evidence for the mechanism is mostly structural rather than attitudinal, which is
what makes it convincing: the movement's *priorities* give it away. Conservationism
protects rural churches, working-class terraces and commercial downtowns — places where
almost no NIMBYs live. A movement whose protections cluster where its supposed
beneficiaries are absent is not being driven by those beneficiaries.

The second thing worth holding onto is the sublimation move. Hughes suspects
conservationists were actually reacting to ugliness but expressed it as reverence for age,
because the aesthetic argument was socially unavailable against high-status modernism.
Stated reasons drift toward whatever is defensible in public; the operative reason stays
unstated. This means the textual record of a preference is systematically not the
preference — and it is most distorted exactly where the real motive is contested or
low-status.

## AI Integration

- **This is the shape of RLHF, and it is the half `ideal-reader` does not cover.** A rater
  pool supplies large numbers of cheap, low-stakes judgments about outputs whose real
  consequences they will never encounter, and the aggregate becomes a binding policy for
  users whose situations the raters never saw. `ideal-reader` covers the flattening effect
  of aggregation — averaging many tastes produces no taste. The NITBY structure adds
  something sharper: diffuse preference does not merely dilute, it can *veto*, and the
  resulting policy is biased toward what reads well on quick inspection. A response that
  looks careful and balanced in isolation beats a response that is actually correct for a
  situation the rater cannot see. That is the same failure as judging a building from a
  rendering.
- **Any cheap-evaluation loop drifts toward surface legibility.** The mechanism does not
  require human raters at all. LLM-as-judge pipelines, automated preference models, and
  thumbs-up telemetry all sum large volumes of low-cost evaluations, and all should be
  expected to select for inspectability over quality by default. The design question this
  raises is whether evaluation weight can be made proportional to evaluation cost — a rater
  who used the output for a week counting more than one who skimmed it.
- **Stated reasons are the wrong training signal for motive.** Because the socially
  acceptable justification systematically displaces the operative one in text, a model
  learning human motivation from written argument learns the sublimated version by
  construction, and learns it most confidently where the substitution is most complete.
  This is a structural reason to be skeptical of LLM-inferred "why" over LLM-inferred
  "what."
- **What it reveals about systems generally.** Preference aggregation is not neutral with
  respect to what it aggregates. Summing across a population implicitly weights by how
  cheap it is to hold an opinion, which means the aggregate is shaped most by those with
  the least at stake. Any mechanism that counts opinions rather than exposures inherits
  this, whether it is a planning system, a recommender, a moderation queue, or a reward
  model.

## Related Concepts

- [Ideal Reader](ideal-reader.md) — the complementary half: aggregation flattens
  distinctiveness, where this concept covers aggregation acquiring veto power
- [Recommendation as Identity](recommendation-as-identity.md) — the gap between aggregate
  optimization and individual situation, in the recommender domain
- [Metrics Trap](metrics-trap.md) — what happens when the cheap-to-evaluate proxy becomes
  the target
- [Information Asymmetry](information-asymmetry.md) — the resident and the distant
  objector are judging from radically different information sets
- [Incentive-Aligned Infrastructure](incentive-aligned-infrastructure.md) — the system that
  preceded the veto, and what the veto replaced

## Open Questions

- Can evaluation weight be tied to evaluation cost or exposure duration without making
  feedback collection prohibitively expensive? Every obvious implementation (weight by time
  spent, by depth of engagement, by whether the rater actually used the output) is far more
  costly to gather than the thumbs-up it would replace.
- Is there a diagnostic for detecting that a system has drifted toward surface legibility,
  short of a controlled comparison against people with real exposure? Hughes found it by
  looking at *where* protections clustered rather than at what anyone said — the analogous
  move for a model might be to look at which categories of output its reward model protects
  most, and ask whether the users of those categories are the ones supplying the signal.
- Does the sublimation effect have a measurable textual signature — can a stated reason
  that has displaced an unstated one be detected from the text alone?
- **Is the diffuse preference sometimes correct?** `urban-expansion-age-of-liberalism`
  complicates the picture: under the permissive nineteenth-century regime, middle-class
  buyers paid real premiums for privately covenanted neighborhoods promising to freeze
  character, which implies the system was supplying *less* stability than people valued.
  Adding restrictions sometimes raised value rather than lowering it. So the distant
  objector may occasionally be registering a genuine underprovision rather than merely
  imposing a cheap judgment — and the two are hard to tell apart from the objection
  itself. Sharpens the RLHF parallel considerably: a rater with no stake is not
  automatically wrong, they are merely unaccountable, and distinguishing "cheap and
  correct" from "cheap and wrong" is the whole problem.

## Project Connections

The soft-constraint scoring in `wiki/projects/game/fact-database-design.md` §3 is
mechanically an instance of this: many weak multipliers (NPC cooldown, template variety,
trust gradient, callback freshness) are summed into a single selection decision, and no
individual multiplier is decisive. That is fine as a pacing mechanism, but it is worth
being explicit that such a system will systematically prefer whatever the cheap signals can
see. The equivalent drift to watch for is quests that score well on measurable variety
while being flat in the way that only reading them reveals.
