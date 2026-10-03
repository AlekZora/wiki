---
type: book
title: "Characters and Viewpoint"
author: Orson Scott Card
published: 1988
ingested: 2026-06-22
tags: [writing-craft, narrative, character, fiction, psychology, viewpoint, storytelling, identity]
concepts:
  - ../concepts/mice-quotient.md
---

## Summary

A practical craft guide for inventing, constructing, and performing fictional characters. Card divides the work of characterization into three stages: Invention (where characters come from and how to deepen them), Construction (how to match characterization depth and type to the kind of story you're telling), and Performance (how to handle point of view, voice, and narrative distance). The central argument is that fictional characters must be functionally more knowable than real people — readers can access inner life, motive, and context in ways real relationships never allow. Good characterization means answering the reader's three unconscious questions at all times: So what? Oh yeah? Huh?

## Key Ideas

- A character is revealed through: action, motive (what they mean to do), past, reputation, stereotypes, network/relationships, habits, talents/abilities, tastes/preferences, and body — in roughly that order of narrative power. Action is strongest; physical description alone is weakest.
- The "cliché shelf": the first answer you reach for when asking why a character does something is almost always a cliché. Keep interrogating with "why?" and "what result?" until you find an answer that feels alive.
- Exaggeration + twist: take a character assumption and push it further than expected (archetypal) or invert it (twist). Gene Wolfe's celibate king who is terrified he'll accidentally break his vow — opposite of expected restlessness — is the canonical example.
- The MICE Quotient: every story is a mix of four factors — Milieu, Idea, Character, Event — and the dominant factor determines the structure and the kind/depth of characterization needed.
- The implied past: you can give a character depth and history without stopping the narrative — through what they expect, how they habitually behave, what quick references they drop. A child who flinches from an extended hand implies her past instantly, without exposition.
- Stereotype is a tool: readers classify strangers into categories automatically and unconsciously (so do chimpanzees). Writers count on this for efficiency, and can use it to set expectations that are later subverted.
- Character attitude in viewpoint: the reader experiences a scene through the viewpoint character's filter of attitude — what they notice, what they assume about it, how it feels. Attitude is what gives description function; without it, description is inert.
- Character transformation must be justified: the more important the character and the greater the change, the more the writer must prepare for and explain it. Unjustified change destroys reader trust.
- The "thousand ideas" interrogation technique: starting from a single trait or situation, ask "what could go wrong?" and "why would they do that?" — continuously branching until you have a fully realized situation and character.

## Quotes

> "A character is what he does, yes — but even more, a character is what he *means* to do."

> "This book is a set of tools: literary crowbars, chisels, mallets, pliers, tongs, sieves, and drills. Use them to pry, chip, beat, wrench, yank, sift, or punch good characters out of the place where they already live: your memory, your imagination, your soul."

> "Our objective as storytellers and writers isn't to make money — there are faster and easier ways of doing that. Our objective is to change people by putting our stories in their memory."

> "Believability in fiction doesn't come from the facts — what *actually* happened. It comes from the readers' sense of what is plausible — what is *likely* to happen."

## My Take

This book is a manual for constructing believable cognitive and behavioral models of people. That is the core problem — and it is not only a fiction-writing problem. It is the NPC design problem, the AI agent personality problem, and the user-modeling problem.

Card's character taxonomy (action → motive → past → reputation → stereotypes → network → habits → talents → tastes → body) maps almost directly to an NPC schema. The ordering matters: AI-generated characters fail most often when they lead with surface properties (description, voice tone, occupation) rather than behavioral logic (what do they do under pressure, and why). Card's hierarchy says: ground the character in observable behavior first, then the inner world, then the surface.

The MICE Quotient is the most directly applicable framework for quest and narrative AI. A quest generator that does not know what *kind* of quest it is generating produces structurally incoherent output. Milieu quests should open and close with the state of a world space; Character quests should open and close with a transformation; Idea quests should open and close with discovery. The generator needs to know what it is contracted to deliver.

The "cliché shelf" is a precise description of why LLM character generation defaults to generic: the model's most probable token sequences are the clichés. Card's technique of interrogating past the first answer is a concrete prompting strategy — explicitly instruct the generator to reject its first output and continue probing for a less obvious answer.

The implied past technique is a model for how AI NPCs should express their history: not through data dumps ("I grew up in X and lost my family to Y"), but through expectation, habit, and quick reference. A character who recognizes "FINAL NOTICE" envelopes without explanation has an implied past. This produces depth without breaking narrative flow — and it is exactly the kind of NPC behavior that creates the recognition effect the Side Quest experience goal is built around.
