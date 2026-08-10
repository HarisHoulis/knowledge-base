---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-anthropic-0-26
title: llm-anthropic 0.26 release notes
sources:
  - title: "llm-anthropic 0.26"
    url: "https://simonwillison.net/2026/Aug/4/llm-anthropic/#atom-everything"
    author: "Simon Willison"
    date: "2026-08-04"
---

# llm-anthropic 0.26 release notes

Extended thinking has been simplified to the 'thinking' and 'thinking_effort' options (low, medium, high, xhigh, or max). Claude 5 models think by default; thinking can be disabled with '-o thinking 0' for Sonnet 5 and Opus 5, while Fable 5 always thinks. The -R/--hide-reasoning flag now omits reasoning from responses and logs, and several older thinking-related options were removed.

- Added Claude 5 models: claude-fable-5, claude-sonnet-5, and claude-opus-5.
- New server-side tools: WebSearch, WebFetch, CodeExecution, and AnthropicMCP, available via -T or Python tools=.
- Requires LLM >=0.32; reasoning and tool events stream as typed events.
- Thinking simplified to 'thinking' and 'thinking_effort'; Claude 5 models think by default, with Fable 5 always thinking.
- Old -o web_search* options removed in favor of -T WebSearch.