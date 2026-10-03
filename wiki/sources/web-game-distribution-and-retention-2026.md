---
type: article
title: "Web game distribution, portal requirements and retention benchmarks (2026) — research synthesis"
url: https://app.cinevva.com/guides/web-game-monetization
author: Synthesis across Cinevva, CrazyGames developer docs, Game Growth Advisor, Playio and MobiLoud
published: 2026
ingested: 2026-09-21
tags: [game-design, distribution, monetization, retention, web, benchmarks, business]
concepts:
  - ../concepts/backward-chain-game-design.md
  - ../concepts/retention-proxy-testing.md
  - ../concepts/compulsion-vs-craft.md
---

## Summary

Gathered 2026-09-21 to supply the commercial constraints the basic-game project derives
backward from. Web game revenue is a product of five terms and a solo developer controls two of
them. Portals publish hard technical gates and split ad revenue at rates differing by more than
2×. Retention benchmarks exist but are thinner and noisier than their circulation suggests —
one of these sources says outright that no verified 2026 genre breakdown exists beyond
casual/puzzle and that the grids people quote are unverified folklore.

**Provenance warning.** No raw file; this is outside general knowledge from public web guides,
not from primary portal terms or first-party analytics. Every figure should be re-verified
before it drives a spending decision. Revenue shares in particular are reported by third-party
guides rather than the portals themselves.

## Key Points

