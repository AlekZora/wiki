# Decision Log

Important decisions with context and reasoning. Most recent at the top.

Format: date · decision · why · trade-offs considered.

---

## 2026-09-23 — Basic Game replatforms to Roblox; the Zone is demoted from distribution strategy

**Decision:** Ship target becomes a **Roblox experience**. One throwaway web prototype per candidate verb (TypeScript + Canvas, unpublished) is kept as the loop *instrument*. The Attractor Zone is retained as tone and format canon but **demoted from distribution strategy**. The anthology becomes an in-game retention mechanic rather than marketing. Timeline withdrawn pending re-scope. See [constraint-sheet.md](../projects/basic-game/constraint-sheet.md); the web sheet is preserved at [constraint-sheet-WEB-SUPERSEDED.md](../projects/basic-game/constraint-sheet-WEB-SUPERSEDED.md).

**Why:** The Zone has **3 followers and 50 likes**. Yesterday's 0.8 joined the game to it on the argument that doing so would start Phase 2 with an audience — an assumption that was never checked and is false. Checking it removed both the case for the web-plus-Zone plan and the strongest objection that had been raised against Roblox, namely that Roblox would discard an existing distribution asset. There was no asset. What remains is the structural point: on the web you must build a game *and* an audience from zero as one person, and only one of those is the problem worth solving; Roblox discovery is competitive and opaque but it exists.

**The supporting finding, which was stronger than expected:** Roblox's 2026 algorithm reportedly rewards **session return rate within 24h**, **sessions-per-user-per-day above 1.2**, and **short repeatable loops over long sessions** — two 12-minute sessions outrank one 45-minute session. That is this project's Gate 0 sentence written by someone else. On the web, retention buys portal placement; on Roblox it buys the audience. Horror is also a large category there and the 90s-Goosebumps register is well matched to the population.

**Trade-offs considered:**
- **D8–28 is the grading window and a one-verb arcade loop cannot reach it.** Roblox states it moved *off* 7-day proxies toward optimising D1, D2–7 and D8–28. This is a design objection, not a platform one, and it is answered by making the **anthology a mechanic**: one experience, short self-contained fables, new episodes over time. Each episode stays basic; the anthology carries D28. Recorded as 0.9 and now the binding design constraint. Notably the format that makes it good horror is the format that survives the algorithm.
- **Revenue was raised as a motivation and the arithmetic does not support it at achievable scale.** DevEx converts at $0.0035/Robux, Roblox takes 30% of gamepasses, and ~800 concurrent players is the reported threshold for US minimum wage; 1,000 concurrent with conservative monetization is $360–$720/month pre-tax. So Roblox monetization is a consequence of scale rather than a route to it. 0.2 therefore stays **reach, not revenue** — the platform change does not change the payout decision, and the reported conclusion that placement outweighs the DevEx rate says the same thing.
- **Cold start is unresolved and may cost money.** Ads and organic ranking are separate systems and the reported bootstrap is paying for players whose behaviour then feeds organic ranking. The "free audience" may not be free. Carried as an open risk rather than assumed away.
- **New toolchain is the largest schedule uncertainty.** Studio and Luau are unknown, 3D is a different production problem, and Attractor's quality came from frame-level physics tuning that a canvas gives and Studio may not. Mitigated by keeping the web prototype as the instrument, so no Studio time is spent on an unproven verb — and by testing **sub-second restart in Studio in the first hours, not the last**, since the entire craft list rests on it and it is unproven on this platform.
- **Timeline withdrawn rather than re-guessed.** The previous calendar costed a known stack. Putting a number on an unknown one would be fiction dressed as a plan. Only Phase 2a remains costable (2–3 days per candidate). Re-scope trigger is the first Studio spike.
- **Content moderation for horror on a platform with a young population is unchecked** and is a real constraint on the Zone's tone. Flagged in 0.4 as required before Phase 2, not at submission.

**What this says about the method:** backward chaining did its job late rather than never — the chain's top link (payout, then channel) was derived from an unverified audience assumption, and the error propagated all the way down to stack and iOS seams before anyone checked the number. The cheap check that would have caught it — *how many followers does the Zone actually have* — was never asked. Logged in [backward-chain-game-design](../concepts/backward-chain-game-design.md) as a failure mode of the method: it verifies portal terms rigorously and is silent about verifying your own assets.

**Not yet locked:** 0.4 technical envelope unfilled and deliberately not guessed; 0.3's Roblox column unverified against Creator Analytics; timeline; episode cadence; whether a persistent cross-episode layer is needed or is scope creep. Project still unnamed. **Gate 0 is not clear.**

