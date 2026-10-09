---
domain: ai-workflows
subdomain: agent-context-management
concept: context-engineering
title: Why Bigger Context Windows Won't Save Your Agent
sources:
  - title: "Why Bigger Context Windows Won't Save Your Agent — Elizabeth Fuentes Leone, AWS"
    url: "https://www.youtube.com/watch?v=DrfyORO8RqA"
    author: "AI Engineer"
    date: "2026-10-08"
---

# Why Bigger Context Windows Won't Save Your Agent

Elizabeth Fuentes Leone argues that the idea of an infinite context window is a myth: agent systems break when tools return large amounts of data, causing the context window to overflow, the agent to hallucinate, and its reasoning to deteriorate. She notes that a year ago, before the agent era, the assumption was that more tokens would fix everything, but today we know this is not the case because of the model's attention curve — when too much data is present, the model forgets the middle and only remembers the beginning and end of what was sent.

Her proposed remedy is context engineering: providing the model with the right information exactly when it's needed. Sometimes a model doesn't need all the information in the context window, and sometimes the context window is actively harmful because prompt injection can get in. Context engineering helps optimize the window for better results and token savings.

She combines several methods into a strategy: external storage to move big data to persistent storage with a memory pointer; selection/compression to extract only what is relevant and summarize reduced tokens; and isolation to share context between agents. She demonstrates these using the open-source, model-agnostic Strands agent framework, which offers a sliding window (keep only the most recent messages), summarization (summarize old messages while preserving the latest), and a combination of both. A conversation manager can be configured with a summarization ratio (e.g., 50%) and a number of recent messages to keep (e.g., four).

She also distinguishes short-term memory, where recent conversation history is stored, from long-term memory backed by a vector database for when a new session starts and short-term memory is unavailable.

- The infinite context window is a myth: agents break when tools return large data, overflowing the window and causing hallucination and degraded reasoning.
- The model's attention curve means that with too much data the model forgets the middle and only remembers the beginning and end of the context.
- Context engineering — giving the model the right information exactly when needed — optimizes results and saves tokens, and can also reduce prompt-injection risk.
- Key strategies include external storage with memory pointers, selection/compression of relevant data, and isolation for sharing context between agents.
- The open-source, model-agnostic Strands framework provides sliding-window, summarization, and combined conversation-manager strategies, with short-term memory for recent history and vector-database long-term memory for new sessions.