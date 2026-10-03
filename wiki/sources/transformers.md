---
title: But what is a GPT? Visual intro to transformers
type: video
status: processed
source_path: raw/videos/transformers.md
created: 2026-05-09
tags:
  - transformers
  - large-language-models
  - attention-mechanism
  - word-embeddings
  - neural-networks
  - machine-learning
  - GPT
concepts:
  - ../concepts/transformer-architecture.md
  - ../concepts/word-embeddings.md
  - ../concepts/neural-networks.md
---

# Summary

This video provides a visually-driven, intuitive explanation of the Transformer architecture, the core technology behind models like GPT. Its purpose is to demystify how these models work by breaking down their internal data flow into understandable, sequential steps. The video begins by deconstructing the "GPT" acronym (Generative Pre-trained Transformer), emphasizing that the Transformer is the key innovation.

The core of the explanation follows the journey of data through the model. It starts with input text being broken into "tokens." These tokens are then converted into high-dimensional numerical vectors via an "embedding matrix." The video spends significant time explaining the concept of word embeddings, demonstrating how the geometric structure of this high-dimensional "embedding space" captures semantic relationships between words (e.g., the vector from "man" to "woman" is similar to the vector from "king" to "queen").

Next, the video presents a high-level overview of the main processing pipeline. This sequence of vectors flows through a series of repeating blocks, each containing two main components: an "attention block," which allows the vectors to exchange information and build context, and a "multi-layer perceptron" (MLP) block, which processes each vector in parallel. The video frames the entire process as an operation designed to allow each initial word vector to "soak in" context from its surrounding words, becoming a richer, more nuanced representation of its meaning within the specific passage.

Finally, the process of generating an output is explained. The model takes the final, context-rich vector from the end of the sequence and uses an "unembedding matrix" to transform it into a list of raw scores (logits), one for each possible token in the vocabulary. These logits are then passed through a "softmax" function to be converted into a valid probability distribution. The video explains how this next-token prediction mechanism is used iteratively to generate long passages of text and how a "temperature" parameter in the softmax function can control the output's creativity. Throughout, the video uses GPT-3's specific parameter counts as a concrete, running example.

# Key Claims

*   The "Transformer" is the core neural network architecture and key invention underlying the current boom in AI, including models like GPT.
*   The fundamental task of a GPT-style model is next-token prediction: given a sequence of text, it calculates a probability distribution for what token comes next.
*   Coherent, long-form text generation is achieved through an iterative, autoregressive loop: predict the next token, sample from the distribution, append it to the context, and repeat.
*   The entire computational process within a Transformer is primarily composed of matrix multiplications applied to vectors.
*   Input tokens are first converted into high-dimensional vectors (embeddings), where geometric directions and distances in this vector space encode semantic meaning.
*   The primary goal of the Transformer's layered structure is to progressively enrich each token's vector with information from its context.
*   A Transformer consists of a stack of repeating blocks, each containing an "attention" sub-layer (for inter-vector communication) and an "MLP" sub-layer (for parallel processing of each vector).
*   The final output is produced by an "unembedding" matrix that maps the final vector back to the vocabulary space, followed by a softmax function to create a probability distribution.
*   The "temperature" parameter in the softmax function is a key control for generation, balancing between predictable, high-probability outputs (low temperature) and more creative, random outputs (high temperature).

# Mechanisms

