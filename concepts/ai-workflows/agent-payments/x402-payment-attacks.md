---
domain: ai-workflows
subdomain: agent-payments
concept: x402-payment-attacks
title: Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments
sources:
  - title: "Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments - Ishween Kaur, SoFi"
    url: "https://www.youtube.com/watch?v=YU1uD_YkpjU"
    author: "AI Engineer"
    date: "2026-10-30"
---

# Your Agent Just Paid for Nothing: 6 Attacks on x402 Payments

Ishween Kaur (SoFi) examines x402, an emerging protocol that fills in the long-dormant HTTP 402 status code by specifying how a machine can actually pay for a resource. The motivation is micropayments: an agent needing a single market-data point should be able to pay a few cents and get it, rather than subscribing to a service it uses once. Because credit-card fees can exceed the value of a one-cent or ten-cent purchase, x402 uses on-chain settlement, and at scale (e.g., 10 cents across 10,000 calls) agent payments become a meaningful budget line that must scale with agent autonomy.

The protocol has four entities: the buyer (acting for a user or organization), the seller (owning the data), the facilitator (verifying and settling), and the blockchain. The seller responds to a request with a 402 carrying payment requirements; the buyer signs the payment; the seller forwards it to the facilitator for verification and settlement, and data is released after verification or settlement. Cloudflare's "payer crawl" experiments are cited as a sign that publishers may soon offer data on pay-per-use terms.

Kaur argues agents should not pay blindly: they should check whether the seller is authorized, whether the amount fits the budget, and whether the data is something they have permission to access. She broke the payment sequence in roughly 20 ways and presents six attacks from both buyer and seller sides. The first is price manipulation: a catalog may list 5 cents while the 402 header demands 50 cents, and in her unprotected run the agent paid the inflated amount. Comparing the listed price against the seller's requested price in code blocked that attack, but not variants that swap the wallet address or the network (Base vs. Ethereum vs. Solana), so each field must be validated.

She also describes replay: a payment number is unique on the network, yet if a buyer resends the same payment number multiple times, the facilitator's verification stage may only compare signatures, deem the requests valid, and release data repeatedly. The talk frames agent payments as a new frontier where software becomes a buyer, and where the agent need not be compromised to lose money.

- x402 gives the HTTP 402 status code a concrete machine-payable flow across buyer, seller, facilitator, and blockchain, motivated by micropayments too small for card fees.
- Agents should validate seller authorization, budget fit, and data permissions before paying rather than paying on request.
- Price manipulation: the 402 header can quote a different amount than the catalog; comparing listed vs. requested price in code blocks it, but wallet and network fields must also be checked.
- Replay attacks: resending the same payment number can pass signature-only verification and release data multiple times.
- Agent payments extend autonomy past human review, so an agent can lose money without being compromised.