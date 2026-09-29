---
domain: system-design
subdomain: data-center-networking
concept: homa-protocol
title: Homa: The End of TCP for AI Clusters
sources:
  - title: "Homa: The End of TCP for AI Clusters — John Ousterhout, Stanford"
    url: "https://www.youtube.com/watch?v=eZ8WWZzoaR0"
    author: "AI Engineer"
    date: "2026-09-17T13:00:08+00:00"
---

# Homa: The End of TCP for AI Clusters

AI workloads have historically consisted of enormous transfers between machines, such as gigabytes of weight gradients, where throughput is the key metric. In those environments, TCP and RDMA — specifically RoCE — perform well because connection setup latency is negligible relative to long-running transfers (Ousterhout, 2026).

Ousterhout argues that AI workloads are changing, especially in inference and agentic workloads, toward smaller, more granular exchanges. These include metadata and coordination messages, checking for entries in distributed KV caches, and barrier synchronization between compute phases. For these workloads, round-trip latency — and especially tail latency — is crucial (Ousterhout, 2026).

High tail latency can stall the whole system: if computation phases are split across nodes, all exchanges must complete before the next GPU compute phase begins. As agentic workloads push computation periods toward millisecond scales, slow small-message exchanges become more costly. Legacy protocols like TCP and RDMA are poorly suited when small messages are mixed with large ones and suffer from high tail latency (Ousterhout, 2026).

To address this, Homa is a clean-slate protocol developed at Stanford for data center workloads. It is designed to handle these latency-sensitive patterns and can reduce tail latency by an order of magnitude or more (Ousterhout, 2026).

- AI workloads are shifting from throughput-dominated large transfers to latency-sensitive small exchanges in inference and agentic workloads.
- Tail latency matters because synchronization delays can leave GPUs idle while waiting for the slowest exchange to complete.
- TCP and RDMA/RoCE were designed for large transfers and are poorly suited to mixed small and large messages, causing high tail latency.
- Homa, a clean-slate Stanford protocol, is designed for data center workloads and can reduce tail latency by an order of magnitude or more.