*   **Tokenization & Embedding:** Input text is broken into tokens (words or sub-words). Each token is mapped to a specific column in a large, learnable "embedding matrix" to produce a high-dimensional vector. This vector is the initial, context-free representation of the token's meaning.
*   **Autoregressive Generation Loop:** A model generates extended text by first processing a prompt. It computes a probability distribution for the next token, samples one, appends it to the prompt, and feeds this new, longer sequence back into itself to generate the subsequent token. This loop repeats until a desired length or stop condition is met.
*   **Layered Contextualization:** The sequence of vectors passes through multiple identical blocks. Each block has two main sub-layers:
    1.  **Attention Block:** Allows each vector in the sequence to exchange information with all other vectors, updating itself to incorporate relevant context. (The mechanism's purpose is described, but its detailed function is deferred to a later video).
    2.  **Multi-Layer Perceptron (MLP) / Feed-Forward Layer:** Processes each vector independently and in parallel, applying the same learned transformation to all of them.
*   **Prediction Head (Unembedding & Softmax):** After passing through all layers, the final vector in the sequence is multiplied by an "unembedding matrix". This produces a vector of raw scores ("logits"), with one score for each token in the model's vocabulary. The logits are then passed through the softmax function, which converts them into a clean probability distribution (all values are positive and sum to 1), from which the next token is sampled.

# Useful Examples

*   **GPT Acronym:** GPT stands for Generative Pre-trained Transformer.
*   **GPT-2 vs. GPT-3 Scale:** An animation shows GPT-2 generating an incoherent story from a prompt, while the much larger GPT-3 generates a sensible one, illustrating how emergent capabilities arise with scale.
*   **Semantic Vector Arithmetic:** The classic analogy `vector(King) - vector(Man) + vector(Woman) ≈ vector(Queen)` is used to show that directions in the embedding space correspond to concepts like gender.
*   **Other Vector Analogies:** More examples are given to reinforce the concept of semantic directions, such as `Italy - Germany + Hitler ≈ Mussolini` and `Germany - Japan + Sushi ≈ Bratwurst`.
*   **Plurality Direction:** The vector difference `cats - cat` is used to represent a "plurality" direction. Its dot product is higher with plural nouns (e.g., "dogs") than singular ones ("dog") and increases with the numerical embeddings for 1, 2, 3, etc.
*   **Temperature Parameter:** The prompt "Once upon a time there was a..." is fed to GPT-3 at different temperatures. Temperature 0 produces a predictable story about Goldilocks. A higher temperature generates a more creative but ultimately nonsensical story.
*   **GPT-3 Architecture:** The video uses GPT-3's specific numbers as a running example: 175 billion parameters, a vocabulary of 50,257 tokens, an embedding dimension of 12,288, and a context size of 2048 tokens.

# Possible Relevance

*   **AI agent design:** The autoregressive prediction loop is the core of how language-based agents think, plan, and communicate. Understanding the context window limit explains why agents can "lose the thread" in long interactions. The "temperature" parameter provides a direct mechanism for tuning an agent's creativity versus its reliability, a critical trade-off in agent system design. The concept of vectors "soaking in context" is a powerful mental model for an agent's state representation.
*   **Narrative Systems:** The video explicitly demonstrates how a next-token predictor functions as a storyteller. The temperature setting is a direct mechanical lever for controlling narrative voice and style—low temperature for coherent but possibly clichéd plots, high temperature for novelty and potential incoherence. This could be exposed as a user-facing mechanic in a procedural narrative game.
*   **Game Mechanics:** The idea of a semantic vector space could be the basis for a crafting or magic system. A player could combine concepts via vector arithmetic: `vector(fire) + vector(arrow) = vector(fire_arrow)`. A discovery mechanic could be built around finding the "nearest neighbor" to a novel vector combination in the game's conceptual space.
*   **Knowledge Management:** Word embeddings offer a way to implement semantic search in a personal wiki, finding notes based on conceptual similarity rather than just keyword matches. The system of vector arithmetic allows for analogical queries (e.g., finding the "Python equivalent" of a specific "Lisp function"). The model of vectors updating with context is analogous to how a note's relevance changes depending on the project or query it's being viewed through.

# Links

*   **Models/Concepts:** GPT (Generative Pre-trained Transformer), GPT-2, GPT-3, DALL-E, Midjourney, Transformer, Neural Network, Deep Learning, Backpropagation, Tokenization, Word Embeddings, Attention Block, Multi-Layer Perceptron (MLP), Softmax, Logits, Dot Product.
*   **Organizations:** Google (originated the Transformer in 2017).
*   **Misc:** *Karate Kid* (used as an analogy for foundational learning).