---
type: concept
title: MICE Quotient
aliases: [story type taxonomy, narrative contract, milieu-idea-character-event]
tags: [narrative, writing-craft, storytelling, ai, agents, game-design, fiction]
sources:
  - ../sources/characters-and-viewpoint-card.md
updated: 2026-06-22
---

## Definition

A taxonomy of story types proposed by Orson Scott Card. Every story is composed of four factors in varying proportions: **Milieu** (the world — physical, cultural, social), **Idea** (information the reader is meant to discover), **Character** (the inner nature of one or more people; how they change or fail to change), and **Event** (what happens and why; a disruption and its resolution). The factor that dominates determines the story's structure, the kind of characterization it requires, and its implicit contract with the reader about when the story is finished.

## How I Think About It

The MICE Quotient solves a problem most craft advice ignores: not all stories require the same kind or depth of characterization. If Milieu dominates, characters are primarily lenses — they move through the world and reveal it to the reader. We don't need their full psychology. If Character dominates, the inner arc is the point; we need to know not just what they do but why they are that way and what they become. If Idea dominates, characters serve clarity — their job is to make the information emotionally real. If Event dominates, characters need to be competent and reactive; what matters is how they handle pressure.

The structural corollary: what changes when a dominant-factor story opens is what must resolve when it closes. A Milieu story opens when a character enters the new world and ends when they leave or have understood it. A Character story opens when a character can no longer cope with who they are and ends when they have changed — or confirmed they cannot. An Idea story opens with a question and ends when it is answered. An Event story opens with a disruption to normal order and ends when order is restored or permanently altered.

This is a decision framework, not just a diagnostic. Before writing or generating a scene, quest, or episode, ask: which MICE factor dominates here? That answer determines what the reader (or player) is owed at the end.

## AI Integration

- Quest generators without a MICE-equivalent classification produce structurally incoherent output: quests that open a character arc and close with a world-exploration reward, or pose a mystery and resolve it through combat. The MICE Quotient is the contract the generator must honor.
- In a game NPC quest system, each quest template should map to a dominant MICE factor. The generator's output must satisfy the structural contract that factor implies. This is why [[drama-management]] systems like Façade track narrative beat types — beats are implicit MICE classifications.
- LLMs generating narrative content will default to mixing MICE factors incoherently because training data is mixed. Explicit MICE classification in the system prompt constrains output toward structural coherence.
- In agentic systems, MICE maps onto task types: exploration tasks (Milieu), discovery/search tasks (Idea), adaptation/learning tasks (Character), disruption-response tasks (Event). Each type rewards different planning strategies.
- MICE explains why genre conventions exist: they are socially agreed dominant factors. Mystery is Idea-dominant (question → answer). Romance is Character-dominant (incomplete self → transformation through relationship). Thriller is Event-dominant (disruption → resolution). Worldbuilding-heavy sci-fi/fantasy is often Milieu-dominant. Genre signals tell the reader which contract is active before the first page.
- For AI-generated interactive narratives, MICE provides a principled way to design player-facing branches: each branch is a different MICE entry point into the same situation, giving different players a differently-structured experience while sharing underlying world state.

## Related Concepts

- [Drama Management](drama-management.md) — beat sequencing systems are implicitly MICE-aware; beats track which narrative obligation is currently active
- [Emergent Narrative](emergent-narrative.md) — emergent narrative produces MICE-mixed output by default; explicit MICE classification is one way to give emergent systems more structural coherence
- [Story as Excavation](story-as-excavation.md) — Card's character interrogation ("keep asking why") is the excavation approach applied to character; MICE is the structural frame that surrounds and guides that excavation
- [Experience Goals](experience-goals.md) — the experience goal for a quest or session closely corresponds to its dominant MICE type: the dominant factor determines what the player should feel at resolution

## Open Questions

- Is MICE a complete taxonomy, or are there story types it doesn't cleanly capture? (Metafiction, autofiction, interactive narrative with player-driven MICE drift?)
- In a game with procedurally generated quests, should MICE type be selected by the system based on narrative context, or implied by the NPC's situation and emotional state?
- Can a single quest simultaneously honor two MICE contracts without structural incoherence? Or does serving two dominant factors dilute both?
- How does MICE interact with player agency? A player who wants an Event resolution inside what the system has classified as a Character quest creates a contract mismatch — should the system adapt or hold the original contract?

## Project Connections

- Side Quest AI: quest templates (callback, discovery, favor, conflict) implicitly map to MICE types. Explicitly labeling each template with its dominant MICE factor would clarify what the quest generator is contracted to deliver at resolution, and give the AI lens validation for whether output is structurally complete.
