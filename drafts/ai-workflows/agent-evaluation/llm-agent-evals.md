---
domain: ai-workflows
subdomain: agent-evaluation
concept: llm-agent-evals
title: How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude
sources:
  - title: "How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI"
    url: "https://www.youtube.com/watch?v=SHMCGrNJJGc"
    author: "AI Engineer"
    date: "2026-10-17"
---

# How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude

Laurie Voss (Arize AI) frames the core problem of agent development: you build an LLM-powered app or agent, it seems to work in a few tries, then a user hits an unexpected path and it breaks — or you fix one thing and suspect you broke another, with no way to tell. Evals are the answer to determining whether an agent is good and whether a change improved or worsened it, without reading every output by hand.

Voss defines evals as tests run against traces. Traces record everything the AI did at a fine-grained level — every agent step, tool call, and LLM call, with incoming and source data at each step. A trace is composed of spans, where each span is one step of execution (like a line in a log), and the whole agent run is a span containing nested spans.

The key distinction from unit tests is that evals target non-deterministic outputs — results that are never exactly the same twice — which is inherent to LLM outputs. The workshop's promise is that by the end you will have an agent tracked end-to-end with code-based evaluations, LLM-judge assessments, and custom evaluations you write yourself, plus an experiment proving your judge can be trusted and that your changes actually worked. All of this runs as a set of tests via npm test so it can be wired into CI.

The hands-on setup uses Phoenix launched locally (viewable at localhost:6060) via uvx, so Python runs under the hood from a JavaScript/TypeScript project requiring Node 22+. Examples use Claude via an Anthropic API key, though any LLM provider could be substituted.

- Evals are tests run against traces; unlike unit tests they handle non-deterministic LLM outputs that never repeat exactly.
- Traces capture every agent step, tool call, and LLM call with input/source data, composed of nested spans.
- The goal is to detect regressions from changes without manually reading each output.
- Combine code-based evals, LLM-judge assessments, and custom evals, and run an experiment to verify the judge itself is trustworthy.
- Package evals as npm tests so they can run in CI.