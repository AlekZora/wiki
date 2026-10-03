---
type: answer
title: Goal Map — What the Wiki Says
question: Which notes in this wiki could inspire or challenge Goal Map's engine, engagement and revenue design?
answered: 2026-10-01
updated: 2026-10-02
tags: [ai, design, game-design, narrative, psychology, behavior, motivation, productivity]
---

# Goal Map — what the wiki says

Research pass over this vault, 2026-10-01. Paths below are relative to the vault root; paths like
`docs/DESIGN.md` and `lib/prompts/map.ts` refer to the Goal Map repo at `~/projects/goal-map/`.
Follows on from [Goal Map Feature Inspiration](goal-map-feature-inspiration.md), which was an
unprioritised exploration pass; this one ranks ideas against the product's purpose.

**Method.** Started from `wiki/index.md`, grepped `wiki/` for about 25 keyword families (fog of war, core loop, cozy, companion, juice, hero's journey, procrastination, deep work, time-boxing, planning fallacy, habit, self-monitoring, shame/guilt, progress, retention, monetization, build in public, narrator, ritual, streak, setback, coach, procedural), then read about 45 notes in full. Concept pages, answers and decision records (your own synthesis) were preferred over clipped sources.

**Update, later on 2026-10-01.** One source was ingested after the first pass: `wiki/sources/evidence-based-goal-achievement-system.md`, an AI-written research report (likely Perplexity) on evidence-based goal-app design. It is the closest source in the vault to Goal Map, and it was partly written *for* this prototype: two of its references are prompts about it. Its evidence is woven into ideas 2, 3, 5, 7 and 9, Tension A, and new Tensions G and H, each marked **Research report (2026-10-01 update)**. The ranking was not changed. Effect sizes are as the report states them, not checked against the papers.

**Second update, 2026-10-01 — checked against primary sources.** The report's key claims were checked against the studies themselves, and two more gaps were filled. **Section 5 has the verdict on each claim.** Most held. Two were overstated, and the ideas that relied on them are corrected in place (marked **Evidence check**). New sources: Gollwitzer & Sheeran 2006 (if–then plans), Wang et al. 2021 (MCII), Harkin et al. 2016 (progress monitoring), Singh et al. 2024 (habit formation), Leroy & Glomb 2018 (via press release; the paper is paywalled), Project Horseshoe 2017 (coziness), RevenueCat 2026 (subscription benchmarks). **Third update, same day:** the user's planning-fallacy brief, plus Buehler, Griffin & Ross 1994, which was checked against it. Woven into ideas 8 and 9, Tension J and Section 5.

**Fourth update, 2026-10-02.** One video: Roger Chen on building Lobby and Bro (`wiki/sources/bro-app-store-roger-chen.md`; a founder's own account, metrics not checked). Woven into the shareable-map bullet in "Engaging but off-purpose", Tension E, Bold 2 and new Tension K, each marked **Roger Chen (2026-10-02 update)**. The ranking was not changed.

**Scope (decided 2026-10-01): Goal Map is going to be a product.** Where an idea collides with `PROJECT.md`'s out-of-scope list (payments, notifications, replanning, weekly reflection, multiple goals), the collision is a product decision to make in `PROJECT.md`, not a reason to drop the idea.

**Convention.** "*The note says*" = what is written in the note. **Inference:** = my reasoning, not in any note.

**Coverage gaps (current as of the third update, 2026-10-01).** Still **no notes** on: the hero's journey or its alternatives, deep work (beyond flow), and consent and privacy for shared journeys. Fog of war appears once, in passing (`wiki/concepts/situational-awareness.md`). Anything below touching those areas is built from adjacent notes, and is marked as inference. *Filled since first writing:* procrastination, habit formation and self-monitoring (the research report, then primary sources); cozy games (Project Horseshoe 2017); subscription pricing (RevenueCat 2026); planning fallacy (the user's brief plus Buehler et al. 1994). See Section 5.

---

## 1. Top 10 ideas, ranked by fit

Ranked by how directly each one moves a user toward their next milestone, and how well it fits the engine / engagement / revenue design.

### 1. The narrator controls the setup, never the resolution

**Idea.** The Attractor decision record set a rule for its adaptive AI director. It may choose what happens *before* an event exists, but it may never alter an outcome. It also sets a test: would the player feel "cheated or interested" if they read the design doc? Applied to Goal Map: the story, the traveler and the map may only narrate events that were actually logged. They may frame a setback, but never invent progress, soften a drift, or quietly move the summit.

*The notes say:* "authorial control over the setup and zero control over the resolution"; "**consistent generosity is a mechanic, adaptive generosity is a lie**". The same entry also notes that a practice-replay of the failure moment was more useful than "an LLM-generated motivational line — and needing no AI at all." The hallucinated-agency note names the failure this rule prevents: an agent making promises or claims "that the environment cannot fulfill," which turns inaccuracy into "broken trust."

**Sources.** `wiki/decisions/decision-log.md` (2026-09-09, adaptive director entry) · `wiki/concepts/hallucinated-agency.md` · `wiki/concepts/neuro-symbolic-agent-architecture.md` (via hallucinated-agency)

**In the product.** A validator on every story beat: each beat must reference real `CheckIn` / `Classification` / `Milestone` ids, and the beat is rejected if it doesn't. This extends the existing Zod-retry-then-error pattern to narrative.

**Closer to the milestone?** Yes. **Inference:** the whole value of "am I still on my path?" depends on the user trusting the map. A flattering story destroys the signal the product sells.

**Effort** S (a rule plus a validator). **AI** Governs AI, needs none itself.

### 2. End every focus session with a hand-off line

**Idea.** Separate motivation from momentum, and design for momentum. Close each focus session by writing the very next action, and stop before exhaustion so re-entry is obvious. The next session starts from that line, not from a blank.

*The notes say:* "Motivation: 'I strongly feel like doing this.' Momentum: 'I already know what the next action is, so continuing is easy.'" The same note recommends "stopping sessions before exhaustion to leave an obvious re-entry point." The flow source lists four task properties that induce flow: variety, wholeness (finishing a whole unit), autonomy and appropriate time pressure. It treats removing distractions as a prerequisite.

**Sources.** `wiki/sources/human-agency-analysis-chatgpt.md` · `wiki/sources/Flow-Erleben Theorie von Csikszentmihalyi.md` · `wiki/concepts/flow-state.md`

**In the product.** The post-session one-line check-in gets a second optional field: "Next time, start with…". That field is `nextStep`, already in the `CheckIn` schema and in Optional Task 10. The next focus session opens pre-filled with it. **Inference:** a session sized to finish one whole small unit (wholeness) beats a fixed 25-minute timer.

**Research report (2026-10-01 update).** This idea now has cited evidence, not just a vault heuristic. The report calls the **ready-to-resume plan** (Leroy & Glomb, four studies) its "most defensible distinctive micro-intervention": briefly writing where work stopped and how to return reduces attention residue. Its checkpoint has four fields (what was just completed, the very next move, what is still uncertain, when it reopens), and in a map interface "the checkpoint becomes a **footprint at the last known position**." The resume screen should show "You stopped here / Do this next / This was the unresolved question", not the whole backlog. It proposes **resume latency** (opening the route → first meaningful action) as the metric. Source: `wiki/sources/evidence-based-goal-achievement-system.md`.
**Inference:** `nextStep` covers the second field. An optional "still unsure about…" line would cover the third at almost no cost, and both fit the footstep the map already draws.

**Evidence check (primary source).** **Partly overstated.** Leroy & Glomb measured the benefit on the task people switched *to*: less attention residue, better decisions and recall. They **did not test** whether the note helps when people come back. Their press release says so, and the samples were small lab groups (n = 66, n = 44). The report's "resume from footprint" and "resume latency" build on the untested half. The idea survives with a more honest pitch: "write the next step so you can stop thinking about it", not "you'll restart faster". Whether it speeds up restarting is something Goal Map can measure itself: time from opening the app to the first check-in, with and without a stored `nextStep`. Source: `wiki/sources/leroy-glomb-2018-ready-to-resume.md`.

**Closer to the milestone?** Directly. It removes the start-up cost that sits between sessions.

**Effort** S. **AI** No.

### 3. The worst-day version and if-then contingencies, as the core of "help when stuck"

**Idea.** Plans fail when they depend on willpower. List the barriers first, lower the friction until the plan works on a bad day, and write contingencies ("if tired, do X"). Temporary patches are tracked as debt, and fixing the root cause becomes a goal of its own.

*The notes say:* "You want it to work on the worst day." "Good plans contain contingencies." The concept note flags the source as an anecdotal coaching talk, "a heuristic, not a finding". It also notes that an AI could run this barrier dialogue, and leaves open whether it would "resist settling for the first plausible plan."

**Sources.** `wiki/concepts/worst-day-design.md` · `wiki/sources/build-systems-not-goals.md`

**In the product.** "I'm stuck / low energy" on the session-start screen offers the milestone's stored smallest step, or splits the active milestone. Each milestone carries a one-line worst-day step, generated with the milestones and editable.

**Research report (2026-10-01 update).** It supports this idea with evidence and sharpens it. If–then plans are implementation intentions, with meta-analytic effects reported at d = 0.27–0.66. Adding an obstacle step (MCII) gives g ≈ 0.34 and works better **interactively than as a document**. The sharper part is that "stuck" should be **diagnosed before it is treated**. It splits into seven barriers, each with a matched response: unclear → "list three unknowns", overwhelming → shrink, threatening → "a version no one will see", boring → reward or companion, blocked → remove the blocker, conflicted → resolve priority, depleted → reschedule "without moralizing". It also warns that **planning can become procrastination**: stop once a next action, a cue and an obstacle response exist. Source: `wiki/sources/evidence-based-goal-achievement-system.md`.
**Inference:** the stuck button becomes one question ("What makes starting hard right now?") with seven answers. Code maps each answer to a response, and only "split this milestone" would need AI. That keeps most of the feature deterministic, which matters given Tension F and the three-jobs rule.

**Evidence check (primary sources).** The if–then core **holds**: d = .65 across 94 tests (Gollwitzer & Sheeran). Three corrections and additions:
- **"Interactive beats a document" meant a human experimenter**, face-to-face (g 0.465 vs 0.277). It did not mean software. Whether an AI conversation behaves like the human arm or the document arm is untested (Wang et al.). The corrected overall MCII effect is g ≈ 0.24. The paper says self-written plans fail on *quality*, so the defensible AI job here is narrow: check the user's own if–then for vagueness and non-executable responses. Don't present the AI as a coach that replaces the person in the room.
- **Rehearse, don't just remind.** People who rehearsed the cue–response link acted 87% of the time, vs 40% for a written plan left as a reminder and 20% with no plan (one study, cited in Gollwitzer & Sheeran). **Inference:** when a worst-day step is created, ask the user to complete "When ___ happens, I will ___" in their own words. Don't just save the AI's version.
- **Reinforcement matters:** plans without any reinforcement showed no significant effect in one physical-activity meta-analysis cited by Wang et al. A plan made at goal creation and never seen again may do little.

Sources: `wiki/sources/gollwitzer-sheeran-2006-implementation-intentions.md` · `wiki/sources/wang-2021-mcii-meta-analysis.md` · `wiki/concepts/implementation-intentions.md`.

**Closer to the milestone?** Yes. It is the difference between a zero day and a small step on the trail.

**Effort** M. **AI** Yes, via the existing milestone job or a narrow new "split this milestone" job. See Tension F.

### 4. A story built from a beat library, not free prose

**Idea.** The drama-management architecture from Façade: a library of small authored "beats", each with preconditions and a tension effect. A director picks the next beat from story state, so the arc has a shape without the player facing branches. The note's own lesson: quality is bounded by the richness of the beat library, and an LLM can fill in wording while the structure stays authored. Emergent narrative adds that mechanics produce story only when they operate on "human values"; resource optimization produces "data, not story."

**Sources.** `wiki/concepts/drama-management.md` · `wiki/sources/mateas-gdc2003.md` · `wiki/concepts/emergent-narrative.md` · `wiki/concepts/story-as-excavation.md` (situation-first beats generative prompts that spell out the plot)

**In the product.** About 15–25 beat types keyed to real events: first step, first off-route day, declared detour, blocker, blocker cleared, return after a gap, worked ahead, milestone reached, summit. Code picks the beat from stored classifications. Optionally an LLM writes one or two sentences inside the beat, validated per idea 1. **Inference:** Goal Map's value axis is "on my path / lost / found again", which is a human value in Sylvester's sense, so the raw material for story is already there.

**Closer to the milestone?** Partly. **Inference:** a story that names the real situation ("the path has waited three days") gives a reason to come back. Without idea 1 it becomes off-purpose decoration.

**Effort** M–L. **AI** Optional and narrow. Code-only beats work.

### 5. A commitment window at goal creation, plus a cheap, respectable retire

**Idea.** The bottleneck in starting is possibility → commitment. It closes through **option-collapse** (deadlines, commitment windows, kill criteria, a shipped artifact), not through better evaluation. Make commitments temporary ("hypothesis until day N"), refuse to reject an idea before it has produced an external artifact, and make exit cheap. Willingness to start depends on the cost of stopping.

*The notes say:* "An idea is not allowed to be rejected before producing an external artifact." "Shrinking the set does [converge]." Failure-cost asymmetry: the leverage point "is making bad outcomes cheap to discover and cheap to abandon — not making good outcomes more rewarding."

**Sources.** `wiki/answers/why-origination-is-harder-than-execution.md` · `wiki/concepts/self-initiation-gap.md` · `wiki/sources/human-agency-analysis-chatgpt.md` · `wiki/concepts/failure-cost-asymmetry.md`

**In the product.** Goal intake ends with "This is your path until ⟨date⟩." Changing course before that date goes through a declared detour, not a rewrite. At the date the user chooses: continue, re-map, or **Retire**. Retire archives the goal with a one-line lesson and replaces "Start over".

**Research report (2026-10-01 update).** This independently backs the retire option. The report names **goal-persistence bias** as a design risk ("Product incentives often favor keeping goals active"; pausing, narrowing and stopping must be "legitimate outcomes"). It also says any review "must end in a decision: continue, increase, simplify, change cue, remove friction, seek support, pause, or stop. A graph without an action is decorative analytics." Source: `wiki/sources/evidence-based-goal-achievement-system.md`.
**Inference:** the commitment-window date is the natural place for that decision. It gives Goal Map one review point without building the weekly reflection that `PROJECT.md` rules out.

**Evidence check (primary source).** **Holds, and the support is stronger than the report implied.** Gollwitzer & Sheeran found if–then plans had medium-to-large effects on *disengaging from failing goals*, not only on persisting (fewer studies there). Wang et al. note that mental contrasting leads people with low expectations to let go, and treat that as a feature. Retire is a researched outcome, not just a kindness. Separately, the RevenueCat reactivation essay ("users reactivate when the problem comes back") suggests a retired goal is not a lost customer. The next goal is the return.

**Closer to the milestone?** Yes. It stops the mid-route re-planning that never converges.

**Effort** S. **AI** No.

### 6. Turn real mechanics into laws of the world

**Idea.** A camouflaging constraint turns a property that could read as a flaw into a stated law of the world, and it holds only if it "survives being explained." The Attractor Zone did this with its real difficulty curve: "the Zone is generous at first, and that is how it keeps you." On setbacks as plot, the vault has two supporting notes. Rowling: failure "meant a stripping away of the inessential". Miyazaki: harsh stretches balanced with moments to "come up for air".

**Sources.** `wiki/concepts/constraint-as-camouflage.md` · `wiki/projects/attractor/attractor-zone.md` · `wiki/answers/why-origination-is-harder-than-execution.md` (Rowling quote) · `wiki/sources/miyazaki-guardian-interview-2024.md`

**In the product.** The drift rule (3 unmarked off-route steps) becomes a law the traveler knows: "the path waits three days before it grows over." A declared detour becomes "a side trail the map remembers." These are written as rules in the story voice and are literally true of the code. **Inference:** this also lets the drift banner speak in the story's voice without an AI writing it, which keeps "no AI-written drift messages" (PROJECT.md) intact.

**Closer to the milestone?** Yes. A rule the user can predict is a rule they can plan around.

**Effort** S. **AI** No.

### 7. Craft over compulsion, with feedback while the decision is still open

**Idea.** Two families of "hard to put down". "**Craft mechanisms** make the next attempt genuinely attractive. **Compulsion mechanisms** make stopping feel costly." Streak-loss pain, forced waits and manufactured scarcity belong to the second family, which the note calls "a loan against the game's future." Persistence comes from autonomy, competence and relatedness, not reward schedules (Jansz et al., N = 7252). Referral incentives went *negative* when players already felt autonomous. The Attractor feel spec adds a timing rule: feedback must arrive "**while the decision is still open**, not as an epilogue."

**Sources.** `wiki/concepts/compulsion-vs-craft.md` · `wiki/concepts/self-determination-theory.md` · `wiki/sources/persistence-gaming-sdt-jansz.md` · `wiki/concepts/intrinsic-motivation.md` · `wiki/projects/attractor/feel-spec.md`

**In the product.** A review checklist for every engagement mechanic: no streak counter, no "your traveler is sad you left", no chapter that expires. Drift signs show on the map *as the steps drift* (the footstep sits visibly off-trail at check-in), not only in the banner after the third day. **Inference:** the same rule decides the paywall. See Tension C.

**Research report (2026-10-01 update).** The report brings habit research to the no-streak rule. A habit is a context–response association, not a streak. Formation times reported: medians of 59–66 days, individual estimates from 4 to 335 days. So: no 21-day promises, never reset to zero after a miss, and "absence should not erase accumulated learning." It also names **shame loops**: binary streaks and red overdue counts "transform evidence into self-judgment." Source: `wiki/sources/evidence-based-goal-achievement-system.md`.

**Closer to the milestone?** Yes. It keeps return visits about progress rather than guilt.

**Evidence check (primary source).** The habit numbers are **confirmed exactly** (Singh et al. 2024: medians 59–66 days, individuals 4–335). Two limits: the evidence covers simple health behaviours only, mostly at high risk of bias, and the review does **not** directly test "never reset after a miss". That rule is plausible design, not a finding from this paper. One finding the report missed: **self-chosen habits formed more strongly** than assigned ones. That supports keeping the goal in the user's own words (idea 10), and having the AI propose milestones the user accepts or edits rather than imposing them. Source: `wiki/sources/singh-2024-habit-formation-meta-analysis.md`.

**Effort** S (a discipline more than a feature). **AI** No.

### 8. The first milestone is a crude but complete version of the whole goal

**Idea.** Whole-game learning: engage with a complete, working, junior version before drilling components. Lemarchand's vertical slice is the production twin: one small section at full quality proves the target experience is reachable. The metrics-trap note calls splitting a goal into separately measured parts ("atomization") the thing that "destroys any sense of the 'whole game'."

**Sources.** `wiki/concepts/whole-game-learning.md` · `wiki/sources/A Playful Production Process For Game Designers - Richard Lemarchand.md` · `wiki/concepts/metrics-trap.md` · `wiki/sources/fastai-no-dashboard.md`

**In the product.** One line in the milestone prompt (`lib/prompts/map.ts`): the first milestone should be the smallest end-to-end version of the goal, e.g. "one ugly page live", "one full 1 km run". This also gives story beat 1 its obvious subject.

**Planning-fallacy evidence (2026-10-01).** Supports this from the time side. An AI generating milestones plans from the inside view: it narrates how the goal *should* unfold, which is the fallacy's mechanism. The brief lists the work inside-view plans leave out: setup, coordination, revision, waiting and recovery. Estimating subtasks and summing them gives longer, less biased estimates than estimating the whole. **Inference:** two lines in `lib/prompts/map.ts`. Make milestone 1 the crude end-to-end version, and have each milestone name its hidden work ("includes: finding a gym, buying shoes"). Don't ask the model for durations at all; see idea 9. Sources: `wiki/sources/planning-fallacy-evidence-and-product-implications.md` · `wiki/concepts/planning-fallacy.md`.

**Closer to the milestone?** Yes. It makes the first milestone reachable in days, which starts the momentum loop.

**Effort** S. **AI** Uses the existing milestone job.

### 9. Forecast-and-check: predict the effort, then see your calibration

**Idea.** Research craft as a trainable habit: forecast an outcome before acting, check your hit rate, and log hypothesis → expectation → result. "Research speed is mostly the speed at which you discover you're wrong."

**Sources.** `wiki/concepts/research-craft.md` · `wiki/sources/how-to-be-good-at-research-vivek.md`

**In the product.** When a milestone becomes active, ask "How many sessions do you think this takes?" At the milestone, show forecast vs. actual. Over several milestones the user sees their own planning bias. *(Superseded 2026-10-01: the planning fallacy now has its own concept note and a primary source; see below.)*

**Research report (2026-10-01 update).** One caution applies: **false precision**. The app should not show its own completion probabilities; the report prefers "scenario ranges, confidence labels, and stated assumptions," and bars AI from fabricating "confidence about completion dates." Source: `wiki/sources/evidence-based-goal-achievement-system.md`. **Inference:** this idea survives, because the forecast is the *user's*, and the app only shows the user's own forecast against the actual result. It would break if the app started predicting.

**Planning-fallacy evidence (2026-10-01). This idea now has a primary source, and it changes the design.** Buehler, Griffin & Ross (1994), Study 4:
- People who only **recalled** similar past tasks before forecasting stayed as optimistic as people with no prompt (38% vs 29% finished on time).
- People led to **link** that past to the current task lost the bias (60% on time, average error 0.1 days).
- So *showing* forecast vs. actual, as written above, is the recall condition. On its own it may change nothing.

**Revised idea:** at the next milestone's forecast, show the last result *and ask the linking question*: "Your last milestone took 9 sessions; you guessed 4. What's likely to be similar this time?" Then take the forecast.

Two more points from the evidence:
- Half of Buehler's thesis writers missed even their **worst-case** date, so ask for a range (likely and safe), not one number.
- Count **sessions or check-ins** (active effort) separately from **calendar days** (elapsed). The brief says mixing them up blocks learning.

**Cold start:** a new user has no history, and the brief warns against forecasts from thin data. Until there are about two finished milestones, show nothing but the user's own guess. Don't fill the gap with an AI estimate. **Inference:** that also keeps this inside the three-AI-jobs rule, since all of it is code over stored check-ins. Sources: `wiki/sources/buehler-griffin-ross-1994-planning-fallacy.md` · `wiki/concepts/planning-fallacy.md`.

**Closer to the milestone?** Yes, indirectly: later milestones get better-sized plans.

**Effort** S–M. **AI** No.

### 10. Keep the traveler's first words: the past-self layer

**Idea.** Memory reconsolidation: every recall rewrites the memory, and "often-told stories are the *least* faithful". So the original motive drifts every time it is remembered. Self-continuity is the drive to keep a felt connection with earlier selves. Kept verbatim, the day-1 record becomes an anchor.

**Sources.** `wiki/concepts/memory-reconsolidation.md` · `wiki/concepts/self-continuity.md`

**In the product.** `Goal.rawText` is shown untouched when the goal is created, at each milestone, and at the summit ("On the first day you wrote: …"). Optionally the user restates the why at a milestone and sees both side by side.

**Closer to the milestone?** Somewhat. **Inference:** it re-anchors the chosen path at exactly the points where drift or quitting is most likely. The evidence is about memory, not goal completion.

**Effort** S. **AI** No.

### Engaging but off-purpose

These came up, are well supported in the vault, and don't by themselves move a user toward the next milestone. Keep them as retention or distribution layers, not engine features.

- **Shareable map and one retellable peak.** Recommendation is identity expression, and "a byproduct of genuine play value, not a lever you can pull with mechanics bolted on top." People retell what they felt at the emotional peak, so design the summit moment as the peak. A shared image must pass the comprehension floor (a stranger can read it). Sources: `wiki/concepts/recommendation-as-identity.md`, `wiki/sources/why-players-recommend-games.md`, `wiki/concepts/emotional-memory.md`, `wiki/concepts/comprehension-floor.md`, `wiki/concepts/network-effects-vs-wom-diffusion.md`. Effort M, no AI. Strongest distribution idea in the vault.
  **Roger Chen (2026-10-02 update).** Lobby's best invite feature was a *group picture*: a countdown everyone sees, so people pose together, producing a watermarked boomerang they posted to their stories. Two details carry over. The artifact is made at a natural moment of the experience, not on request, and its subject is something the user is proud of, so sharing is identity expression rather than a favour to the app. **Inference:** Goal Map's equivalent is a map image made at a reached milestone or the summit, which matches the planned Plus sharing points in `PROJECT.md`. What doesn't carry over: Lobby prompted the picture with a button that lit up every 5–10 minutes and random-time one-minute calls. Those are engagement prompts that `wiki/concepts/compulsion-vs-craft.md` and `PROJECT.md`'s "leads back to the next milestone" rule would block.
- **Mastery-gated easter eggs on the map.** Rewards comprehension rather than completion; players who find them "become evangelists". Source: `wiki/concepts/easter-eggs-as-design.md`. Effort S–M.
- **A companion whose relationship deepens.** The character-AI note's retention pillars (consistency, memory made visible, relationship arc). Source: `wiki/concepts/ai-agent-personality-design.md`. See Tension E for why this is risky.
- **Land revealed as you walk (fog of war).** No vault support beyond one mention; see Tension B.
- **Wonder and "come up for air" moments** in the art (Miyazaki). Source: `wiki/sources/miyazaki-guardian-interview-2024.md`.

---

## 2. Tensions: where the vault argues against the current design

### A. "A traveler who walks while you work" rewards time, and the product says success is milestones

*The notes say:* when a measure becomes a target it stops measuring the thing (`wiki/concepts/metrics-trap.md`). `wiki/sources/fastai-no-dashboard.md` warns that AI "optimizes metrics too effectively." Flow vs. workaholism: long hours can be compulsion wearing intrinsic clothing (`wiki/concepts/flow-state.md`, `wiki/concepts/intrinsic-motivation.md`).

**Inference, what they suggest.** Let the traveler *animate* during a session (ambient feedback) but *advance on the map* only from check-in outcomes: on-path steps, milestones, cleared blockers. Minutes should never buy distance. Otherwise leaving a timer running becomes the optimal play, and the map lies.

**Research report (2026-10-01 update).** It agrees and names the failure **metric substitution**. "Focus minutes" should be secondary, since "a 20-minute episode that resolves a crucial uncertainty may matter more than two uninterrupted hours of low-value work." Its north star is verified progress per goal, not task or time volume. Source: `wiki/sources/evidence-based-goal-achievement-system.md`.

**Evidence check (primary source).** Harkin et al. add the mechanism behind this. **Monitoring behaviour changes behaviour, and monitoring outcomes changes outcomes**, not the other way round. Goal Map has both sensors: footsteps (behaviour) and milestones (outcome). **Inference:** keep both visible and don't let one stand in for the other. Footsteps say "I'm showing up", milestones say "it's working". Moving the traveler only on outcome events is consistent with this.

### B. Fog of war hides the one thing the design says must always be visible

The current `docs/DESIGN.md` makes the summit visible "from the first day". Whole-game learning argues for seeing the whole before the parts (`wiki/concepts/whole-game-learning.md`). The situational-awareness note makes a subtler point: the interesting asymmetry is information "not hidden — it is merely unattended-to" (`wiki/concepts/situational-awareness.md`). Wicked-vs-kind: hiding feedback makes an environment more wicked, and harder to learn in (`wiki/concepts/wicked-vs-kind-learning-environments.md`).

**Inference, what they suggest.** Fog over *texture*, never over *destination or route*. The summit and the trail stay drawn. What's revealed as you walk is the land's detail: names, landmarks, the look of places you've been. Exploration then rewards having walked, without hiding where you're going.

**Second update — the cozy report agrees, from a different direction.** "Vast spaces eliminate a sense of safety by being unknowable"; coziness comes back with a bounded refuge inside the large space, "like a campfire in the middle of a wood" (`wiki/sources/project-horseshoe-2017-coziness.md`). Hiding the destination makes the map's world unknowable. Fog over texture, with the route and summit always drawn, keeps the walked part as the familiar, safe region.

### C. Paying for engagement risks charging for the worst day

Worst-day design says the system must work when things are bad (`wiki/concepts/worst-day-design.md`). Compulsion-vs-craft says a mechanism must give "a reason to return," not "a penalty for leaving" (`wiki/concepts/compulsion-vs-craft.md`). Overjustification: extrinsic layers can corrode intrinsic motivation, including at the recommendation layer (`wiki/concepts/intrinsic-motivation.md`).

**Inference, what they suggest.** Your own rule already forbids selling "things that can be enjoyed without progress". Add a second rule: **never sell the thing a stuck user needs.** Help when stuck, the worst-day step and the drift warning stay free. Paid tiers deepen what progress *produces*: richer story beats, map art, landmarks, archive and export, multiple goals. One unverified data point from the vault: subscription apps ~14% D30 vs. 5.4% for ad-supported (`wiki/sources/web-game-distribution-and-retention-2026.md`, third-party figures).

**Second update — benchmarks and an ethic.** RevenueCat 2026 replaces that single figure (`wiki/sources/revenuecat-state-of-subscription-apps-2026.md`; vendor data, its customers only):
- **AI apps sell but don't stick:** higher trial conversion (8.5% vs 5.6%) and 41% more revenue per payer, but lower 12-month retention on every plan (annual 21.1% vs 30.7%). Goal Map is an AI app, so it starts on the wrong side of that gap. Retention has to come from goals reached, not from the AI being impressive.
- **Day zero decides:** most trial starts and most trial cancellations happen on the day of download. Task J4 (a head start and one step for today) is the most commercially important task in `TASKS.md`.
- **Hard paywall vs. freemium:** about 5× better download-to-paid with the same year-one retention, *but* the founder says freemium is right when free users drive word of mouth. The vault's strongest distribution idea is the shareable map, which is word of mouth. **Inference:** a free first goal, then paid, fits both the data and the distribution plan better than a hard paywall.
- **Price anchors:** $9.99 a month, $29.99–$39.99 a year. Don't use the report's "Productivity" category: it means design and developer tools, not goal apps.

The cozy report states the "never sell the thing a stuck user needs" rule almost word for word: "Don't be the doctor who poisons their patient and then sells the cure." Sell what meets real needs, and don't create needs in order to sell against them (`wiki/sources/project-horseshoe-2017-coziness.md`).

### D. An AI storyteller vs. "don't outsource the reflection"

The Dan Koe source explicitly bans outsourcing the morning reflection to AI. The ingest reads this as a task "where getting an answer easily defeats the point" (`wiki/sources/fix-your-life-in-a-day-dankoe.md`). Post-institutional meaning-making warns that personalized AI reflection "can validate a bad decision as readily as a good one" (`wiki/concepts/post-institutional-meaning-making.md`). Representation-shapes-the-solution: "Automating the artifact destroys the mechanism" when the value is in the making (`wiki/concepts/representation-shapes-the-solution.md`). The Attractor decision found a replay beat an LLM motivational line (`wiki/decisions/decision-log.md`).

**What they suggest.** The AI narrates *events*, never *meaning*. The user's own check-in sentence is the canonical record. The story quotes it, doesn't paraphrase it, and never tells the user what their journey means. Combined with idea 1, this keeps the AI as a mirror of logged fact, not a validator.

### E. A companion traveler vs. autonomy

SDT's open question: "Does autonomy survive an AI that adapts to keep the player engaged?" The same note names the failure: an AI "optimized for engagement can *simulate* need satisfaction" (`wiki/concepts/self-determination-theory.md`). The intrinsic-motivation note also asks whether being *watched* turns an autotelic activity into a performance (`wiki/concepts/intrinsic-motivation.md`). That applies to you building in public.

**Inference, what they suggest.** Make the traveler a *representation of the user* (their footsteps, their pace), not a separate character with feelings about them. Nothing in the vault supports a companion that reacts emotionally to absence, and B, C and 7 all argue against one.

**Roger Chen (2026-10-02 update).** A founder who *did* build an AI companion arrives at the same line from the other side. Companions read as dystopian when they try to replace real relationships; his rule is to **augment, not replace**, and to use AI "to create context, not content", meaning reasons for people to do and say more themselves. **Inference:** for Goal Map the "real relationship" is the user's relationship with their own work. The traveler and the story should make the user's own record easier to act on, and must never become something the user tends instead of the goal. A quick test for any traveler feature: after it shows up, does the user do more of the work, or more with the traveler?

**Second update.** The cozy report names this exactly: "needy pets, companions, or entities that require constant, non-optional care" are on its list of what destroys coziness, because they create responsibility (`wiki/concepts/coziness.md`).

### F. Focus sessions are exactly the "ceremony" the interface-lag note wants deleted

"The recurring refusal appears to be the session" (`wiki/concepts/interface-lag.md`). The note flags this as a hypothesis from a small number of cases.

**Inference, what it suggests.** Keep the session for *the user's work* (the flow notes support protected time) but delete ceremony from *the app's* part: session start pre-filled from `nextStep` (idea 2), check-in as one line, no setup screens.

### G. A product that works may be opened less (added 2026-10-01)

**Research report.** "A healthy product may reduce its own daily active use as users develop effective routines. Standard engagement optimization can conflict with the product's stated purpose." It recommends **fading support**: once a start cue works on its own, reduce prompting to test whether the behavior holds. Its guardrail metrics include compulsive checking, recommendation override rate, and "difference between app engagement and real-world progress." Source: `wiki/sources/evidence-based-goal-achievement-system.md`.

**Inference, what it suggests.** This goes further than Tension C. Pricing by engagement fails at exactly the moment the product succeeds. Revenue should attach to goals and progress (a new goal, a finished map, the archive), never to daily opens. Also: the report's MVP (start cues, protected focus card, weekly route review) collides with `PROJECT.md`'s out-of-scope list (notifications, replanning, weekly reflection). The report describes a fuller product. It is not a spec for the two-day prototype.

**Second update — the market data makes this sharper.** In RevenueCat's churn survey, **"not enough usage" is a top cancellation reason (26–40%)**. A goal app that succeeds by being opened less looks, to a subscriber, like an app they don't use enough. Two things in the same report point to a way through. Reactivation follows the *problem* returning, and the essay recommends letting users **pause instead of cancel**. **Inference:** price and frame Goal Map around *journeys*: a goal, its map, its archive. Make pausing between goals first-class, and make the archive of finished maps the thing that's always there, so value doesn't depend on daily use.

### H. The report's map vocabulary comes from a borrowed-IP prompt (added 2026-10-01)

Two of the report's references are Perplexity threads asking what productivity features a *Marauder's Map*-style app could have, and its closing map metaphors (locked doors, secret passages, footprints, moving hazards) follow from that framing. `PROJECT.md` bans borrowed IP and names Harry Potter as the example.

**Inference, what it suggests.** The mechanics are generic and safe to use: a checkpoint as a footprint, a dependency as a gate. Words or visual motifs that point back to the source are not: footprints *labelled with names*, "secret passages", parchment, an incantation to open the map. When taking anything from the report, keep the function and rename it in Goal Map's own survey-sheet language from `docs/DESIGN.md`.

### I. A goal is a responsibility, and responsibility breaks coziness (added 2026-10-01)

`docs/DESIGN.md` describes Goal Map as "calm, hand-made, kept for yourself", which is a cozy brief. The cozy report defines coziness by what breaks it, and **responsibility** is on that list next to notifications and extrinsic rewards. A goal is a responsibility by definition. Source: `wiki/sources/project-horseshoe-2017-coziness.md` · `wiki/concepts/coziness.md`.

**Inference, what it suggests.** Goal Map can't be cozy all the way through, but it can contain cozy spaces, using the report's own contrast principle: pressure kept *outside the window*, not in the room.
- The **map** is the refuge. Walked land is familiar and safe, and nothing on it decays.
- The **daily check-in** is a safe ritual: *known* (always one line, never an unexpected amount of work), *safe* (no wrong answer), *relaxed* (low mental cost).
- The **drift warning** is where the goal's pressure enters the room. It needs to read as weather seen from inside, not a demand: say it once, quietly, and offer the worst-day step. Harkin's ostrich problem is the reason it can't be skipped altogether: people avoid progress information that feels like judgement, but monitoring only works if they face it.
- **Notifications**, if they ever come into scope, are the report's worked example of how coziness gets broken. Make them opt-in per reminder, with a reason attached.

### J. "Recalculate the route without blame" vs. the commitment window (added 2026-10-01)

The planning-fallacy brief recommends that when reality diverges, the app "recalculate the route and capture the reason instead of marking the user as having failed." Idea 5 says the opposite about the *route*: no rewriting before the commitment date, because mid-route re-planning is how goals never converge. Source: `wiki/sources/planning-fallacy-evidence-and-product-implications.md`.

**Inference, how they fit.** Separate the **route** from the **timeline**. Milestones (what) stay committed until the window closes. Changing them is a detour or a retire decision. Time expectations (when) recalculate freely and without blame, because they were always a forecast. That also matches the Gollwitzer & Sheeran finding that if–then plans rarely make people rigid about *opportunities*, only about the plan's structure.

### K. The decision-point test measures use, not whether strangers want it (added 2026-10-02)

**Roger Chen (2026-10-02 update).** Before Bro was built, the team carried a tappable mockup and used it daily ("a lot of things look good in Figma but it just does not work once you get your hands on it"), then spent a few thousand dollars on TikTok ads to see which concept strangers responded to. His argument: the gap between idea and launch is where teams "go on the wrong path" with no feedback, and ads are fastest *early* (for scaling they get expensive). He also needed a **wedge**: "always there for you" was too vague, so they started with one scenario (texting). Source: `wiki/sources/bro-app-store-roger-chen.md`.

**Inference, what it suggests.** `PROJECT.md`'s decision point (10–20 people for a week, after P1–P3 and J1) tests whether people *use* the product, which ads can't. But testers you recruit yourself have already said yes to you, so the week says little about whether a stranger wants Goal Map at all. The comprehension-floor warning applies too (`wiki/concepts/comprehension-floor.md`): enthusiasm is cheap to collect. Two cheap additions, neither of which changes the plan:
- **A demand check before the test week:** a short screen recording of a real path being drawn, or the founding-offer checkout link, shown to strangers through a small ad or post. Count clicks and purchases, not compliments.
- **A wedge:** pick the one goal type (one playbook) where the rule-checked path is most clearly better than asking ChatGPT directly, the main competitor `PROJECT.md` names, and recruit testers with that goal.

The mockup habit also fits the journey layer: walk through a fake of the land and story daily yourself before building J-tasks.

### Not from the vault, but found while reading: conflicts with `docs/PROJECT.md`

The new layers collide with rules in `PROJECT.md`, which says to stop and ask on conflicts. An AI narrator would be a fourth AI job ("AI does exactly three jobs"). Splitting milestones when stuck is replanning, which is out of scope. Payments and multiple goals are out of scope. Ideas 1, 4 and 6 are designed to fit inside those rules where possible. The rest need an explicit decision to update `PROJECT.md` first.

---

## 3. Two bolder directions

### Bold 1: Goal Map as an anthology world, launched in character

Apply the Attractor Zone move to Goal Map. The marketing becomes a fictional world where every traveler's real journey is one entry. The narrator's voice is constant, the world's laws are the product's real rules (idea 6), and the entries come from real, consented maps: "*⟨Name⟩ left the path for eleven days. The path waited.*" Your own journey is entry one, which fits your plan to use the app on your own reach-people goal. The recommendation notes favour an identity people want to claim over referral mechanics. The comprehension-floor note warns that content least like the product spreads furthest.

**Sources.** `wiki/projects/attractor/attractor-zone.md` · `wiki/concepts/constraint-as-camouflage.md` · `wiki/concepts/recommendation-as-identity.md` · `wiki/concepts/comprehension-floor.md` · `wiki/concepts/network-effects-vs-wom-diffusion.md`

**Risks.**
1. Attractor's never-break-character rule conflicts with an honest "this app helped me" claim. You'd need to decide where the fiction ends. The attractor-zone note already records this friction with the tester outreach plan.
2. Using other users' journeys raises consent and privacy questions. No note covers this.
3. Fiction can cover up a weak product. Enthusiasm and comprehension are "independent measurements, and enthusiasm is far cheaper to collect" (`wiki/concepts/comprehension-floor.md`).
   *Second update:* Harkin et al. found progress monitoring worked better when results were **reported or made public** (`wiki/sources/harkin-2016-progress-monitoring.md`). That supports some shared form of the map. The authors list experimenter demand as one possible explanation, and the evidence is almost all from health goals.
4. Running two in-character worlds splits the attention your memory says went to Attractor.

### Bold 2: Traces of other travelers (asynchronous mutual help)

**Inference built on two notes.** Strangers on *similar trails* leave small traces: "the step that got me unstuck here", a marker at a blocker they cleared. No chat, no feed, no accounts visible to each other. The Miyazaki note records the icy-road story: strangers pushing stuck cars, "a connection of mutual assistance between transient people." The Kojima interview: "Only by venturing out can you meet people by chance or stumble upon unexpected places." This would add a thin network effect to a word-of-mouth product, which the network-effects note lists as an open question worth testing. SDT's relatedness leg is the one solo goal apps can't satisfy. Any mechanic or name from those games stays out; only the feeling is borrowed.

**Sources.** `wiki/sources/miyazaki-guardian-interview-2024.md` · `wiki/sources/kojima-death-stranding-2-ps-interview.md` · `wiki/concepts/network-effects-vs-wom-diffusion.md` · `wiki/concepts/self-determination-theory.md`

**Risks.** Needs accounts, a backend and moderation, all out of scope today. It has a cold-start problem: traces are worthless below a critical mass per goal type, and the note warns network-effect products die "below that threshold, regardless of total user count." Matching "similar trails" would be a new AI job. And it could turn the map into a comparison surface, which pulls against 7 and E.

**Roger Chen (2026-10-02 update).** Lobby gives the cold-start risk a number to aim at. Retention followed one per-user figure: the share of new users with five friends on day one (about 60% where it broke out, about 20% elsewhere). Content marketing made it *worse* by bringing users with no cluster. **Inference:** the equivalent for traces is "a new user's goal type already has enough traces on day one". That argues for launching traces one playbook at a time and seeding each one (your own journey, early testers) before opening it. One point in this idea's favour: Lobby also needed *temporal* density (friends online at the same second); asynchronous traces don't, which removes the harder of its two thresholds.

---

## 4. Notes worth rereading yourself

1. `wiki/decisions/decision-log.md`, the 2026-09-09 adaptive-director entry. The honesty rule behind idea 1, written by you for a different product and a direct fit here.
2. `wiki/concepts/compulsion-vs-craft.md`. A ready-made review checklist for every engagement and paywall decision.
3. `wiki/sources/human-agency-analysis-chatgpt.md` and `wiki/answers/why-origination-is-harder-than-execution.md`. Momentum vs. motivation, and option-collapse. The engine of focus sessions and goal commitment.
4. `wiki/concepts/drama-management.md` and `wiki/sources/mateas-gdc2003.md`. The only architecture in the vault for a story that has an arc without scripting it.
5. `wiki/concepts/worst-day-design.md`. What "help when stuck" should actually do.
6. `wiki/concepts/comprehension-floor.md`. Blind-sample testing, which you'll need the first time you ask whether a stranger can read a shared map.
7. `wiki/concepts/recommendation-as-identity.md`. Why a referral bonus would backfire.
8. `wiki/sources/how-might-we-learn.md`. Guidance in service of the user's real aims, and why "chatbot tutors" fail. The closest vault note to Goal Map's AI-as-coach question.
9. `wiki/projects/attractor/attractor-zone.md`. Before deciding on Bold 1.
10. `wiki/concepts/metrics-trap.md`. Before deciding what makes the traveler move.
11. `wiki/sources/evidence-based-goal-achievement-system.md` *(added 2026-10-01)*. The only evidence-based source in the vault on goal pursuit itself. Its "Decision framework" (seven questions before adding any feature) and its single-mechanism validation tests are reusable for every idea above. The tests measure whether a feature changes behavior, a different question from whether the AI classifies correctly, which is what Task 8's eval harness covers. Both are worth showing in a portfolio piece.
12. `wiki/concepts/implementation-intentions.md` *(added 2026-10-01)*. Everything the primary sources say about if–then plans, including the rehearsal finding and when AI can help.
13. `wiki/concepts/coziness.md` and `wiki/sources/project-horseshoe-2017-coziness.md` *(added 2026-10-01)*. A checklist of what breaks the calm the design spec asks for.
14. `wiki/sources/revenuecat-state-of-subscription-apps-2026.md` *(added 2026-10-01)*. Before any pricing decision. Note the AI-app retention gap.
15. `wiki/concepts/planning-fallacy.md` and `wiki/sources/buehler-griffin-ross-1994-planning-fallacy.md` *(added 2026-10-01)*. Before writing the milestone prompt or any time estimate.
16. `wiki/sources/bro-app-store-roger-chen.md` *(added 2026-10-02)*. Before the decision-point week, and before anything social (sharing, Bold 2).

---

## 5. Evidence check: the research report against its primary sources (2026-10-01)

| Report claim | Verdict | Primary source |
|---|---|---|
| If–then plans: d = .65 across 94 tests | **Confirmed.** Also helps people disengage from failing goals | Gollwitzer & Sheeran 2006 |
| MCII g = 0.336; "interactive" beats document-only | **Number confirmed; meaning overstated.** "Interactive" was a human experimenter, not software. Bias-corrected g ≈ 0.24 | Wang et al. 2021 |
| Habit medians 59–66 days, individual 4–335 | **Confirmed.** Simple health behaviours only; most studies high risk of bias. Self-chosen habits stronger | Singh et al. 2024 |
| "Never reset progress after a missed day" | **Not in this source.** Plausible design rule; traces to other work | Singh et al. 2024 (mentions in passing) |
| Monitoring: 138 RCTs, d = 0.40; recorded and public stronger | **Confirmed.** Plus: behaviour monitoring changes behaviour, outcome monitoring changes outcomes | Harkin et al. 2016 |
| Ready-to-resume plan reduces attention residue | **Confirmed** (small lab samples; via press release, paper paywalled) | Leroy & Glomb 2018 |
| …so resuming from a checkpoint is faster | **Not tested by the study.** Extrapolation | Leroy & Glomb 2018 |
| (New) Rehearsing a plan beats a reminder note: 87% vs 40% | **Single study**, reported inside the meta-analysis | Gollwitzer & Sheeran 2006, p. 108 |
| *Planning-fallacy brief:* connecting forecasts to past experience eliminated the bias | **Confirmed, with a key detail:** recall alone did nothing; only explicit linking worked (60% vs 29–38% on time) | Buehler, Griffin & Ross 1994, Study 4 |
| *Planning-fallacy brief:* segmentation reduces underestimation; reference-class forecasting depends on comparable cases | **Not checked** (Forsyth & Burt 2008; Cantarelli et al. 2026) | — |

**Cross-finding (inference).** Two independent literatures show the same thing: rehearsing an if–then link beat holding a reminder, and linking past experience to the current forecast beat recalling it. **Information about yourself changes behaviour when it is tied to the current situation, not when it is stored or displayed.** For Goal Map, that means the record (footsteps, past forecasts, worst-day steps) should be *brought into* the moment of decision with a short question, not just kept on a screen.

**What this changes in the ranking.** Nothing moves. Idea 3 gets *stronger*: the if–then core is the best-evidenced idea in the document. Its AI role gets *narrower*: check plan quality, don't stand in for a human coach. Idea 2 stays because it's cheap and harmless, but should be pitched as letting go of the task, not as restarting faster, until Goal Map measures that itself. Idea 5 (Retire) gains real support.

**Still unverified:** the report's procrastination figures (the 2018 treatment meta-analysis), its interruption review (247 publications), and its just-in-time adaptive intervention (JITAI) reviews. Those were not fetched.

**Worth adding to the vault**, given the gaps above: none of the core areas remain empty. The planning fallacy was filled 2026-10-01 from the user's brief, verified against Buehler et al. 1994. Lower priority: story structure beyond the hero's journey (only if the narrator gets built), deep work, and consent and privacy (only for Bold 1 or 2). Cozy design and subscription pricing were added 2026-10-01. *(Procrastination was on this list. The research report now covers it at secondary level. A primary source, e.g. the procrastination-treatment meta-analysis it cites, would make it firmer.)*
