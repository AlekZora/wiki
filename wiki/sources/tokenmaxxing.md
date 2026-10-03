---
title: Token Maxing and the New Era of Agentic Software Development
type: video
status: processed
source_path: raw/videos/tokenmaxxing.md
created: 2026-05-12
tags:
  - agentic-engineering
  - software-development
  - llms
  - prompt-engineering
  - productivity
concepts:
  - token-maxing
  - metaprompting
  - harness-engineering
  - agentic-coding
  - multi-agent-orchestration
  - agent-skills
  - software-factory
---

# Summary

Gary Tan, CEO of Y Combinator, details his return to hands-on software development after a 13-year hiatus, catalyzed by modern AI-powered coding tools. He claims a 400x increase in productivity, measured in logical lines of code, by shifting his role from a programmer to a director of AI agents. The conversation chronicles his journey, which began with a personal project: building "Gary's List," a political advocacy website for California issues like public school education. This practical need forced him to master a new paradigm of AI-assisted development.

The core philosophy Tan espouses is "token maxing": the aggressive use of LLM compute to achieve a level of completeness and quality that a human, constrained by time and effort, would not. Instead of settling for a single source, an agent can "boil the ocean" by ingesting and cross-referencing dozens of sources to write a journalistic article. Similarly, instead of writing minimal tests, an agent can be directed to generate 80-90% test coverage automatically. This treats token spend not as a cost to be minimized, but as a crucial investment for superior output, analogous to paying high rent in a tech hub for serendipity and network effects.

Tan's workflow is built on a principle he calls "thin harness, fat skills." The "harness" is the minimal, reusable code that runs the agent's core loop (e.g., OpenDevin, which he calls OpenClaw). The "skills" are the "fat" prompts—written in natural language or Markdown—that contain all the domain knowledge, process steps, and strategic direction. This architecture separates deterministic code from the flexible, context-aware logic best handled by LLMs. He demonstrates this with "GStack," a suite of prompts that simulate a development team with roles like CEO and CTO, using techniques like metaprompting (e.g., refining a feature plan by asking the LLM to act like Brian Chesky designing a "10-star experience").

Throughout, Tan emphasizes that the human remains essential for providing agency, taste, and high-level direction. The goal is not full automation but extreme augmentation. He compares the current state of agentic tools to a powerful but temperamental Ferrari: exhilaratingly fast, but it breaks down often, requiring the driver to also be a mechanic. This marks the "Homebrew Computer Club" era of a new personal AI revolution, where users face a choice between owning and controlling their tools or being subject to corporate-controlled platforms.

# Key Claims

*   Modern AI tools enable a 100x to 400x productivity increase for software developers.
*   "Token maxing"—aggressively spending on API calls to achieve comprehensive results—is the key to unlocking the full potential of AI in knowledge work.
*   The optimal architecture for agentic systems is a "thin harness" (minimal, reusable agent code) and "fat skills" (rich, domain-specific prompts in natural language).
*   The developer's role is shifting from writing code line-by-line to directing and orchestrating AI agents as a CEO or product manager.
*   Markdown and other natural language instructions are effectively a new form of code for LLMs.
*   Human agency, taste, and product vision are irreplaceable; the goal is to augment the human, not replace them.
*   We are at the start of a "personal AI" revolution analogous to the personal computer revolution, forcing a choice between sovereign and corporate-controlled tools.
*   Different LLMs have distinct capabilities and "personalities" (e.g., a creative "CEO" model vs. a logical "CTO" model) and should be used as a team.
*   The current state of agentic tooling is like an early-era Ferrari: incredibly powerful but brittle, requiring the user to be a hands-on "mechanic."

# Mechanisms

