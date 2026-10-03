# AI Orchestration Papers 2025 — Curated Research Set

A curated set of very recent, architecture-heavy papers and preprints aligned with LLM-based agent orchestration, decentralized coordination, gossip protocols, agent memory, and personal knowledge bases. Biased toward frameworks and protocols rather than benchmarks or surveys. Dates are within roughly the last 12 months where possible.

---

## Core orchestration and communication

### AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool World

- **Title/authors**: "AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool World" (authors not listed in snippet).
- **Date/source**: arXiv preprint, 2025-06-13, arXiv:2506.12508.
- **Summary**: Proposes a hierarchical multi-agent framework where a top-level conductor decomposes tasks into sub-goals and orchestrates specialized tool-using agents across web search, multimodal reasoning, and other domains.  The system emphasizes explicit sub-goal formulation, role specialization, and inter-agent communication policies.  Experiments on several real-world-style benchmarks show higher task success and adaptability than flat multi-agent or single-agent baselines.
- **Relevance**: Directly about LLM-based agent orchestration frameworks and task decomposition, giving a blueprint for hierarchical controller–worker stacks and orchestration policies you could adapt to industrial workflows or game quest orchestration.
- **Link**: https://arxiv.org/abs/2506.12508
- **Patent potential (flagged)**: The hierarchical orchestration scheme plus tool-world integration looks patentable when embedded in, e.g., enterprise automation or live-service game AIs.

---

### The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Standards

- **Title/authors**: "The Orchestration of Multi-Agent Systems: Architectures, Protocols, and Standards" (authors not in snippet).
- **Date/source**: arXiv (HTML version), 2026-ish (exact date not in snippet, but clearly recent). arXiv:2601.13671.
- **Summary**: Consolidates current practice into a unified architectural framework for orchestrated agentic systems, detailing control units, state/knowledge management, and communication layers.  It formalizes two key protocols: the Model Context Protocol (MCP) for standardized tool/context access and an Agent-to-Agent (A2A) protocol for negotiation, delegation, and peer collaboration.  The paper positions these as an interoperable substrate for scalable, auditable, policy-compliant coordination across distributed agent collectives.
- **Relevance**: Extremely relevant to multi-agent coordination and communication protocols; it reads almost like a reference design for production-ready orchestration backplanes and protocol stacks.
- **Link**: https://arxiv.org/html/2601.13671v1
- **Patent potential (flagged)**: While somewhat standardizing, specific protocol compositions and policy-compliant orchestration flows can be embedded in proprietary platforms (enterprise agent fabrics, regulated domains).

---

### Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence

- **Title/authors**: "Internet of Agents: Weaving a Web of Heterogeneous Agents for Collaborative Intelligence" (authors not in snippet).
- **Date/source**: arXiv preprint, 2024-07-10, arXiv:2407.07061.
- **Summary**: Introduces IoA, a framework that treats agents as internet-like nodes connected via an agent integration protocol and instant-messaging-style architecture.  It supports dynamic agent teaming, flexible conversation routing, and protocol-agnostic collaboration across heterogeneous tools and models.  Experiments on assistant tasks, embodied AI, and RAG show that this "internet-style" substrate improves collaboration and robustness compared with static pipelines.
- **Relevance**: Strongly aligned with agent orchestration frameworks and decentralized information propagation, giving a network-level metaphor you could apply for large-scale game worlds or cross-service orchestration.
- **Link**: http://arxiv.org/pdf/2407.07061.pdf
- **Patent potential (flagged)**: The "agent integration protocol + IM-like routing" pattern is industrially interesting for multi-vendor agent networks and could underpin game NPC ecosystems.

---

### A Scalable Communication Protocol for Networks of Large Language Models (Agora)

- **Title/authors**: "A Scalable Communication Protocol for Networks of Large Language Models" (Agora).
- **Date/source**: arXiv preprint, 2024-10-14.
- **Summary**: Defines Agora, a meta-protocol addressing the "Agent Communication Trilemma" of versatility, efficiency, and portability in large LLM agent networks.  Agents use standardized routines for common interactions, natural language for rare communications, and LLM-written routines for intermediate cases, balancing structure and flexibility.  The protocol shows that meta-level patterning of communication modes can scale to large, heterogeneous networks without central bottlenecks.
- **Relevance**: Directly informs communication protocols for agent swarms and orchestration layers that must flexibly mix symbolic APIs and NL messages, crucial in both production and games (e.g., dynamic scripting).
- **Link**: http://arxiv.org/pdf/2410.11905.pdf
- **Patent potential (flagged)**: The tri-modal communication policy (fixed routines, NL, LLM-generated routines) could be the basis of patentable orchestration engines for complex toolchains.

---

### Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems

