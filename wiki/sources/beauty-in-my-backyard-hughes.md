---
type: article
title: "Beauty In My Backyard"
url: "https://worksinprogress.co/issue/beauty-in-my-backyard/"
author: Samuel Hughes
published: 2026-07-29
ingested: 2026-08-02
tags: [architecture, systems, economics, psychology, history, design, preferences]
concepts: [diffuse-preference-aggregation]
---

## Summary

Hughes argues that ugly architecture does block housebuilding, but not through the
mechanism usually claimed. The standard theory says local residents resent having
ugliness inflicted on them and therefore oppose development; Hughes thinks ugliness
plays only a minor role in motivating that local opposition, since local objectors
have plenty of other concerns (construction disruption, lost green space, pressure on
services, diminished social exclusivity) and since demonstrably beautiful schemes still
attract fierce local resistance. His alternative is that ugliness drives opposition
among people who live nowhere near the development — NIMBYs ("not in my backyard")
versus what he coins **NITBYs**, "not in *that* backyard." NITBYs are mostly only
casually interested and their motives are faint but basically altruistic: they are
asking whether, on a cursory look, a development improves its neighborhood. Individually
weak, they aggregate into a potent political force. Hughes applies this to heritage
conservation, arguing against both dominant explanations of why it triumphed so fast.
It was not a reaction to unprecedented postwar destruction, because earlier generations
destroyed at least as much without provoking resistance; and it was not a NIMBY pretext,
because NIMBYism had already won decades earlier and conservation protects many places
NIMBYs do not live. What actually changed was that modernist architecture — a style most
people demonstrably dislike — became dominant in the 1950s, so redevelopment switched
from being aesthetically neutral to being uglifying. Conservationism was a reaction to
postwar redevelopment, but less to what modernists destroyed than to what they built.

## Key Points

- **The sequencing refutes the standard NIMBY-ugliness story.** Restrictive zoning
  emerged in Germany and Austria-Hungary in the 1890s and spread fast — Italy in the
  1900s, Britain 1909, France 1919, the US across the interwar period. Modernism emerged
  only in the 1920s and did not triumph globally until the 1950s. The Great Downzoning
  therefore happened while most new buildings were still traditional in style. NIMBYism
  won long before the average new building was widely considered uglier than the average
  old one.
- **The sequencing also refutes the pretext theory.** If conservationism were a NIMBY
  cover story, the 40-to-70-year gap is inexplicable: why invent it in the 1960s, long
  after NIMBYs had already protected their suburbs by other means?
- **Postwar planners were not unusually destructive.** Paris retains only two fully
  intact timber-framed houses out of what were once tens of thousands, destroyed by
  ordinary redevelopment rather than fire or war. Of roughly 100,000 homes in the
  brick-built London of 1700, only 100–200 survive — a destruction rate of about 99.8
  percent, more thorough than the Great Fire. Fewer than twenty buildings of any kind
  survive in New York from before 1800. Roughly three quarters of Manhattan's Gilded Age
  urban palaces were demolished in a short burst in the late 1920s.
- **Conservation then brought demolition almost to a standstill.** France demolished 1.8
  percent of pre-1949 dwellings between 1999 and 2013. Berlin demolished nine pre-1919
  buildings in 2022 out of 50,337. At North Rhine-Westphalia's 2023 rate it would take
  7,951 years to clear its prewar stock. Britain's count of pre-1919 dwellings actually
  *rose* between 2012 and 2024 through subdivision.
- **Conservation's priorities are NITBY, not NIMBY.** It protects working-class housing,
  commercial downtowns, public buildings, isolated country houses and rural churches —
  categories where NIMBYs are scarce or absent — and often affects those more than
  suburbs, which zoning had already protected.
- **The 'L transect' as evidence.** Cities with little historic stock (Melbourne, Miami,
  Toronto, Calgary, Brisbane) have densified sharply at the core while their suburbs stay
  petrified: strong local NIMBYism, weak NITBY conservation. European centers, where the
  historic stock is concentrated, have been frozen almost completely since 1960.
