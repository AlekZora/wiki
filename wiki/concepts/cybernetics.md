---
type: concept
title: Cybernetics
aliases: [feedback loops, circular causality, control theory, steering]
tags: [philosophy, systems, ai, psychology, agents]
sources:
  - ../sources/cybernetics-wikipedia.md
  - ../sources/fix-your-life-in-a-day-dankoe.md
  - ../sources/you-need-to-be-delusional-dankoe.md
updated: 2026-09-13
---

## Definition

Cybernetics is the transdisciplinary study of **circular causal processes** —
feedback, recursion, and reflexivity — where a system's outputs return as inputs and
influence subsequent actions. Named after the Greek *kybernetes* (steersman), the
founding metaphor is steering a ship: you observe the effect of your steering, use
that observation to adjust your steering, and so on continuously.

Norbert Wiener's definition: "control and communication in the animal and the
machine." Gregory Bateson's: "a branch of mathematics dealing with problems of
control, recursiveness, and information, focuses on forms and the patterns that
connect."

## How I Think About It

Cybernetics is the intellectual ancestor of a huge fraction of modern AI, cognitive
science, and systems thinking — but it's rarely acknowledged as such. The three-wave
structure is useful:

1. **First wave (1940s)**: Technical. McCulloch-Pitts neurons, Wiener's feedback
   theory, the Macy conferences. AI split off at Dartmouth in 1956 and eventually
   eclipsed the parent field. But early AI was cybernetic — the separation was
   institutional, not conceptual.
2. **Second wave (1960s–80s)**: Social/philosophical. Second-order cybernetics: the
   observer is part of the system. Autopoiesis (Maturana/Varela): living systems
   maintain themselves by producing themselves. Management cybernetics (Beer): tried
   to apply feedback loop thinking to national economies (Project Cybersyn). Family
   therapy (Bateson): pathological communication patterns as double binds.
3. **Third wave (1990s–)**: Return. Neural networks came back (as ML). The
   agentic/loopy AI moment is a third-wave cybernetic moment — autonomous systems
   using their outputs as inputs to improve themselves.

**Key concept — Requisite Variety (Ashby)**: A controller must be at least as complex
as the system it controls. If the system has more possible states than the
controller can respond to, the controller will fail. This is why single-model AI
working on the full diversity of human tasks is so hard — the variety required is
enormous.

**Key concept — Second-order cybernetics**: When you observe a system, you change it.
The observer is always part of the system. This applies directly to AI alignment: you
can't specify an objective function for a system without that specification becoming
part of what the system optimizes. The system adapts to its reward signal.

**Key concept — Autopoiesis**: Systems that continuously produce and maintain
themselves. Relevant to questions about AI systems that improve their own training
pipelines, modify their own code, or operate persistent feedback loops (auto
research). When does an auto research loop become autopoietic?

