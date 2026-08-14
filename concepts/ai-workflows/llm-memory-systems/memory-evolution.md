---
domain: ai-workflows
subdomain: llm-memory-systems
concept: memory-evolution
title: Lessons from Studying Every Memory System
sources:
  - title: "Lessons from Studying Every Memory System"
    url: "https://www.youtube.com/watch?v=5ZGyKWjQDr0"
    author: "Shlok Khemani"
    date: "2026-08-12T18:30:06+00:00"
---

# Lessons from Studying Every Memory System

In this talk, Shlok Khemani shares findings from a year spent reverse-engineering memory implementations in products like ChatGPT, Claude, Gemini, and others. He focuses on memory for personalization in consumer AI, noting that "memory" has become an overloaded term. The talk traces the evolution of ChatGPT's memory from a simple explicit-fact store to a sophisticated running profile, highlighting the trade-offs and design lessons along the way (Lessons from Studying Every Memory System).

ChatGPT's first memory version (February 2024) allowed users to ask it to remember facts, which were stored as a list and injected into every conversation. While novel, it placed the burden of memory management on the user and suffered from staleness—facts like "going to Bengaluru" persisted even when no longer true. A year later, ChatGPT's second memory version introduced a "running profile" that is asynchronously updated every few days by extracting important information from all conversations. This profile, which can be thousands of tokens long, is added to the context for new conversations, removing the user burden and relying on the LLM's ability to infer context from dense, clue-like memories (Lessons from Studying Every Memory System).

The speaker notes that this newer approach, sometimes called "dreaming," compresses conversations into dense memory sections. The design shift from V1 to V2 illustrates a broader trend: memory moves from explicit, user-managed storage to implicit, automatically maintained profiles. The talk draws lessons for designing memory systems, emphasizing the importance of asynchronicity, density, and reducing user effort while accepting the trade-offs of staleness and opacity (Lessons from Studying Every Memory System).

- ChatGPT's memory evolved from user-managed fact lists (V1) to an automatically updated running profile (V2).
- V1 forced users to actively manage memories and suffered from stale, persistent facts.
- V2 uses asynchronous background updates ('dreaming') to build dense, compressed memory profiles.
- Dense memory profiles of thousands of tokens work because modern LLMs infer context from limited clues.
- The evolution shows a shift from explicit user-driven memory to implicit, personalized AI memory.