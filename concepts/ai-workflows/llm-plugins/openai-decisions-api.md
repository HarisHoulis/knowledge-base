---
domain: ai-workflows
subdomain: llm-plugins
concept: openai-decisions-api
title: llm-openai-decisions 0.1a0
sources:
  - title: "llm-openai-decisions 0.1a0"
    url: "https://simonwillison.net/2026/Oct/6/llm-openai-decisions/"
    author: "Simon Willison"
    date: "2026-10-06"
---

# llm-openai-decisions 0.1a0

Simon Willison released llm-openai-decisions 0.1a0, a plugin for his LLM tool that wraps OpenAI's new Decisions API, which OpenAI announced at DevDay and released as a Jev-style API. He had GPT-6 Astra read the new OpenAI API documentation and build the plugin, inspired by his existing llm-typesafe plugin for talking to Jev.

Unlike Jev, the new gpt-6-luna decision model supports image input in addition to text. Both models charge for input only and not for output: OpenAI's is 10 cents per million input tokens, while Jev's is 4.2 cents per million. Otherwise the API shape is conceptually very similar to Jev, and OpenAI Decisions supports the same three question types Jev does: yes/no, choices, or scores.

The plugin is installed with `llm install llm-openai-decisions`. An example query against an image attachment uses `llm -m openai-decisions/gpt-6-luna -a <image-url> -s 'Does this image contain any mammals?'`, producing output like `{"type": "predicate", "name": "evaluation", "probability": 0.0}`. The README covers how to run the other question types.

- llm-openai-decisions 0.1a0 is a plugin wrapping OpenAI's new Jev-style Decisions API, built by GPT-6 Astra from the API docs and inspired by llm-typesafe.
- The gpt-6-luna decision model supports image input in addition to text, unlike Jev.
- Both models charge for input only: OpenAI at 10 cents per million input tokens, Jev at 4.2 cents per million.
- OpenAI Decisions supports the same three question types as Jev: yes/no, choices, or scores.