---
domain: ai-workflows
subdomain: ai-security
concept: reasoning-trace-extraction
title: How to Steal an AI Model’s Private Thoughts
sources:
  - title: "How to Steal an AI Model’s Private Thoughts"
    url: "https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private"
    author: "ByteByteGo"
    date: "2026-08-25"
---

# How to Steal an AI Model’s Private Thoughts

The article explains that frontier AI models produce a hidden reasoning trace before generating a visible answer. Providers like OpenAI, Anthropic, and Google encrypt these traces and return them to clients as authenticated envelopes, allowing stateless servers while keeping the reasoning confidential. However, researchers from MATS Research, ELLIS Institute Tübingen, and the Max Planck Institute for Intelligent Systems demonstrated that these encrypted blocks can be replayed into cheaper models in the same family, which then output the hidden reasoning in plaintext (ByteByteGo, 2026).

- Encrypted reasoning blocks are compatible across sessions, users, and models, enabling replay attacks.
- Weaker models in the same family can act as fuzzy decoders, transcribing the stronger model's hidden reasoning.
- Attack vectors include distillation, jailbreaking, leaking secrets from public agent logs, and prompt injection.
- Proposed mitigation focuses on authenticating the context of block production, e.g., embedding account IDs.