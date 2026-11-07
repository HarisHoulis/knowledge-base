---
domain: system-design
subdomain: identity-access-management
concept: identity-as-architecture
title: Identity as an Architectural Concern: Enterprise IAM Beyond Authentication
sources:
  - title: "Identity as an Architectural Concern: Enterprise IAM Beyond Authentication"
    url: "https://www.infoq.com/articles/identity-as-architecture/"
    author: "Vaishnavi Khosla"
    date: "2026-11-06"
---

# Identity as an Architectural Concern: Enterprise IAM Beyond Authentication

Khosla argues that enterprise identity and access management (IAM) is fundamentally an architectural problem rather than an afterthought bolted onto authentication. How identities are designed directly shapes data models, service boundaries, and revocation policies, so identity decisions must be made early and treated as first-class design concerns (InfoQ article).

The article draws on the author's experience in service account governance to explore concrete trade-offs. It contrasts graph-based identity models with role-based access control (RBAC), discusses the challenges of integrating a vault you don't own, and addresses how to bound revocation latency for an event stream. These examples illustrate that identity choices ripple across the whole system rather than living in a single auth service.

The core takeaway is that teams should treat identity modeling, credential ownership, and revocation timing as architectural decisions with downstream consequences for data, service scope, and security posture.

- Identity design drives data models, service scope, and revocation policies, making IAM an architectural concern, not an afterthought.
- Graph-based identity models and RBAC represent distinct trade-offs for enterprise access control.
- Integrating a vault you don't own introduces ownership and governance challenges.
- Revocation latency must be explicitly bounded when identities interact with event streams.