---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-openrouter-0-7
title: llm-openrouter 0.7
sources:
  - title: "llm-openrouter 0.7"
    url: "https://simonwillison.net/2026/Aug/21/llm-openrouter/"
    date: "2026-08-21T16:58:19+00:00"
---

# llm-openrouter 0.7

The llm-openrouter 0.7 release brings compatibility with LLM 0.32, enabling the display of reasoning traces for models accessed through OpenRouter. This update ensures that users can now see detailed reasoning outputs directly in the LLM CLI tool, enhancing transparency and debuggability of model responses.

- Updated for compatibility with LLM 0.32, allowing reasoning trace display.
- Models now use OpenRouter's implementation of the Responses API.
- Added three server-side tools: Shell, WebFetch, and WebSearch, enabled via options like -T WebSearch.