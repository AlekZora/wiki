---
type: concept
title: Affect Circumplex (Valence–Arousal)
aliases: [Russell's circumplex, valence arousal model, psychophysiological sensing, affective sensing loop]
tags: [psychology, emotion, feel, behavior, systemic, ai]
sources: [sources/psychophysiology-emotions-gur.md, sources/why-players-recommend-games.md]
updated: 2026-05-19
---

## Definition

Russell's circumplex model maps emotion not as a list of discrete labels but as a position in a 2D space defined by two axes: **valence** (the emotion's positive/negative direction) and **arousal** (its intensity, high to low). Anger and sadness share negative valence but differ in arousal; excitement and contentment share positive valence but differ in arousal. Psychophysiological instruments cannot read discrete emotions, but they *can* read signals correlated with valence and arousal — facial EMG for valence; heart rate, electrodermal activity (EDA/GSR), respiration, and pupillometry for arousal and cognitive load; EEG for flow, cognitive control, and approach/withdrawal. The hard constraint: the signal-to-state mapping is **many-to-one** — a racing heart can mean fear or attraction — so position on the circumplex is *inferred*, never read, and the cause is never recoverable from the signal alone.

## How I Think About It

This is the most architecturally important concept in the 2026-05-19 batch for Thread B (AI integration). The Try Evidence source is written for a human researcher in a lab, but the loop it describes — read involuntary signals → infer valence/arousal → adjust the experience — is exactly an *affective sensing loop*. Replace the human psychologist with a real-time system and you have an AI that perceives the player's emotional state directly, bypassing their input and their self-report entirely.

That is a different category of player-AI relationship than the priority list names. Not building, fighting, coexisting, or becoming, but **being read by**. Left 4 Dead's Director infers player stress from gameplay proxies (health, position, time-since-last-threat); the circumplex/psychophysiology stack says you can infer it from the body itself — EDA on a finger clip, frontal asymmetry on an EEG band. The Director, but sensed from the player rather than the game.

The many-to-one constraint is not a defect to engineer away — it is the richest part of the design space. An AI that *knows* exactly what the player feels is omniscient and dramatically inert. An AI that feels the player's arousal spike and has to *guess* whether it was fear, delight, or frustration — and can guess wrong, and act on the wrong guess — has interiority-adjacent behavior: it is interpreting, not reading. Its misreadings are characterization.

This also closes a loop with the rest of the batch: emotional peaks (high-arousal moments) create durable, retellable memories ([emotional-memory.md](emotional-memory.md)), which is what drives recommendation. The circumplex is the instrument that tells you, physiologically, where those peaks actually are — not where the designer assumed they were (cf. Capcom finding a Resident Evil 3 zombie chase was less scary than intended).

## Related Concepts

- [Emotional Memory](emotional-memory.md) — high-arousal positions on the circumplex are what get consolidated and retold; the circumplex locates the peaks emotional memory depends on
- [Flow State](flow-state.md) — flow has an EEG signature; flow is a measurable region of the affective/attentional space, detectable without self-report
- [Experience Goals](experience-goals.md) — designing for a target emotion means designing for a target circumplex region; physiology checks whether you hit it
- [Recommendation as Identity](recommendation-as-identity.md) — the emotional-peak driver of recommendation; arousal is the measurable substrate of "the moment you tell your friends about"
- [AI Agent Personality Design](ai-agent-personality-design.md) — an AI whose misreadings of player affect become its characterization
- [Metrics Trap](metrics-trap.md) — the warning: physiological signals are precise but many-to-one; optimizing the proxy (arousal) is not optimizing the experience (which emotion)

## Open Questions

Touches **Q3** (AI as a living system that adapts through play — here, adapting to sensed affect), **Q5** (interiority — does an AI that *interprets and misreads* the player read as having a mind?), **Q7** (emotional investment — engineered and measured rather than assumed), **Q1** (the weakest link: AI that can't tell what the player feels — making the inference gap the subject matter).

- Can an AI's *misreadings* of player affect be designed as characterization rather than error — an AI with a recognizable interpretive bias?
- Does a player who knows they are being physiologically read behave differently? (The observation effect — does sensing destroy the thing it senses?)
- Is the many-to-one ambiguity reducible by triangulation (EMG + EDA + EEG), or is the cause of an emotion fundamentally unrecoverable from the body?
- Where is the ethical line between an AI that responds to sensed affect (adaptive) and one that exploits it (manipulative)? (Connects to [illusory-insight.md](illusory-insight.md): manufacturing a felt state.)

## Game Design Vector

**Mechanic:** The game (optionally) reads a coarse arousal proxy and infers a valence/arousal position, then adjusts pacing, threat, or the AI's behavior — but always under the many-to-one constraint, so the system acts on a *guess* about the player's state, visibly and sometimes wrongly. The misread is a designed event, not a bug.

**2D Expression:** A 2D plane lets the player *see* the AI's model of their emotional state rendered into the same plane they act in — the AI's guess about how the player feels can be made spatially legible (where it concentrates threat, where it backs off) without a separate UI layer. The inference becomes part of the readable world.

**Addictive Loop:** The loop is sustained by an AI that responds to the player's actual emotional arc, not a fixed difficulty curve — every session is shaped by the player's real arousal trajectory, so it never adapts away into sameness. The return pull is "what will it read in me this time, and will it be right?"

**Novel Angle:** No shipped game makes the AI's *interpretation gap* the subject matter — an AI that feels your arousal but cannot know its cause, narrates its guesses, and is sometimes movingly wrong about you. The drama is in the misreading, not the reading.

## AI Integration Vector

**Player-AI Relationship:** Names an unlisted relationship type: *being sensed by* an AI that reads your body, not your input — and that interprets rather than knows. Intimacy and unease come from the same source: it feels you, but it can misunderstand you.

**AI as Evolving System:** An AI that adapts to a specific player's affective patterns over many sessions builds a private model of how *that* player's body responds — it evolves into an interpreter specialized to one person, which is a form of genuine learning through play, not a fixed script.

**AI as Development Environment:** Surfacing the AI's valence/arousal inference makes its model of the player visible and watchable — the player witnesses the AI's emotional model of them being built, refined, and corrected, which is AI development made directly perceptible inside the fiction.

**Persistence:** What persists is the AI's affective model of *this* player — a representation of how they feel, accumulated across sessions and resistant to a save wipe in the sense that the relationship's whole value is in that accumulated reading. Reset it and the AI no longer knows you; that is the designed loss (Q8).
