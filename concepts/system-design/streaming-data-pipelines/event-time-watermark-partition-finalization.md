---
domain: system-design
subdomain: streaming-data-pipelines
concept: event-time-watermark-partition-finalization
title: Pinterest Uses Event Time Watermarks to Finalize Petabyte Scale Data Partitions
sources:
  - title: "Pinterest Uses Event Time Watermarks to Finalize Petabyte Scale Data Partitions"
    url: "https://www.infoq.com/news/2026/10/pinterest-event-time-partition/"
    author: "Leela Kumili"
    date: "2026-10-19"
---

# Pinterest Uses Event Time Watermarks to Finalize Petabyte Scale Data Partitions

Pinterest introduced event time-based partition finalization for its database ingestion framework, addressing the problem of determining when continuously ingested CDC data is complete enough for downstream processing. The mechanism uses Apache Flink to track event time and Apache Iceberg metadata to publish a non-regressing watermark, so downstream jobs can decide when a partition is sufficiently complete.

The approach targets petabyte-scale data partitions and relies on event time rather than processing time, which lets consumers reason about data completeness independently of ingestion lag. By publishing the watermark through Iceberg metadata, the framework exposes a durable, shared signal that downstream jobs can consult instead of guessing at partition readiness.

- Event time-based partition finalization lets downstream jobs know when CDC data is sufficiently complete
- Apache Flink tracks event time while Apache Iceberg metadata publishes a non-regressing watermark
- The mechanism operates at petabyte scale for continuously ingested database data