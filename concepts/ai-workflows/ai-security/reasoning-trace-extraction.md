---
domain: ai-workflows
subdomain: ai-security
concept: reasoning-trace-extraction
title: How to Steal an AI Model's Private Thoughts
sources:
  - title: "How to Steal an AI Model's Private Thoughts"
    url: "https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private"
    author: "ByteByteGo"
    date: "2026-08-25"
---

# How to Steal an AI Model's Private Thoughts

The article discusses a security vulnerability discovered by researchers at MATS Research, the ELLIS Institute Tübingen, and the Max Planck Institute for Intelligent Systems. Modern frontier AI models generate a hidden reasoning trace before producing a visible answer. To keep their services stateless, providers like Anthropic, OpenAI, and Google encrypt this trace and return it to the client, which stores and resends it with each request. The researchers found that these encrypted blocks can be replayed across sessions, users, and even models, because they authenticate only the content, not the context in which they were produced.

- Encrypted reasoning blocks are not bound to their origin; they can be replayed across sessions, users, and models.
- Weaker models in the same family can act as fuzzy decoders to extract the strong model's hidden reasoning in plaintext.
- The attack enables distillation, jailbreaking, prompt injection via shared logs, and mass leakage of secrets from public agent trajectories.
- The root cause is that the AEAD envelope authenticates content but not the producing account or conversation.
- Proposed mitigation includes embedding account and conversation identifiers in the authenticated envelope to prevent cross-user replay.