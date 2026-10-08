---
domain: system-design
subdomain: database-migration
concept: wide-column-to-aerospike-migration
title: Grab Redesigns Counter Service Storage for 50% Lower P99 Latency
sources:
  - title: "Grab Redesigns Counter Service Storage for 50% Lower P99 Latency"
    url: "https://www.infoq.com/news/2026/10/grab-counter-aerospike-migration/"
    author: "Leela Kumili"
    date: "2026-10-07"
---

# Grab Redesigns Counter Service Storage for 50% Lower P99 Latency

Grab migrated its high-volume Counter Service from a wide column database to Aerospike, following a structured migration approach that included storage abstraction, shadow traffic, data parity validation, and gradual traffic migration. The redesign consolidated time buckets into map-based records rather than the previous wide-column layout.

The migration delivered measurable production improvements: roughly 50% lower p99 read latency, disk usage reduced from 3 TB to 1 TB, and 45% to 50% lower cost per node. The combination of a storage abstraction layer and shadow traffic allowed Grab to validate the new data model and Aerospike behavior against production workloads before cutting over.

Data parity validation and gradual traffic migration were used to de-risk the switch, ensuring the new store produced equivalent results before full traffic was moved. The results show that a redesigned data model plus a purpose-built key-value store can substantially cut latency, storage footprint, and per-node cost for high-volume counter workloads.

- Grab migrated its Counter Service from a wide column database to Aerospike using storage abstraction, shadow traffic, data parity validation, and gradual traffic migration.
- The redesigned data model consolidated time buckets into map-based records.
- Production results include about 50% lower p99 read latency, disk usage down from 3 TB to 1 TB, and 45% to 50% lower cost per node.