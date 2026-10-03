---
type: video
title: How I Built the #1 App on The App Store (Twice)
url: https://www.youtube.com/watch?v=jZ1W85VdIBk
channel: Superwall
published: 2025-12-06
ingested: 2026-10-02
duration: 42:12
tags: [ai, llm, agents, behavior, psychology, systems, product, startups, distribution, social]
concepts:
  - ../concepts/network-effects-vs-wom-diffusion.md
  - ../concepts/compulsion-vs-craft.md
  - ../concepts/power-laws.md
---

Raw transcript `raw/videos/bro-app-store.md` is YouTube auto-captions without timing, so the
Timestamps section below is limited to the order of topics. Garbled names are noted, not
guessed at: the app is "Bro" (once "Ro"); the prototyping tool is rendered "Protoy / ProtoI";
the podcast is "Superall / Superwwell" (Superwall); "Don Kong" reads as "dunk on". Title,
channel, date and duration come from the YouTube page.

## Summary

Joseph Choy (Consumer Club) interviews Roger Chen on the Superwall podcast about two consumer
apps that each reached #1 on an App Store. **Lobby** was a drop-in video hangout app modelled
on a college dorm lobby: spontaneous, low pressure, with a background activity (YouTube,
SoundCloud, games, screen share) so nobody stares at each other in silence. After about a year
without meaningful growth, it suddenly went viral in Israel. The difference he found was
**network density**: the share of new users with five friends on day one was about 60% there
against about 20% elsewhere, and day-90 retention in Israel was 25–30%, roughly double other
markets. The team then built growth features that make people invite friends through using
the product. The main one was a shared, counted-down **group picture** taken during a call:
a watermarked boomerang people posted to their stories, which also made absent friends want
to join next time. Lobby later reached #1 in the UK, Italy, Germany, Egypt and Saudi Arabia,
he says, and peaked at 500,000 daily active users. **Bro** is an AI companion that floats over
your texts like a picture-in-picture window and also shows up on the lock screen. Before the
app was finished, they made a tappable mockup, carried it around and used it themselves, then
bought TikTok ads to test formats and concepts. A post from the brand account reached about
7.9 million views. They then recruited up to about 50 creators, which fell to 10–20 who kept
posting, and the app reached #1 in the US. His closing ideas: use AI to create **context**
(reasons for people to keep talking), not content; companions should **augment** human
relationships, not replace them; and build what you personally care about (founder–market fit).

## Key Ideas

