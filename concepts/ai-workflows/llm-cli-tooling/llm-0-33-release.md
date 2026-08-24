---
domain: ai-workflows
subdomain: llm-cli-tooling
concept: llm-0-33-release
title: llm 0.33: Embedding Keys, Template Composition, and Reasoning Summaries
sources:
  - title: "llm 0.33"
    url: "https://simonwillison.net/2026/Aug/22/llm/"
    author: "Simon Willison"
    date: "2026-08-22T17:01:16+00:00"
---

# llm 0.33: Embedding Keys, Template Composition, and Reasoning Summaries

The llm 0.33 release introduces per-call key support for embedding models, aligning them with regular LLM models. The `llm embed` and `llm embed-multi` commands now accept `--key`, and the Python methods `EmbeddingModel.embed()`, `EmbeddingModel.embed_multi()`, `Collection.embed()`, and `Collection.embed_multi()` accept a `key=` argument. This passes the resolved per-call key to embedding plugins without altering shared model state, while existing plugins that read `self.key` continue to work through a compatibility fallback (source: simonwillison.net).

A significant workflow improvement is that `llm prompt -t/--template` can now be repeated to combine templates in order. This allows a model configuration template (e.g., one that sets a model and default options) to be chained with a prompt template, enabling patterns like saving a model package and a prompt separately then invoking them together with `llm -t lhigh -t pelican` (source: simonwillison.net).

Finally, the release adds a `reasoning_summary` option for reasoning-capable Responses API models, supporting `auto`, `concise`, and `detailed` values. This is usable with `llm openai endpoint --responses`, making it easier to exercise different models that implement their own version of the OpenAI Responses API (source: simonwillison.net).

- Embedding commands and Python methods now support per-call keys with backward compatibility for existing plugins.
- Repeating `-t/--template` combines templates in order, enabling reusable model configuration and prompt templates.
- A new `reasoning_summary` option (auto, concise, detailed) is available for reasoning-capable Responses API models.
- This release also includes a comprehensive fix for the earlier 0.32.1 quick fix.