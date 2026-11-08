---
domain: system-design
subdomain: distributed-databases
concept: control-plane-scaling
title: Cloudflare Scales D1 Control Plane to Millions of Databases
sources:
  - title: "Cloudflare Scales D1 Control Plane to Millions of Databases"
    url: "https://www.infoq.com/news/2026/11/cloudflare-d1-control-plane/"
    author: "Renato Losio"
    date: "2026-11-08"
---

# Cloudflare Scales D1 Control Plane to Millions of Databases

Cloudflare redesigned the control plane of its D1 serverless SQL database to support millions of databases. The redesign avoids centralized bottlenecks, adds retries and idempotency, and relies on eventual consistency (InfoQ, Losio, 2026).

The article frames the control plane as the coordination layer that must scale alongside the data plane, and describes the core techniques used: eliminating centralized bottlenecks, making operations retry-safe through idempotency, and accepting eventual consistency rather than requiring strong consistency across the control plane.

- Cloudflare redesigned D1's control plane to handle millions of databases
- The design avoids centralized bottlenecks
- Retries and idempotency are used to make operations safe
- The control plane relies on eventual consistency