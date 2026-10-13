---
domain: system-design
subdomain: privacy-preserving-networking
concept: oblivious-http-gateway
title: Cloudflare's OHTTP Gateway Refuses to Decrypt Requests That Arrive Through Cloudflare
sources:
  - title: "Cloudflare's OHTTP Gateway Refuses to Decrypt Requests That Arrive Through Cloudflare"
    url: "https://www.infoq.com/news/2026/10/cloudflare-ohttp-gateway/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-13"
---

# Cloudflare's OHTTP Gateway Refuses to Decrypt Requests That Arrive Through Cloudflare

Cloudflare has opened a closed beta of its OHTTP Gateway, a managed endpoint that decrypts Oblivious HTTP (OHTTP) requests on behalf of an origin. OHTTP is designed to separate the identity of a client from the contents of its request, so that no single party sees both. The notable design decision is a deliberate refusal: the Gateway will not decrypt requests that arrive from Cloudflare Workers or from hosts proxied through Cloudflare, because doing so would place client identifiers and request contents in the same hands, defeating the privacy guarantee OHTTP is meant to provide.

By declining to serve requests that traverse its own network, Cloudflare enforces a separation-of-trust boundary at the infrastructure level rather than relying on policy alone. The Gateway acts as a managed relay that decrypts OHTTP requests for an origin, but only when the request path does not already expose the client's identity to Cloudflare. This makes the trust model explicit: the party that can see who is asking must not be the party that can see what is being asked.

The closed beta positions the Gateway as a turnkey way for origins to adopt OHTTP without operating their own decryption endpoint, while the self-imposed restriction signals that the privacy property is treated as non-negotiable rather than a configuration option.

- Cloudflare's OHTTP Gateway is a managed endpoint that decrypts Oblivious HTTP requests for an origin, now in closed beta.
- It refuses to decrypt requests arriving from Cloudflare Workers or hosts proxied through Cloudflare.
- The refusal exists because combining client identifiers and request contents in one party would defeat OHTTP's privacy purpose.
- The design enforces a separation-of-trust boundary at the infrastructure level rather than through policy alone.