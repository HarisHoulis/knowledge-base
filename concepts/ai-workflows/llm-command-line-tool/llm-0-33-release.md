---
domain: ai-workflows
subdomain: llm-command-line-tool
concept: llm-0-33-release
title: llm 0.33: Enhanced key handling, template composition, and reasoning summaries
sources:
  - title: "llm 0.33"
    url: "https://simonwillison.net/2026/Aug/22/llm/"
    author: "Simon Willison"
    date: "2026-08-22"
---

# llm 0.33: Enhanced key handling, template composition, and reasoning summaries

The llm 0.33 release introduces several improvements for embedding models and command-line workflows. Most notably, `llm embed` and `llm embed-multi` now accept a `--key` argument, and the corresponding Python methods (`EmbeddingModel.embed()`, `EmbeddingModel.embed_multi()`, `Collection.embed()`, and `Collection.embed_multi()`) accept a `key=` parameter. This allows per-call keys to be passed to embedding plugins without modifying shared model state, while a compatibility fallback ensures existing plugins that read `self.key` continue to work (Willison, 2026).

Another significant enhancement is the ability to repeat the `-t/--template` flag to combine templates in order. This lets users package a model with default options in one template and combine it with a prompt template from another, enabling reusable configurations. For example, users can save a template like `llm -m gpt-5.6-luna -o reasoning_effort high --save lhigh` and then run `llm -t lhigh -t pelican` to apply both model settings and a specific prompt (Willison, 2026).

The release also adds support for a `reasoning_summary` option for reasoning-capable Responses API models, with values `auto`, `concise`, and `detailed`. This option works with the `llm openai endpoint --responses` command and provides finer control over reasoning output (Willison, 2026).

- `llm embed` and `llm embed-multi` now support `--key` for per-call keys, with Python method equivalents and a compatibility fallback for existing plugins.
- Repeated `-t/--template` flags combine templates in order, allowing model configuration and prompt templates to be reused together.
- New `reasoning_summary` option for reasoning-capable Responses API models supports `auto`, `concise`, and `detailed` values.
- The release includes a comprehensive fix for the prior 0.32.1 issue.