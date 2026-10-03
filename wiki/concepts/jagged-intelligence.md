---
type: concept
title: Jagged Intelligence
aliases: [jagged capabilities, spiky LLM performance]
tags: [ai, llm, philosophy]
sources: [karpathy-no-priors-code-agents.md, karpathy-sequoia.md]
updated: 2026-04-30
---

## Definition

Jagged intelligence describes the uneven, spiky capability profile of LLMs. A model can be simultaneously superhuman at tasks that fall inside RL-verifiable or heavily-trained domains and stuck at the level of a child (or stuck in 2020) at tasks outside those domains. The same model that writes a production-quality systems program can't reliably tell a fresh joke — because joke variety sits outside what RL optimization targets.

## How I Think About It

The "jagged" metaphor is useful because it counters two failure modes: overestimating the model (assuming PhD performance generalizes everywhere) and underestimating it (writing it off because it failed somewhere basic). The actual question is always: does my specific problem sit inside or outside the model's trained/RL circuits?

The chess example from the Sequoia talk is illustrative: GPT-4o spiked in chess capability not because of some general reasoning improvement, but because chess data entered the pre-training mix. Capability is at the mercy of what the lab chose to put in. This means capability improvements don't generalize — they cluster around whatever domains the training process optimized for.

The "same joke" problem is the clearest marker of the soft ceiling: outside RL-verifiable domains, the model defaults to its modal output with no pressure to improve. There's no gradient signal pushing it toward variety.

## Related Concepts

- [speciation-of-models](speciation-of-models.md)
- [agentic-engineering](agentic-engineering.md)

## Open Questions

- Is there a reliable way to test whether a specific task sits inside or outside the RL circuits before committing to a model?
- Does more compute reliably expand the jagged frontier, or just sharpen existing peaks?
- How much of the jaggedness is fixable with fine-tuning vs. requiring fundamentally different training objectives?
- The "stuck in 2020" framing — is this a training data cutoff artifact or something structural about how RL shapes the distribution?

## Game Design Vector

**Mechanic:** The AI's capability profile is jagged — nearly unbeatable within its trained corridors, child-level outside them. The player must map where the peaks and valleys are, designing challenges that exploit the valleys and survive the peaks. A challenge inside the AI's RL corridor is a different game entirely from one outside it; the player must recognize which terrain they're in before choosing their approach.

**2D Expression:** The AI's jagged capability is spatially legible — certain zones of the 2D world correspond to the AI's trained corridors (nearly impossible to beat the AI there), others correspond to its unoptimized domains (the AI produces near-random behavior). The player navigates between these zones, choosing when to engage the AI inside its peaks and when to lure it into its valleys. The map is a capability topology.

**Addictive Loop:** The player maps the jagged frontier — discovering where the corridor edges are, finding the transitions from superhuman to child-level, exploiting valleys while surviving peaks. Each session extends the map of the AI's capability topology. The frontier is never fully mapped, because capability improvements in one domain may shift adjacent domains in unpredictable ways.

**Novel Angle:** No shipped game has made the AI's jagged capability profile the primary terrain — a world whose difficulty is not uniformly distributed but spiked and hollow in ways determined by what the AI was trained on. The player's intelligence is applied to topology-reading: understanding the shape of the jagged frontier rather than developing uniform skill.

## AI Integration Vector

**Player-AI Relationship:** Adversarial intelligence-gathering — learning where the AI is godlike and where it is a child, and building strategy around that map. The relationship requires the player to develop an accurate model of the AI's capability topology, not just respond to its outputs. Fighting an AI that you partially understand is different from fighting one you don't.

**AI as Evolving System:** Capability improvements don't generalize — they cluster around training/RL domains. As the AI evolves through play, it develops new peaks in domains the game exercises heavily, while valleys in unexposed domains persist unchanged. The jagged profile changes shape as the player plays: some spikes grow, others don't, and the overall jaggedness remains even as specific peaks shift.

**AI as Development Environment:** The AI's training history is legible as its capability topology: what was heavily evaluated shows as a peak, what was never evaluated shows as frozen performance. The player reads the AI's development history in the shape of its jagged frontier.

**Persistence:** RL-optimized peaks persist across sessions because the optimization was durable. Valleys persist because no gradient ever touched them. The jagged topology is the stable structure the AI carries across sessions; what changes with play is the height of specific peaks in the zones the game exercises. The overall jaggedness does not reduce.