**Status:** Active — agreed 2026-09-23. Supersedes the platform half of 2026-09-21 and 2026-09-22; the experience-goal ordering, generation filter and metric-trap discipline from those entries survive unchanged.

---

## 2026-09-22 — Basic Game ships inside The Attractor Zone; Phase 0 metrics signed off

**Decision:** The basic game ships as a **second entry in The Attractor Zone**, not as its own world. 0.3 metric floors signed off in full (60% replay rate, 4+ runs/session, 3+ min median, 20% D1, read only above 200 sessions). Gate 0 rewritten as a reach sentence. Theme ideas sealed unopened until Phase 4. See [constraint-sheet.md](../projects/basic-game/constraint-sheet.md) §0.8.

**Why:** The Zone is already running with two fables live since 2026-09-14 across five platforms in a proven ~24s format. Under a reach goal, starting Phase 2 with an audience rather than from zero is the entire argument. Three sequential prototype releases map onto three fables, which is the form the Zone was built for.

**Trade-offs considered:**
- **The obvious objection is that joining imposes the Zone's tone on Phase 1 — theme constraining mechanic, the thing 2026-09-21 rejected.** Examined and rejected: the Zone's rule is an ordinary person, a rule, and you got exactly what you reached for. That constrains the *cruelty structure* — failure must be self-caused — not the verb. And self-caused failure is the legible-failure property the craft list in [compulsion-vs-craft](../concepts/compulsion-vs-craft.md) wants for retention reasons entirely independent of the fiction. The Zone narrows Phase 1 in the direction Phase 3 would have pushed anyway, so it is a **productive constraint**, not an inversion. Recorded as a hard generation filter rather than a preference.
- **Anthology vs sequel.** Attractor's feeling is temptation and the moment you fail to stop. A second entry with the same feeling is a sequel and the anthology collapses into one fable told twice. Binding consequence: the Phase 1.0 experience goal must be a *different* route to getting exactly what you reached for. This is now the tightest constraint on Phase 1 and the likeliest place for the project to go wrong quietly.
- **Sealing the theme ideas rather than using or discarding them.** Julien has theme ideas already. Held in mind they steer generation invisibly; written down and sealed they cannot. The second purpose is that comparing the sealed ideas against the theme *derived* at Phase 4 is the falsification test [backward-chain-game-design](../concepts/backward-chain-game-design.md) currently lacks — if they match, the derivation added nothing.
- **Metric floors set by comparison, not derivation.** Accepted knowingly; with no revenue to solve back from there is nothing to derive from, and the sheet says so rather than dressing comparison up as derivation.

**Not yet locked:** 0.6 (iOS seams) is proposed and is the only remaining Gate 0 sign-off. Whether the game keeps its own name inside the Zone, Zone posting cadence, our load-time budget, and portal review latency all remain open and are deliberately non-blocking. Project still unnamed.

**Status:** Active — agreed 2026-09-22. Gate 0 clears on 0.6; Phase 1 begins with the experience goal.

---

## 2026-09-21 — Basic Game Phase 0: reach over revenue, stacked channels, no tester pool

**Decision:** 0.2 payout is **reach, not revenue** — v1 is not required to pay for itself, ad integration leaves the critical path. 0.1 channel is **stacked and non-exclusive** — self-host plus itch.io plus CrazyGames, Poki deferred. 0.5 stack is **TypeScript + Canvas2D + Vite**, with telemetry promoted to critical path from Phase 2. 0.7 replaces the tester pool with **instrumented public releases fed by story-led TikTok**. Phase 2 becomes **three sequential public releases** rather than a private bake-off, and each candidate's story is **derived from its verb after Phase 1**, never before. See [constraint-sheet.md](../projects/basic-game/constraint-sheet.md).

**Why:** Verification against primary sources invalidated the channel table the sheet was built on. Neither Poki nor CrazyGames publishes a revenue percentage — Poki's terms are per-game and negotiated, CrazyGames' are "objectively quantifiable criteria" with no number. Poki additionally requires **five-year web exclusivity** and hand-picks after playtests, which no third-party guide mentioned; CrazyGames requires none and composes with itch and self-hosting. Separately, CrazyGames pays on **net** — gross minus VAT minus Direct Game-related Costs fixed at 20% minus distribution fees — so every headline percentage in circulation overstates the effective take, and the revenue equation needed `share × (1 − 0.20 − fees)` rather than a single multiplier. Against that, and [north-star.md](../mission/north-star.md)'s framing of game work as compounding audience and skill, a revenue target on a first basic game would be a target set to be missed.

