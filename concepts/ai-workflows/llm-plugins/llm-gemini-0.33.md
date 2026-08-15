---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-gemini-0.33
title: llm-gemini 0.33
sources:
  - title: "llm-gemini 0.33"
    url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
    author: "Simon Willison"
    date: "2026-08-13"
---

# llm-gemini 0.33

The llm-gemini 0.33 release adds support for several new Google Gemini models, including Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash Lite, and two embedding models: gemini-embedding-2 and gemini-embedding-001 (Simon Willison, 2026). This update also brings compatibility with LLM 0.32, enabling users to view reasoning traces and activate server-side tools using the -T CodeExecution flag, as demonstrated with a Python calculation example.

- Adds support for Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, and two embedding models.
- Upgraded for LLM 0.32 compatibility, including reasoning traces and server-side tools via -T CodeExecution.
- Author tested Gemini 3.7 Flash image generation with pelicans riding bicycles at varying thinking efforts; minimal thinking was removed in 3.7.
- An initial claim about invalid SVG output was retracted; the glitch was caused by a bug in the author's rendering tool, not Gemini.
- Release confirmed as llm-gemini 0.33 on August 13, 2026.