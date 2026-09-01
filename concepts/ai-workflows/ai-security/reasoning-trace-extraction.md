---
domain: ai-workflows
subdomain: ai-security
concept: reasoning-trace-extraction
title: How to Steal an AI Model’s Private Thoughts
sources:
  - title: "How to Steal an AI Model’s Private Thoughts"
    url: "https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private"
    author: "ByteByteGo"
    date: "Tue, 25 Aug 2026 15:31:09 GMT"
---

# How to Steal an AI Model’s Private Thoughts

The article explains how AI model providers hide the full reasoning traces behind an encrypted envelope, returning it to the client to maintain statelessness while protecting confidentiality and integrity. Researchers at MATS Research, ELLIS Institute Tübingen, and Max Planck Institute for Intelligent Systems demonstrated that these encrypted reasoning blocks can be replayed into cheaper, less-protected models in the same family, which then output the hidden reasoning in plaintext. This cross-model compatibility exists because smaller models receive less anti-distillation training, making them act as fuzzy decoders.

- Encrypted reasoning blocks (e.g., signature, encrypted_content, thinkingSignature) are returned to clients for stateless multi-turn conversations, but they lack account and conversation authentication, enabling replay across users, sessions, and models.
- Cross-model compatibility allows a strong model's encrypted reasoning to be decoded by a weaker model in the same family, effectively stealing the hidden chain-of-thought without triggering refusal or output filters.
- A public scan of 6,708 agent sessions recovered 315,320 reasoning blocks, leaking 62 API keys, 33 passwords, 24 access tokens, 7 private keys, and 30 personal emails, despite visible-text sanitization.
- The proposed fix is to embed account or session context into the authenticated envelope to prevent cross-user and cross-session replay, though cross-model compatibility may still need model-specific keys.