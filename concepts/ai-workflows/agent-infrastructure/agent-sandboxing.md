---
domain: ai-workflows
subdomain: agent-infrastructure
concept: agent-sandboxing
title: Why AI Agents Should Have Their Own Sandbox
sources:
  - title: "Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind"
    url: "https://www.youtube.com/watch?v=oWTEiYpxl80"
    author: "AI Engineer"
    date: "2026-10-07"
---

# Why AI Agents Should Have Their Own Sandbox

Philipp Schmid of Google DeepMind traces the evolution of LLM interaction from simple text continuation through instruction-following and chat dialogue to today's goal-driven agents that run autonomously for hours or days. In this agentic paradigm, users set a goal, explain how to test achievements, and how to deploy, then hope the model delivers expected results over extended runs.

Schmid introduces the Interactions API as Google's answer to OpenAI's Responses API, emphasizing that it is developer-oriented and treats models and agents through the same interface. The API supports server-side state management, long-running asynchronous operations (useful for slow tasks like video generation), and simplified tool creation combining built-in tools like Google Search with custom functions.

The central argument is that every model or agent should have its own sandbox. The Interactions API is named for the shift from merely getting a response to actively interacting with models and agents, where continuing a dialogue means passing an ID from the previous step and letting the server combine all prior inputs so the model sees everything that has been done before.

- LLM interaction evolved from text continuation to instruction-following to chat to goal-driven agents that run for hours or days
- The Interactions API unifies model and agent invocation under one interface across all modalities
- Server-side state management and long-running async operations simplify agent development
- Every model or agent should have its own sandbox environment