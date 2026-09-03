---
domain: ai-workflows
subdomain: corporate-ai-security
concept: corporate-intelligence-leak-prevention
title: Your Company Brain Will Leak Secrets: How We Stopped It for Big Banks — Tanmai Gopal, PromptQL
sources:
  - title: "Your company brain will leak secrets: how we stopped it for big banks — Tanmai Gopal, PromptQL"
    url: "https://www.youtube.com/watch?v=0uC6u0lJJl4"
    author: "AI Engineer"
    date: "2026-09-03"
---

# Your Company Brain Will Leak Secrets: How We Stopped It for Big Banks — Tanmai Gopal, PromptQL

Tanmai Gopal, CEO and co-founder of PromptQL, explains that building corporate intelligence is likely to leak company secrets—the same risk as giving an intern access to all corporate data (Gopal, 2026). This fear is the biggest obstacle preventing organizations from deploying AI agents like Open Claw or Hermes across the enterprise. He shares lessons from PromptQL's year working with 15–20 select customers, ranging from AI-focused companies and fast-moving firms like Instacart to Fortune 100 banks with extremely stringent, "cosmic" security requirements (Gopal, 2026).

PromptQL, which comes from the Hasura GraphQL engine background, models its own company brain as about 5,000 interconnected wiki pages, though the approach can be adapted to markdown files, knowledge graphs, or other structures (Gopal, 2026). Gopal discusses a key health metric: the daily number of brain updates. A declining curve indicates early enthusiasm followed by neglect; a fluctuating curve suggests reactive, bursty usage; but a healthy, continuously learning corporate brain shows a steadily growing number of updates (Gopal, 2026). He reveals that PromptQL's own data over the past two months follows a smooth upward curve, which he found exciting because it demonstrates that the brain is genuinely being used and expanded every day (Gopal, 2026). The talk focuses on how the company built this system securely, particularly for security-conscious clients like banks, and on the hard-won patterns that make corporate AI trustworthy enough for production.

- Corporate intelligence systems that access company-wide data create the same leak risk as giving an intern access to everything, which is the main obstacle to rolling out AI agents.
- Different customers have vastly different security postures, from AI-native firms that act fast and iterate to Fortune 100 banks with exceptionally strict safety rules.
- PromptQL models its company brain as 5,000 interconnected wiki pages, illustrating the scope of an enterprise-wide knowledge system.
- A healthy corporate brain shows a steadily upward trend in daily updates, not a decline or bursty spikes, indicating continuous learning and adoption.
- Because the talk targets high-security environments like banks, the design emphasizes rigorously controlled data access to prevent secrets from leaking.