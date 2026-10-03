---
type: article
title: "Play, watch, share: the dissemination of the cultural presence of games on video-based social media"
url: https://www.nature.com/articles/s41599-025-05112-3
author: Qiaohe Zhang, Yixuan Shao, Xu Li
published: 2025-07-22
ingested: 2026-08-30
tags: [games, culture, social-media, emotion, china, diffusion]
concepts:
  - ../concepts/network-effects-vs-wom-diffusion.md
---

## Summary

An academic study (Humanities and Social Sciences Communications) analyzing how
*Black Myth: Wukong* — the first AAA Chinese digital game — became a cultural
phenomenon rather than just a hit product, using Interaction Ritual (IR) chain theory
and digital emotional contagion (DEC) as the analytical frame. The authors collected
462 videos and ~78,000 Danmaku (real-time scrolling comments) from Bilibili, using a
YOLOv8-based computer-vision model to detect streamer facial emotion in sync with video
timestamps, plus TF-IDF/LDA text analysis on the comment stream. They analyze three
levels: (1) player perspective — human-computer interaction during play, where
emotional contagion clusters around game animations, characters, story, and gameplay,
and progresses from sensory identification (visual/audio/tactile response) through
group identification (game rules, roles, shared understanding) to emotional
identification (story background, identity projection, emotional resonance); (2) game
perspective — how game information itself spreads through evaluation videos, moving
from operation-stage topics (graphics, mechanics) through narrative-stage topics (plot
adaptation, cultural connotation) to culture-stage topics (business, rating
controversy, social discourse); (3) video perspective — how the 462 videos, sorted into
9 content types, disseminate across platforms, revealing an inverse relationship
between a video's closeness to the game itself and its cross-platform reach (strongly
game-related content stays within the player community; weakly game-related content —
music covers, cosplay, lifestyle videos — travels furthest and recruits non-players by
grafting game symbols onto pre-existing cultural forms).

## Key Points

- Cultural presence is not passive absorption but an active ritual process: shared
  attention + emotional synchronization + symbol sharing produce group identity, which
  is the mechanism by which a "hit game" becomes a "cultural phenomenon."
- Three-stage progression (both at the individual player level and at the aggregate
  discourse level): sensory/operational engagement → narrative/experiential engagement
  → cultural/social engagement. Each stage widens the audience and raises the stakes of
  the content (from "is this fun" to "what does this mean for national culture").
- The inverse relationship between game-relevance and dissemination breadth is the
  paper's sharpest finding: content that most resembles "playing the game" stays inside
  the existing player community (Bilibili functions as a high-context, jargon-gated
  space); content that's least game-specific (a folk-music cover of the soundtrack, a
  cosplay performance) is what actually recruits new audiences, because it requires no
  prior game literacy to appreciate.
- Different platforms shape different diffusion patterns: Bilibili rewards deep
  specialization via in-group "argot" and algorithmic precision-matching; cross-platform
  spread (e.g. to TikTok/Douyin) favors pan-cultural, broadly legible symbols and
  hotspot-driven algorithmic amplification.
- The study explicitly frames this as a template for cultural-heritage promotion —
  governments/platforms could deliberately design "gamification of traditional
  culture" using this diffusion model.

## My Take

The methodology is itself an AI story worth noting separately from the findings: the
researchers built a custom real-time facial-emotion-detection pipeline (YOLOv8) to
capture streamer emotion in sync with viewer comments — this is a case of AI-as-
research-instrument, using computer vision to make a previously unmeasurable variable
(felt emotion during play, at scale, across hundreds of videos) tractable for social
science. On the substantive finding: the inverse relationship between content's
closeness to the "product" and its dissemination breadth is a strong, generalizable
principle for AI-driven virality more broadly — it suggests that content *about* an AI
system that requires no literacy in the system (a meme, a reaction, a cultural
remix) will always outrun content that demonstrates the system's actual capability,
because the former has a lower comprehension floor. This has direct implications for
how any AI product's cultural footprint forms: the product's own demo videos stay
inside the community that already understands it; what actually crosses into public
consciousness is the least technical, most remixable artifact adjacent to it.

## Related

[How Single-Player and Multiplayer Games Spread](single-multiplayer-diffusion-social-networks.md) —
the general framework this paper's single-player case exemplifies. [Quick take: Word of
mouth](word-of-mouth-discovery-midia.md) — discovery-channel data referenced across this
cluster.
