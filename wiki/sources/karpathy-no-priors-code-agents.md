---
type: video
title: "Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI"
url: 
channel: No Priors
published: 
ingested: 2026-04-30
duration: 
tags: [ai, llm, tool, philosophy]
concepts: [vibe-coding, ai-agents, auto-research, agentic-workflow, open-source-ai, speciation-of-models]
---

## Summary

Andrej Karpathy joins the No Priors podcast to talk about the dramatic shift that happened around December 2024, when he stopped writing code himself and started delegating almost entirely to AI agents. He describes the resulting "AI psychosis" — a feeling that capability is now nearly unlimited and every failure is a skill issue. He covers his Dobby home automation claw, the concept of auto research (closed-loop autonomous ML experimentation), the distributed untrusted-compute model for open internet research, his MicroGPT project, and how education is being restructured around explaining things to agents rather than people.

## Timestamps
- 00:00 — Introduction; the December 2024 capability jump
- — Multi-agent parallelism and token throughput as the new bottleneck
- — Dobby: home automation via natural-language claw controlling lights, HVAC, Sonos, security
- — The agentic web: apps should be APIs; agents are the intelligence glue
- — Auto research: closed-loop autonomous hyperparameter search; found improvements Karpathy missed
- — Program.md: the idea that a research org is just a set of markdown files that can be optimized
- — Auto research at home: distributed untrusted compute for collaborative ML improvement (blockchain-like)
- — Job market analysis; digital vs physical world acceleration
- — Staying outside frontier labs vs joining them; tradeoffs of alignment and independence
- — Open source vs closed frontier; current ~6–8 month lag is a healthy dynamic
- — Robotics: physical world will lag digital; interface between digital and physical is the next frontier
- — MicroGPT: 200-line distillation of LLM training; education now targets agents not humans
- — Jokes and jaggedness: why models excel at verifiable tasks but stagnate elsewhere

## Key Ideas

- **December 2024 was the inflection point** — Karpathy went from 80/20 (human/agent) to nearly 0/100 in code writing. Token throughput replaced GPU flops as the resource constraint.
- **Everything is skill issue** — When agents fail, the framing is that the prompt, memory tool, or instructions weren't good enough — not that capability is missing.
- **Dobby pattern** — One WhatsApp-accessible agent controlling all smart home systems. Natural language replaces six separate apps. Argues apps shouldn't exist; just APIs + agents.
- **Auto research** — Give an LLM an objective metric, a sandbox, and a loop. Let it run overnight. It found weight decay and Adam beta tunings Karpathy had missed after two decades of manual tuning.
- **Program.md as research org** — A research organization can be described as a set of markdown files; those files can be optimized; the meta-optimization layer is the next frontier.
- **Distributed auto research** — Untrusted compute on the internet can contribute to model improvement if verification is cheap (train and measure). Similar to SETI@home / folding@home. Blockchain-like structure with commits as blocks.
- **Jaggedness of models** — Models are simultaneously like a PhD systems programmer and a 10-year-old. They're superhuman inside RL-verifiable domains and stuck in 2020 outside them (e.g., always the same joke).
- **Speciation vs monoculture** — Labs are currently building monoculture models. Karpathy expects speciation over time, but the science of fine-tuning without capability loss isn't mature yet.
- **Digital before physical** — Bits move at the speed of light; atoms don't. Digital world will be massively transformed first. Physical robotics will lag. The interesting interface is sensors/actuators bridging the two.
- **MicroGPT** — 200 lines of Python capturing the full LLM training algorithm (architecture + autograd + optimizer + training loop). Not explainable in a video anymore — the right medium is a skill for an agent to teach it.
- **Education shift** — We're moving from explaining things to humans to writing curricula for agents to explain. The teacher's job is to encode the few non-obvious bits; the agent handles delivery.

## My Take

This is one of the most practically grounded takes on where we actually are in the agentic transition. The "psychosis" framing is honest — it captures the disorientation of operating in a space where the ceiling keeps rising faster than you can find it. The auto research concept is directly relevant to anyone building AI products: the right question isn't "how do I prompt better?" but "how do I remove myself from the loop entirely?" The Dobby home automation example is a simple, concrete proof of concept for the agent-as-OS model. The speciation argument is underdeveloped — he acknowledges the science isn't there yet — but it's worth tracking.
