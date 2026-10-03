---
type: article
title: AI Orchestration Papers 2025–2026 — Curated Research Set
url: 
author: curated
published: 
ingested: 2026-04-19
tags: [ai, ml, llm, tool]
concepts: [multi-agent-orchestration, agent-memory]
---

## Summary

A curated breakdown of the most novel AI agent orchestration papers from 2025–2026, organized by theme (decentralized coordination, memory systems, emergent behavior) with patent-worthiness assessments. The standout finding is that emergent collective memory shows a phase transition: individual agent memory alone yields 68.7% performance improvement over no-memory baselines, but stigmergic (environmental trace) coordination dominates by 36–41% once agent density crosses ~ρ=0.20.

## Key Points

### Decentralized Coordination
- **AgentNet** (`arXiv:2504.00587`): removes central orchestrator entirely; agents self-organize via peer-to-peer task delegation and adaptive specialization. Privacy-preserving cross-org design. Patent-worthy routing engine.
- **MAS Orchestration** (`arXiv:2601.13671`): formalizes unified framework integrating Model Context Protocol (MCP) and Agent2Agent (A2A) protocol for enterprise deployments.
- **ODI** (`arXiv:2503.13754`): multi-loop feedback + *cognitive density* framework for human-AI hybrid decision networks.

### Memory Systems
- **Emergent Collective Memory** (`arXiv:2512.10166`): individual memory = +68.7% over no-memory baseline; stigmergic coordination dominates above agent density ρ≈0.20 by 36–41%. Phase-transition-based memory model is strongly patent-worthy.
- **DAMCS**: knowledge-graph memory for LLM agents in open-world multi-agent scenarios; better scalability than MARL via external language-based knowledge.

### Emergent Behavior & Self-Organization
- **AgentRxiv** (`arXiv:2503.18102`): autonomous agent labs share research via preprint repository; +13.7% on MATH-500 vs. isolated agents. Genuine spontaneous collective intelligence.
- **AdaptOrch** (Feb 2026): dynamic model-selection orchestration for post-convergence LLM landscape; routes tasks to best model rather than relying on a single provider.
- **MA-Gym** (`arXiv:2510.02557`): workflow orchestration as Partially Observable Stochastic Game (POSG); GPT-5 Manager Agents across 20 workflows. Exposed that LLMs still struggle to jointly optimize goal completion, constraints, and runtime.

## Notable Points

- The phase-transition memory model in `arXiv:2512.10166` is the most specific and quantifiable novel mechanism — maps cleanly onto patentable claims.
- The shift from "which model is best" to "adaptive routing across equivalent models" (AdaptOrch) reflects the post-benchmark-saturation era.
- AgentRxiv's emergent discovery loop (agents build on each other's findings) is a working prototype of collective AI science.

## My Take

The stigmergic memory phase transition is the most interesting result — it suggests multi-agent systems have something like a critical mass, below which coordination is best done at the individual level and above which environmental signaling takes over. This is a structural property, not just a performance finding.
