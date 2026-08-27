---
domain: system-design
subdomain: background-processing
concept: offloading-ffmpeg-to-cloudflare
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

The article recounts the author's experience running FFmpeg directly on the primary Fly.io instance for 226 podcast episodes, which worked until an extra-long episode caused CPU saturation (400–500% load average) and site degradation, prompting an emergency upgrade. The author defends the original simple design, noting it was a reasonable first choice and that the problem only surfaced when audio length and CPU quota collided [1]. The new architecture moves FFmpeg to Cloudflare: the app enqueues a job to Cloudflare Queue, a Worker passes it to a Container, and the container pulls audio from R2, processes it, uploads results, and sends a signed callback. The app verifies the HMAC signature and updates the draft status. Metrics show an 85% reduction in peak load (60–80% vs 400–500%) with no throttling [1]. The author discusses costs and operational lessons. Cloudflare's pay-per-use model scales to zero, but the container's lifecycle required careful design—heartbeat pings and stop-if-idle instructions through the Worker/Durable Object boundary. He also removed a local fallback that would have secretly reintroduced the original risk. The takeaway is to start simple and iterate when reality demands it [1].

- Moving FFmpeg off the primary app server eliminated CPU throttling and site degradation.
- New flow: enqueue to Cloudflare Queue → Worker → Container → callback with HMAC signature.
- Load average dropped from 400–500% to 60–80%, an ~85% reduction.
- Cost is usage-based and scales to zero; remove hidden fallbacks that reintroduce risk.