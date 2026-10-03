---
type: book
title: "The Library of Greek Mythology"
author: Apollodorus (pseudo-Apollodorus)
published: c. 100 (1st–2nd century AD)
ingested: 2026-07-23
tags: [mythology, history, philosophy, narrative, systems, knowledge-representation]
concepts: [genealogy-as-knowledge-graph]
---

## Summary

The *Library* is the only comprehensive handbook of Greek mythology to survive from antiquity. Its author is traditionally called Apollodorus, but scholars have established this attribution is false: the real author is unknown and probably wrote in the first or second century AD, several centuries after the Alexandrian scholar Apollodorus of Athens he was long confused with. The author was an editor rather than an original writer — he compiled the book by selecting and summarizing material from earlier poets and mythographers (chiefly Homer, Hesiod, and the fifth-century prose writers Pherecydes and Acousilaos), rather than researching or interpreting the myths himself. The book covers the full span of Greek mythical history: it opens with the *Theogony* (the origin of the cosmos and the gods), then organizes the whole of heroic mythology genealogically around six main families — the Deucalionids, Inachids, Atlantids, Asopids, the Athenian royal line, and the Pelopids — and concludes with the Trojan War and the returns of the Greek heroes, including a summary of the *Odyssey*. Unlike many later Hellenistic mythographers, the author makes no attempt to rationalize the myths (e.g., explaining gods as forces of nature or deified humans) and does not try to resolve contradictions between variant traditions — he simply records what earlier sources said. The book was valued in later antiquity as a reliable reference work; the 9th-century Byzantine scholar Photius praised it as a useful summary of "the most ancient stories of the Greeks," and it was used extensively by the 12th-century scholar John Tzetzes.

## Key Points

- The genealogical structure is the organizing spine of the entire work: because Greek heroic myth has no single absolute chronology, the author (following the earlier example of Hesiod's *Theogony* and the *Catalogue of Women*) uses family succession — who married whom, who was born to whom — as the only available timeline, letting every story be located at its correct point in a family tree.
- The genealogical tables (added by translator Robin Hard, not present in the original manuscript) formalize this: parentage and marriage are marked with swung dashes, order of succession with lettered labels, and figures who belong to more than one family tree are boxed to flag the cross-reference.
- Only six main heroic families are needed to organize the entire mythological tradition of the Greek world, despite its many independent regional centers (Argos, Thebes, Sparta, Athens, Crete, Troy, etc.) — the families interlock through intermarriage and shared ancestors rather than each city having its own isolated lineage.
- The author is unusually thorough with catalogues that serve no narrative purpose — e.g., naming all fifty daughters of Danaos and their husbands, all fifty sons of Lycaon, the full roster of the Argonauts, the Greek leaders at Troy — treating completeness as a virtue in itself, even where most named figures never reappear.
- The work's own authorship is a small mystery within its own textual tradition: internal evidence (a citation of the *Chronicles* of Castor of Rhodes, datable to 61 BC) proves it postdates the historical Apollodorus of Athens by a century or more, and stylistic features of the Greek point to composition under the early Roman Empire.
- The book was almost certainly not written as a children's primer, despite that common assumption — while individual stories are told very briefly (Perseus in three pages, Oedipus in two sentences), the density of names and the demand that the reader hold an extensive genealogical system in mind exceeds what a simple introductory text would require.

## Quotes

> "In the same volume, I read a small work by the scholar Apollodorus; it is entitled the Library. It contained the most ancient stories of the Greeks: all that time has given them to believe about the gods and heroes... All in all, it is a general summary which is by no means lacking in usefulness to those who attach some value to the memory of the ancient stories." — Photius, Patriarch of Constantinople, 9th century

> "Now, due to my erudition, you can draw upon the coils of time, and know the stories of old. Look no longer in the pages of Homer... seek no longer the sonorous verses of the cyclic poets; no, look in me, and you will discover all that the world contains." — prefatory poem placed before the *Library* in Photius' copy

## My Take

The *Library* is a compression project, not a creative one, and that's exactly what makes it interesting through the AI lens. The author had no originality and made a virtue of it: faced with a mass of partially lost, mutually contradictory poetic sources (Homer, Hesiod, the epic cycle, regional oral traditions), the job was to synthesize them into one coherent, navigable reference structure without editorializing — without "fixing" the contradictions by imposing a preferred version. That's precisely the discipline a good RAG summarizer or retrieval system should have and usually doesn't: canonicalize without hallucinating consensus where the sources disagree. The genealogical backbone is the more concrete AI parallel — it's a relational schema, entities (gods, heroes) connected by typed edges (parent-of, married-to), that lets any narrative fragment dock into a fixed structure at a known coordinate. The translator's convention of *boxing* names that recur across multiple family trees is a manuscript-era solution to exactly the entity-disambiguation problem a knowledge graph or a wiki's concept-linking system has to solve computationally: the same node, referenced from more than one place, needs one canonical identity. This wiki does the same thing with its own concepts/ directory and cross-linking convention — the *Library* is a pre-digital instance of the same design problem: how do you store a large, inconsistently-sourced body of knowledge so it stays queryable and doesn't silently lose the parts that don't fit a tidy narrative.
