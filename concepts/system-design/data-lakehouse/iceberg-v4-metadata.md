---
domain: system-design
subdomain: data-lakehouse
concept: iceberg-v4-metadata
title: Apache Iceberg V4: Redesigning Table Metadata for Scale
sources:
  - title: "QCon San Francisco 2026: The Future of Apache Iceberg"
    url: "https://www.infoq.com/news/2026/11/iceberg-v4-metadata/"
    author: "Renato Losio"
    date: "2026-11-20"
---

# Apache Iceberg V4: Redesigning Table Metadata for Scale

At QCon San Francisco, Daniel Weeks, co-creator of Apache Iceberg and a member of technical staff at Databricks, presented the fourth version of the Iceberg open table format specification. The V4 proposal centers on a redesign of table metadata aimed at improving scalability and supporting more frequent writes, while also adding new capabilities for data management and schema evolution (InfoQ).

The talk frames V4 as an evolution of the open table format specification rather than a new product, with metadata architecture as the primary lever for handling higher write throughput and larger tables. Alongside the metadata redesign, the session covers new features for managing data and evolving schemas (InfoQ).

- Iceberg V4 proposes a redesign of table metadata to improve scalability and support more frequent writes
- The specification also adds new capabilities for data management and schema evolution
- Presented by Daniel Weeks, Iceberg co-creator and Databricks staff member, at QCon San Francisco