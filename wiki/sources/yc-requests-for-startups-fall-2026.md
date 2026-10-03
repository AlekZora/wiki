---
type: article
title: "Requests for Startups — Fall 2026"
url: https://www.ycombinator.com/rfs
author: Y Combinator
published: 2026-09
ingested: 2026-09-03
tags: [ai, tool, economics, engineering, space]
concepts: [world-models, adaptive-tutoring]
---

## Summary

Y Combinator's Fall 2026 list of startup ideas they want to fund. The framing shift from the Spring 2026 batch: AI is "moving into the physical world" — the requests span education, defense, consumer software, aging care, blue-collar work, physical-world data collection, identity verification, compliance, and API maintenance. For the first time, one request comes directly from a sitting U.S. Secretary of the Army. Several entries in the clipped source have no section heading (likely a scraping artifact from embedded video blocks) — those are described by content below rather than by an invented title.

## Key Points

- **The Primer** (Andrew Miklas): Named for the AI tutor-book in Neal Stephenson's *The Diamond Age*. One-on-one tutoring has always produced the best learning outcomes (Aristotle/Alexander) but was reserved for the few. Wants a product that adaptively teaches young children to read, write, and do arithmetic at private-tutor quality, at consumer scale — a supplement to teachers, not a replacement, and a first step toward something that learns a child's mind over years.
- **The Future of American Defense** (Daniel P. Driscoll, US Secretary of the Army): The Army says its old acquisition playbook can't keep pace with modern threats and wants commercially developed, modular, open-system defense tech — low-cost interceptors, next-gen sensors/software/payloads, drones, resilient logistics, and advanced manufacturing built to survive extreme environments.
- **A Cloud for Small Software** (Pete Koomen): Agents now make it easy to build "small software" — bespoke tools for one team or a handful of users — but hard to deploy and share, because incumbent clouds (AWS, Azure) were built for software that scales to many users. Wants a cloud designed for small software: as easy to share as a Google Doc, with solved auth/permissions and safe code-sharing for nontechnical users.
- **Multiplayer AI** (Aaron Epstein): Argues AI tools are still "single-player" — one person, one chat window — while the tools that won the last two decades (Google Docs over Word, Figma over Photoshop) won by going multiplayer. As agents take on tasks lasting hours or weeks, teams need to co-inhabit a live agent session — watching, redirecting, handing off — rather than trading read-only transcripts.
- **Compute at Sea** (Francois Chaubard): Data centers are constrained by land, permitting, and power. Proposes moving compute offshore on standardized modular vessels — "compute flotillas" — using the ocean's sunlight and heat-sink capacity, since water isn't subject to the same permitting fights as land.
- *(untitled — consumer AI)*: Three years into the AI platform shift, the only new consumer icon is ChatGPT. Argues intelligence is now good enough to "treat an agent like a person," and cost per user is falling ~10x/year from today's ~$1,000/month — so the consumer moment (how we get around, learn, manage money, connect with friends) is close, and whoever builds first owns it.
- *(untitled — aging population)*: By 2030, one in five Americans will be over 65, with millions of unfilled caregiving jobs and 53 million family members already doing unpaid care work. Argues AI finally enables real products for seniors: voice interfaces that hold genuine conversations, safety/independence monitoring, assistive robotics, and coordination software for family caregivers.
- *(untitled — operating systems for physical-world work)*: 80% of the global workforce doesn't sit at a desk, and field-service/construction/fleet software hasn't fundamentally changed in 20 years. There are now three kinds of workers — AI agents, robots, and wearable-tracked humans — and no existing system manages all three together. Frames this as a bigger opportunity than existing software because these industries spend 10–100x more on labor than software, and a company here would own end-to-end data no model lab or robotics startup has.
- *(untitled — crypto)*: Makes a bull case for crypto despite a bear market: regulatory clarity, stablecoin adoption by major institutions, tokenized stocks, and an expectation that AI agents will eventually use crypto rails for payments. Argues bear markets filter for builders over yield-chasers, and cites BlindPay, Infinia, and Aspora as examples of infrastructure being built for underserved payment corridors.
- **Data for the Real World** (Austin Tindle & Diana Hu): AI is superhuman at code, language, and images but starved of dense data about the physical world — current sensor data is sparse and built for humans, not AI. Cites Sorcerer's (Tindle's company) autonomous weather balloons feeding US government forecasting, and Gecko Robotics' hard-to-reach-place data collection, as examples. The core claim: once a physical system can be modeled precisely, it can be controlled — with examples ranging from steering hurricanes to reversing desertification.
- *(untitled — trust/identity layer)*: Opens with an anecdote — a finance worker wired $25M after a video call where every other participant turned out to be a deepfake. Argues voice/face verification, the trust signals humans have relied on, no longer work now that faking a human is cheap. Wants a way to verify a real human is on the other end of a call, message, or transaction — ideally without requiring people to give up privacy — with applications from bot-free social platforms to fraud-free dating apps.
- **AI-Native Compliance Infrastructure** (Daivik Goel): Financial compliance today is spreadsheets, siloed point solutions, and expensive headcount, and the cost compounds as businesses expand into new jurisdictions. Argues monitoring regulatory change, flagging anomalies, generating reports, and maintaining audit trails are exactly the kind of tasks AI can do faster and cheaper — wants infrastructure that consolidates the fragmented stack rather than just automating the existing manual workflow.
- **Self-Maintaining APIs** (Harsha Gaddipati): Having worked with 50+ API vendors, observes that API communication is broken — breaking changes ship with little warning, features launch unnoticed, changelogs go unread (30% of AWS service downtime he saw traced to unnoticed external API/package changes). Argues agentic coding tools (Claude Code, Devin, Greptile) have already normalized giving external tools codebase access, so API providers should ship an agent that scans customer codebases and opens a fix PR when they change something — either per-vendor ("install Stripe's update agent") or as a neutral cross-vendor service, "Dependabot for APIs."

