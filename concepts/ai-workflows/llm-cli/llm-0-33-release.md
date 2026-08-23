---
domain: ai-workflows
subdomain: llm-cli
concept: llm-0-33-release
title: LLM 0.33 release highlights
sources:
  - title: "llm 0.33"
    url: "https://simonwillison.net/2026/Aug/22/llm/"
    author: "Simon Willison"
    date: "2026-08-22"
---

# LLM 0.33 release highlights

The release of LLM 0.33 introduces two significant improvements to embedding workflows. The `llm embed` and `llm embed-multi` commands now accept a `--key` argument, and the corresponding Python methods (`EmbeddingModel.embed()`, `EmbeddingModel.embed_multi()`, `Collection.embed()`, and `Collection.embed_multi()`) accept a `key=` parameter. This allows per-call keys to be passed to embedding plugins without altering shared model state. Existing plugins that rely on `self.key` continue to work through a compatibility fallback, as noted in the release notes (Simon Willison, 2026).

- Embedding commands and Python methods now support per-call keys via `--key` and `key=`, with a compatibility fallback for existing plugins that use `self.key`.
- The `llm prompt -t/--template` option can be repeated to combine templates in order, allowing model configuration to be decoupled from the prompt.
- A new `reasoning_summary` option is available for reasoning-capable Responses API models, with values `auto`, `concise`, and `detailed`.
- This release includes a more comprehensive fix following a quick 0.32.1 patch, addressing the same issue more thoroughly.