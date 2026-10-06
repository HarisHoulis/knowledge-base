---
domain: system-design
subdomain: multi-tenant-security
concept: cross-tenant-data-exposure
title: Cloudflare Fixes Cross-Tenant Data Exposure in Containers
sources:
  - title: "Cloudflare Fixes Cross-Tenant Data Exposure in Containers"
    url: "https://www.infoq.com/news/2026/10/cloudflare-cross-tenant-exposure/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Steef-Jan Wiggers"
    date: "Mon, 05 Oct 2026 08:48:00 GMT"
---

# Cloudflare Fixes Cross-Tenant Data Exposure in Containers

Cloudflare disclosed a cross-tenant data exposure vulnerability affecting its Containers and Sandboxes offerings. The issue stemmed from thin-provisioned storage pools that were configured to skip zeroing reused blocks, leaving prior tenant data accessible [InfoQ, 2026].

Researchers were able to recover directory structures, database pages, and complete SQLite databases across four continents, demonstrating the cross-tenant impact [InfoQ, 2026].

Cloudflare remediated the vulnerability and stated it found no evidence that the exposure was exploited [InfoQ, 2026].

- Vulnerability caused by thin-provisioned storage pools configured to skip zeroing reused blocks.
- Researchers recovered directory structures, database pages, and complete SQLite databases across four continents.
- Cloudflare remediated the issue and found no evidence of exploitation.