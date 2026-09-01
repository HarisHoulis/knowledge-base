---
domain: system-design
subdomain: background-job-offloading
concept: offload-ffmpeg-to-cloudflare
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    author: "Kent C. Dodds"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

Kent C. Dodds describes how his podcast publishing pipeline initially ran FFmpeg inline on the same Fly.io primary instance serving kentcdodds.com. For 226 episodes this worked fine, but on March 6, 2026, an extra-long episode caused load averages of 400–500%, CPU throttling, and site degradation, forcing an emergency upgrade (source: Kent C. Dodds, 2026). The incident revealed that the primary machine is the worst place for compute-heavy work because it also handles all write operations, and stalling it affects every stateful user action.

The new architecture enqueues a job to Cloudflare Queues when an episode is submitted, with draft ID and R2 keys. A Cloudflare Worker consumes the message and forwards it to a Cloudflare Container, which pulls audio from R2, runs FFmpeg, uploads outputs back to R2, and POSTs a signed callback to the app. The app verifies the HMAC-SHA256 signature and advances the draft through states. The admin UI now shows incremental progress. After the offload, peak load dropped to 60–80% on the same machine, an ~85% reduction (source: Kent C. Dodds, 2026).

Dodds also discusses cost, noting Cloudflare's pay-per-use model scales to zero for a personal podcast but a dedicated Fly machine might be simpler for steady high-volume workloads. He highlights operational isolation as the main benefit. He mentions three first-pass mistakes: a local FFmpeg fallback that masked failures and was removed; container lifecycle issues solved with heartbeats and stop-if-idle signals; and the queue worker initially blocking on the full transcode, which was fixed by returning 202 Accepted immediately (source: Kent C. Dodds, 2026).

- Running FFmpeg inline on the primary app server caused severe CPU saturation and throttling on long episodes.
- Offloading to Cloudflare Queues + Containers reduced peak load on the primary machine by ~85%.
- Cloudflare's pay-per-use model is cost-effective for sparse workloads, but the real win is operational isolation.
- A 'safety net' local fallback was counterproductive and was removed; failures should surface for retry.
- Container lifecycle needs careful management via heartbeats and immediate shutdown when idle to avoid wasted resources.