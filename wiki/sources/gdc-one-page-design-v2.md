---
type: video
title: The Art of the One-Page Design Document
url: unknown
channel: GDC
published: unknown
ingested: 2026-09-22
duration: unknown
tags: [game-design, design, systems, documentation, visualization, cognition, communication, abstraction, engineering]
concepts: [representation-shapes-the-solution]
---

> **Second ingest of the same raw file.** This page is a deliberate re-pass over
> `raw/videos/gdc-one-page-design.md`, written alongside the earlier
> [gdc-one-page-design.md](gdc-one-page-design.md) rather than replacing it, so the two can be
> compared. Differences are substantive, not stylistic — see the note at the foot of the page.

## Summary

Stone Librande, creative director at EA Maxis, argues that the one-page design document beats
every other format he has used in a decade-plus of writing them. He walks through what came
before — the printed design "bible," then the design wiki — and grants each its real strengths
before naming the failure they share: nobody reads them, and the wiki additionally *hides the
relationships* between systems by chopping them into separate pages. His alternative is a
single sheet, as large as the printer allows, dense and visually composed, drawing on
architectural drawings, LEGO instructions, kids' placemats and Minard's Napoleon's-March
diagram. The examples run from Diablo level flow and combat "atoms" at Blizzard North, through
a cardboard-and-sticky-note Springfield built on a table at EA, to Spore's consequence system —
where the format stopped being a way to present a design and became the thing that fixed it.
The strongest claim in the talk is not about communication at all: twice, redrawing a system
changed the system. And the failure case is equally load-bearing — when a design refuses to fit
on one page, Librande treats that as evidence the design is wrong, not that the page is too
small.

*Transcript note: the speaker's name is rendered phonetically as "Stone Le Brandy" throughout
the raw file — an automatic-transcription artifact. The talk is also un-timestamped, and the
recording cuts off mid-Q&A (see Structure and Open Threads below).*

## Key Ideas

**On the formats that came before**

- Design bibles: 100+ pages, printed, bound, authoritative. Real pros — definitive, thorough,
  portable, readable away from a screen. Real cons — don't scale with team size, can't be
  updated once distributed ("I've already printed 20 copies"), hard to search.
- **The bible is not dismissed as a writing process, only as a distribution format.** Librande
  says he *still writes them* — "I just don't show anybody my documents anymore." His reason is
  the sharpest defence of longhand design in the talk: "the act of writing that document is the
  act of designing," because committing a sentence forces a decision you could otherwise leave
  vague in your head. He describes sitting fifteen minutes on a single sentence.
- Wikis: easy to update, whole team can edit, history and attribution for free. But they demand
  constant maintenance, degrade into "a tangled mess of spaghetti," and — the structural
  objection — **they hide design relationships**, because everything is chunked into separate
  pages and a hyperlink "is not really a real connection." Plus screen DPI is far worse than
  print, and the viewport forces every design into an arbitrary rectangle.
- The shared failure: people don't read. Librande cites eye-tracking work — readers check
  headlines, pictures, then the scroll bar, and leave if the scroll bar is too small.

**On what a one-pager is**

- Inspirations are all non-game: architectural drawings (the same sheet serves a client who
  wants the elevation and a contractor who wants stud spacing — **one page, audience-targeted
  layers**), LEGO instructions (wordless, followable by a five-year-old), technical cutaway
  drawings, kids' placemats, and Minard's Napoleon's March (army size as line width, plus
  temperature, dates and river crossings).
- The genesis was an accident: a UI flowchart he drew for Diablo ended up pinned on a
  programmer's wall — someone not even working on that feature, who said "I thought it looked
  cool." The lesson he drew was competitive: *what if documents were things people wanted to
  hang up?*
- "One page" is elastic by design — legal, then tabloid, then EA's wide-format plotters. He
  concedes this is partly a trick and does it anyway.
- Recommended template: a title (if you can't write the title, stop — you don't know what the
  document is for), **a date** (the only way to tell versions apart once printed), generous
  white space, a central illustration to pull people in, call-outs and notes arranged around it.
- Tooling is a firm opinion: Adobe Illustrator, not Photoshop — vector art stays agile under
  rotate/scale/rearrange, files stay small (the entire Springfield map ≈ 2 MB), and printing
  happens at *printer* resolution rather than document resolution.

**The examples**

- **Diablo, act one** (tabloid): every waypoint, monster, model name and AI type
  (melee/poison/electricity), plus expected player level and elapsed time. He calls it "almost
  like a musical score" — a view of the whole game you can never get while playing it. It
  doubles as a testable pacing claim: you should be level 13 at Winterstone; are you?
