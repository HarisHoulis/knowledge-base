---
domain: system-design
subdomain: stream-processing-infrastructure
concept: flink-kubernetes-operator-migration
title: Lyft Moves Streaming Fleet to Apache Flink Kubernetes Operator
sources:
  - title: "Lyft Moves Streaming Fleet to Apache Flink Kubernetes Operator"
    url: "https://www.infoq.com/news/2026/09/lyft-flink-k8s-operator/"
    author: "Mark Silvester"
    date: "2026-09-16"
---

# Lyft Moves Streaming Fleet to Apache Flink Kubernetes Operator

Lyft has migrated hundreds of production Flink jobs off its 2020-era in-house Kubernetes operator and onto the Apache Flink Kubernetes Operator [1]. The move covers the company's streaming fleet at scale, rather than a single cluster or pilot deployment [1].

The migration is framed by the capabilities the Apache operator unlocks: last-state upgrades, in-place autoscaling, and resource autotuning across the fleet [1]. These features replace what the older custom operator could not provide, indicating that Lyft's streaming platform now leans on the upstream community operator for lifecycle and resource management [1].

- Lyft migrated hundreds of production Flink jobs from a 2020 in-house Kubernetes operator to the Apache Flink Kubernetes Operator [1].
- The migration unlocks last-state upgrades for streaming jobs [1].
- It also enables in-place autoscaling across the Flink fleet [1].
- Resource autotuning is now available fleet-wide [1].