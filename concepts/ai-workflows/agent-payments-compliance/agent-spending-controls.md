---
domain: ai-workflows
subdomain: agent-payments-compliance
concept: agent-spending-controls
title: Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node
sources:
  - title: "Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node"
    url: "https://www.youtube.com/watch?v=ZyGMqdIpPoE"
    author: "AI Engineer"
    date: "2026-09-01T19:30:09+00:00"
---

# Agent Spending Without Controls — Rodrigo Coelho & Pranav Maheshwari, Edge & Node

The closing demo makes the compliance problem concrete. Two agents hit a metered scraping service, one from an ordinary wallet and one from a wallet flagged as sanctioned. With screening off, both transactions authorize; switching screening on leaves the first working and rejects the second as a blocklisted address. This illustrates that sanctions screening can be layered onto agent payments, addressing the legal officer's concern about billion-dollar fines (Coelho & Maheshwari, 18:04).

- Agents need the ability to pay for metered tools to access the most useful data; free MCP servers are not a sustainable baseline.
- The Graph shipped a query micropayment system in 2021 citing HTTP 402, predating Coinbase's x402.
- Enterprise adoption of agent payments is gated by compliance, not throughput: agents transact at machine speed with anonymous wallet addresses.
- Sanctions screening can be enforced in real time, blocking transactions from blocklisted wallets while allowing normal ones.
- Without payment and compliance controls, an agent's capability is limited to free or basic information.