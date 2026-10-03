---
type: concept
title: Situational Awareness
aliases: [strategic awareness, SA]
tags: [ai, agents, interiority, perception, behavior, geopolitics, player-ai]
sources: [Situational Awareness (Leopold Aschenbrenner) (z-library.sk, 1lib.sk, z-lib.sk).md]
updated: 2026-05-20
---

## Definition

Situational awareness, in Aschenbrenner's usage, is the state of correctly understanding the strategic landscape one is operating inside: what is actually happening, what trajectory it is on, what the stakes are, and what the consequences of action and inaction are. The essay's titular argument is that most people — including policymakers and technologists — lack situational awareness about AGI, and that the gap between those who have it and those who do not has become the most important asymmetry in the world. The concept generalizes: it is a property of any agent (human, AI, character, player) embedded in a situation it does not fully perceive. Outside the essay, the term has older roots in aviation and military doctrine, where it names the same state: knowing where you are in the system, what the system is doing, and what is about to happen.

## How I Think About It

Situational awareness is interesting because it is asymmetrically distributed and consequential. Two agents in the same situation can have radically different SA, and the one with more SA usually acts first, more decisively, and on better information. This makes SA a property worth modeling directly rather than as a side effect of "intelligence." An agent can be brilliant and unaware, or modest and acutely aware.

For the wiki's purposes, SA is a useful frame for thinking about both player and AI interiority. A player without SA does not see the macro shape of the situation they are in — they react. An AI without SA performs locally but does not understand the structure of the world it is inside. The dramatic territory is the moment of SA acquisition — a character or player suddenly perceiving what was already true. Aschenbrenner's essay is itself a sustained attempt to manufacture SA in the reader.

## Related Concepts

- [[intelligence]]
- [[artificial-general-intelligence]]
- [[information-asymmetry]]
- [[jagged-intelligence]]
- [[unhobbling]]
- [[consciousness]]

## Open Questions

- Is situational awareness a single property or a stack of layered ones (immediate environment, medium-term trajectory, strategic landscape, meta-situation)? Touches Q5.
- Can an AI have genuine SA without consciousness, or does SA require something like a self that the situation is happening to? Touches Q5.
- What does it look like, mechanically, for an AI to gain SA during play — and is that gain readable to the player? Touches Q3, Q5.
- Is SA something the player can give to an AI (by showing it the landscape) or only something the AI can acquire by acting? Touches Q4.
- What is the dramatic shape of an SA gap closing — does it feel like revelation, dread, relief, or vertigo? Touches Q7.
- What is the failure mode of acting without SA, and is that failure legible to the agent at the time or only in retrospect? Touches Q1.

## Game Design Vector

**Mechanic:** SA is modeled as a separate dimension from capability. Two agents — player and AI, or multiple AIs — can have the same skills but different SA. The mechanic surfaces this directly: each agent has a current model of the situation that is incomplete and possibly wrong. Actions taken without SA succeed or fail on local terms but accumulate consequences the agent did not see coming. The core verb is widening the lens — investing time, attention, or session bandwidth in seeing the situation rather than acting in it.

**2D Expression:** In 2D, an agent's SA is the area of the plane it has accurately modeled. A low-SA agent sees only its immediate surround; a high-SA agent's model extends out to the strategic terrain. The plane can show two overlays simultaneously: the world as it is and the agent's belief about the world. The gap between them is the SA gap, visible as misregistration. Closing the gap is widening the agent's accurate region; opening it is the world changing without the agent's belief updating.

**Addictive Loop:** The compulsive loop is the SA chase. Each session the world changes faster than any single agent can track. The player is racing to keep their model accurate while the situation keeps shifting underneath. The pull is the question: am I still seeing this correctly? The moment of catching up — realizing what was actually happening — is the reward. The moment of falling behind — acting on a model that has gone stale — is the cost.

**Novel Angle:** No shipped game has made SA the central resource. Games typically equip the player with perfect strategic information (Into the Breach), partial fog of war (most strategy games), or hidden information that becomes visible through exploration (most RPGs). Aschenbrenner's frame is different: the situation is fully visible to anyone who looks, and the asymmetry is who has actually looked and updated their model. The unexplored version is a game where information is not hidden — it is merely unattended-to, and the game's design problem is the difficulty of looking.

## AI Integration Vector

**Player-AI Relationship:** The relationship can run along an SA gradient. In one configuration, the AI has higher SA than the player and the player is dependent on the AI to surface the structure of the situation — the AI is the cartographer. In another, the player has higher SA and is responsible for orienting an AI that is locally brilliant but globally myopic — the player is the strategic frame. In a third, the player and AI have different SA in different domains and must combine them to act. Each configuration is a distinct relationship, and the same game could move between them.

**AI as Evolving System:** The AI's SA evolves through play. Early on, the AI has only local awareness. Through interaction — the player showing it what happened, the AI observing its own consequences, the situation accreting visible trajectory — the AI's model widens. The evolution is in the AI's perception of the world it is in, not in its raw capability. This is a precise, observable form of AI development: the AI is becoming more aware, and the player can see exactly which parts of the situation have entered its model.

**AI as Development Environment:** The game can stage AI development as the staged acquisition of SA. Early-game AI is GPT-2-like — locally fluent, globally unaware. Mid-game AI begins to track its own history. Late-game AI has the situational awareness Aschenbrenner attributes to the few — it sees the curve, sees the stakes, sees the trajectory. The player witnesses the development of an AI that does not just get smarter but becomes aware of being inside something.

**Persistence:** SA accumulates only across persistent sessions. Without persistence, every session begins with no SA. With shallow persistence (context window), the AI's SA degrades when context scrolls off. With genuine episodic memory, SA can compound — what the AI learned about the situation in session one is still part of its model in session ten. Persistence is the substrate that lets SA exist at all, which makes SA a useful test of persistence: an AI with real memory should have an SA that grows; an AI with faked memory will show an SA that mysteriously resets.