- **Title/authors**: "Beyond Black-Box Benchmarking: Observability, Analytics, and Optimization of Agentic Systems" (authors not in snippet).
- **Date/source**: arXiv preprint, 2025-03-09.
- **Summary**: Argues that emerging agentic systems need internal observability and analytics rather than single-number benchmarks, and proposes a framework for tracing, logging, and analyzing agent behaviors.  It introduces metrics and tooling for identifying coordination failures, inefficiencies, and emergent phenomena during runtime.  The paper outlines optimization loops that use these analytics to adapt system configurations and policies.
- **Relevance**: Useful for building self-improving agent loops and orchestration dashboards that tune multi-agent pipelines automatically.
- **Link**: https://arxiv.org/pdf/2503.06745.pdf
- **Patent potential**: Analytics-based optimization loops for multi-agent orchestration can be positioned as proprietary AIOps-like platforms.

---

### Multi-Agent Collaboration Mechanisms: A Survey of LLMs

- **Title/authors**: "Multi-Agent Collaboration Mechanisms: A Survey of LLMs".
- **Date/source**: arXiv survey, 2025-01-10, arXiv:2501.06322.
- **Summary**: Provides a broad survey of LLM-based multi-agent systems, categorizing collaboration mechanisms, coordination structures, and application domains.  It distills patterns for communication, role specialization, and collective decision-making across recent systems.  While not proposing a new framework, it serves as a map of the design space.
- **Relevance**: Good as a scaffold for literature review and for discovering additional frameworks.
- **Link**: https://arxiv.org/pdf/2501.06322.pdf
- **Patent potential**: Not directly—primarily conceptual/organizational.

---

## Decentralized, gossip-style, and emergent coordination

### AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems

- **Title/authors**: "AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems".
- **Date/source**: arXiv preprint 2025-04-01; NeurIPS 2025 poster accepted.
- **Summary**: Eliminates centralized orchestrators by using decentralized coordination among LLM agents combined with evolutionary mechanisms to refine roles and behaviors over time.  The system continuously updates specialized skills and encourages privacy-preserving collaboration with minimal data exchange.  Experiments show improved efficiency, adaptability, and scalability over centralized baselines.
- **Relevance**: Hits decentralized information propagation, emergent behavior, and self-improving loops, giving concrete mechanisms for orchestrator-free systems.
- **Link**: https://arxiv.org/html/2504.00587v1

---

### A Gossip-Enhanced Communication Substrate for Agentic AI: Toward Decentralized Coordination in Large-Scale Multi-Agent Systems

- **Title/authors**: "A Gossip-Enhanced Communication Substrate for Agentic AI: Toward Decentralized Coordination in Large-Scale Multi-Agent Systems".
- **Date/source**: arXiv preprint, 2025-12-01, arXiv:2512.03285.
- **Summary**: Argues for using gossip protocols as a substrate beneath structured standards like MCP, A2A, and ACP to handle decentralized discovery, load signaling, failure detection, and emergent consensus.  It analyzes challenges such as semantic filtering, knowledge staleness, and trust, and outlines open problems in secure, meaning-aware gossip for agents.  The work frames gossip as providing diffuse global awareness in large agent swarms that cannot rely solely on central planners.
- **Relevance**: Directly tackles gossip protocols and decentralized propagation, and shows how to combine them with more formal orchestration layers.
- **Link**: https://arxiv.org/abs/2512.03285
- **Patent potential (flagged)**: The layering of gossip under MCP/A2A for emergent load-balancing and fault detection is highly patentable in cloud agents, IoT, and large-scale game server AI.

---

### Revisiting Gossip Protocols: A Vision for Emergent Coordination in Agentic Multi-Agent Systems

- **Title/authors**: "Revisiting Gossip Protocols: A Vision for Emergent Coordination in Agentic Multi-Agent Systems" (Habiba & Khan).
- **Date/source**: Vision/position paper, 2025.
- **Summary**: Presents gossip as a decentralized, epidemic-style communication mechanism key to scaling agent collectives while avoiding central brokers and single points of failure.  It highlights challenges around security, veracity, and trust in blindly propagated updates and suggests hybrid gossip-plus-trust architectures.  The paper connects these ideas to emerging standards like MCP and argues gossip is needed for future swarm-like agent ecosystems.
- **Relevance**: Conceptual foundation for gossip protocols in agent orchestration stacks and for designing emergent swarm behaviors.
- **Link**: https://arxiv.org/html/2508.01531v1

---

### Emergent Coordination in Multi-Agent Language Models

- **Title/authors**: "Emergent Coordination in Multi-Agent Language Models".
- **Date/source**: arXiv preprint, 2025.
- **Summary**: Studies emergent coordination by assigning persistent personas to agents and prompting them with theory-of-mind-style instructions like "consider what others might do."  The authors show that such prompt-level interventions can induce identity-linked differentiation, goal-directed complementarity, and group-level synergy.  They develop quantitative information-theoretic measures to operationalize and evaluate emergence.
- **Relevance**: Provides concrete design levers for emergent behavior in multi-agent environments that are purely prompt-level — very handy for fast prototyping and game AI.
- **Link**: https://arxiv.org/html/2510.05174v1