- **The Blitz as a natural experiment.** One study found bomb damage ultimately made
  London's economy 10 percent larger by enabling higher densities on former bomb sites.
  Under a purely NIMBY account this is inexplicable — sites randomly cleared to zero
  density should, if anything, end up denser-resistant. It makes sense if the binding
  constraint is NITBY protection of heritage fabric rather than local objection to density.
- **The railway exception is a second natural experiment.** Nineteenth-century railways
  produced steam and coal smoke and were seen as blights, and there are almost no cases
  of a railway being cut through a city center — hence the ring of termini around London
  and Paris. On the one kind of infrastructure Victorians found overwhelmingly ugly, they
  behaved exactly like twentieth-century conservationists.
- **Conservationists barely defend modernist heritage.** England had listed about 300
  postwar buildings as of 2003 and roughly 500 by 2015, out of some 375,000 listed
  buildings. The American National Register applies a blanket fifty-year rule.
- **Motive and stated reason diverge.** Hughes suspects conservationists were appalled by
  uglification but sublimated a preference for beauty into a preference for age, because
  attacking high-status modernism directly invited charges of pastiche-mongering.

## Quotes

> "Conservationism was a reaction to postwar redevelopment, as its proponents claimed.
> But it was less a reaction to what the modernists destroyed, than to what they created."

> "In other words, many conservationists secretly love old buildings because they are
> beautiful, while pretending to love them because they are old."

> "Commercial public works, of a magnitude unrivalled since the days of imperial Rome…
> are educating our workmen, from the lowest to the highest, to a style of craftsmanship
> entirely unknown in this country at the commencement of the present century." — *The
> Builder*, 1868, on the belief that architecture was steadily improving

> "So long as people feel this, they will never tolerate the large-scale destruction of
> historic building stock, no matter what ingenious arguments YIMBYs make for it. Their
> dread of ugliness will hang over our cities like a curse, freezing them in the last
> moment of their beauty."

## My Take

Three things here bear directly on AI, and none of them are about buildings.

**The method is the most transferable part.** Hughes demolishes two dominant explanations
almost entirely on chronology — X cannot have caused Y, because Y was already in place
decades before X existed. It costs nothing and it is devastating, and it is precisely the
check that language models skip. An LLM asked why conservation laws exist will produce the
postwar-destruction story fluently, because that narrative is causally *plausible* and
overwhelmingly represented in the corpus; verifying that the dates actually permit the
causal arrow requires stepping outside narrative coherence into arithmetic. This is a
concrete, testable failure mode for any system doing historical or causal reasoning over
text, and it suggests a cheap eval: take contested causal claims where the ordering
refutes the popular story, and see whether the model checks. My guess is that retrieval
makes this *worse*, not better, since retrieval surfaces the well-represented narrative
rather than the timeline.

**The NITBY structure is a preference-aggregation problem, and it is the same shape as
RLHF.** A large population of people with faint, low-stakes, basically well-meaning
opinions about outcomes that do not affect them, aggregating into a binding constraint on
the people who actually live with the result. That is structurally identical to a rater
pool shaping a model's behavior for users whose situation the raters never encounter —
weak signal, no skin in the game, decisive in aggregate. `ideal-reader` already covers one
half of this (aggregation flattens distinctiveness); the half Hughes adds is that diffuse
preference does not merely dilute, it can *veto*, and the resulting policy is systematically
biased toward what is legible on cursory inspection. A development is judged on whether it
looks like an improvement in a photograph. So is a model response.

**Stated versus operative reasons.** Hughes's closing suspicion — that conservationists
love old buildings for their beauty while claiming to love them for their age, because the
beauty argument was socially unavailable — describes exactly what a model trained on
justifications learns. Text records the socially acceptable reason, not the operative one,
and the gap is largest precisely where the real motive is contested or low-status. Any
system attempting to model human motivation from written argument is learning the
sublimated version by construction. For the Side Quest AI project this is directly usable:
`npc.want` is the stated ask and `npc.stake` is the operative motive, and the design already
assumes those differ — Hughes gives a real-world account of *why* they differ and of which
direction the substitution runs.

## Note on attribution

The clipped file's frontmatter lost the byline (it records the site's `wip-admin`
placeholder). Authorship is attributed to Samuel Hughes on the basis of the first-person
voice and three photographs credited to him within the piece. Worth confirming against the
live page if the citation matters.
