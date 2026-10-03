---
type: video
title: Five AI Paper Presentations at Y Combinator
url:
channel: Y Combinator
published:
ingested: 2026-06-13
duration:
tags: [ai, ml, llm, agents, self-play, biology, formal-verification, agentic-workflow]
concepts: [self-guided-self-play, verified-intelligence, agentic-workflow]
---

# Summary

This document is a transcript of a Y Combinator event featuring five presentations on applied AI research. The host's introduction frames the session around key research frontiers: escaping the "human-generated data subspace" (the F-H problem) via self-play, improving "intelligence per sample" and "intelligence per watt," and finding alternatives to backpropagation.

The presentations cover:
1.  **AI for Biology (Yasi Beg):** This talk applies Richard Sutton's "The Bitter Lesson" to protein biology. It shows how large-scale protein language models (PLMs) like ESM, trained on massive sequence datasets using masked language modeling, learn emergent properties like 3D structure without explicit supervision. By massively scaling data (from 50M to 2.8B sequences), these general models can approach and sometimes surpass specialized, hand-engineered models like AlphaFold, particularly in domains like antibody design where evolutionary data is sparse. The models also develop an interpretable, hierarchical latent space corresponding to biological concepts from amino acids to functional protein domains.

2.  **Self-play for LLMs (Luke):** This presentation addresses the failure of naive self-play for LLMs, where models tasked with creating difficult problems for themselves degenerate into generating messy, artificially complex, and useless tasks. The proposed solution, "Self-Guided Self-play" (SGS), introduces a three-part system: a "conjecturer" generates new problems prompted by existing unsolved problems, a "solver" attempts them, and a "guide" scores the generated problems for relevance and elegance. This dual-reward system keeps the self-play loop grounded and productive, pushing the model's capabilities on meaningful tasks.

3.  **Stream RAG (Arnab Matei):** This talk focuses on reducing latency in voice AI agents that use Retrieval-Augmented Generation (RAG). Instead of waiting for a user to finish speaking, "Stream RAG" begins the retrieval process on partial, incoming chunks of speech. The core challenge is determining the optimal moment to trigger the RAG pipeline. The paper explores methods like fixed-interval triggers and fine-tuned models that decide when a partial query is "good enough" to retrieve relevant information, significantly reducing response time for more natural conversation.

4.  **Lean for Science (Robert George):** This presentation advocates for a new era of "verified intelligence" using formal verification tools like the Lean theorem prover. While LLMs excel at informal math, formal methods provide absolute correctness guarantees. The talk highlights the synergy between LLMs (for proof search) and formal provers (for verification). It showcases applications beyond math, including proving the correctness of software and even neural network components like Flash Attention, establishing a foundation for verifiable and trustworthy AI and scientific discovery.

5.  **Agentic Software Engineering (Luke Orthwine):** This talk proposes a radical shift in software development methodology, from a linear, chess-like process to a parallel, Real-Time Strategy (RTS) game-like one. Developers should act as commanders, "macro-ing" by spawning numerous AI agents to work on tasks in parallel. The focus is on maximizing throughput and developer attention via high-visibility interfaces (like an RTS mini-map), rapid course correction, and satisficing (good-enough solutions). This workflow is supported by tools for managing parallel environments, a continuously updated knowledge base for agents, and even gamified feedback like audio cues to manage the developer's cognitive load.

# Key Claims

-   Training AI exclusively on human-generated data (H) constrains it, preventing the discovery of novel solutions in the full potential solution space (F-H).
-   Richard Sutton's "Bitter Lesson" (scale is all you need) applies to biology; large models trained on vast sequence data can learn complex emergent properties like protein structure without hand-engineered features.
-   Naive self-play for LLMs fails because optimizing for task difficulty leads to the generation of messy, artificially complex problems that do not advance the model's core capabilities.
-   Effective self-play requires grounding task generation in a set of known, high-quality problems and using a separate "guide" to enforce relevance and elegance.
-   RAG-based voice agents can achieve low latency by "streaming" the retrieval process, acting on partial user queries while the user is still speaking.
-   Formal verification languages like Lean, when combined with LLMs, enable a new paradigm of "verified intelligence" that can guarantee the correctness of code, mathematical proofs, and scientific models.
-   Agent-driven software development should be modeled on Real-Time Strategy (RTS) games, prioritizing parallelization, high throughput ("macro"), and rapid iteration over perfect, linear planning.
-   Maximizing developer productivity in the agentic era requires building systems for high visibility, low-friction task spawning, and a continuously updated, machine-readable knowledge base.

# Mechanisms

-   **Protein Language Modeling (PLM):** A BERT-style masked language modeling objective applied to hundreds of millions of protein sequences. By predicting masked amino acids based on their context, the model learns co-occurrence patterns that implicitly encode the physical and functional constraints leading to 3D structure.
-   **Self-Guided Self-play (SGS):** A system with three roles for the LLM. 1) **Conjecturer:** Generates a new problem prompted with an unsolved problem from a trusted set. 2) **Solver:** Attempts to solve the new problem. 3) **Guide:** Scores the generated problem on its relevance and quality. The conjecturer is trained on a dual reward signal: the solver's failure (indicating difficulty) and the guide's score (indicating quality).
-   **Stream RAG:** The user's incoming speech is chunked. As chunks arrive, a decision module (e.g., fixed-interval or a learned model) triggers a RAG query on the partial transcript. This allows the computationally expensive retrieval to happen in parallel with the user's utterance, minimizing end-to-end latency.
-   **Lean Theorem Proving:** A formal system where mathematical proofs are written as code. Each step, or "tactic," is checked for logical validity by a trusted kernel. LLMs can be used in a search loop to propose sequences of tactics to solve a given goal.
-   **RTS-style Agentic Workflow:** A human developer acts as an orchestrator, issuing high-level commands. This spawns multiple autonomous worker agents, each in its own sandboxed environment (e.g., a git work-tree). The agents work in parallel to complete tasks and submit them as pull requests. The developer monitors all agents via a high-visibility dashboard (the "mini-map") and provides course corrections.

