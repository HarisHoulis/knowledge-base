---
domain: ai-workflows
subdomain: llm-memory-systems
concept: memory-system-evolution
title: Lessons from Studying Every Memory System
sources:
  - title: "Lessons from Studying Every Memory System — Shlok Khemani, Independent"
    url: "https://www.youtube.com/watch?v=5ZGyKWjQDr0"
    author: "AI Engineer"
    date: "2026-08-12T18:30:06+00:00"
---

# Lessons from Studying Every Memory System

Shlok Khemani, an AI engineer, spent a year reverse-engineering how products like ChatGPT, Claude, Gemini, and others implement memory systems for personalization in consumer AI applications. He traces the evolution of memory from early thread-only context in ChatGPT to the introduction of explicit memory management in 2024, where users had to manually ask the model to remember facts. This approach, while a first attempt, placed the burden of memory management on users and suffered from staleness, as facts like 'going to Bengaluru' persisted even after they became outdated. In April 2025, ChatGPT released a more sophisticated version, introducing a 'running profile'—a dense, dynamically updated set of user knowledge memories that are asynchronously generated from conversations. This profile, which can be thousands of tokens long, is injected into every new conversation, freeing users from manual memory editing while leveraging LLMs' ability to infer context from keyword-like clues. Khemani highlights trade-offs between transparency, staleness, and automation, and shares lessons for designing memory systems in AI products.

- Early ChatGPT memory was thread-bound with no cross-conversation recall, forcing users to manually carry context.
- ChatGPT's memory v1 (Feb 2024) allowed explicit memory creation but burdened users with management and suffered from staleness.
- ChatGPT's memory v2 (April 2025) introduced an automatically updated 'running profile' that densifies user info and is added to the context window.
- Modern memory systems shift from user-managed facts to background, asynchronous profiling that relies on LLMs to infer context from sparse clues.