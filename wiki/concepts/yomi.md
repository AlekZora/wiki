---
type: concept
title: Yomi
aliases: [reading the mind, psychological meta-game, strategic prediction]
tags: [game-design, psychology, game-theory, strategy]
sources:
  - ../sources/Designing Games A Guide to Engineering Experiences (Tynan Sylvester).md
updated: 2026-05-11
---

## Definition

A Japanese term meaning "reading" (the opponent's mind). In game design, yomi describes the psychological meta-game that arises when no single strategy dominates — when the game has no pure Nash Equilibrium. Players must predict, deceive, and outwit each other rather than execute a known-best strategy. The game shifts from mechanics to psychology.

## How I Think About It

Yomi emerges from rock-paper-scissors structures: when every strategy has a counter, the "game" becomes predicting which strategy your opponent will choose. Street Fighter II is the classic example — will they block, throw, or attack? The mechanical skill is the floor; the real game is modeling the other player's mind.

Sylvester's insight: designers create yomi by ensuring no pure Nash Equilibrium exists. If one strategy dominates, there's no reason to read the opponent — just execute. When every option has a counter, the game becomes recursive: "I think they think I'll do X, so they'll do Y, so I should do Z, but they might anticipate that..."

This recursive modeling is what makes competitive games feel like they have infinite depth from finite mechanics. It's also what makes them feel *human* — you're not optimizing against a system, you're reading a person.

## Related Concepts

- [Elegance (Game Design)](elegance-game-design.md) — yomi is a product of elegant competitive design
- [Information Asymmetry (Narrative)](information-asymmetry.md) — yomi is information asymmetry applied to strategy rather than story
- [Flow State](flow-state.md) — yomi at its best produces flow through perfect calibration of challenge to skill

## Open Questions

- Can yomi exist in single-player games against AI opponents? Or does it require genuine unpredictability (another human mind)?
- How does yomi relate to the "theory of mind" concept in cognitive science?
- Could multi-agent AI systems develop yomi-like dynamics when competing or negotiating?

## Project Connection

For Dead Reckoning: characters with hidden agendas in a confined space are playing yomi against each other. Each character is trying to read the others' true intentions while concealing their own. The audience watches multiple simultaneous yomi games unfold — which is what creates the paranoid atmosphere.

## Game Design Vector

**Mechanic:** The AI has no dominant strategy — every behavior pattern it adopts has a counter the player can learn. But the AI also models the player's counter-patterns and adjusts. The game is entirely about predicting what each side predicts the other will do. Mechanical skill is the floor; the real game is recursive mind-reading — "I think it thinks I'll do X, so it will do Y, so I should do Z, but it might anticipate that."

**2D Expression:** In 2D, positional choices are fully legible — both player and AI can see each other's spatial commitments without occlusion. This makes the yomi recursion readable: the player can observe the AI committing to a position and infer what it predicts they'll do. 2D yomi is played in full information; 3D yomi is partially obscured. Full information doesn't make the problem easier — it makes the mind-reading more exposed and more pressured.

**Addictive Loop:** Infinite depth from finite mechanics is the core pull — players return because they haven't finished understanding the AI, and the AI hasn't finished understanding them. Each session deepens the mutual model without exhausting it. The recursion has no bottom: "I think it now knows that I know that it knows..." continues indefinitely.

**Novel Angle:** The open question in the file is the novel angle: can yomi exist against an AI, or does genuine unpredictability require a human mind? No shipped game has answered this affirmatively — an AI that produces the subjective experience of reading a mind rather than decoding a system. The design challenge is making the AI feel genuinely unreadable without scripting random behavior.

## AI Integration Vector

**Player-AI Relationship:** Fighting — but entirely at the psychological level. The player and AI are in a sustained adversarial contest of mind-modeling. To beat the AI, the player must build a deep model of it; the AI models the player equally. The relationship is adversarial and intimate simultaneously: opponents who know each other better than allies do.

**AI as Evolving System:** An AI capable of yomi must genuinely update its model of this specific player — not from a fixed behavior script but from ongoing inference about what this player predicts and how they respond to being read correctly. The AI studies the player across sessions, building a prediction model that is specific to them. Its behavioral repertoire expands based on what it has learned about this player's tendencies.

**AI as Development Environment:** The player observes the AI updating its read in real time — it tries a pattern, observes the player's response, adjusts. This is AI development made visible as game outcome: the player watches the AI getting better at modeling them as a direct consequence of their own play. Every session the AI has learned something. The player can see what it has learned by watching what it tries next.

**Persistence:** Yomi memory is not event logs but inference logs — not "what the player did" but "what this player tends to predict I'll do, and how they respond when I do what they predicted." This is qualitatively different from event recording. Across sessions, the AI carries an accumulated prediction model of this specific player — the most intimate form of AI memory possible.
