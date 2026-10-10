---
domain: system-design
subdomain: event-streaming
concept: object-storage-backed-event-log
title: Cloudflare K2 Builds Event Streams on R2 Object Storage
sources:
  - title: "Cloudflare K2 Builds Event Streams on R2 Object Storage, at a Second of Produce Latency"
    url: "https://www.infoq.com/news/2026/10/cloudflare-k2-serverless-streams/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-09"
---

# Cloudflare K2 Builds Event Streams on R2 Object Storage

Cloudflare has launched K2 in public beta, a serverless event streaming service that implements a durable log on top of R2 object storage [1]. The service targets produce latency of roughly one second at p99, according to Cloudflare [1].

A tester reported an end-to-end p99 latency of 7.5 seconds, which a commenter responding on behalf of the team acknowledged was higher than expected [1]. Consume charges are stated to match produce charges per GB [1].

- K2 is a serverless event streaming service built as a durable log on R2 object storage, now in public beta [1].
- Cloudflare claims produce latency of about one second at p99 [1].
- An independent tester measured end-to-end p99 of 7.5 seconds, which the team said was higher than expected [1].
- Consume pricing matches produce pricing per GB [1].