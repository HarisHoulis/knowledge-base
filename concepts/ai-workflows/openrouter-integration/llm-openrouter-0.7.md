---
domain: ai-workflows
subdomain: openrouter-integration
concept: llm-openrouter-0.7
title: llm-openrouter 0.7 Release
sources:
  - title: "llm-openrouter 0.7"
    url: "https://simonwillison.net/2026/Aug/21/llm-openrouter/"
    date: "2026-08-21T16:58:19+00:00"
---

# llm-openrouter 0.7 Release

The llm-openrouter plugin has been updated to version 0.7, now compatible with LLM 0.32. This compatibility enables the display of reasoning traces for LLMs available through OpenRouter (https://simonwillison.net/2026/Aug/21/llm-openrouter/). The plugin now leverages OpenRouter's implementation of the Responses API for model interactions.

Additionally, version 0.7 introduces three new server-side tools: Shell, WebFetch, and WebSearch. These can be enabled via command-line options such as `-T WebSearch` (https://github.com/simonw/llm-openrouter).

- Compatible with LLM 0.32, enabling reasoning trace display.
- Switched to OpenRouter's Responses API.
- New server-side tools: Shell, WebFetch, and WebSearch.
- Tools can be enabled with options like -T WebSearch.