---
type: concept
title: Fair Uncertainty
aliases: [legible uncertainty, fog of war done fairly, known / inferred / unknown, tension without judgment, forecast not ambush]
tags: [design, game-design, systems, psychology, behavior, ai, agents, llm, maps]
sources:
  - ../sources/goal-map-visual-references-perplexity.md
updated: 2026-10-03
---

## Definition

Uncertainty that creates anticipation and tension without feeling like a punishment, a trick,
or a judgment of the person living with it. A system has fair uncertainty when:

1. **Structure is visible, contents are not.** The person can see where things are (the
   destination, the main forks) while what happens there stays uncertain. The source calls
   this separating *route topology* from *event certainty*.
2. **Three knowledge states are kept apart and shown differently:** *known* (observed),
   *inferred* (guessed, and drawn as a guess), and *unknown* (left open, with nothing invented
   to fill it).
3. **Unknown is not the same as dangerous.** Unseen territory invites curiosity. It doesn't
   imply threat.
4. **Hazards are foreshadowed before commitment,** and nothing arbitrary is added after a choice
   is made.
5. **Changes come with reasons:** when conditions change, the system shows what changed and why
   the old plan no longer fits.
6. **Difficulty is placed in the world, not in the person.** "The pass is closed until the
   hosting issue clears", not "you fell behind".

The framing comes from an AI research report on map design for Goal Map, which draws it from
portolan charts (coastlines known, interiors open), *Darkest Dungeon* (rooms visible, contents
revealed by travel or scouting), *Slay the Spire* (the boss always visible, branches chosen
under partial information) and *Death Stranding* (routes judged by terrain and weather, not
one difficulty score).

## How I Think About It

The useful contrast is **a forecast vs. an ambush.** Both are uncertain. A forecast is
uncertainty the person was shown before deciding, so whatever happens next feels like
something they chose to face. An ambush is uncertainty that turns out to have been there all
along, hidden, and it feels like the system was against them. The amount of uncertainty is the
same; what differs is when it became visible and who seems to have authored it.

That's why the six conditions mostly fall into two groups. Conditions 1–4 are about **timing**:
what can be seen before a commitment. Conditions 5–6 are about **attribution**: whether a change
reads as the world's doing (weather, terrain, a dependency) or the system's verdict on the
person. Tension that comes from the world can be exciting. Tension that seems to come from a
judge is just pressure.

The portolan example is the most intuitive one. An incomplete chart reads as *discovered*, not
*deficient*, because what it shows is reliable and what it doesn't show is plainly blank. A
chart that showed confident coastlines that turned out to be wrong would feel worse than one
with honest gaps. The report's rule for the unknown, "no fabricated threats", is the same
point: don't fill an honest gap with invented content.

It's close to the rule the Attractor project set for its adaptive director: the director may
shape the *setup* before an event exists but never touch the *outcome*, tested by asking whether
the player reading the design doc would feel "cheated or interested"
([drama-management](drama-management.md); `wiki/decisions/decision-log.md`, 2026-09-09). Fair
uncertainty is that test applied to what's hidden, not just to what's adjusted.

Fair isn't the same as gentle. A route can be closed, a leg can be long and exposed, the
destination can be far. All of that is fair as long as it was legible and true.

## AI Integration

- **LLMs collapse the three states.** A language model writes an inference in the same voice
  as an observation, and fills unknowns with plausible content. In this concept's terms that's
  inferred drawn as known and unknown filled with fabricated threats (or fabricated
  treasure). [Hallucinated agency](hallucinated-agency.md) is the same failure in an agent: it
  acts on invented world content. A fair-uncertainty interface for AI output would mark which
  claims are observed, which are guesses, and which questions are open, and keep those
  markings visually stable.
- **AI-generated plans are inferred territory.** Milestones or steps proposed by a model are an
  inside-view guess at a route ([planning-fallacy](planning-fallacy.md)). Showing them as
  firm, fully-drawn ground claims a certainty nobody has. Drawing them as "inferred", firming up
  as the person gets closer or as real evidence comes in, is an honest way to show model
  uncertainty without numbers.
- **Replanning agents need condition 5.** An agent that silently swaps its plan feels like
  sabotage even when the new plan is better; the source lists an "optimal route" algorithm
  silently overriding the user as a pitfall. When an agent changes course it should show what
  it learned and why the old route no longer fits, and leave the old route visible.
- **Attribution must stay true.** "Put the difficulty in the world" can be misused: an AI
  narrator that blames the weather for a choice the user made is lying, even kindly. The world
  framing is only fair when the world is actually where the cause is. A choice should be shown
  as a choice, without blame.
- **AI directors and generated content.** Game directors and procedural generators can add
  tension fairly by setting up hazards *before* the player commits and foreshadowing them, and
  unfairly by inserting them afterwards. Generated obstacles keyed to a player's committed
  choice are exactly what reads as an ambush.
- **Visual consistency is part of fairness.** States can only be read if their marks are
  stable. The source's list of "AI-generated look" failures (symbols that change between
  states, inconsistent hatching, physically incoherent terrain) are all consistency failures.
  Its fix, a fixed library of authored marks, suggests that whatever encodes uncertainty in a
  UI should be drawn by code, with generation kept out of the state layer.
- **What it says about people and systems:** people tolerate, and even seek out, uncertainty
  that's visible and attributed to the world, and they reject the same uncertainty when it seems
  to have been hidden or authored against them. For trust in AI systems, the
  question isn't only "how uncertain is the agent?" but "did it show me that before I relied on
  it?"

## Related Concepts

- [Drama Management](drama-management.md): the director that may set up but not resolve
- [Hallucinated Agency](hallucinated-agency.md): the failure of filling unknowns with invented content
- [Coziness](coziness.md): "vast unknowable spaces" break coziness; pressure kept outside the window
- [Worst-Day Design](worst-day-design.md): obstacles met with legitimate alternatives, not blame
- [Planning Fallacy](planning-fallacy.md): why AI-proposed plans belong in the inferred state
- [Representation Shapes the Solution](representation-shapes-the-solution.md): how a plan is drawn changes what it seems to claim
- [Compulsion vs. Craft](compulsion-vs-craft.md): tension that serves the person vs. tension that hooks them

## Open Questions

- **Can a real-world tool foreshadow anything?** A game knows its hazards; a goal app doesn't
  know what life will do. Maybe a tool can only be fair about its *own* rules (for example,
  publishing the drift rule as a law of the world) and about what the user logged, never about
  the future.
- **Does drawing plans as "inferred" weaken commitment?** If-then plans work partly because
  they're specific ([implementation-intentions](implementation-intentions.md)). A milestone
  shown as tentative might be easier to drop. Where's the line between honest and wobbly?
- **Is fairness measurable?** The source is a design report, not a study. Does fair uncertainty
  change persistence or trust, or does it just feel better? A test would compare return rates
  after an obstacle that was foreshadowed vs. one that wasn't.
- **Where does "world, not person" stop being true?** Some setbacks really are the person's
  choice. What's the honest, non-judging way to show those?

## Project Connections

- **Goal Map** ([overview](../projects/goal-map/overview.md)): the proposed journey layer in
  `~/projects/goal-map/docs/DESIGN.md` already has conditions 1 and 5 (summit visible from day
  one, closed paths kept on the map with the new way drawn around). Missing so far: an
  *inferred* state between revealed land and blank paper, and route-quality labels on the
  redrawn way. The drift warning is where condition 6 matters most. Tension B in
  [the synthesis](../answers/goal-map-wiki-synthesis.md) ("fog over texture, never over
  destination or route") is condition 1.
