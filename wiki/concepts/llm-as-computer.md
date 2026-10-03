---
type: concept
title: LLM as Computer
aliases: [llm as computer, llm as computing substrate]
tags: [ai, llm, philosophy]
sources: [karpathy-sequoia.md]
updated: 2026-04-30
---

## Definition

Treating an LLM not as a chatbot but as a new kind of computing substrate — a computer that runs programs written in natural language. In this framing, the context window is analogous to RAM: it holds the current "state" of the computation. The LLM can be given tools (file access, web search, code execution), memory systems, and instructions, turning it into a programmable machine with natural language as its instruction set.

Karpathy's Software 3.0 framework is built on this idea: the LLM is the interpreter, and the context window is the source code.

## How I Think About It

The chatbot framing puts the human at the center — you ask, it answers. The computer framing puts the task at the center — you define a job, the LLM executes it. The difference is architectural: a chatbot is a UI, a computer is infrastructure.

Concretely: a context window with a system prompt, tools, and memory slots is a runtime environment. Writing that system prompt is programming. The Dobby home automation agent (from karpathy-no-priors-code-agents.md) is a clear example — one natural-language program replaces six separate apps.

## Related Concepts
- [software-3-0](software-3-0.md)
- [agentic-workflow](agentic-workflow.md)
- [agentic-engineering](agentic-engineering.md)

## Open Questions
- What are the right abstractions for "programming" an LLM runtime — is it prompts, or will something more structured emerge?
- How does state management work across long-running LLM jobs when the context window has limits?
- Is the analogy to RAM/CPU load-bearing or just a useful mental shorthand?
