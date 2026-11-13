---
domain: system-design
subdomain: architecture-coupling
concept: hidden-coupling
title: Top Types of Hidden Coupling and How to Deal With Them
sources:
  - title: "Top Types of Hidden Coupling and How to Deal With Them"
    url: "https://blog.bytebytego.com/p/top-types-of-hidden-coupling-and"
    author: "ByteByteGo"
    date: "2026-11-12"
---

# Top Types of Hidden Coupling and How to Deal With Them

Architecture diagrams show services, databases, and queues, but they cannot capture every dependency a component has. ByteByteGo argues that these invisible dependencies are "hidden coupling" and that, while coupling cannot be eliminated, developers should keep it clear, limited, and stable so ordinary changes don't create a large impact footprint. The article frames coupling along several dimensions: whether components must run together, share interpretations of data, change together, deploy together, or recover together.

The piece catalogs concrete forms of coupling. Temporal coupling occurs when one component's work depends on when another runs or responds—e.g., an account service blocking registration on a slow email service, or an export/import schedule that silently assumes a 5-minute window. Mitigations include durable messages, the transactional outbox pattern, and explicit readiness signals instead of timing assumptions. Semantic coupling arises when components assign different meanings to the same field (e.g., "available_quantity") or duplicate the same business rule; bounded contexts, precise naming, clear rule ownership, and anti-corruption layers help.

Deployment coupling means changes require coordinated releases; the expand-migrate-contract pattern breaks incompatible interface changes into steps. Shared schemas and shared libraries spread decisions beyond their owner—addressed via stable APIs, consumer-owned read models, and versioned, narrowly scoped libraries. Observability coupling makes monitoring part of the dependency chain, both at runtime (synchronous logging, unbounded buffering) and operationally (alerts keyed to log text or metric names). Finally, shared incidents arise when components share a failure domain—common clusters, networks, DNS, or databases—even without direct communication.

- Hidden coupling spans temporal, semantic, deployment, schema/library, observability, and shared-failure dimensions; aim to keep it clear, limited, and stable rather than eliminate it.
- Replace timing assumptions with durable messages, transactional outbox, and explicit completion signals to reduce temporal coupling.
- Use bounded contexts, precise field names, single ownership of business rules, and anti-corruption layers to combat semantic coupling.
- Adopt expand-migrate-contract for interface changes, and prefer stable APIs or consumer-owned read models over direct shared-schema access.
- Bound telemetry resource usage with failure isolation, and track which log fields and metric names operational tools depend on.