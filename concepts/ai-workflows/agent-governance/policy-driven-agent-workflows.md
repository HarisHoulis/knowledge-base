---
domain: ai-workflows
subdomain: agent-governance
concept: policy-driven-agent-workflows
title: Knowing When an AI Agent Can Work Unsupervised in Policy-Driven Workflows
sources:
  - title: "How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase"
    url: "https://www.youtube.com/watch?v=_4Ph2dhmUFI"
    author: "AI Engineer"
    date: "2026-10-19"
---

# Knowing When an AI Agent Can Work Unsupervised in Policy-Driven Workflows

Evan Kormos (Coinbase) frames organizational policy as the "original institutional intent" or "original system prompt" — the written rules, expressed with must/may/should language, that govern how work gets done, especially around risk and compliance. He argues for separating policy (the build state, changed deliberately) from the running system (the run state, which is constantly evolving through product-driven changes), while expecting the running system to remain roughly bound by policy.

- Treat written policy as the organization's original system prompt, using must/may/should to encode rules and decisions.
- Separate the build state (policy definition/change) from the run state (the constantly evolving running system).
- Model workflows as DAGs (e.g., with Airflow) for gated, forward-moving processes, and as cyclic graphs (e.g., LangGraph) for iterative inner loops like code review.
- Agents cut across people, process, and technology; the focus is where agents meet process — what work they get, what boundaries are set, and how trust in outputs is built.
- Design exception flows to monitor failures (e.g., canceled or non-compliant code) without trying to cover every edge case.