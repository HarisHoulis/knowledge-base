---
domain: ai-workflows
subdomain: llm-reasoning
concept: hy4-reasoning-effort
title: Introducing Hy4 Preview
sources:
  - title: "Introducing Hy4 Preview"
    url: "https://simonwillison.net/2026/Aug/29/hy4/"
    author: "Simon Willison"
    date: "2026-08-29T23:53:13+00:00"
---

# Introducing Hy4 Preview

The article introduces Hy4 Preview, a new large language model from Tencent, described as a significant size increase over its predecessor Hy3. While Hy3 had 295B parameters, the exact size of Hy4 is not stated, but the increase is highlighted as substantial (source: https://simonwillison.net/2026/Aug/29/hy4/). The article focuses on the model's chat template on Hugging Face, which defines the reasoning effort settings.

- Hy4 Preview is a major size upgrade from Tencent's previous Hy3 model.
- The chat template supports only two reasoning effort levels: 'high' (default) and 'no_think' (reasoning disabled).
- If no reasoning_effort is specified, it defaults to 'high'.
- The model's reasoning trace uses truncated English, indicating token efficiency is prioritized over grammatical completeness.