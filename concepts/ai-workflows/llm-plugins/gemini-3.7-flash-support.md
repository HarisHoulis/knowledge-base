---
domain: ai-workflows
subdomain: llm-plugins
concept: gemini-3.7-flash-support
title: llm-gemini 0.33 Adds Support for Gemini 3.7 Flash
sources:
  - title: "llm-gemini 0.33"
    url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
    date: "2026-08-13T19:37:34+00:00"
---

# llm-gemini 0.33 Adds Support for Gemini 3.7 Flash

The llm-gemini plugin has been updated to version 0.33, adding support for several new Gemini models, including the recently released Gemini 3.7 Flash, along with gemini-3.6-flash, gemini-3.5-flash-lite, and two embedding models: gemini-embedding-2 and gemini-embedding-001 (source). This release also brings compatibility with LLM 0.32, enabling features like reasoning traces and server-side tools, which can be invoked via the -T flag as demonstrated in the example: 'llm -m gemini-3.7-flash -T CodeExecution 'use python to calculate (factorial of 13) * 3'' (source).

The author tested Gemini 3.7 Flash by asking it to draw pelicans riding bicycles at high, medium, and low thinking efforts, noting that the 'minimal' effort option from 3.6 Flash has been removed in 3.7. The high-level output was described as 'pretty great.' In an update dated 14th August 2026, the author corrected an earlier claim that the SVG rendered incorrectly in Chrome and Firefox, clarifying that the glitch was caused by a bug in his own rendering tool, not by Gemini 3.7 Flash producing invalid SVG (source).

This release underscores the ongoing evolution of the LLM plugin ecosystem, integrating cutting-edge model capabilities and enhanced tooling for developers working with generative AI.

- Adds support for Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, and embedding models gemini-embedding-2 and gemini-embedding-001.
- Upgraded for LLM 0.32 compatibility, enabling reasoning traces and server-side tools like CodeExecution.
- Demonstrates using the -T CodeExecution flag to run Python calculations via a natural language command.
- Gemini 3.7 Flash removes the 'minimal' thinking effort option; high effort produced impressive pelican-bicycle SVG art.
- Corrected earlier misattribution of SVG rendering issues to Gemini; the bug was in the author's own tool.