**Trade-offs considered:**
- **Losing the Poki ceiling.** Poki plausibly offers the largest audience, and stacking forecloses it for now. Accepted because a five-year exclusivity on an unproven game is the wrong direction of commitment, and because Poki cannot be planned around — it is hand-picked, not applied for. Explicitly deferred rather than rejected; revisit at Gate 5.
- **Declining the CrazyGames two-month exclusivity bonus** (+50% compensation). Rejected because it costs itch and self-host reach during exactly the launch window, which under a reach goal is backwards.
- **Dropping the tester pool.** This is a strict improvement on the protocol it replaces: [comprehension-floor](../concepts/comprehension-floor.md)'s binding constraint was scarcity, and public traffic removes the ceiling while eliminating observer inflation. The cost is a confound that must be held permanently — **TikTok measures the video, not the game**, and per the Wukong finding in [network-effects-vs-wom-diffusion](../concepts/network-effects-vs-wom-diffusion.md) the content that travels furthest is the content least representative of the product, so a story that performs brilliantly says *less* about the loop, not more. Mitigation: two instruments never blurred, and a candidate that spreads well but retains badly is still a kill.
- **Schedule.** Sequential public releases cost roughly nine days against a private bake-off. Five weeks to launch, six with buffer, against an original 2–4 week target. Accepted knowingly for the anthology compounding — three shots at one audience, each entry building the next, a retired entry reading as an episode rather than a failure, which is the form [attractor-zone.md](../projects/attractor/attractor-zone.md) already argues for. If the deadline later matters more, the lever is candidate count, not the depth pass.
- **Story-before-mechanic rejected.** Writing the story first would pull design toward what is narratable rather than playable, the exact failure backward chaining exists to prevent. The Attractor precedent settles the ordering: the Zone fiction was read out of the physics afterwards.
- **Metric targets are proposals, not derivations.** With no revenue to solve back from, 0.3's numbers are set at "good enough to build an anthology around" rather than derived, which is weaker than the method intends and is flagged as such in the sheet.

**Not yet locked:** 0.3 floors unsigned; 0.4 envelope not transcribed; 0.6 iOS hooks not chosen; TikTok signal-vs-noise threshold undefined; CrazyGames payout threshold discrepancy (€100 FAQ vs €80 terms) unresolved; project still unnamed. **Gate 0 is not cleared.**

**Standing gap:** D7 is where ad-supported games die and no instrument in this plan sees it. Carried forward openly rather than dropped.

**Status:** Active — 0.1, 0.2, 0.5, 0.7 agreed 2026-09-21; 0.3, 0.4, 0.6 pending.

---

## 2026-09-21 — Basic Game: derive backward, execute forward; project lives in this vault

**Decision:** Adopt a backward-chained pipeline for the basic-game project — derive payout → channel → metric → experience goal → session → loop → verb → theme, then execute in the forward direction — with six phases and kill gates. See [pipeline.md](../projects/basic-game/pipeline.md). The project lives in this vault rather than in the separate `creative-wiki`, and the framework was rewritten into this vault's conventions and against its existing concepts.

**Why:** Web portal constraints are published, non-negotiable and early-binding (50MB initial payload, must land directly in gameplay, mandatory SDK events), so they are cheap to satisfy on day one and expensive to retrofit. More importantly the revenue decomposition — plays × sessions-per-player × ads-per-session × eCPM × rev-share — shows sessions-per-player is the only term that is both controllable and compounding, and portals promote what retains, so retention is also upstream of plays. The stated goal and the economics select for the same variable.

**Trade-offs considered:**
- **Backward chaining cannot generate a game, only filter one.** Guarded by ordering taste ahead of metrics and by citing [metrics-trap](../concepts/metrics-trap.md) rather than restating it. If this guard fails the method produces a compliant, boring game.
- **Compressed preproduction.** Lemarchand holds that rushing preproduction causes most project failures, and Phase 3 gets five days. Accepted only because a single-mechanic game's vertical slice is the game, so the phases collapse rather than one being cut. The residual risk is the skipped slice gate, so Gate 3 was written as a vertical-slice gate with a naive player hitting the experience goal at final quality as its first condition.
- **Theme decided last.** Risks thin theming. Counter-evidence in-vault: the Attractor Zone fiction was derived from the mechanic after the fact and is not thin.
- **Proxy testing instead of cohort data.** Five testers is an anecdote and no proxy plausibly predicts D7. Accepted because the schedule cannot produce cohort data at all; superseded by first-party numbers the moment they exist.
- **Separate vault rejected.** It duplicated concepts this vault already owns and sat away from `projects/attractor`, this log, and [north-star.md](../mission/north-star.md).

