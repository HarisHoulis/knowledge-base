---
domain: ai-workflows
subdomain: enterprise-ai-agents
concept: audit-log-architecture
title: Why Your Enterprise Tech Stack Isn’t Ready for AI Agents
sources:
  - title: "Why Your Enterprise Tech Stack Isn’t Ready for AI Agents"
    url: "https://www.youtube.com/watch?v=mav15aW9lLM"
    author: "Christopher Lovejoy & Saul Howard"
    date: "2026-08-19T18:30:15+00:00"
---

# Why Your Enterprise Tech Stack Isn’t Ready for AI Agents

Proof-of-concept AI agents often succeed on accuracy and speed, but stall when auditors ask for an audit trail. Lovejoy and Howard argue that an audit trail is not a developer log; it must be a complete, court-defensible record of every action, data touchpoint, and authorization. Their solution is to design for constraints first, building immutability into the storage model so auditability emerges naturally, rather than bolting it on later. They pair an append-only event log with schema-driven object storage: events hold only references to patient data, enabling debugging without exposing sensitive health information and providing a natural boundary for zero trust and prompt-injection control. Humans and models are treated as the same kind of agent, so escalation paths and permissions are uniform. Evaluation then becomes a byproduct of these primitives, allowing production-grade evals without moving data outside the customer's environment.

- An audit trail must be a durable, court-defensible chain of evidence, not a developer log.
- Use an immutable append-only event log so auditability is inherent to the storage model, despite harder reads.
- Store sensitive data in schema-driven object storage beside the log, with events containing only references, to enable safe debugging and zero-trust enforcement.
- Treat humans and models as the same kind of agent to simplify escalation and permissioning.
- Design evaluation as a byproduct of the core primitives, including on production data that never leaves the customer environment.