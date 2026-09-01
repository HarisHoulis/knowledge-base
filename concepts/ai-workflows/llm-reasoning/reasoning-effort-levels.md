---
domain: ai-workflows
subdomain: llm-reasoning
concept: reasoning-effort-levels
title: Introducing Hy4 Preview
sources:
  - title: "Introducing Hy4 Preview"
    url: "https://simonwillison.net/2026/Aug/29/hy4/"
    date: "2026-08-29T23:53:13+00:00"
---

# Introducing Hy4 Preview

Hy4 Preview is a new large language model from Tencent, representing a significant size increase over its predecessor Hy3. The model's chat template reveals two reasoning effort levels: "high" (default) and "no_think" (reasoning disabled), differing from more granular effort controls seen in other models. An example prompt to generate an SVG shows the model's reasoning trace uses slightly truncated English, likely for token efficiency in hidden reasoning.

- Hy4 Preview increases in size from Hy3's 295B parameters to a larger unspecified count, with 21B active parameters and 256,000 context.
- The chat template supports only two reasoning effort settings: 'high' and 'no_think'.
- The reasoning trace for a sample prompt uses truncated English, suggesting hidden reasoning text prioritizes efficiency over perfect grammar.