---
domain: python-backend
subdomain: sdk-migration
concept: anthropic-sdk-v1-compatibility
title: llm-anthropic 0.27: Compatibility with Anthropic SDK v1.0
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    date: "2026-08-24T16:27:04+00:00"
  - title: "llm-anthropic 0.27 release"
    url: "https://github.com/simonw/llm-anthropic/releases/tag/0.27"
  - title: "Anthropic SDK migration guide"
    url: "https://github.com/anthropics/anthropic-sdk-python/blob/v1.0.0/MIGRATION.md"
  - title: "Upgrade PR"
    url: "https://github.com/simonw/llm-anthropic/pull/84"
---

# llm-anthropic 0.27: Compatibility with Anthropic SDK v1.0

The llm-anthropic 0.27 release updates the Anthropic plugin for LLM to maintain compatibility with the recently released anthropic v1.0.0 Python library, which switches from httpx to httpx2. This change mirrors OpenAI's v3.0.0 release, which made the same HTTP client transition two weeks earlier. The release ensures users of llm-anthropic can continue using the latest Anthropic SDK without breaking changes.

To handle the upgrade, the author used Claude Code with Fable 5 to prompt the migration: "Upgrade to anthropic>=1 - read MIGRATION.md and get the tests passing". This AI-assisted process resulted in a pull request that implemented the changes. The migration guide provided by Anthropic was a key reference for the transition.

The release thus demonstrates a practical workflow for upgrading Python packages when upstream dependencies make major changes, leveraging AI coding tools to automate the migration while keeping the test suite green.

- llm-anthropic 0.27 adds compatibility with anthropic v1.0.0.
- anthropic v1.0.0 switches HTTP client from httpx to httpx2.
- OpenAI's Python SDK v3.0.0 made a similar transition two weeks earlier.
- The upgrade was performed with AI assistance (Fable 5 in Claude Code) using the official migration guide.