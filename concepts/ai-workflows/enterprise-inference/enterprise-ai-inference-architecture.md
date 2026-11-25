---
domain: ai-workflows
subdomain: enterprise-inference
concept: enterprise-ai-inference-architecture
title: Inferencing for Enterprises
sources:
  - title: "Presentation: Inferencing for Enterprises"
    url: "https://www.infoq.com/presentations/enterprise-ai-inference-architecture-costs/"
    author: "Dio Rettori"
    date: "2026-11-24"
---

# Inferencing for Enterprises

Dio Rettori's presentation examines the operational realities of running AI inference at enterprise scale, arguing that fast token generation alone is insufficient and that inference demands dedicated systems engineering. He covers GPU utilization pitfalls, comparing on-prem versus cloud total cost of ownership, and the latency determinism challenges of multi-agent systems.

A central architectural argument is that teams should embed domain ontology directly into models rather than relying solely on retrieval-augmented generation (RAG). The talk frames inference as an engineering discipline spanning cost, performance, and model design rather than a simple serving concern.

- Enterprise inference requires dedicated systems engineering beyond fast token generation
- GPU utilization pitfalls and on-prem vs cloud TCO are key operational tradeoffs
- Multi-agent systems introduce latency determinism challenges
- Embedding domain ontology into models is preferred over relying solely on RAG