## Quotes

> "For the first time in history, something like the Primer is starting to feel possible." — Andrew Miklas

> "AI hasn't had its multiplayer moment yet. AI agents are the most powerful new tool a team has, but it's the one thing people still use by themselves." — Aaron Epstein

> "Every trust signal we have was built for a world where faking a human was expensive, and that world is gone."

> "Once you can model a system, you can control it. Steering hurricanes. Reversing desertification. Cooling the planet." — Austin Tindle & Diana Hu

## My Take

The AI lens is unusually literal in this source — it's YC explicitly betting on where AI capability creates new company categories, so almost every entry already is an AI-intersection claim. The more interesting move is reading it for the *pattern underneath* the individual pitches: repeatedly, the claim isn't "AI does X" but "AI closes the gap between measuring/modeling a system and controlling it" — that's explicit in Data for the Real World (dense sensor data → simulator → control of hurricanes, desertification), but it's the same shape as Self-Maintaining APIs (detect drift → act on the codebase) and AI-Native Compliance (detect regulatory change → act on the filing). It's a renderer/simulator/planner progression happening across totally unrelated domains at once — see [World Models](../concepts/world-models.md), which this source directly extends with a concrete non-gaming, non-robotics example of the "simulator gap" closing.

The Multiplayer AI framing is a genuinely useful naming of something that's been true for a while: current AI interfaces default to one human per session even when the underlying task (a multi-day agent run) obviously involves a team. It reframes a UX gap as the actual bottleneck, not model capability.

The trust-layer idea is the most unsettling because it's a second-order effect of the same generative capability the rest of the batch treats as pure upside — cheap deepfakes are the negative externality of the exact capability gains (multimodal generation, cheap inference) that make the Primer, consumer AI, and physical-work-guidance ideas possible. YC funding both the capability wave and the "clean up after the capability wave" wave in the same document is worth noticing.
