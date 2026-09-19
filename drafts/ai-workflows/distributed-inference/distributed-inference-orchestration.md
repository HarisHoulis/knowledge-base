---
domain: ai-workflows
subdomain: distributed-inference
concept: distributed-inference-orchestration
title: Operating Distributed Inference Systems at Scale
sources:
  - title: "Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta"
    url: "https://www.youtube.com/watch?v=7c9FSUVcXR0"
    author: "AI Engineer"
    date: "2026-09-19T15:00:10+00:00"
---

# Operating Distributed Inference Systems at Scale

Nishant Gupta and Naman Ahuja of Meta argue that inference is no longer just a research artifact or product bolt-on but a foundational hyperscale infrastructure workload. They state that inference traffic already outpaces the largest microservices in the world and is growing faster than any workload previously seen (Nishant Gupta & Naman Ahuja, Meta). They compare the AI era to the cloud era: cloud value moved from virtual machines to scheduling, service meshes, autoscalers, and platforms, and AI is following the same trajectory in compressed time. Model serving frameworks like vLLM and Triton are now giving way to an orchestration layer that handles routing, KV cache management, prefill/decode disaggregation, and multi-model multiplexing.

The talk highlights an agentic demand explosion that breaks traditional capacity planning. In classical web serving, capacity scaled roughly linearly with users, so doubling users mostly doubled QPS and infrastructure. In agentic serving, capacity scales with users × calls per user × tokens per call, and calls per turn can vary from one for a chatbot to 10–20 for copilots, 50 for research agents, and thousands for autonomous workflows with no human in the loop. The speakers conclude that agents cannot be planned for like microservices; operators need elasticity, workload-aware scheduling, and admission control.

LLM inference also differs sharply from microservice serving across request shape, batching, state, scaling units, and failure modes. Requests can range from 50 to 100,000 tokens with vastly different compute profiles for prefill and decode. LLM serving requires continuous in-flight batching, otherwise throughput collapses by an order of magnitude. It also requires a large per-request KV cache that is expensive to build and even more expensive to discard. GPUs are 100 times more expensive than CPUs, 10 times slower to acquire, and cannot be casually overprovisioned. Mid-decode GPU failure can drop thousands of in-flight tokens and cause queue buildup. The speakers emphasize that the bottleneck is not just the model but the orchestration itself, including hidden decisions behind a prompt such as authentication, model selection, region selection, admission control, caching lookup, GPU execution, and batching.


- Inference is now a hyperscale infrastructure workload whose traffic outpaces the largest microservices and is growing faster than any prior workload.
- AI infrastructure is following the cloud era's trajectory: value and complexity are shifting to the orchestration/control plane, including routing, KV cache management, prefill/decode disaggregation, and multi-model multiplexing.
- Agentic workloads scale as users × calls per user × tokens per call, so capacity planning cannot be a spreadsheet exercise; elasticity, workload-aware scheduling, and admission control are required.
- LLM serving differs from microservices: highly variable request sizes, continuous in-flight batching, expensive per-request KV cache, costly GPUs, slow cold starts, and mid-decode failures that drop in-flight tokens.
- The bottleneck is orchestration, not just the model; a prompt triggers hidden steps like authentication, model choice, region selection, admission control, caching lookup, GPU execution, and batching.