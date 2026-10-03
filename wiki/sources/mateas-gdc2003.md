---
type: article
title: "Façade: An Experiment in Building a Fully-Realized Interactive Drama"
url: ""
author: Michael Mateas, Andrew Stern
published: 2003-03-01
ingested: 2026-06-15
tags: [ai, narrative, game-design, agents, llm, nlp, systems]
concepts: [drama-management]
---
## Summary
This paper details the architecture and design philosophy behind *Façade*, a seminal interactive drama. The authors aim to create an experience that combines the high player agency of open-ended simulations with the well-paced, unified structure of authored narratives. The system centers on an AI "drama manager" that sequences story "beats"—small, self-contained units of dramatic action—in response to player interaction. The player communicates via natural language, which is interpreted by a "broad and shallow" NLP system into a set of "discourse acts." These acts influence the behavior of two autonomous, AI-driven characters, Grace and Trip, whose marriage is dissolving over the course of the 20-minute, replayable experience. The architecture is designed to make the plot feel mutable and responsive to the player's nuanced social interventions.

## Key Ideas
- Contemporary games are limited by their focus on physical action, preventing them from exploring complex human relationships, a domain best addressed through natural language.
- *Façade* seeks a middle ground between structured narrative (which offers good pacing but limited freedom) and open-ended simulation (which offers freedom but lacks narrative coherence).
- The architecture is built on three core AI components:
    1.  **Believable Agents:** The characters Grace and Trip are built using A Behavior Language (ABL), a reactive planning system allowing for complex, parallel behaviors.
    2.  **Drama Manager:** An AI that selects the next "beat" (a small, authored dramatic scenario) based on preconditions, story state, and a desired dramatic tension arc. This provides global agency.
    3.  **Natural Language Processing (NLP):** A custom, template-based system maps player-typed text into a fixed set of "discourse acts" (e.g., `criticize`, `agree`, `referTo <topic>`), which trigger character reactions. This provides local agency.
- The player's actions have both local effects (immediate reactions within a beat) and global effects (influencing which beats are chosen by the drama manager).
- The system acknowledges significant challenges, primarily the immense authorial labor required to create the thousands of behaviors and rules, and the brittleness of its NLP system, which can lead to misunderstandings or shallow responses.

## Quotes
> What is needed is a drama manager, that is, an artificial intelligence system that uses knowledge about how stories are structured to construct new story-like experiences in response to the player’s moment-by-moment, real-time interaction.

> Façade is an attempt to find a capable middle ground between structured narrative and simulation. We want to combine the strengths and minimize the weaknesses of each approach.

> The Façade system is generative in the sense that it mixes and sequences behaviors in sophisticated ways, as this paper will describe, but it does not generate the individual behaviors. Hand-authoring behaviors is a time consuming process...

## My Take
This paper outlines a foundational architecture for AI-driven interactive narrative that remains highly relevant. The hierarchical structure—a high-level Drama Manager orchestrating mid-level Beats composed of low-level Behaviors—is a powerful and transferable framework for designing agents that must balance long-term goals with immediate, context-sensitive reactivity. The core challenges *Façade* faced, authorial burden and brittle NLP, are precisely where modern AI could provide transformative solutions. An LLM could be integrated to replace their template-based NLP with a far more nuanced understanding of player intent. More powerfully, generative models could assist in authoring the vast library of behaviors and dialogue required for the beats, dramatically reducing the "two man-years" of labor and enabling richer, more scalable narrative experiences built upon this pioneering architectural vision. *Façade* provides the structural "skeleton" of a story; modern generative AI could provide the "flesh."