**Not yet locked:** revenue model (deliberately deferred to Phase 0.2, and "reach, not revenue" is a live answer given the north star's framing of game work), channel, stack, project name. The constraint sheet is unfilled, so Phase 1 has not started.

**Status:** Active — framework agreed 2026-09-21; Phase 0 pending.

---

## 2026-09-14 — Distribution channel resolved: The Attractor Zone, storytelling not promotion

**Decision:** Attractor's distribution channel question (open since 2026-09-11) is resolved.
Rather than market the game directly (dev-diary posts, "check out my game" links, the drafted
Reddit legibility test), the user is building a fictional anthology-horror world around it —
**The Attractor Zone** — and running it as an in-character social media series. The game keeps
its own name and stays live on itch.io; the Zone is the fiction wrapped around it. Full spec:
`wiki/projects/attractor/attractor-zone.md`.

**Why:** the story is already latent in the mechanic, not invented for marketing. Attractor is
about temptation and about the moment you fail to stop. Nothing in the game is random — spike
paths are fixed, and the only force pulling danger toward the player is the player's own held
finger — so every death is self-caused. That is the Twilight Zone ending structurally: you got
what you reached for. The game's actual difficulty curve (generous for ~30 seconds, then it
turns) becomes true in-fiction rather than needing to be explained: the Zone is generous at
first, and that is how it keeps you.

**Form:** Twilight Zone for tone, Goosebumps for rhythm, no protected material from either.
Fixed template — an ordinary person meets a rule the world runs on, and gets exactly what it
promises — repeated with a new person each time, same law, narrator cold/flat/unexplaining.
Three formats: micro-fables (3 lines, close on "[Name] has entered the Attractor Zone"), Rules
of the Zone (single-line laws), and ~24s vertical video episodes (serif title cards → gameplay
→ closing line, tape hiss throughout). Accounts under the handle **attractorzone** on TikTok,
X, Bluesky, Instagram, YouTube — **never break character, never reveal a person made the game.**

**What this does and doesn't settle:**
- Does not reopen the store question. No store stands (2026-09-11 entry, below); itch.io
  remains the only place the game itself is hosted and played.
- Does not itself specify how a viewer gets from a Zone post to the itch page — no link
  mechanism has been decided. Flagged as open in `attractor-zone.md`.
- The prior legibility test (does the mechanic read from a silent clip to a stranger) was
  designed as a direct ask-in-your-own-voice post (the drafted Reddit copy) — that form is
  incompatible with an account that never breaks character. The underlying question is *more*
  relevant now, since video episodes are themselves silent gameplay clips, but it needs a new
  test method. Not solved by this decision.
- The prior outreach ask (go back to the ten existing testers for one share each,
  `outreach-copy.md`) is not explicitly superseded — it's a direct, in-your-own-voice ask,
  which sits oddly next to an in-character-only strategy. Left for the user to decide rather
  than assumed either way.

**Status:** Active — decided 2026-09-14. Supersedes the "distribution channel OPEN" status of
the 2026-09-11 entry below (the store portion of that entry, no store, still stands).

---

## 2026-09-11 — Google Play rejected, Apple deferred; distribution channel OPEN

*Archived here from `memory/MEMORY.md` on 2026-09-11 during the hot-cache restructure.
**Corrected 2026-09-11** — an earlier version of this entry recorded "distribute as an iOS
home-screen web app" as a decision. It was not. That was Claude's recommendation, made in one
message and never agreed to by the user. The user's actual decisions are the two store
rejections below; the replacement channel is undecided. See "Not decided" at the end.*

**Decision:** No store for now. Google Play is **rejected**. Apple is **deferred** — and if a
store ever happens it is Apple, because that is where the audience actually is.

**How this moved in one day, in three steps:**

**(a) Apple → Google Play.** The user judged the App Store costly and premature. Play compared
favourably on two axes: **$25 once vs $99/yr**, and **no native rewrite** — Apple Guideline 4.2
was the expensive part of that path (see the 2026-09-09 entry), whereas Play is permissive and a
TWA-over-PWA is Google's own recommended route. Play rejects lazy wrappers (no splash screen, a
back button that instantly exits, a blank page when the network drops) and Attractor dodges all
three *structurally*: one self-contained HTML file, zero external refs, no network dependency at
all. It needed only a splash screen, a history-aware back button, and a manifest + service
worker — an afternoon, not SpriteKit.

**(b) The gate that killed it.** Personal Play accounts created after **2023-11-13** cannot even
*apply* for production until **12 testers have been opted in continuously for 14 days** — any
dropout resets that tester's clock — then ≤7 days of review. Source:
`support.google.com/googleplay/android-developer/answer/14151465`. So **Apple charges money;
Google charges an audience.** Exemptions exist (a pre-2023-11-13 personal account, or an
organization account) but both were ruled out: there is no evidence a Play account was ever
created, and the organization route needs a D-U-N-S number that can take **up to 30 days** —
longer than the 14-day test it would avoid — on an exemption that is only an *inference from
Google's silence*, never something Google states. Full check: `wiki/projects/attractor/outreach-copy.md`.

