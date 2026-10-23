---
domain: system-design
subdomain: serverless-architecture
concept: serverless-genomic-query
title: CSIRO Serverless Beacon: Querying Genomic Variants Without Central Databases
sources:
  - title: "CSIRO Uses Serverless Architecture to Query 100x More Genomic Variants on AWS"
    url: "https://www.infoq.com/news/2026/10/csiro-serverless-genomic-variant/"
    author: "Leela Kumili"
    date: "2026-10-23"
---

# CSIRO Serverless Beacon: Querying Genomic Variants Without Central Databases

CSIRO built Serverless Beacon, a serverless architecture for querying genomic variants that avoids copying VCF files into a central database. The system combines Amazon S3, Lambda, Athena, and DynamoDB, relying on metadata indexes and HTTP byte range requests to query compressed genomic regions directly (InfoQ, Leela Kumili).

The approach reportedly enables querying 100x more genomic variants, with tests showing 1.52 second average latency for 10,000 base pair queries. By querying compressed regions in place rather than ingesting data into a database, the design sidesteps the cost and duplication of centralized storage.

- Serverless Beacon queries genomic variants without copying VCF files into a central database
- Architecture uses Amazon S3, Lambda, Athena, and DynamoDB
- Metadata indexes plus HTTP byte range requests enable querying compressed genomic regions
- Reported 1.52 second average latency for 10,000 base pair queries