---
domain: ai-workflows
subdomain: llm-gemini
concept: gemini-3-8-flash-support
title: llm-gemini 0.34
sources:
  - title: "llm-gemini 0.34"
    url: "https://simonwillison.net/2026/Sep/2/llm-gemini/"
    date: "2026-09-02T16:39:38+00:00"
---

# llm-gemini 0.34

The llm-gemini 0.34 release adds support for Google's newly announced Gemini 3.8 Flash model, including configurable low, medium, and high thinking levels. It also fixes a bug where async responses failed to record the resolved model version, with thanks to contributor Charlie Tonneslan (source: https://simonwillison.net/2026/Sep/2/llm-gemini/).

- Gemini 3.8 Flash is now supported in llm-gemini 0.34, with low, medium, and high thinking levels.
- The release fixes async responses not recording the resolved model version.
- Simon Willison highlights Gemini Flash as fast, cheap, and competent at generating HTML and JavaScript, using it to add HTML rendering support to markdown-svg-renderer via a coding agent.