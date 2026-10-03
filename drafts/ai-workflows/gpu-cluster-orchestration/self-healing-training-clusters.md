---
domain: ai-workflows
subdomain: gpu-cluster-orchestration
concept: self-healing-training-clusters
title: GPU Died. Training Didn't: Self-Healing Training at Scale
sources:
  - title: "GPU Died. Training Didn't: Self-Healing Training at Scale — Crusoe"
    url: "https://www.youtube.com/watch?v=bRGyYaE0lxI"
    author: "Connor, Nikhil, Yang (Crusoe)"
    date: "2026-10-03"
---

# GPU Died. Training Didn't: Self-Healing Training at Scale

At Crusoe, hyperscale training workloads run on thousands of GPUs, which makes GPU failures inevitable and manual troubleshooting completely unviable (Crusoe, "GPU Died. Training Didn't"). Crusoe Cloud provides infrastructure as a service — compute, storage, networking, and the latest Nvidia and AMD GPUs — and on top of it Crusoe built a managed Kubernetes service (CMK) plus a managed Slurm service built on CMK and Slinky, SchedMD's official open-source project for running Slurm on Kubernetes.

The architecture pairs Slurm's highly efficient task scheduling with Kubernetes' infrastructure resilience and observability, including a system Crusoe calls "autoclusters" that automatically detects and replaces nodes with failing GPUs when a failure is detected.

Traditional Slurm was created 20+ years ago by researchers for universities and labs, built for high-performance computing — a good fit for modern AI training, which needs tight collective connectivity between ranks, a purpose-built network, topology awareness, and prologues/epilogues for cluster validation, all driven by familiar sbatch and srun commands. Its shortcomings for modern AI are dynamic workloads: training is only one part of what AI labs do, alongside post-training, evaluation, and inference, some of which may not even run on the Slurm cluster. Slurm's traditional partitioning is static, and GPU power limitations constrain how dynamically resources can be used.

Operationally, health checking and maintenance add burden: you must identify faulty nodes, take them out of service, and work around them, whether manually or via automation. Slurm can requeue tasks and detect failed nodes using prologues and open-source tools, but observability is limited — Slurm knows a task failed but can't necessarily explain why, and network outages or switch problems can also cause degraded or lost performance.

- At thousands-of-GPU scale, GPU failures are inevitable and manual troubleshooting is unviable, motivating automated error correction.
- Crusoe's managed Slurm runs on its managed Kubernetes (CMK) via Slinky (SchedMD's open-source Slurm-on-Kubernetes project), combining Slurm task scheduling with Kubernetes resilience and observability.
- "Autoclusters" automatically detect and replace nodes with failing GPUs when failures occur.
- Traditional Slurm suits multi-node training (collective connectivity, topology awareness, cluster-validation prologues/epilogues) but is static in partitioning and lacks rich failure observability.