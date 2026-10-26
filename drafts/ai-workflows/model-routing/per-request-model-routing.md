---
domain: ai-workflows
subdomain: model-routing
concept: per-request-model-routing
title: Cloudflare Auto Router: Per-Request Model Selection via Complexity Scoring
sources:
  - title: "Cloudflare's Auto Router Rates Each Request for Stakes, from the Most Recent Turns"
    url: "https://www.infoq.com/news/2026/10/cloudflare-auto-router/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-26"
---

# Cloudflare Auto Router: Per-Request Model Selection via Complexity Scoring

Cloudflare released Auto Router in public beta through its AI Gateway, which selects a model for each request using a classifier that scores complexity, ambiguity, stakes, and context dependence (Wiggers, InfoQ, 2026-10-26). Rather than fixing a model per workload, the router makes a per-request decision about which model to invoke.

Cloudflare's own benchmark reports Auto Router landing ten points below Claude Opus 5.5 on success rate while costing roughly a third as much, framing the tradeoff as a deliberate cost-versus-quality position. The stakes dimension is notable because it implies the router weighs how consequential a request is, not just how hard it is.

Practitioners have raised a specific concern: how the stakes assessment holds up across a long agent session, where the most recent turns may not reflect the overall risk of the task. The article surfaces this as an open question rather than a resolved one.

- Auto Router is a public beta feature in Cloudflare AI Gateway that picks a model per request rather than per workload.
- The classifier scores four dimensions: complexity, ambiguity, stakes, and context dependence.
- Cloudflare's benchmark shows ~10 points lower success rate than Claude Opus 5.5 at about one-third the cost.
- Practitioners question whether the stakes signal remains reliable over long agent sessions.