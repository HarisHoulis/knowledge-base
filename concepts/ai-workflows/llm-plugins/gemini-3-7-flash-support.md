---
domain: ai-workflows
subdomain: llm-plugins
concept: gemini-3-7-flash-support
title: llm-gemini 0.33 adds Gemini 3.7 Flash support
sources:
  - title: "llm-gemini 0.33"
    url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
    date: "2026-08-13T19:37:34+00:00"
---

# llm-gemini 0.33 adds Gemini 3.7 Flash support

The llm-gemini plugin has been updated to version 0.33, adding support for Gemini 3.7 Flash, along with gemini-3.6-flash, gemini-3.5-flash-lite, and two embedding models: gemini-embedding-2 and gemini-embedding-001. This release also brings compatibility with LLM 0.32, enabling reasoning traces and server-side tools via the -T CodeExecution pattern.

- Adds support for Gemini 3.7 Flash, gemini-3.6-flash, gemini-3.5-flash-lite, gemini-embedding-2, and gemini-embedding-001.
- Upgraded for LLM 0.32 compatibility, supporting reasoning traces and server-side tools.
- Demonstrates using server-side code execution with the -T CodeExecution flag to run Python calculations.
- A rendering issue with SVG output was initially attributed to Gemini 3.7 Flash but was later found to be a bug in the author's rendering tool.