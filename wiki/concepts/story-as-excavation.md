---
type: concept
title: Story as Excavation
aliases: [situation-driven narrative, story discovery, fossil model of fiction]
tags: [narrative, creative-process, writing-craft, storytelling, ai, agents]
sources:
  - ../sources/On Writing_ A Memoir of the Craft - Stephen King.md
updated: 2026-06-08
---

## Definition

The epistemic stance that a story pre-exists in potential and the writer's job is to uncover its true shape rather than construct one. The writer devises a "What if" situation, places characters in it, and honestly records what they do — excavating the story rather than engineering it. Plot is not planned; it emerges from character behavior under pressure.

## How I Think About It

King's fossil metaphor is the clearest statement of this idea: a story is already there, like a dinosaur bone in rock. Planning the plot before you've written it is like deciding where the skeleton's joints are before you've dug it up — you'll either force it into the wrong shape or break it. The writer's discipline is to follow what the situation and the characters actually demand, not what a pre-made outline says should happen.

The practical consequence: situation is the seed, not the ending. Start with "What if a woman's biggest fan holds her captive?" (*Misery*). Don't decide what happens next. Put a character in that situation and ask: what would this specific person actually do? The story is found in the honest answer.

This is distinct from [[emergent-narrative]], which describes systems (game mechanics, AI agents) that generate story as a byproduct of agent interaction. Story-as-excavation is about the individual writer's cognitive relationship to their own material — treating it as discovery, not construction. Both produce the same anti-plotting conclusion, but from different starting points.

The failure mode it diagnoses is "plot-first" writing: the writer decides what should happen, then makes the characters do it. This produces characters who feel like puppets — they act against their own logic to serve the author's outline. Readers detect this as falseness. The excavation model forces the writer to stay honest about character, which is where authentic fiction lives.

The "door closed / door open" two-draft process is excavation's companion mechanism. The first draft is the dig — fast, rough, private, focused on finding the shape. The second draft is the cleaning and mounting — slow, analytical, for the audience. Mixing the two (editing while digging, or digging for an audience) ruins both.

## AI Integration

- LLMs can be understood literally as excavation engines: the model is sampling from a latent space of human narrative possibility formed from millions of texts. The story is already "in there" in statistical potential; generation is the act of finding a coherent path through that space. Prompting as situation-seed fits this model: give the system a compelling "What if" and constrain the path without scripting the destination.
- Empirically, situation-seed prompts tend to outperform plot-spec prompts for LLM story generation. "A surgeon is trapped in a blizzard with a patient who turns out to be the drunk driver who killed her daughter" generates more interesting output than "Write a story where a surgeon first refuses to help someone, then helps them, and learns forgiveness." The situation forces the model to excavate; the plot spec forces it to execute.
- Narrative agents in interactive fiction or game NPC systems can be architected around the excavation model: give each agent a defined situation (goal, fear, secret, resource state) and let behavior emerge from agent-to-agent and agent-to-environment interaction. The designer is the geologist who sets the strata — not the sculptor who carves the shape.
- The "door closed" first draft maps to an unconstrained generation pass (high temperature, no critic); the "door open" second draft maps to a constrained revision pass (critic model, pruning, coherence check). Separating these passes is an architectural principle with empirical support in multi-agent writing pipelines.
- The Ideal Reader (see [[ideal-reader]]) is the excavation's quality signal: not "does this follow the outline" but "does this feel true to someone who knows what true feels like."

## Related Concepts

- [Emergent Narrative](emergent-narrative.md) — systems-level version of the same anti-plotting insight; agents interacting produce story nobody authored
- [Ideal Reader](ideal-reader.md) — the quality signal that tells the excavating writer when they've found the real shape
- [Creativity](creativity.md) — Gabora's honing theory: creative work resolves dissonance between task and worldview; excavation is a method for following that resolution honestly
- [World Models](world-models.md) — the latent space an LLM is sampling from is a world model; generation is a traversal of that space

## Open Questions

- Is "treating it as excavation" a productive cognitive stance, or just a useful fiction that happens to produce better output? Does the epistemic model matter, or only the behavioral output?
- Does the excavation model break down at scale? King writes novels; does situation-first work for 500-page arcs, or does it only apply at the scene and chapter level?
- Can an AI agent genuinely "excavate" in the sense of surprising its operator, or is generation always constrained enough by training distribution that the surprise is illusory?
- What is the minimum character complexity needed before situation-driven generation produces narratively satisfying emergence? (Connects to [[emergent-narrative]] open questions.)
