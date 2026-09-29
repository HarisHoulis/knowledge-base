---
domain: system-design
subdomain: edge networking / TLS optimization
concept: per-origin-tls-measurement
title: Cloudflare Measures Origin TLS Preferences, Cutting Handshake Retries from 52% to 3.7%
sources:
  - title: "Cloudflare Measures Origin TLS Preferences, Cutting Handshake Retries from 52% to 3.7%"
    url: "https://www.infoq.com/news/2026/09/cloudflare-automatic-key-exchang/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Steef-Jan Wiggers"
    date: "2026-09-20"
---

# Cloudflare Measures Origin TLS Preferences, Cutting Handshake Retries from 52% to 3.7%

Cloudflare replaced its static X25519 guess for origin TLS handshakes with per-origin measurement ([InfoQ](https://www.infoq.com/news/2026/09/cloudflare-automatic-key-exchang/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design)). HelloRetryRequests on scanned origins dropped from roughly 52% to 3.7%, removing more than 150 ms from p90 latency ([InfoQ](https://www.infoq.com/news/2026/09/cloudflare-automatic-key-exchang/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design)).

The change also improved post-quantum connections completing in a single round trip, which rose from 0% to 99.2% ([InfoQ](https://www.infoq.com/news/2026/09/cloudflare-automatic-key-exchang/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design)). However, only 12.8% of origins support post-quantum TLS ([InfoQ](https://www.infoq.com/news/2026/09/cloudflare-automatic-key-exchang/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design)).

- Static X25519 key-exchange guesses caused frequent HelloRetryRequests in origin TLS handshakes.
- Per-origin measurement reduced HelloRetryRequests from ~52% to 3.7% on scanned origins.
- The optimization removed over 150 ms from p90 latency.
- Post-quantum one-round-trip success rose from 0% to 99.2%, but only 12.8% of origins support it.