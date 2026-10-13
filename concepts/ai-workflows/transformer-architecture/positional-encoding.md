---
domain: ai-workflows
subdomain: transformer-architecture
concept: positional-encoding
title: How 19th-Century Heat Physics Math Powers LLM Positional Encoding
sources:
  - title: "How the Math Used in 19th-Century Heat Physics Helps LLMs Understand Sentences"
    url: "https://blog.bytebytego.com/p/how-the-math-used-in-19th-century"
    author: "ByteByteGo"
    date: "2026-10-13"
---

# How 19th-Century Heat Physics Math Powers LLM Positional Encoding

Fourier's 1822 work on heat propagation introduced the use of sine and cosine functions to represent complex patterns as combinations of simpler waves. Nearly two centuries later, the same functions appear in the transformer architecture behind modern language models, where they encode token positions in a sequence. The article draws this connection: sine and cosine turn positions into structured numerical patterns that a transformer can use to learn how word order affects meaning.

Word order carries information that token identity alone cannot provide—"Alice trusts Bob" and "Bob trusts Alice" contain identical words but different meanings. Basic attention, however, does not automatically use order: reordering inputs reorders outputs but does not independently recognize new grammatical relationships. Positional encoding solves this by converting a sequence location into a numerical representation that is combined with the token embedding, giving the model a signal influenced by both identity and location.

The article explains why sine and cosine are used rather than plain integers: a single scalar requires the model to construct positional features from one number, while a collection of sine and cosine values supplies multiple bounded, structured features that change at different rates. Multiple rotation speeds (frequencies) provide a richer position code that distinguishes positions separated by a full cycle of any single hand. The original transformer adds the position encoding to the token embedding component-wise, and the sinusoidal structure gives a consistent relative-position relationship: advancing by a fixed offset always rotates each frequency pair by a fixed angle, independent of starting position.

The article also covers RoPE (rotary position embeddings) as a modern approach, noting that the mathematical family of sine and cosine functions underlies both Fourier's heat analysis and LLM positional encoding.

- Sine and cosine functions, used by Fourier in 1822 to model heat, now encode token positions in transformer-based LLMs.
- Basic attention does not inherently use word order; positional encoding makes sequence location available to the model.
- Multiple rotation speeds (frequencies) create a richer position code that distinguishes positions a single wave would conflate.
- The original transformer adds position encoding to token embeddings component-wise, yielding a representation influenced by both identity and location.
- Sinusoidal encodings give a consistent relative-position structure: a fixed offset always rotates each frequency pair by a fixed angle.