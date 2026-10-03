---
type: article
title: "High-quality generation of dynamic game content via small language models: A proof of concept"
url: https://arxiv.org/abs/2601.23206
author: Morten I.K. Munk, Arturo Valdivia, Paolo Burelli
published: 2026-05-19
ingested: 2026-06-08
tags: [ai, game-design, llm, slm, fine-tuning, game-content-generation, procedural, pddl, dag]
concepts: [task-specialized-slm-networks, hallucinated-agency, neuro-symbolic-agent-architecture]
---
## Summary

Proposes aggressively fine-tuned small language models (SLMs) as an alternative to LLMs for dynamic game content generation. The core argument: LLMs are cloud-dependent, costly, and narratively incoherent on complex tasks; naive SLMs perform poorly; but SLMs fine-tuned on narrowly scoped tasks using synthetically generated DAG-structured training data can match LLM quality for those tasks while running locally at real-time speeds. Proof-of-concept: DefameLM, a fine-tuned Llama 3.2-1B that generates medieval RPG smear campaigns (reputational conflict game loop). Results: 8-bit quantized model achieves ~93% success under LLM-as-judge evaluation, with median generation time of 2.5s on consumer GPU hardware.

## Key Points

- **Two context types**: *open-ended* contexts require multiple coordinated SLMs (each handling a subtask); *game-loop-anchored* contexts (generation tied to an explicit, fixed game situation) are narrow enough for a single SLM — this is the proof-of-concept target
- **Task complexity framework**: complexity = number of correlated "base dimensions" that must be jointly satisfied (e.g., intelligence synthesis + rhetorical angle + audience targeting + alignment simultaneously); harder tasks require narrower scope and higher specialization
- **DAG-based synthetic training data**: a teacher LLM (GPT-4o) generates 1,800 diverse input-output pairs following a DAG structure — choice nodes select from predefined lists, generation nodes produce LLM-generated content; the DAG controls input variety while ensuring game-world adherence; GPT-4o-mini writes description text, final GPT-4o call produces output
- **DefameLM**: Llama 3.2-1B fine-tuned via LoRA (α=128, rank=256, prompt-loss weight 5%) on 1,440 training pairs; task: given sender/target character metadata + 3 intelligence items + rhetorical angle + target audience → ~150-word medieval smear campaign poster
- **Quantization results** (AMD Ryzen 9 7950X + NVIDIA RTX 3070 8GB VRAM):
  - 16-bit: 2.48 GB, median generation 4.8s, ~93% success — **slowest practical**
  - 8-bit: 1.32 GB, median generation 2.5s, ~93% success — **robust practical choice** (statistically indistinguishable from 16-bit, p=0.41)
  - 4-bit: 808 MB, median generation 2.1s, ~78% success — introduces new failure modes on hardest prompts
- **Retry-until-success strategy**: temperature T=0.75; retry if LLM-as-judge fails; >80% of prompts succeed within 2 attempts for 8-bit/16-bit models; expected time-to-success stays within 5-second budget for vast majority of prompts
- **LLM-as-judge**: GPT-4o evaluates 7 criteria (overall assessment, angle implementation, intelligence implementation, alignment/no-hallucination, writing quality, audience targeting, rhetorical targeting); overall verdict = minimum across all criteria (all must pass); writing quality, audience targeting, and rhetorical targeting achieved perfect scores across all models — these were dropped from comparative reporting
- **Creativity-consistency trade-off**: structured input/output format reduces creative range but is necessary for quality consistency; highly structured prompts produce stylistic repetitiveness across outputs — DAG-based data generation addresses this by varying inputs, but the tension is not fully resolved
- **Key limitation**: local quality assessment (replacing cloud LLM-as-judge at runtime) remains unsolved; deployment requires either a local judge model or a different quality-assurance strategy (batch pre-generation, simplified rubric)
- **World-grounding mechanism**: DAG choice nodes query actual game state (factions, character metadata) at runtime — the model receives real game entities as inputs and is trained to stay within them; constraint adherence is in the weights, not an external validator

## Quotes

> "More difficult tasks require narrower scope and higher specialization to the training corpus."

> "By targeting scenarios where the generative task is challenging but the scope remains narrow enough for aggressive fine-tuning to reliably produce quality outputs, we can investigate if the most fundamentally difficult tasks are feasible in this framework."

> "The creative role shifts from authoring individual pieces to designing the systems and constraints that generate them."

## My Take

This paper is the complement to the neuro-symbolic approach, not the alternative. Where the PDDL-based architecture prevents hallucinated agency through external constraint enforcement (the planner rejects invalid actions), the SLM approach prevents it through internal constraint absorption (the model never learned to generate content outside the game world's scope). Both solve the grounding problem; they differ in where the constraint lives.

The DAG-based training data generation is the most transferable technique here. It's a systematic methodology for generating high-quality, structurally varied synthetic training data for any narrowly scoped task: decompose the input space into choice nodes (discrete game-world facts) and generation nodes (open-ended text), then use a teacher LLM to generate outputs. This pattern is general beyond games.

The 8-bit sweet spot finding is practically important for the Side Quest AI project. If a quest-generator SLM can be fine-tuned on synthetic quest data derived from the game's state structure, it could run entirely locally, stay within the game world's constraints by construction, and generate at 2–3 seconds — comfortably within a "walk to the quest giver" masking window. The local judge problem is the critical remaining issue.

The creativity-consistency trade-off is honest and worth attending to. Fine-tuned SLMs heavily mirror their training data's style and structure. For DefameLM this produces some repetitiveness; for a quest generator, it might produce formulaic quests. The DAG approach addresses variety at the input level; the output style is harder to diversify without degrading consistency.

AI intersection: this paper demonstrates that the grounding problem can be solved at training time rather than inference time — you don't need a world model in the inference pipeline if you've baked the world's structure into the training data. The tradeoff is that the model is frozen at training-data-time: it can't handle world-state changes that weren't represented in the DAG. For games with finite, well-defined state spaces, this is acceptable; for open-world games with unbounded state, it is not.
