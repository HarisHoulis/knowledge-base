---
domain: system-design
subdomain: cloud-ingress
concept: ecs-gateway
title: Amazon ECS Gateway Arrives with Generated Hostnames and No Custom Domain Support
sources:
  - title: "Amazon ECS Gateway Arrives with Generated Hostnames and No Custom Domain Support"
    url: "https://www.infoq.com/news/2026/11/introducing-amazon-ecs-gateway/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-04"
---

# Amazon ECS Gateway Arrives with Generated Hostnames and No Custom Domain Support

AWS released Amazon ECS Gateway, an account-level ingress resource that lets platform teams define networking once while application teams opt services in via a connector (InfoQ, Steef-Jan Wiggers). Each service receives a generated hostname, and routing is host-based.

The announcement and documentation do not cover custom domain support, leaving that gap unaddressed in the source material.

- ECS Gateway is an account-level ingress resource, separating platform-defined networking from per-service opt-in.
- Application teams connect services through a connector rather than configuring ingress themselves.
- Routing is host-based, with each service getting a generated hostname.
- No custom domain support is documented or mentioned in the announcement.