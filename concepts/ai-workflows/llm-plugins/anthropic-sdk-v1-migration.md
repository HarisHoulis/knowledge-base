---
domain: ai-workflows
subdomain: llm-plugins
concept: anthropic-sdk-v1-migration
title: llm-anthropic 0.27 release
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    date: "2026-08-24T16:27:04+00:00"
---

# llm-anthropic 0.27 release

The llm-anthropic 0.27 release updates the Anthropic plugin for LLM to be compatible with the recently released anthropic v1.0.0 Python library, which migrated from httpx to httpx2. This mirrors a similar change made by OpenAI in their v3.0.0 SDK release two weeks earlier. The upgrade was performed by prompting Fable 5 in Claude Code to read the official Anthropic migration guide and get the tests passing, resulting in a pull request that resolved compatibility issues.

- llm-anthropic 0.27 adds compatibility with anthropic v1.0.0.
- The anthropic v1.0.0 SDK switches from httpx to httpx2.
- OpenAI made a similar httpx-to-httpx2 switch in its v3.0.0 release.
- The upgrade was automated with Fable 5 in Claude Code using Anthropic's migration guide.