---
type: video
title: "Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI"
url: 
channel: No Priors
published: 2026-04
ingested: 2026-04-09
duration: 
tags: [ai, llm, autonomous-agents, ml, tool, philosophy]
concepts:
  - ../concepts/agentic-coding.md
  - ../concepts/auto-research.md
  - ../concepts/llm-jaggedness.md
---

## Summary

Wide-ranging conversation between Andrej Karpathy and the No Priors podcast. Karpathy describes living in a state of "AI psychosis" since around December, when he stopped writing code himself and shifted to directing agents for 16 hours a day — "manifest" rather than "code." The episode covers parallelizing multiple agents (inspired by Peter Steinberg's setup), persistent background agents he calls "claws," his Dobby home-automation elf, auto research (autonomous ML experiment loops that found tuning improvements he'd missed after years of work), the jagged capability profile of LLMs, the digital-vs-physical acceleration gap, open source vs frontier dynamics, and micro-GPT as an example of education shifting from human-to-human to human-to-agent.

## Timestamps

- 00:00 — Karpathy on "manifesting" rather than coding; the December capability jump
- ~05:00 — Token throughput as the new GPU utilization; Peter Steinberg's multi-agent setup
- ~15:00 — What are "claws"? Persistent background agents vs interactive sessions
- ~20:00 — Dobby the home elf claw: controlling Sonos, lights, HVAC, pool, security camera via WhatsApp
- ~35:00 — Auto research: removing yourself as bottleneck from ML experiments
- ~45:00 — Open-source auto research / distributed untrusted workers (like folding@home)
- ~55:00 — LLM jaggedness: why models still tell 5-year-old jokes
- ~70:00 — Open source vs frontier; Karpathy's view on centralization risk
- ~80:00 — Digital vs physical world acceleration; robotics will lag
- ~95:00 — Micro-GPT and the shift to explaining things to agents, not humans

## Key Ideas

- Since December, Karpathy hasn't typed a line of code himself — ratio flipped from 80/20 (human/agent) to effectively 0/100. The bottleneck is now him, not compute.
- "Token throughput" is the new GPU utilization — you feel nervous when your Claude/Codex subscription has headroom left, just like idle GPUs during PhD.
- Peter Steinberg's setup: 10 repos checked out simultaneously, multiple Codex agents each taking ~20-min tasks in parallel. Karpathy wants to replicate this pattern.
- "Claws" = persistent background agents that loop independently, have more sophisticated memory, and act on your behalf without you being in the session. Open Claw is the main example he's excited about.
- Dobby the elf claw: built in a week of claw psychosis. Agents found Sonos, reverse-engineered its API via IP scan, built a dashboard, and now control all smart home subsystems — lights, HVAC, shades, pool, spa, security camera — via WhatsApp in natural language. Six apps replaced by one agent.
- The "app store model" is the wrong layer — everything should be APIs + agents as glue. The customer is no longer the human but agents acting on behalf of humans.
- Auto research: arrange it once, hit go, remove yourself from the loop entirely. An overnight run on nanochat found weight decay settings on value embeddings Karpathy had missed, plus under-tuned Adam betas that interact — things that jointly required rediscovery.
- Program.md = natural-language description of how the research org should operate. Different program.mds yield different rates of improvement. You can meta-optimize the program.md itself.
- Distributed/untrusted auto research: cheap to verify a candidate commit (just train and check val loss), very expensive to find it. Structurally similar to folding@home or a blockchain — proof-of-work is experimentation, the reward is leaderboard position. Earth's untrusted compute could potentially rival frontier labs.
- LLM jaggedness: the same model that codes for hours, moves mountains, and builds home automation still gives the exact same "atoms make everything up" joke from 5 years ago — because RL only improves verifiable things. Soft/creative domains stay frozen.
- Open source is ~6-8 months behind frontier and converging. Karpathy prefers this dynamic to full centralization — "ensembles always outperform any individual model" applies to research orgs too.
- Digital space will change at "speed of light" first (bits are easier than atoms). Robotics and physical world will lag but are a larger total addressable market. The interesting interface: sensors and actuators connecting agent intelligence to the physical world.
- Micro-GPT: 200 lines of Python capturing the full essence of LLM training. He no longer writes explanatory videos — agents can explain it to any human in their own terms. His value-add is the few design bits; everything downstream is the agent's job now.
- Education shift: you write curriculum hints (skills/program.md) for agents, not explanations for humans. Agents route and translate to the individual learner.

## My Take

The "token throughput" framing is genuinely clarifying — it reframes the new bottleneck correctly. The Dobby story is the best concrete demo of what claws actually feel like in practice: not a chat session, but an ambient intelligent layer that manages your environment. The auto research finding (missed hyperparameter interactions after years of tuning) is the strongest empirical argument for removing humans from loops wherever evaluation is objective. The jaggedness observation feels important and underappreciated — RL being the organizing principle of frontier improvement means whole swaths of capability are systematically frozen. The distributed untrusted compute idea is speculative but structurally sound.
