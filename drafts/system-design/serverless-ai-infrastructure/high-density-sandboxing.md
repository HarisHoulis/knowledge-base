---
domain: system-design
subdomain: serverless-ai-infrastructure
concept: high-density-sandboxing
title: Presentation: Fixing the AI Infra Scale Problem by Stuffing 1M Sandboxes in a Single Server
sources:
  - title: "Presentation: Fixing the AI Infra Scale Problem by Stuffing 1M Sandboxes in a Single Server"
    url: "https://www.infoq.com/presentations/unikraft-microvm-sandboxes-cloud-scaling/"
    author: "Felipe Huici"
    date: "2026-09-09"
---

# Presentation: Fixing the AI Infra Scale Problem by Stuffing 1M Sandboxes in a Single Server

Felipe Huici's presentation introduces Unikraft as a solution for scaling AI workloads by packing up to one million sandboxes onto a single server. The approach centers on achieving millisecond cold boots and stateful scale-to-zero, allowing infrastructure to remain highly responsive while minimizing idle resource usage. Unikraft also claims extreme density, directly addressing the AI infrastructure scale problem by maximizing the number of isolated execution environments per physical machine.

The talk covers technical mechanisms including isolation primitives, Linux kernel optimizations, and snapshotting tricks to maintain sub-10ms performance at scale. These optimizations allow Unikraft to integrate seamlessly into Kubernetes environments while providing hardware-level security for sandboxed workloads. The presentation thereby demonstrates a path toward high-performance, secure, and dense sandboxing for AI applications.

- Unikraft enables up to 1 million sandboxes in a single server, providing extreme density for AI workloads.
- Millisecond cold boots and stateful scale-to-zero reduce latency and resource waste.
- Isolation primitives, Linux kernel optimizations, and snapshotting tricks are used to sustain sub-10ms performance at scale.
- Solutions integrate seamlessly with Kubernetes while maintaining hardware-level security.