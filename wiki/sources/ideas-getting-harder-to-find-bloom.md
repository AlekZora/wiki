---
type: article
title: "Are Ideas Getting Harder to Find?"
url: https://doi.org/10.1257/aer.20180338
author: Nicholas Bloom, Charles I. Jones, John Van Reenen, and Michael Webb
published: 2020-04
ingested: 2026-07-15
tags: [economics, growth-theory, innovation, research, ai, scaling, moores-law, systems]
concepts: [diminishing-research-returns]
---

## Summary

This American Economic Review paper (110(4): 1104–1144) tests a core assumption behind most growth theory: that a constant number of researchers can sustain constant exponential growth. The authors define research productivity as new ideas produced per researcher, and measure it directly at the micro level across several very different domains — Moore's Law in semiconductors, crop yields (corn, soybeans, cotton, wheat), medical research (new drugs, cancer and heart-disease mortality), and firm-level data from Compustat and the US Census of Manufacturing. In every case, research effort (the number of "effective researchers," measured by deflating R&D spending by wages) has risen sharply — often by a factor of 10–40 over the sample period — while research productivity has fallen just as sharply, at rates typically between 3% and 15% per year. The clearest example is Moore's Law: it now takes roughly 18 times more researchers to keep chip density doubling every two years than it did in 1971, even though the growth rate itself hasn't changed. Applied to the aggregate US economy since the 1930s, research productivity has declined by a factor of 41, and the economy must roughly double its research effort every 13 years just to sustain the same rate of growth. The authors argue this is consistent with "semi-endogenous" growth models, in which the idea production function includes a term that makes it progressively harder to generate constant exponential growth as the existing stock of ideas grows — a "Red Queen" dynamic where you must run faster and faster just to stay in place.

## Key Points

- Core equation: Economic growth = Research productivity × Number of researchers. Research productivity is falling; researchers are rising; the product stays roughly constant, which is why aggregate growth looks stable even as the underlying process is not.
- Moore's Law: transistor density has doubled every two years (35%/year) since 1971 with remarkable stability, but the number of researchers needed to sustain that has grown by a factor of 18 — research productivity in semiconductors fell at ~6.8%/year.
- Agriculture: research effort on corn and soybean yields rose by a factor of ~23 since 1969, while yield growth stayed roughly flat — research productivity fell by ~6%/year (narrow) to ~4%/year (broad) on average across crops.
- Medicine: new molecular entities per R&D dollar fell by a factor of 5 (1970–2014, factor of 11 by 2007 before recovering some). Years-of-life-saved per clinical-trial publication for cancer and heart disease declined by factors of 5–25 (1975–2011), though productivity rose in the earliest years (1975–mid-1980s) before falling — the decline is not monotonic in every case.
- Firm-level evidence (Compustat, 1980–2015 and US Census of Manufacturing, 1982–2012): research productivity falls at roughly 4–15%/year depending on the outcome measure (sales, market cap, employment). Less than 5% of firms show roughly constant research productivity — decline is the norm, not an artifact of a few cases.
- Aggregate US economy: research effort (deflated R&D spending) rose by a factor of 23 since the 1930s; research productivity fell by a factor of 41 (~5.1%/year), implying a half-life of about 13 years.
- Semi-endogenous growth formalization: Ȧ/A = α·A^(−β)·S, where A is the stock of ideas/quality, S is research effort, and β measures how fast diminishing returns set in as A grows. Semiconductors have the *smallest* β (~0.2) of any case studied — meaning they have the least diminishing returns of anything measured — yet productivity still falls fastest there simply because research effort in that sector is growing fastest of all.
- The paper explicitly frames its finding as a "Red Queen" problem (citing Lewis Carroll's Through the Looking-Glass): constant growth requires running twice as fast just to stay in the same place.
- Caveat acknowledged by the authors: any unmeasured input to research (spillovers, "garage" innovation, business improvements from workers) gets folded into the measured productivity decline. If such inputs are themselves growing fast and going uncounted, the true decline could be smaller than measured — or the measured decline could understate it if those inputs are growing even faster than what's captured.

## Quotes

> "More generally, everywhere we look we find that ideas, and the exponential growth they imply, are getting harder to find."

> "Perhaps a more accurate title for this paper would be 'Is Exponential Growth Getting Harder to Achieve?'"

> "Research productivity is falling sharply everywhere we look. Taking the US aggregate number as representative, research productivity falls in half every 13 years: ideas are getting harder and harder to find. Put differently, just to sustain constant growth in GDP per person, the United States must double the amount of research effort every 13 years to offset the increased difficulty of finding new ideas."

> "Now, here, you see, it takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!" (Lewis Carroll, quoted by the authors as the "Red Queen" framing for their semi-endogenous growth result)

## My Take

The direct AI intersection is structural, not incidental: this paper's central relationship — output grows at a constant rate only if input (researchers) grows exponentially, because the marginal cost of the next idea rises as the existing stock of ideas grows — is the same functional form behind neural scaling laws (Kaplan et al. 2020; Chinchilla, 2022). Frontier AI labs face exactly the β this paper measures: constant-rate reductions in model loss require exponentially more compute and data, and the whole "scaling laws are slowing" debate in AI right now is a live instance of the question this paper asks about semiconductors, crops, and drugs. Semiconductors are the paper's own case with the *smallest* diminishing returns of anything they study (β≈0.2) — and semiconductors are literally the substrate AI training rides on. As chip-density gains from Moore's Law continue slowing, that's one more exogenous drag layered under AI's own scaling curve, which is part of why the field has shifted so hard toward algorithmic efficiency and inference-time (test-time) compute — trying to buy capability gains from a channel that hasn't yet hit the same diminishing returns.

The more interesting angle is the paper's own caveat about missing inputs. They note that anything they fail to measure (spillovers, uncounted "garage" effort) gets silently absorbed into the productivity decline they report. AI-as-researcher is exactly this kind of missing input, deployed deliberately: if AI can substitute for or augment the S_t term (the human researchers doing the work) without the same wage and training-time cost as growing the human research population, it's a genuine candidate for the first structural break in a trend this paper traces back to the 1930s — decoupling "more effective research effort" from "more human capital," which is the actual bottleneck the equation describes. That's the strongest economic argument I've seen for why AI-accelerated science (automated hypothesis generation, experiment design, and verification loops) matters more than incremental productivity gains elsewhere: it targets the exact term that has been driving the Red Queen effect for a century.

There's also a smaller, more personal parallel: any system that accumulates state over time — a knowledge base, a codebase, an agent's memory store — should expect the same curve by default. As accumulated state (this wiki's A, in the paper's notation) grows, the marginal value of the next unit of undirected research effort tends to fall, unless the system finds a way to raise its own effective β — e.g., by using accumulated state to make retrieval and synthesis more targeted instead of scanning more broadly. Worth keeping in mind as a general skepticism check on "just add more compute/more scanning" as a strategy for anything cumulative.

