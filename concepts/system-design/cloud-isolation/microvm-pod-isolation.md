---
domain: system-design
subdomain: cloud-isolation
concept: microvm-pod-isolation
title: AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field
sources:
  - title: "AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field"
    url: "https://www.infoq.com/news/2026/11/aws-nitro-sandboxes-eks/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-16"
---

# AWS Nitro Sandboxes Put Each EKS Pod in Its Own MicroVM with One RuntimeClass Field

AWS launched Nitro Sandboxes, which run each opted-in EKS pod, ECS task, or EC2 workload inside its own Firecracker microVM with a separate kernel. Opting in requires only a single runtimeClassName field, and there is no extra charge for the feature (InfoQ).

The offering includes a confidential mode that adds attestation-gated key release, extending isolation guarantees to key material. The documentation explicitly lists trade-offs: no GPU passthrough, a maximum of five sandboxes per vCPU, and half the compute available on SMT instances (InfoQ).

The design trades raw performance and hardware flexibility for stronger workload isolation, making it relevant for multi-tenant or security-sensitive container workloads where kernel-level separation matters more than density or GPU access.

- Each opted-in EKS pod, ECS task, or EC2 workload runs in its own Firecracker microVM with a separate kernel
- Enablement is a single runtimeClassName field, at no extra charge
- A confidential mode adds attestation-gated key release
- Trade-offs: no GPU passthrough, max five sandboxes per vCPU, and half the compute on SMT instances