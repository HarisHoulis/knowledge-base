---
domain: system-design
subdomain: multi-tenant-isolation
concept: four-layer-tenant-isolation
title: ReadyOn Builds Four-Layer Tenant Isolation for Multi-Tenant Amazon EKS
sources:
  - title: "Readyon Builds Four Layer Tenant Isolation for Multi Tenant Amazon EKS"
    url: "https://www.infoq.com/news/2026/10/readyon-four-layer-isolation/"
    author: "Leela Kumili"
    date: "2026-10-26"
---

# ReadyOn Builds Four-Layer Tenant Isolation for Multi-Tenant Amazon EKS

ReadyOn has published details of a four-layer tenant isolation architecture for its Harmony platform running on Amazon EKS. The design stacks Kubernetes namespaces, dedicated Karpenter node pools, VPC security groups, and per-tenant Aurora databases to separate tenants at multiple levels rather than relying on a single boundary (InfoQ).

The controls were evaluated against a 10-stage multi-tenant threat model that focuses specifically on cross-tenant access and lateral movement, meaning the layering is intended to contain a breach at one layer from spreading to others. By combining workload-level (namespaces), infrastructure-level (node pools), network-level (security groups), and data-level (per-tenant databases) isolation, ReadyOn targets defense in depth for multi-tenant SaaS on EKS.

- Four isolation layers: Kubernetes namespaces, dedicated Karpenter node pools, VPC security groups, and per-tenant Aurora databases
- Design validated against a 10-stage multi-tenant threat model centered on cross-tenant access and lateral movement
- Layered approach provides defense in depth rather than relying on a single tenant boundary