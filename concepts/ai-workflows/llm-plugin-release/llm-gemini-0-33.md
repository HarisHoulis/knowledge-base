---
domain: ai-workflows
subdomain: llm-plugin-release
concept: llm-gemini-0-33
title: llm-gemini 0.33
sources:
  - title: "llm-gemini 0.33"
    url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
    date: "2026-08-13T19:37:34+00:00"
---

# llm-gemini 0.33

The llm-gemini 0.33 release adds support for newly announced Gemini 3.7 Flash, along with Gemini 3.6 Flash, Gemini 3.5 Flash Lite, and two embedding models: gemini-embedding-2 and gemini-embedding-001. This marks an update after a long gap, bringing the plugin in line with recent Gemini model releases.

- Adds support for Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, and two embedding models.
- Upgraded for LLM 0.32 compatibility, enabling reasoning traces and server-side tool execution.
- Server-side tools can be enabled using the -T flag, e.g., `llm -m gemini-3.7-flash -T CodeExecution '...'`.
- Gemini 3.7 Flash offers high, medium, and low thinking efforts; minimal effort has been removed.
- A previous claim about invalid SVG was corrected to a bug in the author's rendering tool.