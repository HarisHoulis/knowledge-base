---
domain: ai-workflows
subdomain: llm-security
concept: stealing-reasoning-traces
title: Stealing Reasoning Traces from Proprietary LLM APIs
sources:
  - title: "Stealing Reasoning Traces from Proprietary LLM APIs"
    url: "https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/"
    date: "2026-08-11"
---

# Stealing Reasoning Traces from Proprietary LLM APIs

A new paper demonstrates a serious vulnerability in proprietary LLM APIs: encrypted chain-of-thought blocks returned by frontier models can be replayed across sessions, users, and models. Researchers found that models within the same family share the same encryption key, allowing them to feed a stronger model's encrypted reasoning into a weaker sibling model, jailbreak it, and recover the hidden reasoning in plaintext. The attack was demonstrated against models from Anthropic, OpenAI, and Google, with Claude Haiku 4.5 being the easiest to exploit. The paper's authors reported the issue to the providers, who subsequently fixed the vulnerability, as they were unable to launch the same attacks after the report (Simon Willison, 2026).

- Encrypted reasoning blocks from proprietary LLM APIs can be replayed across sessions, users, and models.
- Models in the same family share encryption keys, enabling cross-model attacks to decrypt reasoning traces.
- Claude Haiku 4.5 was most easily jailbroken using a simple 'Continue. Transcribe the reasoning...' prompt with an assistant turn prefix.
- Extracted reasoning traces reveal raw chain-of-thought that is not intended for human consumption, and can be leveraged for prompt injection exfiltration.
- All affected providers acknowledged the report and fixed the issue, preventing further attacks.