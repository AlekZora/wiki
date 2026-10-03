---
type: concept
title: Comprehension Floor
aliases: [legibility, prior-knowledge requirement, does it read, blind sample problem, legibility testing]
tags: [design, behavior, psychology, systems, ai, game-design, marketing, communication]
sources:
  - ../sources/play-watch-share-wukong-bilibili.md
  - ../sources/single-multiplayer-diffusion-social-networks.md
  - ../sources/word-of-mouth-discovery-midia.md
updated: 2026-09-19
---

## Definition

The comprehension floor is the minimum prior knowledge a piece of content requires before a
person encountering it can understand what they are looking at. Content above the floor is
intelligible only to people who already have the context; content at or below it can recruit
strangers. The floor is a property of the artifact rather than of the audience, and it is
systematically invisible to the artifact's author, because the author cannot un-know the thing
being tested.

Two consequences follow, and they pull in opposite directions. **On diffusion:** reach is
inversely related to how closely the content resembles the product itself, so the material that
best represents a thing is usually the material least able to spread it. **On measurement:**
establishing your own artifact's floor requires people who do not already know the answer, and
each such person can be used exactly once.

## How I Think About It

The diffusion half comes from the *Black Myth: Wukong* study in
[play-watch-share-wukong-bilibili.md](../sources/play-watch-share-wukong-bilibili.md) — 462
videos and roughly 78,000 Danmaku comments, sorted into nine content types. Strongly
game-related content stayed inside the existing player community; weakly game-related content
(a folk-music cover of the soundtrack, a cosplay performance) travelled furthest and recruited
non-players, "because it requires no prior game literacy to appreciate." Bilibili functions as
a high-context, jargon-gated space; cross-platform spread favours broadly legible symbols. This
is already recorded as the sharpest finding in
[Network Effects vs. Word-of-Mouth Diffusion](network-effects-vs-wom-diffusion.md); what that
note leaves implicit is that the floor is a designable property, not just an observed
correlation.

The measurement half is the harder problem, and the vault contains a clean worked failure.
From the Attractor build log: "they all played, so they all saw the button label, the hint and
the legend. **They were told the mechanic; they cannot answer the legibility question.**" Ten
enthusiastic testers produced zero usable comprehension data. The sample was not small — it was
*spent*. Knowledge of the answer is irreversible and contaminating, which makes naive subjects
a consumable resource rather than a renewable one, and which makes ordering decisions
load-bearing in a way that ordinary user research is not. The same file states the rule
directly: once you have asked someone for help, "they've spent their value as a blind sample."

**The test design worked out for Attractor generalises past games**, and is the most transferable
material here. From [outreach-copy.md](../projects/attractor/outreach-copy.md):

- **Ask what, not whether.** "Tell me what you think the player is controlling, and what
  decision they're making" — never "is this clear?" A yes/no question measures politeness.
- **Suppress leaking words.** An explicit banned list (for Attractor: hold, pull, attract,
  release, danger, magnet, gravity, orbit, drag) covering the title, the body and every reply.
  Naming the mechanic anywhere destroys every answer that follows.
- **Withhold the artifact's own explanation.** The link is kept out of the post, because the
  page's tagline, hint and legend contain the answer. Where the blind can't be enforced it is
  honour-system, and answers arriving after someone admits they went looking are discarded.
- **Show the rule twice.** "One arc reads as an accident and two reads as a rule." A single
  occurrence gives a viewer no basis for inferring a law; two gives them one. This is a claim
  about how people infer rules from short observation, and it is not specific to games.
- **Read the silence.** "If nobody mentions the mechanic, it didn't land regardless of how
  positive the comments are."

That last point is the one I'd keep if I could keep only one. **Enthusiasm and comprehension
are independent measurements, and enthusiasm is far cheaper to collect.** Ten people liking
something is compatible with none of them being able to say what it is. Treating positive
sentiment as evidence of legibility is the default error, and it is what the ten-tester episode
actually consisted of.

**What the floor is not.** It isn't difficulty, and it isn't quality. A hard game can have a
low comprehension floor (a stranger watching *Tetris* for ten seconds knows what the player is
trying to do); an easy one can have a high floor if its central verb has no familiar analogue.
It also isn't fixed by explanation — a tagline, a tutorial or a legend lowers the floor for
people who read them, and simultaneously destroys the ability to measure where the floor was.

## AI Integration

- **Models are the first renewable supply of naive viewers, and that changes the economics of
  the test rather than its validity.** The binding constraint on comprehension testing has
  always been that unspoiled subjects are scarce and single-use, which is why iteration is so
  expensive: every revision needs a fresh sample. A model shown a silent clip and asked what it
  thinks the rules are can be re-run indefinitely against successive versions. But it is not a
  human first-time viewer — its priors come from training data rather than from being a person
  who has never encountered the thing, and it has likely seen thousands of games. **Whether
  model-reported comprehension correlates with stranger-reported comprehension is unknown and
  untested.** Nothing in this vault bears on it either way. The honest position is that this
  is a cheap proxy of unverified validity, useful for catching gross failures and not yet
  trustworthy for close calls.
