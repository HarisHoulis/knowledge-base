---
domain: python-backend
subdomain: llm-plugins
concept: anthropic-sdk-compatibility
title: llm-anthropic 0.27
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    author: "Simon Willison"
    date: "2026-08-24"
---

# llm-anthropic 0.27

Simon Willison announced the release of llm-anthropic 0.27, a plugin for the LLM CLI tool, primarily to add compatibility with the recently released anthropic v1.0.0 Python library. This new version of the Anthropic SDK switches from httpx to httpx2, mirroring a similar transition made by OpenAI in their v3.0.0 release two weeks prior. The article highlights that this change is significant enough to require careful migration.

To perform the upgrade, Willison used Claude Code with Fable 5, prompting it to read the official Anthropic migration guide and ensure the test suite passed. The resulting pull request demonstrates an AI-assisted approach to dependency migration, where the AI model interprets migration documentation and drives code changes to completion. This serves as an example of using large language models to automate routine yet complex library upgrades.

- llm-anthropic 0.27 adds support for anthropic v1.0.0, which uses httpx2 instead of httpx.
- OpenAI's Python SDK made a similar httpx to httpx2 transition in its v3.0.0 release.
- The migration was automated using Fable 5 in Claude Code, guided by Anthropic's official migration guide.
- The automated process produced a pull request with passing tests, showcasing AI-assisted code migration.