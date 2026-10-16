---
domain: system-design
subdomain: service-mesh-dependency-analysis
concept: automated-dependency-analysis
title: Uber Automates Dependency Analysis Across Its Service Mesh
sources:
  - title: "Uber Automates Dependency Analysis Across Its Service Mesh"
    url: "https://www.infoq.com/news/2026/10/uber-automated-dependency/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "2026-10-16"
---

# Uber Automates Dependency Analysis Across Its Service Mesh

Uber has developed an automated dependency analysis system that uses RPC middleware and production metrics to correlate caller and downstream failures, according to Leela Kumili's InfoQ report. The system classifies dependencies as fail-close, fail-open, or unknown, giving teams a clearer picture of how failures propagate through the mesh.

The approach is positioned as a response to the limitations of sampled distributed tracing, which can miss rare failures that occur across Uber's large service mesh. By relying on RPC middleware and production metrics rather than trace sampling alone, the system aims to capture dependency behavior more reliably at scale.

The classification of dependencies into fail-close, fail-open, or unknown categories helps teams reason about the blast radius of downstream failures and make informed decisions about resilience and fallback behavior.

- Uber built an automated dependency analysis system using RPC middleware and production metrics to correlate caller and downstream failures.
- Dependencies are classified as fail-close, fail-open, or unknown.
- The system addresses limitations of sampled distributed tracing for detecting rare failures across a large service mesh.