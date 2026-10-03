# Goal Map — Build Log

Newest first. Code lives in `~/projects/goal-map/` (`github.com/AlekZora/goal-map`); this file
keeps the prose, per the CLAUDE.md Build Log Rule (Goal Map added to the rule 2026-10-01).

Entry format: date · what was completed · files · tests · current step and what comes next.

---

## 2026-10-01 (late night) — Starting-point question clarified

- **Completed:** the constraints screen now asks "What do you already have for this?" (placeholder
  "e.g. what you've tried, what you have, what's already done"), so the answer no longer invites
  time. The plan prompt labels the answer as the starting point and says it is not available time.
  TASKS.md P1 step 1 updated to match. Files: `components/GoalConstraints.tsx`,
  `lib/prompts/plan-context.ts`, `docs/TASKS.md`. Commit `7cd08dc`. **Pushed** by the user
  the same night (`aa681e0..7cd08dc`, includes both P1 commits).
- **Tests:** 113 pass; build and eslint clean. No model re-run (a label-only prompt change).
- **Next:** Task P2.

## 2026-10-01 (late night) — P1 follow-up: prompts and logging

- **Compared first:** the three P1 cases on Sonnet 5.5 (now `LLM_PLAN_MODEL` in `.env.local`)
  against Opus 5.5, with the same goals pinned. All six paths passed the eight rules on a read; Sonnet
  was about a third cheaper per path. Both models wrote the race itself as the bad-day step, and
  Sonnet put the race-availability check second.
- **Completed:** prompts now say that `worstDayStep` is always a preparation step, even for events;
  that dates are never invented but the user's own deadline may be named; and that a check that can
  end the goal outright goes in milestone 1. Plan logs now split: backcast, risks, goal text and
  check notes only in development; production logs rule pass/fail, counts, tokens and latency.
  Files: `lib/prompts/plan-context.ts`, `plan-draft.ts`, `plan-critique.ts`, `lib/plan.ts`,
  `app/api/map/route.ts`. Commit `cf8d729`, **not pushed**.
- **Tests:** 113 pass; build and eslint clean. Sonnet re-run: the race check is now in milestone 1,
  and every bad-day step is a preparation step.
- **Next:** Task P2.

## 2026-10-01 (night) — Task P1 committed (path design pipeline)

- **Completed:** four optional intake questions (`GoalConstraints`, stored on `Goal.constraints`);
  six draft playbooks in `lib/playbooks/` (Zod-validated, status "draft", for Julien to review);
  `planPath()` in `lib/plan.ts`: draft call (playbook → backcast → pre-mortem → milestones),
  critique-and-revise call against the eight rules (`lib/pathRules.ts`), pure `planChecks` with one
  critique retry. Plan calls use `LLM_PLAN_MODEL` (falls back to `LLM_MODEL`). `lib/prompts/map.ts`
  retired. Commit `9f99c30`, **not pushed**.
- **Tests:** 113 pass (new: planChecks pass/fail fixture per check, plan-model fallback, playbook
  load). `npm run build` and eslint clean.
- **Manual runs** (Opus 5.5 as plan model, Haiku 4.5 for intake): all three acceptance cases met —
  side-project app (crude version → tester installs → blockers fixed → released), watercolor
  (paintings made and shown, not lessons), half marathon in 3 weeks at <2 h/week (feasibilityNote
  present). The critique failed rule 4 / 6 / 7 on the drafts and fixed them; no code-check retries.
- **Not done:** browser check of the constraints screen (no browser tooling); `LLM_PLAN_MODEL` is
  not set in `.env.local`, so the app still plans on Haiku until it is.
- **Next:** Task P2 (review and commit to the path).

## 2026-10-01 (evening) — Task 6 committed

- **Committed** after the user confirmed: `58e491c` "Daily check-in and classification (Task 6)"
  (code only), then `aa681e0` "Product plan and research docs" (PROJECT/TASKS/DESIGN,
  `docs/prototypes/`, `docs/research/`). Fetched first; origin had no new commits. **Not pushed.**
- **Next:** Task P1.

## 2026-10-01 (evening) — Task 6 verified; waiting on browser check and commit

- **Completed:** verified the uncommitted Task 6 work (daily check-in and classification) against
  `docs/TASKS.md`. It was written 09-28/09-30, not in this session. No code changed in this session.
  - `classifyCheckIn` is the single entry point. The output schema rejects milestone numbers out
    of range, missing milestones for on_path/milestone_reached, and detour_deliberate without an
    active detour, so those count as validation failures and get one retry.
  - `CONFIDENCE_THRESHOLD = 0.7` lives in one place (`lib/checkins.ts`).
  - The confirm form, one check-in per local day with edit-to-reclassify, the milestone pulse
    with `prefers-reduced-motion`, and footsteps derived only from stored classifications are
    all present. On reload: `loadState()` on mount, no API calls.
- **Files (uncommitted, Task 6):** `lib/classify.ts`, `lib/prompts/classify.ts`,
  `app/api/classify/route.ts`, `lib/checkins.ts` + test, `lib/classify.test.ts`,
  `components/CheckIn.tsx` + css, `components/GoalAppClient.tsx`, plus changes to
  `GoalApp.tsx`, `GoalMap.tsx`/css, `layout.ts` + test, `schemas.ts`, `app/page.tsx`.
  Separate from Task 6 and also uncommitted: `docs/PROJECT.md`, `docs/TASKS.md` and
  `docs/DESIGN.md` (rewritten 10-01 for the product plan), `docs/prototypes/`, `docs/research/`.
- **Tests:** `npm test` 100/100 pass (7 files). `npm run build` passes. Acceptance check-ins run
  against the real model via `POST /api/classify`:
  - "fixed the login bug" → on_path, m1 'Login works', 0.9
  - "reorganized my bookshelf" → off_route, 0.95
  - "worked a bit" → off_route, 0.3, below threshold, so the confirm UI shows
  - Note for Task 8: the vague case's best guess is off_route, so the confirm form preselects
    "Off the path". Worth an eval case.
- **Current step:** Task 6, the browser check (done by hand, since no browser tooling is
  available) and then the commit.
- **Next:** Task P1 (constraints, playbooks, `planPath` pipeline).

## 2026-10-01 — Log created; state recorded from git (no build work this session)

- **Completed:** nothing built. This log was opened and the current state recorded from
  `git log` and `git status`.
- **Current step:** Task 6, daily check-in and classification. **In progress, uncommitted.**
  New `app/api/classify/route.ts`; modified `app/page.tsx`, `components/GoalApp.tsx`,
  `components/GoalMap.tsx`, `components/GoalMap.module.css`, `lib/layout.ts`,
  `lib/layout.test.ts`, `lib/schemas.ts`, `docs/DESIGN.md`, `docs/TASKS.md`.
- **Tests:** not run this session.
- **Next:** finish and commit Task 6, then J1–J4, Task 7 (detours + drift rule), Task 8
  (eval harness), Task 9 (polish, empty states, README), optional Task 10.
- **Decision recorded:** Goal Map will be a product, not only a prototype (user, 2026-10-01).

## 2026-09-28 — Tasks 1–5 (backfilled from git, not written at the time)

Commits, in order: scaffold (Task 1) · set LLM provider · schemas and storage (Task 2) · LLM
adapter and goal intake (Task 3) · tighten goal intake (Task 3 follow-up) · milestone
generation (Task 4) · note clarify-state UX for Task 9 · the map: design and deterministic
layout (Task 5) · summit follow-ups (clearer upcoming summit, label clear of rings).
Test results from that day were not recorded.
