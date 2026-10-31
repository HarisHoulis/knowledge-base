---
domain: system-design
subdomain: cryptography
concept: post-quantum-geo-fenced-keys
title: Cloudflare's Post-Quantum GeoKey Manager Enters Closed Beta Without Attribute-Based Encryption
sources:
  - title: "Cloudflare's Post-Quantum GeoKey Manager Enters Closed Beta Without Attribute-Based Encryption"
    url: "https://www.infoq.com/news/2026/10/cf-pq-geokey-manager/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-31"
---

# Cloudflare's Post-Quantum GeoKey Manager Enters Closed Beta Without Attribute-Based Encryption

Cloudflare has moved a post-quantum rebuild of its GeoKey Manager into closed beta, replacing the attribute-based encryption it has used since 2022 with hybrid ML-KEM-768 and X25519 to protect geo-fenced keys. The design keeps keys only in kernel memory on verified regional servers, so they never persist outside the constrained region.

The system is fail-closed: any failed verification check rejects the request outright. Practitioners have raised the concern that this strictness could turn a regional verification failure into a regional outage, since there is no fallback path. Cloudflare plans general availability for Q1 2027.

- GeoKey Manager's post-quantum rebuild uses hybrid ML-KEM-768 and X25519 instead of attribute-based encryption.
- Keys reside only in kernel memory on verified regional servers.
- The design is fail-closed, which critics note could cause a regional outage on verification failure.
- Closed beta is underway, with GA planned for Q1 2027.