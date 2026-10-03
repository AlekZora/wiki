---
type: game-article
title: "2048"
url: https://en.wikipedia.org/wiki/2048_(video_game)
game: 2048
author: Wikipedia contributors
published: 2014-03-09
ingested: 2026-09-09
tags: [game-design, elegance, ai, puzzle, open-source, virality]
concepts:
  - ../concepts/elegance-game-design.md
---

## Summary

Encyclopedia entry on *2048*, the sliding-tile puzzle written in JavaScript and CSS
over a single weekend by Gabriele Cirulli, a 19-year-old Italian web developer, and
released March 9, 2014 as free and open-source software under the MIT License. The
game runs on a 4×4 grid: arrow keys slide every tile until blocked, identical tiles
that collide merge into one of their combined value, and a new tile spawns after each
move (a 2 with 90% probability, a 4 with 10%). The player wins by producing a 2048
tile but may keep going; the game ends only when no legal move remains — no empty
cell and no adjacent matching pair. Cirulli described it as "conceptually similar" to
*Threes!*, released a month earlier, and as directly influenced by *1024* (a *Threes!*
clone by Veewo Studio) and a further clone by Saming, which led James Vincent of *The
Independent* to call it "a clone of a clone." It drew over 4 million visitors in under
a week, spawned a clone wave of its own, and — because it is open source and
mathematically tractable — became both a common programming teaching exercise and a
standing target for AI search research.

## Notable Points

- The entire rule set is one verb (slide) plus one interaction (equal tiles merge)
  plus one generation rule (weighted random spawn), on a board with no hidden state.
- Cirulli built it as a personal programming challenge — "It was a way to pass the
  time" — not as a product.
- He refused to monetize it, saying he was unwilling to make money "from a concept
  that [he] didn't invent," and treated the spinoffs as "part of the beauty of open
  source software" so long as they made "new, creative modifications to the game."
- The *Threes!* developers published their 14-month development log in response,
  stating they had **considered and rejected** the merge-on-collision mechanic because
  it made the game too easy, and claiming in *Wired* that each of them beat *2048* on
  their first play.
- The merge rules contain genuine edge cases despite the simplicity: a merged tile
  cannot merge again on the same turn; with three matching tiles in a line only the
  two farthest along the direction of motion combine; a full row of four matching
  tiles combines as two separate pairs.
- Reception clustered on "viral" and "addictive" — the *Wall Street Journal* called it
  "almost like Candy Crush for math geeks," *Business Insider* "Threes! on steroids,"
  and Caitlin Dewey in the *Washington Post* "a nerdy, minimalist, frustrating game."
- The theoretical maximum tile is 131,072.
- AI progress on the game is tracked as a benchmark: by 2022 systems reached >95%
  probability of building a 16,384 tile and >75% for 32,768; by 2025, expectiminimax
  with pre-built tablebases reached 99.9% and 86.1% respectively. An AI solver placed
  second in a MATLAB coding contest.

## What It Attempted

A weekend programming exercise, not a designed product — an implementation of an
existing mechanic (merge-on-collision) that its originators had explicitly discarded
as too permissive, released free and open under a license that invited reproduction.

## Where It Succeeded / Where It Failed

Succeeded far beyond intent on reach (4M+ visitors in a week from a hobby project with
no monetization, marketing, or publisher) and on longevity as an artifact — its open
licensing turned it into teaching material and an AI research target, which is a form
of durability most commercial puzzle games never reach. It "failed" on originality by
its own author's admission, and arguably on difficulty design by its predecessors':
the *Threes!* team's claim that merge-on-collision made the game too easy is a rare
case of one design team publishing their reasoning for rejecting the exact mechanic
that made a competitor viral. Whether that is a failure depends on which axis you
measure — *Threes!* optimized for mastery depth, *2048* for immediate legibility, and
the market rewarded the second.

## My Take

*2048* is the cleanest available instance of a design constraint the vault has been
circling: the whole game is one screen, with the entire state visible and no hidden
information anywhere except in what enters the board. That single structural fact
does most of the work. Because the state is fully exposed, complexity cannot hide in
the simulation — it can only live in generation (the 90/10 spawn) — so the weighted
random tile is simultaneously the only hidden rule and the only source of uncertainty
the game has. And because there are no levels, difficulty has nowhere to escalate
*to*: instead the player's own success fills the board and shrinks the option space,
making the difficulty curve a function of progress rather than a tuned parameter.
That is a structurally different answer to the flow problem in
[flow-state](../concepts/flow-state.md) than Flappy Bird's, which holds a fixed
tolerance window and lets the player's fatigue supply the variance.

The AI intersection here is unusually concrete, and it is not the usual "could an LLM
play this." *2048* is a **stochastic full-information single-player** game — no
opponent, no hidden state, randomness confined entirely to the spawn — which makes it
a near-perfect isolation rig for the complexity/uncertainty split in
[elegance-game-design](../concepts/elegance-game-design.md). Expectiminimax works
here precisely because the uncertainty is enumerable and stationary; the search can
average over the known 90/10 distribution rather than model an adversary. That the
2025 systems reach 99.9% on the 16,384 tile but only 86.1% on 32,768 is a measurement
of how the difficulty compounds as the board's free space contracts — the machine
result quantifies the human design intuition. It also sharpens a claim I have been
making loosely: an agent is cheap to scale against complexity and expensive to scale
against uncertainty. Here the uncertainty is the *easiest possible kind* — known
distribution, no adversary, no non-stationarity — and it still costs 14 percentage
points at the top of the curve.

The *Threes!* rejection note is the most valuable single fact in the article. It is a
documented case of a design team correctly identifying that a mechanic reduced mastery
difficulty, rejecting it for that reason, and being commercially beaten by the team
that shipped it anyway. That is direct evidence that "hard to master" and "successful"
are not the same axis, and it is the kind of counter-example worth holding onto when
using elegance as a design target — the framework predicts depth, not adoption.

## Related

[Flappy Bird](flappy-bird-wikipedia.md) — the paired minimal case: one input, unbounded
ceiling from execution tolerance rather than combinatorics.
[What Makes Games Easy to Learn And Hard to Master](easy-to-learn-hard-to-master-jozwik.md)
— the framework this is a test case for.
[10 Games That Are Easy To Learn But Hard To Master](easy-learn-hard-master-gamerant.md)
— Tetris and Pac-Man as the other single-screen entries.
