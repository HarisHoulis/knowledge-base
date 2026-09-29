---
domain: system-design
subdomain: distributed-caching
concept: memory-efficient-dns-cache
title: Cloudflare Cuts 100 TB of Memory from 1.1.1.1 DNS Cache
sources:
  - title: "Cloudflare Cuts 100 TB of Memory from 1.1.1.1 DNS Cache"
    url: "https://www.infoq.com/news/2026/09/cloudflare-dns-cache/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "Wed, 23 Sep 2026 13:22:00 GMT"
---

# Cloudflare Cuts 100 TB of Memory from 1.1.1.1 DNS Cache

Cloudflare redesigned the in-memory representation of its Big Pineapple DNS cache used for 1.1.1.1, cutting the per-entry footprint by 56% and freeing roughly 100 TB of working-set memory across its fleet (Kumili, 2026). The company reported the Rust-based changes also improved cache insertion throughput by 43% and reduced lookup latency by 19% (Kumili, 2026).

The redesign lets Cloudflare increase cache capacity without additional memory, making the DNS resolver more efficient at fleet scale (Kumili, 2026).

- Cloudflare reduced the per-entry memory footprint of its Big Pineapple DNS cache by 56%.
- The change freed roughly 100 TB of working-set memory across Cloudflare's fleet.
- Rust-based improvements increased cache insertion throughput by 43% and reduced lookup latency by 19%.
- Cloudflare can now increase cache capacity without adding memory.