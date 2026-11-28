---
domain: ai-workflows
subdomain: edge-ai-platforms
concept: edge-ai-infrastructure
title: Why Cloudflare Became a Neolab
sources:
  - title: "Why Cloudflare Became a Neolab — Michelle Chen, Cloudflare"
    url: "https://www.youtube.com/watch?v=cYcYfM9Mvwo"
    author: "AI Engineer"
    date: "2026-11-27"
---

# Why Cloudflare Became a Neolab

Michelle Chen, Group Product Manager at Cloudflare, traces the company's evolution from a 16-year-old CDN into what she calls a "Neolab." Cloudflare began as a CDN that sits between user requests and origin servers, doing caching and security. Unlike hyperscalers that concentrate compute in regions like US East 1, Cloudflare built data centers distributed around the world, as close to users as possible, and launched on its own infrastructure in 2010.

That distributed footprint became the basis for a developer platform. In 2017 Cloudflare launched Workers, serverless functions with millisecond startup that you pay for only while executing, followed by Durable Objects for more stable state and containers in 2025 for workloads that need a virtual machine. Storage primitives like KV, R2 object storage, and the D1 database let people build full-stack applications on the platform.

In 2023, prompted by ChatGPT's rise, Cloudflare launched Workers AI, adding GPUs to its network so inference runs as close to the edge as possible rather than in a centralized region. The original hypothesis was that as models got smaller, network latency would matter more, but the opposite happened: models grew from roughly 7 billion parameters, then state of the art, toward 3 trillion parameters.

- Cloudflare's edge-distributed infrastructure, built for CDN delivery, became the foundation for its developer and AI platform.
- Workers (2017) introduced serverless functions with millisecond startup and pay-per-execution pricing, later joined by Durable Objects and containers.
- Storage primitives (KV, R2, D1) enable full-stack applications on Cloudflare.
- Workers AI (2023) added GPUs distributed to the edge; the bet on smaller models and latency proved wrong as models grew far larger.