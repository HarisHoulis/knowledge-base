---
domain: system-design
subdomain: confidential-computing
concept: attestation-based-key-release
title: Kubernetes Confidential Containers Get Fortanix Attestation and Key Management
sources:
  - title: "Kubernetes Confidential Containers Get Fortanix Attestation and Key Management"
    url: "https://www.infoq.com/news/2026/10/k8s-confidential-containers/"
    author: "Mark Silvester"
    date: "2026-10-31"
---

# Kubernetes Confidential Containers Get Fortanix Attestation and Key Management

Fortanix has integrated its key management with Kubernetes Confidential Containers (CoCo), tying workload attestation to the release of decryption keys for AI workloads running on the platform. The approach ensures keys are only released once a workload's attestation is verified, rather than relying on static secrets provisioning.

GPU-verification settings are a key variable: how GPU attestation is configured directly affects the level of protection the integration provides. The article notes that Fortanix's offering is not the only path—upstream Trustee and Azure Secure Key Release provide alternative routes to attestation-based key release for teams building confidential AI workloads on Kubernetes.

- Fortanix's CoCo integration links workload attestation to decryption-key release for Kubernetes AI workloads.
- GPU-verification configuration affects the actual protection level delivered.
- Upstream Trustee and Azure Secure Key Release are alternative approaches to attestation-based key release.