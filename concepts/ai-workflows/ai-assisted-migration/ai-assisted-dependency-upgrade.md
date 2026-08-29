---
domain: ai-workflows
subdomain: ai-assisted-migration
concept: ai-assisted-dependency-upgrade
title: llm-anthropic 0.27
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    author: "Simon Willison"
    date: "2026-08-24"
  - title: "llm-anthropic releases"
    url: "https://github.com/simonw/llm-anthropic/releases/tag/0.27"
    author: "Simon Willison"
    date: "2026-08-24"
  - title: "Pull request #84"
    url: "https://github.com/simonw/llm-anthropic/pull/84"
    author: "Simon Willison"
    date: "2026-08-24"
---

# llm-anthropic 0.27

The release of llm-anthropic 0.27 focuses on compatibility with the newly released anthropic v1.0.0 Python library, which migrates from httpx to httpx2. This mirrors a similar change in OpenAI's v3.0.0 release two weeks earlier, signaling a broader ecosystem transition to httpx2 ([source](https://simonwillison.net/2026/Aug/24/llm-anthropic/)).

To perform the upgrade, Simon Willison used Fable 5 in Claude Code, prompting it to read the official migration guide and get the tests passing. The resulting PR demonstrates an effective workflow for AI-assisted dependency upgrades, where the AI agent handles code changes guided by upstream migration documentation ([PR](https://github.com/simonw/llm-anthropic/pull/84)).

This approach highlights a growing pattern: using large language models to automate tedious library migration tasks, while still relying on tests to verify correctness. The release itself is part of the ongoing maintenance of the LLM plugin ecosystem, ensuring compatibility with the latest SDK changes ([release notes](https://github.com/simonw/llm-anthropic/releases/tag/0.27)).

- llm-anthropic 0.27 adds support for anthropic v1.0.0, which swaps httpx for httpx2.
- OpenAI's SDK also moved to httpx2 in v3.0.0, showing an industry-wide shift.
- The upgrade was performed by Fable 5 in Claude Code using the official migration guide and tests.
- This demonstrates an effective AI-assisted dependency upgrade workflow.