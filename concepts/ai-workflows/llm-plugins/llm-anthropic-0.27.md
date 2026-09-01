---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-anthropic-0.27
title: llm-anthropic 0.27: Anthropic SDK v1 Compatibility
sources:
  - title: "llm-anthropic 0.27"
    url: "https://simonwillison.net/2026/Aug/24/llm-anthropic/"
    author: "Simon Willison"
    date: "2026-08-24"
---

# llm-anthropic 0.27: Anthropic SDK v1 Compatibility

llm-anthropic 0.27 is a release of the Anthropic plugin for LLM, primarily aimed at compatibility with the recently released anthropic v1.0.0 Python library. This new version of the SDK switches from httpx to httpx2, a change OpenAI also made in its v3.0.0 release two weeks earlier. The release notes highlight the official migration guide provided by Anthropic for upgrading to 1.0.

The upgrade itself was performed by prompting Fable 5 in Claude Code with the migration guide URL and the instruction 'get the tests passing'. This resulted in a pull request (PR #84) that contains the necessary changes. This demonstrates an AI-assisted workflow for dependency upgrades, where a language model reads migration documentation and applies the required code changes automatically.

- llm-anthropic 0.27 provides compatibility with anthropic v1.0.0.
- anthropic v1.0.0 and openai v3.0.0 both migrated from httpx to httpx2.
- The upgrade was performed using Claude Code with Fable 5, guided by the official migration guide.
- The resulting code changes are available in PR #84.