---
domain: ai-workflows
subdomain: llm-memory
concept: memory-system-evolution
title: Lessons from Studying Every Memory System
sources:
  - title: "Lessons from Studying Every Memory System"
    url: "https://www.youtube.com/watch?v=5ZGyKWjQDr0"
    author: "Shlok Khemani"
    date: "2026-08-12T18:30:06+00:00"
---

# Lessons from Studying Every Memory System

The talk reviews how memory systems in consumer AI applications have evolved over three years, focusing on ChatGPT and Claude. In 2023, ChatGPT had no cross-thread memory, forcing users to manually carry context between conversations. In February 2024, ChatGPT memory v1 introduced explicit, user-created facts stored in a list and injected into every context window. While a decent first effort, this approach placed the burden of memory management on the user and suffered from staleness—memories that were once true remained in context even after becoming outdated (Shlok Khemani, 2026).

A year later, in April 2025, ChatGPT memory v2 introduced 'user knowledge memories' (a running profile). This profile is updated asynchronously every few days, automatically extracting important information from recent conversations and creating dense, keyword-like memory entries. The running profile is then added to every new conversation. This shift reduces user burden and leverages the model's ability to infer context from limited clues, but the problem of stale memories persists. The talk highlights the trade-off between user control and automation, as well as the design evolution from static lists to dynamic, dense profiles (Shlok Khemani, 2026).

- Early LLM products had no persistent memory; users manually copied context between threads, which was unsustainable for mainstream adoption.
- ChatGPT memory v1 stored explicit user facts as a list in context, but it shifted memory management to the user and became stale over time.
- ChatGPT memory v2 introduced a running profile that is automatically updated every few days, packing dense clues into the context window without requiring user oversight.
- The evolution reflects a move from user-managed, static memories to system-managed, dynamic profiles, though staleness remains an open challenge.