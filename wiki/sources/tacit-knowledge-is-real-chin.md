---
type: article
title: Why Tacit Knowledge is More Important Than Deliberate Practice
url: https://commoncog.com/tacit-knowledge-is-a-real-thing/
author: Cedric Chin
published: 2020-06-09
ingested: 2026-06-14
tags: [psychology, expertise, learning, skill-acquisition, tacit-knowledge, ndm]
concepts: [recognition-primed-decision-making]
---

## Summary

Tacit knowledge — knowledge that cannot be captured through words alone — is real, pervasive, and more important to expertise development than deliberate practice. The author argues that transmissionism (the belief that explanation alone can teach skill) is a failed pedagogy, that deliberate practice is only applicable in domains with established pedagogy (chess, music, math), and that the field of Naturalistic Decision Making (NDM) offers more useful tools for practitioners in fields like programming, business, and design. The article establishes that tacit knowledge should be sought directly through emulation and apprenticeship, not decoded into explicit rules.

## Key Points

- Tacit knowledge = knowledge that cannot be captured through words alone. Physical examples: bike riding, judo. Cognitive examples: software architecture judgment, surgical decision-making.
- Transmissionism — teaching through explanation — is widely considered a failed pedagogy among serious educators.
- Expert explanations inevitably devolve into a cascade of caveats and gotchas. This is a diagnostic signal: when you see this, you are looking at tacit knowledge.
- In the 1970s, the US military commissioned expert systems to replace human specialists. Gary Klein's research showed this failed because extracting the relevant judgment from expert heads was intractable — the "knowledge acquisition problem." Aircraft maintenance officers couldn't be replaced because their knowledge couldn't be fully encoded.
- Making tacit knowledge explicit is theoretically possible but practically too difficult to be a reliable strategy.
- Deliberate practice (Ericsson) is only defined for domains with long histories of established pedagogy. Ericsson acknowledges this but hand-waves the application to other fields. NDM doesn't.
- Learning tacit knowledge: emulation, imitation, apprenticeship, osmosis — not explanation. The key is building the embodied or intuitive feel through repeated exposure and feedback.
- Warren Buffett under Benjamin Graham is the archetype: years of proximity and emulation, not lectures.

## Quotes

> "Tacit knowledge instruction happens through things like imitation, emulation, and apprenticeship. You learn by copying what the master does, blindly, until you internalise the principles behind the actions."

> "People with expertise in any sufficiently complicated domain will always explain their expertise with things like: 'Well, do X. Except when you see Y, then do Z, because A. And if you see B, then do P.' And if you push further, eventually they might say 'Ahh, it just feels right. Do it long enough and it'll feel right to you too.'"

> "Tacit knowledge does exist, and understanding that it does exist is one of the most useful things you can have happen to you. Once you understand that tacit knowledge exists, you will begin to see that big parts of any skill tree is tacit in nature, which means that you can go hunting for it."

## My Take

The key insight for AI: the knowledge acquisition problem that killed expert systems in the 1970s is the same problem LLMs are now navigating from the other direction. Expert systems tried to extract tacit knowledge through interviews and encode it as rules — and failed because the rules were always incomplete. LLMs skip the extraction step entirely: they pattern-match at scale across millions of human decisions, absorbing tacit knowledge implicitly the same way an apprentice does, but at much greater breadth. The question is whether that absorbed pattern-matching constitutes genuine expertise or sophisticated mimicry — and the RPD model in Part 2 gives a sharper way to think about this.

For NPC design: the cascade-of-caveats pattern that reveals tacit expertise is exactly the behavior a well-grounded NPC should exhibit. An NPC merchant who immediately suspects a trade offer because the prices are wrong is operating from a prototype, not a rule list. The quest generator produces quests, but what would make NPCs feel expert is RPD-like reasoning: immediate cue recognition, expectancy generation, satisficing action. See [recognition-primed-decision-making](../concepts/recognition-primed-decision-making.md).

The deliberate practice critique is also useful context for thinking about AI training. RLHF and reward modeling are analogous to deliberate practice: they work well when feedback is clear and fast. But for soft expertise (judgment, taste, creative direction), the feedback is slow and ambiguous — closer to the domains where NDM is needed.

Pair with: [copying-better-tacit-knowledge-chin.md](copying-better-tacit-knowledge-chin.md) (Part 2 — the RPD model and acquisition techniques).
