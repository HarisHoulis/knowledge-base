---
domain: ai-workflows
subdomain: LLM privacy and security
concept: encrypted-reasoning-replay
title: How to Steal an AI Model’s Private Thoughts
sources:
  - title: "How to Steal an AI Model’s Private Thoughts"
    url: "https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private"
    author: "ByteByteGo"
    date: "2026-08-25"
---

# How to Steal an AI Model’s Private Thoughts

Frontier AI models generate hidden reasoning traces before producing visible answers. These traces contain intermediate hypotheses, tool outputs, and potentially sensitive data. Providers withhold them for commercial and safety reasons, but still need the state for multi-turn conversations. To avoid server-side storage, they return an encrypted envelope to the client, which the client resends with each request (ByteByteGo, 2026).

The envelope uses AEAD encryption to ensure confidentiality and integrity, but the authenticated fields only cover the model name, version, and key identifier—not the account or session. This leads to three forms of compatibility: cross-session, cross-user, and cross-model. Researchers demonstrated that a valid block from one model can be replayed into a cheaper model in the same family, which will decode the private reasoning in plaintext (ByteByteGo, 2026).

This extraction method enables several attack vectors: distillation (training imitation models on stolen traces), jailbreaking (revealing harmful reasoning), secret leakage from public agent logs, and prompt injection. In a scan of 6,708 public trajectories, the researchers decoded 315,320 reasoning blocks and found 62 API keys, 33 passwords, and other sensitive data. They also noted that summaries often diverge from the actual traces, complicating oversight (ByteByteGo, 2026).

The proposed mitigation focuses on binding the encrypted envelope to the original context—e.g., embedding an account ID—to prevent cross-user replay. However, a fully comprehensive fix remains elusive, as cross-model compatibility also needs to be addressed (ByteByteGo, 2026).

- Encrypted reasoning blocks are returned to clients for statelessness, but they lack context binding, allowing cross-session, cross-user, and cross-model replay.
- Smaller, less safety-trained models can decode the reasoning of larger models, enabling practical attacks like distillation and jailbreaking.
- Public agent logs leak secrets because encrypted reasoning blocks cannot be sanitized by developers.
- Recovered traces may differ significantly from the visible summaries, undermining trace-based monitoring.
- Proposed fixes include adding account/session context to the authenticated envelope, but cross-model replay remains a challenge.