---
domain: ai-workflows
subdomain: agent-authorization
concept: agent-authorization-ladder
title: Your Agent Just Authorized What?!
sources:
  - title: "Your Agent Just Authorized What?! — Jay Mok & Ben Coumes, Paypal"
    url: "https://www.youtube.com/watch?v=vGn6N4-bxBY"
    author: "AI Engineer"
    date: "2026-09-01T18:30:06+00:00"
---

# Your Agent Just Authorized What?!

The talk argues that agent authorization ultimately reduces to three questions: Did the human authorize this? Is it allowed right now, in this scope? And can we prove it later? The answers depend on the stakes involved and whether the agent and the counterparty have ever met (Mok & Coumes, 2026).

- PayPal's approval token inverts the traditional flow: the user approves before the agent selects an item or merchant, and the token carries amount, expiry, and permitted merchant.
- Authorization design falls into a ladder based on stakes: low-stakes coding agents use tool-level allow/ask/deny; medium-stakes payments between known parties use OAuth scopes and mandates; high-stakes autonomous transactions with unknown counterparties are not yet production-ready.
- For high-stakes unknown-counterparty scenarios, the proposal is a layered selective disclosure JWT, letting a merchant verify checkout and a processor verify payment without either seeing the other's data.
- Ordinary logs are sufficient for low-stakes actions because they can be reverted, but higher stakes demand stronger proof mechanisms like transaction logs or cryptographic tokens.