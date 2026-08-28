---
domain: system-design
subdomain: background-jobs
concept: offloading-cpu-intensive-tasks
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    author: "Kent C. Dodds"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

The author initially ran FFmpeg inline on the primary Fly.io server that also serves kentcdodds.com. This simple design worked for 226 podcast episodes, but a particularly long recording caused CPU saturation (load average 400–500%) and site degradation, forcing an emergency machine upgrade. The incident highlighted that the primary machine is the worst place for CPU-heavy work because it handles all writes and must remain responsive.

The new architecture moves FFmpeg to Cloudflare Queues and Containers. The app enqueues a job with draft ID and R2 object keys, a Cloudflare Worker forwards it to a container that pulls audio from R2, runs the FFmpeg pipeline, uploads outputs back, and POSTs a signed callback. The app verifies the HMAC signature and advances the draft status. This reduces peak load on the primary server from 400–500% to 60–80%, with no throttling.

The article also covers costs (Cloudflare scales to zero, while a dedicated Fly.io machine has ongoing costs) and lessons learned: remove fallback paths that hide risks, manage container lifecycle with heartbeats and immediate stop-on-idle, and avoid long-running workers by returning 202 Accepted. The author concludes that simple-first design was correct until reality demanded iteration, and the tooling available made the migration worthwhile.

- Running CPU-intensive tasks like FFmpeg on the primary app server risks site degradation; isolate them to a separate compute environment.
- Cloudflare Queues + Containers provide an event-driven pipeline where the app enqueues a job and returns immediately, keeping the primary server responsive.
- A fallback that runs the heavy task locally is counterproductive—it hides outage risk instead of eliminating it.
- Container lifecycle management needs explicit control (heartbeats and stop-if-idle) to avoid premature shutdown or wasted resource billing.
- Start simple and iterate when real incidents reveal scaling pain; the tooling landscape may have improved by then.