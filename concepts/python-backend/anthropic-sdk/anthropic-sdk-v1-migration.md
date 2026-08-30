---
domain: python-backend
subdomain: anthropic-sdk
concept: anthropic-sdk-v1-migration
title: llm-anthropic 0.27: Anthropic SDK v1 Compatibility
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    date: "2026-08-24T16:27:04+00:00"
---

# llm-anthropic 0.27: Anthropic SDK v1 Compatibility

llm-anthropic 0.27 is a new release of the Anthropic plugin for LLM, primarily focused on compatibility with the recently released anthropic v1.0.0 Python library. This version of the SDK switches from httpx to httpx2, a change also made by OpenAI in its v3.0.0 release two weeks earlier (source: simonwillison.net/2026/Aug/24/llm-anthropic).

- llm-anthropic 0.27 ensures compatibility with anthropic v1.0.0.
- anthropic v1.0.0 replaces httpx with httpx2.
- OpenAI's v3.0.0 made the same httpx2 switch.
- The upgrade was automated using Claude Code and Fable 5.
- Migration steps are documented in Anthropic's MIGRATION.md.