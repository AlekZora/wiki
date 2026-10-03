---
title: But what is a neural network? | Chapter 1, Deep learning
type: video
status: processed
source_path: raw/videos/deep-learning.md
created: 2026-05-09
tags:
  - neural-networks
  - deep-learning
  - machine-learning
concepts:
  - ../concepts/neural-networks.md
---

# Summary

This video provides a visual and conceptual introduction to the structure of a basic, feedforward neural network, using handwritten digit recognition as a running example. The central argument is that the seemingly complex behavior of a neural network emerges from a simple, repeated mathematical operation organized into a hierarchical structure. The purpose is to demystify the core components of a neural network, building intuition for *what* it is before explaining *how* it learns in a subsequent video.

The video begins by posing the challenge of recognizing a 28x28 pixel image of a handwritten digit, a task trivial for humans but difficult to program explicitly. It then introduces the network's layered architecture: an input layer corresponding to the pixels (784 neurons), one or more "hidden" layers, and an output layer representing the possible digit classifications (10 neurons). A neuron is defined simply as a thing that holds a number between 0 and 1, called its "activation."

The core of the explanation focuses on the "hope" for what these layers do: they build up a hierarchy of abstraction. The first hidden layer might learn to recognize simple patterns like small edges from the raw pixel data. The next layer could learn to combine these edges into more complex subcomponents, like loops and lines. Finally, the output layer learns which combination of these subcomponents corresponds to a specific digit (e.g., an upper loop + a vertical line = a 9).

The video then details the mathematical mechanism enabling this. The activation of any single neuron is calculated by taking a weighted sum of all activations from the previous layer, adding a "bias" term, and then passing the result through a non-linear "squishification" function like the sigmoid function, which clamps the output to a value between 0 and 1. The weights determine the pattern a neuron is looking for, while the bias acts as a threshold for how active the input pattern must be before the neuron "fires." The entire network, with its thousands of tunable weights and biases, is ultimately just a very complex mathematical function that maps the input pixel values to the output classification scores. This process is concisely represented using linear algebra notation (`a_out = σ(W * a_in + b)`), which is how it's implemented in software. The video concludes by noting that modern networks often use the ReLU activation function instead of the sigmoid.

# Key Claims

- A neural network is fundamentally a complex, highly-parameterized mathematical function inspired by the brain's structure.
- Neurons are simple units that hold an "activation" value, typically between 0 and 1.
- The network's layered structure is motivated by the concept of hierarchical abstraction, where simple features are combined into progressively more complex ones.
- The flow of information is feedforward: activations in one layer determine the activations in the next.
- The activation of a neuron is calculated via a weighted sum of the previous layer's activations, plus an added bias.
- A non-linear activation function (like sigmoid or ReLU) is essential for the network to learn complex patterns.
- The network's "knowledge" is stored in its thousands of numerical parameters: the weights and biases.
- "Learning" is the process of finding the optimal set of values for these weights and biases to solve a given task.
- The entire layer-to-layer transition can be represented compactly and efficiently using linear algebra (matrix-vector products).

# Mechanisms

- **Feedforward Activation Propagation:** Information flows strictly in one direction, from the input layer through the hidden layers to the output layer. The activation of each neuron is computed based on the outputs of the neurons in the immediately preceding layer.
- **Weighted Summation and Pattern Detection:** Each connection has a weight. The network computes a weighted sum of the previous layer's activations. This mechanism allows a neuron to assign different levels of importance to its inputs, effectively "looking for" a specific pattern. For example, a neuron can be tuned with positive and negative weights to detect an edge in a specific region of the input image.
- **Bias as Activation Threshold:** A bias term is added to the weighted sum. This value acts as an adjustable threshold, determining how high the weighted sum must be before the neuron becomes meaningfully active. It provides the model with more flexibility than a simple `> 0` threshold.
- **Non-Linear Transformation (Squishification):** The weighted sum plus bias is passed through a non-linear activation function (e.g., sigmoid). This is critical; without this non-linearity, a deep network would be mathematically equivalent to a single-layer network and lose its ability to model complex functions. The sigmoid function maps any real-valued input to the range (0, 1).
- **Hierarchical Feature Composition:** The conceptual mechanism behind the layers. By tuning the weights and biases, the first hidden layer learns to detect low-level features (e.g., edges). The second hidden layer learns to combine those features into mid-level concepts (e.g., loops, corners). The final layer combines these concepts to make a classification (e.g., "9").

# Useful Examples

- **Handwritten Digit Recognition (MNIST):** The primary example used throughout. The network takes a 28x28 (784) pixel grayscale image as input and outputs a classification among 10 digits (0-9).
- **Conceptual Recognition of a '9':** An illustration of the hierarchical abstraction model. Pixels are combined by the first hidden layer to detect small edges. These edges are combined by the second hidden layer to detect an "upper loop" and a "vertical line." The output layer then recognizes that this combination signifies the digit "9".
- **Visualizing a Weight Matrix as an Edge Detector:** To explain how a neuron can detect a feature, the video visualizes the weights connecting a single neuron to all 784 input pixels as a grid. By setting weights to be positive in a small vertical region and negative in the surrounding area, the neuron becomes a detector for that specific vertical edge.
- **Speech Recognition Hierarchy Analogy:** To generalize the concept of layered abstraction beyond vision, the video cites speech recognition: raw audio is processed into distinct sounds, which are combined into syllables, then words, then phrases, and finally abstract thoughts.

# Possible Relevance

- **AI agent design:** This source explains the fundamental building block of a perception system for an AI agent. An agent operating in a visual environment could use such a network to process raw pixel data from its "eyes" into abstract concepts like "obstacle," "ally," or "item," enabling more complex decision-making. The hierarchical feature detection is a model for how an agent can build a world model from low-level sensory input.
- **Narrative systems:** The concept of hierarchical abstraction (pixels -> edges -> shapes -> concepts) can be a powerful metaphor for procedural narrative generation. A system could be designed to combine basic narrative atoms (actions, dialogue fragments) into scenes (hidden layer 1), scenes into plot arcs (hidden layer 2), and plot arcs into a complete story (output layer), with the "weights" representing thematic or stylistic rules.
- **Game mechanics:** The network's structure could be externalized as a core game mechanic. A player could "train" an in-game AI companion by providing examples, with the game visualizing the weights of the AI's "brain" using the video's green (positive) and red (negative) grid system. This would make the abstract process of machine learning tangible and interactive.
- **Knowledge management:** The layered network architecture mirrors a way of structuring knowledge. Raw notes and data points are the input layer. These are synthesized into intermediate concepts or "Maps of Content" (MOCs) in the hidden layers. These MOCs are then combined to support high-level arguments or conclusions in the output layer. This provides a formal model for building knowledge from the bottom up.

# Links

- **People:** Leysa Lee
- **Concepts:** Neural Network, Deep Learning, Activation, Hidden Layers, Weights, Bias, Sigmoid Function, Logistic Curve, Linear Algebra, Matrix-Vector Multiplication, ReLU (Rectified Linear Unit)
- **Organizations:** Amplify Partners
- **External Sources:** 3Blue1Brown series on Linear Algebra