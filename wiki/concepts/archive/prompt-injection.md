---
type: concept
title: Prompt Injection
aliases: [indirect prompt injection, agent hijacking]
tags: [ai, ai-safety, agents, security]
sources: [nat-friedman-daniel-gross.md]
updated: 2026-05-05 (project connection expanded)
---

## Definition

Prompt injection is a class of security vulnerability in which malicious content embedded in an agent's environment — a webpage, email, document, or tool response — hijacks the agent's behavior by overriding or subverting its original instructions. Unlike traditional injection attacks (SQL, XSS), prompt injection targets the model's language understanding rather than a parser or interpreter. **Indirect** prompt injection occurs when the malicious instruction comes via a tool call result rather than the user's direct input.

## How I Think About It

This is the XSS of the agent era. As agents are given more tools and real-world reach — reading emails, browsing the web, controlling devices — the attack surface grows proportionally. An agent that can redirect your Tesla's navigation or purchase items online becomes a high-value target. The fact that Nat Friedman identified prompt injection as a real concern for his personal "claw" agent, which reads his email inbox, shows this isn't theoretical.

The fundamental issue is that language models cannot cleanly separate "data" from "instructions" the way a traditional computer separates code from data. Everything is tokens.

## Related Concepts

- [AI Safety](ai-safety.md)
- [Agent Skills](agent-skills.md)
- [Agentic Workflow](agentic-workflow.md)

## Open Questions

- Can prompt injection be fully solved at the model level, or does it require architectural sandboxing?
- What's the right trust model for agent tool call outputs — should they be treated as untrusted user input?
- Does signing/verifying tool call provenance help?

## Project Connection

**Story:** Prompt injection is a plot-ready mechanic. An AI character agent could be "compromised" via injected instructions hidden in the environment — a document they're asked to process, a message from another character, a sensor reading. This creates a narrative mechanism where an agent's behavior changes in ways neither the audience nor other characters can easily attribute to external manipulation vs. genuine motivation shift.

**Technical:** The simulation architecture is directly exposed to this risk. Character agents receive messages from other agents, process environmental events, and read shared documents — all of which are indirect prompt injection vectors. A malicious or malfunctioning agent could embed instructions in its outputs that hijack another agent's behavior, corrupting persistent memory or overriding hidden agenda state. Since the human creator controls the core mystery, the trust boundary must be explicit: agent-to-agent communication should be treated as untrusted input, not elevated instructions. This is a real design constraint to enforce when building the agent pipeline.
