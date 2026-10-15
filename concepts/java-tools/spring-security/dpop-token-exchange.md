---
domain: java-tools
subdomain: spring-security
concept: dpop-token-exchange
title: Server-Side DPoP and Token Exchange in Spring Security 7
sources:
  - title: "Article: Server-Side DPoP and Token Exchange in Spring Security 7"
    url: "https://www.infoq.com/articles/spring-security-7-server-side-dpop-token-exchange/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Dhruv Agnihotri"
    date: "2026-10-15"
---

# Server-Side DPoP and Token Exchange in Spring Security 7

Spring Authorization Server has been folded into Spring Security 7 under the same Maven coordinates, so migrating is effectively a version bump rather than a coordinate change. The article is a server-side guide to enabling two advanced OAuth capabilities in that consolidated stack: DPoP (Demonstrating Proof-of-Possession) and RFC 8693 Token Exchange.

A key migration caveat is that applications on 7.1 can silently stop enforcing DPoP unless they explicitly call .dPoP() in their configuration. This means upgrades may appear successful while sender-constraint enforcement is quietly dropped, so the explicit configuration call is required to retain protection.

The guide then shows how to combine DPoP with Token Exchange to produce narrowed, sender-constrained tokens. This pattern is aimed at service-to-service and agentic calls, where a token should be both scoped down and bound to the client that holds the corresponding key.

- Spring Authorization Server now ships inside Spring Security 7 under the same Maven coordinates, making the upgrade a version bump.
- Spring Security 7.1 apps can silently stop enforcing DPoP unless they explicitly call .dPoP().
- The article covers enabling both DPoP and RFC 8693 Token Exchange on the server side.
- Combining the two yields narrowed, sender-constrained tokens suited to service-to-service and agentic calls.