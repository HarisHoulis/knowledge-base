---
domain: ai-workflows
subdomain: browser-agents
concept: browser-agents-for-financial-data
title: Building Financial Agents That Work Across the Web
sources:
  - title: "How to Build Financial Agents That Work Across the Web - Jay Sahnan & Arik Bird, Browserbase"
    url: "https://www.youtube.com/watch?v=DZ24Xbm9Joc"
    author: "AI Engineer"
    date: "2026-10-25"
---

# Building Financial Agents That Work Across the Web

Jay Sahnan and Arik Bird of Browserbase explain that a browser agent is a tool an agent uses to access websites, read information, and perform actions on the web—especially on complex sites that lack an API or MCP. They argue that for any action on the internet, an agent needs a browser-like tool, citing examples like booking a plane ticket or gathering competitor pricing.

The talk centers on financial institutions such as Ramp, Bill, and Stripe, which handle highly sensitive data that often lives behind login portals or on sites heavily protected from bots. Ramp's receipt-capture workflow is the running example: after a card transaction, a browser agent logs into the merchant site (e.g., Delta), captures the receipt, and matches it to the transaction. Manually staffing a team to fetch receipts from portals does not scale as a company grows, which is where browser agents come in.

The core technical challenge is that a laptop browser carries a rich digital footprint—browser version, OS, fonts, screen size, time zone, cookies, login state, behavioral patterns, and network reputation—that signals a familiar human visitor. Moving Chromium to a data center breaks this: each run may have a different fingerprint, fresh cookies, forced re-logins, and a data-center IP. Proxies can reduce captchas or fake location, but the speakers argue they do not solve Chromium's underlying problems, so companies need scalable infrastructure that lets agents visit websites reliably.

- A browser agent lets an agent access, read, and act on websites that lack APIs or MCP, making it essential for complex web actions.
- Financial institutions like Ramp, Bill, and Stripe hold sensitive data behind login portals and bot-protected sites, a natural fit for browser agents.
- Ramp uses browser agents to log into merchant sites, capture receipts, and match them to card transactions at scale.
- Scaling from a laptop to a data center breaks browser fingerprints, cookies, login state, and IP reputation, triggering anti-bot friction.
- Proxies can reduce captchas or mask location but do not fix Chromium's underlying data-center problems; reliable infrastructure is required.