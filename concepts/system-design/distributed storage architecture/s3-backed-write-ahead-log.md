---
domain: system-design
subdomain: distributed storage architecture
concept: s3-backed-write-ahead-log
title: Cursor Continuity: S3 WAL for Git Storage at 300+ Pushes per Second
sources:
  - title: "Cursor Uses S3 WAL to Scale Git Storage to More than 300 Pushes per Second"
    url: "https://www.infoq.com/news/2026/09/cursor-continuity-git-storage/"
    author: "Leela Kumili"
    date: "2026-09-30"
---

# Cursor Continuity: S3 WAL for Git Storage at 300+ Pushes per Second

Cursor introduced Continuity, a Git storage architecture that uses an S3-backed write-ahead log (WAL) as the source of truth, according to Leela Kumili's InfoQ report [1]. Rather than treating local disk as authoritative, the design relegates local NVMe repositories to the role of warm caches, with the S3-backed log providing durability and consistency [1].

The architecture explicitly separates replica coordination from consistency, decoupling these concerns so that replication and data integrity are handled independently [1]. Cursor reports that this yields linear read scaling with up to 100 replicas [1].

On the write path, Cursor reports more than 300 pushes per second when running against S3 Express One Zone in synthetic tests [1]. Note that these figures come from synthetic testing rather than production workloads.

- Continuity uses an S3-backed write-ahead log as the source of truth for Git storage [1]
- Local NVMe repositories are demoted to warm caches rather than authoritative storage [1]
- The design separates replica coordination from consistency [1]
- Cursor reports linear read scaling up to 100 replicas [1]
- Cursor reports 300+ pushes per second with S3 Express One Zone in synthetic tests [1]