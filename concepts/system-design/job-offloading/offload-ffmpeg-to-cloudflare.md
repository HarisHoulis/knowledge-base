---
domain: system-design
subdomain: job-offloading
concept: offload-ffmpeg-to-cloudflare
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    author: "Kent C. Dodds"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

The article recounts how running FFmpeg inline on the primary Fly.io server for the Call Kent podcast eventually caused severe CPU throttling and site degradation during a long episode publish. The original design was intentionally simple—serving 226 episodes without incident—but when a single extra-long recording pushed load to 400-500% on the shared-CPU primary machine, the author moved the FFmpeg pipeline off the critical path entirely (Kent C. Dodds, 2026).

- Simple-first designs can work for a long time; the original inline FFmpeg was fine until a single large episode exceeded the CPU quota.
- The primary server is the worst place for compute-heavy tasks because it also handles all writes; replicas are read-only and cannot substitute.
- The new architecture uses Cloudflare Queues to enqueue jobs, a Worker to dispatch to a Cloudflare Container running FFmpeg, and R2 for storage, with a signed callback to the app.
- Heartbeats and explicit container stop signals prevent premature shutdown or idle billing, and the queue worker no longer blocks on the full job.
- Costs are near-zero for a low-volume podcast, and the main benefit is operational isolation—the app server stays responsive even during long transcodes.