---
domain: system-design
subdomain: background-jobs
concept: offloading-compute-heavy-tasks-to-cloudflare
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    author: "Kent C. Dodds"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

In this article, Kent C. Dodds describes how he moved the FFmpeg audio processing for his podcast 'Call Kent' off the primary Fly.io instance that serves kentcdodds.com. Initially, FFmpeg ran inline during the publish flow on the same machine, which worked for 226 episodes but caused extreme CPU saturation (load average 400–500%) and throttling when a longer-than-usual episode was processed (Source: Offloading FFmpeg with Cloudflare, https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare). 

The new architecture enqueues a job to a Cloudflare Queue when an episode is submitted. A Worker forwards the job to a Cloudflare Container, which pulls audio files from R2, runs the FFmpeg stitching pipeline, uploads outputs back to R2, and sends a signed callback to the app to update the draft status. This offload reduced the primary machine's peak load to 60–80% and eliminated CPU throttling. The article also covers the cost implications, the trade-offs of scaling to zero, and lessons learned about removing a fallback path, managing container lifecycle with heartbeats, and ensuring the queue worker acks quickly rather than blocking on the entire job (Source: Offloading FFmpeg with Cloudflare, https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare). 

The author emphasizes that the original simple design was the right starting point, and the iteration was prompted by a real incident, not speculative scalability concerns. He also notes that this approach might not suit steady high-volume workloads, but for intermittent jobs, Cloudflare Queues and Containers offer a clean, cost-effective isolation from critical infrastructure (Source: Offloading FFmpeg with Cloudflare, https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare).

- Running FFmpeg inline on a critical primary instance can cause severe CPU throttling and site degradation; offloading it to a queue and isolated worker prevents this.
- Cloudflare Queues and Containers provide a scalable, 'scale-to-zero' solution for intermittent batch processing, with costs mostly incurred only when the container runs.
- Avoid hidden fallback paths that reintroduce the original bottleneck; instead, fail loudly and keep the job in a retryable state.
- Queue workers should acknowledge messages quickly and let the container process run asynchronously, not block for the entire job duration.
- Start simple and only add architectural complexity when real usage justifies it; the author's inline FFmpeg worked for 226 episodes before failing.