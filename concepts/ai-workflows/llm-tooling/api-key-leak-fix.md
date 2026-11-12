---
domain: ai-workflows
subdomain: llm-tooling
concept: api-key-leak-fix
title: LLM 0.37.2 Fixes API Key Leak to Third-Party OpenAI-Compatible Endpoints
sources:
  - title: "llm 0.37.2"
    url: "https://simonwillison.net/2026/Nov/11/llm/"
    author: "Simon Willison"
    date: "2026-11-11"
---

# LLM 0.37.2 Fixes API Key Leak to Third-Party OpenAI-Compatible Endpoints

LLM 0.37.2 is a security release of Simon Willison's LLM CLI tool, fixing an issue reported by Daniel de Araujo (GHSA-v9h7-jj4g-f862 and GHSA-r639-rr7r-x72w). The tool supports third-party OpenAI-compatible API endpoints via an extra-openai-models.yaml mechanism, now managed by the `llm openai endpoint add` command introduced in 0.37.

The bug could accidentally send a user's configured OpenAI API key to one of those third-party providers in two scenarios: when the key named by `api_key_name` had never been stored, or when a `responses: true` model was run with the `-o chat_completions 1` option. The patch closes both paths.

- LLM 0.37.2 patches a security issue where the OpenAI API key could leak to third-party OpenAI-compatible endpoints
- Two trigger conditions: an unstored `api_key_name` key, or running a `responses: true` model with `-o chat_completions 1`
- The extra-openai-models.yaml mechanism is now managed by the `llm openai endpoint add` command added in 0.37