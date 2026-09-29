---
domain: ai-workflows
subdomain: agentic-payments
concept: machine-payments-protocol
title: AI Agents Can Think. Now They Can Pay.
sources:
  - title: "AI Agents Can Think. Now They Can Pay."
    url: "https://blog.bytebytego.com/p/ai-agents-can-think-now-they-can"
    author: "ByteByteGo"
    date: "Mon, 28 Sep 2026 15:31:11 GMT"
---

# AI Agents Can Think. Now They Can Pay.

The article argues the web’s payment flow still assumes human customers, while automated systems now generate around 57.5% of HTTP requests to web content (ByteByteGo). As AI tools become autonomous agents that plan, act, and evaluate outcomes, Stripe and Tempo’s Machine Payments Protocol (MPP) aims to let agents buy services without account creation, forms, or API-key purchase (ByteByteGo). MPP launched on March 18, 2026; its core spec, Payment HTTP Authentication Schema, was submitted to the IETF standards track (ByteByteGo).

MPP uses HTTP 402 Payment Required. A server returns a WWW-Authenticate: Payment header with a Challenge containing an ID, amount, currency, recipient, payment method, intent, and expiry. The agent checks the terms and authorizes within a delegated signing key’s spending cap, expiry, permitted recipients, and scope. It retries with an Authorization: Payment Credential. The server verifies payment and returns access plus a Payment-Receipt. Servers must not perform side effects for unpaid requests, and proofs are single-use (ByteByteGo).

For micropayments, MPP uses sessions: the agent commits funds, then sends signed IOUs per request; the server verifies signatures and serves immediately, later claiming the total in one real transaction. This spreads one processing fee across thousands of requests, making per-request costs near zero. Use cases include agents paying pennies for searches or API calls and readers buying a single ByteByteGo article via an attached Tempo wallet (ByteByteGo).

Removing signup also removes identity and account history. The seller may only get a public key; payment proves control of the key, not company or end-user identity. Spending limits prevent overspend but not spending correctly on the wrong things; abuse control, disputes, refunds, and repeat-buyer detection must change (ByteByteGo).

- MPP is an open protocol that uses HTTP headers and 402 responses so agents can discover price, authorize payment, and receive service without human signup.
- The core exchange is Challenge, Credential, and Receipt; servers must not execute side effects until paid, and credentials are single-use.
- Delegated spending keys enforce caps, expiry, permitted recipients, and scope to limit runaway agent spending.
- Sessions aggregate many micropayments via signed IOUs settled once, making sub-cent agent payments economically viable.
- Without accounts, payment proves control of a key rather than identity, complicating abuse control, disputes, refunds, and customer history.