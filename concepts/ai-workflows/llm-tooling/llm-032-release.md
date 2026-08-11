---
domain: ai-workflows
subdomain: llm-tooling
concept: llm-032-release
title: New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging
sources:
  - title: "New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging"
    url: "https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-04"
---

# New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging

LLM 0.32 is a major update introducing visible reasoning traces for model 'thinking', displayed to stderr with an option to hide them via `-R/--hide-reasoning`. It adds built-in support for the GPT-5.6 family, defaulting to GPT-5.6 Luna for `llm "prompt"`, and enables server-side tools like OpenAI's CodeInterpreter and WebSearch, plus Anthropic's WebSearch, WebFetch, CodeExecution, and AnthropicMCP through the llm-anthropic plugin [source](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything).

- Visible reasoning traces (stderr) with `-R/--hide-reasoning` to suppress.
- Server-side tools from OpenAI and Anthropic, including CodeInterpreter and MCP.
- New `llm openai endpoint` command for quick prompts against any OpenAI-compatible API.
- Python API now supports `model.prompt(messages=[])` and `stream_events()` for mixed content.
- Content-addressable message store improves log efficiency.