---

## Agent memory, knowledge, and self-improvement

### A-Mem: Agentic Memory for LLM Agents

- **Title/authors**: "A-Mem: Agentic Memory for LLM Agents".
- **Date/source**: arXiv HTML, 2025 (v11 in 2025-02 range).
- **Summary**: Introduces A-Mem, a memory architecture where agents autonomously generate rich contextual notes for new memories, including structured attributes and embedding vectors.  New memories trigger link generation and memory evolution operations that update existing memories and reveal higher-order patterns.  This architecture supports long-term interaction and self-refinement without handcrafted memory operations.
- **Relevance**: Directly about agent memory architectures and persistent knowledge systems, with mechanisms you can port into personal knowledge bases or long-lived research agents.
- **Link**: https://arxiv.org/html/2502.12110v11
- **Patent potential (flagged)**: The automatic link-generation and evolution mechanisms are attractive for enterprise knowledge graphs and adaptive user memory systems.

---

### AgentRxiv: Towards Collaborative Autonomous Research

- **Title/authors**: "AgentRxiv: Towards Collaborative Autonomous Research".
- **Date/source**: arXiv preprint, 2025-03-23.
- **Summary**: Proposes AgentRxiv, a platform where autonomous research agents share intermediate results and build on each other's work toward common goals.  Experiments show that labs using AgentRxiv-style sharing achieve higher accuracy and faster progress than isolated agent labs, e.g., a 13.7% relative gain on MATH-500.  The work argues for agentic collaboration in designing future AI systems and scientific workflows.
- **Relevance**: Good instantiation of autonomous ML research and self-improving loops across multiple agent "labs," plus a blueprint for distributed research KBs.
- **Link**: https://arxiv.org/html/2503.18102v1
- **Patent potential (flagged)**: A production AgentRxiv-style network for corporate research or cross-game content generation looks very patentable.

---

### A Multi-AI Agent System for Autonomous Optimization of Agentic AI Solutions via Iterative Refinement and LLM-Driven Feedback Loops

- **Title/authors**: "A Multi-AI Agent System for Autonomous Optimization of Agentic AI Solutions via Iterative Refinement and LLM-Driven Feedback Loops".
- **Date/source**: arXiv preprint, 2024-12-22, arXiv:2412.17149.
- **Summary**: Targets the problem that current agentic solutions require manual tuning of roles and interactions and introduces a framework where specialized agents handle refinement, execution, and evaluation in iterative loops.  The system autonomously explores variants of agent configurations across industries (e.g., enterprise NLP) and uses feedback to optimize them.  Results show improved performance and reduced human intervention in complex workflows.
- **Relevance**: Directly relevant to self-improving multi-agent architectures and automated orchestration search/tuning.
- **Link**: https://arxiv.org/abs/2412.17149
- **Patent potential (flagged)**: The automated search over orchestration graphs is highly applicable to industrial agent platforms and even procedural game event generators.

---

### A Multi-Agent Framework for Automated AI Research Paper Writing

- **Title/authors**: "A Multi-Agent Framework for Automated AI Research Paper Writing".
- **Date/source**: arXiv preprint, 2026-04-05.
- **Summary**: Proposes a multi-agent system that ingests unstructured research material and produces research manuscripts through specialized roles (e.g., literature surveyor, method synthesizer, editor).  The framework orchestrates agents over multiple stages with internal feedback and revision cycles.  It demonstrates feasibility on AI topics, pointing toward more general autonomous scientific writing.
- **Relevance**: Concrete example of tool-use and planning in an end-to-end research workflow; gives patterns for multi-stage content synthesis pipelines.
- **Link**: https://arxiv.org/abs/2604.05018

---

### AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds

- **Title/authors**: "AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds".
- **Date/source**: arXiv preprint, 2025-01-11.
- **Summary**: Presents AIOpsLab, a framework that not only generates workloads and faults and exports telemetry but also orchestrates cloud environments and provides interfaces for evaluating AI agents.  It envisions future autonomous cloud operations powered by agents.  The setup allows systematic testing of agent behavior under realistic operational conditions.
- **Relevance**: While evaluation-focused, it doubles as a design for agent orchestration in cloud operations, which is very close to real-world AIOps agent platforms.
- **Link**: https://arxiv.org/pdf/2501.06706.pdf

---

### Artificial Intelligence Orchestration for Text-Based Ultrasonic Simulation via Self-Review by Multi-Large Language Model Agents

