---
type: concept
title: Assembly of Complexity
aliases: [ecosystem assembly, system bootstrapping, incremental assembly, scaffold species, Humpty Dumpty Effect]
tags: [systems, biology, engineering, ai, emergence, design, complexity]
sources:
  - ../sources/out-of-control-kelly.md
updated: 2026-07-01
---

## Definition

Assembly of complexity is the principle that highly complex systems cannot be constructed by simultaneously combining all their components — they must be grown incrementally, with order of introduction mattering as much as the final inventory of parts. The components needed to enable early stages of assembly (scaffold components) may not be present in the mature system; without them, the system cannot reach its mature state regardless of what parts are available later.

Stuart Pimm's laboratory finding names the core claim: "To make a wetland you can't just flood an area and hope for the best. You are dealing with systems that have assembled over hundreds of thousands, or millions of years. Nor is compiling a list of what's there in terms of diversity enough. You also have to have the assembly instructions."

Kevin Kelly calls the failure mode the **Humpty Dumpty Effect**: once a complex system disassembles, it cannot necessarily be put back together even if all the parts are present, because the assembly sequence that created it took millions of years and depended on now-extinct scaffold components.

## How I Think About It

The key move is separating "what's in the system" from "how the system got there." A complete parts list is necessary but not sufficient. You also need the assembly instructions — the sequence in which components must be introduced — and the scaffold components that are necessary during assembly but not present in the final state.

This is counterintuitive because most engineering treats systems as configurations: a car is the same car whether you assemble it from left to right or right to left. But complex adaptive systems are path-dependent: the state you reach depends on the history of how you got there. The same inventory of species assembled in a different order produces a different stable ecosystem. The same model architecture trained on data in a different sequence produces a different model.

Kelly's clearest illustration: Steve Packard couldn't restore an Illinois prairie by planting prairie seeds, because what he thought was a prairie was actually a savanna — a prairie with trees. The "oddball" savanna species that didn't belong on any prairie species list turned out to be the chaperone species without which the system couldn't assemble. Once introduced in the right order, rare birds, butterflies, and plants returned on their own through increasing-returns dynamics. But if those species had gone globally extinct, no amount of standard restoration effort could have reconstructed the ecosystem.

The practical design rule Kelly extracts: "Complex machines must be made incrementally and often indirectly. Don't try to make a functioning mechanical system all at once, in one glorious act of assembly. You have to first make a working system that serves as a platform for the system you really want."

## AI Integration

- **AI system bootstrapping**: you cannot train a capable AI system from scratch in one pass. You need scaffold components — simpler models that generate training data for more capable models, curricula that introduce concepts in learnable order, intermediate capabilities that unlock subsequent capabilities. The AI equivalent of Packard's savanna species: components that must be present during development but may not be visible in the final system.
- **Assembly order in training**: the sequence in which data, tasks, and objectives are introduced during training affects the final model's capabilities in ways that aren't predictable from the inventory of training inputs. Curriculum learning is assembly-of-complexity in practice: introduce simpler patterns first to scaffold the learning of harder ones.
- **The Humpty Dumpty problem in AI**: if critical training data is lost, corrupted, or legally restricted after training, the model trained on it cannot be reconstructed even if all other components remain. The data is the scaffold species. This is why model lineage and training data provenance matter — not just for reproduction, but because they represent assembly instructions that may be impossible to recover.
- **Multi-agent system bootstrapping**: building a capable multi-agent AI system is an assembly problem. Introducing all agents simultaneously into a cold system may produce a different (worse) equilibrium than gradually bootstrapping: start with two agents, let them develop interaction patterns, then introduce a third, etc. The stable attractor of the mature system depends on the assembly path.
- **The "thumb for intelligence" problem**: Danny Hillis observed that the human opposable thumb was scaffolding for intelligence — necessary for developing intelligence (tool use → dexterous manipulation → intelligence is advantageous), but not required once intelligence is established. Many capabilities of AI systems are thumbs: necessary during development, not present or necessary in the deployed system. Identifying which current capabilities are thumbs (scaffolding) vs. load-bearing structures guides development strategy.
- **Staged deployment as ecosystem succession**: Pimm's succession sequences (fire → weed → pine → broadleaf) map to AI deployment stages. Trying to skip stages — deploying highly capable agents before simpler infrastructure is stable — is like trying to grow broadleaf trees before the weed stage has prepared the soil. "Unripe machinery let out before it is fully grown and fully integrated with diversity will be a common complaint."
- **Increasing returns and system self-assembly**: once a system is past a tipping point — enough scaffold species present, enough connectivity established — it can self-assemble further. The law of increasing returns: "If you build it, they will come. And the more you build it, the more that come." AI capability development exhibits this: certain capability thresholds trigger qualitative jumps that wouldn't be predictable from below the threshold.

## Related Concepts

- [Swarm Intelligence](swarm-intelligence.md) — swarm systems assemble through local interactions over time; the assembly path determines which attractor the swarm reaches
- [Concentric Development](concentric-development.md) — a game design application of assembly of complexity: build working systems inside-out, each shell building on a complete inner system
- [Coevolution](coevolution.md) — coevolving systems are simultaneously assembling each other; neither can reach its mature state independently
- [Emergence](emergent-narrative.md) — emergent properties appear at threshold moments in the assembly process; they cannot be engineered directly, only scaffolded toward
- [World Models](world-models.md) — world models in AI are assembled incrementally; the final model's structure reflects the assembly history, not just the final data distribution

## Open Questions

- What are the scaffold components for current AI systems? Which capabilities are thumbs — necessary for development, not present in the deployed system?
- Is there a general method for identifying chaperone components (Packard's savanna species) before they go extinct / become unavailable?
- Can assembly instructions be extracted post-hoc from a mature system, or must they be recorded prospectively during construction?
- At what complexity threshold does Humpty Dumpty become irreversible? Is there a complexity level above which destroyed systems cannot be reconstructed?
- How much of the difficulty in AI alignment is an assembly-order problem — not that the components aren't available, but that they're being introduced in the wrong sequence?

## Project Connections

The Side Quest AI system is an assembly problem. The build plan (Steps 1–8) is an assembly sequence, not an arbitrary order — each step creates the scaffold for the next. Step 6 (fact database + constraint validator) is a scaffold species: it enables Step 7 (Godot setup) to work correctly, but it won't be visible to the player in the final experience. Skipping to Godot before the constraint validator exists is exactly the error Packard made before finding the savanna species — building the visible structure before the enabling substrate.
