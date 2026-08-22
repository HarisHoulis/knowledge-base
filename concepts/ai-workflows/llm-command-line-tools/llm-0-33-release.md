---
domain: ai-workflows
subdomain: llm-command-line-tools
concept: llm-0-33-release
title: llm 0.33
sources:
  - title: "llm 0.33"
    url: "https://simonwillison.net/2026/Aug/22/llm/"
    author: "Simon Willison"
    date: "2026-08-22"
---

# llm 0.33

The [llm 0.33 release](https://simonwillison.net/2026/Aug/22/llm/) introduces several improvements to the LLM command-line tool, following a quick 0.32.1 fix. A major update is that `llm embed` and `llm embed-multi` now accept `--key`, and the Python `EmbeddingModel.embed()`, `EmbeddingModel.embed_multi()`, `Collection.embed()`, and `Collection.embed_multi()` methods accept a `key=` argument. This passes the resolved per-call key to embedding plugins without changing shared model state, and existing plugins that read `self.key` continue to work through a compatibility fallback.

Another key enhancement is that `llm prompt -t/--template` can now be repeated to combine templates in order. This allows model configuration and options from one template to be used with a prompt from another, enabling patterns like creating a template that packages a model with default options and combining it with a separate prompt template. The release also adds a `reasoning_summary` option for reasoning-capable Responses API models, with `auto`, `concise`, and `detailed` values, which can be used with `llm openai endpoint --responses`.

- `llm embed` and `llm embed-multi` support `--key`, and Python embedding methods accept `key=` to pass per-call keys without mutating shared model state, with backward compatibility for existing plugins.
- `llm prompt -t/--template` can be repeated to combine templates sequentially, enabling separation of model configuration and prompt content.
- New `reasoning_summary` option for Responses API models with values `auto`, `concise`, and `detailed`.
- The release is a more comprehensive fix following the 0.32.1 hotfix.