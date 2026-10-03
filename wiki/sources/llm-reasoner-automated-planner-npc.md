---
type: article
title: "LLM Reasoner and Automated Planner: A new NPC approach"
url: https://arxiv.org/abs/2501.10106
author: Israel Puerta-Merino, Jordi Sabater-Mir
published: 2025-01-17
ingested: 2026-06-08
tags: [ai, game-design, agents, llm, npc, grounding, pddl, automated-planning, neuro-symbolic]
concepts: [neuro-symbolic-agent-architecture, hallucinated-agency, world-models]
---
## Summary

Proof-of-concept implementation of a three-module intelligent agent architecture that combines an LLM for goal selection with a classical automated planner (PDDL) for action generation. Applied to the "FireFighter Problem" scenario in the RHYMAS multi-agent simulation framework. The Reasoner module uses an LLM to decide what goal to pursue given the current world state and personality traits; the Planner uses PDDL/Unified Planning to generate an executable sequence of actions to achieve that goal; the Interface coordinates both and communicates with the environment. Results show consistently plausible, human-like NPC behavior across multi-agent scenarios.

## Key Points

- **Core division**: "The Reasoner decides *what to do*; the Planner decides *how to do it*" — the LLM handles intent and goal selection from a list of possible goals; the automated planner handles valid action sequencing against the actual world state
- **Three modules**: (1) **Reasoner** — maintains a memory stream of world-state perceptions in natural language, holds personality traits, uses LLM to select among possible goals; (2) **Planner** — maintains the PDDL AP Problem (objects, predicates, goal), calls Fast Downward planner to generate action sequences; (3) **Interface** — receives world state updates, generates the possible-goals list, updates both Reasoner and Planner, executes the top action
- **Grounding mechanism**: the Interface maintains a live PDDL AP Problem updated every iteration; when the Planner generates a plan, every action in that plan is valid with respect to actual world state predicates — the LLM never directly produces actions, only goals
- **Personality traits**: supplied as a natural-language prompt field; influences goal selection but does not fully control it — the LLM exhibits "common sense" that sometimes overrides explicit personality (e.g., a firefighter instructed to prioritize fires will still sometimes save a trapped person first)
- **Memory stream**: a list of natural-language perceptions the NPC has experienced, updated by the Interface; provides the Reasoner's situational context without requiring the LLM to query world state directly
- **PDDL domain limitation**: the AP Domain Definition file must be manually authored; it is environment-specific and cannot be auto-generated from world state information — this is the primary scaling bottleneck
- **Technology stack**: Mistral model via LM Studio (local inference), Unified Planning Python library (AIplan4EU project), Rhymas multi-agent framework, Unreal Engine 5 front-end
- **Multi-agent results**: tested with 1–4 concurrent agents (CI=person in car, CO=common person, FF=firefighter prioritizing people, FP=firefighter prioritizing fires, PA=paramedic); agents consistently pursue goals aligned with their personality, with expected edge cases where common sense overrides personality
- **Emergent behavior**: agents not explicitly instructed about edge cases still handle novel situations reasonably — a common person with no firefighter available will call for them rather than attempting to extinguish the fire

## Quotes

> "The combination aims to equip an agent with the ability to make decisions in various situations, even if they were not anticipated during the design phase."

> "The Reasoner decides 'What to do' using the LLM's decision-making capacity, while the Planner decides 'How to do it' using the AP's planning capacities. This results in a reasonable, intelligent, reactive and humanized agent with a high degree of autonomy."

> "Full control over the agent's decisions remains elusive, so these traits can only generate some decision propensity."

## My Take

This is the cleanest articulation of the neuro-symbolic NPC architecture's core principle: the LLM handles the *semantics* of goal selection (what matters given who I am and what I perceive), the planner handles the *mechanics* of execution (what steps are actually valid in this world). Neither component tries to do both, and neither is burdened with the other's failure modes.

The "personality propensity vs. control" finding is worth emphasizing: the LLM introduces irreducible uncertainty into goal selection, which makes NPC behavior non-deterministic but also more plausible. This is actually desirable for games — fully deterministic behavior is what makes NPCs feel scripted — but it means personality is a *tendency*, not a specification.

The manual PDDL domain requirement is the key limitation and the core unsolved problem. LOOP and PSALM-V (both cited in the companion synthesis) directly attack this. Until it's solved, this architecture requires a dedicated knowledge engineer per game world.

AI intersection: this paper demonstrates that the renderer/simulator separation works at the NPC scale. The LLM is not asked to know what is real in the world — the Planner does that. The LLM is only asked to know what it wants, which is what it's actually good at. The division of labor by epistemic competence is the architectural insight that generalizes.
