# Wiki System — Claude Instructions

This is a personal knowledge base. Its organizing lens is AI, 
and above all AI agents: for every source ingested, the 
primary question is how AI intersects with, changes, 
advances, or could be applied to the ideas in that source, 
and what it teaches about building agents that perceive, 
remember, plan, act and stay trustworthy. The wiki covers 
any topic (science, history, fiction, philosophy, 
engineering, biology, anything). The AI lens is constant.

Focus shifted 2026-10-03: games are no longer a focus of 
the wiki. Older pages written through a game-design lens 
stay, but new work does not default to game framing.

Specific projects live in wiki/projects/ and are 
cross-referenced when relevant but do not define the 
wiki's scope.

## Directory Layout

raw/           — drop zone for unprocessed content
  articles/    — any articles, AI/tech or otherwise
  videos/      — YouTube transcripts, talks, lectures
  games/       — game articles, postmortems, analyses
  books/       — book notes or converted text
wiki/          — processed, interlinked knowledge
  concepts/    — evergreen concept notes
  sources/     — one file per ingested source
  projects/    — ongoing personal projects
  answers/     — researched answers to open questions
  decisions/   — important decisions and reasoning
  mission/     — north star and weekly progress
  index.md     — master index
  log.md       — chronological processing log
memory/        — session state (top level)
  MEMORY.md    — hot cache: current project state

## Mission Context

Ultimate goal: fund and contribute to space exploration.
Path: smaller AI projects → game projects → personal AI 
assistant → space exploration.
Full detail in mission/north-star.md.

## The AI Lens

When ingesting any source — regardless of topic — always ask:

1. How could AI change, advance, or be applied to this topic?
2. What problems in this domain could AI help solve?
3. What does this source reveal about human cognition, 
   behavior, or systems relevant to building AI?
4. Does this source contain patterns or frameworks that 
   could transfer to AI agent design?
5. Where does this source's domain intersect with current 
   AI research or capabilities?
6. What would an agent built on this idea get wrong, and 
   how would you detect it (evaluation, verification, 
   failure modes)?

Note these intersections explicitly in the My Take section 
of every source page and in the AI Integration section of 
every concept page.

## Ingest Workflow

When asked to ingest a file:

### Step 1 — Create source page
Create wiki/sources/<slug>.md using the schema matching 
the content type. Fill all sections. In My Take always 
include at least one specific observation about the AI 
lens — how AI intersects with the ideas in this source.

### Step 2 — Conditional concept extraction
After creating the source page, evaluate:

A. Does this source introduce an idea substantial enough 
   to be reusable across other topics or sources?
B. Does a concept page for this idea already exist in 
   wiki/concepts/?
C. Is the AI intersection specific and interesting enough 
   to add genuine depth to a concept page?

Then act accordingly:

- If A=YES, B=NO, C=YES → create a new concept page
- If A=YES, B=YES, C=YES → update the existing concept page
- If A=NO or C=NO → skip concept extraction

When creating or updating a concept page, frame the concept 
through the AI lens — not through the lens of any specific 
project or domain. If the source is a game article, the 
concept is not a game design concept by default — ask first 
whether it reveals something about intelligence, behavior, 
or systems that applies broadly. Project connections 
(game design, Side Quest Engine, etc.) go only in the 
Project Connections section, and only when the link is 
specific and genuine.

When creating or updating a concept page fill in all 
sections including AI Integration. Never create shallow 
concept pages — only create one if the source has enough 
substance to populate it meaningfully.

### Step 3 — Update log
Prepend one dated line to wiki/log.md, directly under the 
table header row. wiki/log.md is sorted newest first — 
never append to the bottom. The line notes:
- Source title and file path
- Whether a concept was created, updated, or skipped
- If skipped: brief reason (too thin / already exists / 
  not concept-worthy)

### Step 4 — Update index
Add the new source to wiki/index.md.
If a new concept was created, add it to wiki/index.md too.
wiki/index.md is grouped by type and is the lookup view — 
do not re-sort it by date.

### Step 5 — Regenerate the recency view
Run `python3 scripts/recent.py` from the vault root. It 
rewrites wiki/recent.md — every wiki file ordered by date, 
newest first — from frontmatter dates (`ingested:` on 
sources, `updated:` on concepts). Never edit wiki/recent.md 
by hand; it is overwritten on every run.

## Content Schemas

