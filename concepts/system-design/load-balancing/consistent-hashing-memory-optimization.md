---
domain: system-design
subdomain: load-balancing
concept: consistent-hashing-memory-optimization
title: Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing
sources:
  - title: "Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing"
    url: "https://www.infoq.com/news/2026/10/cloudflare-hashing-optimization/"
    author: "Renato Losio"
    date: "2026-10-24"
---

# Cloudflare Reclaims 100 TB of RAM by Optimizing Consistent Hashing

Cloudflare documented how it cut the memory footprint of its internal load-balancing service by more than 100 TB by optimizing the Rust implementation of consistent hashing in pingora-ketama. The work compacted hash-ring entries and applied statistical analysis of hash distribution and collision rates to reduce the number of hashes per backend by roughly 90%.

The optimization targets the memory cost inherent in consistent hashing, where each backend is represented by many entries on a hash ring. By shrinking the per-entry representation and using distribution and collision analysis to justify fewer hashes per backend, Cloudflare achieved a large aggregate memory reduction across its fleet.

The result illustrates how data-structure-level tuning in a core routing component can yield infrastructure-scale savings, and how statistical reasoning about hash behavior can guide capacity decisions rather than relying on fixed over-provisioning.

- Optimizing consistent hashing in pingora-ketama reclaimed over 100 TB of RAM for Cloudflare's internal load balancer
- Hash-ring entries were compacted to reduce per-entry memory cost
- Statistical analysis of hash distribution and collision rates justified ~90% fewer hashes per backend
- Small data-structure changes in core routing components can produce fleet-scale resource savings