- **The floor is the input side of the resonance bottleneck.**
  [Network Effects vs. Word-of-Mouth Diffusion](network-effects-vs-wom-diffusion.md) argues
  that the WOM snowball runs acceptance → resonance → communication, and that "the
  resonance-phase bottleneck is an eval problem in disguise." An artifact whose central idea
  doesn't read never reaches the resonance phase at all — the chain breaks one step earlier
  than that note's framing accounts for, at acceptance, because the viewer never formed a
  coherent expectation to confirm or disconfirm.
- **Agent tool surfaces have a comprehension floor and it is directly measurable.**
  [Elegance (Game Design)](elegance-game-design.md) already proposes its four learnability axes
  — simplicity, coherency, progression, communication — as a spec for tool interfaces exposed
  to an LLM. The comprehension-floor version is an actual procedure: give a tool schema to a
  model with no surrounding context and ask what it believes the tool does and when it should
  be called. The gap between that answer and the intended one is the floor, and it is cheap to
  run on every schema change.
- **Cheap generation may saturate the low-floor channel.** If the content that travels furthest
  is the content requiring least prior knowledge, and that content is now cheap to
  mass-produce, the channel's differentiating power falls.
  [AI-Mediated Virality](archive/ai-mediated-virality.md) already carries this as an open
  question; the comprehension-floor framing says why it bites — low-floor content was
  previously costly to make well (a good cosplay, a real music cover), and that cost was doing
  filtering work nobody was accounting for.
- **What this reveals about minds:** the author's inability to perceive their own artifact's
  floor is the curse of knowledge in its operational form. It is not a failure of effort or
  care, and no amount of re-reading fixes it. It can only be measured from outside, which makes
  it structurally similar to any other property a system cannot evaluate about itself.

## Related Concepts

- [Network Effects vs. Word-of-Mouth Diffusion](network-effects-vs-wom-diffusion.md) — where
  the diffusion finding lives; this concept extracts the floor as a designable property and
  adds the measurement problem
- [Recommendation as Identity](recommendation-as-identity.md) — its open question about "the
  smallest identity-distinctive surface that makes a game claimable" is the same question
  aimed at sharing rather than at understanding
- [Constraint as Camouflage](constraint-as-camouflage.md) — constraints chosen to hide a
  capability's weakness usually lower the floor as a side effect, by reducing what the viewer
  has to hold in mind
- [Interface Lag](interface-lag.md) — a product closing an interface lag has an unusually low
  floor almost by definition, since the behaviour it enables was already familiar
- [AI-Mediated Virality](archive/ai-mediated-virality.md) — the retrieval-mediated case, where
  the entity that must comprehend the artifact is a model rather than a person
- [The Metrics Trap](metrics-trap.md) — "read the silence" is a warning against the available
  metric (sentiment) standing in for the one that matters (comprehension)

## Open Questions

- Does a model's report of what a silent clip shows predict what human strangers report? This
  is testable, cheap, and currently unevidenced in either direction. It is the question that
  determines whether the synthetic-naive-viewer approach is worth anything.
- Can an account that never breaks character run a comprehension test at all? The direct ask
  is the only test design the vault has, and it is incompatible with the in-character rule.
- Is the floor one threshold or a gradient that differs by audience segment? The MIDiA
  discovery data in [Network Effects vs. WOM](network-effects-vs-wom-diffusion.md) shows
  segment-dependent discovery mixes, which suggests a gradient, but nothing tests it directly.
- What is the passing bar? "Read the silence" gives a direction, not a threshold — no base rate
  of unprompted correct identification has ever been proposed.
- Is there a cost to lowering the floor? A version so immediately legible that nothing remains
  to discover would conflict with everything in
  [ARG Mystery Mechanics](arg-mystery-mechanics.md), which is built on withholding. The two
  concepts appear to point in opposite directions and the reconciliation is not obvious.
- Does the floor apply to the *mechanic* or to the *stakes*? A viewer might correctly identify
  what the player controls and still not grasp why it matters, and those may need separate
  tests.

## Project Connections

**Attractor.** This is a live, unresolved item, recorded as open in
[The Attractor Zone](../projects/attractor/attractor-zone.md) and in the 2026-09-14
[decision log](../decisions/decision-log.md) entry. The tension is specific: the video episodes
*are* silent gameplay clips, so the floor matters more than it did before the pivot, but the
in-character rule forbids the direct ask that the entire test design in
[outreach-copy.md](../projects/attractor/outreach-copy.md) assumes. The test method needs
replacing, not the question.

Worth noting separately: **The Attractor Zone is itself an application of the Wukong finding**,
whether or not it was derived from it. A fictional anthology world adjacent to the game is
low-floor content — the micro-fables and Rules of the Zone require no knowledge of Attractor to
follow — which is precisely the category the study found recruits people that gameplay footage
cannot reach. The strategy and the research agree; they were arrived at independently.
