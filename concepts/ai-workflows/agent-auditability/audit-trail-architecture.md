---
domain: ai-workflows
subdomain: agent-auditability
concept: audit-trail-architecture
title: Why Your Enterprise Tech Stack Isn’t Ready for AI Agents
sources:
  - title: "Why Your Enterprise Tech Stack Isn’t Ready for AI Agents"
    url: "https://www.youtube.com/watch?v=mav15aW9lLM"
    author: "Christopher Lovejoy & Saul Howard"
    date: "2026-08-19"
---

# Why Your Enterprise Tech Stack Isn’t Ready for AI Agents

Christopher Lovejoy and Saul Howard argue that the hardest part of deploying AI agents in regulated industries like healthcare is not model accuracy but satisfying enterprise audit requirements. A proof of concept may hit accuracy, speed, and cost targets, yet fail when compliance asks for an audit trail. They emphasize that an audit trail is not a developer log; it must be a complete, durable record of every agent action, data touchpoint, and authorization, sufficient to stand up as evidence in court. The speakers recommend taking these constraints seriously from the start rather than bolting them onto a working demo. (Lovejoy & Howard, 2026)

Their architecture uses an immutable append-only event log to make auditability inherent to the storage model, accepting the tradeoff of harder reads. Patient data is stored in schema-driven object storage alongside the log rather than inside it, so events contain only references. This separation lets engineers debug agent behavior without exposing sensitive health data, supports zero-trust enforcement, and constrains prompt injection. Escalation is handled by treating humans and models as the same kind of agent, allowing either to take any action the other can. Evaluation then emerges as a byproduct of these primitives, including on production data that never leaves the customer's environment. (Lovejoy & Howard, 2026)

- Enterprise readiness for AI agents requires a true audit trail, not a developer log, with complete records of actions, data access, and authorizations.
- An immutable append-only event log makes auditability a property of the storage system, trading off read complexity for durability and trust.
- Storing sensitive data in separate schema-driven object storage and referencing it from events enables debugging without exposing raw data and supports zero trust.
- Treating humans and models as equivalent agents simplifies escalation and makes evaluation a natural byproduct of the architecture.
- Regulated industries like healthcare exemplify constraints that apply broadly to enterprise AI deployments.