- **Diablo combat, the "football documents"**: X's and O's reducing combat to its atoms, on the
  premise that Diablo *is* a 2D mouse-clicking exercise — so the design variables are click
  rate, hold duration, and mouse travel. Atoms then recombine into higher-level skills, one page
  each.
- **Springfield**: cardboard boxes and sticky notes on a table in the middle of the design pit.
  Librande counts this as a one-pager — not printed, but a single simultaneous view, and
  deliberately sited where nobody could reach their desk without walking past it. Later became
  plotter-printed maps with ~25 interior one-pagers folded in.
- **Spore's island march**: the Napoleon diagram applied directly — space along one axis, brain
  level and expected time along the bottom, difficulty escalating with distance so players are
  pulled off the starting beach. He makes a general point here: **put time in the diagram**, so
  intended pacing is a design target rather than something discovered after the game is built.
- **The matrix method**: pick the axes, draw the empty grid, then fill it top-down instead of
  solving bottom-up. Once the grid exists, "90% of the design" is done and the rest is detail
  work — "kind of like a crossword puzzle for game designers." Used for real on Spore's cell
  game, and to replace a programmer's (Jeff Gates) bottom-up, case-by-case handling of cell
  interactions with an exhaustive grid he could work through as a checklist.

**The two moments the representation changed the design — the core of the talk**

- **Rock-paper-scissors → sliders.** A robot game had three factions arranged as
  rock-paper-scissors, one per corner. Looking at the diagram, Librande concluded "the diagram's
  drawn wrong," and redrew the factions along the *sides* of the triangle rather than at its
  corners. That single change converted three fixed choices into continuous tunable sliders —
  players could be "mostly scissors with just a little bit of rock," built by part selection.
  **The redrawing did not communicate the design better; it produced a different and better
  design.**
- **Spore's consequence system, 256 → 36.** Four stages (cell, creature, tribe, civ) × four ways
  to play each (skip, aggressive, nice, neutral) = 256 distinct routes into the space stage. The
  four-dimensional spreadsheet was unworkable — "I can barely keep this document in my head."
  Three attempts: a radial "dreamcatcher" diagram that he loved and that was *wrong* (a circle
  implies the ends are adjacent when they are not — the folded-fan error); a 180°-split fan,
  truer but with an unordered colour spectrum that told him something was still off; and finally
  a **vector solution** — each choice contributes a direction, choices sum, and the 256 routes
  collapse to ~36 reachable outcomes. That replaced a hand-typed lookup table with an algorithm.
  Only after solving it did he plot every vector from a common origin, producing the diagram
  that became the project's poster.
- **The diagnostic.** "Sometimes when you start working on these one-page designs you know your
  design is bad because you can't make it into a one-page design... that usually means it's too
  complex, you're just thinking about the problem wrong." Failure to compress is treated as
  information about the design, not about the medium.

**On getting them read**

- Print them and hand them over in person. Explicitly *not* email, *not* a wiki link — "they
  won't."
- Bring pencils to the meeting. These are working documents; the goal is people writing on them.
  He shows a Galactic Adventures mission sheet (one of 64) clean off the printer, then a scan of
  the same sheet days later covered in a designer's annotations, as the success condition.
- In meetings the one-pager creates a common focus: "everybody's imagining the same thing
  that's in front of them," instead of each person picturing their own version of an abstraction.
- Benefits to the designer, independent of whether anyone reads it: it forces you to actually
  understand the problem, forces concision (rank tier 1/2/3; below four-point type, give up),
  exposes relationships as you draw the connecting lines, and — the long Spore example — aids
  problem-solving directly.

## Structure

The raw transcript carries **no timestamps or time markers of any kind**, so the schema's
Timestamps section cannot be filled honestly. What follows is running order, not timing:

1. Intro; design bibles, their pros and cons (Creature Ball 1997, Leisure Suit Larry's Casino,
   Grim Fandango ~70pp)
2. Design wikis; The Simpsons wiki, kept usable by a producer (Hans ten Kate) whose full-time
   job it was
3. The shared failure: nobody reads; eye-tracking and the scroll bar
4. Inspirations: architecture, LEGO, cutaways, placemats, Napoleon's March
5. Diablo: UI flowchart on a programmer's wall, the D-hack prototype, act one, combat atoms
6. The Simpsons: cardboard Springfield, plotter maps, interior one-pagers
7. Template and tooling: title, date, white space, central illustration; Illustrator over
   Photoshop
8. Smaller examples: creature traits, game-loop flowchart, the "bad flowchart" joke, whole-game
   storyboard, Spore's island march
