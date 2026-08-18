---
domain: ai-workflows
subdomain: ml-infrastructure
concept: gpu-cluster-observability
title: Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai
sources:
  - title: "Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai"
    url: "https://www.youtube.com/watch?v=byn9PURoBNY"
    author: "AI Engineer"
    date: "2026-08-18T17:00:05+00:00"
---

# Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai

Gabriel Jorge Menezes, an AI engineer at Krea.ai, discusses the infrastructure behind training Krea 2 from scratch on thousands of GPUs. He argues that standard GPU utilization metrics are misleading—showing 100% while the cluster is underutilized—and instead tracks tensor core utilization, which rose as training resolution increased from 128 to 1024 pixels. He also emphasizes monitoring hardware-level signals like GPU temperature, pulling any GPU above 78 degrees to prevent throttling, and building custom InfiniBand and NVLink metric collection because nothing off-the-shelf exports them. Most failures were cross-node communication issues, often silent, with dashboards staying green while jobs timed out.

- GPU utilization is a lie; tensor core utilization is a truer measure of training efficiency.
- InfiniBand and NVLink metrics are critical but must be built in-house, as most cross-node failures are missed by standard dashboards.
- Any GPU hotter than 78°C is pulled rather than debugged, because one throttling card destabilizes the entire run.
- Crashes at scale are common and often silent; the practical approach is to let them crash and rerun on the same nodes, relying on aggressive checkpointing to a filesystem that can write a terabyte in under 30 seconds.
- Production and training share a cluster with gang scheduling and training priority, evicting inference to external providers via a fake Kubernetes node and migrating back gradually to avoid downtime.