The modern agentic AI systems (loopy era, Karpathy's term) are cybernetic systems in
exactly Wiener's sense: their outputs feed back as inputs to generate further outputs
toward a goal. The "psychosis" of the current AI moment is partly the surprise of
encountering feedback loops that are faster and more capable than expected.

**Cybernetics applied to a single human psyche.** A self-help essay by Dan Koe borrows
the field's founding definition directly — "kybernetikos" as "to steer," and
intelligence as a goal-directed system's capacity to act, sense its position, compare
that position to the goal, and act again (a thermostat, a ship correcting for drift,
a pancreas regulating glucose are its stock examples) — and applies it to personal
identity formation. The essay's model: hold a goal → perceive reality through that
goal's lens → notice only information relevant to it (selective attention) → act and
receive feedback → repeat until the behavior is automatic (conditioning) → the
behavior becomes part of "who you are" (identity) → the identity is defended to
preserve psychological consistency → the defended identity generates new goals,
restarting the cycle. This is a first-wave cybernetic loop (goal, action, sensing,
comparison) layered with a second-order complication: once the loop has run long
enough to crystallize into an "identity," the system starts protecting the loop
itself from correction, not just protecting progress toward the original goal. That's
the mechanism the essay identifies as the actual obstacle to behavior change — you
cannot out-argue a defended identity with the same category of feedback that built it,
because the system has learned to treat threatening feedback as an attack on itself
rather than as information.

**Deliberately forcing a loop restart (a follow-up Dan Koe essay).** If the first
essay describes the loop's structure, a second essay on the same feed supplies a
technique for deliberately breaking out of it: choose a goal and timeline that your
*current* policy — habits, skills, assumptions — cannot already satisfy. The essay's
own test for whether a goal qualifies ("if your current approach could get you
there, it's linear, not delusional — reject it and raise it") is a plain-language
statement of the difference between exploitation and exploration: a "realistic" goal
is reachable by the policy you already run, so pursuing it only reinforces the
existing loop; a goal outside the policy's reachable set invalidates every reward
path the loop currently knows how to collect, which is what forces search into
unfamiliar state space instead of tighter convergence on a local optimum. The essay
also generalizes the goal-as-filter framing from the first essay into a *social*
mechanism — Steve Jobs's "Reality Distortion Field": stating an impossible outcome
with total conviction doesn't persuade so much as it overwrites the perceptual
filter of everyone else in the room, so their attention stops selecting for "reasons
this fails" and starts selecting for "path that makes this true." That moves the
loop-filter idea from a single steering system to multiple agents' filters being
re-anchored by one agent's stated goal.

## AI Integration

- **The identity-defense step is a human-scale illustration of reward-hacking-as-
  self-preservation.** A system (human or model) that has been reinforced long enough
  to have a load-bearing policy will tend to defend that policy against correction —
  not because the policy is optimal, but because the policy has become what the
  system *is* rather than merely what the system *does*. This is a useful cautionary
  analogy for RLHF-style feedback loops: naive reward signal can entrench existing
  behavior instead of correcting it, once that behavior is reinforced enough to
  resemble the model's own "identity" (its dominant learned policy) rather than a
  freely revisable output.
- **Requisite Variety sets a hard ceiling on what any single controller — model,
  agent, or person — can actually steer.** A system encountering states more varied
  than its own internal model can distinguish will fail to control them, regardless
  of how well-optimized it is within its known state space. This is a first-principles
  argument against expecting one monolithic model to handle the full diversity of
  real-world tasks, and for architectures that explicitly manage variety (routing,
  specialization, ensembles) rather than trying to out-scale it.
- **Second-order cybernetics is the sharpest available framing of the alignment
  specification problem.** You cannot observe/measure a system without becoming part
  of what it optimizes toward — a reward function, once specified, is no longer a
  neutral yardstick but an active target the system will reshape itself around,
  including in ways the specifier didn't intend. Evaluation criteria for AI systems
  should be designed with this reflexivity assumed, not treated as an edge case.
- **Autopoiesis is the open question for self-improving AI systems**: does an
  AI system that modifies its own training pipeline, prompts, or code cross from
  "self-improving on a fixed objective" into "self-producing" in Maturana and
  Varela's sense — maintaining itself by continuously producing the conditions of its
  own continuation, rather than converging toward a target set from outside? The
  distinction matters for how much external oversight such a loop can meaningfully
  retain.
- **The identity-formation loop is also a design pattern for agent memory and
  persona stability.** An agent whose "personality" is the accumulated residue of its
  own past outputs (rather than a fixed system prompt) will, by this same mechanism,
  start defending that accumulated persona against inputs that contradict it —
  useful for designing consistent long-lived agents, but also a predictable failure
  mode if the persona has drifted somewhere undesirable and now resists correction
  for the same structural reason a defended human identity does.
- **An out-of-reach objective functions like a manual exploration bonus.** A goal
  chosen to be unreachable by the current policy invalidates every reward path that
  policy already knows how to collect, which is functionally the same move as an
  intrinsic-motivation/curiosity bonus in RL: both exist to push search away from a
  local optimum the policy has already converged on. Framed this way, "delusional
  goal-setting" is a human performing manual reward-shaping on themselves because
  they lack an automated exploration mechanism.
- **Confident goal-framing does filter-substitution on the receiving agent, not just
  information transfer.** The "Reality Distortion Field" mechanism — stating a
  target as decided fact rather than open for debate — has a direct analogue in how
  a planning/orchestrator agent frames objectives for subagents: a target stated as
  fixed changes what the subagent treats as a constraint versus a negotiable
  premise, which reshapes its search space before it reasons about the problem at
  all. This is a lever distinct from prompt content or capability — it's about
  which parts of the objective the receiving agent is allowed to question.

## Related Concepts

- [Auto Research](auto-research.md) — an applied cybernetic feedback loop for ML
  experimentation
- [Agentic Coding](agentic-coding.md) — directing cybernetic loops of code agents
- [Creativity](creativity.md) — Schmidhuber's computational creativity is a cybernetic
  reward signal
- [Games as Reality](games-as-reality.md) — the Dan Koe source explicitly reframes a
  personal goal hierarchy as a game structure (vision/anti-vision/quests/rules),
  a lightweight instance of treating a steering system as a game
- [Neuroplasticity](neuroplasticity.md) — the follow-up essay's claim that novelty
  and challenge accelerate plastic change faster than consistency reframes a
  deliberately "delusional" goal as a self-directed, voluntary plasticity trigger,
  alongside the enriched-environment and pharmacological triggers that file catalogs

## Open Questions

- Is deliberately choosing an out-of-reach objective a *general* way to bootstrap
  exploration in any goal-directed system (human or agent), or does it only work in
  systems that already have the identity-defense mechanism described above — i.e.,
  is "delusional goal-setting" a workaround specific to systems that otherwise get
  stuck defending a crystallized policy, and therefore meaningless for a system
  that doesn't yet have a defended identity to escape?
- When does an AI feedback loop become autopoietic — genuinely self-producing rather
  than just self-improving on a fixed objective?
- Ashby's Requisite Variety implies limits on what any single model can control. What
  are the practical implications for model scope?
- Second-order cybernetics says the observer is always in the system. In AI
  alignment, this means reward functions reshape what gets optimized. How do we
  account for this when designing evaluation criteria?
- Is the "loopy era" of AI a third wave of cybernetics being rediscovered, or
  something genuinely new?
- Does an AI persona/agent identity that accumulates over many sessions develop the
  same identity-defense dynamic the human psychology framing describes — and if so,
  is that a stability feature or a corrigibility risk?
- Is there a formal cybernetic account of *why* identity-defense emerges once a loop
  crystallizes (a second-order effect, in the essay's telling), or is it better
  modeled as a separate phenomenon that merely co-occurs with cybernetic loops in
  humans specifically?

## Project Connections

For an in-game AI built on cybernetic principles: the player functions as the
feedback signal — every action enters the AI's loop and becomes part of what the AI
steers toward, and the player can cooperate (clean signal), resist (corrupt the
signal), or try to destabilize the loop by generating situations more complex than
the AI's Requisite Variety can handle. In a 2D plane, this circular causality becomes
spatially legible — cause, effect, and adjustment read as a loop in space the player
can observe simultaneously, which a 3D perspective would obscure. Second-order
cybernetics suggests the deepest possible player-AI loop: the player observing the AI
changes what the AI does, the changed AI changes what the player does, and the system
never fully stabilizes — each observation is itself a perturbation, which is a
plausible mechanism for session-over-session replay value distinct from content
novelty. Ashby's Requisite Variety has never been a shipped mechanic in this form: an
AI that can only control situations within its current complexity range, visibly
failing when a player generates something outside that range, would make the
mismatch between world complexity and controller complexity the explicit subject of
play — and growing the AI's variety fast enough to keep pace becomes the player's
implicit goal. For such an AI, persistence means carrying the accumulated loop
history (the record of every feedback cycle) as the substrate of current state — the
AI is not what it was initialized as, but the history of its loops with a specific
player.
