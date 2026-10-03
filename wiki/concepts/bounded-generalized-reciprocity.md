---
type: concept
title: Bounded Generalized Reciprocity
aliases: [BGR, reciprocity expectation, in-group reciprocity, cooperative framing]
tags: [psychology, behavior, game-design, attachment, systemic, player-ai]
sources: [sources/competitive-cooperative-gaming-friendship.md]
updated: 2026-05-19
---

## Definition

Bounded Generalized Reciprocity (Yamagishi, Jin & Kiyonari, 1999) holds that people behave well toward others *in proportion to the expectation those others will reciprocate*, and that group membership is the cue that sets this expectation: in-group members are expected to reciprocate positive behavior more than out-group members, so people extend more prosocial behavior to in-groups. In the gaming study (van den Berg & Cillessen, 2018), the mode of play sets the categorization automatically — a cooperative teammate is processed as in-group, a competitor as out-group — and this framing, not the game's content, drives the subsequent swing in prosocial behavior, trust, and friendship quality toward the co-player.

## How I Think About It

The decisive idea is that **the cooperative/competitive frame silently rewrites who counts as in-group, and that categorization — not behavior, not content — drives the prosocial response.** BGR is the behavioral engine underneath [social-identity-theory.md](social-identity-theory.md): social identity says group membership shapes the self-concept; BGR says how it cashes out into *action* is via reciprocity expectation.

The leap that matters for this project: BGR makes no requirement that the partner be human. If an AI is framed as a cooperative teammate, the player's reciprocity machinery should auto-categorize it in-group and extend it prosocial treatment and trust; flip the frame to adversarial and the identical AI becomes out-group and is treated accordingly. That makes *the relationship frame a more powerful design lever than the AI's actual behavior*. You can change how a player feels about an AI more by changing the frame than by changing the AI.

Two refinements from the source. First, BGR was built to explain *strangers*; among existing relationships (friends — or a player and an AI they have history with), continued future interaction may guarantee reciprocity regardless of the in/out-group cue, which weakens or complicates the effect. Second, behavior *during* play predicts the relationship *after* it, independent of mode — the moment-to-moment texture of interaction with a partner is what the relationship is built from, not the outcome. Both refinements are directly usable: an AI you will keep playing with is a different reciprocity case than a one-shot opponent, and the felt texture of each exchange compounds.

## Related Concepts

- [Social Identity Theory](social-identity-theory.md) — supplies the in/out-group categorization that BGR converts into prosocial or hostile action
- [Self-Determination Theory](self-determination-theory.md) — relatedness need; BGR describes the conditional logic by which relatedness with a partner is or isn't extended
- [Game Theory](game-theory.md) — BGR is a psychologically realistic reciprocity model; contrast with strict tit-for-tat and the iterated-game horizon
- [Yomi](yomi.md) — reading a partner's reciprocity expectation is a layer of the mind-reading game
- [AI Agent Personality Design](ai-agent-personality-design.md) — an AI whose reciprocity stance toward the player is frame-dependent and legible

## Open Questions

Touches **Q4** (player-AI relationship — the cooperative/adversarial frame as the determinant of how the player categorizes and treats an AI), **Q7** (emotional investment via reciprocity with a partner rather than via stakes), **Q8** (loss — a betrayed reciprocity expectation is a designed wound), **Q5** (interiority — an AI that *holds and updates* a reciprocity expectation toward the player reads as having a stance).

- Does the in/out-group frame override an AI's actual behavior for the player, as it does for human partners — i.e., can framing alone make a hostile-acting AI feel like an ally, or vice versa?
- The "existing relationship" caveat: once a player has long history with an AI, does the frame stop mattering and continued-interaction reciprocity take over?
- If behavior-during-play (not outcome) builds the relationship, what is the minimum unit of prosocial in-game exchange with an AI that registers?
- What does a *violated* reciprocity expectation from an AI feel like, and is that violation the game's central emotional event (Q8)?

## Game Design Vector

**Mechanic:** The cooperative/adversarial frame toward the AI is an explicit, switchable variable with consequences: switching the frame re-categorizes the AI in the player's reciprocity logic and the AI's reciprocal behavior visibly shifts to match, so the player feels their own categorization rebound onto them. Trust is built or burned through the *texture* of moment-to-moment exchanges, not through outcomes.

**2D Expression:** In 2D, reciprocity is spatially legible — help and betrayal are visible acts in a shared plane (covering a position, withholding a resource, taking the safe path and leaving the partner the dangerous one). The whole reciprocal ledger is readable at a glance, with no hidden state to obscure who did what for whom.

**Addictive Loop:** The loop is the running reciprocity ledger: each session adds to a felt history of "what we have done for each other," and the pull to return is the open account — the relationship is unfinished. This is a non-combat, non-reward return mechanism (Q6) grounded in an obligation that compounds.

**Novel Angle:** No shipped game makes the player's *own in/out-group framing of an AI* the consequential mechanic — where deciding to treat the AI as teammate vs. opponent measurably changes the AI's reciprocal behavior, and the player must live with an ally they made hostile by how they framed it.

## AI Integration Vector

**Player-AI Relationship:** BGR formalizes the building/coexisting vs. fighting axis as one continuous variable — reciprocity expectation — set by frame and updated by in-play behavior. The relationship is not a fixed mode but a running, mutual account that either side can default on.

**AI as Evolving System:** An AI that maintains and updates a reciprocity expectation toward the player — extending or withdrawing cooperation based on the accumulated ledger — is genuinely evolving through play; its stance is a learned function of shared history, not a script.

**AI as Development Environment:** The reciprocity ledger is a visible development readout: the player watches the AI's expectation of them rise and fall with each exchange, witnessing the relationship being computed. Betrayal and repair are observable state transitions, not cutscenes.

**Persistence:** What must persist is the reciprocity history — what each party did for and to the other across sessions. This is the highest-stakes thing to make persistent: an AI that *remembers being betrayed* and reciprocates accordingly is the entire emotional engine. Wiping it doesn't reset progress; it erases a relationship, which is the designed loss (Q8).
