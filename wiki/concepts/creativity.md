---
type: concept
title: Creativity
aliases: [creative thinking, creative process]
tags: [philosophy, psychology]
sources:
  - ../sources/creativity-wikipedia.md
  - ../sources/insight-learning-psychestudy.md
updated: 2026-04-12
---

## Definition

Creativity is the capacity to produce something both **novel and useful** — whether a tangible object, an idea, a theory, or a solution to a problem. The consensus definition is minimal; beyond "novel and useful," over 100 competing definitions exist in the literature. Creativity may also mean the ability to find new solutions to problems, not just produce new artifacts.

## How I Think About It

The historical arc is interesting: humans spent most of recorded history not believing they were creative at all — art was discovery (Plato), or divine inspiration, or transmission through a Muse. The modern concept of creativity as an individual human capacity is a post-Renaissance, post-Enlightenment idea. This matters because it means the category is much younger than it feels.

The Schmidhuber computational framing is the most useful for thinking about AI creativity: creativity is driven by the intrinsic reward of learning progress — compressing new regularities into a model. Random noise is boring (no compression). Already-known patterns are boring (no new compression). Only novel-but-regular patterns produce "wow-effects." This cleanly explains why the best creative work feels surprising yet inevitable — it's new regularity, not chaos.

The honing theory (Gabora) adds something the other theories miss: why the same creator's different works have a recognizable voice. If creativity is the process of resolving dissonance between a task and your worldview, then your worldview is the stable element that shows through in everything you make. This implies creative voice is a signature of a coherent worldview — and raises the question of whether AI systems have anything analogous.

Threshold theory (creativity correlates with IQ up to ~120, then the relationship weakens or reverses) suggests that beyond a base level of competence, the variables that drive creativity diverge from those driving general intelligence. Openness to experience is the personality trait most robustly correlated with creativity across domains.

The Four C model is practically useful for calibrating conversations: most human creativity is mini-c or little-c, not Big-C. Confusing them inflates both the threshold required to "be creative" and the stakes of creative work unnecessarily.

## Related Concepts

- [Cybernetics](cybernetics.md) — feedback loops in learning systems; Schmidhuber's "wow-effect" is a cybernetic reward signal
- [LLM Jaggedness](llm-jaggedness.md) — AI systems may be "creative" (in a narrow, RL-optimized sense) in some domains while frozen in others
- [Insight Learning](insight-learning.md) — the cognitive mechanism behind sudden creative breakthroughs; the "aha moment" as a discrete jump in understanding

## Open Questions

- Does the Schmidhuber account actually explain creativity, or just curiosity? What's the difference between seeking novel regularities and genuinely creating them?
- If creativity requires a worldview (honing theory), what does it mean for AI systems to be creative? Is context window = worldview?
- Is Big-C creativity qualitatively different from little-c, or just more of the same process?
- What does the cross-cultural variation in the concept of creativity (27/28 African languages have no direct translation) imply about whether creativity is a universal human capacity or a culturally constructed category?

## Game Design Vector

**Mechanic:** The AI's output is evaluated against the Schmidhuber criterion — the player steers the AI toward the productive middle zone between pure noise (no compression, no pattern) and already-known regularity (no new compression, boring). Too much constraint produces repetition; too little produces incomprehensible output. The game is calibrating the AI toward the zone that produces genuine "wow-effects": surprising yet inevitable, new regularity rather than chaos.

**2D Expression:** The Schmidhuber criterion maps onto 2D visual pattern — the player can see in real time whether the AI's behavior is in the noise zone, the regularity zone, or the productive middle. In 2D, pattern and deviation from pattern are simultaneously visible across the whole plane. The "novel-but-regular" target is visually assessable without external scoring.

**Addictive Loop:** The AI's output trajectory follows the wow-effect curve: the player steers it toward the productive middle, but calibration drifts — the AI tends toward either repetition (pattern without novelty) or noise (novelty without pattern). Each session reveals whether the calibration held, improved, or drifted. The compulsive loop is continuous re-calibration toward a moving target.

**Novel Angle:** The honing theory question is the unexplored design direction: does the AI have a worldview — a stable element that shows through in everything it makes? A game that deliberately gives an AI a coherent interpretive frame (not a scripted personality but a stable worldview) and lets the player observe whether a recognizable creative voice emerges from it has never been shipped.

## AI Integration Vector

**Player-AI Relationship:** Aesthetic coexistence — the player evaluates the AI's creative output and steers it toward or away from the wow-effect zone. The relationship is between a creative director and a creative system: the player doesn't specify the output, they evaluate it and adjust the conditions that produce it.

**AI as Evolving System:** The Schmidhuber account frames creativity as a learning-progress signal — the AI seeks novel-but-regular patterns because compressing them produces intrinsic reward. An AI that evolves through play toward greater novelty-with-regularity is developing its creative range. Development is measurable against the wow-effect: are the AI's outputs becoming more surprising-yet-inevitable, or drifting toward noise or repetition?

**AI as Development Environment:** The player observes the AI's creative output shifting across sessions — becoming more surprising, more coherent, or drifting into noise or predictability. The development trajectory is visible as a change in the AI's output distribution: does this session's output feel different from last session's in the right direction?

**Persistence:** The honing theory implies the AI should carry a stable worldview across sessions — the element that shows through in everything it makes. Persistence here is the accumulated interpretive frame: the coherent set of dispositions that gives the AI's creative output a recognizable signature across sessions, even as individual outputs vary.