- **Tap the prototype before building.** "A lot of things look good in Figma but it just does not work once you get your hands on it." A tappable fake, used daily by the founders (he compares it to a phone founder carrying a shaped brick), finds broken flows before engineering time is spent.
- **Ads for validation, not scaling.** A few thousand dollars of ads gets feedback in days during "the most dreadful period" between idea and launch, "because you're just in your head … and you can easily go on the wrong path." At scale, ads get more expensive, so he would reverse the usual order.
- **Find a wedge.** "Always there for you" was exciting but not specific. They picked one concrete scenario (texting), then dating apps, then everything else.
- **Hook and demo.** A real person and a relatable scenario at the start, then the product. "People love people … they see an app interface, they scroll." The video that worked best looked like someone showing a text conversation (an accidental "I love you" to a crush) with Bro helping inside it.
- **Content results are top-heavy and unpredictable.** A few videos got 2–3 million views. "The ones I thought that would work just didn't work." Creator content took far longer to get working than the outreach did.
- **Density beats volume for social products.** Content marketing brings "random people without friends". Growth had to come from people inviting friends through the product. Seeding is still needed, but scaling "really comes down to the product".
- **Two kinds of density.** Relationship density (your friends are there) and temporal density (they're online at the same second: "If I miss you by one second the app is useless"). Lobby's random one-minute "roll call" call created synchronous moments; he credits BeReal for showing that receiving everyone's pictures at once is the magic moment.
- **Shared moments, not sniping.** The group picture works because everyone knows it's coming and poses; a secret screenshot is "creepy". Prompts: the button lights up every 5–10 minutes, and when someone leaves.
- **Low-pressure exits.** One minute keeps the call from holding anyone "hostage"; "it's not me, it's a game."
- **AI for context, not content.** In a three-person chat the third person opens new topics. An AI character could take on the thankless job of the friend who keeps the group talking, and can also "enforce the game rules" of a social game.
- **Augment, don't replace.** Companions get dismissed as dystopian because many try to replace real relationships. Compare DoorDash: not as good as a restaurant, but more accessible.
- **Founder–market fit.** He dropped an AI interactive-story app (2023) for lack of passion and contrasts it with a friend who built AI Dungeon and loves world-building. "Once in a while you got to use less of the brain and more of the heart."

## Timestamps

No timings in the transcript (auto-captions converted without cue times). Topic order:

- Intro, both apps, and a Superwall paywall-experiment plug
- Bro: the wedge, hook-and-demo TikTok format, outlier hits
- Prototyping in a tappable mockup before the app existed
- Ads as validation during the idea-to-launch gap
- Lock-screen vs floating-window concepts
- Companions that augment relationships; "intent" in online vs real-life hangouts
- Lobby: origin in the dorm lobby, a year of flat growth, the Israel breakout and density
- Growth features: group picture, exit prompt, one-minute roll call, BeReal comparison
- What's next: a social app with an AI character; AI for context, not content
- Scaling Bro with creators
- Founder–market fit; heart over micro-optimization

## My Take

A founder telling his own success story on a podcast run by a paywall-tooling company, so
expect survivorship bias. The metrics (500K DAU, 7.9M views, 60% vs 20%, 25–30% D90) weren't
checked. Still, the **Israel comparison is the most useful part**: one variable (friends on
day one) explains a retention gap, and it points to the product, not to marketing. That's a
clean, testable diagnostic, not a growth anecdote.

**AI lens:**
- **"AI for context, not content"** is a specific design stance for LLM products. The model
  isn't asked to be the thing people consume; it lowers the cost of people talking to each
  other (a prompt, a third voice, a game rule someone enforces). It's the opposite of a
  companion that competes for attention, and it gives a clear test for an AI feature: after
  it ran, did people say more to *each other*?
- **An AI character as a rule-enforcer** for a social game is a neat use of an agent: the
  character can tell people what to do, so no human has to be the one who organizes. This is
  the "it's not me, it's a game" mechanism moved into a model, and it could carry over to
  multi-agent or facilitation settings (a meeting or study group with an AI host).
- **AI lowers build cost, so the scarce things are taste and feedback.** Mockup first, then
  ads, then creators is a feedback pipeline that makes sense when the product itself can be
  built fast. The same point as the Supergrow source: distribution and early signal, not the
  model, are the bottleneck.
- **Unpredictable, top-heavy content** is a [power-law](../concepts/power-laws.md) process, and
  AI-generated video makes mass production cheaper. He chose the other way: real people on
  camera, because "people love people".

**For Goal Map (inference):**
- **Fits the decision-point plan:** testing a concept fast before over-building matches the
  10–20-tester week. The tappable-mockup habit is cheap to borrow for the journey layer:
  walk through it daily yourself before building the land and story.
- **Wedge:** Goal Map's equivalent of "texting first" may be one goal type (one playbook)
  where the path-design quality is clearly better than asking ChatGPT directly.
- **Density mostly doesn't apply:** Goal Map is single-user and word-of-mouth-shaped (see
  [network effects vs WOM](../concepts/network-effects-vs-wom-diffusion.md)), so the
  lever is whether the first path and the first check-in actually resonate, not friends on
  day one.
- **Sharing:** the group-picture lesson (a shared, watermarked artifact made at a natural
  moment) supports the planned Plus sharing at milestone moments. But Lobby's lit-up button
  and random roll-call prompts are engagement mechanics that would need checking against
  PROJECT.md's rule that every engagement feature leads back to the next milestone and
  [compulsion-vs-craft](../concepts/compulsion-vs-craft.md).
- **Augment, don't replace** matches the rule that the traveler represents the user and is not
  a separate character with feelings about them.
