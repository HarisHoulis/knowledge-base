---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-gemini-0.33-release
title: llm-gemini 0.33
sources:
  - title: "llm-gemini 0.33"
    url: "https://simonwillison.net/2026/Aug/13/llm-gemini/"
    date: "2026-08-13T19:37:34+00:00"
---

# llm-gemini 0.33

llm-gemini 0.33 adds support for several new Gemini models, including Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash Lite, and two embedding models (gemini-embedding-2 and gemini-embedding-001). The plugin is also upgraded for compatibility with LLM 0.32, enabling reasoning traces and server-side tools via the -T flag, as demonstrated with the CodeExecution tool.

The author tested Gemini 3.7 Flash by generating SVG images of pelicans riding bicycles at high, medium, and low thinking efforts, noting that the minimal effort option from 3.6 Flash was removed. The high-effort result was described as "pretty great." A subsequent update clarified that an initially reported SVG rendering issue was not a Gemini bug but a bug in the author's rendering tool, which has since been fixed.

- llm-gemini 0.33 supports Gemini 3.7 Flash, 3.6 Flash, 3.5 Flash Lite, and two embedding models.
- Compatibility with LLM 0.32 adds reasoning traces and server-side tool support.
- The CodeExecution tool can be enabled with the pattern: llm -m gemini-3.7-flash -T CodeExecution "...".
- Gemini 3.7 Flash removed the minimal thinking effort option; high/medium/low remain.
- An initial report of invalid SVG output was retracted; the issue was a bug in the author's rendering tool, now fixed.