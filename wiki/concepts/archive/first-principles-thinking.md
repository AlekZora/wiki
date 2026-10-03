---
type: concept
title: First Principles Thinking
aliases: [physics-reasoning, first-principles, idiot-index, five-algorithm]
tags: [product, engineering, startups, philosophy, design]
sources: [sources/elon-musk-isaacson.md]
updated: 2026-04-10
---

## Definition

Reasoning from the fundamental constraints of a problem (physics, materials, logic) rather than from analogy to how things have been done before. Don't ask "what does this cost?"—ask "what *should* it cost, given the raw material costs and basic physical constraints?" The gap between what it costs and what it should cost reveals organizational and process inefficiencies, not material ones.

## How I Think About It

The key move is distinguishing between **physical constraints** (mass, energy, materials, information capacity) and **organizational constraints** (how things are currently done, who controls what, what expertise exists). First principles reasoning strips away the organizational layer to find the physical floor.

**The idiot index**: (current price) / (raw materials cost) = how much the organization is failing at its job. High idiot index = obvious organizational inefficiency. SpaceX applied this to every rocket component.

**The five-step algorithm** (Musk's version):
1. Question every requirement — most requirements aren't real, they're organizational artifacts
2. Delete — if you're not regularly deleting steps, you're not looking hard enough
3. Simplify — only after deletion
4. Accelerate — only after simplification
5. Automate — only after acceleration; automating a bad process makes it worse faster

**Where first principles thinking fails**: It's expensive to apply (requires deep domain knowledge to know what the actual physical constraints are), it can produce solutions that are technically optimal but organizationally impossible, and it can be used as motivated reasoning (deciding what you want and then constructing first-principles arguments for it).

**For AI product building**: Apply to the interaction design, not just the technology. What does this interaction *need* to do, at minimum? What is the "materials cost" of a good conversation? Most AI product failures are high-idiot-index failures—unnecessary complexity, extra steps, wrong abstractions.

## Related Concepts

- [Style of Thinking](style-of-thinking.md) — Hamming's related framework
- [Constraints as Advantages](constraints-as-advantages.md) — Rework's version of working from limits

## Open Questions

- How do you know when you've found a genuine physical constraint vs. a very entrenched organizational one?
- ~~Is first principles thinking learnable as a general skill or only domain-specific?~~ → [answered](../answers/first-principles-as-general-skill.md)
- When does deleting requirements cross from efficiency to hubris (like Jurassic Park)?
