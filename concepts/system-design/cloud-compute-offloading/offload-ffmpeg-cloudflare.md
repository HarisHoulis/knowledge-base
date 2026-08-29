---
domain: system-design
subdomain: cloud-compute-offloading
concept: offload-ffmpeg-cloudflare
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

Running FFmpeg inline on the primary web server worked for 226 podcast episodes, but a long episode on March 6, 2026 caused extreme CPU saturation (load average 400–500%) and throttling, degrading kentcdodds.com. The author acknowledges the original design was a reasonable simple-first choice, but the incident made it clear that the primary machine—which handles all writes—was the worst place for CPU-heavy work. The fix moves FFmpeg to Cloudflare using Queues, Workers, Containers, and R2 storage (source: https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare).

The new architecture enqueues a job when an episode is submitted, a Worker forwards it to a Cloudflare Container, which downloads audio from R2, runs the FFmpeg stitching pipeline, uploads the result, and sends a signed callback to the app. The primary machine no longer blocks on FFmpeg; load during episode processing dropped to 60–80%, roughly an 85% reduction. Cloudflare's pay-as-you-go pricing makes the cost nearly zero for a personal podcast, but the larger benefit is operational isolation—the app server is no longer in the blast radius of long transcodes (source: https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare).

Several implementation pitfalls surfaced after the initial PR: a local fallback path that could run FFmpeg on the primary machine was removed because it reintroduced the exact risk being eliminated; container lifecycle management required heartbeats and an explicit stop-if-idle signal to avoid premature shutdown or idle billing; and the queue worker should return 202 Accepted immediately rather than waiting for the entire job. The author concludes that starting simple was still the right call, and that job queues are not always necessary until you feel the pain (source: https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare).

- Inline FFmpeg on the primary Fly.io machine caused extreme CPU saturation and throttling during a long episode, degrading the site.
- The new architecture offloads FFmpeg to Cloudflare Queues, Workers, and Containers, using R2 for storage and signed callbacks for completion.
- Primary machine load dropped from 400–500% to 60–80% during episode processing, an 85% reduction.
- Local fallback was removed because it would hide risk; container lifecycle needs heartbeats and explicit stop to avoid premature shutdown or idle billing.
- Starting simple with inline processing was a reasonable choice until reality demanded iteration, but the right tooling was available when needed.