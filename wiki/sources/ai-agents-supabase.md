---
title: Leveling Up AI Agent Skills with Supabase and Evals
type: video
status: processed
source_path: raw/videos/ai-agents-supabase.md
created: 2026-05-05
tags: ai-agents, agent-skills, supabase, postgresql, agent-evaluation, progressive-disclosure, mcp, software-engineering, testing, database-security
concepts: [agent-skills, eval-driven-development]
---

# Summary

This workshop, presented by Pedro, an AI tooling engineer at Supabase, demonstrates a practical methodology for improving AI agent performance using "skills." The core argument is that for agents to reliably perform complex, domain-specific tasks, they need more than general knowledge; they require curated, contextual information provided through a structured "skill" system. The workshop focuses on how to write, test, and evaluate these skills, framing the process as a form of "eval-driven development."

The presentation begins by defining skills as modular folders containing instructions (`skill.md`), reference files, and executable scripts. The key mechanism enabling their efficiency is "progressive disclosure." An agent initially only sees a skill's name and description from its markdown front matter, a low-token "envelope" that saves precious context space. If relevant, the agent can then choose to load the skill's full content, which can be analogized to a book's index on steroids. The speaker clarifies the relationship between skills and MCP (Model-Component Protocol) tools, arguing they are complementary: MCP tools provide the agent with actions and integrations, while skills provide the deep context and workflows on how and when to use those tools effectively.

The central part of the workshop introduces a systematic cycle for skill development, adapted from an OpenAI framework: 1) Define Metrics, 2) Create the Skill, 3) Test with Evaluations, and 4) Grade & Iterate. This process is demonstrated with a concrete example: building a performance review application on Supabase. An agent is tasked with creating a new SQL view for department statistics. Without a skill, the agent creates a functionally correct view that, due to a subtle PostgreSQL feature, inadvertently bypasses Row-Level Security (RLS) policies, creating a major data leak.

The solution is to create a `supabase-security` skill that contains specific knowledge about PostgreSQL, including the necessity of using the `SECURITY INVOKER` flag to enforce RLS on views. When the agent is run again with this skill available, it correctly produces a secure SQL view. This powerfully illustrates how skills inject critical domain knowledge to prevent subtle, high-impact errors. The workshop concludes by showing how this manual testing process can be automated. A simple Python evaluation harness is presented, which runs the agent against the same scenario under two conditions—with and without the skill—and then programmatically asserts that the correct, secure output was generated when the skill was used. This provides a blueprint for creating a CI/CD-like pipeline for reliably developing and maintaining agent capabilities.

# Key Claims

- AI agent "skills" are a primary mechanism for improving agent performance and reliability on complex, domain-specific tasks.
- "Progressive disclosure" is the core principle of skills, allowing agents to manage context efficiently by loading only high-level metadata initially.
- Skills and MCP (Model-Component Protocol) tools are complementary, not competitive; skills provide detailed context and workflows for how to use tools.
- A systematic, "eval-driven" development cycle (Define Metrics, Create Skill, Test, Grade, Iterate) is essential for building and maintaining robust agent skills.
- Without domain-specific knowledge provided by skills, agents can produce functionally correct but contextually flawed or insecure solutions.
- Automated evaluation pipelines are crucial for regression testing and ensuring that changes to a skill do not break existing agent functionality.
- The structure of a skill, as a human-readable markdown file with references, makes complex knowledge modular, accessible, and maintainable.
- The phrasing of a skill's description (e.g., using action verbs like "use") can significantly influence an agent's likelihood of loading and using it.
- Scripts within skills are tied to the local execution environment, whereas MCP tools can run remotely, making MCP better for service integrations.

# Mechanisms

