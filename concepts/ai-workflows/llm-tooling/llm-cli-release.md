---
domain: ai-workflows
subdomain: llm-tooling
concept: llm-cli-release
title: llm 0.37 Release Notes
sources:
  - title: "llm 0.37"
    url: "https://simonwillison.net/2026/Nov/2/llm/"
    author: "Simon Willison"
    date: "2026-11-02"
---

# llm 0.37 Release Notes

Simon Willison released version 0.37 of his LLM CLI tool and Python library, accumulating roughly two months of features and fixes. The release adds the `gpt-6.1-sol` and `gpt-6.1-terra` models and a new `llm openai endpoint add` command for configuring additional models that use OpenAI-compatible endpoints. The default model, for users who haven't set their own, switches to `gpt-6-luna`, which is half the price of the previous default `gpt-5.6-luna`.

Embeddings support now accepts different content-types for different binary content, which is needed for models like Gemini Embedding 2 that can embed text, audio, images, and video.

Willison addresses the common maintainer complaint about floods of AI-assisted PRs, saying LLM is his most-affected project but he doesn't find it a problem—largely because he uses Opus 5.5 or GPT-6 Astra to help triage for the most useful fixes. The release includes fixes from 12 authors, almost all AI-assisted, and he frames them as bug reports with attached examples: sometimes he lands them, sometimes he writes his own fix.

- Adds `gpt-6.1-sol` and `gpt-6.1-terra` models plus an `llm openai endpoint add` command for OpenAI-compatible endpoints
- Default model changes to `gpt-6-luna`, half the price of the prior default `gpt-5.6-luna`
- Embeddings now support per-content content-types, enabling models like Gemini Embedding 2 for text, audio, images, and video
- AI-assisted PRs are manageable when triaged with AI help and treated as bug reports with attached examples