**Portal revenue shares (developer's cut of ads).** Poki 50% on Poki-sourced traffic and 100%
on self-directed traffic; CrazyGames 60% ads / 70% IAP; Playgama Bridge 80%; GameMonetize 45%;
GameDistribution 33%; itch.io developer-set, default 10% platform cut.

**Ad rates, gross eCPM before the split.** Rewarded video — US $15–28, EU $8–15, tier-3 markets
$1–3. In-game intrinsic brand placement $2–6.

**Realistic earnings.** ~80% of paid itch.io games earn under $50/month; most earn under $100
lifetime. Well-performing casual games on ad portals $200–$2,000/month. One cited portfolio
figure: ~EUR 1.20 per thousand plays.

**CrazyGames technical gates.** Basic launch — initial download ≤50MB, total ≤250MB, ≤1500
files, PEGI12, visual QA; SDK optional but monetization disabled. Full launch — SDK and a
Gameplay Start event mandatory, ads via SDK and must work with AdBlock, progress linked to
CrazyGames accounts, and the game must **land directly in gameplay** rather than open on menus.
50k combined plays unlocks dedicated technical support.

**Retention.** Whole-market medians D1 ~22%, D7 3.4–3.9%, D30 0.68–0.79%. Casual/puzzle on
Android D1 28–32%, D7 9–12%, D30 3.5–5%. Widely repeated "good" target 35/15/5; top quartile
40/20/10+. Subscription apps ~14% D30 against 5.4% for ad-supported.

**Sessions.** Median session 3.1–3.5 min, 3.8–3.9 sessions/day, ~12 min daily playtime. Top 1%:
22–24+ min, 12–14+ sessions, 94–99+ min daily.

**Per-user revenue.** Ad-only casual ARPDAU $0.01–$0.05; hybrid casual $0.15–$0.50.

**Apple review, for a later iOS port.** Guideline 4.2 (minimum functionality) is the live risk:
an app must "include features, content, and UI that elevate it beyond a repackaged website."
Rejection triggers are web navigation instead of native UI, no platform integration, no distinct
value over the browser. Webview technology is not itself prohibited; thin execution is what gets
rejected.

## Quotes

> "Initial download size ≤ 50MB … Land directly in gameplay."
> — CrazyGames requirements

> "[Apps must] include features, content, and UI that elevate it beyond a repackaged website."
> — App Store Review Guidelines, 4.2, as quoted by MobiLoud

## My Take

**The decomposition is the finding, not the numbers.** Revenue is
`plays × sessions-per-player × ads-per-session × eCPM × rev-share`. eCPM is set by the player's
geography, rev-share by the portal, and plays by the portal's recommendation algorithm. A solo
developer directly controls sessions-per-player and ads-per-session, and only the first
compounds.

**Retention is upstream of the term you don't control.** Portals promote what retains, so
retention buys plays as well as converting them. That makes it the single highest-leverage
design variable rather than one KPI among several — and it means the stated project goal
("hardest to put down") and the revenue equation select for the same thing. There is no
stickiness-versus-earnings tradeoff to manage here.

**"Land directly in gameplay" is a design rule wearing a technical-requirement costume.** It
forbids a title screen, a tutorial gate and a difficulty selector. It has to be designed for,
not patched in — and it interacts badly with the legibility-testing problem in
[Comprehension Floor](../concepts/comprehension-floor.md), since the on-screen legend that makes
a game readable on arrival is the same artifact that spends your naive testers.

**The 50MB ceiling is a stack decision**, effectively ruling out a heavyweight engine export for
a fast solo build and favouring hand-written TypeScript over Canvas or minimal WebGL.

**Self-directed traffic changes the economics more than portal choice does.** Poki paying 100%
on traffic you bring means a modest owned audience is worth more per play than a better split —
which is an argument for the distribution approach already sketched in
[The Attractor Zone](../projects/attractor/attractor-zone.md).

**The benchmarks deserve less trust than their precision implies.** With market D7 at ~3.5% and
the honest admission that genre grids are folklore, the planning posture is to treat published
figures as order-of-magnitude orientation and to trust first-party numbers over any of them.
This is [The Metrics Trap](../concepts/metrics-trap.md) arriving early: the numbers are
diagnostic instruments, and the moment one becomes the target it stops measuring the thing.

**The iOS decision has an architectural deadline.** Guideline 4.2 compliance means native hooks
must be planned before the web architecture is locked, even if built months later.

## Cross-Reference Checklist

- [Backward-Chain Game Design](../concepts/backward-chain-game-design.md) — the method these
  figures feed
- [Retention Proxy Testing](../concepts/retention-proxy-testing.md) — what to do when you cannot
  wait for these numbers
- [Compulsion vs Craft](../concepts/compulsion-vs-craft.md) — which mechanisms move
  sessions-per-player, and at what cost
- [The Metrics Trap](../concepts/metrics-trap.md) — why the benchmark table is an instrument and
  not a goal
- [Comprehension Floor](../concepts/comprehension-floor.md) — the collision between landing
  directly in gameplay and being able to test legibility
- [Network Effects vs. WOM Diffusion](../concepts/network-effects-vs-wom-diffusion.md) — the
  self-directed traffic term

## Project Connection

Supplies Phase 0 of [Basic Game — Pipeline](../projects/basic-game/pipeline.md) and populates
the portal and benchmark tables in
[constraint-sheet.md](../projects/basic-game/constraint-sheet.md). Also bears on Attractor,
which is already live on itch.io — the Poki self-directed-traffic term and the CrazyGames gates
are both live options for it, and neither has been evaluated.

## Sources

- https://app.cinevva.com/guides/web-game-monetization
- https://docs.crazygames.com/requirements/intro/
- https://gamegrowthadvisor.com/blog/2026-03-17-mobile-game-kpis-benchmarks-2026/
- https://blog.playio.co/d1-d7-d30-retention-benchmarks-2026
- https://www.mobiloud.com/blog/app-store-review-guidelines-webview-wrapper/

## Uncertainty

- Revenue shares and eCPM ranges are third-party reported, not from portal terms pages.
- Sources are inconsistent about whether quoted eCPMs are pre- or post-split.
- No verified 2026 retention breakdown exists for hypercasual or arcade; 35/15/5 is widely
  repeated and weakly sourced.
- CrazyGames requirements are current as of the fetch date and change without notice.
- Apple's Guideline 4.7 treatment of HTML5 mini-apps was not confirmed against a primary Apple
  source and remains open.
