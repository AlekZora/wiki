---
type: concept
title: Gradient Descent
aliases: [backpropagation, loss landscape, cost function minimization]
tags: [ai, ml, optimization, deep-learning]
sources:
  - ../sources/deeplearning-chatper-second.md
updated: 2026-05-09
---

## Definition

Gradient descent is the optimization algorithm that trains neural networks. A cost function measures how wrong the network's outputs are across all training examples, producing a single scalar. The gradient of this function with respect to every parameter points in the direction of steepest increase. Moving in the *opposite* direction — the negative gradient — decreases the cost. Repeating this iteratively causes the network to converge on a local minimum of the cost landscape.

The algorithm for efficiently computing the gradient across all parameters is called **backpropagation** — it applies the chain rule of calculus through every layer from output back to input.

## How I Think About It

The cost function lives in a space with as many dimensions as the model has parameters (13,000 for a small MNIST network; 175 billion for GPT-3). Gradient descent is like a ball rolling down a hill in this unimaginably high-dimensional space. You can't visualize it, but the math is the same.

Two uncomfortable truths follow: (1) You find a *local* minimum, not the global one — the solution you get depends on where you start. (2) The learned solution often doesn't correspond to human-interpretable features. A network trained to 96% accuracy on digit recognition may have learned patterns that look like noise to a human. Performance and interpretability are orthogonal.

## Related Concepts

- [Neural Networks](neural-networks.md)
- [Eval-Driven Development](eval-driven-development.md)

## Open Questions

- Why do very large models (LLMs) appear to avoid the worst local minima and generalize well, despite being trained in an even more complex landscape?
- Is there a cost function formulation that would produce interpretable, human-readable weight patterns in hidden layers?

## Project Connection

The concept of a "cost landscape" maps naturally to narrative generation: a story generation system is searching for a low point in a "narrative quality" space. Getting stuck in a bad local minimum could explain repetitive, clichéd outputs. Designing the cost function well (what makes a story good?) is the real design challenge — analogous to the challenge of designing reward functions for AI agents in the series.
