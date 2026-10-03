# MEMORY — hot cache

Only what is needed to resume work right now. Restructured 2026-09-11 (was 307 lines).
Everything removed was archived, not deleted — see the pointers at the bottom.
Synced with auto-memory 2026-10-03 (projects other than Goal Map and Side Quest removed). Previous sync 10-01.


## Active: GOAL MAP — current build (confirmed 2026-10-01)

Web app that turns one personal goal into a living map and shows, day by day, whether you're
still on the path you chose. Goal → AI proposes 3–7 milestones → code draws the map → one line
a day, AI classifies it, code places a footstep → 3 unmarked off-route steps in a row trigger a
gentle drift warning. Two-day prototype and AI-engineering portfolio piece.

- Code `~/projects/goal-map/` (Next.js + TS) · `github.com/AlekZora/goal-map`
- Rules `docs/PROJECT.md` · visual spec `docs/DESIGN.md` · plan `docs/TASKS.md`
- Tasks 1–6 and **P1 (path design: intake questions, playbooks, planPath pipeline)** done and
  pushed 2026-10-01 (`7cd08dc`). Plan model Sonnet 5.5 via `LLM_PLAN_MODEL`. **Next: P1b**
  (TASKS.md order updated 10-02: P1b → P3 → P4 → W → G → GE → P2 → visual direction → J1–J3 →
  7 → H → S → J4 → 8 → 9). Playbooks are drafts awaiting Julien's review.
- **One copy per document (2026-10-03).** Specs (PROJECT/TASKS/DESIGN, `docs/design/`,
  `docs/prototypes/`) live only in the repo. Everything else lives in the vault:
  `wiki/projects/goal-map/` (hub `overview.md`, research, design-references, testing, launch,
  ideas, build log), plus Goal Map entries in `wiki/decisions/decision-log.md`. The
  `wiki/projects/goal-map/docs` symlink points to `/Users/alekozoranov/Projects/goal-map/docs`
  and is Mac only. Never copy spec text into the vault; link through the symlink. The repo's
  `docs/research/wiki-synthesis.md` is now a pointer to the vault answer.
- **Real vault = `~/Vaults/wiki` (git, pushed to AlekZora/wiki).** The iCloud copy at
  `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/` is being retired by the user
  (Obsidian Sync moving to B). Don't touch it.
- Vault research: `wiki/answers/goal-map-feature-inspiration.md` (09-29),
  `wiki/answers/goal-map-wiki-synthesis.md` (10-01, ranked top 10 + evidence check)
- **Going to be a product** (decided 2026-10-01). PROJECT.md's out-of-scope list is prototype
  scope; product ideas that collide with it need a PROJECT.md decision.