*   **Agentic Workflow Orchestration:** A human operator acts as a director, queuing up high-level tasks. An AI agent (e.g., inside a tool called "Conductor") executes these tasks by following a multi-step plan, invoking specialized prompts ("skills") for different phases like product strategy, design, implementation, and QA.
*   **Metaprompting:** Using an LLM to generate or refine a prompt for another task. For instance, feeding a basic feature plan into a "CEO skill" prompt that asks the model to reimagine it as a "10-star experience," thereby generating a more ambitious and detailed implementation plan.
*   **Automated RAG for Journalism:** The system behind "Gary's List" automates investigative journalism. It performs deep, recursive web crawls on a topic, ingests dozens of articles and social media posts, cross-references claims, identifies conflicting viewpoints, and synthesizes the findings into a fully-sourced long-form article.
*   **Automated QA via Browser Control:** An agent is prompted to use a browser automation framework (like Microsoft Playwright) to perform end-to-end testing. The agent analyzes the code changes on the current git branch to understand the new feature and then writes and executes tests to validate its functionality in a live browser environment.
*   **Multi-Agent Collaboration:** A primary, generalist agent (e.g., based on a Claude model) handles the main workflow. When it encounters a particularly difficult logical problem or needs a rigorous code review, it can invoke a specialized, more powerful agent (e.g., based on a "Codex" model), passing it the relevant context and receiving feedback to incorporate.

# Useful Examples

*   **Rebuilding Posterous:** Tan's first startup, Posterous, initially took a team 1.5 years and $4M to build. A later version took two people 3 months and $100k. Using modern agentic tools, he built a full-featured equivalent for his "Gary's List" project in five days for about $200 in API costs.
*   **The "CEO Skill" Prompt:** Inspired by Brian Chesky's "10-star experience" concept, this prompt asks the AI to think beyond the immediate request and envision a 10x more ambitious version of the feature for only 2x the effort, forcing the model to generate more creative and valuable solutions.
*   **ASCII Art Diagrams as Pre-computation:** Before writing code, Tan forces the agent to generate ASCII art diagrams of data flows, state machines, and dependency graphs. This acts as a form of "chain of thought," forcing the model to load the full context and plan its implementation, which results in more robust and less buggy code.
*   **Claude as "ADHD CEO" vs. Codex as "non-verbal CTO":** This analogy explains his multi-agent strategy. He uses a Claude-based agent for creative brainstorming and rapid, iterative work. For complex, logically demanding tasks, he "calls in" a more powerful model to act as a focused, deep-thinking specialist.
*   **Automating Tedious Work:** Tan highlights his dislike for writing tests. By directing an agent to achieve 80-90% test coverage or to run QA using Playwright, he automates the parts of the job he finds tedious, freeing him up for high-level strategic work.

# Possible Relevance

*   **AI agent design:** The "thin harness, fat skills" principle is a powerful architectural pattern for building flexible and maintainable agentic systems. The multi-agent "CEO/CTO" collaboration model provides a practical template for hierarchical agent teams.
*   **Narrative systems:** The agentic journalism process used for "Gary's List" is a direct blueprint for a dynamic narrative or lore generation system. It could ingest a corpus of worldbuilding documents, character sheets, and event logs to generate in-world news articles, histories, or character backstories that reflect the current game state.
*   **Game mechanics:** "Token maxing" could be a core resource management mechanic. A player could be given a "compute" budget, forcing strategic trade-offs between cheap, fast, "good enough" actions and expensive, comprehensive, "perfect" actions performed by their AI-controlled units or advisors.
*   **Knowledge management:** Tan's work on "GBrain," inspired by Andrej Karpathy's "LLM wikis," points to a future where a personal knowledge base (e.g., a folder of Markdown files) serves as the persistent memory for a personal AI assistant. This agent could then reason over and act upon the user's private knowledge.

# Links

*   **People:** Gary Tan, Jake Heler, Brett Gibson, Brian Chesky, Andrej Karpathy, Pete Kumin, Steve Jobs, Steve Wozniak, Boris Cherny.
*   **Companies/Projects:** Y Combinator (YC), Posterous, Casetext, Perplexity, X (Twitter), Microsoft, Apple, Twilio, Stack Overflow, OpenClaw (likely a reference to OpenDevin).
*   **Concepts:** "Token Maxing", "Thin Harness, Fat Skills", RAG (Retrieval-Augmented Generation), Metaprompting, "10-star experience", Homebrew Computer Club.
*   **Tools:** Claude Code, Conductor (the UI for Claude Code), Grok, Playwright, PostgreSQL, PGVector.