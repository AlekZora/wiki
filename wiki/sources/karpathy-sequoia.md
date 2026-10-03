---
type: video
title: "Andrej Karpathy at Sequoia: Vibe Coding, Agentic Engineering, and Software 3.0"
url: 
channel: Sequoia Capital
published: 
ingested: 2026-04-30
duration: 
tags: [ai, llm, tool, philosophy]
concepts: [vibe-coding, agentic-engineering, software-3-0, jagged-intelligence, llm-as-computer]
---

## Summary

Andrej Karpathy speaks at a Sequoia Capital event about the shift he experienced in December (presumably 2024) when agentic AI coding tools crossed a threshold where he stopped correcting them and started trusting them fully — what he coined as "vibe coding." He frames this as part of a larger paradigm shift he calls Software 3.0, where programming becomes prompting and the LLM is the interpreter. He distinguishes vibe coding (raising the floor for everyone) from agentic engineering (preserving quality while going faster), discusses "jagged intelligence" as a mental model for LLM capabilities, and closes on the importance of human understanding as the irreducible bottleneck even when AI does the thinking.

## Timestamps

- 00:00 — Introduction by host; Karpathy introduced as co-founder of OpenAI, Tesla Autopilot lead, and coiner of "vibe coding"
- early — Karpathy describes December as the inflection point where agentic tools stopped needing correction; he started fully trusting them and "vibe coding all the time"
- mid — Software 1.0 / 2.0 / 3.0 framework: explicit code → learned weights → prompting the LLM as interpreter; context window is the lever
- mid — MenuGen example: vibe-coded app that photos a restaurant menu and generates images of each dish; deployed on Vercel; illustrates the shift but also friction of non-agent-native infrastructure
- mid — "Jagged intelligence": LLMs have uneven, spiky capabilities; performance depends on whether your use-case falls inside or outside the training/RL distribution; fine-tuning needed when outside
- mid — Chess capability spike in GPT-4o explained by chess data entering pre-training; illustrates how capability is at the mercy of what labs put in the mix
- mid-late — Vibe coding vs. agentic engineering: vibe coding raises the floor; agentic engineering preserves the quality bar of professional software while going faster; 10x engineer multiplier is now far larger
- mid-late — Founder advice: verifiable domains are tractable because you can apply RL; build your own fine-tuning environments if labs aren't focused on your niche
- late — Agent-native infrastructure: everything still written for humans; Karpathy's pet peeve is docs that tell you what to do rather than giving you the prompt to paste to your agent
- late — Education and understanding: "You can outsource your thinking but you can't outsource your understanding"; human remains the bottleneck for directing agents; LLM knowledge bases as tools for enhancing personal understanding

## Key Ideas

- Karpathy's December inflection point: agentic tools went from helpful-but-flawed to fully trustworthy; he stopped correcting them entirely.
- Software 3.0 reframes programming as prompting: the context window is your source code; the LLM is the interpreter. Claude Code's install-via-paste-to-agent is the canonical example of this shift.
- Vibe coding vs. agentic engineering are distinct: one democratizes creation, the other disciplines it. Both matter, but conflating them creates problems (e.g., shipping vulnerabilities).
- Jagged intelligence: LLM capability is not uniform. It peaks inside RL-trained or heavily-represented domains and drops sharply outside them. Knowing which "circuits" your problem sits in is critical.
- Agent-native infrastructure is still largely missing. Most tools, docs, and deployment flows are designed for human hands. Karpathy sees this as a major friction point and opportunity.
- Human understanding remains irreplaceable as the director of agents. You can delegate execution but you cannot delegate the judgment about what to build and why.
- The 10x engineer multiplier has exploded. People skilled at agentic engineering appear to operate well beyond 10x relative to before.

## My Take

The Software 1.0/2.0/3.0 framing is clean and useful — I've seen it referenced elsewhere but hearing Karpathy explain it through concrete examples (OpenClaw install, MenuGen) makes it stick. The vibe coding vs. agentic engineering distinction feels important for anyone building production software: the temptation is to vibe code everything, but the discipline is agentic engineering.

The jagged intelligence framing is a practical tool for evaluating whether to use off-the-shelf LLMs or fine-tune — if your domain isn't in the RL circuits, you're going to fight the model constantly.

The closing point about understanding as the irreducible bottleneck hits close to home. Building a wiki like this one is exactly the kind of "synthetic data generation over fixed data" Karpathy describes as how he processes information and maintains understanding.
