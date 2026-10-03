---
type: concept
title: Speciation of Models
aliases:
  - model speciation
  - AI speciation
tags:
  - ai
  - ml
  - llm
  - agents
  - systems
  - biology
  - ecosystem
  - specialization
  - emergence
  - philosophy
sources:
  - karpathy-no-priors-code-agents.md
  - origin-of-species-darwin.md
updated: 2026-07-10
---

## Definition

Speciation of models is the idea that rather than one monoculture model attempting to be good at everything, the AI ecosystem should evolve toward specialized intelligences — each tuned for a distinct niche, the way animal brains have diversified across species. Karpathy frames the current lab approach (one large general model) as monoculture, and speciation as a pressure that exists but hasn't yet materialized because the science of deep fine-tuning without capability loss isn't mature. The mechanism sitting one level below the concept is [[natural-selection]] — specifically Darwin's "principle of divergence of character," which observes that populations under sustained selection radiate outward into ill-occupied niches, because specialists outcompete their more average relatives at the niche edges.

## How I Think About It

The animal kingdom analogy is apt: a dolphin's brain isn't a worse human brain, it's optimized for a different problem space. The monoculture approach assumes one model can cover all niches without meaningful trade-offs — which is probably false at the edges. The reason speciation hasn't happened yet is a technical one: fine-tuning tends to improve the target capability at the cost of degrading others (catastrophic forgetting, capability collapse). Until that's solved, labs default to the safest path, which is the big general model.

The pressure toward speciation is real even if the execution isn't there yet. Verifiable-domain tasks (code, math, science benchmarks) are already seeing specialized models pull ahead. The question is whether soft domains will follow the same path or remain monoculture forever.

The right image is horticultural rather than mechanical. Specialists don't get manufactured to spec; they get grown — cultivated over time with curated data, feedback shaping, and exposure to their target niche. That framing turns AI development from a factory floor into a garden, and turns the humans doing the work into growers rather than engineers.

## AI Integration

**How AI changes or advances this concept.** Speciation is not a metaphor imported into AI from biology — it is a diagnosis of what AI development itself could look like once fine-tuning without capability loss becomes tractable. Continual learning, adapter methods (LoRA and its descendants), retrieval-augmented specialization, and mixture-of-experts routing all move the field incrementally toward speciation. The concept sharpens further as base-model training commoditizes and the leverage shifts to differentiation rather than raw scale.

**How this concept could inform AI agent design.** Design agent systems as populations, not solo generalists. Route tasks to specialists by niche fit rather than expecting one agent to cover everything. Make specialization legible: the operator should be able to see which specialist owns which niche and where the niche edges are. Treat catastrophic forgetting as a first-class design concern — when a specialist is fine-tuned into a new niche, know what capability profile you gave up. The operator's role shifts from prompt author to ecosystem manager.

**What AI applications exist or could exist in this domain.** Already emerging in verifiable domains (code, math): specialized models pull ahead of generals on narrow benchmarks. Could exist: palliative-care specialists, per-biome ecological specialists, traditional-knowledge preservation specialists, neurodivergent-fit tutoring specialists, per-craft artisan specialists. The organizational analog is "one agent per role" replacing "one super-agent for the entire org." The civilizational analog is a diverse ecology of trained minds instead of a single monoculture.

**What this concept reveals about intelligence, behavior, or systems relevant to AI.** Intelligence is not a scalar. The dolphin brain is not a worse human brain — it is optimized for a different problem space. General and specialized intelligence are different products, not different points on the same axis. Monoculture is fragile: one training run, one alignment target, one corporate incentive shapes the entire ecosystem. Speciation is resilient in the way biological ecosystems are: heterogeneous, distributed, harder to collapse in a single failure. This flips the AI safety question — a plural ecosystem is a fundamentally different threat model than a single frontier lab's chosen values.

## Related Concepts

- [natural-selection](natural-selection.md) — the underlying mechanism; speciation is what natural selection does to a population of models when the variation pool is rich enough and the selection pressure varies by niche
- [jagged-intelligence](jagged-intelligence.md) — jaggedness is what monoculture produces at the edges; speciation is one structural response
- [coevolution](coevolution.md) — specialists coevolve with the niches they inhabit; the ecosystem changes both sides at once
- [swarm-intelligence](swarm-intelligence.md) — the inverse pole: many uniform units vs. many differentiated ones
- [ai-agent-personality-design](ai-agent-personality-design.md) — specialists carry distinct behavioral profiles by construction, not by prompt
- [verified-intelligence](verified-intelligence.md) — verifiable domains are where speciation is already visible in the wild
- [world-models](world-models.md) — different niches necessarily produce different world models
- [wet-ai](wet-ai.md) — biological register for cultivation, growth, and ecology as AI development metaphors
- [unhobbling](unhobbling.md) — specialization is often an unhobbling scoped to a single niche
- [assembly-of-complexity](assembly-of-complexity.md) — specialists as composable components in larger assembled solutions
- [culture-universe](culture-universe.md) — ecosystems of specialists as cultural niches at civilizational scale
- [memory-forgetting](memory-forgetting.md) — catastrophic forgetting is the current technical obstacle to specialization without loss

## Open Questions

- What does "the science of fine-tuning without capability loss" actually require — better training methods, better data curation, or architectural changes?
- Is speciation more likely to emerge from open-source fine-tuning ecosystems or from frontier labs deliberately carving niches?
- Are there domains where a specialized model would be categorically better than a general one, or just marginally better?
- Does speciation increase or decrease the risk of AI misuse (specialized models for narrow harmful tasks)?
- Who chooses which niches deserve specialists — the market, a new profession of "growers," or emergent user pressure?
- How do specialists exchange knowledge with each other without collapsing back into monoculture?
- What social and economic structures emerge around a speciated AI ecosystem — guilds, breeders, curators, ecologists, insurers?
- Can specialist populations go extinct, and what would "AI biodiversity loss" mean at civilizational scale?
- Is monoculture a stable attractor because of economies of scale, or a transient artifact of current training methods?
- Does speciation shift AI safety from a unipolar alignment problem to a pluralistic ecology problem, and are current safety frameworks equipped for the shift?
- What is the human role in a speciated ecosystem — peers, growers, ecologists, or all three at different scales?
- What does "diversity" mean for a population of models — architectural diversity, training-data diversity, alignment-target diversity, or behavioral diversity?

## Project Connections

- **Side Quest AI game.** SQAI can serve as a small-scale demonstration of the film's civilizational thesis. The current SQAI architecture (one Haiku model for all NPCs) is the monoculture pattern in miniature. A speciation version treats each NPC as its own specialist — via prompt + curated context in the near term, potentially per-NPC fine-tuning long term. The player becomes an ecologist rather than a prompt author. This tightens SQAI's "disorienting recognition" experience goal: recognition becomes plural, not singular — the world's specialists have each been paying attention to the player's story from their own niche. See [[../../memory/project_game_side_quest.md]].
