---
domain: ai-workflows
subdomain: local-llm-integration
concept: openai-compatible-endpoints
title: datasette-llm 0.1a11 Adds OpenAI-Compatible Endpoint Support
sources:
  - title: "datasette-llm 0.1a11"
    url: "https://simonwillison.net/2026/Nov/14/datasette-llm/"
    author: "Simon Willison"
    date: "2026-11-14"
---

# datasette-llm 0.1a11 Adds OpenAI-Compatible Endpoint Support

datasette-llm is an intermediate Datasette plugin that lets other Datasette plugins configure and use LLMs. Release 0.1a11 adds support for OpenAI-compatible endpoints, so Datasette can be pointed at any LLM host that speaks the OpenAI-style web protocol.

This makes it possible to run Datasette against local models served by LM Studio, Ollama, or llama.cpp (which recently reached v1.0.0). The post shows a `uvx` command that downloads a sample database and launches Datasette with a `default_model` setting pointing at a local LM Studio endpoint (`http://localhost:1234/v1`), yielding a Datasette Agent instance powered by a local model.

- datasette-llm is the intermediate plugin for configuring LLMs across Datasette plugins
- Version 0.1a11 adds OpenAI-compatible endpoint support
- Works with local model servers like LM Studio, Ollama, and llama.cpp
- Can be launched via uvx with a default_model setting pointing at a local API base