**(c) The fact that decided it.** Ten people had already tested Attractor, played it, and liked
it — **all on iOS**. Everyone around the user uses iPhones. Play's gate requires 12 testers *on
Android*, so satisfying it means recruiting 12 strangers on the wrong platform — a harder task
than the campaign it was supposed to enable. **Play was only ever attractive on price; once
audience became the deciding factor it inverted from cheapest route to hardest first step.**

**Trade-offs considered:**
- **No store discoverability.** Accepted — organic store discovery was never the plan; the
  4–6 week campaign was.
- **The corrected Play ordering, kept in case Android ever matters:** testers install *through*
  Play, so the $25 account and the wrap are prerequisites for *starting* the 14-day clock, not
  the step after it. Opt-in is to the **track, not a build**, so updates ship to testers
  mid-test without resetting anyone — meaning the gate would have run *parallel* with
  development, not after it. Recruit 16–20, not 12, against dropout.
- **Watch item:** Android developer verification will cover all apps on certified devices,
  sideloaded APKs included (Brazil/Indonesia/Singapore/Thailand from 2026-09-30, global 2027),
  so handing out an APK stops being a free escape hatch. A no-fee hobbyist/student flow is
  promised but unspecified.

**Still open, and not solved by any of this:** the **legibility question**. All ten testers
*played*, which means all ten saw the button label, the hint and the legend — they were told the
mechanic, so they cannot answer whether it reads from a clip. That still needs strangers watching
video, and it still matters because the campaign premise rests on it. A Reddit post attempting it
was silently removed for low karma on 2026-09-11; karma gates apply to posts, not to comments in
existing threads, so the venues are r/IndieDev's weekly megathread, itch.io's To Dev / Feedback
board, Feedback Friday threads, and Discord.

**NOT DECIDED — the replacement channel is open.** Both stores are out and nothing has replaced
them. The user's stated constraints are: move fast, the game is ready, and the reachable audience
is on iOS. itch.io is already live and remains the only channel actually in use.

