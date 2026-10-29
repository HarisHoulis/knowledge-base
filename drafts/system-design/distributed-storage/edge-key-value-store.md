---
domain: system-design
subdomain: distributed-storage
concept: edge-key-value-store
title: Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope
sources:
  - title: "Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope"
    url: "https://www.infoq.com/news/2026/10/workers-kv-instant/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-28"
---

# Cloudflare Opens Quicksilver to Customers as Workers KV Instant, Inside a 1 MB Envelope

Cloudflare has exposed Quicksilver, the internal key-value store that backs nearly every request it serves, as a private beta mode of Workers KV called Workers KV Instant (InfoQ, 2026). The headline gain is latency: reads resolve at 1.62 ms p99 versus 287 ms for classic KV, a roughly two-orders-of-magnitude improvement for edge lookups.

The trade-off is a deliberately tight envelope. Each namespace is capped at 10,000 keys and one megabyte of total data, and writes are limited to one per namespace per second. Those constraints, not the latency figure, are what determine whether a workload fits: the mode suits small, read-heavy, slowly changing configuration or routing data rather than general-purpose storage.

The design reflects Quicksilver's role as an internal fast-path store, where data is small and replicated aggressively for low-latency reads. Exposing it to customers means accepting that same shape of workload. Teams evaluating it should treat the write-rate and size limits as architectural boundaries, not tuning knobs.

- Workers KV Instant is a private beta mode exposing Cloudflare's internal Quicksilver store to customers.
- Read latency drops to 1.62 ms p99 from 287 ms for classic Workers KV.
- Hard limits: 10,000 keys, 1 MB per namespace, and one write per namespace per second.
- The constraints make it suitable for small, read-heavy, rarely updated data rather than general storage.