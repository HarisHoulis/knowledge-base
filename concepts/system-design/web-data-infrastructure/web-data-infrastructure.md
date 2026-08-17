---
domain: system-design
subdomain: web-data-infrastructure
concept: web-data-infrastructure
title: How Web Data Infrastructure Powers the Next Generation of AI
sources:
  - title: "How Web Data Infrastructure Powers the Next Generation of AI"
    url: "https://www.youtube.com/watch?v=1UmZHb_E_SM"
    author: "AI Engineer"
    date: "2026-08-14T17:00:37+00:00"
---

# How Web Data Infrastructure Powers the Next Generation of AI

The talk, presented by Patricija Žemaitytė of Oxylabs, argues that AI models are shifting from static training data to needing fresh, real-time web data to remain useful. Oxylabs provides infrastructure for extracting public web data at scale, and this capability is becoming critical for powering AI models, agents, and databases. The speaker shares a case study where sales returned with a demand for a video API for AI training, requiring a pipeline for collection, transfer, storage, and delivery at a scale of 5 petabytes per month, with a two-week deadline.

Starting as a simple downloader, the feature evolved through repeated client requests into a full product suite supporting transcripts, subtitles, channel metadata, and search. This iterative process transformed a one-off request into a robust internal library and product family. The key lesson is that innovation is not a neat roadmap but a repeated adaptation under high pressure, and that building for real AI workloads demands infrastructure-level thinking rather than single product features.

- AI models need access to fresh, real-time web data in addition to static training data.
- Building data pipelines for AI training requires infrastructure for collection, transfer, storage, and delivery at massive scale.
- Customer needs evolve rapidly; a simple downloader became a full video API suite with subtitles, transcripts, and metadata within roughly three months.
- Innovation often emerges from high-pressure deadlines and repeated adaptation rather than a planned roadmap.
- Successful AI data infrastructure must support multimodal content and structural context around the raw data.