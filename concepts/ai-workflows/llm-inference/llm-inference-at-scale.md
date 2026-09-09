---
domain: ai-workflows
subdomain: llm-inference
concept: llm-inference-at-scale
title: Deep Dive on LLM Inference at Scale
sources:
  - title: "Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher"
    url: "https://www.youtube.com/watch?v=y2W4FNAuPEA"
    author: "Harshul Jain & Tanmay Sah"
    date: "2026-09-08T15:00:06+00:00"
---

# Deep Dive on LLM Inference at Scale

This workshop introduces the fundamental challenges of LLM inference in production. The speakers motivate the topic by contrasting one-time training costs, such as the $4.6M reported for GPT-3, with ongoing inference costs that scale with every user, token, and session. They note that profitability demands extremely low per-query costs—for example, search query costs must be under $0.005 for the business to remain viable—and that teams need to either reduce token usage or optimize inference serving. The session presents a first-principles framework for understanding inference bottlenecks, then separates solutions into two broad categories: model optimization and serving/maintenance optimization. It includes hands-on notebooks, a benchmark report, and a decision diagram to help users choose among available serving mechanisms. The material is designed for beginners and intermediate users, using a small 7B model on GPU to demonstrate practical GPU metrics and behavior.

- LLM inference cost is an ongoing operational expense that grows with user traffic, in contrast to the one-time training cost of models like GPT-3.
- To make AI-powered products viable (e.g., search), per-query inference cost must be extremely low (e.g., under $0.005).
- The two main levers for reducing inference cost are reducing token usage and optimizing inference decisions/serving for clients.
- The workshop covers model-level optimization and serving-level optimization, providing a decision diagram for choosing serving mechanisms.
- All materials, including slides, notebooks, and benchmarks, are available in an open-source repository with GPU-enabled demo setups.