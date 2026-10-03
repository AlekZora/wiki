---
type: article
title: "Goal Map visual references: voyage maps, old cartography, journey games, and tension without judgment"
url: https://www.perplexity.ai/search/17265d38-c6f1-4621-8559-c7329b0b2649
author: Perplexity Deep Research (prompt written by the user for Goal Map), citing the Library of Congress, Wikimedia Commons, Gallica, archive.org, Parks Canada, studio press pages and others
published: 2026-10-03
ingested: 2026-10-03
tags: [design, game-design, cartography, maps, narrative, history, fiction, psychology, ai, llm, productivity]
concepts:
  - ../concepts/fair-uncertainty.md
  - ../concepts/coziness.md
  - ../concepts/worst-day-design.md
  - ../concepts/drama-management.md
  - ../concepts/hallucinated-agency.md
---

## Summary

An AI research report commissioned by the user for Goal Map's journey layer. The prompt
described the map (milestones as places, a destination that is always visible, land that
appears only where you have walked, routes that close, detours as side trails) and asked for
visual references that give the feeling of an epic voyage, with the tension "in the world
(weather, terrain, the unknown, closed passes), never in judging or shaming the user". The
report surveys about 30 references in five groups: literary voyage maps (Ortelius's map of
Odysseus's wanderings, Riou and de Neuville's Verne engravings, Stevenson's Treasure Island map,
the 1914 Oz map, Denslow's 1900 Oz illustrations); old cartography (portolan charts, Olaus
Magnus's *Carta Marina*, the Lewis and Clark track map, Franklin expedition route maps);
journey games (*80 Days*, *Sunless Sea*, *Heaven's Vault*, *Death Stranding*, *The Banner Saga*,
*Darkest Dungeon*, *Slay the Spire*, *Obra Dinn*, *Pentiment*); film map sequences; and living
mapmakers. Each entry gives the feeling, the techniques that produce it, a Goal Map application
and a copyright status. It then ranks eight references, proposes five visual directions, sets
out rules for tension without judgment, and lists clichés, product pitfalls, signs of an
AI-generated look, and rights boundaries.

The report was written for this product from a prompt that already described the design, so a
good part of its advice confirms the brief rather than adding to it. Its sources were not
checked: most links go to search-result pages rather than specific images, and several
citations were collapsed in the clipping ("loc+2", "wikipedia+1").

## Key Points

- **Overall direction:** an Odyssey-shaped route drawn like a growing expedition chart. The
  destination stays visible, walked ground gains engraved detail, and weather or terrain, not
  moral judgment, creates the uncertainty.
- **Three knowledge states:** *known* (walked land, dated footsteps, conditions met),
  *inferred* (faint contours, a possible pass, an approximate milestone location), *unknown*
  (atmosphere and silhouette, not blackness, and "no fabricated threats").
- **Separate route topology from event certainty** (from *Darkest Dungeon*): the user can see
  where milestones are while weather, closures and exact effort stay unknown until closer.
- **Promised places:** a named place on a map works like a promise. Reveal milestone names,
  silhouettes and broad terrain; hold back local paths, weather and minor landmarks.
- **Routes described by quality, not difficulty score** (from *Death Stranding*): "longer but
  sheltered", "short but exposed", "good for low-energy days", "blocked until an external
  dependency clears".
- **Travel as memory** (from Lewis and Clark): every detour stays on the finished map, which
  should say "this is how it happened", not "this is the efficient route you should have taken".
- **Odyssey mapped to milestones** in eight stages: home visible, departure, episode-islands,
  winds and trials, tempting harbours (side trails), reckoning, recognition, homecoming. Its
  ethical change from the source: obstacles never imply "the user deserved the storm".
- **Strongest eight, ranked:** Ortelius's *Ulyssis Errores*, Agnese's portolan atlas, Riou's
  Verne engravings, *Death Stranding*, the Lewis and Clark track map, the early Oz map and
  Denslow palette, *The Banner Saga*, *Sunless Sea*.
- **Five visual directions:** engraved expedition (warm off-white, near-black hatching, walked
  regions gain detail), Odyssean sea chart (milestones as islands, home harbour always
  visible), storm and terrain (land as working conditions, weather with a readable cause and an
  alternative), chromatic stations (one muted palette per phase), living field notebook (dates,
  crossed-out route guesses, notes like "pass closed", "found another way").
- **Tension without judgment**, in five rules: put pressure outside the user; always offer at
  least two legitimate responses to an obstacle; make uncertainty fair (foreshadow hazards,
  unknown is not danger, no arbitrary punishment after a route is chosen, explain what changed);
  honour recovery (rest doesn't break a streak or dim the map, and camps count as travel);
  record rather than score.
- **Product pitfalls** include random closures "that feel like the app is sabotaging
  progress", real obstacles such as illness or care work turned into cute monsters, an
  "optimal route" algorithm silently overriding the user, and a poetic map sitting next to
  streaks, leaderboards or shaming notifications elsewhere in the product.
- **Signs of an AI-generated look:** hatching that changes direction between neighbouring
  terrain, fake writing, repeated near-identical trees and waves, detail at every scale with no
  hierarchy, symbols that change slightly between states, rivers and shadows that make no
  physical sense, and a mix of styles with no system behind it. The fix it gives is to build "a
  controlled library of authored marks, terrain modules and line weights" rather than generating
  final assets one by one.
- **Rights:** public-domain works (Homer, Ortelius, Verne's original illustrations, the 1900
  and 1914 Oz material) can inspire style more directly, but modern scans, restorations and
  editions may have their own terms. Tolkien, Baynes's Narnia maps and the 1939 Oz film are off
  limits. The report also says to check EU rights, since Goal Map operates from Germany, and
  marks its own classifications as "not legal advice".

## Quotes

> The strongest synthesis for **Goal Map** is an Odyssean route structure rendered like an evolving expedition chart: the destination remains visible, travelled ground gains engraved detail, and weather or terrain—not moral evaluation—creates uncertainty.

> Useful uncertainty is not the same as missing information.

> **Unknown:** Atmosphere and silhouette rather than empty blackness; no fabricated threats.

> The final image should say, "This is how it happened," not, "This is the efficient route you should have taken."

> The important adaptation is ethical: unlike many ancient trials, obstacles should never imply that the user deserved the storm. The system narrates circumstances, choices and recovery, not virtue.

> Distinguish "unknown" from "dangerous"; unrevealed land should invite curiosity, not imply menace.

> Generating final map assets independently instead of building a controlled library of authored marks, terrain modules and line weights.

## My Take

**Mostly confirmation, and that's partly circular.** Most of the report's central advice is
already in the proposed journey layer in `~/projects/goal-map/docs/DESIGN.md`: summit visible
from day one, land revealed by walking, closed paths kept on the map at 45% with a barrier,
detours as dotted side trails ending in a cairn, no compass or parchment. That's reassuring,
but the prompt described exactly that design, so agreement is weak evidence. The parts that are
actually new:

- **An *inferred* state between walked land and blank paper.** DESIGN.md has two states (land
  up to 70 units ahead of the furthest step, blank paper beyond). A faint third layer, such as a
  possible pass or an approximate shape for the next milestone, would let the map show what it
  only guesses. It also matches what the milestones are: an AI's inside-view guess at the route
  ([planning-fallacy](../concepts/planning-fallacy.md)). Drawing upcoming milestones as
  "inferred", firming up as you get near, would be an honest way to show AI uncertainty.
- **Route qualities instead of a difficulty score** fit the closed-path redraw. When the way
  round is drawn, a short label ("longer, sheltered") gives the user a reason, not a verdict.
- **Rest and camps.** "Rest should not break a streak or dim the map." The current drift rule
  counts off-route steps, not missing days, so it already behaves this way. The camp idea gives
  a worst-day check-in somewhere to sit on the map ([worst-day-design](../concepts/worst-day-design.md)).
- **The AI-look checklist** is the most useful single section for the build. Almost every item
  on it (symbols that change between states, inconsistent hatching, rivers that make no sense,
  repeated silhouettes) is a consistency failure, which is what you get from generation with no
  state behind it. That's the renderer-without-simulator failure from
  [hallucinated-agency](../concepts/hallucinated-agency.md), seen in pictures instead of text.
  The report's fix, a fixed library of authored marks, is already Goal Map's architecture:
  `terrain.ts` draws land with pure functions seeded from the goal id, and AI does only its
  three jobs. The report gives a design argument for a decision the project made for
  engineering reasons.

**Where it pulls against the project's rules:**

- **"Attribute rerouting to conditions and new knowledge, even when the user consciously
  changes priorities."** This conflicts with synthesis idea 1 (the map may frame a setback but
  never soften a drift or invent an event) and with declared detours, which are the user's own
  choice. If the user changed course and the map says a storm did it, the map is lying, and a
  map you can't trust can't answer "am I still on my path?". The report's own better rule is
  in the same section: "Treating side trails as temptations to be resisted rather than
  deliberate choices" is a pitfall. Choices can be shown as choices without blame. **Inference:**
  only conditions the user actually logged (a blocker) become weather; a change of priorities
  becomes a declared detour or a re-route, shown as the user's decision.
- **Weather fronts moving across the map.** Unless they come from logged blockers, they are
  events the app invents, and the report's own pitfall list names "random closures" as
  sabotage. It also says "no fabricated threats". So any weather has to be data-driven or
  purely decorative, never a closure.
- **"Reckoning: one final difficult passage."** As a picture this is fine. As a mechanic it
  would mean making the last leg harder on purpose, which is a resolution the product would be
  authoring. The setup-only rule from the Attractor director ([drama-management](../concepts/drama-management.md))
  allows a dramatic-looking last leg but not an invented obstacle.
- **Chromatic stations** (a colour per phase) would break DESIGN.md's restrained six-token
  palette. That's a design decision, not something to slip in.

**The AI lens more broadly.** The report's main idea, uncertainty that creates tension without
feeling like a judgment, is a general rule for any system whose hidden state a person has to
live with, including AI agents. A user forgives a forecast and resents an ambush. The
difference is whether the uncertainty was visible before they committed and whether changes
come with a reason. Extracted as [fair-uncertainty](../concepts/fair-uncertainty.md). The
pressure-outside-the-user rule is the same move as [coziness](../concepts/coziness.md)'s
"rain on the window, not through it": the drift warning is where the goal's pressure comes into
the room, so it's the one place where the "weather, not verdict" wording matters most, and it
can be written in code, since `PROJECT.md` rules out AI-written drift messages.

**On the report as a source.** It's AI-written and unchecked. Its copyright calls look
sensible and are hedged, but they aren't legal advice, and Goal Map's "no borrowed IP" rule is
stricter than "public domain is fine" anyway. The prompt itself named Oz, Tolkien and Narnia as
inspirations, and the report handled that well: it uses them for principles and says not to
take names, places or art. The Odyssey names (Ithaca, Ortelius's title) are public domain, but
"no names from existing stories" in DESIGN.md's journey layer is still the safer reading.
Tension H in [the synthesis](../answers/goal-map-wiki-synthesis.md) applies again: keep the
function, rename it in Goal Map's own survey-sheet language.
