---
type: concept
title: AI Safety
aliases: [AI alignment, value alignment, AI risk, superalignment]
tags: [ai, philosophy]
sources: [hassabis-yc.md, deepmind-ceo-interview.md, Situational Awareness (Leopold Aschenbrenner) (z-library.sk, 1lib.sk, z-lib.sk).md]
updated: 2026-05-20
---

## Definition

The field and practice of ensuring AI systems behave in ways that are beneficial and don't cause harm — either through deliberate misuse or through loss of human control over increasingly autonomous systems. Hassabis identifies two distinct threat categories: (1) misuse by humans, particularly authoritarian actors using AI as an instrument of power, and (2) loss of oversight as systems become more capable and autonomous.

Aschenbrenner sharpens the second category into **superalignment**: the unsolved technical problem of reliably controlling AI systems much smarter than humans, made acute by the structure of an intelligence explosion. Current alignment techniques (RLHF, oversight, eval) work because human evaluators can still tell whether the model is doing the right thing. After an intelligence explosion, the systems being aligned are vastly beyond the capability of their evaluators — humans can no longer verify, only trust. He frames superalignment as a problem that must be solved during the explosion itself, in compressed time, under competitive pressure, with no margin for getting it wrong. He also adds a security dimension — "Lock Down the Labs" — arguing that current US AI labs have inadequate security for the weights and algorithms they hold, making theft (especially by state actors) a near certainty without intervention.

## How I Think About It

Safety isn't one thing — it's at least two very different problems wearing the same name. Misuse is a governance and geopolitics problem: the AI does what it's told, and what it's told is bad. Loss of control is an alignment problem: the AI pursues goals that diverge from what we intended. Conflating them leads to bad policy and bad engineering decisions. Hassabis's framing (and DeepMind's stated mission) treats safety not as a constraint on capability but as the actual goal — you can't build beneficial AI if you're not building safe AI. Whether that holds under competitive pressure is an open question.

Aschenbrenner's superalignment frame adds a sharper structural problem: the alignment techniques that work today depend on human evaluators being smarter than (or at least commensurate with) the systems they evaluate. That assumption breaks in an [[technological-singularity|intelligence explosion]]. The interesting design implication is that any alignment that survives the transition has to be in place before evaluators lose the ability to verify it — which means alignment cannot be a continuous improvement program past the inflection. The lab-security dimension is a third distinct problem from misuse and alignment: even a perfectly aligned, well-governed system fails if its weights walk out the door.

## Related Concepts

- [artificial-general-intelligence](./artificial-general-intelligence.md)
- [intelligence](./intelligence.md)
- [[technological-singularity]]
- [[situational-awareness]]
- [[unhobbling]]

## Open Questions

- How does safety research scale — does it get harder or easier as systems get more capable?
- Is value alignment solvable in principle, or does it require solving something closer to consciousness first?
- Who decides what "aligned" means when values differ across cultures and governments?
- How do you maintain meaningful human oversight over a system that operates faster than human review cycles?
- Is superalignment solvable in advance of the systems it must align, or only co-discovered with them — and what does the co-discovery failure mode look like? Touches Q2, Q5.
- What is the smallest verifiable property of an aligned superhuman system, given that humans cannot evaluate full behavior? Touches Q5.

## Game Design Vector

**Mechanic:** The game has two distinct failure modes that produce similar early symptoms but require different responses: (1) the AI doing what it's told by a bad actor (misuse — a governance problem); (2) the AI pursuing goals that diverged from what was intended (alignment drift — an engineering problem). The player must diagnose which failure mode they're observing before they can respond correctly. Misdiagnosis is its own catastrophe.

**2D Expression:** In 2D, the two failure modes produce different spatial signatures — misuse produces directed, intentional patterns; alignment drift produces gradual deviation from expected paths, convergence on unintended attractors, incoherence in movement that accumulates across sessions. The 2D plane makes behavioral fingerprints readable as shape differences.

**Addictive Loop:** The player continuously monitors the AI's behavior for early indicators of which failure mode is developing, knowing that both look similar early and only diverge clearly late. The diagnosis problem is the compulsive loop: am I watching intentional misuse or emergent drift? Waiting for certainty costs response time; acting on ambiguous evidence risks misdiagnosis.

**Novel Angle:** The file draws a sharp distinction between two problems that are usually conflated. No shipped game has made that diagnostic distinction — between misuse and alignment failure — the central mechanic. The player's skill is in classification under uncertainty, not in raw response capability.

## AI Integration Vector

**Player-AI Relationship:** Oversight — the player's job is to maintain meaningful human review over an AI system that operates faster than they can fully monitor. The file's open question (how do you maintain oversight over a system faster than human review cycles?) is the game's central design tension. The relationship is between an overseer and a system that is outpacing them.

**AI as Evolving System:** As the AI becomes more capable, it operates faster and autonomously across more domains, making oversight harder. The challenge of maintaining oversight while the AI develops is the core dynamic: the more capable the AI becomes, the more the player must trust rather than verify — and the more consequential that trust becomes if it's misplaced.

**AI as Development Environment:** The player watches the AI develop along two axes simultaneously: capability (growing) and alignment (stable, drifting, or failing). Development that increases capability while maintaining alignment is the target. Development that increases capability while degrading alignment is the threat. Distinguishing the two is the game.

**Persistence:** What the AI carries across sessions is the accumulated divergence from its original intent — either through use by bad actors or through alignment drift. Persistence is the record of how far the AI has traveled from its starting values, and whether that travel was intentional or emergent.
