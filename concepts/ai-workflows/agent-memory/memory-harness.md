---
domain: ai-workflows
subdomain: agent-memory
concept: memory-harness
title: Memory Harnesses for Long-Running Research Agents
sources:
  - title: "Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai"
    url: "https://www.youtube.com/watch?v=R3-anFK1YM8"
    author: "Stefania Druga"
    date: "2026-08-12T15:00:06+00:00"
---

# Memory Harnesses for Long-Running Research Agents

Research agents tackling long-horizon tasks often suffer from context rot: models contradict themselves, repeat work, or drift from user questions. With industry trends pointing toward longer tasks and fewer model releases, managing context effectively becomes a critical priority (Druga, 2026).

Local models are increasingly viable for agentic tool use, as demonstrated by companies like Coinbase cutting AI spend while increasing usage through local models, better routing, caching, and keeping context clean. The speaker's harness runs on a Mac M3 Ultra (96GB, 28-core CPU) using Qwen 27B (4-bit quantized) and DeepSeek V4 Flash, with a design built around a core trace, a recall block, and an archival block (Druga, 2026).

Memory is conceptualized as a write-manage-read control loop around the model, not merely a database store. The recall block compares several modes: no memory baseline, vector RAG, a decisions ledger, and an oracle ground truth. In an example literature-review task, a retracted scientific claim is the correct answer hidden among more prominent headlines, testing whether the system can retrieve that needle (Druga, 2026).

- Context rot is a key failure mode in long-running agents, leading to contradictions, repeated work, and loss of user intent.
- The trend toward longer horizon tasks and fewer model releases makes memory management essential.
- Local models are becoming practical for agentic tasks; a Mac M3 Ultra can run Qwen 27B (4-bit) and DeepSeek V4 Flash.
- Memory is best treated as a write-manage-read loop, with recall modes ranging from none to vector RAG, decisions ledger, and oracle.
- Testing on asymmetrical information (e.g., a retracted claim) reveals how effective each recall mode is at retrieving the correct memory.