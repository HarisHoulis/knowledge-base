---
domain: system-design
subdomain: pki-and-certificates
concept: intermediate-ca-compromise
title: eMudhra Intermediate CA Compromise
sources:
  - title: "eMudhra Intermediate CA Compromise"
    url: "https://www.infoq.com/news/2026/10/emudhra-ca-compromise/"
    author: "Chris Swan"
    date: "2026-10-21"
---

# eMudhra Intermediate CA Compromise

Private keys for eight eMudhra intermediate CA certificates were compromised, enabling attackers to forge certificates for any site. The compromise stemmed from low entropy in key generation rather than a known breach, meaning the keys were effectively guessable.

Browsers mitigated the issue by blocking the affected certificates via revocation lists, but other software had to remove the emSign ECC G3 root entirely. Systems that remain unpatched are still exposed to forged certificates, including for client authentication and mTLS.

The incident highlights the fragility of trust chains: a weakness at the intermediate CA level undermines the entire hierarchy beneath it, and revocation only helps clients that actually check it.

- Eight eMudhra intermediate CA private keys were compromised, allowing forgery of certificates for any site
- The root cause was low entropy in key generation, not a known breach
- Browsers blocked the certificates via revocation lists; other software had to remove the emSign ECC G3 root
- Unpatched systems remain vulnerable to forged certificates, including client auth and mTLS