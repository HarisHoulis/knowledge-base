---
domain: ai-workflows
subdomain: llm-cli
concept: llm-034-release
title: llm 0.34 Release Notes
sources:
  - title: "llm 0.34"
    url: "https://simonwillison.net/2026/Sep/2/llm/"
    date: "2026-09-02"
---

# llm 0.34 Release Notes

Simon Willison announced the release of llm 0.34, a command-line tool for working with large language models. The main new feature is that `llm logs --usage` Markdown output now includes response duration in milliseconds and as a human-readable duration, while `llm logs --short` includes a new `duration_ms` field. This enhancement helps users track latency and performance of their LLM API calls.

- `llm logs --usage` Markdown output now shows response duration in both milliseconds and human-readable form.
- `llm logs --short` adds a `duration_ms` field to its output.
- The release also includes several contributed bug fixes and a significant performance improvement to `llm logs` by waveplate.