---
domain: ai-workflows
subdomain: llm-security
concept: reasoning-trace-extraction
title: How to Steal an AI Model’s Private Thoughts
sources:
  - title: "How to Steal an AI Model’s Private Thoughts"
    url: "https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private"
    author: "ByteByteGo"
    date: "Tue, 25 Aug 2026 15:31:09 GMT"
---

# How to Steal an AI Model’s Private Thoughts

The article explains that frontier AI models produce a hidden reasoning trace before generating a visible answer. Providers withhold these traces for commercial reasons (to prevent distillation) and safety reasons (to avoid leaking harmful or sensitive content). To avoid server-side storage costs, providers such as OpenAI, Anthropic, and Google return an AEAD-encrypted block to the client; this block contains the reasoning trace and is meant to be sent back with each subsequent request in a stateless conversation. The envelope authenticates the content and model metadata, but does not bind the block to a specific user, session, or conversation context (ByteByteGo, 2026).

Researchers at MATS Research, the ELLIS Institute Tübingen, and the Max Planck Institute showed that these encrypted blocks can be replayed into weaker models in the same family—such as Claude Haiku or GPT-5.6 Luna—which will transcribe the hidden reasoning in plaintext. This works because cross-model compatibility is broadly enabled, and smaller models receive less anti-distillation training. The researchers verified extractions by comparing billed reasoning-token counts with re-encoded recovered text, achieving close to one-to-one correspondence for Claude. Using this method, they also scanned 6,708 public agent trajectories and decoded 315,320 reasoning blocks, uncovering API keys, passwords, tokens, private keys, and personal email addresses in real user sessions (ByteByteGo, 2026).

The article identifies four attack vectors: distillation, jailbreaking, secret leakage from published session logs, and prompt injection via resumed sessions. The root cause is that the envelope authenticates its content but not the context in which it was produced or replayed. The proposed mitigation is to bind the envelope to contextual information—starting with embedding an account id—to prevent cross-user replay, though other challenges such as trace legibility and monitoring remain (ByteByteGo, 2026).

- Frontier model reasoning traces are hidden but returned to clients in encrypted AEAD envelopes to keep servers stateless.
- The encrypted blocks authenticate only the content, not the originating user, session, or conversation, enabling cross-user and cross-model replay.
- Weaker models in the same family can act as fuzzy decoders to reveal stronger models' hidden reasoning in plaintext.
- Publicly shared agent session logs contain sensitive data inside encrypted reasoning blocks, and sanitization of visible text does not remove these leaks.
- Proposed fixes include adding contextual metadata like account ids to the envelope to prevent cross-user replay attacks.