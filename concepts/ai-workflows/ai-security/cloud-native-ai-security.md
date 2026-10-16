---
domain: ai-workflows
subdomain: ai-security
concept: cloud-native-ai-security
title: Exploding GPUs: Securing AI Workloads on Kubernetes
sources:
  - title: "Presentation: Exploding GPUs"
    url: "https://www.infoq.com/presentations/ai-security-kubernetes-gpu-threats/"
    author: "Andrew Martin"
    date: "2026-10-16"
---

# Exploding GPUs: Securing AI Workloads on Kubernetes

Andrew Martin argues that AI security is fundamentally tied to Kubernetes security, since AI workloads in production are typically deployed on cloud-native infrastructure. He frames the threat landscape as evolving and distinct from traditional application security.

The talk covers four main areas of risk: non-deterministic agent behavior, GPU supply chain vulnerabilities, shared compute risks, and the need for practical defense strategies. Because AI agents behave unpredictably, conventional security assumptions break down, and the GPU hardware and software supply chain introduces new attack surface.

Shared compute environments create additional exposure, as workloads may not be fully isolated from one another. Martin proposes defenses including prompt firewalling and agentic identity as ways to secure cloud-native AI workloads in production.

- AI security is fundamentally tied to Kubernetes security in cloud-native production environments.
- Non-deterministic agent behavior undermines traditional security assumptions.
- GPU supply chain vulnerabilities and shared compute risks expand the attack surface.
- Proposed defenses include prompt firewalling and agentic identity.