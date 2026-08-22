---
domain: ai-workflows
subdomain: llm-tooling
concept: llm-openrouter-plugin
title: llm-openrouter 0.7
sources:
  - title: "llm-openrouter 0.7"
    url: "https://simonwillison.net/2026/Aug/21/llm-openrouter/"
    author: "Simon Willison"
    date: "2026-08-21"
---

# llm-openrouter 0.7

The article announces the release of llm-openrouter 0.7, a plugin for the LLM CLI that is now compatible with LLM 0.32. This compatibility enables the plugin to display reasoning traces for LLMs available through OpenRouter, enhancing transparency in model outputs. The update also shifts models to use OpenRouter's implementation of the Responses API, aligning with modern API standards. Additionally, three new server-side tools are introduced: Shell, WebFetch, and WebSearch, which can be enabled via command-line options like `-T WebSearch`. These tools extend the plugin's functional reach, allowing users to perform shell operations, fetch web content, and search the web directly within their LLM workflows. Overall, llm-openrouter 0.7 significantly boosts the integration between LLM and OpenRouter, offering advanced capabilities and improved compatibility.

- Now compatible with LLM 0.32, allowing display of reasoning traces.
- Models use OpenRouter's Responses API implementation.
- Adds three server-side tools: Shell, WebFetch, and WebSearch.
- Tools are enabled via options such as `-T WebSearch`.