# Useful Examples

-   **AlphaGo vs. AlphaZero:** AlphaGo learned from human games, while AlphaZero learned purely from self-play, discovering superior, non-human strategies. This exemplifies escaping the human data subspace (H).
-   **ESM Protein Model:** A concrete protein language model that learns to predict 3D protein structure from sequence data alone, demonstrating the success of scaling over hand-engineering.
-   **Nucleophilic Elbow:** A specific protein motif that ESM learned to identify across evolutionarily distant proteins, showing it learned a functional, not just a superficial, representation.
-   **Formal Math Problems in Lean:** The domain used to test Self-Guided Self-play, where the correctness of a solution can be automatically and definitively verified.
-   **Warcraft/Starcraft Analogy:** Programming with agents is compared to an RTS game. The developer manages their "economy" (token usage, compute), "production" (spawning agents for new tasks), and "micromanagement" (deeply engaging with a single critical task) to maximize overall progress ("macro").
-   **APM (Actions Per Minute) Tracker:** A tool used by Luke Orthwine's team to measure agentic productivity, not by keystrokes, but by the number of tool calls the agents make per minute.

# Possible Relevance

-   **AI Agent Design:** The Self-Guided Self-play (SGS) mechanism is a blueprint for building agents capable of recursive self-improvement without a human-in-the-loop, while avoiding degenerative failure modes. The RTS-style workflow provides a meta-architecture for human-agent teams, emphasizing parallelization, high-visibility monitoring, and shared knowledge systems. Stream RAG is a key technique for agents that need to interact with the world in real-time.
-   **Narrative Systems:** The F-H problem and self-play are directly analogous to generating novel stories that go beyond existing tropes. An SGS-like system could use a "guide" model as a story critic to maintain thematic coherence while a "conjecturer" explores novel plot structures.
-   **Game Mechanics:** The RTS workflow is a direct application of game mechanics (macro, micro, resource management, APM) to a professional discipline. This could inspire the design of management or simulation games based on orchestrating AI agents. Self-play is a core mechanic for creating advanced AI opponents that can discover emergent strategies.
-   **Knowledge Management:** Orthwine’s system of using agents to continuously build and refine a structured, linked knowledge base (in Markdown) is a practical, automated KM strategy for human-AI teams. The use of Lean for formal verification represents the ultimate in building a knowledge base with provably correct information.

# Links

-   **People:** Yasi Beg, Luke (from Tatsu's lab), Arnob Matei, Robert George, Luke Orthwine, Richard Sutton, Noam Brown, Steve Quake, Terry Tao, Max Tegmark.
-   **Concepts:** The Bitter Lesson, AlphaGo, AlphaZero, Self-play, RAG (Retrieval-Augmented Generation), Lean (theorem prover), Formal Verification, Mechanistic Interpretability, Multiple Sequence Alignment (MSA), RTS (Real-Time Strategy) games.
-   **Systems/Models:** ESM (Evolutionary Scale Modeling), ESM2, ESMC (ESM Cambrian), AlphaFold, Stream RAG, Mathlib, Channel AI.
-   **Papers:** "Scaling Self-play with Self-guidance".

## My Take

Five papers, one underlying problem: how do AI systems escape the ceiling imposed by human-generated data and human-supervised processes? The F-H gap (the solution space unreachable by learning only from humans) is the thread connecting every talk. Self-play generates novel training signal beyond human games. Formal verification provides ground-truth correctness checks independent of human judgment. Protein language models find emergent structure humans couldn't encode by hand. Stream RAG removes the human speech-pace bottleneck from retrieval. The RTS workflow recasts the human entirely — from controller to commander.

The self-guided self-play mechanism has direct relevance to quest generation: instead of hand-authoring templates, an SGS-like system could conjecture new quest scenarios from existing high-quality ones, have a solver-agent attempt to "play" them, and score output on relevance to a specific player's history. The conjecturer/solver/guide split mirrors the Renderer/Simulator/Planner architecture — the guide is the validator that keeps generation grounded.

The RTS analogy for agentic coding is the clearest articulation I've seen of what the developer role becomes in an agent-heavy workflow: set strategy, spawn units, watch the minimap, course-correct on outliers. APM as a productivity metric — not keystrokes but agent tool calls per minute — reframes what "working fast" means in this era. Satisficing (ship good-enough, not perfect) combined with high parallelism is a production philosophy, not just a workflow tip.

The verified intelligence framing (Lean + LLMs) is the most distant from current work but the most structurally interesting: a system where a language model generates proofs and a kernel verifies them is a model for any domain where "correct" can be formally specified. For NPC simulation, formal grounding constraints (the fact database from Step 6) are a weak version of this — assertions the system cannot violate. The more formal the constraint layer, the closer to verified intelligence.

AI intersection: these five papers collectively define the frontier of AI self-improvement — the boundary where AI systems stop learning from humans and start generating their own training signal, verified by formal or empirical feedback loops rather than human annotation.