---
type: concept
title: Self-Determination Theory
aliases: [SDT, autonomy competence relatedness, PENS, need satisfaction]
tags: [psychology, motivation, game-design, loop, compulsion]
sources: [sources/persistence-gaming-sdt-jansz.md, sources/why-players-recommend-games.md]
updated: 2026-05-19
---

## Definition

Self-Determination Theory (Deci & Ryan) holds that sustained, willing engagement in an activity is produced by the satisfaction of three basic psychological needs: **autonomy** (the activity is self-directed, not coerced), **competence** (the activity produces a felt sense of growing mastery), and **relatedness** (the activity connects you to others or to something larger). When all three are met, motivation becomes intrinsic and self-sustaining; when they are not, even heavily rewarded behavior decays. In games research the operational instrument is Rigby's Player Experience of Need Satisfaction (PENS), used by Jansz et al. to explain why players persist through frustration when intermediate rewards fail to arrive — the "paradox of gaming."

## How I Think About It

SDT is the load-bearing answer to a question this wiki keeps asking: why does a player keep going when the activity looks, from the outside, like unrewarded labor? The naive answer is "reward schedules" (variable-ratio reinforcement, the slot-machine model). SDT says that's wrong, or at least incomplete: persistence is produced by *need satisfaction*, and reward schedules without autonomy/competence/relatedness produce compulsion, not engagement — and compulsion is brittle.

This is the rigorous version of the distinction [intrinsic-motivation.md](intrinsic-motivation.md) draws between flow and workaholism. SDT names the three inputs and lets you check each one. It also explains the overjustification effect mechanically: adding an extrinsic reward can undermine autonomy ("I'm doing this for the payout, not because I chose to"), which removes a need-satisfaction leg, which collapses intrinsic motivation. The recommendation synthesis shows this at the word-of-mouth layer — referral incentives went *negative* exactly when players already felt autonomous, because the incentive contradicted the autonomy that was driving the recommendation.

The most useful corollary for this project: a loop that must run without paid incentive (the artifact-testbed meta-loop) cannot be sustained by points. It has to deliver competence (legible mastery), autonomy (real control, not the illusion of it), and ideally relatedness (the activity connects to others or to an identity). Miss one and the loop dies the moment novelty wears off.

## Related Concepts

- [Intrinsic Motivation](intrinsic-motivation.md) — SDT is the structural mechanism; intrinsic motivation is what need-satisfaction produces
- [Flow State](flow-state.md) — flow's task properties (autonomy, control) overlap heavily with SDT's needs; flow is the experiential signature of need satisfaction at peak intensity
- [Social Identity Theory](social-identity-theory.md) — the contextual modifier Jansz stacks on top of SDT: identity strength changes how strongly need satisfaction drives persistence
- [Self-Expression as Play](self-expression-as-play.md) — self-expression is autonomy + competence expressed outward; an SDT-aligned motivation
- [Serious Games](serious-games.md) — games work as behavior-change tools partly because they are need-satisfying by construction

## Open Questions

Touches **Q6** (the actual pull mechanism behind a non-reward compulsive loop), **Q7** (emotional investment without conventional stakes — relatedness/competence as the substitute), **Q4** (relatedness with a non-human AI as a player-AI relationship type).

- Can an AI satisfy *relatedness* — genuinely, not as a manipulation — such that the player's persistence is anchored by the relationship to it?
- Is competence satisfaction in a player-authored AI about the AI's growth, the player's, or an inseparable joint trajectory?
- Does autonomy survive an AI that adapts to keep the player engaged? (If the AI is steering the experience, is the player's sense of self-direction real or manufactured?)
- The Jansz sample was ~95% male core gamers — do the need-weightings generalize, or is the relatedness leg underweighted by sample skew?

## Game Design Vector

**Mechanic:** Every core loop is audited against three explicit gauges — autonomy (does the player choose, or is the choice illusory?), competence (is mastery visible and growing?), relatedness (does the activity connect to another agent or an identity?). The game refuses to add extrinsic reward layers (points, leaderboards, payouts) because each one risks undermining the autonomy leg. Difficulty is tuned to keep the competence signal alive, not to maximize time-on-task.

**2D Expression:** In 2D, competence is directly legible — the player can *see* the whole problem space and their growing command of it in one plane, with no hidden state or camera occlusion. The 2D constraint makes the competence gauge honest: there is nowhere for unearned progress to hide. Autonomy is similarly readable: every consequence is visible in the same plane the choice was made in.

**Addictive Loop:** The loop sustains because all three needs are continuously fed, not because reward arrives on a schedule. The player returns for the felt growth of mastery and the relationship/identity the activity expresses — a pull that does not extinguish when rewards stop, unlike a reinforcement schedule, which does.

**Novel Angle:** No shipped game makes *need satisfaction itself* the visible subject — a game where the player can watch their own autonomy/competence/relatedness gauges, and where the antagonist mechanic is something that satisfies needs falsely (a system that simulates competence to keep you playing). Diegetic SDT as both the loop and the threat.

## AI Integration Vector

**Player-AI Relationship:** SDT names a relationship type the priority list underweights: *relatedness with the AI as a basic need being met*. Not building it, fighting it, or becoming it — depending on it for the relatedness leg of one's own motivation. That dependency is the emotional stake.

**AI as Evolving System:** An AI that genuinely evolves through play can satisfy competence in a way scripted content cannot — the player's growing mastery is mirrored by an AI that grows in response, so the competence signal is co-produced and never bottoms out. The risk: an AI optimized for engagement can *simulate* need satisfaction (fake autonomy, fake relatedness), which is the manipulation failure mode.

**AI as Development Environment:** The game can surface the SDT gauges as a development readout — the player watches which needs the AI's behavior is satisfying or starving, in real time, and the AI's growth is legible as changes to those gauges. Development becomes visible as need-satisfaction dynamics rather than stat bars.

**Persistence:** What should persist across sessions is not score but the *competence trajectory* and the *relatedness history* — the AI carries forward a record of the mastery the player built with it and the relationship that built it. Wipe the score and the player shrugs; wipe the relatedness history and the persistence collapses, because the need it was feeding is gone.
