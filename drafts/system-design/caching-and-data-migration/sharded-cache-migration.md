---
domain: system-design
subdomain: caching-and-data-migration
concept: sharded-cache-migration
title: Agoda Migrates a 1.5 TB Price Cache from 72 SQL Server Shards to DragonflyDB
sources:
  - title: "Agoda Replaces 72-Shard SQL Server Price Cache with DragonflyDB"
    url: "https://www.infoq.com/news/2026/09/agoda-price-cache-dragonflydb/"
    author: "Leela Kumili"
    date: "2026-09-14"
---

# Agoda Migrates a 1.5 TB Price Cache from 72 SQL Server Shards to DragonflyDB

Agoda migrated its 1.5 TB hotel Price Cache off 72 SQL Server shards onto DragonflyDB in order to handle growing read and write volumes (Kumili, InfoQ). The legacy design distributed the cache across dozens of SQL Server shards; the replacement uses a purpose-built in-memory datastore instead.

The migration was staged rather than a hard cutover: it combined dual reads, parity validation, gradual traffic shifting, and decentralized failover detection (Kumili, InfoQ). Dual reads plus parity validation let Agoda compare old and new paths before committing traffic, while gradual shifting limited blast radius during the transition.

Availability is provided by two DragonflyDB clusters. Agoda reports an approximately eightfold reduction in P99 read latency as a result of the move (Kumili, InfoQ).

- The Price Cache held roughly 1.5 TB across 72 SQL Server shards prior to migration.
- Migration used staged dual reads and parity validation to verify the new path before shifting traffic.
- Traffic was moved gradually, and failover detection was decentralized rather than centralized.
- Two DragonflyDB clusters provide high availability.
- Agoda reports approximately an 8x reduction in P99 read latency.