---
domain: ai-workflows
subdomain: ai-concepts
concept: ai-terminology-and-model-evolution
title: AI Terms You Need to Know: From Agentic AI to GPT-6
sources:
  - title: "EP231: AI Terms You Need to Know"
    url: "https://blog.bytebytego.com/p/ep231-ai-terms-you-need-to-know"
    author: "ByteByteGo"
    date: "2026-10-31"
---

# AI Terms You Need to Know: From Agentic AI to GPT-6

This ByteByteGo refresher defines core AI vocabulary and traces the evolution of GPT models. Agentic AI is described as a system-level behavior: the agent interprets a goal, plans, calls tools and APIs, evaluates results, and self-corrects until the goal is met. A Large Reasoning Model is trained to solve problems requiring many logical steps by decomposing them into smaller sub-problems. A Vector Database stores vectors (lists of numbers) that encode the meaning and characteristics of text, audio, video, or other data. Retrieval Augmented Generation (RAG) supplies relevant information to a model on demand, typically from a vector database but also via APIs, SQL, or hybrid search. The Model Context Protocol (MCP) provides a standard interface for AI applications to connect to external tools and APIs, with an MCP client inside the application communicating through MCP servers.

The article then charts GPT generations. GPT-2 (2019) was a 1.5B-parameter decoder-only prototype trained only on next-token prediction, capable of continuing text but not answering questions. GPT-3 (2020) kept the same recipe at 175B parameters and showed in-context learning from examples. GPT-4 (2023) added RLHF fine-tuning, multimodality, and a 32K-token context. GPT-5 (2025) introduced built-in reasoning tokens, a 400K context window, and a router deciding when thinking mode is needed. GPT-6 (2026) expands context to 1.05M tokens, supports async tool calling, is generally safer, and adds mid-turn steering so it can accept a new instruction while thinking.

Rounding out the issue, the author lists AI/ML interview topics split into Traditional AI (pre-neural-network ML fundamentals) and Modern AI (neural network foundations, transformers, RAG, post-training), noting interviewers expect both and want explanations of how things work, when they break, and their trade-offs. A final section explains GPU parallelism: many Streaming Multiprocessors each contain a warp scheduler, CUDA cores, register file, load/store and texture units, and L1 cache, connected via an on-chip interconnect to a shared L2 cache and memory controllers fronting high-bandwidth, high-latency global memory—which is why GPUs rely on massive parallelism to hide memory latency.

- Agentic AI is defined by system behavior—goal interpretation, planning, tool use, evaluation, and self-correction—not by a single model.
- RAG retrieves relevant context on demand from vector databases or other sources (APIs, SQL, hybrid search); MCP standardizes how AI apps connect to external tools via clients and servers.
- GPT evolution moved from pure pre-training (GPT-2, GPT-3) to RLHF and multimodality (GPT-4), built-in reasoning (GPT-5), and async tool calling plus mid-turn steering (GPT-6).
- AI/ML interviews test fundamentals across both Traditional AI and Modern AI, emphasizing mechanisms, failure modes, and trade-offs.
- GPUs achieve performance through massive parallelism across many SMs, hiding high-latency global memory behind thousands of concurrently executing threads.