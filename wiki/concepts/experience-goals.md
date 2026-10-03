---
type: concept
title: Experience Goals
aliases: [experience goals, player experience goals, emotional design targets]
tags: [game-design, creative-process, narrative-design, user-experience]
sources:
  - "../sources/A Playful Production Process For Game Designers - Richard Lemarchand.md"
updated: 2026-05-11
---

## Definition

Project-level goals that define the desired emotional and experiential journey for the player/audience, as distinct from design goals (what the system should do) or feature goals (what to build). Experience goals answer "how should the player *feel*?" rather than "what should the player *do*?"

## How I Think About It

Lemarchand's key example: the Cloud project at USC began with the experience goal "to evoke the feeling of relaxation and joy that you get when you look up at the clouds." That's not a feature spec — it's an emotional target. Every design decision filters through it: does this mechanic bring us closer to that feeling or further away?

This is the creative compass for a project. Without it, teams optimize for the wrong things — technical impressiveness, feature count, market trends — and end up with a product that does many things but feels like nothing.

The Uncharted team's "What is Uncharted?" document served this function: it defined the target experience (adventure, discovery, cinematic action) before defining any mechanics. Mechanics were then evaluated against whether they served the experience.

The connection to Sylvester's "engines of experience" framing is direct: if games are machines for producing emotions, experience goals are the spec for which emotions to produce.

The distinction between experience goals and design goals matters: "the player should feel paranoid uncertainty about who to trust" (experience goal) vs. "each character has a hidden agenda revealed on a schedule" (design goal). The first guides; the second implements.

## Related Concepts

- [Elegance (Game Design)](elegance-game-design.md) — elegance is evaluated against experience goals: does this mechanic efficiently serve the target emotion?
- [Flow State](flow-state.md) — flow is often an implicit experience goal; Lemarchand makes it explicit
- [Paranoid Contained Narrative](paranoid-contained-narrative.md) — the experience goal for Dead Reckoning is paranoid uncertainty in a confined space
- [Information Asymmetry (Narrative)](information-asymmetry.md) — a mechanic in service of the experience goal of suspense/curiosity

## Open Questions

- How specific should experience goals be? "Feel paranoid" vs. "feel the specific paranoia of suspecting your closest ally"?
- Can a project sustain multiple competing experience goals, or does that dilute the design compass?
- How do you validate experience goals — can you playtest for emotion reliably?

## Project Connection

Dead Reckoning's experience goals should be defined before any character or plot design. Candidates: "paranoid uncertainty about who to trust," "the slow vertigo of realizing nothing is what it seems," "the thrill of reading someone correctly." These filter every design decision.

## Game Design Vector

**Mechanic:** Every mechanic is evaluated against a single experience goal — not feature completeness, technical elegance, or market fit — but whether it brings the player closer to the target emotional state. Mechanics that don't serve the goal are cut. The experience goal functions as a design filter applied to every decision.

**2D Expression:** The choice of 2D is itself an experience-goal-serving decision — the flat plane, the visible-everything quality, and spatial legibility all produce a specific emotional register. The medium is not neutral. Before any mechanic is designed, the experience goal should determine whether 2D or another medium is the right instrument for producing it.

**Addictive Loop:** The experience goal defines the loop's emotional signature — not what the player does but what they feel at each iteration. A well-specified experience goal makes the loop coherent across sessions: players return because the emotional state the game produces is something they want to re-enter, not because of what they accumulate.

**Novel Angle:** The open question — can a project sustain multiple competing experience goals — is the unexplored design challenge. A game whose experience goal for the player shifts deliberately over time (from curiosity in early sessions to trust to grief in later ones) would require the AI's design to change in correspondence. No shipped game has made the evolution of the experience goal itself an explicit design arc.

## AI Integration Vector

**Player-AI Relationship:** The experience goal defines the relationship category. The file's example — "the player should feel paranoid uncertainty about who to trust" — specifies a relationship of suspicious coexistence. The AI's design, behavior, and persistence strategy all flow from this emotional target. Relationship type is a consequence of experience goal, not a design choice made independently.

**AI as Evolving System:** The AI's development across sessions is evaluated against the experience goal. Development that moves the player toward the target emotion is correct; development that doesn't is design failure regardless of technical sophistication. The AI grows in service of producing a specific feeling, not in pursuit of a performance metric.

**AI as Development Environment:** The player witnesses AI development through the lens of the experience goal — not "what is the AI learning?" but "how does what the AI is becoming make me feel?" The development environment is evaluated emotionally. A technically impressive AI that doesn't serve the experience goal has failed.

**Persistence:** What the AI carries across sessions should maintain the emotional register defined by the experience goal. If the goal is sustained uncertainty, the AI's persistence must ensure certainty never accumulates too quickly — the player should always have more to discover. Persistence is designed to protect the target emotion from erosion over time.
