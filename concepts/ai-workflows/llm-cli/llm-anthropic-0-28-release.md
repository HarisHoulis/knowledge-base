---
domain: ai-workflows
subdomain: llm-cli
concept: llm-anthropic-0-28-release
title: llm-anthropic 0.28
sources:
  - title: "llm-anthropic 0.28"
    url: "https://simonwillison.net/2026/Sep/2/llm-anthropic/"
    date: "2026-09-02T17:59:32+00:00"
---

# llm-anthropic 0.28

Simon Willison announced the release of llm-anthropic 0.28. The update adds support for Claude Fable 5.1. For models supporting reasoning traces, those traces are now shown by default. The release also introduces a new exception, llm_anthropic.ClaudeRefusal, which is raised when Claude refuses a request. The post is tagged with llm, anthropic, claude, and claude-mythos-fable, indicating it addresses both the LLM CLI ecosystem and recent Claude model developments.

- llm-anthropic 0.28 supports Claude Fable 5.1
- Reasoning traces are now displayed by default for supported models
- New exception llm_anthropic.ClaudeRefusal handles Claude refusals