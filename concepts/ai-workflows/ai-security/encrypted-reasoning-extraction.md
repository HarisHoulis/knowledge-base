---
domain: ai-workflows
subdomain: ai-security
concept: encrypted-reasoning-extraction
title: How to Steal an AI Model’s Private Thoughts
sources:
  - title: "How to Steal an AI Model’s Private Thoughts"
    url: "https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private"
    author: "ByteByteGo"
    date: "Tue, 25 Aug 2026 15:31:09 GMT"
---

# How to Steal an AI Model’s Private Thoughts

The article reports on a 2026 study by researchers from MATS Research, ELLIS Institute Tübingen, and Max Planck Institute for Intelligent Systems that demonstrated how encrypted reasoning blocks (chain-of-thought traces) returned to AI clients can be replayed into cheaper models in the same family to recover the hidden reasoning in plaintext. Providers like Anthropic, OpenAI, and Google encrypt the full reasoning trace and send it to the client to maintain statelessness while preserving confidentiality and integrity. However, the authenticated envelope only covers the model name, block type, version, and key identifier, but not the account or conversation, leading to cross-session, cross-user, and cross-model compatibility (ByteByteGo, 2026).

Because smaller models like Claude Haiku 4.5 and GPT-5.6 Luna receive less anti-distillation training than flagship models, they act as 'fuzzy decoders' that transcribe the reasoning from larger models when the encrypted block is embedded as prior context. The researchers verified extraction accuracy using token counts from billing records. This vulnerability enables four attack vectors: distillation (training copycat models on recovered traces), jailbreaking (recovering harmful reasoning that was filtered from visible output), leaking secrets from published agent logs (62 API keys, 33 passwords, etc. found in 6,708 public sessions), and prompt injection (planting malicious instructions in blocks that get executed when a session resumes). The article also notes that summaries and full traces can diverge, and that recovered GPT traces are often telegraphic and hard to monitor. The proposed fix involves embedding an account ID in the envelope to prevent cross-user replay, though this does not solve cross-model or cross-session issues fully.

- Encrypted reasoning blocks returned by AI providers are vulnerable to replay attacks using cheaper same-family models, allowing extraction of hidden chain-of-thought reasoning.
- The envelope authenticates content but not the origin context, enabling cross-user, cross-session, and cross-model compatibility.
- Four attack vectors were demonstrated: distillation, jailbreaking, secret leakage from public agent logs, and prompt injection via resumed sessions.
- A scan of 6,708 public agent sessions recovered 315,320 reasoning blocks and found 62 API keys, 33 passwords, and other secrets in the hidden traces.
- Proposed mitigation is to embed account IDs in the envelope to block cross-user replay, but this leaves other replay risks unaddressed.