---
type: concept
title: Holography
aliases: [hologram, wave interference, light field recording]
tags: [physics, optics, information, holography]
sources:
  - ../sources/holograms.md
updated: 2026-05-09
---

## Definition

Holography is the technique of recording and reconstructing a complete 3D light field — not just a single perspective image, but the full set of waves emanating from a scene. It works by recording the *interference pattern* between light reflected from the scene (object wave) and a clean reference wave. This pattern encodes phase information (which a conventional photograph discards), allowing perfect reconstruction when the reference wave is shone through the film again.

Two key properties distinguish holograms from photographs:
1. **The whole is in every part.** Every region of the film contains information about the entire scene. Cutting the film in half doesn't give you half the image — it gives you the whole image at lower resolution.
2. **Extreme sensitivity.** Recording requires mechanical stability at the nanometer scale; any vibration comparable to the wavelength of light (hundreds of nm) destroys the interference pattern.

## How I Think About It

The "whole in every part" property is the philosophically interesting one. Information is distributed, not localized. This is the opposite of a photo, where you can trace exactly which part of the image came from which part of the film. In a hologram, information is smeared across the entire surface — a fundamentally different architecture.

The physics is: record the *relationship* between two waves (interference), not the waves themselves. Reconstruction is the inverse: use the known reference to decode the relationship and recover the original wave. You don't store the object — you store how the object transformed a reference.

## Related Concepts

- [Information Asymmetry](information-asymmetry.md)
- [Neural Networks](neural-networks.md)
- [Cognitive Externalization](cognitive-externalization.md)

## Open Questions

- Are there practical information storage or compression architectures that are holographic in this distributed sense — where any fragment can reconstruct the whole?
- How does this relate to NeRFs (Neural Radiance Fields), which reconstruct 3D scenes from 2D observations?

## Project Connection

"Holographic narrative" is a compelling structural model for the paranoid sci-fi series. Each episode (or each character's perspective) contains the whole story at a limited resolution and from a constrained angle. The audience accumulates viewing angles, progressively reconstructing the true scene from its interference patterns. Layer 2 (hidden agendas) is the phase information that ordinary photographs (Layer 1 / official narrative) cannot capture — you need interference to see it.

The "extreme sensitivity" property maps to paranoid fiction: in confined spaces, small perturbations (a word out of place, a glance held too long) carry enormous information. The environment is interferometrically sensitive.

## Game Design Vector

**Mechanic:** The game world stores information holographically: the relationship between elements, not the elements themselves. The player cannot read any single part of the plane in isolation — they must read the interference pattern between elements to recover what is encoded. Cutting a section of the plane doesn't remove half the information; it reduces the resolution of the whole. The player accumulates viewing angles across sessions, each one increasing the reconstruction fidelity of the true scene.

**2D Expression:** In 2D, the holographic property is directly expressible: the entire plane contains the same information at varying resolutions depending on where the player reads it from. The 2D surface records relationships between elements (as an interference pattern records the relationship between waves), not the elements themselves. Small perturbations — a position held too briefly, a delay fractionally too long — carry enormous information, because the plane is interferometrically sensitive at that scale.

**Addictive Loop:** The player is progressively reconstructing the game world from its interference pattern — accumulating viewing angles until the true scene resolves. Each session adds a new angle; accumulated angles increase the resolution of the reconstruction. The player returns because the reconstruction is not complete, and each new angle reveals something that was previously ambiguous. The session limit is the hologram's: you can only reconstruct what your accumulated angles span.

**Novel Angle:** The extreme sensitivity property — nanometer-scale vibrations destroy a holographic interference pattern — as the game's signal design. In the game world, small perturbations are the load-bearing signals: the word out of place, the glance held too long, the path taken that was slightly inconsistent with prior behavior. The gross movements carry little information; the residuals carry everything. Reading the residuals is the player's skill.

## AI Integration Vector

**Player-AI Relationship:** The player does not observe the AI directly; they observe the interference pattern between the AI's behavior and a reference. The AI is the object wave; the player's baseline expectation is the reference wave. What the player records is the relationship between the two — phase information that direct observation (a photograph of behavior) would discard. The relationship is between a reader of interference patterns and the object that creates them.

**AI as Evolving System:** The AI's development is visible as changes in the interference pattern — not as direct capability announcements but as shifts in the relationship between behavior and the player's reference expectation. The player must distinguish between a change in the AI's internal state and a change in what the AI is choosing to make visible. Development is the accumulation of viewing angles that progressively resolve the AI's true structure.

**AI as Development Environment:** The player constructs a reference — a baseline theory of how the AI should behave — and uses it to decode the interference pattern of how the AI actually behaves. Development happens in the residual: what the reference can't yet explain is what the AI has become that the player hasn't modeled yet. The reference is the player's evolving theory; the residual is the AI's evolving reality.

**Persistence:** The AI carries phase information across sessions — the relationship between its internal state and what it expresses behaviorally. Persistence is a record of relationships, not events. The player's accumulated viewing angles are what persist from the player's side; the AI's interference pattern is what persists from the AI's side. Neither is directly readable; the reconstruction is the product of both.
