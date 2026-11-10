---
domain: system-design
subdomain: post-quantum-security
concept: merkle-tree-certificates
title: Cloudflare Develops Public Certificate Authority for Post-Quantum Web Security
sources:
  - title: "Cloudflare Develops Public Certificate Authority for Post-Quantum Web Security"
    url: "https://www.infoq.com/news/2026/11/cloudflare-merkle-certificates/"
    author: "Leela Kumili"
    date: "2026-11-09"
---

# Cloudflare Develops Public Certificate Authority for Post-Quantum Web Security

Cloudflare is building a public certificate authority for Merkle Tree Certificates (MTCs), aiming to cut the bandwidth overhead that post-quantum cryptography introduces into the web's certificate ecosystem. MTCs are positioned as a more efficient certificate format for the post-quantum transition.

A Chrome experiment validated the approach at scale: Cloudflare served billions of MTCs to 50% of Chrome Beta 146 for selected domains, and reported 9% faster median performance compared with the baseline. That result suggests the efficiency gains are real in production-like conditions, not just theoretical.

Broader deployment remains gated on several factors: browser support, transparency requirements, and further production-scale validation. The work is therefore an early but concrete step toward making post-quantum web security practical rather than merely available.

- Cloudflare is developing a public certificate authority for Merkle Tree Certificates to reduce post-quantum cryptography's bandwidth overhead.
- A Chrome experiment served billions of MTCs to 50% of Chrome Beta 146 for selected domains, with 9% faster median performance.
- Wider rollout depends on browser support, transparency, and production-scale validation.