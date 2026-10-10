---
domain: system-design
subdomain: observability
concept: proxy-layer-tracing
title: Cloudflare Traces Turns the Proxy Layer into OpenTelemetry Spans, with New Volume-Based Pricing
sources:
  - title: "Cloudflare Traces Turns the Proxy Layer into OpenTelemetry Spans, with New Volume-Based Pricing"
    url: "https://www.infoq.com/news/2026/10/cloudflare-traces-open-beta/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-10"
---

# Cloudflare Traces Turns the Proxy Layer into OpenTelemetry Spans, with New Volume-Based Pricing

Cloudflare has moved Traces into open beta, extending automatic tracing beyond Workers to cover security rules, transformations, cache, routing, and origin handling, all emitted as OpenTelemetry spans. This means the proxy layer itself becomes observable through standard OTel telemetry rather than only the application code running on Workers.

Traces accept and forward W3C traceparent headers, enabling context propagation across the request path, and Trace Rules allow targeted sampling so teams can control which traffic is traced. Pricing shifts to ingestion and retention volume starting December 1, replacing the prior model.

- Cloudflare Traces is now in open beta, extending automatic tracing from Workers to security rules, transformations, cache, routing, and origin handling.
- Traces are emitted as OpenTelemetry spans and accept/forward W3C traceparent headers for context propagation.
- Trace Rules enable targeted sampling of requests.
- Pricing moves to ingestion and retention volume from December 1.