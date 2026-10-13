---
domain: system-design
subdomain: resilience-and-disaster-recovery
concept: disaster-recovery-rpo-rto
title: Building Resilient AI-Powered Software: Disaster Recovery, RPO/RTO, and AI-Specific Resilience
sources:
  - title: "Building resilient AI-powered software, and planning for when things go wrong"
    url: "https://newsletter.pragmaticengineer.com/p/building-resilient-systems"
    author: "Gergely Orosz"
    date: "2026-10-13"
---

# Building Resilient AI-Powered Software: Disaster Recovery, RPO/RTO, and AI-Specific Resilience

Sam Newman's book Building Resilient Distributed Systems addresses a timely problem: outages are increasing as AI agents write more code, leading to more deploys and more production incidents. Newman spent three years finishing the book, reworking sections to address how AI changes resilient system design. The excerpt covers disaster recovery (DR) planning, DR patterns, infrastructure availability constraints, and the resilience challenges specific to AI-powered software.

DR planning centers on two measurable targets: the recovery point objective (RPO), the maximum acceptable data loss measured as time since the last backup or sync, and the recovery time objective (RTO), how long the system may be unavailable after an incident. Reducing either increases cost and complexity dramatically, and zero RPO or RTO is technically impossible. Different workloads warrant different targets — a bank needs low RPO/RTO for payments but can tolerate higher targets for new-account signup — so targets should be negotiated with stakeholders against end-user needs, regulatory requirements, and implementation cost, and should exceed any SLA commitments. RPO and RTO fit poorly as SLOs because disasters are too rare to gather useful service level indicators; related SLOs like data replication speed are only tangential proxies.

Newman describes four DR patterns of increasing complexity and improving RPO/RTO: backup-and-restore (periodic backups to a separate site, infrastructure provisioned on failover, longest RTO), pilot light (continuous data replication to a failover site with infrastructure provisioned only on failover, keeping costs down), warm failover, and multisite active-active. All require some form of traffic rerouting, and most require cross-site data replication. Patterns can be layered incrementally, and mixed approaches make sense when different parts of a system have different RPO/RTO targets. Backup-and-restore is straightforward but its RTO depends on restore time, data volume, automation level, and crucially the availability of replacement computing resources — which can stretch to weeks if equipment must be purchased.

AI-specific resilience concerns include model provider resilience, the challenge of models changing underneath you, and the need for observability. Newman recommends handling uncertainty through tactics like being multi-model and multi-vendor, making costs transparent, and frequently analyzing vendors. Ongoing GPU and CPU shortages mean infrastructure availability cannot be assumed, so teams must understand their vendors' constraints and prioritize critical services.

- RPO defines maximum acceptable data loss (time since last backup/sync); RTO defines acceptable downtime after an incident — both increase cost and complexity as they shrink, and zero is impossible.
- RPO/RTO targets should be negotiated per workload with stakeholders against user needs, regulation, and cost, and should exceed SLA commitments; they fit poorly as SLOs because disasters are too rare for useful SLIs.
- Four DR patterns increase in complexity and improve RPO/RTO: backup-and-restore, pilot light, warm failover, and multisite active-active; all need traffic rerouting and most need cross-site data replication.
- Backup-and-restore RTO depends on restore time, data volume, automation, and availability of replacement infrastructure — potentially weeks if new equipment must be purchased.
- AI-powered software adds resilience concerns: model provider resilience, models changing, observability, and uncertainty tactics like multi-model/multi-vendor, transparent costs, and frequent vendor analysis.