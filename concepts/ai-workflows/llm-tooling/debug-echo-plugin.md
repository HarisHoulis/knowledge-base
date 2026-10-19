---
domain: ai-workflows
subdomain: llm-tooling
concept: debug-echo-plugin
title: llm-echo 0.5: Debug Plugin for LLM
sources:
  - title: "llm-echo 0.5"
    url: "https://simonwillison.net/2026/Oct/18/llm-echo/"
    author: "Simon Willison"
    date: "2026-10-18"
---

# llm-echo 0.5: Debug Plugin for LLM

Simon Willison released version 0.5 of llm-echo, a debug plugin for his LLM CLI tool that provides a "model" which involves no actual LLM—it simply repeats back the prompts fed to it. The release was prompted by work toward a new LLM release and testing PRs.

The main change in 0.5 is that simulated token usage counts now account for tool calls, system prompts, and reasoning tokens. The post demonstrates usage via `uvx --with llm-echo llm -m echo 'hi there' -o thinking 1 --usage`, which echoes the prompt as JSON and reports token usage of 2 input and 24 output tokens.

- llm-echo is a debug plugin providing a fake model that echoes prompts without invoking an LLM
- Version 0.5 updates simulated token usage to account for tool calls, system prompts, and reasoning tokens
- Can be run ad hoc with uvx and the --usage flag to inspect prompt structure and token counts