- **Progressive Disclosure:** An agent first sees only the `name` and `description` from a `skill.md` file's YAML front matter. This acts as a low-token "envelope." Based on this summary, the agent decides whether to load the file's full markdown content into its context, which contains detailed instructions and can reference other files. This prevents context window overflow with irrelevant information.
- **Skill Structure:** Skills are organized as folders centered around a `skill.md` file. This file can reference other markdown files or scripts (e.g., Python, bash), creating a modular and interconnected graph of knowledge that the agent can traverse.
- **Eval-Driven Development Cycle:** An iterative four-step process for skill creation: 1) Define success metrics for the skill. 2) Write the `skill.md` and associated files. 3) Run the agent against predefined test scenarios ("evals"). 4) Grade the agent's performance (by checking outputs or using an LLM-as-a-judge) and refine the skill based on the results.
- **Automated Evaluation Harness:** A script that programmatically executes an agent in a controlled environment. It feeds the agent a prompt from a test case, runs it under different conditions (e.g., with and without a skill), captures the output, and runs deterministic assertions to verify the agent's behavior changed as expected.
- **PostgreSQL Security Invoker:** A specific database mechanism at the heart of the demo. When a view is created on a table with Row-Level Security (RLS), it defaults to using the creator's permissions. The `WITH (security_invoker = true)` flag forces the view to execute with the permissions of the user *querying* it, thereby correctly enforcing RLS. The skill's purpose is to teach the agent this non-obvious requirement.

# Useful Examples

- **Performance Review App:** A demo Next.js application built on Supabase that manages employee data, including sensitive information like salaries, serving as the testbed for the agent task.
- **Insecure SQL View:** The agent's initial attempt to create a department statistics view. The generated SQL is syntactically correct but lacks the `SECURITY INVOKER` flag, leading to a security flaw where all users can see all salary data.
- **Supabase Security Skill:** The `skill.md` file created to solve the problem. It contains a checklist of Supabase and PostgreSQL security best practices, explicitly stating the need to use `SECURITY INVOKER` for views on RLS-enabled tables.
- **Secure SQL View:** The agent's second attempt, this time with the security skill loaded. The agent's output now correctly includes the `WITH (security_invoker = true)` clause, fixing the vulnerability.
- **`eval.json` File:** A file defining an automated test case. It contains the `prompt` to give the agent, the `expected_output` for an LLM-as-a-judge, and an array of deterministic `assertions` to check, such as whether the generated SQL contains the string "security_invoker".
- **Vercel's `skills` npm package:** The speaker uses this CLI tool (`npx skills install ...`) to install the locally-developed skill into the Claude Code agent's environment, demonstrating a practical workflow.

# Possible Relevance

- **AI Agent Design:** The talk provides a concrete architectural pattern for injecting domain knowledge into agents. The concept of "progressive disclosure" is a critical technique for managing context in any complex agent system. The clear distinction between MCP tools (actions) and skills (knowledge/workflows) is a valuable separation of concerns.
- **Narrative Systems:** Skills can function as "lore books" or "codexes" for an AI-driven character. A skill's structure, with a high-level summary (`skill.md` front matter) linking to deeper content, mirrors how a character might recall a key fact and then elaborate. An NPC could have skills for "local customs," "faction history," or "technical schematics" to guide its behavior.
- **Game Mechanics:** The eval-driven development cycle is directly applicable to testing AI-driven NPCs. One could create "evals" for game scenarios (e.g., "player insults the bartender") to test if the NPC agent (with its "bartender etiquette" skill) behaves as intended. The security vulnerability example is a perfect analogue for an AI finding a clever but game-breaking exploit that a skill can "patch."
- **Knowledge Management:** The skill format serves as a template for modular, machine-readable knowledge artifacts. A personal knowledge wiki could be structured as a collection of skills, where each note's front matter is the "envelope" for progressive disclosure, allowing a personal agent to efficiently search and reason over the knowledge base.
- **Industrial/Ruhr Region Context:** The core problem—an automated system making a subtle but critical error due to a lack of deep domain expertise—is highly relevant to industrial automation. An agent controlling a factory process requires skills on safety protocols, material tolerances, and machine-specific quirks. This talk's methodology is a blueprint for building and verifying the reliability of such industrial agents.

# Links

- **People:** Pedro
- **Companies/Orgs:** Supabase, OpenAI, Anthropic, Brain Trust, Vercel, Google DeepMind
- **Concepts:** Skills, Progressive Disclosure, Eval-Driven Development, Evaluations (Evals), LLM as a Judge, Row-Level Security (RLS), `SECURITY INVOKER` (PostgreSQL), Developer Agent Experience (DAX), MCP (Model-Component Protocol)
- **Tools:** Supabase, PostgreSQL, Firebase, Claude Code, Cursor, Next.js, Vercel `skills` npm package, Brain Trust, Langfuse
- **External Sources:** OpenAI blog post "Systematically evaluate agent skills"