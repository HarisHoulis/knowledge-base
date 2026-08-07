---
domain: ai-workflows
subdomain: agent-loop-optimization
concept: harness-api-inference-layers
title: How ChatGPT Optimizes its Agent Loop: Harness, API, and Inference
sources:
  - title: "How ChatGPT Optimizes its Agent Loop: Harness, API, and Inference"
    url: "https://blog.bytebytego.com/p/how-chatgpt-optimizes-its-agent-loop"
    author: "ByteByteGo"
    date: "2026-07-29"
---

# How ChatGPT Optimizes its Agent Loop: Harness, API, and Inference

The article explains that modern AI agent applications like Codex are not a single LLM call but a multi-layer system. User queries pass through a harness layer, which manages the conversation and executes tool calls; an API layer, which handles authentication, rate limiting, and tokenization; and an inference layer, which runs the model on GPUs. Each layer introduces overhead, and a single task can repeat the loop over 100 times, so optimizing every layer is critical to reduce cost per successful task.

At the harness layer, OpenAI uses persistent WebSockets to avoid repeated TCP/TLS handshakes and sends only the delta (new tool result) with a reference to the previous response, instead of resending the entire payload. They also maintain stable prompt prefixes by treating history as append-only, keeping volatile state out of prompts, and using deferred tool discovery via BM25 search so only the needed tool schemas are loaded. Code Mode further reduces round trips by letting the model emit a script that makes multiple tool calls inside an embedded JavaScript runtime, returning only the compact final result.

At the API layer, OpenAI tokenizes only the delta rather than the full conversation, and runs safety classifiers in parallel with inference, letting them finish before the first token is generated. The inference layer employs cache-aware routing to send requests to GPUs with matching prefix caches, manages KV cache memory efficiently, uses speculative decoding to generate multiple candidate tokens in parallel, and separates prefill and decode phases to maximize GPU utilization. These optimizations explain how GPT-5.6 Sol can outperform Fable 5 on coding benchmarks while costing less than half as much per task.

The key takeaway is that eliminating repeated work across all three layers—network payloads, tokenization, and prompt computation—yields significant cost and latency improvements. The article suggests that developers can apply these principles to their own agentic systems by keeping contexts append-only, using stable prefixes, moving orchestration into a client-side runtime, and designing layers with explicit responsibilities.

- Cost per successful task is the real metric; capability alone is insufficient.
- Persistent WebSockets and delta payloads eliminate redundant connection setup and data transfer in agent loops.
- Stable prompt prefixes and deferred tool discovery maximize prompt caching and keep context compact.
- Code Mode reduces model round trips by executing multi-tool scripts in an embedded runtime.
- Inference optimizations (cache-aware routing, KV cache management, speculative decoding, prefill/decode separation) dramatically lower GPU cost per task.