One option was *proposed by Claude on 2026-09-11 and has not been accepted*: distribute as a web
app on its own URL, installable via iOS Add to Home Screen (Vercel for hosting, since the game is
iframed on itch's domain so the manifest could not be ours; plus a manifest and service worker).
The argument was that a ~20-second-run arcade game converts better as a tapped link than an app
install, and that nothing would be wasted if a store happened later. **Recorded here as an open
option only.** Do not treat it as the plan, and do not build toward it without the user's
agreement.

**Status:** Partially decided — the two store rejections are firm as of 2026-09-11. The
distribution channel is OPEN. Supersedes the iOS App Store plan of 2026-09-09.

---

## 2026-09-09 — Untangle chosen over Unfold and Little Garden, then parked the same day

*Archived here from `memory/MEMORY.md` on 2026-09-11 during the hot-cache restructure.*

**Decision:** Untangle was selected as the weekend distribution-skills test, then **parked the
same day** when Attractor was judged further along and took the slot. Parked *before* the user's
build guide arrived. Do not start it unless unparked.

**Scope, as decided:** explicitly a **distribution-skills test, not a product.** Mechanic: move
anchors to separate overlapping ribbons until no crossings remain. Experience goal — "the player
voluntarily immerses and walks away satisfied."

**Why Untangle over the two alternatives — content economics, not fun:**
- **Unfold** had the better hook ("you want to see what it becomes") but every object is
  authored art: zero replay after the first solve, and the hardest build of the three.
- **Little Garden** has no endpoint without inventing arbitrary goals.
- **Untangle generates itself:** build a non-crossing layout, then scramble the anchors. Solvable
  **by construction**, infinite content, zero authoring, and one difficulty parameter (node
  count). Planned graft: on the last crossing resolving, the ribbons settle into a recognizable
  form — keeping Unfold's reveal, procedurally.

**The deliberate anti-decision:** *not* "compelling like 2048." That fork was considered and
rejected — a game designed to both relax and compel has a conflict at its centre, with Flappy
Bird as the cautionary case. Success metric is **people put it down feeling better**, NOT session
length or retention; optimising those builds a compulsion loop in calm clothing. Therefore no
streaks, no leaderboards, no score (overjustification effect).

**Trade-offs considered:**
- **Shallow on the "hard to master" axis** — abandons the mastery half of the elegance framework.
  Accepted, and it means no long-tail retention and no mastery community.
- **Open caution, never resolved:** neither 2048 nor Flappy Bird had engineered virality, so the
  distribution hypothesis (channel, expected result, window) must be defined *before* building.
  "Ship and watch" teaches little.

**Design grounding:** `wiki/concepts/elegance-game-design.md` · `flow-state.md` ·
`affect-circumplex.md` (unwinding = positive valence + LOW arousal; 2048 = positive valence +
HIGH arousal) · `intrinsic-motivation.md`

**Status:** Parked 2026-09-09. No code written.

---

## 2026-08-01/02 — Locale question reopened: NO decision; the output is a criterion, not a candidate

*Archived here from `memory/MEMORY.md` on 2026-09-11 during the hot-cache restructure. Recorded
deliberately as an **open question**, not a decision — it amends nothing in the 2026-07-24 entry
below, which stands.*

**Status of the question:** OPEN. The candidate locale named in the 2026-07-24 entry (the road
from Troezen to Athens) was **not** locked and is now argued against. Player-character identity
is also reopened.

**The actual output — a selection criterion:** the locale needs a **stable cast that travels.**
Stable cast so Template 3 callbacks accumulate; travel so new pressure arrives without the
generator having to invent it. Both halves are load-bearing, and they eliminate the prior
front-runners:
- **Theseus's road fails the first** — the cast resets at every encounter.
- **Ithaca / the *Odyssey* fails the second** — a siege is static. (The user's objection,
  accepted.)

**Front-runner, in discussion only: the Argo.** The ship is a persistent cast; the ports are a
content generator; the ~50-name roster is mostly canon-blank, which is exactly the slack the
generator needs. **Not yet stress-tested** — every other candidate broke under one round of
pushback and the Argo has not had one. That test is the next move on this project.

**Player identity also reopened.** A possible third option is a **catalogue name** — canonically
named, zero canonical content — instead of the "nobody" fixed in the 2026-07-24 entry. This
*would amend* that entry if adopted. **NOT adopted.**

**Two working files produced, neither a decision:**
- `wiki/projects/game/canon-safe-missions.md` — where a player can act inside fixed myth. Six
  kinds of "slack"; a mission catalogue; the **variant-seam mechanic** (the player decides which
  *attested* version gets told); and a fourth outcome type — succeeded-and-it-changed-nothing /
  failed-and-that-is-the-record. Implies fact-DB additions: an `events.immutable` flag, a
  `variants` table, and seeding entities from myth catalogues.
- `wiki/projects/game/locale-selection-open.md` — the locale exploration itself. OPEN.

**Next session on this project:** stress-test the Argo → decide identity → only *then* consider
locking a locale. Does **not** change the build step, which remains Step 8.

**Status:** Open — no decision made. Deliberately left unresolved 2026-08-02.

---

## 2026-08-12 — blackwater.db source of truth: UNDECIDED, and must be settled before Q6

*Archived here from `memory/MEMORY.md` on 2026-09-11 during the hot-cache restructure. Full
narrative detail is in `wiki/projects/game/build-log.md`; this is the decision stub.*

**The problem:** two divergent databases, neither a superset of the other.

| File | Contents |
|---|---|
| `~/blackwater-wiki-archive.db` | 13 quests, 6 validated (archived vault copy, 122,880 bytes) |
| `~/side-quest-ai/prototype/blackwater.db` | 8 quests, 2 validated (live) |

Rows 1–6 agree. **Rows 7–8 have opposite validation outcomes** — same templates, same trigger,
different results, which is what running one pipeline against two separate databases produces.
`blackwater.db` was gitignored and therefore never version-controlled, which is how this
happened.

**Why it must be decided:** Step 8 (Q6) treats generated quests as experiment *data*. The repo's
current copy is not "the" history — it is whichever file happened to be on disk. The archive is
the larger sample (13 vs 8), so the choice should be made deliberately rather than inherited.

**Status:** Undecided as of 2026-09-11. Blocks Q6 using quests as data. Project is parked.

---

## 2026-09-09 — The adaptive director is barred from ranked play; renamed to Attractor

**Decision (a):** The game is called **Attractor**, renamed from Magnet.

**Decision (b):** The adaptive spawn director runs in **endless mode only**. Ranked and daily
challenge use a fixed, identical course for every player. Ship order: **v1 has no director**
(juice, haptics, persistence, an offline-generated wave table replacing seed 71, and a daily
challenge on a date-derived seed with a Game Center leaderboard). The **director lands as v1.1,
mid-campaign.**

**Why (a):** "Magnet" is generic, unsearchable, and likely contested. Attractor is clear on the
App Store — the destination and the place a collision actually hurts. Two same-name projects
exist on itch.io, judged irrelevant: itch URLs are account-scoped (`alekzora.itch.io/attractor`)
and traffic will arrive from Reddit links, not itch search. Name collisions only cost you when
you depend on organic discovery on that platform. Bonus: "attractor" is the real
dynamical-systems term, which supplies something to talk about later.

**Why (b):** A reviewer of the plan caught a genuine contradiction — Game Center leaderboards
and live adaptive difficulty had both been recommended, and they are incompatible. If the
director shapes each player's run differently, scores are not comparable and the leaderboard is
decoration. The fix is mode separation, not abandoning either feature.

The sequencing argument turned out to matter more than the design one: six-week campaigns die in
week four because everything got spent on launch day. Holding the director back creates a second
news beat exactly when the campaign needs one — and *"we added an AI that shapes your run, and
here's why it's locked out of ranked"* is a better story than launch-day noise, because the
integrity constraint is itself interesting.

**The invariant that makes an adaptive director honest** (this was the design crux):
the director has **authorial control over the setup and zero control over the resolution.**
It chooses what spawns, where, and when — before the object exists. Once a hazard is in flight
its physics are untouched: never moved, never slowed, never deleted, never a resized hitbox.
Same shape as the Side Quest AI rule that the LLM reads world state but never writes it.

Composing a near-miss (spawning on a trajectory that was always going to pass close) is level
design. Nudging a hazard aside at the last moment is cheating, and players smell it. Related
distinction: **consistent generosity is a mechanic, adaptive generosity is a lie** — a fixed
80ms coyote window is a rule; one that secretly widens when you're struggling is a betrayal.

The test: *if the player read the design doc, would they feel cheated or interested?* Since the
whole plan is build-in-public, that stops being hypothetical — anything that would feel weird to
explain in a clip shouldn't be in the build.

**Trade-offs considered:**
- **Is the director patronising / rubber-banding?** (User raised this; it is the right question.)
  Resolved: the target is ~65% wave survival, so it steers you toward death a third of the time
  and pushes *harder* on good players. It is a pressure regulator running both directions, not a
  safety net. What it actually fixes is dead air — runs where nothing is near you and holding is
  free, so there is no decision to make. Better framing than "manufactures near-misses":
  **it guarantees the hold/release decision is always live.** The near-miss is the symptom of a
  good decision moment, not the goal.
- **Marketing phrasing tension, unresolved.** "Manufactures your near-misses" is the punchier
  line *and* the one that implies outcome control, so it invites exactly the cheating objection.
  Punchy-with-an-answer-ready vs. accurate-up-front is still a live choice.
- **The reviewer's closing either/or was rejected** — "equal challenge and leaderboards" vs.
  "adapts to each player" is a false choice that mode separation dissolves.
- **The reviewer's scope was rejected too**: ranked play, personalised practice curricula and
  competitive infrastructure describe a mature product, not a game that currently has no sound.
- **Where the reviewer was right and earlier advice was wrong:** the leaderboard/adaptive
  conflict, "AI proposes, validator disposes," and a practice-replay of the death moment being
  more useful than an LLM-generated motivational line — and needing no AI at all.
- **Daily challenge was the buried lede**, mentioned once in passing and underrated: fair
  competition, retention loop and content engine at once, since everyone plays the same course
  today and clips become comparable. Cheap too — derive the seed from the date, no backend.

**Status:** Active — decided 2026-09-09.

---

## 2026-09-09 — Single-track on Magnet; App Store ship is the setup, the campaign is the work

**Decision:** Park **everything** except Magnet, temporarily. Side Quest AI (at Step 8) and the Untangle prototype are both suspended. Magnet — the existing hold-to-attract arcade prototype at `~/.codex/.chatgpt-projects/.../magnet-site`, repo `github.com/AlekZora/magnet` — becomes the sole active track: refine it, ship it to the iOS App Store, and run a 4–6 week distribution campaign around it.

Explicitly adopted framing: **shipping to the App Store is not the goal, it is the setup.** The real work is the campaign. Magnet was chosen as the vehicle because the near-miss moment is inherently clippable and the "AI director manufactures your close calls" angle supplies something to *say*, not just a link to post.

**Why:**
1. **Distribution is the known weakness and it needs a real trial.** roastmycvai.com worked technically and failed on distribution. That failure has never been directly attacked. A small, finishable game is the cheapest possible instrument for attacking it.
2. **Magnet is small enough to finish.** Game logic is ~18 lines. The gap between prototype and shippable is measured in weeks, not quarters — so the calendar goes to distribution rather than to building.
3. **The AI angle is genuine, not decoration.** The adaptive director (player model → controller targeting manufactured near-misses) is a real mechanic *and* the marketing hook *and* content in itself.
4. **Single-tracking removes the three-way split.** Side Quest AI + Untangle + Magnet across a six-month runway was the actual risk.

**Trade-offs considered:**
- **Side Quest AI loses momentum at Step 8.** Accepted as temporary. Step 8 (Q6 experiment protocol) and the two unresolved items — the divergent `blackwater.db` source-of-truth question and the dead Build Log Rule scope — are frozen in place, not cancelled.
- **Untangle is superseded as the distribution test.** It was scoped for exactly this purpose; Magnet now serves it and is further along. Untangle parked before the build guide arrived.
- **App Store Guideline 4.2 (Minimum Functionality) is a live rejection risk.** An 18-line single-mechanic game with no sound, persistence, or progression gets bounced — and a WKWebView/Capacitor wrapper compounds it as "repackaged website." Mitigation: native rewrite (SpriteKit favoured over Godot on binary size and signing friction), and the juice/persistence/progression/director work is treated as a *submission prerequisite*, not polish.
- **Campaign abandonment is the real failure mode**, not a bad plan. Someone whose weakness is distribution stopping in week 2 is the thing to guard against — hence a held cadence and a success metric defined before launch rather than rationalised after.
- **Blocker inherited from the prototype:** the ChatGPT export wrapper's CSP (`connect-src blob: data:`) and `sandbox="allow-scripts"` (opaque origin) forbid all network calls *and* `localStorage`. Extraction from the wrapper is step zero regardless of path.

**Status:** Active — decided 2026-09-09.

---

## 2026-07-24 — Greek mythology as the game's world foundation

**Decision:** The Side Quest AI game will use **Greek mythology** as its world and content foundation. The player is an original mortal — a "nobody" by mythic standards — living in the margins of the canonical myths. The famous hero-arcs (Heracles' labours, Jason's voyage, Theseus' road to Athens, etc.) run as fixed canonical backdrop; the AI generates the *player's* side quests around them. The target "disorienting recognition" moment is reframed as: the mythic world notices someone it had no reason to notice.

**Why:** Three structural fits with the system we have already built — not aesthetic preference:
1. **Ready-made relational world-model.** The myth corpus (anchored on Apollodorus's *Library*, ingested 2026-07-23 → see [genealogy-as-knowledge-graph](../concepts/genealogy-as-knowledge-graph.md)) is already a consistent entity/relationship fact database. The hardest part of the grounding/simulator layer — a rich, internally consistent world for the LLM to read but never touch — arrives pre-built.
2. **Genre is natively variant-tolerant.** Greek myth exists in multiple contradictory canonical versions ("according to some… according to others…"). The characteristic failure mode of generative narrative — plausible but non-canonical content reading as a hallucination — is *licensed by the genre* instead of breaking it.
3. **Myth's moral engine already IS the experience goal.** Xenia, hubris/nemesis, oaths remembered and enforced years later, delayed divine consequence — "the world is paying attention to your specific behavior" is the native grammar of the genre (cf. Nessus's delayed-payload gift; Theseus's forgotten black sail).

Bonus: public domain (no license); the "wow" moment is self-explanatory to outsiders (shared cultural context = distribution leverage against our known distribution weakness).

**Trade-offs considered:**
- **Tone / content curation (biggest risk).** Source material is pervasively dark (rape, child-murder, cannibalism, mutilation); an LLM sampling the corpus will drift there. Requires an explicit tone decision (leaning stylized / mythic-abstract) plus a curation layer on the generator.
- **Scope creep.** The corpus is an encyclopedia and tempts abandoning the vertical-slice discipline. Mitigation: scope the demo to ONE bounded locale with one canonical arc as backdrop. Candidate (NOT locked): the road from Troezen to Athens (Theseus's road-clearing chain) — linear, bounded, known fixed landmarks.
- **Two-tier canon burden.** Immutable "everyone knows this" spine vs. mutable margins. Maps cleanly onto our existing constraints (main story human-authored and fixed; NPCs cannot resolve main beats) and the renderer/simulator/planner split: canonical events = fixed simulator facts; player side-story = planner output. The validator must encode the canonical spine.
- **Crowded setting** (Hades, AC Odyssey, God of War…). Accepted: our differentiator is the *mechanic*, not the setting; a familiar backdrop makes the novel mechanic read more clearly.
- **Player = hero vs. nobody.** Chose nobody: player-as-hero collides with the hero's fixed canonical arc, leaving no room for a generated personal story; player-as-nobody is both mechanically freer and thematically truer to the genre.

**Not yet locked:** specific locale, player-character specifics, tone treatment. This does **not** change the current build step — still Step 7 (Godot setup). Setting work begins after the engine bridge is running.

**Status:** Active — direction agreed 2026-07-24; specifics pending.

---

<!-- Template:

## YYYY-MM-DD — <Decision title>

**Decision:** 

**Why:** 

**Trade-offs considered:**
- 

**Status:** Active / Reversed / Superseded by [link]

-->
