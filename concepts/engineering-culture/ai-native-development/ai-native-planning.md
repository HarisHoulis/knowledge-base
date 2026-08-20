---
domain: engineering-culture
subdomain: ai-native-development
concept: ai-native-planning
title: How to build an AI-Native Health Company — Dan Feng, Maven Clinic
sources:
  - title: "How to build an AI-Native Health Company — Dan Feng, Maven Clinic"
    url: "https://www.youtube.com/watch?v=WJRdLNhrsLQ"
    author: "AI Engineer"
    date: "2026-08-19T17:30:19+00:00"
---

# How to build an AI-Native Health Company — Dan Feng, Maven Clinic

Dan Feng, an AI engineer at Maven Clinic, argues that the cost of implementation has fundamentally shifted. Building software now takes minutes, but debating requirements is the expensive part. As a result, Maven's planning process now treats a one-year view only as direction, while real commitments are made for two-to-four-week sprints. Three-to-six-month plans are considered nearly unplannable, as no one can predict AI model capabilities that far in advance. This has replaced lengthy requirement documents with one-to-two-page briefs meant to be challenged (source: https://www.youtube.com/watch?v=WJRdLNhrsLQ).

- Implementation is now cheap, so planning shifts to short sprints and a directional annual vision, eliminating 3-6 month plans as impractical.
- Code review must adapt to tenfold volume via self-certification, capped pull-request size around 500 lines, and stacked changes, while avoiding rubber-stamp reviews.
- Reliability expectations must be differentiated: acceptable for low-stakes actions, but zero tolerance for high-stakes ones like reimbursement claims, where multiple models must agree.
- Integration tests should run many times because passing a nondeterministic system on one attempt proves little.