---
domain: ai-workflows
subdomain: agent-payments
concept: x402-limitations
title: x402 Isn't Good (Yet): A Critique of HTTP 402 for Agentic Payments
sources:
  - title: "x402 isn’t good (yet) — Jan Curn, Apify"
    url: "https://www.youtube.com/watch?v=h6mi88VrPtQ"
    author: "AI Engineer"
    date: "2026-09-01T19:00:09+00:00"
---

# x402 Isn't Good (Yet): A Critique of HTTP 402 for Agentic Payments

Jan Curn, founder of Apify, delivers a critical assessment of x402, a protocol that uses HTTP 402 for agentic payments. Despite being bullish enough to ship x402 on Apify's marketplace two days before the talk—expanding the catalog from 2,000 to 20,000 tools—Curn identifies fundamental gaps. The core issue is a double-spending window: between the moment a server verifies a payment signature and the moment the transaction settles on the blockchain, nothing prevents the buyer from spending the same funds elsewhere. This makes it unsafe for sellers to start work based solely on verification, strictly limiting x402 to fast, fixed-price API calls (Curn, 9:19).

Protocol conflicts compound the problem. x402 expects HTTP 402 as the server's first response, while MCP expects 401, and since a single response cannot satisfy both, companies stand up a second hostname purely for payments—an antipattern Curn likens to having a separate Amazon for every credit card (Curn, 11:10). Pricing models are also flawed: the original 'exact' scheme charges a fixed fee per call, which fails for tools that run for seconds or hours, while the 'up to' scheme meant to enable metered billing leaves the double-spending window open. Apify's workaround is to charge in full and refund the remainder, costing a second chain transaction and creating a trust assumption pointing the wrong way. Curn is watching batch settlement and has shipped a markdown page that an agent reads to buy a prepaid token, deliberately not an API (Curn, 13:55).

- x402 has a double-spending window between payment verification and blockchain settlement, making it risky to start work on the strength of verification alone.
- HTTP 402 conflicts with MCP's 401 requirement, forcing separate payment hostnames—an antipattern that fragments services.
- The 'exact' fixed-fee pricing model doesn't fit tools with variable execution times; the 'up to' variant reintroduces double-spending risk.
- Apify ships x402 by charging in full and refunding the remainder, which adds a second on-chain transaction and a trust assumption.
- Curn remains optimistic about x402, having increased Apify's marketplace catalog tenfold, and is exploring batch settlement for future improvements.