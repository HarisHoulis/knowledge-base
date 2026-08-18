---
domain: ai-workflows
subdomain: context-engineering
concept: context-compaction-trap
title: Context Engineering in 2026
sources:
  - title: "Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI"
    url: "https://www.youtube.com/watch?v=WP3hjUXd918"
    author: "AI Engineer"
    date: "2026-08-17T16:26:35+00:00"
---

# Context Engineering in 2026

The cheapest configuration tested was the one sending the most tokens. Across 11 presets run against their open source AI tutor, doing nothing at all to the context beat every compaction technique on recall, cost, and latency at once, and their own production defaults scored worse than leaving the history alone. Prompt caching is why. With 97% of tokens served from cache, and cached tokens up to 50 times cheaper on some APIs, compaction has to shrink a context by more than 50 times before it pays for itself, because rewriting the context invalidates the cache. Louis-François Bouchard's framing is that summarization is potentially a trap.

- Leaving context unmodified outperformed all 11 compaction presets on recall, cost, and latency due to prompt caching.
- Compaction must reduce context by over 50x to overcome cache invalidation costs, given cached tokens are up to 50x cheaper.
- Summarization recovered specific details 95% of the time vs 32% after summarizing, and facts remained intact up to 800k tokens.
- With a local 32k window, compaction becomes necessary; dense retrieval failed at 400k tokens where BM25 still succeeded.
- Name the actual constraint (cache economics, window size, retrieval) before choosing to compact, rather than compacting by default.