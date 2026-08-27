---
domain: ai-workflows
subdomain: llm-plugin-release
concept: llm-anthropic-027
title: llm-anthropic 0.27 Release with Anthropic SDK v1.0 Compatibility
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    author: "Simon Willison"
    date: "2026-08-24"
---

# llm-anthropic 0.27 Release with Anthropic SDK v1.0 Compatibility

This release of the llm-anthropic plugin for LLM primarily ensures compatibility with the recently released anthropic v1.0.0 Python library, which switched from httpx to httpx2. The same change was made by OpenAI in their v3.0.0 release two weeks earlier. The upgrade was performed using Claude Code with Fable 5, prompted to read the official Anthropic migration guide and get the tests passing, resulting in pull request #84. This highlights how AI assistants can streamline dependency upgrades and migration tasks by leveraging official documentation and automated test feedback.

- llm-anthropic 0.27 adds compatibility with anthropic v1.0.0, which migrated from httpx to httpx2.
- OpenAI's Python SDK v3.0.0 made the same HTTP client change, indicating a broader ecosystem transition.
- The upgrade was completed by prompting Claude Code with Fable 5 to read the migration guide and fix tests, resulting in PR #84.
- Anthropic's official migration guide served as the authoritative reference for the upgrade process.