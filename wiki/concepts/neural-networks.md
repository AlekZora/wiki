---
type: concept
title: Neural Networks
aliases: [feedforward network, deep neural network, multilayer perceptron]
tags: [ai, ml, deep-learning, neural-networks]
sources:
  - ../sources/deep-learning.md
  - ../sources/deeplearning-chatper-second.md
updated: 2026-05-09
---

## Definition

A neural network is a highly parameterized mathematical function loosely inspired by the brain. It maps raw inputs to outputs via a series of layers, where each layer applies a weighted summation followed by a non-linear activation function. The "knowledge" of the network is stored entirely in its numerical parameters: weights and biases.

## How I Think About It

The key insight is that a deep network is *not* magic — it is a composition of simple operations organized into a hierarchy. Each layer detects progressively more abstract features: raw pixels → edges → shapes → concepts. What looks like intelligence is an emergent property of stacking many cheap linear operations with non-linearities between them.

The second key insight: "learning" is just optimization. Given a cost function that measures error, gradient descent iteratively nudges all parameters in the direction that reduces cost. The network has no understanding; it is searching a very high-dimensional surface for a low point.

## Related Concepts

- [Gradient Descent](gradient-descent.md)
- [Transformer Architecture](transformer-architecture.md)
- [Cognitive Externalization](cognitive-externalization.md)

## Open Questions

- Why do hidden layer weights in trained networks often look like noise rather than clean detectors? Is this a general phenomenon or specific to shallow/narrow architectures?
- What is the relationship between a local minimum's "depth" in the loss landscape and the generalization quality of the resulting model?

## Project Connection

The hierarchical feature composition model (low-level → high-level) is a useful metaphor for designing AI character agents in the paranoid sci-fi series. An agent's "perception" of the environment could be structured as a hierarchy: raw events → behavioral signals → inferred motive. The brittleness of networks on out-of-distribution inputs mirrors how a character operating outside their expected context will behave unpredictably — a useful narrative mechanic.

## Game Design Vector

**Mechanic:** The game world operates on hierarchical feature composition: the AI's perception builds from raw inputs (pixels, positions) through intermediate representations (edges, shapes) to high-level concepts. The player can interact at any level of this hierarchy. The AI's behavior is a function of which level the player's interactions register at. Out-of-distribution inputs — anything outside the training distribution — produce unpredictable, brittle responses. The player can discover the AI's training distribution by probing its failure edges.

**2D Expression:** In 2D, the hierarchical feature composition is legible as a layered plane: raw elements at the surface, intermediate patterns in a middle layer, conceptual structures at the depth. The AI processes the plane bottom-up; the player can read it top-down. The brittleness on out-of-distribution inputs appears as incoherence: a region of the plane the AI has never encountered produces behavior that doesn't fit the pattern of any adjacent region.

**Addictive Loop:** The player searches for the AI's out-of-distribution edges — the inputs that produce unexpected, brittle responses. Each session presses further from the AI's training distribution. The compulsive loop is: probe → observe failure signature → update model of the training distribution → probe the next edge. The AI's brittleness is a map of where it has and hasn't been; the player is mapping territory the AI has never processed.

**Novel Angle:** "Learning is just optimization" — gradient descent searching a high-dimensional surface for a low point — as the game's visible structure. The player can see the loss landscape the AI is searching, the cost function that shapes it, and the optimization path. The player is not building the network but designing the loss surface: the reward landscape that determines what the network learns to do. Designing the cost function is the design act.

## AI Integration Vector

**Player-AI Relationship:** The player is upstream of the AI's feature hierarchy — they operate at the raw input level, but the AI's behavior is determined at the concept level. The relationship is mediated by the hierarchy: the player cannot directly control high-level features, only the low-level inputs the hierarchy processes into them. The player's craft is designing inputs that produce intended high-level features.

**AI as Evolving System:** The network's knowledge is stored in parameters, updated through gradient descent. Development is optimization: each session's experience is a cost-function evaluation that nudges parameters toward lower loss. The player observes development as a change in which inputs produce which outputs — not a change in the parameters themselves (invisible) but a change in the behavior they produce.

**AI as Development Environment:** The cost function is the development environment's primary structure — it defines what the network is optimizing for. The player who designs the cost function is designing the development environment. The network searches the loss landscape the player has shaped; what it finds there is a function of both the landscape and the search path.

**Persistence:** The network's knowledge is stored in weights — persistent, compact, opaque. Between sessions, the weight state persists without change; development only occurs through additional optimization. What the network knows is always present but never directly inspectable. Persistence is the weight state; its content is visible only through behavior.
