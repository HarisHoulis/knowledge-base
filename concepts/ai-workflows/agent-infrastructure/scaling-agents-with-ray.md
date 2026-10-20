---
domain: ai-workflows
subdomain: agent-infrastructure
concept: scaling-agents-with-ray
title: Beyond the Prototype: Scaling Framework-Agnostic AI Agent Infrastructure with Ray
sources:
  - title: "Presentation: Beyond the Prototype: Scaling Framework Agnostic AI Agent Infrastructure with Ray"
    url: "https://www.infoq.com/presentations/scale-llm-agents-production-ray/"
    author: "Deepak Mohanakumar Chandramouli, Bhumik Vinodkumar Thakkar"
    date: "2026-10-20"
---

# Beyond the Prototype: Scaling Framework-Agnostic AI Agent Infrastructure with Ray

This presentation by Deepak Mohanakumar Chandramouli and Bhumik Vinodkumar Thakkar describes moving AI agents from local FastAPI prototypes to resilient production systems on Kubernetes using Ray. The approach is framework-agnostic, so the infrastructure does not depend on a particular agent framework.

The speakers cover RayCluster topology, stateful memory handling, auto-scaling under dynamic traffic, and robust control plane designs. They also emphasize critical guardrails and multi-region setups for production resilience.

Evaluation is treated as part of the infrastructure: the talk highlights LLM-as-a-judge evaluation pipelines for assessing agent behavior. The overall focus is on operational insights gained from running agents in production rather than on prototype-level demos.

- Move agents from local FastAPI prototypes to production on Kubernetes using Ray
- Design RayCluster topology, stateful memory handling, and auto-scaling for dynamic traffic
- Build robust control planes with guardrails and multi-region setups
- Use LLM-as-a-judge evaluation pipelines to assess agents in production
- Keep the infrastructure framework-agnostic rather than tied to one agent framework