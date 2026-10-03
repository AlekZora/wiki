---
type: concept
title: Agent Skills
aliases: [skill injection, agent knowledge modules, progressive disclosure, skill externalization, capability packages]
tags: [ai, agents, memory, tool, llm, architecture]
sources:
  - ../sources/ai-agents-supabase.md
  - ../sources/externalization-llm-agents-zhou-2026.md
  - ../sources/tokenmaxxing.md
  - ../sources/garry-tan-claude-.md
updated: 2026-05-12
---

## Definition

Agent skills are modular, structured knowledge artifacts that package procedural expertise into reusable, discoverable, composable units that an agent can load at runtime. A skill externalizes not raw actions but *repeatable task know-how* — the combination of operational procedures (what steps to follow), decision heuristics (how to handle branches and tradeoffs), and normative constraints (what boundaries must not be crossed). In practical implementations, a skill is often a folder containing a `skill.md` file with YAML frontmatter, optional reference files, and executable scripts.

## How I Think About It

**The core representational shift** (from Zhou et al. 2026): skills convert the agent's task from *improvised generation* to *composition from pre-validated components*. Without skills, the model must probabilistically reconstruct the right workflow from its parameters every time — producing variance: omitted steps, misordered operations, inconsistent stopping conditions. With skills, the model recognizes which procedure applies and follows it, trading generative freedom for execution stability.

**Three components of a skill** (what makes it more than a document):
1. **Operational procedure** — the task skeleton: steps, phases, dependencies, stopping conditions. Turns fragile process knowledge into an explicit operating path.
2. **Decision heuristics** — rules of thumb at branch points: what to try first, when to back off, what evidence is sufficient, which tradeoffs to prefer. Reduces deliberation cost and makes behavior more stable under uncertainty.
3. **Normative constraints** — the conditions under which a procedure counts as acceptable: scope limits, access restrictions, testing requirements, safety rules. Skills are carriers of governance as much as carriers of capability.

**Four acquisition pathways**:
- *Authored* — human-designed SKILL.md, AGENTS.md, or SOP files. Most common. Operational experience is gradually turned into reusable behavioral structure.
- *Distilled* — induced from episodic memory traces. When successful patterns recur in trajectories, the harness abstracts them into stable procedural units.
- *Discovered* — autonomously generated through environmental interaction (e.g., Voyager's Minecraft skill library). The agent builds its own capability repertoire.
- *Composed* — higher-order skills assembled from existing lower-level ones. Composition is both an execution strategy and an acquisition mechanism.

**Progressive disclosure** is the key deployment mechanism: the agent initially sees only the skill's name and a brief description (the "envelope"), loads deeper detail only when needed. This prevents context saturation while making deep guidance available on demand. Claude Code's skill system is cited as a reference implementation of this pattern.

**The distinction from MCP tools**: **tools give the agent actions**, **skills give the agent workflows**. Tools expose operations; protocols govern how those operations are described and invoked; skills encode how a *class of tasks* should be carried out with them. You use a tool to query a database; you use a skill to know *how* to write safe queries for that database.

**Boundary conditions — where skills fail**:
- *Semantic alignment*: a model may follow the literal wording of a skill while missing the real objective. Description and invocation intent must stay aligned.
- *Portability and staleness*: changes in APIs, environments, or workflows can make a once-effective skill partially misleading or obsolete.
- *Unsafe composition*: skills that appear harmless in isolation can interact unsafely when combined — prompt injection, privilege escalation, and supply-chain risks are documented in public skill ecosystems.
- *Context-dependent degradation*: detailed skill guides can interfere with global task tracking when too much procedural detail saturates the context.

The phrasing of a skill's description matters — using action verbs ("use this skill when...") significantly increases the agent's likelihood of loading it.

**GStack as a skill library in practice** (Tan 2026): GStack implements skills as role-specialized prompts — `Office Hours` (Socratic product strategy), `Design Shotgun` (generative UI brainstorming), `Adversarial Review` (red-teaming plans), and automated QA (Playwright browser control). Each skill encodes a distinct phase of the development lifecycle. The "CEO skill" is a metaprompting skill: it takes a basic plan and asks the model to reimagine it as a "10-star experience," producing a more ambitious input for downstream skills. This demonstrates skills as carriers of strategic ambition, not just procedural steps.

## Related Concepts

- [Cognitive Externalization](cognitive-externalization.md) — skills as the procedural dimension of externalization
- [Harness Engineering](harness-engineering.md) — the runtime that discovers, loads, governs, and evolves skills
- [Agent Memory](agent-memory.md) — memory preserves experience; skills extract reusable structure from it
- [Multi-Agent Orchestration](multi-agent-orchestration.md) — protocols bind skills to executable action substrates
- [Agentic Workflow](agentic-workflow.md)
- [Eval-Driven Development](eval-driven-development.md)
- [Context Development Lifecycle](context-development-lifecycle.md)

## Open Questions

- How do skills interact with long-context models that can hold more in context — do skills become less necessary?
- Can a skill itself be dynamically generated or personalized per user?
- What's the optimal granularity for a skill — one concept per skill, or a workflow-level bundle?

## Project Connection

Skills are directly applicable to the paranoid sci-fi series project. Each AI character agent could have a set of skills representing their hidden domain expertise — the things they "know" that others don't. A character's skill set is a mechanical expression of their information asymmetry. A security officer's skills would differ from a scientist's, creating naturally divergent behavior even when given the same prompt.
