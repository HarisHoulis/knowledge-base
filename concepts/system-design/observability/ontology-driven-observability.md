---
domain: system-design
subdomain: observability
concept: ontology-driven-observability
title: Ontology-Driven Observability: Building the E2E Knowledge Graph at Netflix Scale
sources:
  - title: "Presentation: Ontology‐Driven Observability: Building the E2E Knowledge Graph at Netflix Scale"
    url: "https://www.infoq.com/presentations/netflix-observability-aiops-ontology-scale/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Prasanna Vijayanathan, Renzo Sanchez-Silva"
    date: "2026-10-09"
---

# Ontology-Driven Observability: Building the E2E Knowledge Graph at Netflix Scale

Prasanna Vijayanathan and Renzo Sanchez-Silva describe how Netflix handles observability at a scale of 38M events/sec. Rather than relying on reactive monitoring, they replace it with an AI-driven operational ontology and agentic workflows built on Claude and graph databases. The core idea is to unify MELT telemetry (metrics, events, logs, traces) into queryable knowledge graphs, which enables automated triaging, root-cause analysis, and self-healing systems.

- Netflix processes 38M observability events per second, motivating a shift away from reactive monitoring.
- An AI-driven operational ontology plus agentic workflows (using Claude and graph databases) replaces traditional monitoring.
- Unifying MELT telemetry into queryable knowledge graphs enables automated triaging, root-cause analysis, and self-healing.