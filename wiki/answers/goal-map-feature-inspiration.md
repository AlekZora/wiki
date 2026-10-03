---
type: answer
title: Goal Map Feature Inspiration
question: Which concepts in this wiki, including ones from unrelated fields, could inspire new features for Goal Map, a goal-tracking productivity app?
answered: 2026-09-29
tags: [ai, design, psychology, behavior, systems, productivity]
---

## Scope and method

This is an exploration pass, deliberately unfiltered for feasibility; prioritisation comes later.

- Goal Map is not documented anywhere in this vault. The app description came from the question itself: goal structuring, milestones, check-ins, drift detection, map visuals, rewards.
- Coverage: the definitions of all 120 concept pages were read, and about a dozen pages in full. Source pages were not swept one by one, so ideas that live only in sources are probably missing.
- **AI rule** from the question: AI is limited to goal structuring, milestone generation and check-in classification, unless an idea justifies a new, narrow job.
- In the AI column, "Structuring", "Milestones" and "Classification" mean one of those existing jobs covers the idea. "New AI job" means it would need a new one. "Code" means deterministic code is enough.
- Rows marked *Loose inspiration* are indirect finds rather than direct matches.

## 1. Starting, committing and quitting

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Self-initiation gap](../concepts/self-initiation-gap.md) | A goal starts as a "hypothesis until day N" with a review date built in. It can only be deleted after the user has made one small real thing for it, which forces contact with reality before rejection. | Goal structuring, new goal lifecycle | Code |
| [Failure-cost asymmetry](../concepts/failure-cost-asymmetry.md) | Make quitting cheap and respectable: a "retire" action that archives the goal with a one-line lesson. People attempt riskier goals when exit costs little. | New goal lifecycle | Code |
| [Worst-day design](../concepts/worst-day-design.md) | Each goal stores a list of barriers and a "worst-day version" (the smallest action that still counts). Plans contain if/then contingencies. | Milestones, check-ins | Milestones |
| [Whole-game learning](../concepts/whole-game-learning.md) | The first milestone is a complete tiny version of the goal, like a full 1 km run, rather than one component of it. | Milestones | Milestones |
| [Vertical slice](../concepts/vertical-slice.md) | One early milestone is done to full quality, to prove the goal is real before scaling it. | Milestones | Milestones |
| [Backward-chain design](../concepts/backward-chain-game-design.md) | Milestones are derived in reverse from the fixed end constraint (deadline, outcome, audience) and then executed forward. | Goal structuring | Structuring |
| [Concentric development](../concepts/concentric-development.md) | The map has rings. Secondary goals only unlock once the core habit has held for N weeks, so nothing is built on an unproven base. | Map visuals, structuring | Code |
| [Assembly of complexity](../concepts/assembly-of-complexity.md) | Milestone order is modeled as dependencies, and the map flags milestones attempted out of order. | Milestones, map | Code |
| [Constraint as camouflage](../concepts/constraint-as-camouflage.md) | A hard cap on active goals. It removes a decision from the user and also keeps the AI away from multi-goal trade-offs, which it is bad at. | Goal structuring | Code |

## 2. Drift detection and feedback

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Metrics trap](../concepts/metrics-trap.md) | Pair every proxy metric (hours logged) with an outcome milestone. Flag drift when the proxy rises and the outcome stays flat. | Drift detection | Code |
| [Regulatory integrity](../concepts/regulatory-integrity.md) | Watch the brakes, not the output: a skipped weekly review or a lapsed planning ritual is an early warning that comes before milestones slip. | Drift detection | Code |
| [Retention-proxy testing](../concepts/retention-proxy-testing.md) | Predict abandonment early from same-week signals: longer gaps between check-ins, shorter check-in text, repeated postponing. | Drift detection | Code |
| [Closed-loop systems](../concepts/closed-loop-systems.md) / [Cybernetics](../concepts/cybernetics.md) | Check-in outcomes automatically resize next week's milestones: shrink them after misses, grow them after streaks of success. | Check-ins, milestones | Code (sizing rule); Milestones if regenerated |
| [Wicked vs kind environments](../concepts/wicked-vs-kind-learning-environments.md) | Tag each goal by how its feedback behaves. For goals where feedback is delayed or misleading, show "early signal is unreliable" and use a longer review cadence. | Goal structuring, check-ins | Structuring |
| [Power laws](../concepts/power-laws.md) | For fat-tail goals like job applications, outreach or pitches, show attempts made rather than success rate, and say up front that most attempts yield nothing. | Map visuals, drift | Code |
| [Research craft](../concepts/research-craft.md) | Forecast-and-check: the user predicts whether they'll hit a milestone, and the app tracks their calibration over time. | Check-ins, new calibration score | Code |
| [Illusory insight](../concepts/illusory-insight.md) | Check-ins claiming a breakthrough ("I finally figured it out") get tagged, and the next week asks whether it changed what the user did. | Check-ins | Classification (one new label) |

## 3. Memory and reflection

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Memory reconsolidation](../concepts/memory-reconsolidation.md) | Store the original "why" word for word and show it next to the user's current restatement. Memory of motives drifts every time it's recalled. | Check-ins | Code |
| [Mnemonic medium](../concepts/mnemonic-medium.md) | Resurface the user's own past lessons on a spaced-repetition schedule, timed to the point of forgetting. | Check-ins, new lesson resurfacing | Code |
| [Dreaming](../concepts/dreaming.md) | A weekly batch pass over the check-in log to find patterns across weeks ("you miss every Tuesday"). | Drift detection, new weekly digest | Code for statistics. A narrative digest would be a new AI job. |
| [Memory forgetting](../concepts/memory-forgetting.md) | Untouched milestones visibly fade on the map and eventually ask to be removed on purpose. | Map visuals | Code |
| [Experiential memory](../concepts/experiential-memory.md) | "What worked last time" notes attach to goal types and are offered when a similar goal is created. | Goal structuring | Code (tag match) or Structuring |
| [Emotional memory](../concepts/emotional-memory.md) | A completed milestone becomes a landmark on the map with a photo or note. Emotional moments are what people remember. | Map visuals, rewards | Code |

