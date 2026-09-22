---
domain: ai-workflows
subdomain: llm-plugins
concept: llm-typesafe
title: llm-typesafe 0.1a0
sources:
  - title: "llm-typesafe 0.1a0"
    url: "https://simonwillison.net/2026/Sep/22/llm-typesafe/"
    author: "Simon Willison"
    date: "2026-09-22"
---

# llm-typesafe 0.1a0

Simon Willison released llm-typesafe 0.1a0, a new plugin for LLM that adds support for TypeSafe AI's Jev model. Install it with `llm install llm-typesafe`, then set an API key using `llm keys set typesafe` after obtaining one from the TypeSafe console.

The plugin enables yes/no "noul" questions. For example, `llm -m jev 'Please refund my last payment.' -s 'Does this message explicitly request a refund?'` returns `{"type": "noul", "noul": 0.99}`. It also supports choice questions using `-o answer_type choice` and a criteria mapping, such as routing messages to billing, technical, or other teams.

Scoring questions are supported via `-o answer_type score` with a criteria list. An example scores the reproducibility of a problem report from "No reproduction instructions" to "Complete steps with expected and actual results." The README provides more details.

- New LLM plugin `llm-typesafe` adds support for TypeSafe AI's Jev model.
- Install with `llm install llm-typesafe` and set an API key via `llm keys set typesafe`.
- Supports yes/no "noul" questions returning a probability, e.g. `{"type": "noul", "noul": 0.99}`.
- Supports choice questions (`-o answer_type choice`) and scoring questions (`-o answer_type score`) with criteria.
- Further details are in the plugin's README.