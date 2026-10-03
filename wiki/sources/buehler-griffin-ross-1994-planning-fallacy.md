---
type: article
title: "Exploring the \"Planning Fallacy\": Why People Underestimate Their Task Completion Times"
url: http://web.mit.edu/curhan/www/docs/Articles/biases/67_J_Personality_and_Social_Psychology_366,_1994.pdf
author: Roger Buehler, Dale Griffin, Michael Ross
published: 1994
ingested: 2026-10-01
tags: [psychology, behavior, productivity, memory, ai, agents]
concepts:
  - ../concepts/planning-fallacy.md
---

*Journal of Personality and Social Psychology* 67(3), 366–381. Fetched by Claude from the MIT
faculty copy cited in the user's planning-fallacy brief. Saved as
`raw/articles/Buehler Griffin Ross 1994 - Exploring the Planning Fallacy.pdf`.

## Summary

Five studies testing three claims, all supported. (a) People underestimate how long their *own*
tasks will take, but not other people's. (b) When forecasting, they focus on plan-based
scenarios for the future rather than on relevant past experience. (c) They explain away past
failures as external, transient and specific, so the past seems irrelevant. Optimistic bias
appeared for honours theses, academic and household projects, and a computer assignment. In
Study 4, the bias was **eliminated only when people were led to connect** past experiences to
the current task. Just recalling them didn't help. In Study 5, observers forecasting someone
else's task were not optimistic. They actually overestimated the time and made more use of
past experience.

## Key Points

- **Study 1 (theses, n = 33):** best estimate 33.9 days, actual 55.5. Only **29.7%** finished by their best estimate, 10.8% by their optimistic estimate, and fewer than half (48.7%) even by their *worst-case* estimate. Estimates were still informative: r = .77 between predicted and actual. Biased, not random.
- **Studies 2–3:** academic and non-academic projects. About 37–43% finished within the predicted time. Think-aloud protocols showed people mostly considering future plans. Very few mentioned past experience or possible obstacles.
- **Study 4 (computer assignment, N = 123):** three conditions.
  - Control: underestimated by 1.3 days; 29.3% on time.
  - **Recall** (describe past similar assignments first): still underestimated by 1.0 day; 38.1% on time, not significantly better than control.
  - **Recall-relevant** (describe them *and* link them to this assignment): bias gone (−0.1 days); **60.0%** on time.
  - The authors call the null recall result "rather remarkable". People acknowledged they usually finish a day before deadlines and still forecast optimistically.
- **Attributions (Studies 3–4):** past lateness was explained by external, transient, specific causes, which makes it "not relevant this time".
- **Study 5 (observers):** people predicting a yoked actor's completion were pessimistic, and used the actor's past history more.
- **Motivation, untested here:** the authors flag accuracy incentives vs. wanting to finish early as a direction for future work.

## Quotes

> "The bias was attenuated only when subjects were induced both to consider their past experiences and to relate the experiences to the task at hand."

> "Fewer than one third of the respondents (29.7%) finished in the time they reported as their most accurate prediction."

## My Take

The primary source confirms the brief's central claim. The detail that matters for design is
**recall vs. recall-relevant**. Showing someone their history isn't enough; they have to tie it
to *this* task. The same pattern showed up in the if–then evidence, where rehearsing the link
beat holding a reminder ([implementation-intentions](../concepts/implementation-intentions.md)).
**Inference:** across both literatures, *having* information about yourself changes little, and
*linking* it to the current situation changes behaviour.

The worst-case result also matters: half the thesis writers missed even their pessimistic date.
"Add a buffer" isn't enough when people's own worst case is optimistic.

**AI lens:** the actor/observer split is the most interesting part for AI. The forecaster's
position, not their information, drives the bias. An outside system with the same history
forecasts better. That is a principled reason to put an AI (or plain code over recorded
outcomes) in the observer seat for time estimates, while keeping the person in the actor seat
for *what* to do. Untested for LLMs: whether a model prompted with the user's own optimistic
framing takes the observer position or inherits the actor's bias. See
[planning-fallacy](../concepts/planning-fallacy.md).
