---
domain: ai-workflows
subdomain: agent-tooling
concept: agent-guardrails
title: Google's Data Agent Kit Hits GA, Splitting Agent Guardrails Between Skills and IAM
sources:
  - title: "Google's Data Agent Kit Hits GA, Splitting Agent Guardrails Between Skills and IAM"
    url: "https://www.infoq.com/news/2026/10/data-agent-kit-ga/"
    author: "Steef-Jan Wiggers"
    date: "2026-10-24"
---

# Google's Data Agent Kit Hits GA, Splitting Agent Guardrails Between Skills and IAM

Google has released Data Agent Kit as generally available: a free set of MCP tools plus 37 open-source skills that connect coding agents to more than fifteen Google Data Cloud services (InfoQ, Steef-Jan Wiggers, 2026-10-24). The kit's central design concern is guardrails, and it ships two distinct kinds that practitioners must not conflate.

The first guardrail is a skill that asks the agent to stop — a soft, prompt-level instruction. The second is an IAM deny policy that refuses the call outright — a hard, infrastructure-level enforcement. The article's framing makes clear that the distinction matters: one relies on the agent's compliance, the other does not.

- Data Agent Kit is GA and free, offering MCP tools and 37 open-source skills for 15+ Google Data Cloud services.
- Two guardrail types ship with it: skill-based stop instructions and IAM deny policies.
- Skill guardrails are advisory (the agent is asked to stop); IAM deny policies hard-refuse the call.
- Practitioners need to distinguish the two when designing agent safety.