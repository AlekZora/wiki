---
type: concept
title: Blockchain Interoperability
aliases: [cross-chain communication, omnichain, LayerZero]
tags: [crypto, blockchain, infrastructure, web3]
sources: [sources/layerzero-bryan-pellegrino.md]
updated: 2026-04-13
---

## Definition

The ability for distinct blockchain networks (each with its own rules, tokens, and state) to communicate, exchange data, and transfer assets without routing through centralized intermediaries. The blockchain equivalent of TCP/IP — a standardized messaging layer beneath all applications.

## How I Think About It

The problem: blockchains were each built to do specific things well, and no single chain has become the universal standard. Moving value between chains currently requires bridges — centralized servers that are expensive, slow, and a major hack target ($14B lost in 2021). LayerZero's insight was that the issue isn't bridges per se but the absence of a generic message-passing layer. If you can pass any generic message between chains, you can build bridges, NFT transfers, and arbitrary cross-chain applications on top of it.

The TCP/IP analogy is strong: it's boring, foundational infrastructure. But boring infrastructure compounds — whoever owns the message layer owns a toll road for all of Web3.

## Related Concepts

- [Information Networks](information-networks.md)

## Open Questions

- Has LayerZero actually achieved the security guarantees it claimed, or has the protocol been exploited since?
- Will the "omnichain" vision require winner-take-all at the messaging layer, or can multiple interoperability protocols coexist?
- How does the regulatory treatment of cross-chain transfers evolve?
