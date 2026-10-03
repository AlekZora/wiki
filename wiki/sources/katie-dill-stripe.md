---
type: video
title: "Zombie Interfaces and the AI Building Boom"
url:
channel: Stripe Sessions (inferred from filename; not stated in transcript)
speaker: Katie Dill (inferred from filename)
published:
ingested: 2026-09-29
duration:
tags: [ai, design, craft, agents, systems, creativity, engineering]
concepts: [post-generation-editing]
source_path: raw/videos/katie-dill-stripe.md
---

## Summary

Katie Dill, speaking for Stripe's design team, compares today's AI-driven building boom to the post-WWII construction boom, when modernism's principles were copied without the intent behind them and produced "zombie buildings." She names three watchpoints that make the same outcome likely for software: LLMs give the most likely (past-oriented) answer rather than the specific one; fast output feels finished when it isn't (the microwave-burrito problem); and cheap work gets treated as disposable. The result is the "zombie user interface", meaning monotonous, empty or neglected. She offers four recommendations: have a point of view, encode standards into the machine, refuse to confuse "ready" with "good", and use AI to unleash creativity rather than only speed. The closing image is Ruskin's Gothic architecture, where no two columns are alike and the maker's hand shows.

Note: the transcript is a rough machine translation with some garbled passages (e.g. "pipsing", "AI scum"); details below stick to what is clear.

## Key Ideas

- **Quality is judged by outcome, not method.** Users don't care whether something was made with AI, only whether it is good. This became Stripe's basis for the standard applied to AI-made work.
- **Go one level deeper than the customer can see.** Stripe's design review of an ad produced 17 small fixes (softer edges, smaller bubbles, a little frost), and "pipsing" became an in-house verb for this kind of finishing. The aim is care, not perfection.
- **Noticing is the root skill.** Taste comes from attending to what users need beyond what they say, and to what signals good work in products, art and science.
- **Old design systems scaled consistency; new ones must scale intent.** With agents and generative UI making decisions when no designer is present, the object of design becomes the system, including whole patterns and flows, not just components.
- **Stripe's experience:** an MCP that read design documentation gave three different results for three people asking the same thing. They moved to a CLI built on the design system that makes the AI "more obedient" and loads documentation at the right time and place to avoid context rot.
- **The filter has moved.** Before, scarcity of finished ideas (20 ideas, capacity for one) pruned work throughout the process. Now 20 ideas can be generated a week, so filtering must happen after creation, when saying no is harder. Hence the editor role: someone who sees the whole and asks whether it is fully formed.
- **Details are the tell.** Citing Nabil Qureshi, great art is unexpected details plus deeper themes tying them together, which AI is weak at; AI slop offends because it implies the details don't matter ("the cup is green but could be blue").
- **Worked example:** an intro animation was started from a 3D scene and iterated with AI 56 times before it looked right. AI made a more complex scene and more attempts possible, but it still took heavy vetting.
- **Creativity, not only efficiency.** Chat boxes and CLIs are not the final interaction forms; like multi-touch or the synthesizer, new interfaces and aesthetics are yet to be invented. Give specific prompts with beliefs and source material, don't accept the first output, use adversarial agents to critique, and "protect the strange."

## Timestamps

- Not available (no timestamps in transcript).

## Quotes

> "The old system scaled consistency. But the new system must scale intent."

> "A system can follow all the rules and still be dead." (Christopher Alexander, quoted)

> "AI can help us raise the ceiling, not just the floor."

## My Take

**The AI lens is the whole talk, so the useful question is which claims are mechanistic.** Three are:

1. *Most-likely-answer bias.* Her "LLMs tell you the most likely answer" is the mode-seeking behavior of a trained model, and the Korean BBQ site with no character is what an unconditioned prompt returns. Her fix, specific prompts loaded with beliefs and source material, is conditioning away from the mean. This links to [representation-shapes-the-solution](../concepts/representation-shapes-the-solution.md): what you hand the model determines the answer space it searches.
2. *Same query, three results.* The failed MCP is a concrete data point on why loose documentation retrieval doesn't give reproducible agent behavior, and why a constrained tool surface (the CLI) does. It matches [harness-engineering](../concepts/harness-engineering.md): reliability came from the environment around the model, not from the model.
3. *The filter moved downstream.* This is the piece worth extracting, and I did: [post-generation-editing](../concepts/post-generation-editing.md). It is a structural claim about what happens when generation cost falls, and it applies beyond design.

**Where I'd push back.** The talk states that AI is weak at unexpected details and deeper themes, but the 56-iteration example shows the actual mechanism: a human judging pixel by pixel and re-rolling. That is human taste as a search-guidance signal over cheap samples. Whether a critic model could do this (she mentions adversarial agents but says the human must still push for better) is left open, and it is the interesting AI-design question here.

**Agent-design transfer:** "encode standards into the machine" is the same problem as writing specs and evals for autonomous agents. Standards that only live in a designer's head don't scale to agents, and the talk's answer, patterns and flows rather than atomic components, is a design-space version of giving agents workflows rather than tools.

**Project connection (specific):** the Attractor Zone depends on being recognizably specific rather than generic anthology-horror; "zombie" content is the risk if the series is generated at volume. The 17-fixes idea is a usable review pass: read each episode as a user would and ask whether it is fully formed, not whether it exists.
