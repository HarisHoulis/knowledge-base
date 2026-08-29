---
domain: system-design
subdomain: background-job-offloading
concept: offloading-ffmpeg-to-cloudflare
title: Offloading FFmpeg with Cloudflare
sources:
  - title: "Offloading FFmpeg with Cloudflare"
    url: "https://kentcdodds.com/blog/offloading-ffmpeg-with-cloudflare"
    author: "Kent C. Dodds"
    date: "2026-03-09"
---

# Offloading FFmpeg with Cloudflare

The article describes how the author initially ran FFmpeg inline on the primary Fly.io machine that serves kentcdodds.com, processing podcast audio during the publish flow. This simple approach worked for 226 episodes but broke on a long episode, causing extreme CPU saturation (load average 400–500%) and site degradation. The author argues that this simple-first design was reasonable, but the failure exposed the primary machine as the worst place for compute-heavy work because it handles all write operations and cannot afford to be slow [1]. 

The new architecture offloads FFmpeg to Cloudflare using Queues, Workers, and Containers. The app enqueues a job with draft and R2 object keys, a Worker forwards to a Container that processes audio from R2, and a signed callback updates the app. This reduced peak load on the primary machine by roughly 85% (60–80% vs 400–500%) with no throttling. The article also covers cost analysis, noting that Cloudflare's pay-per-use model scales to zero and is cost-effective for sporadic podcast publishing, and shares lessons about removing fallback paths and managing container lifecycle through heartbeats and stop-if-idle signals [1]. 

The author emphasizes that the original simple design was validated by 226 incident-free episodes, and the iteration only became necessary when reality demanded it. However, they caution against always using job queues, as complexity should be introduced when pain is actually felt [1].

- Running FFmpeg inline on the primary web server caused extreme CPU saturation and site degradation when a long episode was published; offloading to Cloudflare reduced peak load by ~85%.
- The new architecture uses Cloudflare Queues to enqueue jobs, a Worker to forward them, and a Container to run FFmpeg with audio from R2, with a signed callback to the app.
- Cost-wise, Cloudflare scales to zero and is nearly free for a few episodes per month, whereas a dedicated Fly.io machine would incur ongoing costs and lifecycle management.
- Avoid fallback paths that re-run heavy compute on the primary server, and manage container lifecycle via heartbeats and immediate stop signals to prevent wasted resources.
- A simple-first approach was appropriate; only add queue infrastructure when real incidents justify the added complexity.