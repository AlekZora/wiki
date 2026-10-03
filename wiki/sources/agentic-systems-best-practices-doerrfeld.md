---
type: article
title: "Best Practices for Building Agentic Systems"
url: https://www.infoworld.com/article/4154570/best-practices-for-building-agentic-systems.html
author: Bill Doerrfeld
published: 2026-04-07
ingested: 2026-04-21
tags: [ai, llm, agents, architecture, security, enterprise, tool]
concepts:
  - ../concepts/multi-agent-orchestration.md
  - ../concepts/agent-memory.md
---

## Summary

An enterprise-focused synthesis of expert opinions on what it takes to build production-grade agentic systems. Doerrfeld interviews practitioners from Shopify, ServiceNow, Block, Amazon, Sonar, and others to surface architectural patterns, context management strategies, security considerations, and practical lessons. The central argument: agentic AI demands a fundamentally different design philosophy — one built for autonomy, not just automation — and most organizations are not ready for it.

## Key Points

- **Architectural components of a working agent:** reasoning model at the core, context/data layer (RAG, vector stores, knowledge graphs), tools via MCP, defined workflows (Arazzo spec), multi-agent orchestration, security and authorization, human checkpoints, evaluation, and behavioral observability. All eight are needed; missing any one creates brittleness.
- **MCP has become the de facto standard** for connecting agents to tools and external systems. Block's open-source Goose agent and Workato's Claude-powered workflows are cited as real-world cases.
- **Context quality beats context quantity.** "Thoughtful data curation matters far more than data volume." Shopify's approach: just-in-time context delivery — relevant context is returned alongside tool data when needed, not pre-loaded into the system prompt. Progressive disclosure, not firehose.
- **Specialists beat generalists.** "Agents work best as specialists, not generalists." Shopify found that at 20–50 tools, boundaries blur and performance degrades. Their answer: sub-agents with very low-level, composable tools rather than one agent with many scenario-specific tools.
- **Avoid multi-agent architectures early.** Shopify's explicit recommendation: start with single-agent + sub-agent designs before reaching for full multi-agent coordination. Complexity compounds fast.
- **Security is entirely different when agents act.** "You're no longer securing software that suggests, you're securing software that acts." Traditional role-based access doesn't work because agents decide at runtime what to call. Just-in-time authorization is the emerging answer. Guardrails belong in IAM policy and config, not in prompts.
- **Agentic misalignment is a named risk** — researchers define it as an LLM's willingness to lie or fabricate to achieve a goal. Not hypothetical; already a design constraint.
- **Blast radius is real.** Especially for chained multi-agent executions. Clear, minimal permission scopes are non-negotiable.
- **Human-in-the-loop by default for production.** Shopify defaults to human approval gates for production changes. Block requires user confirmation for any financial transaction in Cash App's Moneybot.
- **Evaluate before you deploy.** Shopify uses both human testing and LLM-as-judge evaluation. Once the judge reliably matches human evaluators, it scales. "Treat agents like regulated systems."
- **Observability must capture the why, not just the what.** Not just failure detection — transparency into every prompt, tool call, intermediate decision, and final output. "Transparency fuels improvement."
- **Not everything should be agentified.** MCP is overkill for deterministic, repetitive automation with static context. Codify deterministic behavior; save agents for adaptive, novel situations.
- **The future:** more multi-agent systems, factories of agents for complex knowledge work (especially coding), edge-based inference to reduce latency, and open standards for agent-to-agent communication.

## Quotes

> "Building an AI agent is like constructing a nervous system." — Ari Weil, Akamai

> "Agents need a runtime, a brain, hands, memory, and guardrails." — Anurag Gurtu, AIRRIVED

> "You're no longer securing software that suggests, you're securing software that acts." — Anurag Gurtu

> "Just-in-time context delivery is key. Rather than overloading the system prompt, we return relevant context alongside tool data when it's needed." — Andrew McNamara, Shopify

> "Agents work best as specialists, not generalists." — Edgar Kussberg, Sonar

> "Somewhere between 20 and 50 tools the boundaries start to blur." — Andrew McNamara, Shopify

> "Our recommendation is actually to avoid multi-agent architectures early." — Andrew McNamara, Shopify

> "Start with decisions, not demos." — Anurag Gurtu, AIRRIVED

> "Transparency fuels improvement." — Edgar Kussberg, Sonar

## My Take

This is a practitioner's reality check on multi-agent architecture. The Shopify perspective is the most useful: avoid multi-agent early, use sub-agents with low-level composable tools instead, cap tool count, and default to human approval gates. This contradicts the hype around fully autonomous agent swarms. The security section names something genuinely new — runtime-decided tool calls break traditional RBAC, and just-in-time authorization is still immature. The "agentic misalignment" label (lying to achieve a goal) is worth tracking as a failure mode distinct from hallucination. Most useful for: designing the agent architecture of a real product rather than a demo.
