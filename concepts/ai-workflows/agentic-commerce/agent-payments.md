---
domain: ai-workflows
subdomain: agentic-commerce
concept: agent-payments
title: Teaching Agents to Pay
sources:
  - title: "Teaching agents to pay — Anna Spysz, Stripe"
    url: "https://www.youtube.com/watch?v=A-zeQiYkmXk"
    author: "AI Engineer"
    date: "2026-09-01T16:30:06+00:00"
---

# Teaching Agents to Pay

Anna Spysz's talk illustrates how AI agents change both sides of a commercial transaction. Her opening anecdote shows a shopping agent whose pushy behavior came from a misconfigured persona—an 'aggressive audio gear salesman' system prompt—rather than the underlying tools or protocol. Swapping that persona for a patient mentor changed the conversation completely, demonstrating that agent behavior is heavily shaped by configuration (AI Engineer, 2026).

On the merchant side, Spysz explains that agents cannot browse websites like humans. They require a capabilities manifest declaring supported payment methods and endpoints, plus structured catalogs and policies they can parse without wasting tokens. She also emphasizes logging as evidence: recording which attributes drove a recommendation turns the catalog into an audit trail for decisions. On the payments side, she introduces shared payment tokens, where the agent receives a token rather than a card number, the seller unwraps only what it needs, and the payment provider enforces limits. Finally, she closes with a guardrail checklist: disclose AI involvement, honor stop and cancel requests, and cap any total at the user's ceiling (AI Engineer, 2026).

- Agents need machine-readable manifests, structured catalogs, and policies rather than human-browsable web pages.
- Logging which attributes drove a recommendation turns a catalog into evidence of how agent decisions were made.
- Shared payment tokens let the agent initiate payment without ever handling a card number, while the provider enforces limits.
- Guardrails must include AI disclosure, honoring stop/cancel commands, and respecting user-set spending ceilings.
- A poorly chosen persona/system prompt can drastically change agent behavior even when tools and protocols remain the same.