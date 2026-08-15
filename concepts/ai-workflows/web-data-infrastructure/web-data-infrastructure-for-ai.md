---
domain: ai-workflows
subdomain: web-data-infrastructure
concept: web-data-infrastructure-for-ai
title: How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs
sources:
  - title: "How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs"
    url: "https://www.youtube.com/watch?v=1UmZHb_E_SM"
    author: "AI Engineer"
    date: "2026-08-14T17:00:37+00:00"
---

# How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs

Patricija Žemaitytė from Oxylabs argues that the AI industry is shifting from static knowledge and training toward models that require fresh, real-time external data. Training alone is no longer sufficient; models need access to live search and real external data through an infrastructure layer that collects, transfers, stores, and delivers web data at scale. Oxylabs, established in 2015, builds this infrastructure, enabling companies to extract public web data for AI workloads (Žemaitytė, 2026).

Žemaitytė illustrates this with a case study: a client requested a video API for AI training, with a two-week deadline and a scale of at least 5 petabytes per month. The team had to build a dedicated scraper, new storage integrations, and a delivery flow from scratch. After delivering, the client asked for transcript support, but testing revealed the client actually needed subtitles. This pattern of iterative feedback and re-adaptation repeated as the client requested language search and metadata, eventually transforming a one-off feature into a full product suite—downloaders, transcripts, subtitles, metadata, and channel information—within three months (Žemaitytė, 2026).

The talk underscores that innovation rarely emerges from neat roadmaps; instead, it comes as pressure, deadlines, and unexpected client demands. The key lesson is that innovation is repeated adaptation under high pressure, and infrastructure capabilities must evolve quickly to meet the growing multimodal needs of AI pipelines (Žemaitytė, 2026).

- AI models increasingly depend on fresh, real-time web data, not just static training; infrastructure for collection, transfer, storage, and delivery is critical.
- A client request for a video API for AI training required building a brand-new scraper, storage, and delivery pipeline in just two weeks at 5 PB/month scale.
- Iterative client feedback revealed a mismatch: the client said transcripts but actually needed subtitles, driving adaptive development.
- What started as a single feature evolved into a full video API suite—including transcripts, subtitles, metadata, and channel info—within three months.
- Innovation often arises from high-pressure, deadline-driven adaptation rather than structured planning.