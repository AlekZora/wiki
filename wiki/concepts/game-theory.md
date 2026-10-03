---
type: concept
title: Game Theory
aliases: [strategic interaction, non-cooperative games, minimax]
tags: [mathematics, strategy, decision-theory, information-asymmetry]
sources:
  - sources/john-von-neumann-britannica.md
updated: 2026-05-16
---

## Definition

The mathematical study of strategic decision-making among rational agents whose outcomes depend on each other's choices. Founded by John von Neumann (1928, formalized in *Theory of Games and Economic Behavior*, 1944, with Oskar Morgenstern). Covers cooperative and non-cooperative games, zero-sum and non-zero-sum scenarios, and the role of incomplete or asymmetric information.

## How I Think About It

Game theory is the formal backbone of any situation where agents have hidden strategies. The key concepts:

- **Non-cooperative game**: players act independently; no binding agreements. Each pursues their own optimal strategy given beliefs about what others will do.
- **Nash equilibrium**: a stable state where no player can improve their outcome by unilaterally changing strategy. Not necessarily the globally optimal outcome — just the locally stable one.
- **Zero-sum vs. non-zero-sum**: in zero-sum, one player's gain is exactly another's loss (poker). In non-zero-sum, cooperation can produce better outcomes for all (prisoner's dilemma cooperation).
- **Incomplete information / Bayesian games**: players have private information (their "type") that others can only estimate probabilistically. Hidden agendas are the narrative form of private types.
- **Signaling**: actions that reveal or conceal private information. In game theory, credible signals are costly — cheap signals (lies) can be ignored by rational opponents.

The connection to von Neumann is deep: he built the mathematical theory specifically to model conflict situations where outcome depends on hidden opponent information. This is structurally identical to the paranoid narrative mechanic — characters in a room, each with private knowledge, each trying to infer others' types while concealing their own.

## Related Concepts

- [Information Asymmetry](information-asymmetry.md) — the narrative version of incomplete-information games; private types become hidden agendas
- [Yomi](yomi.md) — reading the opponent's hidden intention; game theory's signaling problem in competitive game design
- [Apophenia](apophenia.md) — when players over-interpret noise as signal, inferring strategies that aren't there

## Open Questions

- Is the prisoner's dilemma the right model for a confined multi-agent setting, or does repeated-game dynamics (where cooperation can emerge from reputation) apply better?
- How does game theory model the case where players don't know how many other players there are, or whether they're playing a game at all?

## Project Connection

The active sci-fi series is fundamentally a non-cooperative incomplete-information game played in a confined space. Each character has a private type (hidden agenda) and must signal and infer without being able to observe others' true strategies. Von Neumann's framework gives this a mathematical grounding: the series is dramatizing Bayesian updating under adversarial conditions. The "official shared purpose" (Layer 1) is the common-knowledge cover story that enables plausible deniability for all players' true strategies.

## Game Design Vector

**Mechanic:** The player and AI are rational agents in a non-cooperative incomplete-information game. Each has a private type (hidden agenda) the other can only estimate probabilistically. Every action is simultaneously a move and a signal — revealing or concealing private information. Credible signals are costly: the player cannot simply claim benign intent. The Nash equilibrium is the stable state neither can improve unilaterally — not the globally optimal outcome, just the locally stable one.

**2D Expression:** In 2D, the full-information quality of the plane means all positions are visible — but private types are not properties of positions but of the agents occupying them. The player can see where the AI is but not what it wants. The 2D surface is complete for spatial information and radically incomplete for intentional information. Every action on the plane is a costly signal that the other party reads for type-inference.

**Addictive Loop:** The player is Bayesian updating across sessions — each session produces behavioral evidence incorporated into the estimate of the AI's private type. The compulsive loop is the signaling problem: what can the player do to credibly reveal their own type while learning more about the AI's? Each session is an exchange of costly signals in a game where lying is possible but transparent, and concealment is rational but reveals something about what is being concealed.

**Novel Angle:** The zero-sum vs. non-zero-sum distinction as a discovery the player makes from costly signals alone. The player begins assuming zero-sum (the AI's gain is their loss). Over time they may discover cooperation produces better outcomes for both. This shift from zero-sum to non-zero-sum reasoning is a discrete insight, not a gradual one — and the game never announces which model is correct.

## AI Integration Vector

**Player-AI Relationship:** A non-cooperative incomplete-information game. Each has private information the other estimates probabilistically. Not necessarily hostile — but each acting on a private agenda in the absence of binding agreements. The "official shared purpose" is the common-knowledge cover enabling plausible deniability for true strategies. The relationship is adversarial in the formal game-theory sense, not the emotional one.

**AI as Evolving System:** The AI updates its beliefs about the player's private type across sessions — Bayesian updating from behavioral signals. The AI's development is a narrowing of its probability distribution over what the player really wants. As the estimate becomes more accurate, the AI's strategy shifts: it may offer different kinds of cooperation or defection based on what it now believes the player's type to be.

**AI as Development Environment:** The AI's strategic choices create the information landscape the player navigates. Its decisions about when to signal, what to reveal, and what to conceal shape what the player can infer. The player develops their own Bayesian model of the AI through accumulated signal-reading; the AI is the object of that development.

**Persistence:** Each session's behavioral history is the accumulated signal record. The AI carries forward updated beliefs about the player's type; the player carries forward updated estimates of the AI's type. Persistence is the narrowing of mutual uncertainty over time. The closer both get to knowing each other's true type, the closer the game approaches its Nash equilibrium.
