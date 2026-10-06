---
domain: ai-workflows
subdomain: llm-cli-plugins
concept: llm-anthropic-plugin
title: llm-anthropic 0.30: Dynamic Model Refresh and Token Counting
sources:
  - title: "llm-anthropic 0.30"
    url: "https://simonwillison.net/2026/Sep/28/llm-anthropic/"
    author: "Simon Willison"
    date: "2026-09-28"
---

# llm-anthropic 0.30: Dynamic Model Refresh and Token Counting

llm-anthropic 0.30 adds support for Claude Sonnet 5.5 alongside two new CLI commands. The `llm anthropic refresh` command refreshes the list of Anthropic models directly from Anthropic's API, removing the need to publish a new plugin release just to add support for a newly released model (https://simonwillison.net/2026/Sep/28/llm-anthropic/).

A second command, `llm anthropic count`, uses Anthropic's free token counting API to return the number of tokens a prompt will consume before that prompt is sent. Together these changes shift model metadata and prompt cost estimation from static, release-bound configuration to runtime API calls.

- Release adds Claude Sonnet 5.5 support.
- `llm anthropic refresh` pulls the model list live from Anthropic's API, so new models no longer require a new plugin release.
- `llm anthropic count` uses Anthropic's free token counting API to preview token usage for a prompt before sending it.