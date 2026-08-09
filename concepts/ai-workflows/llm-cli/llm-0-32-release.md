---
domain: ai-workflows
subdomain: llm-cli
concept: llm-0-32-release
title: New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging
sources:
  - title: "New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging"
    url: "https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-04T23:58:24+00:00"
---

# New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging

Simon Willison announced LLM 0.32, a major update to the LLM command-line tool. It introduces visible reasoning traces to stderr (configurable via -R), support for the GPT-5.6 model family with GPT-5.6 Luna as the new default, and server-side tools such as OpenAI's CodeInterpreter and WebSearch. The llm-anthropic plugin also gained WebSearch, WebFetch, CodeExecution, and AnthropicMCP tools, allowing prompts that execute MCP calls against services like Datasette (Simon Willison, 2026).

- Reasoning traces are now displayed to standard error and can be hidden with -R/--hide-reasoning.
- Server-side tools like CodeInterpreter and WebSearch are supported for OpenAI and Anthropic.
- The Python API now supports full message lists and streaming events (reasoning, text, tool calls).
- Logs use a content-addressable message store modeled after Git to avoid duplicate JSON.
- LLM is becoming agent-shaped, with tool chains that can pause for human approval and resume from stored history.