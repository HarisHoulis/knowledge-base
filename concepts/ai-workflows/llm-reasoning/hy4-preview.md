---
domain: ai-workflows
subdomain: llm-reasoning
concept: hy4-preview
title: Introducing Hy4 Preview
sources:
  - title: "Introducing Hy4 Preview"
    url: "https://simonwillison.net/2026/Aug/29/hy4/"
    date: "2026-08-29"
---

# Introducing Hy4 Preview

Hy4 Preview is a new large language model from Tencent, representing a significant size increase over their previous Hy3 model. The exact parameters are not specified in the article, but Hy3 had 295B total parameters with 21B active and 256k context, and Hy4 is described as a big step up from that. The model is accessible via OpenRouter, and its chat template reveals a simple reasoning-effort control with only two levels: 'high' (the default) and 'no_think' (reasoning disabled). This binary design indicates a deliberate choice to offer either full chain-of-thought or none, without intermediate settings.

The author tested Hy4's default high reasoning mode with a creative prompt asking for an SVG of a pelican riding a bicycle, and observed the model's hidden reasoning trace. The trace used slightly truncated English, likely because perfect grammar is neither useful nor token-efficient for internal reasoning text. This observation highlights an emerging pattern in LLM design where hidden reasoning traces are optimized for efficiency over readability, offering insight into how models trade off linguistic correctness for computational frugality in their internal monologues.

- Hy4 Preview is a new Tencent model, significantly larger than its predecessor Hy3.
- The chat template supports only two reasoning effort levels: high and no_think.
- Hidden reasoning traces use truncated English, presumably to save tokens.
- The model was tested with a creative SVG generation prompt via OpenRouter.