---
type: answer
question: At what level of fidelity does a game's world model need to simulate for AI-generated quests to feel coherent?
related_concept: ../concepts/world-models.md
related_project: ../projects/game/gap-report.md
answered: 2026-06-07
tags: [ai, game-design, agents, simulation, world-models]
---

## Short Answer

Five symbolic fact tables at the complexity of a small relational database. No geometry. No physics. The fidelity axis that matters is *semantic richness of social and causal facts*, not physical simulation accuracy.

---

## Why Physics Is Not the Problem

Quest coherence is a constraint satisfaction problem, not a simulation problem. A quest becomes incoherent when it violates known facts — asking the player to find someone who is already dead, referencing an event that never happened, offering a reward the giver doesn't own. It becomes non-contextual when it ignores the current emotional or causal state. Neither failure requires physics to detect or prevent.

The right frame: a world model is sufficient for quest coherence when a **symbolic constraint-checker** can verify, before the quest reaches the player, that:

1. All referenced entities exist and are in the claimed state
2. The quest giver has a plausible reason to care (causal or relational connection to the task)
3. The task is achievable given current world state
4. The player hasn't already completed it or rendered it impossible

These are all symbolic checks over discrete facts. No simulation of continuous physical quantities enters any of them.

---

## Evidence from Shipped Systems

**Ultima VII (1992)** — NPCs had schedules and needs (hunger, sleep, money) tracked as simple integers. Quests emerged from those states. No physics beyond basic collision. State complexity: roughly 10–15 fields per NPC. The world felt alive from state density, not simulation fidelity.

**Dwarf Fortress** — coherence comes from an event log (what happened), memory (who remembers what), and emotional reactions (discrete symbolic tags on events). The richness people describe is causal density: many facts connected by causal edges, not accurate physics. The game runs no continuous physical simulation of character bodies during social events.

**Disco Elysium** — world state is entirely epistemic and social. Every quest trigger is a combination of: what the player knows, what an NPC believes about the player, and what has happened in the world. State is roughly 5–6 boolean or integer fields per character plus a shared event log. Zero physics in the quest layer.

**Left 4 Dead's AI Director** — reads player stress and resource state as approximately 4–5 scalar values (health, ammo, time since last threat, recent intensity). Adjusts the entire encounter feel in real time. The complete "responsive world" experience comes from 5 variables and a rule system over them.

**Classical AI planning (STRIPS, 1971)** — proved that coherent, goal-achieving action sequences can be generated from symbolic predicates alone: `at(robot, room1)`, `holding(robot, block)`. No continuous simulation. The insight transfers directly: a quest plan generated from symbolic world facts will be logically coherent if the facts are accurate. What makes it feel *specific* is the semantic richness of those facts, not their physical precision.

---

## The Minimum State Schema

Drawing from what the Side Quest AI system needs to know (per CLAUDE-reference.md Q1) and what the gap report identifies as missing from the wiki, the minimum is:

```json
{
  "events": [
    { "id": "", "what": "", "when": 0, "actor": "", "witnesses": [] }
  ],
  "entities": {
    "<id>": { "type": "", "status": "", "location": "", "owner": "" }
  },
  "relationships": [
    { "from": "", "to": "", "type": "", "strength": 0 }
  ],
  "player": {
    "choices": [],
    "inventory": [],
    "visited": [],
    "completed_quests": []
  },
  "npc_knowledge": {
    "<npc_id>": { "known_events": [], "beliefs": {} }
  }
}
```

Five tables. This is enough to:

- **Prevent contradictions** — entity status check before any quest is generated or presented
- **Ground motivation** — relationship graph tells you why an NPC would care about a task
- **Enable epistemic asymmetry** — each NPC knows a different subset of events; quests emerge from that gap between what they know and what the player knows or has done
- **Pass the specificity test** — quest references actual player choices from the `player.choices` log, not generic template slots

The gap report's "minimum state test" is a one-session build: write this schema, hard-code one world state, prompt the AI to generate 10 quests, count how many feel specific vs. generic. That is the empirical test for whether this schema is sufficient.

---

## Where the Minimum Falls Short

The minimum produces **logically coherent** quests that may be **emotionally flat** — this is the "sim-to-feel" gap (open question 3 in world-models.md). Emotional resonance requires motivation depth: not just that an NPC has a relationship with someone, but *why they care*, what the history is, what it costs them. This is not a physics fidelity problem. It is a semantic richness problem. The solution is more fields in the relationship and entity schemas (backstory, fear, goal, debt) — not more simulation.

Practically: start with the five-table minimum and build one quest. Evaluate it. The failure mode, if it occurs, will reveal which specific field is missing — that is faster than speculating about what richer state you need in advance.

---

## Conclusion

The threshold is symbolic, not physical. Full physics is overkill by several orders of magnitude. The minimum viable world model for quest coherence is a causal fact graph with per-NPC epistemic layers — approximately the complexity of a small relational database with five tables. Every shipped game that has achieved the "world responds to me" feeling has used some version of this, not physics simulation. The field to optimize is semantic richness of social and causal facts.

**Practical next step (from gap report):** Write the five-field game state JSON schema by hand, generate 10 quests against a fixed world state, evaluate. One session. This answers Q1 empirically.
