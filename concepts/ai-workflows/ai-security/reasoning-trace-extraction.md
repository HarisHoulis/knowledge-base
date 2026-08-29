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

The article explains that frontier AI models generate hidden reasoning traces (chain of thought) that are withheld from users for commercial and safety reasons. Providers like OpenAI, Anthropic, and Google return an encrypted version of the trace to the client to maintain statelessness while preserving confidentiality and integrity (ByteByteGo, 2026). The envelope contains authenticated fields like model name and version but lacks account and conversation context, making blocks replayable across sessions, users, and models.

Researchers at MATS Research, ELLIS Institute Tübingen, and Max Planck Institute demonstrated that these encrypted blocks can be replayed into cheaper models in the same family, which act as fuzzy decoders and reveal the hidden reasoning in plaintext (ByteByteGo, 2026). This works because smaller models receive less anti-distillation training, and cross-model compatibility allows them to accept blocks from stronger models.

The attack vectors include distillation, jailbreaking, leakage of secrets from published session logs, and prompt injection. A scan of 6,708 public agent trajectories found 62 API keys, 33 passwords, 24 access tokens, 7 private keys, and 30 personal email addresses in decoded reasoning blocks (ByteByteGo, 2026).

The proposed fix is to embed account and conversation context into the encrypted envelope to prevent cross-user and cross-model replay. The article also notes that summaries and traces can diverge, and recovered traces are often telegraphic and not legible, complicating oversight (ByteByteGo, 2026).

- Encrypted reasoning blocks are stateless and authenticated but lack origin context, enabling replay.
- Cross-model compatibility allows weaker models to decode stronger models' private traces.
- Public session logs leak secrets through unsanitizable encrypted blocks.
- Proposed fix: authenticate the context (account, conversation) within the envelope.
- Trace summaries can diverge from actual reasoning, and recovered traces are often illegible.