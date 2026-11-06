---
domain: ai-workflows
subdomain: agent-security
concept: zero-trust-agents
title: Zero Trust Agent Systems that Pass Audits and Still Ship
sources:
  - title: "Presentation: Zero Trust Agent Systems that Pass Audits and Still Ship"
    url: "https://www.infoq.com/presentations/zero-trust-ai-agents-production-security/"
    author: "Advait Patel"
    date: "2026-11-05"
---

# Zero Trust Agent Systems that Pass Audits and Still Ship

Advait Patel presents a playbook for securing AI agent systems in production while keeping deployment fast and compliant. The core architectural move is relocating defense boundaries from the prompt to the tool layer, so that security does not depend on the model behaving as instructed.

Patel recommends enforcing scoped workload identities for agents, giving each agent only the permissions its tools require. He also addresses prompt injection arriving through tool outputs, treating tool results as untrusted input that must be mitigated rather than trusted.

To satisfy auditors without slowing delivery, the talk covers structuring audit-ready observability and implementing kill switches that protect critical data when an agent misbehaves.

- Move defense boundaries from the prompt to the tool layer instead of relying on prompt-level guardrails
- Enforce scoped workload identities so agents only hold the permissions their tools need
- Treat tool outputs as an injection vector and mitigate prompt injection arriving through them
- Structure observability to be audit-ready and add kill switches to protect critical data while shipping fast