- The CLAUDE.md Build Log Rule covers `~/projects/goal-map/` (on disk it's `~/Projects`,
  capital P; the filesystem doesn't distinguish case).
- Synthesis checked against 7 primary sources 2026-10-01 (section 5, evidence-check table).
  New concepts: implementation-intentions, coziness. Planning fallacy added the same
  day (concept planning-fallacy); no core research gaps open.

## Wiki focus: AI and AI agents, not games (decided 2026-10-03)

The user is moving the wiki away from games, back to AI and agents. Deleted the same day:
`CLAUDE-reference.md`, `CLAUDE-creative.md` and top-level `game/synthesis.md`. CLAUDE.md was
updated: the lens centres on agents, a 6th lens question was added (failure modes and
evaluation), and the creative slash commands and the Attractor build log were removed.
`wiki/creative/` and `wiki/projects/game/` (Side Quest) were kept. The mission path still says
"→ game projects →", unchanged until the user decides.

## Removed projects (2026-10-03)

At the user's request, every project except Goal Map and Side Quest AI was deleted from the
vault and memory: Attractor, Basic Game, Untangle, FutureX and the film project. Deleted:
`wiki/projects/attractor/`, `wiki/projects/basic-game/`, `wiki/projects/_archive/FutureX/`.
The code folders `~/attractor/` and `~/untangle/` were deliberately kept (`~/attractor` has
unpushed commits). Wiki pages, the decision log and CLAUDE.md's Build Log Rule still mention
them in places.

**PARKED:** Side Quest AI. Do not resume unless explicitly unparked.

## Side Quest AI — still parked, but the state moved (Sept 2026)

Parked for feature work. Three things changed since 2026-09-14 and the old shorthand is wrong:

- **DB migrated SQLite → Postgres (Supabase) 2026-09-16**, directed one-off, verified live
  (schema + seed idempotent, `pipeline.py` matches the old SQLite run, `/health` returns
  `npc_count: 7, tick: 50`). `quest_generator_v4.py` not run — it spends API tokens. The two
  old divergent `blackwater.db` SQLite files still exist and still disagree (13 quests / 6
  validated archived, 8 in the repo copy), but that is now **only a Q6-corpus question**, not
  a live-app question.
- **More shipped 2026-09-16→19 than "frozen at Step 8" suggests:** semantic retrieval
  (embeddings + cosine, replacing keyword matching), `npc_beliefs` with contradiction handling,
  Docker + GitHub Actions CI, a confidence/similarity trust gate on the semantic path, and the
  `player_action` knowledge-boundary fix with a regression test. All in git and in
  `~/side-quest-ai/MIGRATION-NOTES.md`.
- **Step numbering is retired** (2026-09-20). It came from `docs/build-log.md`, which stopped
  in August and never covered the September phases — so "Step 8, currently active" was
  pointing at a sequence the repo had already passed. Removed from the README rather than
  renumbered. Don't revive it without backfilling first.

**Nearest real work if unparked:** close the open `MAIN_QUEST` half of the knowledge-boundary
leak (needs C8/HC11 + world_texture's zero-main-quest rule — *not* the knowledge-row rule that
closed `player_action`, which can't work since `MAIN_QUEST` is tied to no `event_id`), then
re-verify the Godot client against Postgres. The client has not run since the migration; it was
last verified 2026-08-05, against SQLite.

**Caveat on the build logs — corrected 2026-09-22, there are two and they diverge:**
`~/side-quest-ai/docs/build-log.md` is a frozen duplicate left by the 2026-08-12 reorg, last
entry 2026-08-12, **zero September entries** — that is the file the retired Step-8 numbering
came from. The live one under the CLAUDE.md Build Log Rule is
`wiki/projects/game/build-log.md`, which has three September entries (09-11 snapshot, 09-16
migration, 09-20 README correction). The earlier note that "its only September entry is the
migration" was true when written and is now wrong; the residual gap is narrower — the 09-16/17
phase work (semantic retrieval, beliefs, Docker/CI) and the 09-18/19 knowledge-boundary work
have no entries of their own. Explicitly not backfilled, flagged for whenever the project unparks.

## Recent sessions — wiki thread, 2026-09-19/21

Four sessions of vault work. Concepts extracted from existing material
rather than new sources: `constraint-as-camouflage`, `comprehension-floor`, `interface-lag`
(09-19), then the answer `inventing-outside-your-field.md` and the concept
`outsider-advantage.md` (09-20). Core claim of the latter: the outsider advantage is **imported
depth applied to a wicked domain**, not ignorance.

**09-21 — two of that answer's own open questions closed**, written into the same file (new
`## Two of the open questions, answered` section; struck through in both the answer and
`outsider-advantage.md`, which carried the identical pair). Q1, a pre-entry wicked/kind test:
partial yes — delay and non-repetition are inspectable from outside, **misleadingness is
retrospective by construction** (it needs a counterfactual); the probe is research-craft's
forecast-and-check run on *other people's* attempts, disambiguated against insiders' own hit
rate. Q3, how much substrate: **no threshold exists** — it is three requirements (source depth
/ target history / target method), marked by RPD's cascade-of-caveats (prototypes vs. a rule
list) and measured in the *source* domain. **The join is the real result:** one probe measures
both and cannot separate them, and both answers end at bounded entry with pre-committed kill
criteria — so the gate is not "measure first" but "make entry cheap enough to be wrong about
both." Directly relevant to the mission's three-domain-entry path, still unassessed.

Open threads, left deliberately:
- `sampling-period` and `late-specialization` still unextracted from `range-epstein.md`.
  Undecided whether one page, two, or folded into `outsider-advantage`.
- Unrun: which *other* April 2026 ingests declare concepts in frontmatter that were never
  created. Two found so far, both from the 2026-04-10 ingest day, both invisible to any search
  starting from `concepts/`.
- Never discussed: running the three filters (wicked-or-kind, transferable substrate, tar pit)
  against the mission's own AI → games → assistant → space path, which is three domain entries
  in a row. `outsider-advantage.md` deliberately marks this **unassessed** rather than
  endorsing it.

## Where the detail lives

- Side Quest AI — all build steps, schemas, file and code paths, Step 8 plan:
  `wiki/projects/game/build-log.md`
- All decision reasoning, by date — The Attractor Zone / distribution resolved (2026-09-14),
  Play vs Apple and the web-first pivot (2026-09-11),
  Untangle vs Unfold vs Little Garden (2026-09-09), single-track + campaign framing
  (2026-09-09), adaptive director + ranked split (2026-09-09), `blackwater.db` divergence
  (2026-08-12), locale reopened / the Argo (2026-08-01/02), Greek mythology (2026-07-24):
  `wiki/decisions/decision-log.md`
- Mission, technical profile, runway, secondary goals: `wiki/mission/north-star.md`
- Governing framing (still operative): **the store ship is not the goal, it's the setup — the
  campaign is the work**, starting week one from the ugly version. Full entry: decision log,
  2026-09-09.

Memory system note: this is the vault-visible mirror. The auto-memory copy lives at
`~/.claude/projects/…/memory/MEMORY.md` and is kept in sync — that one is what actually loads
into context at session start.
