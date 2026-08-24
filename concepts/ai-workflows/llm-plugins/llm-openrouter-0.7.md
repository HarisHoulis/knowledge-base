---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-openrouter-0.7
title: llm-openrouter 0.7 Release
sources:
  - title: "llm-openrouter 0.7"
    url: "https://simonwillison.net/2026/Aug/21/llm-openrouter/"
    date: "2026-08-21T16:58:19+00:00"
---

# llm-openrouter 0.7 Release

The llm-openrouter 0.7 release is now compatible with LLM 0.32, enabling the display of reasoning traces for models accessed through OpenRouter (simonwillison.net, 2026). This compatibility update is significant because it brings parity with LLM 0.32's features, allowing users to see chain-of-thought outputs from OpenRouter-hosted models directly in the CLI.

The plugin has also migrated to using OpenRouter's implementation of the Responses API, which is a more advanced API for interacting with language models. This change likely improves consistency and feature support across different models. Additionally, three new server-side tools were introduced: Shell, WebFetch, and WebSearch. These tools can be enabled via command-line options like `-T WebSearch`, giving LLM agents the ability to execute shell commands, fetch web pages, and perform web searches, thereby expanding the interactive capabilities of the plugin (simonwillison.net, 2026).

- llm-openrouter 0.7 is compatible with LLM 0.32, enabling reasoning trace display for OpenRouter models.
- Models now use OpenRouter's Responses API implementation.
- Three new server-side tools are added: Shell, WebFetch, and WebSearch, enabled via options such as -T WebSearch.