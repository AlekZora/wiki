---
type: concept
title: Recognition-Primed Decision Making
aliases: [RPD, RPD model, expert intuition, naturalistic decision making]
tags: [psychology, expertise, decision-making, learning, skill-acquisition, ai, agents]
sources: [tacit-knowledge-is-real-chin.md, copying-better-tacit-knowledge-chin.md]
updated: 2026-06-14
---

## Definition

Recognition-Primed Decision Making (RPD) is Gary Klein's model of how experts make decisions in the real world. When an expert encounters a situation, their brain immediately pattern-matches it against a collection of **prototypes** stored in implicit memory. If a match is found, the recognition automatically generates four by-products simultaneously:

1. **Expectancies** — how the situation is likely to evolve.
2. **Plausible goals** — what to prioritize right now and what to defer.
3. **Relevant cues** — what signals to pay attention to (and what to ignore).
4. **Action script** — a course of action ready to execute.

Because all of this happens in implicit memory, experts cannot fully verbalize how they did it. "It just felt right" is not evasion — it is an accurate description of an unconscious recognition operation.

When no prototype matches, the expert falls back: gathers more information, constructs a narrative of the situation, and attempts to match a different prototype. Action selection is **satisficing**, not optimizing: the expert mentally simulates each candidate action one at a time and picks the first one that passes their mental test — they do not compare all options and select the best.

The four acquisition levers that follow from RPD:
- **Expand prototype set** — systematically seek unfamiliar situations; use scenario-based training, not lectures.
- **Identify prototype gaps** — when an expert says "felt right" where you would have compared options, they have a prototype you lack. Ask about their cues, expectancies, goals, and actions.
- **Improve mental simulation** — identify your decision requirements, practice them, get feedback so simulations match reality.
- **Cognitive critique** — narrate past events linearly as you experienced them (never revealing what you learned later), then compare cues/expectancies/actions with a more expert practitioner.

RPD was developed by Gary Klein within the field of Naturalistic Decision Making (NDM), which studies expertise under real-world conditions rather than in controlled laboratory settings. NDM is "closer to anthropology than psychology."

## How I Think About It

The key conceptual move in RPD is separating **recognition** from **deliberation**. Most decision-making theory focuses on the deliberation part (how do you compare options, weigh probabilities, select optimally?). But Klein found that experts barely deliberate — they recognize and act. Deliberation is what you do when recognition fails.

This reframes what expertise actually is: not knowing more rules, but having more prototypes. Each prototype is a compressed, experiential pattern that immediately generates four answers (expectancies, goals, cues, actions) without any conscious analysis. Building expertise is therefore about expanding the prototype library, not memorizing principles.

The "cascade of caveats" pattern (expert explains their judgment as "do X, except when Y, but also if A and not B...") is the verbal trace of a prototype that was encoded from experience, not a rule list. The expert is trying to reconstruct, in language, something that was never stored as language.

## AI Integration

- **LLMs as RPD machines at scale**: language models are prototype-matching systems trained on millions of human decisions. The four RPD by-products (expectancies, goals, cues, actions) are what get compressed into model weights across training examples. The key difference: LLMs generate statistically likely next tokens rather than running explicit forward simulations — they skip the satisficing loop Klein describes. Chain-of-thought reasoning and extended thinking modes come closest to the RPD simulation step.
- **The knowledge acquisition problem, resolved**: expert systems in the 1970s tried to extract tacit knowledge through interviews and encode it as rules — and failed. LLMs solve this by absorbing tacit knowledge implicitly from observed decisions at scale, the same way an apprentice absorbs it from proximity, but without the extraction bottleneck.
- **NPC expertise via RPD**: an NPC that feels expert should not compare options — it should recognize and act. A merchant who immediately flags a suspicious trade isn't running comparisons; she's pattern-matching and generating an expectancy about player intent. Designing for this behavior means encoding prototypes (situational patterns + response tendencies) rather than rule lists. The quest generator is a partial implementation: it reads game state (cues), generates situational context (expectancies), and selects from templates (action scripts). Full RPD-style NPCs would require richer prototype libraries.
- **Playtesting via cognitive critique**: narrate a session linearly from the player's perspective, then compare cue recognition and expectancies against the designer's model. This surfaces mismatches between designed intent and actual player prototypes — a systematic method for identifying why a mechanic feels opaque.
- **Training AI on tacit expertise**: RLHF and reward modeling are the current approximations of NDM training programs. They work well when feedback is fast and clear (chess, math proofs). For soft expertise (taste, judgment, creative direction), feedback is slow and ambiguous — closer to the domains where RPD acquisition techniques are needed. Fine-tuning on expert annotated "tough cases" is the closest AI analogue to Klein's CTA method.

## Related Concepts

- [organizational-tacit-knowledge](organizational-tacit-knowledge.md) — organizational version of the same problem: tacit know-how embedded in company culture that cannot be extracted by documentation alone
- [insight-learning](insight-learning.md) — both involve implicit recognition, but insight learning is about sudden restructuring; RPD is about immediate prototype access
- [wicked-vs-kind-learning-environments](wicked-vs-kind-learning-environments.md) — RPD works best in kind environments where prototypes generalize; wicked environments are where RPD can lead experts astray
- [world-models](world-models.md) — the prototype library is a world model: a compressed internal representation of how situations develop
- [loop-engineering](loop-engineering.md) — the cognitive critique method mirrors the maker/checker loop; expert feedback on recognition is the verification step

## Open Questions

- Is LLM pattern-matching genuinely equivalent to RPD prototype matching, or does the absence of a forward simulation loop make the analogy misleading?
- Can you deliberately design "tough cases" for NPC playtesting that expose prototype gaps in the player model?
- In wicked learning environments (where experience gives false prototypes), how do you distinguish good expert intuition from learned miscalibration?
- What is the minimum prototype density before the cascade-of-caveats verbal pattern emerges? Can this be a metric for NPC expertise believability?
