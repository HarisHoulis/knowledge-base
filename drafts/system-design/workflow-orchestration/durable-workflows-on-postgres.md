---
domain: system-design
subdomain: workflow-orchestration
concept: durable-workflows-on-postgres
title: Implementing Durable Workflows on Postgres Without an External Orchestrator
sources:
  - title: "Implementing Durable Workflows on Postgres Without an External Orchestrator"
    url: "https://www.infoq.com/articles/durable-workflows-postgres/"
    author: "Raman Varma"
    date: "2026-09-14"
---

# Implementing Durable Workflows on Postgres Without an External Orchestrator

Postgres can serve as the durable state store and coordination layer for workflows, eliminating the need for an external orchestrator (InfoQ, 2026). The approach relies on database primitives such as SKIP LOCKED for concurrent work processing, primary-key checkpoints for idempotency, and leases for crash recovery.

Long-running workflow elements like sleeps and human approvals can also be persisted as database state, so they survive restarts. This keeps workflow durability and coordination inside Postgres instead of spreading them across separate infrastructure.

- Postgres can act as the durable state store and coordination layer for workflows, removing the need for an external orchestrator.
- SKIP LOCKED enables concurrent processing of workflow work items.
- Primary-key checkpoints enforce idempotency.
- Leases support crash recovery.
- Workflow sleeps and human approvals can be persisted as database state and survive restarts.