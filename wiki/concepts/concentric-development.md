---
type: concept
title: Concentric Development
aliases: [concentric design, core-first development, primary mechanics first]
tags: [game-design, production-methodology, project-management, creative-process]
sources:
  - "../sources/A Playful Production Process For Game Designers - Richard Lemarchand.md"
updated: 2026-05-11
---

## Definition

A hierarchical implementation strategy: fully build and polish the most fundamental mechanics (primary) before layering on secondary systems, then tertiary ones. Each ring builds on a stable, proven inner ring. The goal is to never build complex systems on an unstable, unproven base.

## How I Think About It

This is the production-side twin of [Elegance](elegance-game-design.md). Elegance says "fewer mechanics, more emergence." Concentric development says "build the most important mechanic *first and completely* before touching the next one."

Lemarchand's example: in Uncharted, core traversal (climbing, jumping) had to feel perfect before combat could be layered on, because combat happens *during* traversal. If traversal is broken, combat built on top of it is also broken — and you can't tell if combat is bad because of combat design or because the foundation is shaky.

The anti-pattern is building everything to 50% simultaneously. You end up with nothing proven, nothing polished, and no stable base for testing. Every playtest is contaminated by bugs in every system. You can't tell what's working.

This maps directly to software development: get the core loop right before adding features. It also maps to learning: [Whole-Game Learning](whole-game-learning.md) starts with a working whole, then deepens — concentric development starts with a working core, then expands.

The key insight is that concentric development is also a *knowledge* strategy: by finishing the core first, you learn what the project actually is before committing resources to the periphery. The periphery often changes once the core is solid.

## Related Concepts

- [Elegance (Game Design)](elegance-game-design.md) — elegance determines *what* the core mechanics are; concentric development determines *when* to build them
- [Whole-Game Learning](whole-game-learning.md) — parallel structure: start with the whole, deepen concentrically
- [Flow State](flow-state.md) — core mechanics must produce flow before secondary systems are added
- [Emergent Narrative](emergent-narrative.md) — narrative emergence requires the core character mechanics to be solid first

## Open Questions

- How do you identify which mechanic is truly "primary" when multiple systems are interdependent?
- Does concentric development work for non-game creative projects (films, novels, AI agents)?
- What's the right granularity — is "movement" one ring, or is "walking" one ring and "jumping" the next?

## Project Connection

For Dead Reckoning: build and prove the core character interaction mechanic (hidden agendas + social deduction) before adding environmental systems, external threats, or complex plot machinery. If the core social dynamics don't produce interesting emergent situations, no amount of secondary mechanics will save the project.

## Game Design Vector

**Mechanic:** The game's AI is built concentrically — the player proves the core AI behavior before any secondary behavior is added. Each ring of AI capability builds on a fully proven inner ring. If the core behavior is broken, no outer ring can be tested accurately, because every failure is contaminated by the inner ring's bugs. The player can see which ring the AI is currently at.

**2D Expression:** The concentric structure is spatially literal — inner rings of the game world are fully realized and polished while outer zones are sparse or incomplete. The player's progression moves concentrically outward, following the same logic used to build the game. The medium maps the methodology in a way that is legible as spatial depth rather than abstract architecture.

**Addictive Loop:** The player proves mastery of the core before the next ring unlocks — not through level-gating but through demonstrated competence with the primary mechanic. Each ring adds complexity on a stable, proven base. The player can trust each new layer because the previous one was solid. The loop is: prove the core → unlock the next ring → prove the new ring → unlock the next.

**Novel Angle:** The file's open question is the novel design direction: does concentric development work for AI agents? A game where the player builds an AI concentrically — proving each behavioral ring before adding the next — and observing what breaks when secondary behaviors are built on an unproven inner ring makes development methodology the explicit game content.

## AI Integration Vector

**Player-AI Relationship:** Staged construction — the player builds the AI one ring at a time, proving each layer before adding the next. The relationship is not with a finished AI but with an AI that is always in a specific stage of concentric development. The current ring is the active design surface.

**AI as Evolving System:** Concentric development provides a production discipline for AI evolution: the core behavior must be stable before secondary behaviors are layered on. An AI built concentrically has a deeply solid center and progressively less proven periphery. Development always happens at the outermost ring; the inner rings are stable.

**AI as Development Environment:** The player sees which ring the AI is at and what the proven inner rings look like. The stable, fully developed core is visible as a foundation; the current development ring is the active frontier. Building on an unproven inner ring produces failures that contaminate the outer ring — the player learns this by experiencing it.

**Persistence:** Completed rings persist unchanged across sessions — they are the proven foundation. The outermost ring is the active development frontier where things are still in motion. Persistence is ring-scoped: what is in a proven inner ring is permanent; what is at the current frontier may still change.
