---
domain: system-design
subdomain: network-security
concept: private-origins
title: Cloudflare Private Origins for Application Services
sources:
  - title: "Cloudflare Introduces Private Origins for Application Services"
    url: "https://www.infoq.com/news/2026/11/cloudflare-private-origins/"
    author: "Renato Losio"
    date: "2026-11-15"
---

# Cloudflare Private Origins for Application Services

Cloudflare has made Application Services for Private Origins generally available, enabling public traffic to reach applications hosted on private networks without exposing their IP addresses or opening inbound firewall ports [InfoQ]. This lets teams serve publicly reachable applications while keeping origin infrastructure hidden from the public internet.

The capability is limited in scope: private-to-private connectivity is not yet supported, so the feature currently addresses public-to-private traffic flows only [InfoQ].

- Public traffic can reach private-network applications without exposing origin IPs
- No inbound firewall ports need to be opened
- Private-to-private connectivity is not yet supported