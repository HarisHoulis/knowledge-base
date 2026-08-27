---
domain: ai-workflows
subdomain: llm-release
concept: llm-0.33
title: LLM 0.33 Release
sources:
  - title: "llm 0.33"
    url: "https://simonwillison.net/2026/Aug/22/llm/"
    author: "Simon Willison"
    date: "2026-08-22"
---

# LLM 0.33 Release

LLM 0.33 is a significant release that introduces several enhancements to the command-line tool for working with large language models. The release follows a quick 0.32.1 fix and provides a more comprehensive solution. Key improvements focus on embedding workflows, template composition, and reasoning capabilities.

- The `llm embed` and `llm embed-multi` commands now accept `--key`, and the Python methods `EmbeddingModel.embed()`, `EmbeddingModel.embed_multi()`, `Collection.embed()`, and `Collection.embed_multi()` accept `key=` too, allowing per-call keys without mutating shared model state. Existing plugins reading `self.key` remain compatible via a fallback.
- The `-t/--template` option can now be repeated to combine templates in order, enabling patterns like packaging a model with default options in one template and a prompt in another, then running them together.
- Reasoning-capable Responses API models now support a `reasoning_summary` option with values `auto`, `concise`, and `detailed`, useful for models providing their own imitation of the OpenAI Responses API.
- The release includes a 0.32.1 fix from the previous day, making 0.33 the comprehensive fix for any issues addressed there.