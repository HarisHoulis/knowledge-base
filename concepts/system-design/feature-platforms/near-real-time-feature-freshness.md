---
domain: system-design
subdomain: feature-platforms
concept: near-real-time-feature-freshness
title: Airbnb Cuts Recommendation Staleness from 2 Days to Seconds with Chronon
sources:
  - title: "Airbnb Cuts Recommendation Staleness from 2 Days to Seconds with Chronon"
    url: "https://www.infoq.com/news/2026/10/airbnb-chronon-recommendation/"
    author: "Leela Kumili"
    date: "2026-10-28"
---

# Airbnb Cuts Recommendation Staleness from 2 Days to Seconds with Chronon

Airbnb extended its Chronon feature platform with two capabilities, Push Mode and Near Real-Time Model Transform, to update sequence-based recommendation embeddings within seconds rather than days. The architecture reduced embedding staleness from nearly two days to under a minute [InfoQ].

The impact was measured both offline and online: offline NDCG improved by 1.67%, and online testing increased uncancelled bookings by roughly one-third of a percent [InfoQ]. The work illustrates how feature freshness in a feature platform can translate directly into measurable business outcomes for recommendation systems.

- Push Mode and Near Real-Time Model Transform extend the Chronon feature platform for fast embedding updates
- Embedding staleness dropped from nearly two days to under a minute
- Offline NDCG improved 1.67% and online uncancelled bookings rose about 0.33%