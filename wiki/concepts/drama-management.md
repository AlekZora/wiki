---
type: concept
title: Drama Management
aliases: [drama manager, beat sequencing, narrative AI director]
tags: [ai, game-design, narrative, agents, systems, llm]
sources:
  - ../sources/mateas-gdc2003.md
  - ../sources/diamond-age-stephenson.md
updated: 2026-10-02
---

## Definition

An AI system that acts as an invisible director above a game simulation, monitoring story state and selecting the next narrative event (a "beat") from a curated pool to maintain a desired dramatic arc. The drama manager provides *global agency* — the player's cumulative interaction history shapes the high-level shape of the story — as opposed to the *local agency* of immediate NPC reactions within a single scene.

First formally described by Mateas and Stern in the Façade architecture (GDC 2003). Draws on earlier theatrical theory: a "beat" is borrowed from McKee's screenwriting — the smallest unit of dramatic action that moves a story forward.

## How I Think About It

The drama manager is the part of a narrative system that knows what the whole story should feel like, even as the simulation handles what's happening right now. It's the layer that keeps the experience from collapsing into either pure simulation (no shape, no arc) or pure scripting (no freedom, no surprise).

Façade's specific implementation:
- ~200 authored beats, each with preconditions, effects, and a tension delta
- A desired tension arc (Aristotelian rise/fall curve)
- Beat selection scores each candidate beat by how well its tension delta matches the desired arc's near-term slope
- The player's accumulated interaction history biases which beats are available (preconditions) and which are selected (weighted scoring)

The result: the player experiences a story whose shape they influenced without ever being offered a branch point. The plot feels mutable rather than forked.

Key insight from Façade's self-critique: the drama manager's quality is directly proportional to the richness of its beat library. With only human-authored beats, the system runs out of good options when player behavior is unusual — producing a flat or incoherent arc. The authorial burden is the system's fundamental bottleneck.

## AI Integration

- **LLMs eliminate the authorial bottleneck.** The most expensive part of Façade was hand-writing thousands of behaviors, dialogue lines, and reaction rules. A drama manager backed by an LLM can generate beat content dynamically — the author designs the *structure* (preconditions, tension effects, discourse act types) and the LLM fills the *substance* (the actual dialogue and reactions). This shifts the author's role from content producer to system designer.
- **Drama manager = planner layer.** In the Renderer → Simulator → Planner taxonomy from world-models research, the drama manager is precisely the planner. It reads simulator state (world facts, NPC conditions, player history) and generates the next narrative event. The LLM never touches world state directly — it only reads it, staying grounded.
- **Discourse acts as structured interface.** Façade's NLP layer mapped open-ended player text to ~40 discrete discourse acts (agree, criticize, flirt, etc.) before passing them to the reaction layer. This is the same function that a game state JSON serves in a modern LLM-driven quest system — a structured intermediate representation that keeps the generative layer grounded in the simulation's facts.
- **Beat preconditions as hard constraints.** The drama manager's precondition system maps directly to the hard-constraint validator concept in LLM-driven NPC quest generators. Beats that reference facts not present in the simulator should fail their preconditions — preventing hallucinated narrative events.
- **Tension arc as design language.** The desired value arc (Aristotelian tension curve) is a formal expression of the experience goal. This is a design pattern worth carrying forward: encode the experience you want as a target function the drama manager optimizes against, rather than scripting individual moments.
- **A drama manager whose target is the learner, not the plot.** Stephenson's *Diamond Age* Primer (1995) is a fictional drama manager for one child. It keeps a model of her "psychological terrain" and maps a "catalogue of the collective unconscious" (universal patterns like the Trickster) onto it. It also re-plans the story live from what she tells it ("As Nell spoke the words, the story changed in the Primer"). Its beat design is pedagogical: retryable failures (a heist that only works on the sixth or seventh attempt), deliberately unwinnable branches (once she agrees to go with the stranger, every path ends in capture), and a gradual handover until she narrates her own actions. The optimisation target is the learner's growth instead of a tension curve. See [adaptive-tutoring](adaptive-tutoring.md).

## Related Concepts

- [Emergent Narrative](emergent-narrative.md) — drama management is the structured counterpart: where emergent narrative arises from agent interaction without a director, drama management imposes arc on top of simulation
- [World Models](world-models.md) — the renderer/simulator/planner taxonomy; drama manager is the planner
- [Experience Goals](experience-goals.md) — the tension arc is a formalization of the experience goal; the drama manager exists to pursue it
- [AI Agents](ai-agents.md) — the believable agents (Grace and Trip in Façade) are the simulation layer the drama manager operates above
- [Adaptive Tutoring](adaptive-tutoring.md) — the same director layer pointed at one learner's development (the Diamond Age Primer)
- [Story as Excavation](story-as-excavation.md) — King's situational authorship vs. Façade's beat authorship: both resist plotting, but from different directions

## Open Questions

- How do you encode experience goals (beyond tension) as target functions the drama manager can optimize? Tension is tractable; surprise, intimacy, or disorientation are harder.
- At what granularity should beats be defined when the LLM generates their content? Too coarse and the drama manager loses control; too fine and the LLM's generation overhead becomes prohibitive.
- Can a drama manager handle multiplayer? Façade's architecture was explicitly designed for one player + two NPCs. With multiple players, whose history governs beat selection?
- What happens when player behavior consistently violates all beat preconditions? Façade deferred to generic deflection reactions. A better answer is needed.

## Project Connections

The Side Quest AI System's quest generator is a drama manager. It reads the game state JSON (simulator layer), evaluates NPC situations and player history (preconditions), selects a quest template (beat type), and passes everything to Claude Haiku (LLM planner) to generate grounded quest content. The four quest templates (exploration, collection, retrieval, callback) are Façade's beat library, compressed to four structural types with LLM-generated content filling each instance.

The "stake" field in the NPC schema is the drama manager's precondition signal for emotional salience — it tells the planner what kind of arc the NPC's situation warrants.

Key project file: wiki/projects/game/PROJECT-CONTEXT.md