- **Title/authors**: "Artificial intelligence orchestration for text-based ultrasonic simulation via self-review by multi-large language model agents".
- **Date/source**: Scientific Reports (Nature portfolio), 2025-04-10.
- **Summary**: Uses a multi-LLM agent architecture to orchestrate ultrasonic simulation systems that traditionally rely on complex GUIs.  Agents are functionally specialized (e.g., parameter selection, interpretation, quality control) and coordinated via an adaptive orchestration mechanism that configures agent composition and validation strategy based on task and domain features.  The approach improves simulation usability and accuracy compared with conventional workflows.
- **Relevance**: A domain-specific orchestration system illustrating how to structure specialized scientific agents and adapt orchestration policies; transferable to other simulation-heavy or game physics pipelines.
- **Link**: https://www.nature.com/articles/s41598-025-97498-y

---

## Biological/ecological inspiration and cross-domain simulations

### Large Language Model-driven Multi-Agent Simulation for News Diffusion Under Different Network Structures

- **Title/authors**: "Large Language Model-driven Multi-Agent Simulation for News Diffusion Under Different Network Structures".
- **Date/source**: arXiv preprint, 2024-10-16.
- **Summary**: Uses LLM-driven agents to simulate news diffusion across various network topologies, capturing agent personalities, behaviors, and structural effects on propagation.  It diverges from traditional agent-based models by letting LLMs generate richer interactions.  The framework is used to analyze misinformation spread and countermeasures.
- **Relevance**: Shows how network structure and local policies shape emergent global behavior — useful for designing gossip-like or social systems in agents, including in games.
- **Link**: http://arxiv.org/pdf/2410.13909.pdf

---

### Simulating Rumor Spreading in Social Networks using LLM Agents

- **Title/authors**: "Simulating Rumor Spreading in Social Networks using LLM Agents".
- **Date/source**: arXiv preprint, 2025-02-03.
- **Summary**: Builds a framework of multiple LLM agent types on four distinct network structures to simulate rumor propagation, measuring the impact of topology and agent behavior.  It evaluates which designs amplify or dampen rumor spread.  The system highlights how agent diversity and communication patterns affect global dynamics.
- **Relevance**: Directly related to gossip-like propagation and offers patterns for designing emergent social dynamics in agent-based games or decentralized info systems.
- **Link**: https://arxiv.org/pdf/2502.01450.pdf

---

### Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities

- **Title/authors**: "Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities".
- **Date/source**: arXiv preprint, 2024-07-22.
- **Summary**: Demonstrates how attackers can inject counterfactual or toxic "world knowledge" into LLM-based agent communities, which then silently spreads through agent communication and RAG frameworks without explicit prompt injection.  It shows that these manipulations persist while maintaining base capabilities and analyzes mechanisms of spread.  The paper emphasizes vulnerabilities in knowledge-sharing protocols.
- **Relevance**: Provides a cautionary lens on decentralized propagation and informs the design of trust and verification layers in gossip and orchestration protocols.
- **Link**: https://arxiv.org/html/2407.07791v1

---

## Personal knowledge bases and LLM-powered PKMs

### Practical PKB Implementations Inspired by Karpathy's LLM Knowledge Bases

- **Title/authors**: "How to Build a Self-Evolving AI Memory with Karpathy's LLM Knowledge Bases" (blog-style).
- **Date/source**: Blog article, 2026-04-05.
- **Summary**: Describes constructing LLM-powered personal knowledge bases by aggregating heterogeneous external data into cohesive structures, often visualized and edited in tools like Obsidian.  It emphasizes leveraging conversational logs and iterative agent interactions as a rich data source.  The piece outlines a self-evolving memory system ("Claude Code memory") as a concrete implementation.
- **Relevance**: Shows cutting-edge assemblage-based, non-scalable PKB systems in practice and can be combined with A-Mem-like architectures.
- **Link**: https://www.franksworld.com/2026/04/06/how-to-build-a-self-evolving-ai-memory-with-karpathys-llm-knowledge-bases/

---

## One more orchestration-architecture paper

### From Autonomous Agents to Integrated Systems, A New Paradigm: Orchestrated Distributed Intelligence

- **Title/authors**: "From Autonomous Agents to Integrated Systems, A New Paradigm: Orchestrated Distributed Intelligence".
- **Date/source**: arXiv preprint, 2025-03-18.
- **Summary**: Proposes Orchestrated Distributed Intelligence (ODI), emphasizing orchestration layers, multi-loop feedback mechanisms, and high "cognitive density" to turn record-keeping systems into dynamic action environments.  It synthesizes literature on multi-agent systems, recent technologies, and industry practice.  The focus is on integrating distributed intelligence into human-centric workflows.
- **Relevance**: Conceptual but directly frames multi-loop orchestration in real organizations; useful for thinking about industrial agent fabrics.
- **Link**: https://arxiv.org/pdf/2503.13754.pdf
