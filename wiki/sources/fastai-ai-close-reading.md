---
type: article
title: "How To Use AI for the Ancient Art of Close Reading"
url: https://www.fast.ai/posts/2026-01-21-reading-LLMs/
author: Rachel Thomas
published: 2026-01-21
ingested: 2026-04-13
tags: [ai, llm, education, reading, tool]
concepts: [whole-game-learning]
---

## Summary

Rachel Thomas describes how LLMs can revive the ancient practice of close reading — deep, attentive engagement with a text. Jeremy Howard used an LLM to read Eric Ries's book *Incorruptible* chapter by chapter, asking clarifying questions, following rabbit holes, and generating context summaries for subsequent chapters. Johno Whitaker applied the same approach to a dense Yann LeCun paper. The SolveIt platform supports this workflow.

## Key Points

- Close reading is one of civilization's oldest technologies for understanding — LLMs can serve as real-time interlocutors for it.
- The workflow: convert PDF to Markdown → generate chapter summaries as context → read with LLM, asking questions → generate chapter-end overviews for next session.
- Key benefits: following rabbit holes (Jeremy discovered 4 of 13 Jack Welch mentees ran Boeing during its safety crisis), asking for clarification, seeking counterexamples, personalizing examples.
- The fastanki library allows creating Anki flashcards inline during the reading dialog.
- Preparation is critical: setting up context beforehand ("sharpening pencils") makes the session dramatically better than cold-start.
- Hallucination risk is reduced when the LLM is grounded in the text and allowed to search the web.

## Quotes

> "This is one of the absolute best reading experiences I've ever had!" — Jeremy Howard

> "It's like the architect sharpening his pencils… that little investment up front makes it a very different tool to the vanilla case."

## My Take

The close reading revival angle is interesting — this isn't just AI as productivity tool but AI recovering a contemplative practice. The rabbit hole discovery (Jack Welch's Boeing mentees) is a genuinely useful demonstration of what's unlocked. The spaced repetition + Anki integration is the right call, though the toolchain is still clunky. Worth tracking how SolveIt evolves.
