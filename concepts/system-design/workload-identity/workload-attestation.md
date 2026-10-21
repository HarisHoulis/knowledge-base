---
domain: system-design
subdomain: workload-identity
concept: workload-attestation
title: Netflix Bridges AWS IAM and Internal Identity with Workload Attestation
sources:
  - title: "Netflix Bridges AWS IAM and Internal Identity with Workload Attestation"
    url: "https://www.infoq.com/news/2026/10/netflix-workload-attestation-aws/"
    author: "Leela Kumili"
    date: "2026-10-21"
---

# Netflix Bridges AWS IAM and Internal Identity with Workload Attestation

Netflix built a workload attestation mechanism for Apache Spark jobs on Amazon EMR that lets managed compute workloads authenticate to internal services without directly injecting credentials. The design combines AWS IAM identity with signed claims from Netflix's control plane before issuing short-lived internal X.509 certificates.

The approach bridges two identity systems: AWS IAM, which establishes the workload's cloud identity, and Netflix's internal control plane, which vouches for the workload via signed claims. Only after both signals are validated does the system mint short-lived X.509 certificates for internal service authentication.

By relying on attestation and ephemeral certificates rather than embedded secrets, the mechanism reduces the exposure of long-lived credentials in managed compute environments.

- Workloads on EMR are attested using AWS IAM identity plus signed claims from Netflix's control plane
- Successful attestation yields short-lived internal X.509 certificates
- Avoids directly injecting credentials into managed compute workloads
- Bridges cloud IAM identity with internal service identity