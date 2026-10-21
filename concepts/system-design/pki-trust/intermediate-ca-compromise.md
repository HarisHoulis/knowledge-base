---
domain: system-design
subdomain: pki-trust
concept: intermediate-ca-compromise
title: eMudhra Intermediate CA Compromise
sources:
  - title: "eMudhra Intermediate CA Compromise"
    url: "https://simonwillison.net/2026/Oct/20/emudhra-certificates/"
    date: "2026-10-20"
---

# eMudhra Intermediate CA Compromise

The private keys of eight eMudhra intermediate CA certificates were compromised. These intermediates chain to roots trusted by the Mozilla, Microsoft, Apple, and Chrome root programs, as well as many downstream trust stores, meaning the compromise affects a broad swath of the public key infrastructure.

Because trust is distributed via bundled certificate lists, any software shipping a trusted-certificate store must be updated. The source points to a tracking site and GitHub repository for software updates, noting that Linux distributions need to refresh their `ca-certificates` packages.

In the Python ecosystem, uv 0.13.4, pip 26.2.2, and certifi 2026.10.19 have been released with upgraded certificate lists.

- Eight eMudhra intermediate CA private keys were compromised, chaining to roots trusted by major root programs.
- Any software bundling a trusted certificate list needs updating, including Linux `ca-certificates` packages.
- Python tooling (uv 0.13.4, pip 26.2.2, certifi 2026.10.19) shipped updated certificate lists.