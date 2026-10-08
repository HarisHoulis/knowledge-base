---
domain: ai-workflows
subdomain: ai-economics
concept: usage-based-billing-infrastructure
title: Every AI Company Is Accidentally Building a Bank
sources:
  - title: "Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg"
    url: "https://www.youtube.com/watch?v=cf2IhzqeQH4"
    author: "AI Engineer"
    date: "2026-10-07T00:30:28+00:00"
---

# Every AI Company Is Accidentally Building a Bank

Dor Sasson, co-founder and CEO of Stigg, argues that AI companies are unintentionally building banking-like financial infrastructure because their products behave like financial systems. He points to a wave of pricing crises in April: Anthropic restricted third-party agents like OpenClaude from using subscription plans, OpenAI raised prices fivefold overnight, and GitHub froze and then canceled free Copilot trials. Sasson frames these not as isolated commercial missteps but as infrastructure crises stemming from how the systems were built.

The core failure, according to Sasson, is that entitlement checks happen after billing rather than before. Anthropic subsidized every OpenClaude consumption under Claude Pro, with customers paying dollars while costs ran from $150 to $750 per user, an economy that cannot scale even for a company of Anthropic's size. Because Anthropic could not differentiate between API users and subscription users, it had to shut off access reactively. Sasson generalizes this pattern: one unnamed company burned half a billion in cloud AI credits through a few employees, Uber reportedly exhausted its annual AI budget in weeks, and Replit saw three users consume an entire company credit pool.

Sasson's diagnosis is that in each case users were allowed to consume and spend tokens, with checks made only after the invoice was issued, so costs and consequences are reconciled too late. He contrasts this with banks, which verify funds before withdrawal. AI changes not only the concept of value and who the users are, but also what exactly is being paid for, requiring systems designed to handle the turnaround from usage to billing to audits.

- AI companies face pricing crises because entitlement checks occur after billing rather than before consumption.
- Anthropic subsidized OpenClaude usage at $150–$750 per user while customers paid only dollars and cents under Claude Pro.
- Similar blowups occurred at an unnamed company (half a billion in credits), Uber (annual budget in weeks), and Replit (three users exhausting the company pool).
- Sasson argues these are infrastructure crises, not merely commercial or financial problems, rooted in how systems were built.
- AI changes what is paid for and requires billing architectures that handle usage-to-billing-to-audit turnaround.