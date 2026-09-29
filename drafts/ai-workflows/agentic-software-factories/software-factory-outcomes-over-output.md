---
domain: ai-workflows
subdomain: agentic-software-factories
concept: software-factory-outcomes-over-output
title: No, That's Not a Software Factory — Ryan Cooke, WorkOS
sources:
  - title: "No, That's Not a Software Factory — Ryan Cooke, WorkOS"
    url: "https://www.youtube.com/watch?v=HvboD89DyQ8"
    author: "Ryan Cooke (AI Engineer)"
    date: "2026-09-27"
---

# No, That's Not a Software Factory — Ryan Cooke, WorkOS

Ryan Cooke of WorkOS opens by noting that "software factories" are now a familiar industry concept, tracing the excitement to Ramp's writing about "inspections" (which he recalls as December of last year) and the resulting wave of companies building similar systems. He describes the standard configuration as a sandbox holding the code, an AI agent (e.g. Claude Code or open source), and a query that generates a PR which you merge (Cooke, WorkOS).

WorkOS deliberately took a slightly different approach, driven by skepticism about the popular success metrics. Cooke argues that measures like PR percentage, number of PRs, or how much AI-generated code reaches production are outcome measures that can hide how well these systems actually work — it is hard to distinguish whether the outcome leads to the results, since a rise in PRs could have other causes (Cooke, WorkOS). Instead, WorkOS measures whether the factory accelerates their ability to deliver features, because the dream of a software factory is to give each engineer a small team of engineers to themselves, so they build more, deliver more, and build complex features much faster (Cooke, WorkOS).

They began with the same sandbox architecture on top of Cloudflare with an open source router passing prompts to Claude, but quickly found it was not yielding more results — the increase was neither gradual nor exponential, and was "pretty indistinguishable" from engineers running Claude Code on their laptops (Cooke, WorkOS). This led them to embed their engineering processes into the factory itself, dividing it into two systems: TARS, which is how users interact with the coding agent and is built into the tools they already use — Slack, Linear, and GitHub — subscribing to webhooks so it can track project progress in addition to generating code; and Horizon, an infrastructure orchestration layer similar to inspections or minions, positioned in front of an MCP gateway that Cooke calls truly transformational (Cooke, WorkOS).

By routing actions from source control and project tracking systems through webhooks, WorkOS aims for autonomy where the factory does the work of developing the product, not just working with the code. His example: Linear tickets with dependencies, where TARS receives a webhook when a ticket completes and automatically picks up the next ticket, following a plan the team constructed and executing it autonomously; between steps, TARS can be asked to re-evaluate the Linear project and surface missing tickets so the plan stays fresh as gaps are discovered (Cooke, WorkOS).

- Popular software-factory metrics (PR count, PR percentage, AI-generated code in production) are output measures that can conceal whether the system actually works; WorkOS measures feature-delivery acceleration instead.
- A sandbox + agent + auto-generated PR setup on Cloudflare with Claude provided no distinguishable gain over engineers running Claude Code on their own laptops.
- WorkOS split its factory into TARS (agent interaction embedded in Slack, Linear, GitHub with webhook-driven project tracking) and Horizon (infrastructure orchestration in front of an MCP gateway).
- Webhook-driven autonomy lets the factory follow a plan: completing a Linear ticket triggers the next dependent ticket, and the agent can re-evaluate the project to find missing tickets.