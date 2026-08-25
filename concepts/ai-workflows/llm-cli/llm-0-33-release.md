---
domain: ai-workflows
subdomain: llm-cli
concept: llm-0-33-release
title: llm 0.33
sources:
  - title: "llm 0.33"
    url: "https://simonwillison.net/2026/Aug/22/llm/"
    author: "Simon Willison"
    date: "2026-08-22"
---

# llm 0.33

Simon Willison announced the release of llm 0.33, a comprehensive update following a quick 0.32.1 fix. The release introduces the ability to pass per-call API keys to embedding commands and Python methods, aligning embedding models with the key handling used by regular LLM models. This change, contributed by ChrisJr404, ensures compatibility with existing plugins through a fallback mechanism (Simon Willison, 2026).

- `llm embed` and `llm embed-multi` now accept `--key`, and the corresponding Python methods (e.g., `EmbeddingModel.embed()`) support a `key=` parameter.
- Templates can now be combined by repeating `-t/--template`, enabling model configuration from one template to be used with a prompt from another.
- Reasoning-capable Responses API models support a `reasoning_summary` option with `auto`, `concise`, and `detailed` values.