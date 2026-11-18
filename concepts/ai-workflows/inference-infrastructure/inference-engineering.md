---
domain: ai-workflows
subdomain: inference-infrastructure
concept: inference-engineering
title: Inference Engineering for Software Engineers
sources:
  - title: "Inference engineering for software engineers"
    url: "https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers"
    author: "Gergely Orosz"
    date: "2026-11-17"
---

# Inference Engineering for Software Engineers

Inference providers are companies that host open-weight LLMs on large GPU fleets and sell API access, differing from frontier labs in that they don't pre-train their own models. Modal, Fireworks, and Baseten each take different approaches: Modal emphasizes programmable cloud infrastructure and open-source tooling, Fireworks focuses on specialized workloads with dedicated deployments and fine-tuning, and Baseten positions itself as an all-in-one platform for building agents. Inference providers compete on efficiency and customization, and their uptime can exceed frontier labs, whose self-declared availability (e.g. Anthropic at 99.5%) falls short of the four nines expected of cloud providers.

Teams typically move from frontier labs to inference providers for cost, control, and customization. Smart routing—prompt-aware routing to the cheapest capable model—drove roughly 50% per-token cost cuts at Uber. Choosing a model should rely on private eval sets rather than generic benchmarks, since public per-task cost comparisons (e.g. Artificial Analysis) don't capture a team's own traffic patterns. Provider selection also matters because providers tweak open models differently, yielding endpoint accuracy scores ranging from 93% to 102%.

Onboarding usually starts with a multi-tenant API swap, but rate limits, inconsistent performance, and overpaying signal it's time to move to dedicated GPU nodes. Dedicated deployments give control over latency and model availability, and require decisions about model size, interactivity versus throughput, KV cache sizing, and failover. Fine-tuning or post-training smaller models for niche use cases is a power-user step (about 10% of Modal's customers), and speculative decoding can exploit unused compute during the decode phase. Because any single provider can degrade or go down, teams commonly use an LLM gateway with fallback logic across providers.

- Inference providers host open-weight models and compete on efficiency, pricing, and customization rather than pre-training frontier models
- Switch from frontier labs for cost, latency control, and fine-tuning; use private evals rather than public benchmarks to pick a model
- Multi-tenant API swaps are the easiest start, but rate limits and inconsistent performance signal a move to dedicated GPUs
- Dedicated deployments require tuning model size, KV cache, throughput vs interactivity, and failover; speculative decoding can boost performance
- Use an LLM gateway with fallback logic since any single provider can degrade or go down