## 4. Map visuals and narrative

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Emergent narrative](../concepts/emergent-narrative.md) | The map draws the path actually taken, with detours, retreats and restarts, beside the planned route. | Map visuals | Code |
| [Drama management](../concepts/drama-management.md) | Pacing: choose the next milestone from a pool by its difficulty, so weeks alternate between push and recovery and never stack all hard. | Milestones | Code (scoring) over AI-generated candidates |
| [Representation shapes the solution](../concepts/representation-shapes-the-solution.md) | Let the user switch between map, timeline and dependency tree. Each view makes different problems visible. | Map visuals | Code |
| [Experience goals](../concepts/experience-goals.md) | Each goal carries one line on how it should feel, and milestones are checked against it. | Goal structuring | Structuring |
| [Affect circumplex](../concepts/affect-circumplex.md) | Mood at check-in is a 2D tap (pleasant–unpleasant × energy), not an emoji. Low-and-low over time signals burnout. | Check-ins, drift | Code |
| *Loose inspiration:* [MICE quotient](../concepts/mice-quotient.md) | Goal "story types" (explore, learn, change self, fix a problem) each get a different map shape. | Map visuals | Structuring |
| *Loose inspiration:* [Elegance](../concepts/elegance-game-design.md) | A few simple map rules that produce varied states, rather than many special visuals. | Map visuals | Code |

## 5. Motivation and rewards

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Compulsion vs craft](../concepts/compulsion-vs-craft.md) | Audit rewards: streak-loss penalties are compulsion (stopping feels costly). Prefer rewards that make the next attempt attractive, and offer a streak-free mode. | Rewards | Code |
| [Self-determination theory](../concepts/self-determination-theory.md) | Check-ins are tagged for whether the goal feels chosen ("want") or imposed ("should"). Persistent "should" goals get flagged for review. | Check-ins | Classification |
| [Flow state](../concepts/flow-state.md) / [Intrinsic motivation](../concepts/intrinsic-motivation.md) | Adjust milestone difficulty to the recent hit rate, keeping it in the flow band between boredom and anxiety. | Milestones | Code (the adjustment) |
| [Easter eggs](../concepts/easter-eggs-as-design.md) | Hidden map rewards for depth rather than completion, for example finishing a goal after retiring and retrying it. | Rewards | Code |
| [Leverage](../concepts/leverage.md) | Tag milestones by whether they build a lasting asset or spend time once, and show the ratio. | Goal structuring | Structuring |

## 6. How the AI itself is built

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Neuro-symbolic architecture](../concepts/neuro-symbolic-agent-architecture.md) | The AI proposes milestones, and a deterministic validator checks dates, dependencies and caps before anything is written. This is the Side Quest rule that the LLM never touches state. | Milestones | Code validator around existing AI |
| [Post-generation editing](../concepts/post-generation-editing.md) | AI-generated milestones stay drafts until the user edits or confirms them, so "generated" is never treated as "good". | Milestones | Code (UI gate) |
| [Capability-gated oversight](../concepts/capability-gated-oversight.md) | Let the AI adjust plans automatically only after the user has accepted enough of its suggestions. | New plan-autonomy setting | Code (gating) |
| [Contradiction-driven design](../concepts/contradiction-driven-design.md) | When two goals compete for the same hours, state it as a contradiction and look for a plan that satisfies both, not a split. | Goal structuring | New AI job: conflict resolution between goals |

## 7. Loose inspiration: social and identity

| Concept | Feature idea | Touches | AI |
|---|---|---|---|
| [Recommendation as identity](../concepts/recommendation-as-identity.md) | A shareable finished map as self-presentation, not a stats brag. | New sharing feature | Code |
| [Bounded reciprocity](../concepts/bounded-generalized-reciprocity.md) / [Social identity](../concepts/social-identity-theory.md) | Small accountability pods whose members see each other's maps. Group membership raises follow-through. | New social feature | Code |
| [Comprehension floor](../concepts/comprehension-floor.md) | A shared map must make sense to an accountability partner with no context, so it needs a plain-language summary layer. | Map visuals, sharing | Code |
| [Self-continuity](../concepts/self-continuity.md) | At milestones, show a snapshot of the user's past self (the original entry, where they started). | Rewards | Code |
| [Interface lag](../concepts/interface-lag.md) | Check-ins become an anytime quick note instead of a scheduled ritual, sorted afterwards. | Check-ins | Classification |
| [Tractable immersion](../concepts/tractable-immersion.md) | For learning goals, an early milestone is contributing existing skills to a community in the new field. | Milestones | Milestones |

## Against the AI rule

Almost all of these fit the rule. Only two would need a new AI job:

- **Conflict resolution between goals** (section 6).
- **A narrative weekly digest** (section 3), which also works as plain statistics without AI.

The neuro-symbolic validator would enforce the rule in code rather than rely on the prompt.

## Open

- Prioritisation has not been done.
- A sweep of source pages, not only concepts, could add more ideas.
