---
type: concept
title: Genealogy as Knowledge Graph
aliases: [relational-schema-as-memory, genealogical-compilation]
tags: [knowledge-representation, memory, systems, mythology, history]
sources: [library-of-greek-mythology-apollodorus]
updated: 2026-07-23
---

## Definition

A genealogy — a family tree of parent-child and marriage relationships — is a relational schema: a fixed set of typed edges (parent-of, married-to, child-of) connecting named entities. When a body of narrative knowledge has no absolute external timeline (as with Greek myth, where "once upon a time" is the only native chronology), genealogy becomes the substitute: every story is locatable because it's anchored to a position in a family tree, and family trees can be cross-referenced, merged, and extended without needing a global clock. This is the same underlying structure as a knowledge graph: entities as nodes, typed relationships as edges, and any fact can be attached to a node as long as the node's identity is stable.

## How I Think About It

The interesting move isn't the genealogy itself — it's what genealogy is *for* in a compilation like Apollodorus's *Library*: it's the compression scheme that lets a mass of independently-sourced, partially contradictory oral and poetic material get organized into one navigable structure without an editor having to resolve the contradictions by authorial fiat. You don't need to decide whose version of a myth is "true" — you just need to know where in the family tree the story happens, and multiple versions can coexist at the same coordinate. The genealogy is infrastructure, not content.

The practical wrinkle that shows up immediately once you try to build one of these is entity disambiguation: the same named figure (a "boxed" name in the *Library*'s tables) can be the pivot point connecting two otherwise separate family trees — e.g., a single ancestor shared by both the Argive and Theban royal lines. Handling that correctly is identical to the foreign-key / canonical-ID problem in any relational database or knowledge graph: you need one stable identity for an entity that gets referenced from multiple contexts, or the structure silently forks into two disconnected copies of the same person.

## AI Integration

- **Canonicalization without hallucinated consensus**: A compiler synthesizing many partial, contradictory sources into one structure has to resist the urge to "fix" the contradictions by picking a preferred version and presenting it as settled. This is a direct, useful discipline for RAG and summarization systems — the failure mode isn't just factual hallucination, it's *false consensus* hallucination, where a system smooths over genuinely disputed source material into one confident-sounding answer.
- **Relational schema as long-term agent memory**: An AI agent accumulating facts over a long-running session or across sessions faces the same problem Apollodorus faced — no global timeline, many independently-generated facts, needing a structure that lets any new fact be attached at a stable coordinate. A typed entity-relationship graph (who relates to whom, how) is a much more robust backbone for persistent memory than a flat chronological log, because it supports the same kind of cross-referencing and multi-path lookup a genealogy does.
- **Entity disambiguation as the load-bearing problem**: The manuscript-era trick of *boxing* a name that recurs across multiple genealogical tables is functionally identical to entity resolution in knowledge graphs and to this wiki's own concept-linking convention — the hard part of building any of these structures is not capturing relationships, it's making sure the same entity referenced from different places resolves to one canonical node rather than silently duplicating.
- **What it reveals about intelligence/systems generally**: Humans solved the "how do I store a large, inconsistent, multi-source body of knowledge so it stays queryable" problem with genealogy and other relational scaffolds (family trees, taxonomies, hierarchies) long before computation existed. The pattern — fixed-identity nodes, typed edges, tolerance for multiple co-existing facts at one coordinate — is a recurring solution wherever a system needs to compress a lot of loosely-structured narrative or event data into something navigable, whether the "compiler" is an ancient editor, a database schema designer, or an LLM building a memory graph.

## Related Concepts

-

## Open Questions

- Where's the line between a genealogy/knowledge-graph backbone becoming *too* rigid — i.e., cases where the relational scaffold itself starts distorting which stories can be told, the way genealogical systematization sometimes forced myths from genuinely independent regional traditions into an artificial common ancestry?
- Could an AI memory system explicitly borrow the "boxed shared node" convention — flagging entities referenced from multiple otherwise-separate context clusters as high-value canonicalization targets?

## Project Connections

This wiki's own architecture (wiki/concepts/ + cross-linking + index.md) is itself an instance of this pattern — a relational scaffold letting sources from wildly different domains attach to stable concept nodes. Worth keeping in mind if the Side Quest AI system's fact DB (wiki/projects/game/) ever needs a richer relational layer beyond flat JSON facts — genealogical/graph structure is the natural next step if NPC or world-state relationships start needing multi-hop queries.
