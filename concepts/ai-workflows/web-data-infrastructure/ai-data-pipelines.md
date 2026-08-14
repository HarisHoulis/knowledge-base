---
domain: ai-workflows
subdomain: web-data-infrastructure
concept: ai-data-pipelines
title: How Web Data Infrastructure Powers the Next Generation of AI
sources:
  - title: "How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs"
    url: "https://www.youtube.com/watch?v=1UmZHb_E_SM"
    author: "AI Engineer"
    date: "2026-08-14T17:00:37+00:00"
---

# How Web Data Infrastructure Powers the Next Generation of AI

The talk argues that modern AI models require fresh, real-time web data beyond static training. Oxylabs builds infrastructure for extracting public web data at scale, which is critical for connecting AI models, agents, and databases. Without this infrastructure layer, even the most capable models are limited by their static knowledge (Žemaitytė, 2026).

A central case study describes a two-week deadline to build a video API for AI training, expected to handle at least 5 petabytes per month. Starting as a simple downloader, the product evolved through repeated client feedback—first transcripts, then subtitles, then search, then metadata—eventually becoming a full product suite in roughly three months. This illustrates how innovation often emerges as repeated adaptation under high pressure rather than from a neat roadmap (Žemaitytė, 2026).

The broader lesson is that AI infrastructure is becoming increasingly multimodal, requiring pipelines for video, metadata, transcripts, subtitles, and other structural context. The story also highlights real-world business realities, such as the humorous twist that after gathering 30 petabytes of data, payment was still pending, underscoring that technical success and commercial recovery are distinct challenges (Žemaitytė, 2026).

- AI models need access to fresh, real-time web data to remain useful; static training alone is insufficient.
- Building scalable web data infrastructure involves pipelines for collection, transfer, storage, and delivery.
- Product features evolve rapidly under client pressure; innovation is repeated adaptation under high-pressure deadlines.
- AI infrastructure is becoming increasingly multimodal, needing support for video, transcripts, subtitles, metadata, and more.
- Practical challenges include extremely large scales (e.g., 5 PB/month) and business issues like delayed payments.