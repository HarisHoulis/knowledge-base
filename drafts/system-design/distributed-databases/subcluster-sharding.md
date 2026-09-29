---
domain: system-design
subdomain: distributed-databases
concept: subcluster-sharding
title: Uber Redesigns M3DB Sharding with Subclusters to Limit Failure Impact
sources:
  - title: "Uber Redesigns M3DB Sharding with Subclusters to Limit Failure Impact"
    url: "https://www.infoq.com/news/2026/09/uber-m3db-subcluster-sharding/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "2026-09-21"
---

# Uber Redesigns M3DB Sharding with Subclusters to Limit Failure Impact

Uber redesigned shard placement in M3DB using fixed-size subclusters to limit the impact of node failures, maintenance, and cluster scaling (Kumili, 2026). The approach bounds shard dependencies and preserves replica isolation, according to the report.

The redesign relies on a greedy algorithm to select shard migrations, avoiding a separate rebalancing pass and unnecessary data movement (Kumili, 2026).

- Uber redesigned M3DB shard placement with fixed-size subclusters.
- The design bounds shard dependencies and preserves replica isolation.
- A greedy algorithm selects shard migrations without a separate rebalancing pass.
- The changes aim to limit the impact of node failures, maintenance, and cluster scaling.