9. Rock-paper-scissors redrawn as sliders
10. The matrix method; Spore cell game; the programmer checklist
11. Spore consequence system: 256 cases → dreamcatcher → fan → vector solution → the final
    diagram
12. Benefits to the team, benefits to the designer, summary
13. Q&A (truncated)

## My Take

The AI reading that this talk most obviously invites — *have a model generate the one-pager* —
is the one the talk itself argues against, and noticing that is more useful than the
application. Librande's claim is that the artifact is a by-product: "the act of writing that
document is the act of designing," and the Spore vector insight arrived *through* the drawing,
across three wrong diagrams, not before it. Automating the artifact removes the process that
produced its value and leaves a picture of a design nobody thought through. The genuinely useful
AI role here is the inverse and much cheaper: **the diagnostic, not the draftsman.** "You know
your design is bad because you can't make it into a one-page design" is a falsifiable
complexity check, and a system that reports *this doesn't compress* is doing the load-bearing
work without stealing the thinking.

The deeper transfer is the rock-paper-scissors moment, which is the best small example I have
seen of [representation acting on a problem rather than depicting
it](../concepts/representation-shapes-the-solution.md). Moving three factions from
the corners of a triangle to its sides converted a discrete three-way choice into a continuous
space — the design changed because the drawing changed. For LLM systems this is not a metaphor.
The structure you hand a model *is* an intervention on what it can produce, not a view onto it.
This is directly live in [Side Quest AI](../projects/game/build-log.md): the pipeline's entire
job is deciding what goes into the `game_state` object an NPC's prompt is assembled from, and
the recent knowledge-boundary work is exactly a "what may appear on the page" question — the
`player_action` leak was fixed by scoping what the representation carries, and `MAIN_QUEST`
remains open precisely because it is in the representation without being attached to anything
an NPC could know. Librande would recognise that as a badly drawn diagram.

The 256 → 36 collapse is the sharpest technical analogy, and it cuts against the usual instinct.
Faced with combinatorial explosion, the default modern move is to throw the enumeration at a
model and let it interpolate; Librande instead found the geometry in which the combinatorics
collapse, and got an algorithm that replaced a hand-typed table. That is the same axis as
generate-vs-enumerate in agent design, and the lesson is that the collapse only became available
*after* the right representation was found — three diagrams in. Worth pairing with the talk's
attention economics, which are now an agent-output problem rather than a documentation one:
readers check the scroll bar and leave. Length is a cost paid by the reader, and an agent that
returns everything it found has made the same mistake as the design bible.

Finally, the Q&A exchange that the first pass missed entirely is the best available description
of prompting as a craft. An audience member reframes the whole method as: you build a
comprehensive understanding, *compress* it, then spend your time helping people *correctly
unpack* what you compressed. Librande accepts the framing and names it "subtractive art." That
is the prompt-engineering loop exactly, including its central failure mode — the compression is
lossy, and the decompression happens inside someone else's head, where you have no control and
no error signal. His mitigation is worth porting: hand it over in person, put a pencil in their
hand, and treat the marked-up copy coming back as the only real evidence it was read.

## Open Threads

- **The recording is truncated.** It cuts off mid-Q&A with two questions asked and neither
  answered: (1) what percentage of his time goes to making the documents versus communicating
  them, and (2) what errors he sees co-workers make. The second is the more valuable loss — it
  is the only point where the talk would have covered failure modes from outside his own
  practice.
- No URL, publication date or duration is recoverable from the raw file; the frontmatter records
  these as unknown rather than guessing.
- Unresolved in the talk itself: the "holy grail" of an entire game design on one page. He has
  been "goofing around with it for 10 years" and reports no success.

---

### Note: how this differs from the first pass

Kept deliberately for comparison with [gdc-one-page-design.md](gdc-one-page-design.md). The
first pass is accurate about the talk's thesis and misses most of its argument. Specifically,
it does not contain: the rock-paper-scissors → slider redesign (the strongest claim in the
talk), the 256 → 36 vector collapse as a *process* of three failed diagrams, the
can't-fit-means-it's-broken diagnostic, the matrix/top-down method, the put-time-in-the-diagram
rule, the audience-layering idea from architecture, the compression/unpacking Q&A, and the fact
that Librande still writes design bibles privately — which the first pass inverts into bibles
being simply obsolete. Its Timestamps section lists section names under a heading that promises
times the raw file does not contain, and its frontmatter `tags` is a bare string rather than a
list. Its My Take reads the talk as a model for explainable AI; this pass argues the more
interesting AI point runs the other way.