### Article (wiki/sources/)
---
type: article
title:
url:
author:
published: YYYY-MM-DD
ingested: YYYY-MM-DD
tags: []
concepts: []
---
## Summary
One paragraph, own words. No invented facts.
## Key Points
-
## Quotes
>
## My Take
[Always include: how does AI intersect with this topic?]

### Video / Talk (wiki/sources/)
---
type: video
title:
url:
channel:
published: YYYY-MM-DD
ingested: YYYY-MM-DD
duration: HH:MM
tags: []
concepts: []
---
## Summary
## Key Ideas
-
## Timestamps
-
## My Take
[Always include: how does AI intersect with this topic?]

### Game Article / Postmortem (wiki/sources/)
---
type: game-article
title:
url:
game:
author:
published: YYYY-MM-DD
ingested: YYYY-MM-DD
tags: []
concepts: []
---
## Summary
## Notable Points
-
## What It Attempted
## Where It Succeeded / Where It Failed
## My Take
[Always include: how does AI intersect with this topic?]

### Book (wiki/sources/)
---
type: book
title:
author:
published: YYYY
ingested: YYYY-MM-DD
tags: []
concepts: []
---
## Summary
## Key Ideas
-
## Chapter Notes
One entry per chapter: page range, the chapter's argument, 
key points, and verified quotes with page numbers.
## Quotes
>
## My Take
[Always include: how does AI intersect with this topic?]

### Concept Note (wiki/concepts/)
---
type: concept
title:
aliases: []
tags: []
sources: []
updated: YYYY-MM-DD
---
## Definition
Plain language. What this concept actually is.
## How I Think About It
Personal interpretation, intuitions, analogies.
## AI Integration
- How AI changes or advances this concept
- How this concept could inform AI agent design
- What AI applications exist or could exist in this domain
- What this concept reveals about intelligence, behavior, 
  or systems relevant to AI
## Related Concepts
-
## Open Questions
-
## Project Connections
Only if relevant — link to specific project files.

## Linking Convention

- Source files link to concepts: [name](../concepts/slug.md)
- Concept files list sources in frontmatter sources: field
- Slugs are lowercase kebab-case: persistent-memory.md

## Tags

Use lowercase specific tags freely across any domain:
ai, ml, llm, agents, memory, emergence, behavior,
game-design, narrative, physics, biology, history,
philosophy, psychology, engineering, space, economics,
identity, consciousness, creativity, systems, 2d, design,
music, film, language, mathematics, medicine, fiction

## Claude Behavior

- Always infer ingested: as today's date
- Never invent facts not present in the source
- Keep all summaries in plain language, own words
- Apply the AI lens to every source regardless of topic
- Concept extraction is conditional — evaluate each time
- Never create shallow concept pages — substance required
- Do not create duplicate concept files — search first
- Do not default to game design framing — wiki is broad
- Cross-reference projects only when genuinely relevant
- Update memory/MEMORY.md after significant sessions
- Weekly progress goes in mission/weekly-progress.md
- Never overwrite existing files — version alongside
- Existing concept files may be in an old or outdated 
  format (e.g. legacy ## Game Design Vector / 
  ## AI Integration Vector sections from a prior schema). 
  The schema defined in this file is always canonical, 
  regardless of what existing files look like — never 
  pattern-match formatting off existing files, always 
  derive structure from this schema
- If a concept page being updated or referenced is in the 
  old two-vector format (## Game Design Vector / 
  ## AI Integration Vector), normalize it to the current 
  unified schema as part of the edit — merge both vectors 
  into a single AI Integration section, and move any 
  game-specific content into Project Connections. Do this 
  whenever touching the file for any reason, not just when 
  explicitly asked to migrate it

## Build Log Rule
When working on code or prototype tasks in a 
project repo — ~/side-quest-ai/ or 
~/projects/goal-map/ — only 
(not ingestion, not concept extraction, not wiki maintenance):

After completing any build step, append an entry to that 
project's build log with:
- Date
- What was completed
- Files created or modified
- Test results if applicable
- Current step and what comes next

Build log locations (the code lives outside the vault; 
the vault keeps the prose):
- ~/side-quest-ai/ → wiki/projects/game/build-log.md
- ~/projects/goal-map/ → wiki/projects/goal-map/build-log.md
  (added 2026-10-01)

Scope corrected 2026-09-11. The rule previously named 
"code and prototype work inside wiki/projects/game/", a 
directory that has held no code since 2026-08-05, so it 
could never fire.
Never apply to ingestion or wiki synthesis tasks.